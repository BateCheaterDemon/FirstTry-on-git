import gym
import torch
import torch.nn.functional as F
import torch.nn as nn 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import random   
import rl_utils

# 定义策略网络（Policy Network），用于生成动作的概率分布
class PolicyNet(nn.Module):
    def __init__(self,state_dim,hidden_dim,action_dim):
        super(PolicyNet,self).__init__()
        self.fc1=nn.Linear(state_dim,hidden_dim)
        self.fc2=nn.Linear(hidden_dim,action_dim)

    def forward(self,x):
        x=F.relu(self.fc1(x))
        x=self.fc2(x)
        return F.softmax(x,dim=1) # 通过第二层并应用Softmax激活函数，得到动作概率分布

class ValueNet(nn.Module):
    def __init__(self,state_dim,hidden_dim):
        super(ValueNet,self).__init__()
        self.fc1=nn.Linear(state_dim,hidden_dim)
        self.fc2=nn.Linear(hidden_dim,1)

    def forward(self,x):
        x=F.relu(self.fc1(x))
        return self.fc2(x)
    
class PPO:
    '''PPO算法采用截断方式'''
    def __init__(self,state_dim,hidden_dim,action_dim,actor_lr,critic_lr,
                 lmbda,epochs,eps,gamma,device):
        self.actor=PolicyNet(state_dim,hidden_dim,action_dim).to(device=device)
        self.critic=ValueNet(state_dim,hidden_dim).to(device)
        self.actor_optimizer=torch.optim.Adam(self.actor.parameters(),lr=actor_lr)

        self.critic_optimizer=torch.optim.Adam(self.critic.parameters(),lr=critic_lr)

        self.gamma=gamma
        self.lmbda=lmbda
        self.epochs=epochs # 一条序列的数据用于训练轮数
        self.eps=eps # PPO中截断范围的参数
        self.device=device

    def take_action(self,state):
        state=torch.tensor([state],dtype=torch.float).to(self.device)
        probs=self.actor(state) 
        action_dist=torch.distributions.Categorical(probs) # 用于描述在给定概率分布下，从多个可能的结果中选择一个结果的概率。
        action=action_dist.sample() # 作是根据概率分布 probs 随机选择的，概率越高的动作被选中的可能性越大。
        return action.item() # item()把单个元素的torch元素转为标准python数
    
    def update(self,transition_dict):
        states=torch.tensor(transition_dict['states'],dtype=torch.float).to(self.device)
        actions=torch.tensor(transition_dict['actions']).view(-1,1).to(self.device)
        rewards=torch.tensor(transition_dict['rewards'],dtype=float).view(-1,1).to(self.device)

        next_states=torch.tensor(transition_dict['next_states'],dtype=torch.float).to(self.device)
        dones=torch.tensor(transition_dict['dones'],dtype=torch.float).view(-1,1).to(self.device)

        td_target=rewards+self.gamma*self.critic(next_states)*(1-dones)
        td_delta=td_target-self.critic(states)
        advantage=rl_utils.compute_advantage(self.gamma,self.lmbda,td_delta)

        old_log_probs=torch.log(self.actor(states).gather(1,actions)).detach()

        for _ in range(self.epochs): # 这里的 _ 表示我们不关心 range(self.epochs) 生成的迭代值，我们只是想重复执行代码块 self.epochs 次。
            # self.epochs 很可能是一个整数，表示训练过程中的迭代次数或周期数。
            #如果我们将 _ 替换为其他变量名，代码的行为不会有任何改变，但是代码的可读性可能会降低，因为使用 _ 明确表示我们不关心迭代的具体值
            # for i in range(self.epochs):

            log_probs = torch.log(self.actor(states).gather(1,actions))
            radio = torch.exp(log_probs-old_log_probs)
            surr1=radio*advantage
            surr2=torch.clamp(radio,1-self.eps,1+self.eps)*advantage #截断

            actor_loss = torch.mean(-torch.min(surr1,surr2)) # PPO损失函数
            critic_loss = torch.mean(F.mse_loss(self.critic(states),td_target.detach()))
            self.actor_optimizer.zero_grad()
            self.critic_optimizer.zero_grad()
            actor_loss.backward()
            critic_loss.backward()
            self.actor_optimizer.step()
            self.critic_optimizer.step()

actor_lr=1e-3
critic_lr=1e-2
num_episodes=250
hidden_dim=128
gamma=0.98
lmbda=0.95
epochs=10
eps=0.2
device=torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

env_name='CarPole-v0'
env=gym.make(env_name)
env.seed(0)
torch.manual_seed(0)
state_dim=env.observation_space.shape[0]
action_dim=env.action_space.n
ppo_agent = PPO(state_dim=state_dim,
                hidden_dim=hidden_dim,
                action_dim=action_dim,
                actor_lr=actor_lr,
                critic_lr=critic_lr,
                lmbda=lmbda,
                epochs=epochs,
                eps=eps,
                gamma=gamma,
                device=device)

return_list=rl_utils.train_on_policy_agent(env,ppo_agent,num_episodes=num_episodes)

