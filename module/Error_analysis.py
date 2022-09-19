# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def plot_signal_fea(data, label, plot_name="fea_hist"):

    dim_label0 = data[np.array(label) == 0]
    dim_label1 = data[np.array(label) == 1]
    # python 3.6 需要加这个代码
    dim_label0 = dim_label0[plot_name]
    dim_label1 = dim_label1[plot_name]


    plt.figure()

    plt.hist(x=dim_label0,  # 绘图数据
             bins=20,  # 指定直方图的条形数为20个
             edgecolor='w',  # 指定直方图的边框色
             color=['b'],  # 指定直方图的填充色
             label=['OK'],  # 为直方图呈现图例
             density=False,  # 是否将纵轴设置为密度，即频率
             alpha=0.6,  # 透明度
             rwidth=1,  # 直方图宽度百分比：0-1
             stacked=False)  # 当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放

    plt.hist(x=dim_label1,  # 绘图数据
             bins=20,  # 指定直方图的条形数为20个
             edgecolor='w',  # 指定直方图的边框色
             color=['r'],  # 指定直方图的填充色
             label=['NG'],  # 为直方图呈现图例
             density=False,  # 是否将纵轴设置为密度，即频率
             alpha=0.6,  # 透明度
             rwidth=1,  # 直方图宽度百分比：0-1
             stacked=False)  # 当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放

    ax = plt.gca()  # 获取当前子图
    ax.spines['right'].set_color('none')  # 右边框设置无色
    ax.spines['top'].set_color('none')  # 上边框设置无色
    # plt.xlabel("value")
    # plt.ylabel("frequence")
    # 显示图例
    plt.legend()
    plt.title(plot_name)
    plt.savefig(plot_name)



def generate_error(name, output_fea, Model_probability, pre, label):
    """
    name : str list， 文件的完整路径
    output_fea : Dateframe
    pre ： array_like
    label ： array_like
    """
    # name = [x.split("/")[-1] for x in name]
    val = np.concatenate([np.array(Model_probability).reshape(-1, 1),  np.array(pre).reshape(-1, 1), np.array(label).reshape(-1, 1)], axis=1)
    temp = pd.DataFrame(data=val, index=name, columns=["Model_probability", "pre", "label"])

    out_all = pd.concat((output_fea, temp), axis=1)
    if out_all.shape[0] != temp.shape[0] or out_all.shape[0] != output_fea.shape[0]:
        raise f"something wrong with you."

    out_error = out_all[out_all["label"] != out_all["pre"]]
    return out_all, out_error


def plot_fea(data, label, plot_name="PcaFigure"):
    """
    以data，和 label 生成 一个 PCA 的 plot
    @param data: Dataframe， data行数据，data的列fea
    @param label: array_like,
    @return: save a figure named "222.png"
    @param plot_name: str, title of a  plot
    @return:
    """

    # 只有一个fea, 画histogram
    if data.shape[-1] == 1:
        plot_signal_fea(data, label, plot_name)
        return

    colors = ['b', 'r']
    s = [0, 1]
    marker1 = ["^", "o"]

    pca = PCA()
    X_pca = pca.fit_transform(data)
    component_names = [f"PC{i + 1}" for i in range(X_pca.shape[1])]
    X_pca = pd.DataFrame(X_pca, columns=component_names)
    print("Explained variance of Pricincipal Component 1 is:" + str(pca.explained_variance_ratio_[0]))
    PCA_2dim = X_pca[['PC1', 'PC2']]

    PCA_2dim_label0 = PCA_2dim[np.array(label) == 0]
    PCA_2dim_label1 = PCA_2dim[np.array(label) == 1]

    plt.figure()

    for index in range(2):
        if index == 0:
            XOffset = PCA_2dim_label0["PC1"]
            YOffset = PCA_2dim_label0["PC2"]
        elif index == 1:
            XOffset = PCA_2dim_label1["PC1"]
            YOffset = PCA_2dim_label1["PC2"]
        s[index] = plt.scatter(XOffset, YOffset, c=colors[index], cmap='brg', s=50, alpha=1, marker=marker1[index],
                               linewidth=0, zorder=-index)
        #    plt.legend(result[index])

    plt.legend((s[0], s[1]), ('OK', 'NG'), loc='best')
    plt.xlabel("PCA1")
    plt.ylabel("PCA2")
    plt.title('Scatter Plot')
    plt.savefig("222.png")


    # # plt.title(f'{show_fig_name} split_signal')
    # plt.title('Split Signal')
    # plt.plot(range(1, len(x) + 1, 1), x, label='origin sigal')
    #
    # ax.scatter(degredation['cycle'], degredation['PC1'], color='b', s=5)