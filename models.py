import torch
import torch.nn as nn

class MLPModel(nn.Module):
    def __init__(self, input_size, hidden_channels, output_size):
        super(MLPModel, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size,output_size)
        )

    def forward(self, x):
        z = self.layers(x)
        return torch.sigmoid(z).reshape((-1))
    


