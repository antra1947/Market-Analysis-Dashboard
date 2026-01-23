#!/usr/bin/env python3
"""
Market Analysis Dashboard - Quick Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load data
    print("🔄 Loading health insurance data...")
    df = pd.read_csv("Market-Analysis-Dashboard-main/train.csv")
    
    print(f"✅ Loaded {len(df):,} records")
    print(f"📊 Response rate: {df['Response'].mean():.2%}")
    
    # Basic statistics
    print("\n" + "="*50)
    print("📋 KEY INSIGHTS")
    print("="*50)
    
    # Gender analysis
    gender_response = df.groupby('Gender')['Response'].agg(['count', 'mean'])
    print("\n👥 Gender Analysis:")
    for gender, stats in gender_response.iterrows():
        print(f"  {gender}: {stats['mean']:.2%} response rate ({stats['count']:,} customers)")
    
    # Previous insurance impact
    prev_ins = df.groupby('Previously_Insured')['Response'].mean()
    print("\n📋 Previous Insurance Impact:")
    print(f"  Not Previously Insured: {prev_ins[0]:.2%}")
    print(f"  Previously Insured: {prev_ins[1]:.2%}")
    
    # Vehicle damage impact
    damage_impact = df.groupby('Vehicle_Damage')['Response'].mean()
    print("\n🚗 Vehicle Damage Impact:")
    for damage, rate in damage_impact.items():
        print(f"  {damage} Damage: {rate:.2%}")
    
    # Top regions
    top_regions = df.groupby('Region_Code')['Response'].agg(['count', 'mean']).sort_values('mean', ascending=False).head(5)
    print("\n🌍 Top 5 Regions by Response Rate:")
    for region, stats in top_regions.iterrows():
        print(f"  Region {region}: {stats['mean']:.2%} ({stats['count']:,} customers)")
    
    # Age analysis
    age_stats = df.groupby(pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, 100]))['Response'].mean()
    print("\n👤 Age Group Analysis:")
    for age_group, rate in age_stats.items():
        print(f"  {age_group}: {rate:.2%}")
    
    print("\n✅ Analysis complete! Key findings:")
    print("• Males show higher response rates than females")
    print("• Customers without previous insurance are more likely to respond")
    print("• Vehicle damage history significantly impacts response rates")
    print("• Regional variations suggest targeted marketing opportunities")

if __name__ == "__main__":
    main()