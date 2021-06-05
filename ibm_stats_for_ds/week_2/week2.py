"""Module wrapper for Week 2"""
import numpy
import pandas
import seaborn
import matplotlib.pyplot as plt


def main():
    """Main function"""
    ratings_url = (
        "https://cf-courses-data.s3.us.cloud-object-storage"
        + ".appdomain.cloud/IBMDeveloperSkillsNetwork-"
        + "ST0151EN-SkillsNetwork/labs/teachingratings.csv"
    )
    ratings_df = pandas.read_csv(ratings_url)
    unique_profs = ratings_df.prof.unique()
    not_unique_profs = ratings_df.prof.nunique()

    age_mean = ratings_df["age"].mean()
    age_std = ratings_df["age"].std()

    unique_ratings_df = ratings_df.drop_duplicates(subset=["prof"])
    head = unique_ratings_df.head()

    unique_mean = unique_ratings_df["age"].mean()
    unique_std = unique_ratings_df["age"].std()

    division_eval = ratings_df.groupby("division")[["eval"]].mean().reset_index()

    seaborn.set(style="whitegrid")
    ax = seaborn.barplot(x="division", y="eval", data=division_eval)
    ax = seaborn.scatterplot(x="age", y="eval", data=ratings_df)
    ax = seaborn.scatterplot(x="age", y="eval", hue="gender", data=ratings_df)
    ax = seaborn.boxplot(x="credits", y="beauty", data=ratings_df)

    seaborn.catplot(x="gender", hue="tenure", kind="count", data=ratings_df)
    seaborn.catplot(
        x="gender",
        hue="tenure",
        row="division",
        kind="count",
        data=ratings_df,
        height=3,
        aspect=2,
    )
    seaborn.relplot(
        x="age",
        y="eval",
        hue="gender",
        row="tenure",
        data=ratings_df,
        height=3,
        aspect=2,
    )
    ax = seaborn.distplot(ratings_df["eval"], kde=False)
    seaborn.distplot(
        ratings_df[ratings_df["gender"] == "female"]["eval"], color="green", kde=False
    )
    seaborn.distplot(
        ratings_df[ratings_df["gender"] == "male"]["eval"], color="orange", kde=False
    )

    seaborn.boxplot(x="gender", y="age", data=ratings_df)
    seaborn.boxplot(x="tenure", y="age", hue="gender", data=ratings_df)

    # Question 1
    seaborn.distplot(
        ratings_df[ratings_df["native"] == "yes"]["eval"], color="orange", kde=False
    )
    seaborn.distplot(
        ratings_df[ratings_df["native"] == "no"]["eval"], color="blue", kde=False
    )
    # Question 2
    seaborn.boxplot(x="age", y="minority", data=ratings_df)
    # Question 3
    seaborn.catplot(
        x="tenure", hue="minority", kind="count", data=ratings_df, row="gender"
    )
    # Question 4
    seaborn.boxplot(x="age", y="minority", data=ratings_df)
    plt.show()
