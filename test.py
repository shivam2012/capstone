import torch

print(torch.cuda.get_device_name(torch.device('cuda')))