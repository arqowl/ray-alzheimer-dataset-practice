import pandas as pd
import torch
import numpy as np
from torch.utils.data import Dataset



class RayAlzheymerDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        features = [
    "ANG", "BDNF", "BLC", "BMP-4", "BMP-6", "CK b8-1", "CNTF", "EGF", "Eotaxin", "Eotaxin-2", 
    "Eotaxin-3", "FGF-6", "FGF-7", "Fit-3 Ligand", "Fractalkine", "GCP-2", "GDNF", "GM-CSF", 
    "I-309", "IFN-g", "IGF-1", "IGFBP-1", "IGFBP-2", "IGFBP-4", "IL-10", "IL-13", "IL-15", 
    "IL-16", "IL-1a", "IL-1b", "IL-1ra", "IL-2", "IL-3", "IL-4", "IL-5", "IL-6", "IL-7", 
    "LEPTIN(OB)", "LIGHT", "MCP-1", "MCP-2", "MCP-3", "MCP-4", "M-CSF", "MDC", "MIG", 
    "MIP-1d", "MIP-3a", "NAP-2", "NT-3", "PARC", "PDGF-BB", "RANTES", "SCF", "SDF-1", 
    "TARC", "TGF-b", "TGF-b3", "TNF-a", "TNF-b", "Acrp30", "AgRP(ART)", "ANG-2", "AR", 
    "AXL", "bFGF", "b-NGF", "BTC", "CCL-28", "CTACK", "DTK", "EGF-R", "ENA-78", "FAS", 
    "FGF-4", "FGF-9", "GCSF", "GITR", "GITR-Light", "GRO", "GRO-a", "HCC-4", "HGF", 
    "ICAM-1", "ICAM-3", "IGF-1 SR", "IGFBP-3", "IGFBP-6", "IL-1 RI", "IL-11", "IL-12 p40", 
    "IL-12 p70", "IL-17", "IL-1R4 /ST2", "IL-2 Ra", "IL-6 R", "IL-8", "I-TAC", "Lymphotactin", 
    "MIF", "MIP-1a", "MIP-1b", "MIP-3b", "MSP-a", "NT-4", "OSM", "OST", "PIGF", "spg130", 
    "sTNF RI", "sTNF RII", "TECK", "TIMP-1", "TIMP-2", "TPO", "TRAIL R3", "TRAIL R4", 
    "uPAR", "VEGF-B", "VEGF-D"
]
        dtype_dict = {feature: np.float64 for feature in features}
        dtype_dict['CLASS'] = str
        
        self.data = pd.read_csv(csv_file, delimiter=';',decimal=',', dtype=dtype_dict)
        columns_to_select = ['CLASS',
    "ANG-2", "RANTES", "MCP-3", "HCC-4", "PARC", "IL-8", "EGF", "GCSF", 
    "GDNF", "ICAM-1", "IGFBP-6", "IL-1a", "IL-3", "IL-11", "M-CSF", 
    "PDGF-BB", "TNF-a", "TRAIL R4"
]
        self.data= self.data[columns_to_select]
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data.iloc[idx, 1:].to_numpy(dtype=np.float64)  # Features
        label = self.data.iloc[idx][0]
        label = 1 if label == 'AD' else 0
        if self.transform:
            sample = self.transform(sample)
        return torch.tensor(sample, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
    


if __name__ == '__main__':
    train_dataset = RayAlzheymerDataset(csv_file='datasets/ray_dataset/AD-Train-120.csv')
    test_dataset = RayAlzheymerDataset(csv_file='datasets/ray_dataset/AD-Test-120.csv')