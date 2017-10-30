# NeuralNetwork.py provide graphing.
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
# Ploting
def plotByList(MyList, xlabel='xlabel', ylabel='ylabel', Title='title', LineTags=[], Xlist=None):
    if Xlist.any() != None:
        plt.plot(Xlist, MyList)
    else:
        plt.plot(MyList)
    plt.title(Title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(LineTags, loc='upper right')
    plt.show(block=False)
