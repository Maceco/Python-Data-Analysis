import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male']
    age_men = men['age'].value_counts()
    sum_age_men = 0
    total_men = 0
    for index, value in age_men.items():
        sum_age_men += index * value
        total_men += value

    average_age_men = round(sum_age_men / total_men, ndigits=1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df.loc[df['education'] == 'Bachelors']['education'].value_counts().values[0]
    percentage_bachelors = round(bachelors / len(df) * 100, ndigits=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
        # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]['salary']
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]['salary']

    # percentage with salary >50K
    higher_education_rich = round(higher_education.value_counts()['>50K'] / len(higher_education) * 100, ndigits=1)
    lower_education_rich = round(lower_education.value_counts()['>50K'] / len(lower_education) * 100, ndigits=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].value_counts().index.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == 1]['salary']
    num_min_workers_rich = num_min_workers.value_counts()['>50K']
    rich_percentage = round(num_min_workers_rich / len(num_min_workers) * 100, ndigits=3)

    # What country has the highest percentage of people that earn >50K?
    high_salaries = df.loc[df['salary'] == '>50K']['native-country'].value_counts()
    countries = df['native-country'].value_counts()
    # highest_earning_country
    highest_earning_country = ''
    highest_earning_country_percentage = 0
    for index, value in high_salaries.items():
        perc_high_salaries = value / countries[index] * 100
        if perc_high_salaries > highest_earning_country_percentage:
            highest_earning_country_percentage = round(perc_high_salaries, ndigits=1)
            highest_earning_country = index

    # Identify the most popular occupation for those who earn >50K in India.
    india = df.loc[df['native-country'] == 'India']['occupation'].value_counts()
    top_IN_occupation = india.index[india.values == india.max()].tolist()[0]

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
