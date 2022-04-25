import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['bmi'] = df['weight']/((df['height']/100)**2)
df['overweight'] = (df['bmi'] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars =['active','alco','cholesterol', 'gluc', 'overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly
    

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(x="variable", col="cardio", hue="value", data=df_cat, kind="count", sharey=True)
    graph.set_axis_labels("variable", "total")
    fig1 = graph.fig



    # Do not modify the next two lines
    fig1.savefig('catplot.png')
    return fig1


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
  & (df['height'] >= df['height'].quantile(0.025))
  & (df['height'] <= df['height'].quantile(0.975))
  & (df['weight'] >= df['weight'].quantile(0.025))
  & (df['weight'] <= df['weight'].quantile(0.975))]
    # drop the BMI column
    df_heat.drop(columns=['bmi'], inplace = True)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig2, ax = plt.subplots(figsize=(12, 12))
  
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square=True, linewidths=1, center=0.0, vmin=-0.1, vmax=0.3, annot=True, fmt='.1f').get_figure()


    # Do not modify the next two lines
    fig2.savefig('heatmap.png')
    return fig2
