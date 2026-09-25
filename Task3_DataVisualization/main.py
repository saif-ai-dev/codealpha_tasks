import pandas as pd

df = pd.read_csv("2019.csv")

print(df.head())
print(df.info())
print(df.columns)

import matplotlib.pyplot as plt
import seaborn as sns

top10 = df.sort_values("Score", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x="Score", y="Country or region", hue="Country or region", data=top10, palette="viridis", legend=False)
plt.title("Top 10 Happiest Countries (2019)")
plt.tight_layout()
plt.savefig("top10_happiest.png")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x="GDP per capita", y="Score", data=df)
plt.title("GDP per Capita vs Happiness Score")
plt.tight_layout()
plt.savefig("gdp_vs_score.png")
plt.show()

plt.figure(figsize=(10,8))
numeric_df = df.drop(columns=["Overall rank", "Country or region"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(df["Score"], bins=15, kde=True)
plt.title("Distribution of Happiness Scores")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

bottom10 = df.sort_values("Score", ascending=True).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x="Score", y="Country or region", data=bottom10, color="salmon")
plt.title("Bottom 10 Least Happy Countries (2019)")
plt.tight_layout()
plt.savefig("bottom10_least_happy.png")
plt.show()

selected = df[["Score", "GDP per capita", "Social support", "Healthy life expectancy"]]
sns.pairplot(selected)
plt.savefig("pairplot_factors.png")
plt.show()

plt.figure(figsize=(6,6))
sns.boxplot(y=df["GDP per capita"])
plt.title("GDP per Capita Distribution")
plt.tight_layout()
plt.savefig("gdp_boxplot.png")
plt.show()

def plot_relationship(x_col, y_col, filename):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.title(f"{x_col} vs {y_col}")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

plot_relationship("Freedom to make life choices", "Score", "freedom_vs_score.png")
plot_relationship("Generosity", "Score", "generosity_vs_score.png")