# Forschungsprojekt Kresse-Experiment im Modul WIAS Ws23/24

In diesem Git Repository finden wir alle Materialien, Methoden und Ergebnisse
zu dem Forschungsprojekt.

## Python dependencies

Use the following command to install the dependencies in order to run the
python scripts in this research project:
```sh
pip install pandas matplotlib seaborn
```

## Simulate data

Wir möchten unsere Plot erzeugenden Scripte vorbereiten, bevor schon
Pflanzenwuchshöhen gemessen worden sind. Um dies zu ermöglichen, simulieren wir
uns Wuchshöhendaten. Dies machen wir mit dem Script:
`./Methods/simulate_data.py`

The above script generates an output table (CSV) in the directory
`./Material/simulated_plant_height_data.csv`. 

Call the script from the root directory of this repository.

The output table has four columns:
* Medium
* Height
* Day
* Student

We want to simulate also the data of other students, in order to see whether
our plant height measurements deviate from those of other students.

How to simulate this?
- Rename the already created table `./Material/simulated_plant_height_data.csv`
  and use it as a simulated table of other students
  `./Material/simulated_plant_height_data_other_student.csv`
- Create a new table of simulated plant height measurement data.

Now you have two tables to test your plotting code.


## Scientific plots of plant height measurements

Ongoing process, see file `./Methods/plot_own_plant_heights.py` for details
(see "To Do").
