import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.dropna(inplace = True)
    df = df.astype({
    "education": "category",
    "occupation": "category",
    "race": "category",
    "sex": "category",
    "native-country": "category",
    "salary": "category"
    }) 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = np.round(np.mean(df["age"][df["sex"] == "Male"]), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round((len(df["education"][df["education"] == "Bachelors"]) / len(df["education"])) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_filter = (df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")
    database_higher_education = df[higher_education_filter]
    higher_education = len(database_higher_education["education"])

    lower_education_filter = ~ higher_education_filter
    database_lower_education = df[lower_education_filter]
    lower_education = len(database_lower_education["education"])

    # percentage with salary >50K
    higher_education_rich = np.round(len(database_higher_education[database_higher_education["salary"] == ">50K"]) / higher_education * 100, 1)
    lower_education_rich = np.round(len(database_lower_education[database_lower_education["salary"] == ">50K"]) / lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    database_min_work_hours = df[df["hours-per-week"] == min_work_hours]
    num_min_workers = len(database_min_work_hours["salary"])

    num_min_workers_filter = database_min_work_hours["salary"] == ">50K"
    rich_percentage = np.round(len(database_min_work_hours[num_min_workers_filter]) / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_workers_more50k = df[df["salary"] == ">50K"]
    serie_country_more50k = country_workers_more50k["native-country"].value_counts()
    df["ones"] = 1  #Column of ones created to count the number of people per country
    people_per_country = df.groupby("native-country")["ones"].count().sort_values(ascending=False)
    percentage_earning_country = np.round((serie_country_more50k / people_per_country) * 100, 1).sort_values(ascending=False)

    highest_earning_country = percentage_earning_country.idxmax()
    highest_earning_country_percentage = percentage_earning_country.max()


    # Identify the most popular occupation for those who earn >50K in India.
    india_database = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_database["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
