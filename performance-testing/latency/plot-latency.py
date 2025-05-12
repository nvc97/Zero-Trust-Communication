import pandas as pd
import matplotlib.pyplot as plt

# File paths for the 4 CSV files
baseline_file = 'results/results-base.csv'
scenario1_file = 'results/results-client-to-web.csv'
scenario2_file = 'results/results-inference-to-mq.csv'
scenario3_file = 'results/results-whole.csv'

# Load the data from each file into a DataFrame
baseline_data = pd.read_csv(baseline_file)
scenario1_data = pd.read_csv(scenario1_file)
scenario2_data = pd.read_csv(scenario2_file)
scenario3_data = pd.read_csv(scenario3_file)

# Extract the "Run" and "Average Latency (s)" columns
runs = baseline_data['Run']
baseline_latency = baseline_data['Average Latency (s)']
scenario1_latency = scenario1_data['Average Latency (s)']
scenario2_latency = scenario2_data['Average Latency (s)']
scenario3_latency = scenario3_data['Average Latency (s)']

# Plotting
plt.figure(figsize=(10, 6))

# Plot each dataset with a unique marker
plt.plot(runs, baseline_latency, marker='o', linestyle='-', label='Baseline')
plt.plot(runs, scenario1_latency, marker='s', linestyle='-', label='Scenario 1')
plt.plot(runs, scenario2_latency, marker='^', linestyle='-', label='Scenario 2')
plt.plot(runs, scenario3_latency, marker='d', linestyle='-', label='Scenario 3')

# Labels and title
plt.xlabel('Run')
plt.ylabel('Average Latency (s)')
plt.title('Comparison of Average Latency across Baseline and Scenarios')
plt.legend()
plt.grid()
plt.xticks(ticks=runs)
plt.ylim(0.75, 1.05)

# Show the plot
plt.show()
