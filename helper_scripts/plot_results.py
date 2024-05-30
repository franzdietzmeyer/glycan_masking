import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Assuming input_dir is provided as a command line argument
#input_dir = sys.argv[1]
output=sys.argv[1]
# Define your dataset
df = pd.read_csv(f"{output}/results/scores/final_scores_GM.csv")

# Find the y-value for 'mut0wt'
mut0wt_value = df.loc[df['mut_group'] == 'mut0wt', 'total_score'].values[0]

# Plot PTM against total_score
plt.figure(figsize=(10, 6))
plt.scatter(df['PTM'], df['total_score'])

# Add labels and title
plt.xlabel('PTMMetric score')
plt.ylabel('total_score for mutation variants [REU]')
plt.title('total_score vs PTMMetricPrediction Score')

# Add mut_group as labels for each point
for i, txt in enumerate(df['mut_group']):
    plt.annotate(txt, (df['PTM'][i], df['total_score'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Draw horizontal line at the y-value of 'mut0wt'
plt.axhline(y=mut0wt_value, color='r', linestyle='--', label='mut0wt')

# Draw vertical line at x=0.6
plt.axvline(x=0.6, color='b', linestyle='--', label='x=0.6')

plt.xlim(0, 1)

# Show grid
plt.grid(True)
plt.tight_layout()

# Save plot to file
plt.savefig(f'{output}/results/results_csm_plot.png')

# Display plot
#plt.show()


print('results plotted succsessfully')






# Read the CSV file into a DataFrame
df2 = pd.read_csv(f"{output}/results/scores/final_scores_GM.csv")

mut0wt_score = df2.loc[df2['mut_group'] == 'mut0wt', 'total_score']
mut0wt_score = mut0wt_score.iloc[0]

df2['score_difference'] = df2['total_score'] - mut0wt_score



# Drop rows with 'PTM' value lower than 0.6, except for 'mut0wt'
df2 = df2[(df2['PTM'] >= 0.6) | (df2['mut_group'] == 'mut0wt')]

# Get the 'total_score' value for 'mut0wt' row
reference_score = df2.loc[df2['mut_group'] == 'mut0wt', 'score_difference'].iloc[0]

# Keep only rows where 'total_score' is lower or equal to the reference score
df2 = df2[df2['score_difference'] <= reference_score]

# Find the y-value for 'mut0wt'
mut0wt_value = df2.loc[df2['mut_group'] == 'mut0wt', 'score_difference'].values[0]

# Plot PTM against total_score
plt.figure(figsize=(10, 6))
plt.scatter(df2['PTM'], df2['score_difference'])

# Annotate points with 'mut_group' name
for i, txt in enumerate(df2['mut_group']):
    plt.annotate(txt, (df2['PTM'].iloc[i], df2['score_difference'].iloc[i]))

# Add labels and title
plt.xlabel('PTMMetric score')
plt.ylabel('total_score for mutation variants [REU]')
plt.title('total_score vs PTMMetricPrediction Score better than WT')
plt.xlim(0.6, 1)

# Show grid
plt.grid(True)
plt.tight_layout()
# Save plot to file
plt.savefig(f"{output}/results/results_betterthanWT.png")

# Display plot
#plt.show()

print('results plotted successfully')

output_dir=f"{output}/results"
output_file = os.path.join(output_dir, 'final_mutations_betterthanwt.csv')
# Output the merged DataFrame to a CSV file (optional)
df2.to_csv(output_file, index=False)



# __author__ = "Franz Dietzmeyer"
# __contact__ = "franz.dietzmeyer@medizin.uni-leipzig.de"
# __version__ = "1.5.1"
