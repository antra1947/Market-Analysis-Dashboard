#!/usr/bin/env python3
"""
Market Analysis Dashboard - Python Implementation
Replicates the key insights from the Power BI dashboard using pandas and matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

class MarketAnalysisDashboard:
    def __init__(self, data_path="Market-Analysis-Dashboard-main/train.csv"):
        """Initialize the dashboard with data loading"""
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Load and prepare the dataset"""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"✅ Data loaded successfully: {len(self.df):,} records")
            print(f"📊 Columns: {list(self.df.columns)}")
            print(f"📈 Response rate: {self.df['Response'].mean():.2%}")
        except FileNotFoundError:
            print(f"❌ Error: Could not find {self.data_path}")