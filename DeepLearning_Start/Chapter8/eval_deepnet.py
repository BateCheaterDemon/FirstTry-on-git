import sys, os
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pyplot as plt
from Minist.minist import load_mnist  # 注意：应该是 dataset.mnist
from deep_convnet import DeepConvNet

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)

network = DeepConvNet()
network.load_params(file_name='deep_convnet_params.pkl')  # ✅ 正确

# ✅ 修正：准确率
acc = network.accuracy(x=x_test, t=t_test)
print(f"test acc: {acc:.4f}")

print("eval finish")