# Import the tools (modules / packages) needed for plotting:
import pandas as pd  # Alias for pandas
import matplotlib.pyplot as plt  # library to create scientific plots
import seaborn as sns # library to create grouped boxplots
import sys

# Read in the table of plant height measurements:
table_file = sys.argv[1]
print("Going to read in plant height measurements from", table_file)
plant_heights_data_frame = pd.read_csv(table_file)

# Plot each day's mean value per medium:
mean_values = []
days = plant_heights_data_frame["Day"].unique()
days.sort()
media = plant_heights_data_frame["Medium"].unique()

# Calculate mean values per day:
for day in days:
    # Calculate mean values per medium per day:
    means_of_day = []
    for medium in media:
        plnt_hght_for_day = plant_heights_data_frame[
            plant_heights_data_frame["Day"] == day
        ]
        plnt_hght_for_day_and_for_medium = plnt_hght_for_day[
            plnt_hght_for_day["Medium"] == medium
        ]
        # Calculate the mean:
        medium_mean_per_day = plnt_hght_for_day_and_for_medium["Height"].mean()
        means_of_day.append(medium_mean_per_day)
    # Outer for-loop:
    mean_values.append(means_of_day)

# Create a DataFrame for mean values:
mean_values_df = pd.DataFrame(mean_values, columns=media)
mean_values_df["Day"] = days

# The following is the scatter plot of mean plant height values per day and
# medium -
# Now plot the mean values per day and media:
for medium in media:
    plt.scatter(mean_values_df["Day"], mean_values_df[medium], label=medium)

plt.xlabel("Day")
plt.ylabel("Mean Plant Height [mm]")
plt.title("Mean Plant Height per Day and Medium")
plt.legend()
plt.savefig("mean_plant_heights_per_day_and_medium_scatter_plot.pdf")


# Create a grouped boxplot of plant height values per day and medium:
sns.boxplot(x="Day", y="Height", hue="Medium", data=plant_heights_data_frame)
plt.savefig("plant_heights_per_day_and_medium_boxplot.pdf")



# Create above plots but also showing other students' data:
other_student_table_file = sys.argv[2]
print("Going to read other students' plant height measurements from file",
      other_student_table_file) 
other_student_plant_heights = pd.read_csv(other_student_table_file)

# Create a grouped boxplot of plant height values per day and medium,
# this time comparing my and other students' plant height measurements:
# First rename the media to "my Salzig", "my Sauer", etc
my_plant_heights_tbl = plant_heights_data_frame
my_plant_heights_tbl["Medium"] = list(map(lambda x: "My " + x,
                                              my_plant_heights_tbl["Medium"]))
other_student_plant_heights["Medium"] = list(map(lambda x: "Other " + x,
                                                 other_student_plant_heights["Medium"]))
joint_plant_heights_table = pd.concat([my_plant_heights_tbl, other_student_plant_heights])
sns.boxplot(x="Day", y="Height", hue="Medium", data=joint_plant_heights_table)
plt.savefig("plant_heights_per_day_and_medium_comparison_with_other_students_boxplot.pdf")
