import matplotlib.pyplot as plt

def boxplot(data, title):
    plt.boxplot(data)
    plt.title(title)
    plt.show()
    return

def histogram(data, title, bins=10):
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.show()
    return

def barplot(data,x_ticks, title):
    plt.bar(x_ticks, data)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()
