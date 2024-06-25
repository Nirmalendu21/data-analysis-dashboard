import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the sample dataset from seaborn
df = sns.load_dataset('penguins')

# Display the first few rows of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

sns.pairplot(df, hue='species')
plt.suptitle('Pairplot of Penguin Dataset', y=1.02)
plt.show()


fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species', 
                 title='Bill Length vs Bill Depth')
fig.show()


fig = px.box(df, x='species', y='flipper_length_mm', 
             title='Flipper Length by Species')
fig.show()



fig = px.histogram(df, x='body_mass_g', color='species', 
                   title='Body Mass Distribution')
fig.show()


from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Create subplots
fig = make_subplots(rows=2, cols=2, 
                    subplot_titles=("Bill Length vs Bill Depth", "Flipper Length by Species", 
                                    "Body Mass Distribution", "Pairplot (Matplotlib)"))

# Scatter plot
fig.add_trace(go.Scatter(x=df['bill_length_mm'], y=df['bill_depth_mm'], mode='markers',
                         marker=dict(color=df['species'].map({'Adelie': 'blue', 'Chinstrap': 'red', 'Gentoo': 'green'})), 
                         name='Bill Length vs Bill Depth'), row=1, col=1)

# Box plot
fig.add_trace(go.Box(y=df['flipper_length_mm'], x=df['species'], name='Flipper Length by Species'), row=1, col=2)

# Histogram
fig.add_trace(go.Histogram(x=df['body_mass_g'], marker_color=df['species'].map({'Adelie': 'blue', 'Chinstrap': 'red', 'Gentoo': 'green'}).values, 
                           name='Body Mass Distribution'), row=2, col=1)

# Add an image of the pairplot created by Matplotlib
pairplot_fig = sns.pairplot(df, hue='species')
pairplot_fig.fig.savefig(r'C:\Users\NIRMAL\Downloads\PDA.png')

img = plt.imread(r'C:\Users\NIRMAL\Downloads\PDA.png')
fig.add_trace(go.Image(z=img), row=2, col=2)

# Update layout
fig.update_layout(title_text="Penguin Data Analysis Dashboard", height=800, showlegend=False)

# Show dashboard
fig.show()
