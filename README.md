# Forschungsprojekt Kresse-Experiment im Modul WIAS Ws23/24

In diesem Git Repository finden wir alle Materialien, Methoden und Ergebnisse
zu dem Forschungsprojekt.

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
