# coding: utf-8
import sys, os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取父目录
parent_dir = os.path.dirname(current_dir)
# 添加父目录到Python路径
sys.path.append(parent_dir)

import numpy as np
import matplotlib.pyplot as plt
from Minist.minist import load_mnist
from two_layer_net import TwoLayerNet

# 读入数据
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000  # 适当设定循环的次数
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []
# New list to store loss at each epoch for plotting
epoch_loss_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 计算梯度
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)
    
    # 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        # Store the average loss for this epoch
        epoch_loss = np.mean(train_loss_list[-int(iter_per_epoch):])
        epoch_loss_list.append(epoch_loss)
        print(f"epoch {len(train_acc_list)-1}: train acc: {train_acc:.4f}, test acc: {test_acc:.4f}, loss: {epoch_loss:.4f}")

# 绘制图形 - Create two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Plot 1: Accuracy
x_epochs = np.arange(len(train_acc_list))
ax1.plot(x_epochs, train_acc_list, label='train acc', marker='o', markersize=4)
ax1.plot(x_epochs, test_acc_list, label='test acc', linestyle='--', marker='s', markersize=4)
ax1.set_xlabel("Epochs")
ax1.set_ylabel("Accuracy")
ax1.set_ylim(0, 1.0)
ax1.legend(loc='lower right')
ax1.set_title('Training and Test Accuracy')
ax1.grid(True, alpha=0.3)

# Plot 2: Loss
ax2.plot(x_epochs, epoch_loss_list, label='training loss', color='red', marker='^', markersize=4)
ax2.set_xlabel("Epochs")
ax2.set_ylabel("Loss")
ax2.legend(loc='upper right')
ax2.set_title('Training Loss')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Optional: Also plot the detailed loss per iteration (more granular)
plt.figure(figsize=(10, 4))

# # Smooth the loss for better visualization (optional)
# if len(train_loss_list) > 100:
#     # Use moving average to smooth the loss curve
#     window_size = 50
#     smoothed_loss = np.convolve(train_loss_list, np.ones(window_size)/window_size, mode='valid')
#     plt.plot(range(len(smoothed_loss)), smoothed_loss, label='smoothed loss', color='orange', alpha=0.8)
# else:
plt.plot(range(len(train_loss_list)), train_loss_list, label='loss per iteration', color='orange', alpha=0.7)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.title('Loss per Iteration (Detailed View)')
plt.grid(True, alpha=0.3)
plt.show()