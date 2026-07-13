import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set font family for Korean text and prevent minus sign clipping
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False 

# Load the query result
df = pd.read_csv("gap_21_22.csv")

# Filter the top 12 cities based on the absolute value of the change to keep the plot clean
df['abs_gap'] = df['물동량_변화량'].abs()
df_top = df.sort_values(by='abs_gap', ascending=False).head(12)

# Separate visualization for '출발' (Departure) and '도착' (Arrival)
for g_type in ['출발', '도착']:
    plot_data = df_top[df_top['구분'] == g_type].sort_values(by='물동량_변화량', ascending=False)
    
    if plot_data.empty:
        continue
        
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Use blue for positive changes and red for negative changes for intuitive visualization
    colors = ['#4C72B0' if x > 0 else '#C44E52' for x in plot_data['물동량_변화량']]
    
    sns.barplot(
        data=plot_data, 
        x='물동량_변화량', 
        y='도시명', 
        hue='도시명',       # Added to follow the latest Seaborn formatting guidelines
        palette=colors,
        legend=False,       # Hides the redundant legend
        ax=ax
    )
    
    plt.axvline(0, color='black', linestyle='--', linewidth=1) # Reference line at 0
    plt.title(f"2021 vs 2022 Cargo Volume Change by Major Cities ({g_type})", fontsize=15, pad=15)
    plt.xlabel("Change in Cargo Volume (2022 - 2021)", fontsize=11)
    plt.ylabel("City", fontsize=11)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(f"gap_{g_type}.png", dpi=300)
    plt.close()
