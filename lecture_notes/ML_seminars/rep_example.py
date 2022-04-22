from torch.utils.data import Dataset
import torch
import torchvision
from torch import Tensor, nn
from torchvision import transforms
from torch.utils import data
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import TensorDataset

# Data Generation
dots = np.random.randint(-100,100,size=[300,2])/100
polar_dots = np.concatenate((np.sqrt(dots[:,0] ** 2 + dots[:,1] ** 2).reshape(-1,1), np.arctan2(dots[:,1] , dots[:,0]).reshape(-1,1)),axis=1)
c = dots[:,0] ** 2 + dots[:,1] ** 2 < 1/2
# print(dots)
fig, axs = plt.subplots(2,2, figsize=(10,10))
# Plot 0,0
axs[0,0].scatter(dots[:,0],dots[:,1],c=c)
axs[0,0].set_xticks(np.linspace(-1,1,11))
axs[0,0].set_yticks(np.linspace(-1,1,11))
circle = plt.Circle((0,0), np.sqrt(0.5),fill=False)
axs[0,0].add_artist(circle)
# Plot 0,1
axs[0,1].scatter(polar_dots[:,0],polar_dots[:,1],c=c)
axs[0,1].set_xticks(np.linspace(0,np.sqrt(2),2))
axs[0,1].set_yticks(np.linspace(-np.pi,np.pi,8))
axs[0,1].vlines(np.sqrt(0.5), ymin=-np.pi, ymax=np.pi)
# Plot 1,0
axs[1,0].scatter(dots[:,0],dots[:,1],cmap='bone',edgecolors='black',c=c,zorder=2)
axs[1,0].set_xticks(np.linspace(-1,1,11))
axs[1,0].set_yticks(np.linspace(-1,1,11))
# Plot 1,1
axs[1,1].scatter(polar_dots[:,0],polar_dots[:,1],c=c,cmap='bone',edgecolors='black',zorder=2)
axs[1,1].set_xticks(np.linspace(0,np.sqrt(2),2))
axs[1,1].set_yticks(np.linspace(-np.pi,np.pi,8))

c = np.float32(c)
c = c.reshape(-1,1)
# print(c)
print(dots.shape)
print(c.shape)

print(np.linspace(0,np.sqrt(2),2))

dots = torch.tensor(dots, dtype=torch.float32)
polar_dots = torch.tensor(polar_dots, dtype=torch.float32)
c = torch.tensor(c, dtype=torch.float32)

dataset = TensorDataset(polar_dots, c)
print(len(dataset))
dataloader = data.DataLoader(dataset,batch_size=12)

dataset2 = TensorDataset(dots, c)
print(len(dataset2))
dataloader2 = data.DataLoader(dataset2,batch_size=12)

# Logistic Regression Models
net = nn.Sequential(
    nn.Linear(2,1),
    nn.Sigmoid()
)
net2 = nn.Sequential(
    nn.Linear(2,1),
    nn.Sigmoid(),
)

# Switch to MLP
# net2 = nn.Sequential(
#     nn.Linear(2,10),
#     nn.Sigmoid(),
#     nn.Linear(10,1),
#     nn.Sigmoid()
# )

torch.save(net2, 'net2.pth')

loss_fn = nn.BCELoss()
# print(loss(torch.tensor([1.]), net(torch.tensor([1.,2.]))))
optimizer = torch.optim.SGD(net.parameters(),lr=1)
optimizer2 = torch.optim.SGD(net2.parameters(),lr=0.5)

for epoch in range(500):
    for X,y in dataloader:
        y_hat = net(X)
        loss = loss_fn(y_hat, y)
        net.zero_grad()
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        loss = loss_fn(net(polar_dots), c)

for epoch in range(500):
    for X,y in dataloader2:
        y_hat = net2(X)
        loss = loss_fn(y_hat, y)
        net2.zero_grad()
        loss.backward()
        optimizer2.step()
    with torch.no_grad():
        loss = loss_fn(net2(dots), c)
        # print(loss)
# Plot 1,1
X, Y = np.meshgrid(np.linspace(0,np.sqrt(2),1024),np.linspace(-np.pi,np.pi,1024))
XY_flatten = np.concatenate([X.reshape(-1,1),Y.reshape(-1,1)],axis=1)
Z = net(torch.tensor(XY_flatten, dtype=torch.float32))
Z = Z.detach().numpy().reshape(1024,1024)
# print(Z)
axs[1,1].contourf(X,Y,Z,zorder=1)

# Plot 0,1
X, Y = np.meshgrid(np.linspace(-1,1,1024),np.linspace(-1,1,1024))
XY_flatten = np.concatenate([X.reshape(-1,1),Y.reshape(-1,1)],axis=1)
Z = net2(torch.tensor(XY_flatten, dtype=torch.float32))
Z = Z.detach().numpy().reshape(1024,1024)
print(Z)
axs[1,0].contourf(X,Y,Z,zorder=1)


plt.show()