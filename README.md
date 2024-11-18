Assignment 7
This program allows a user to input a Pokémon ability and exports a file containing the names, type1, type2, and catch rate of Pokémon with the given ability.

Files
assignment7.py: The main script containing the functions to read Pokémon data and export the filtered data to a file.
pokemon_data.csv: The CSV file containing Pokémon data.
Functions
open_pokemon_data()
This function opens the pokemon_data.csv file and reads its contents. It returns the data as a list of lists.

Returns
data: A list of lists containing the Pokémon data, including the header.
Exceptions
FileNotFoundError: If the pokemon_data.csv file is not found, it prints an error message.


pokemon_file(given_ability1)
This function takes a given ability from the user and creates a file with the names, type1, type2, and catch rate of the Pokémon with the given ability.
Parameters
given_ability1: The ability to filter Pokémon by.
Process
Opens the Pokémon data using the open_pokemon_data() function.
Extracts the header and data rows.
Finds the indices of the relevant columns (ability1, name, type1, type2, catch_rate).
Loops through the data rows and filters Pokémon by the given ability.
Appends the filtered Pokémon data to a list.
Creates a file named pokemon_with_<given_ability1>.txt and writes the filtered data to the file.
Exceptions
ValueError: If the given ability is not found in the data, it prints an error message.
Usage
Ensure that the pokemon_data.csv file is in the same directory as assignment7.py.
Run the assignment7.py script.
Enter the desired Pokémon ability when prompted.
The script will create a file named pokemon_with_<given_ability1>.txt containing the filtered Pokémon data.

