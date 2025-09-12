# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style for nicer plots
sns.set(style="whitegrid")

def main():
    # ===== Task 1: Load and Explore Dataset =====
    try:
        # Load Iris dataset from sklearn and convert to DataFrame
        iris_data = load_iris()
        df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
        print("Dataset loaded successfully!\n")

        # Show first 5 rows
        print("First 5 rows:")
        print(df.head(), "\n")

        # Check data types and missing values
        print("Data info:")
        print(df.info(), "\n")
        print("Missing values per column:")
        print(df.isnull().sum(), "\n")

        # No missing values here, but if there were:
        # df = df.dropna()  # or
        # df.fillna(method='ffill', inplace=True)

        # ===== Task 2: Basic Data Analysis =====
        print("Basic statistics:")
        print(df.describe(), "\n")

        # Group by species, compute mean sepal length
        species_group = df.groupby('species')['sepal length (cm)'].mean()
        print("Mean Sepal Length by Species:")
        print(species_group, "\n")

        # ===== Task 3: Data Visualization =====
        # 1. Line chart - Sepal length over sample index (not time-series but for trend)
        plt.figure(figsize=(8,4))
        plt.plot(df.index, df['sepal length (cm)'], marker='o')
        plt.title("Sepal Length Trend Across Samples")
        plt.xlabel("Sample Index")
        plt.ylabel("Sepal Length (cm)")
        plt.tight_layout()
        plt.show()

        # 2. Bar chart - Average petal length per species
        plt.figure(figsize=(6,4))
        sns.barplot(x='species', y='petal length (cm)', data=df)
        plt.title("Average Petal Length per Species")
        plt.xlabel("Species")
        plt.ylabel("Petal Length (cm)")
        plt.tight_layout()
        plt.show()

        # 3. Histogram - Distribution of sepal width
        plt.figure(figsize=(6,4))
        plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
        plt.title("Distribution of Sepal Width")
        plt.xlabel("Sepal Width (cm)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

        # 4. Scatter plot - Sepal length vs Petal length
        plt.figure(figsize=(6,4))
        sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
        plt.title("Sepal Length vs Petal Length by Species")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Petal Length (cm)")
        plt.legend(title="Species")
        plt.tight_layout()
        plt.show()

        # ===== Findings/Observations =====
        print("Observations:")
        print("- Setosa species has the shortest petal and sepal lengths on average.")
        print("- Virginica generally has longer petals and sepals.")
        print("- Sepal width distribution is roughly normal.")
        print("- There is a positive correlation between sepal length and petal length, especially in versicolor and virginica.\n")

    except FileNotFoundError:
        print("Error: Dataset file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
