# Simulate data for the plotting scripts, so we can plot before any meaurements
# (data) are actually available.

# Wir brauchen einige Werkzeuge, die uns helfen Zufallszahlen zu generieren.
import numpy
# Wir brauchen eine Bibliothek, um die simulierten Daten in einer Tabelle
# (comma seperated values, CSV) abzuspeichern:
import pandas

# Wir generieren uns Zufallszahlen, die Gauss (Normal) verteilt sind.

def generate_plant_heights(n_per_day, mean, standard_deviation, add_to_mean_per_day, medium, student):
    """
    Generate (simulate) plant height measurements using normally distributed
    random values. Generate argument 'n_per_day' random numbers for each day of
    1 to 14 and add to the mean of the normal distribution each day the
    argument 'add_to_mean_per_day'.

    :param n_per_day: Defines how many random vavlues per day are generated
    :param mean: The mean value of the normal distribution on day one
    :param standard_deviation: The standard deviation used for the random number generation with numpy.random.normal
    :param add_to_mean_per_day: Each day this value will be added to the mean of the day before.
    :param medium: A string describing the medium the plants were grown in
    :param student: A string, the name of the student that carried out the measurements
    :return: Return an array of arrays, where each row (array) represents a row
    in the plant height measurement table
    """
    random_plant_heights_per_day = []
    for day in range(1,15):
        day_mean = mean + (day - 1) * add_to_mean_per_day
        day_random_plant_heights = numpy.random.normal(day_mean, standard_deviation, n_per_day)
        for random_plant_height in day_random_plant_heights:
            # This is a single row in our simulated plant height measurements
            # output table:
            random_plant_heights_per_day.append(
                    {'Medium': medium, 'Height': random_plant_height, 'Day': day,
                     'Student': student}
                )
    return random_plant_heights_per_day


# Generate plant heights for normal medium
normal_medium_plant_height_sim = generate_plant_heights(20, 3, 2, 2, "Normal", "John Doe")
# Generate plant heights for salty medium
salty_medium_plant_height_sim = generate_plant_heights(20, 2, 1.5, 1, "Salzig", "John Doe")
# Generate plant heights for acidic medium
acidic_medium_plant_height_sim = generate_plant_heights(20, 1, 1, 0.5, "Sauer", "John Doe")

# Write the simulated plant height measurements into a table of the same format
# that will be used to deliver the actual measurements:
normal_df = pandas.DataFrame(data=normal_medium_plant_height_sim)
salty_df = pandas.DataFrame(data=salty_medium_plant_height_sim)
acidic_df = pandas.DataFrame(data=acidic_medium_plant_height_sim)

# Concatonate above tables into one:
final_simulated_plant_heights_table = pandas.concat([ normal_df, salty_df, acidic_df ])
final_simulated_plant_heights_table.to_csv('./Material/simulated_plant_height_data.csv', index=False)

# Finished
print("DONE")
