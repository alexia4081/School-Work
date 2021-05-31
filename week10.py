#This week we will create a program that performs file processing activities.
# Your program this week will use the OS library in order to validate that a directory
# exists before creating a file in that directory.
# Your program will prompt the user for the directory they would like to save the file
# in as well as the name of the file.
# The program should then prompt the user for their name, address, and phone number.
# Your program will write this data to a comma separated line in a file and store the
# file in the directory specified by the user.

# /Users/alexiadiaz/Desktop
# /Users/alexiadiaz/Documents

import os

def process_request():
    # prompt for directory information
    directory = input("Enter directory path to save data: ")
    is_valid_directory = validate_directory_existence(directory)
    if is_valid_directory:
        file_name = input("Enter file name: ")
        write_date_to_os(directory, file_name)

def validate_directory_existence(directory):
    return os.path.isdir(directory)

def write_date_to_os(directory, file_name):
    with open(os.path.join(directory, file_name), "w") as file1:
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        file1.write("Name: {}, Address: {}, Phone Number: {}"
                    .format(name, address, phone_number))

    # After gathering input display to user for validation purposes
    display_data_to_user(directory, file_name)

def display_data_to_user(directory, file_name):
    with open(os.path.join(directory, file_name), "r") as file1:
        print(file1.read())

process_request()

