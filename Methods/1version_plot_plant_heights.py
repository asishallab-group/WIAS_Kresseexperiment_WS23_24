# Import the tools (modules / packages) needed for plotting:
import pandas as pd  # Alias for pandas
import matplotlib.pyplot as plt  # library to create scientific plots

# Read in the table of plant height measurements:
table_file = "/home/ehrebehre/Downloads/simulated_plant_height_data.csv"
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

# Now plot the mean values per day and media:
for medium in media:
    plt.plot(mean_values_df["Day"], mean_values_df[medium], label=medium)

plt.xlabel("Day")
plt.ylabel("Mean Plant Height")
plt.title("Mean Plant Height per Day and Medium")
plt.legend()
plt.show()
