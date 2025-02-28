# GAIL生成式对抗模仿学习代码实践
# 实现判别器模型，其模型架构为一个两层的全连接网络，模型输入为一个状态动作对，输出一个概率标量。
import torch
import torch.nn as nn


class Discriminator(nn.Module):

    def __init__(self, state_dim, hidden_dim, action_dim):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(state_dim + action_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, 1)

    
