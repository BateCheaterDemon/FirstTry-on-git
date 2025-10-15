# coding: utf-8
import sys, os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取父目录
parent_dir = os.path.dirname(current_dir)
# 添加父目录到Python路径
sys.path.append(parent_dir)

import numpy as np
import pickle
from common.functions import sigmoid, softmax
from minist import load_mnist
from tqdm import tqdm  # 导入tqdm

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open('/home/qwx/learning/FirstTry-on-git/DeepLearning_Start/Minist/sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'],network['W2'],network['W3']
    b1, b2, b3 = network['b1'],network['b2'],network['b3']

    a1 = x @ W1 + b1
    z1 = sigmoid(a1)
    a2 = z1 @ W2 + b2
    z2 = sigmoid(a2)
    a3 = z2 @ W3 + b3
    y = softmax(a3)

    return y

def single_predict():
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    # 使用tqdm包装range(len(x))，添加进度条
    for i in tqdm(range(len(x)), desc="forecast schedule", unit="sample"):
        y = predict(network=network, x=x[i])
        p = np.argmax(y) # 获得概率最高的元素的索引
        if p == t[i]:
            accuracy_cnt += 1

    print("Accuracy:"+ str(float(accuracy_cnt)/len(x)))

def batch_predict(batch_size = 100):
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in tqdm(range(0, len(x), batch_size), desc="forecast schedule", unit="sample"):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network=network,x=x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t[i:i+batch_size])

    print("Accuracy:"+ str(float(accuracy_cnt)/len(x)))

def main():
    # single_predict()
    batch_predict()

if __name__ == '__main__':
    main()