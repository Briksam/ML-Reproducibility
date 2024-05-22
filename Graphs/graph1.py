import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Read CSV files
file_paths = [
    "run-n0.8-tag-Accuracy_Eval.csv",
    "run-n0.8-tag-Accuracy_Train.csv",
    "run-n0.0-tag-Accuracy_Train.csv"
]

dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    # Extract filename without extension for legend
    legend_label = ""
    if "Accuracy_Eval" in file_path:
        legend_label = "Test Set"
        color = 'blue'
    elif "n0.8" in file_path:
        legend_label = "Noisy Samples in Training Set"
        color = 'red'
    else:
        legend_label = "Clean Samples in Training Set"
        color = 'green'
    dfs.append((df, legend_label, color))

# Scale step values in the training DataFrames
t1_df = dfs[1][0].copy()  # Copy the DataFrame to avoid modifying the original in dfs
t2_df = dfs[2][0].copy()  # Copy the DataFrame to avoid modifying the original in dfs
t1_df['Step'] /= 391
t2_df['Step'] /= 391
dfs[1] = (t1_df, dfs[1][1], dfs[1][2])
dfs[2] = (t2_df, dfs[2][1], dfs[2][2])

# Plot
plt.figure(figsize=(8.94, 6.09))  # Adjusted size to approximately 644x442

# Plot green first
for df, legend_label, color in dfs:
    if 'Clean Samples' in legend_label:
        smoothed_values = savgol_filter(df["Value"], 51, 3)
        plt.plot(df["Step"], smoothed_values, label=legend_label, color=color)

# Plot red second
for df, legend_label, color in dfs:
    if 'Noisy Samples' in legend_label:
        smoothed_values = savgol_filter(df["Value"], 51, 3)
        plt.plot(df["Step"], smoothed_values, label=legend_label, color=color)

# Plot blue last
for df, legend_label, color in dfs:
    if 'Test Set' in legend_label:
        plt.plot(df["Step"], df["Value"], label=legend_label, color=color)

plt.xlabel('Epochs', fontsize=20, fontweight='bold')  # Adjusted font size and weight
plt.ylabel('Accuracy', fontsize=20, fontweight='bold')  # Adjusted font size and weight
plt.xticks(fontsize=18, fontweight='bold')  # Adjusted font size and weight
plt.yticks(fontsize=18, fontweight='bold')  # Adjusted font size and weight
# plt.title('Accuracy Evaluation')
plt.legend(loc='upper left', fontsize=12)  # Placing legend at upper left corner
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()  # Adjust layout for better fitting
plt.savefig('accuracy_plot.png', dpi=300)  # Set DPI as high as possible
plt.show()
