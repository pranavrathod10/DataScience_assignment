# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('roadsafety_accident_cause.xlsx')

# # Filter the dataframe to only include rows where the cause of accident is overspeeding
# df_overspeeding = df[df['cause of accident'] == 'Overspeeding']

# # Check the column names in df_overspeeding
# print(df_overspeeding)

# # Create a bar plot of the number of accidents caused by overspeeding for each year
# plt.bar(df_overspeeding['year'], df_overspeeding['no of accident'])
# plt.xlabel('Year')
# plt.ylabel('Number of Accidents')
# plt.title('Accidents Caused by Overspeeding')
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Read in the datapi
# df = pd.read_excel('roadsafety_accident_cause.xlsx')

# # Define a list of colors for each cause
# colors = {'Overspeeding': 'red',
#           'Drunken driving/ consumption of alcohol & drug': 'green',
#           'Driving on wrong side/Lane indiscipline': 'blue',
#           'Jumping red light': 'orange',
#           'Use of mobile phone': 'purple',
#           'Others': 'gray'}

# # Set up the plot
# fig, ax = plt.subplots()
# ax.set_xlim(df['no of accident'].min() - 1000, df['no of accident'].max() + 1000)
# ax.set_ylim(0, len(df['cause of accident'].unique()) + 1)
# ax.set_yticks(range(1, len(df['cause of accident'].unique()) + 1))
# ax.set_yticklabels(df['cause of accident'].unique())
# ax.set_xlabel('Number of Accidents')

# # Create a scatter plot of the data
# scatter = ax.scatter(df[df['year'] == 2021]['no of accident'], df[df['year'] == 2021]['cause of accident'], s=150, c=df[df['year'] == 2021]['cause of accident'].apply(lambda x: colors[x]))

# # Define a function to update the scatter plot for each year
# def update(year):
#     scatter.set_offsets(df[df['year'] == year][['no of accident', 'cause of accident']])
#     scatter.set_color(df[df['year'] == year]['cause of accident'].apply(lambda x: colors[x]))
#     return scatter,

# # Animate the plot
# ani = animation.FuncAnimation(fig, update, frames=df['year'].unique(), interval=1000, blit=True)

# plt.show()

# ###########--------------------------------------------##################
# # graphs


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Read in the data
# df = pd.read_excel('roadsafety_accident_cause.xlsx')

# # Define a list of colors for each cause
# colors = {'Overspeeding': 'red',
#           'Drunken driving/ consumption of alcohol & drug': 'green',
#           'Driving on wrong side/Lane indiscipline': 'blue',
#           'Jumping red light': 'orange',
#           'Use of mobile phone': 'purple',
#           'Others': 'gray'}

# # Set up the line plot
# sns.set_style('whitegrid')
# fig, ax = plt.subplots(figsize=(12, 8))
# ax.set_ylabel('Number of Accidents')
# ax.set_xlabel('Year')
# ax.set_title('Number of Accidents by Cause and Year')

# # Create a line plot for each cause of accident
# for cause in df['cause of accident'].unique():
#     data = df[df['cause of accident'] == cause]
#     sns.lineplot(x='year', y='no of accident', data=data, ax=ax, label=cause, color=colors[cause])

# plt.show()

# ########-----------correlation matrix---------##########

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Read in the data
# df = pd.read_excel('roadsafety_accident_cause.xlsx')

# # Calculate the correlation matrix
# corr = df.pivot_table(index='cause of accident', columns='year', values='no of accident', aggfunc='sum').corr()

# # Set up the heatmap
# fig, ax = plt.subplots(figsize=(10, 10))
# sns.heatmap(corr, annot=True, cmap='coolwarm')

# # Add labels and title
# ax.set_ylabel('Cause of Accident')
# ax.set_xlabel('Year')
# ax.set_title('Correlation Matrix of Number of Accidents by Cause and Year')

# plt.show()



################--------------hypothesis graph-------------##############

# The data in the roadsafety_accident_cause.xlsx file contains the number of accidents by cause and year. One possible hypothesis test that can be conducted on this data is to determine if there is a significant difference in the number of accidents for a particular cause between two consecutive years.
# For example, we can test the hypothesis that there is no significant difference in the number of accidents caused by "Overspeeding" between 2021 and 2022. Here are the steps for conducting this hypothesis test:
# Define the null hypothesis: The null hypothesis is that there is no significant difference in the number of accidents caused by Overspeeding between 2021 and 2022.
# Define the alternative hypothesis: The alternative hypothesis is that there is a significant difference in the number of accidents caused by Overspeeding between 2021 and 2022.
# Choose the level of significance: Let's choose the level of significance as 0.05.
# Calculate the test statistic: We can use a paired t-test to calculate the test statistic. This test compares the means of two related groups. In this case, the two related groups are the number of accidents caused by Overspeeding in 2021 and 2022. The test statistic is calculated as:
# t = (x1 - x2) / (s / sqrt(n))
# where x1 and x2 are the sample means, s is the sample standard deviation, and n is the sample size.

# Determine the critical value: We can use a t-distribution table to determine the critical value for the chosen level of significance and degrees of freedom.

# Compare the test statistic with the critical value: If the absolute value of the test statistic is greater than the critical value, we reject the null hypothesis. If the absolute value of the test statistic is less than or equal to the critical value, we fail to reject the null hypothesis.

# Interpret the results: If we reject the null hypothesis, we can conclude that there is a significant difference in the number of accidents caused by Overspeeding between 2021 and 2022. If we fail to reject the null hypothesis, we cannot conclude that there is a significant difference in the number of accidents caused by Overspeeding between 2021 and 2022.

# import pandas as pd
# import scipy.stats as stats

# # Read in the data
# df = pd.read_excel('roadsafety_accident_cause.xlsx')

# # Filter the data for Overspeeding cause and years 2021 and 2022
# overspeeding_data = df[(df['cause of accident'] == 'Overspeeding') & (df['year'].isin([2021, 2022]))]

# # Define the null hypothesis
# null_hypothesis = "There is no significant difference in the number of accidents caused by Overspeeding between 2021 and 2022."

# # Define the alternative hypothesis
# alt_hypothesis = "There is a significant difference in the number of accidents caused by Overspeeding between 2021 and 2022."

# # Choose the level of significance
# alpha = 0.1

# # Calculate the sample means and sample standard deviation
# x1 = overspeeding_data[overspeeding_data['year'] == 2021]['no of accident'].mean()
# x2 = overspeeding_data[overspeeding_data['year'] == 2022]['no of accident'].mean()
# s = overspeeding_data['no of accident'].std()

# # Calculate the test statistic
# n = len(overspeeding_data)
# t = (x1 - x2) / (s / (n ** 0.5))

# # Calculate the degrees of freedom
# df = n - 1

# # Determine the critical value
# critical_value = stats.t.ppf(1 - alpha / 2, df)

# # Compare the test statistic with the critical value
# if abs(t) > critical_value:
#     print(f"We reject the null hypothesis. {alt_hypothesis}")
# else:
#     print(f"We fail to reject the null hypothesis. {null_hypothesis}")





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

# Read in the data
df = pd.read_excel('roadsafety_accident_cause.xlsx')

# Subset the data for overspeeding
df_os = df[df['cause of accident'] == 'Overspeeding']

if df_os.empty:
    print("No data found for 'Overspeeding' accidents")
else:
    # Calculate the mean and standard deviation for each year
    mean_accidents = df_os.groupby('year')['no of accident'].mean()
    std_accidents = df_os.groupby('year')['no of accident'].std()

    # Calculate the paired t-test for the change in mean from 2020 to 2021
    t_stat, p_value = ttest_rel(df_os[df_os['year'] == 2020]['no of accident'], df_os[df_os['year'] == 2021]['no of accident'])

    # Set up the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=mean_accidents.index, y=mean_accidents, yerr=std_accidents, palette='viridis', capsize=0.1, ax=ax)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Number of Accidents')
    ax.set_title('Average Number of Accidents due to Overspeeding')

    # Add annotation for t-test result
    if p_value < 0.05:
        ax.annotate(f'p-value = {p_value:.3f} (significant)', xy=(0.5, 0.9), xycoords='axes fraction', ha='center')
    else:
        ax.annotate(f'p-value = {p_value:.3f} (not significant)', xy=(0.5, 0.9), xycoords='axes fraction', ha='center')

    plt.show()
