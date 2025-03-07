import torch

#Program to Convert Fahrenheit to Celsius
weight = 32
b= 1.8
num = torch.tensor([20,40,38,19])
X = 1*weight + b* num
print(X)
print(X.size())