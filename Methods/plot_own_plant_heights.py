# Import the tools (modules / packages) needed for plotting:
import sys # read out command line arguments
import pandas # read and write tables (CSV)
import matplotlib.pyplot as plt # library to create scientific plots

# Read in the table of plant height measurements:
table_file = sys.argv[1]
print("Going to read in plant height measurements from", table_file)
plant_heights_data_frame = pandas.read_csv(table_file)

# Plot each days mean value per medium:
mean_values = []
days = plant_heights_data_frame["Day"].unique()
days.sort()
media = plant_heights_data_frame["Medium"].unique()

# Calcualte mean values per day:
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


# Now plot the mean values per day and media:
# To Do! Better create a data frame of mean values per day
