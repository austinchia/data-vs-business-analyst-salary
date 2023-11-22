
import matplotlib.pyplot as plt

# Data preparation
roles = ['Data Analyst', 'Business Analyst']
salaries = [82000, 93043]

# Function to format the salary on y-axis
def format_salary(value, tick_number):
    return f'{int(value / 1000)}k'

# Creating the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(roles, salaries, color=['lightblue', 'pink'])

# Adding data labels with increased font size
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval/1000:.0f}k', 
             va='bottom', ha='center', fontsize=14)

# Removing axis lines and grid
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.grid(False)

# Setting labels, title, and y-axis format
plt.xlabel('Role', fontsize=14)
plt.ylabel('Average Salary ($)', fontsize=14)
plt.title('Average Salaries of Data and Business Analysts in the US', fontsize=16)
plt.xticks(fontsize=14)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_salary))
plt.ylim(0, 100000)

plt.show()
