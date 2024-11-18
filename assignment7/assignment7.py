#Write a function where a user inputs an ability1 and the program exports a file of
#  names, type1, type2 and catch rate.

def open_pokemon_data(): #function to open the pokemon data file
    """
    This function opens the pokemon_data.csv file and reads the contents of the file.
    Returns the data in a list of lists.
    """
    try:
        with open("pokemon_data.csv", "r") as file:

            contents = file.read() #reading the contents of the file
            lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
        columns = [line.split(",") for line in lines] 
        data = columns #sets the data to the columns but will still include the header for later on

        return data #returns the data
    except FileNotFoundError: #if the file is not found it will print an error message
        print("Error: The file 'pokemon_data.csv' was not found.")

#function to make the file of pokemon names,type1,type2, and catch rate from the user given ability1
def pokemon_file(given_ability1):
    """
    This function takes in a given ability1 from the user and creates a file with the names, type1, type2, and catch rate 
    of the pokemon with the given ability1.
    Void function
    """
    try:
        pokemon_list = [] #list to store the names, etc. that have the given ability1
        #opens the data
        data = open_pokemon_data()
        
        #grabs the header
        header = data[0]
        #the actual data we'll be using 
        pokemon = data[1:] #excludes the header

        ability1_index = header.index("ability1") #finds where ability1 is
        name_index = header.index("name") #finds where name is
        type1_index = header.index("type1") #finds where type1 is
        type2_index = header.index("type2") #finds where type2 is
        catch_rate_index = header.index("catch_rate") #finds where catch_rate is

        for row in pokemon: #loops through the pokemon data
            if row[ability1_index].strip() == given_ability1:
                name = row[name_index].strip() #grabs the name
                type1 = row[type1_index].strip() #grabs the type1
                type2 = row[type2_index].strip() if row[type2_index].strip() else '-' #grabs the type2
                #grabs the catch_rate and splits it to get the number and not the trailing " that keeps appearing"
                catch_rate = row[catch_rate_index].strip().split()[0] 
                pokemon_list.append((name, type1, type2, catch_rate)) #appends the name, type1, type2, and catch_rate to the list in a tuple

        
        # #creates a file with the given ability1 name
        with open(f'pokemon_with_{given_ability1}.txt', 'w') as file:
            file.write('name\ttype1\ttype2\tcatch_rate\n') #writes the header to the file
            for entry in pokemon_list:
                file.write('\t'.join(entry) + '\n') #write the pokemon name, type1, type2, and catch_rate to the file
        
        #retPurn pokemon_list #returns the list of pokemon with the given ability1
    except ValueError: #if the given ability1 is not found it will print an error message
        print("Error: The inputted ability1 was not found in the pokemon_data.csv file.")


#asks the user to input an ability1
given_ability1 = input("Enter an ability1: ")
pokemon_file(given_ability1.title()) #calls the function and passes the given ability1   

