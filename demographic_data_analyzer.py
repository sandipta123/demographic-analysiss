import pandas as pd
from bokeh.plotting import figure,show,output_file
from bokeh.models import ColumnDataSource,CDSView
from bokeh.layouts import gridplot
import matplotlib.pyplot as plt
#mport matplotlib_terminal as plt
def calculate_demographic_data(print_data =True):
    # Read data from file
    df = pd.read_csv('Desktop/adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors'])/len(df)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K'])/len(higher_education)*100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K'])/len(lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week']== min_work_hours])

    #rich_percentage = round(len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100, 1)
    rich_percentage = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/ df['native-country'].value_counts() * 100).sort_values(ascending=False).fillna(0).idxmax()
    highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == highest_earning_country)])*100,1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]["occupation"].value_counts().index[0]
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
        df_plot = df.groupby(['salary', 'marital-status'])['capital-gain'].max()
        print(df_plot)
        rr=df.groupby(['salary', 'marital-status'])['capital-gain'].mean().unstack()
        print(rr)
        df.groupby(['salary', 'marital-status'])['capital-gain'].mean().unstack().plot(kind='bar')
        plt.legend(['divorced','married af spouse','married civ spouse','married spouse absent','never married','seperated','widowed'])
        plt.title("salary-marital status vs capitalgain")
        plt.show()
        plt.plot(df.groupby(['salary', 'marital-status'])['capital-gain'].max().unstack())
        plt.legend(['divorced','married af spouse','married civ spouse','married spouse absent','never married','seperated','widowed'])
        plt.title("change in salary vs maritial-status")
        plt.show()
        print(df.groupby(['salary','sex'])['age'].mean().unstack())
        df.groupby(['salary','sex'])['age'].mean().unstack().plot(kind='bar')
        plt.title("change in salary & sex vs age")
        plt.show()
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
   
    

    
