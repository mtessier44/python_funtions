# Opening our text file in read only
# mode using the open() function
with open(r'C:\Users\micka\Desktop\test2.csv', 'r') as file:
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()

    # Searching and replacing the text
    # using the replace() function


def am_to_eur(data_in):
    data_in = data_in.replace(",", ";")
    data_in = data_in.replace(".", ",")
    return data_in


def eur_to_am(data_in):
    data_in = data_in.replace(",", ".")
    data_in = data_in.replace(";", ",")
    return data_in


data = eur_to_am(data)
#data = am_to_eur(data)

# Opening our text file in write only
# mode to write the replaced content
with open(r'C:\Users\micka\Desktop\export.csv', 'w') as file:
    # Writing the replaced data in our
    # text file
    file.write(data)