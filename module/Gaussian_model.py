# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

import numpy as np
import pandas as pd
from scipy import stats
# from sklearn.metrics import fbeta_score
# import matplotlib.pyplot as plt

def Confusion_matrix(cv_predictions, label):
    true_positives = sum((cv_predictions == 1) & (label == 1))
    false_positives = sum((cv_predictions == 1) & (label == 0))
    false_negatives = sum((cv_predictions == 0) & (label == 1))
    precision = true_positives / (true_positives + false_positives)  # 0/0 无所谓为nan，可以忽略，最后也不会选这个
    recall = true_positives / (true_positives + false_negatives)
    F1 = 2 * precision * recall / (precision + recall)
    acc = sum((cv_predictions == label) + 0) / label.shape[0]
    # acc_precision_recall_F1 = [acc, precision, recall, F1]
    acc_precision_recall_F1 = np.array([acc, precision, recall, F1])
    return acc_precision_recall_F1


def AnomDet_metrix_select(input_x, label, strategy_metrix, model_fun):
    """
    label 0： 正常
    label 1： 不正常
    模型 < 阈值，代表低概率事件 ； 不正常
    选出阈值，使得异常检测的 对应的 metrix 最佳
    @param input_x: ndarray
    @param label: ndarray
    @param model_fun: function
    @param strategy_metrix: dic
    """

    input_x = np.array(input_x)
    label = np.array(label)

    dir_metrix = {
        #  输入模型的值 and 阈值， 得出给定的指标
        "f1": lambda pval, threshold: [Confusion_matrix((pval < threshold) * 1, label)[3]]
        # 返回 [F1]
        , "recall": lambda pval, threshold: [Confusion_matrix((pval < threshold) * 1, label)[2],
                                             Confusion_matrix((pval < threshold) * 1, label)[1]]
        # 返回 [recall, precision]
        , "precision": lambda pval, threshold: [Confusion_matrix((pval < threshold) * 1, label)[1],
                                                Confusion_matrix((pval < threshold) * 1, label)[2]]
        # 返回 [precision, recall]
        , "accuracy": lambda pval, threshold: [Confusion_matrix((pval < threshold) * 1, label)[0]]
        # 返回 [precision, recall]
    }

    if strategy_metrix not in dir_metrix:
        raise f"{strategy_metrix} are not include in the dir_metrix"

    pval = model_fun(input_x)  # 关于 **kwargs 将 kwargs中的val拿出来, 若是 *kwargs 将 kwargs中的key拿出来
    bestEpsilon = -1  # 阈值
    bestMetrix = None  # 指标

    if strategy_metrix == "recall" or strategy_metrix == "precision":  # 不需要迭代，这个寻找阈值很快
        df_pval_label = pd.DataFrame({"pval": pval, "label": label})
        df_pval_label_sorted = df_pval_label.sort_values(by=["pval"], ascending=False).reset_index(drop=True)
        if strategy_metrix == "recall":
            index = df_pval_label_sorted[(df_pval_label_sorted.label == 1)].index.tolist()[0]
            bestEpsilon = (df_pval_label_sorted["pval"][index] + df_pval_label_sorted["pval"][index-1])/2
            bestMetrix = np.array(dir_metrix[strategy_metrix](pval, bestEpsilon))
            return bestEpsilon, bestMetrix
        else:
            index = df_pval_label_sorted[(df_pval_label_sorted.label == 0)].index.tolist()[-1]
            bestEpsilon = (df_pval_label_sorted["pval"][index] + df_pval_label_sorted["pval"][index+1])/2
            bestMetrix = np.array(dir_metrix[strategy_metrix](pval, bestEpsilon))
            return bestEpsilon, bestMetrix

    for epsilon in np.linspace(max(pval), min(pval), 1001):
        tempMetrix = np.array(dir_metrix[strategy_metrix](pval, epsilon))
        if np.isnan(tempMetrix).any():  # 任何一个为nan，直接考虑下一个阈值
            continue
        if bestMetrix is None:  # 第一次把bestMetrix 赋值为 值-1的shape 和 tempMetrix 一样的和向量
            bestMetrix = np.full_like(tempMetrix, -1)

        for i in range(len(tempMetrix)):
            if tempMetrix[i] < bestMetrix[i]:
                break
            elif tempMetrix[i] == bestMetrix[i]:
                continue
            elif tempMetrix[i] > bestMetrix[i]:
                bestMetrix = tempMetrix
                bestEpsilon = epsilon

    if bestMetrix is None:
        raise f"{bestMetrix} are None"

    return bestEpsilon, bestMetrix


class Gaussian_Model(object):
    """
    先 self.estimateGaussian(x)
    其中x：
    横坐标是 sample num(最高维度)
    纵坐标是 fea num
    """
    # dic_par = None  # 其他一些参数设置在这里，目的为了保存好model需要的参数

    class node_confuse_matrix(object):
        def __init__(self, cv_predictions, label):
            self.confuse_matrix = np.zeros((2, 2))
            true_positives = sum((cv_predictions == 1) & (label == 1))
            false_positives = sum((cv_predictions == 1) & (label == 0))
            false_negatives = sum((cv_predictions == 0) & (label == 1))
            true_negatives = sum((cv_predictions == 0) & (label == 0))
            precision = true_positives / (true_positives + false_positives)
            recall = true_positives / (true_positives + false_negatives)
            F1 = 2 * precision * recall / (precision + recall)
            acc = sum((cv_predictions == label) + 0) / label.shape[0]
            self.acc_precision_recall_F1 = [acc, precision, recall, F1]
            self.confuse_matrix[0][0] = true_positives
            self.confuse_matrix[0][1] = false_positives
            self.confuse_matrix[1][0] = false_negatives
            self.confuse_matrix[1][1] = true_negatives

    def __init__(self):
        self.mu = None  # training set mean
        self.sigma = None  # training set std
        self.Threshold = None  # validation set std
        self.metrix = None  # validation set std

    def estimateGaussian(self, trainX):
        trainX = np.array(trainX)
        m, n = trainX.shape
        self.mu = np.sum(trainX, axis=0) / m
        self.sigma = (np.sum((trainX - self.mu) ** 2, axis=0) / m) ** 0.5

    def Gaussian_pro(self, testX):  # def Gaussian_pro(self, testX, flag_joint_pro=None):
        if testX.ndim != 2:
            raise ValueError("the shape of testX must be (m,n)")

        SubtractWave_text_index_probability = stats.norm(self.mu, self.sigma).pdf(testX)  # 计算累和(假设特征独立)
        out_pro = np.ones_like(SubtractWave_text_index_probability[:, 0])
        for i in range(len(SubtractWave_text_index_probability[0, :])):
            nor_pro = SubtractWave_text_index_probability[:, i]
            out_pro *= nor_pro
        return out_pro

    def SelectThreshold(self, input_x, label, strategy_metrix="F1"):
        bestEpsilon, bestMetrix = AnomDet_metrix_select(input_x, label, strategy_metrix, self.Gaussian_pro)
        self.Threshold, self.metrix = bestEpsilon, bestMetrix
        return bestEpsilon, bestMetrix

    def Gau_prediect(self, testX, label=None, out_pro_flag=False):  # def Gau_prediect(self, testX, label=None, flag_joint_pro=None):
        testX = np.array(testX)
        if testX.ndim != 2:
            raise ValueError("the shape of testX must be (m,n)")
        pro = self.Gaussian_pro(testX)
        outliers = (pro < self.Threshold) + 0

        if label is None:
            return outliers

        label = np.array(label)
        if label.ndim != 1:
            raise ValueError("the shape of label must be (n,)")
        # acc_precision_recall_F1 = self.Confusion_matrix(outliers, label)
        node_confuse_matrix_obj = self.node_confuse_matrix(outliers, label)

        if out_pro_flag:
            return outliers, node_confuse_matrix_obj, pro

        return outliers, node_confuse_matrix_obj
