import zipfile  # Importing necessary libraries
import itertools
import sys
import string
import time

def print_large_letter(letter):

    letters = {
        'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
        'M': ["*   *", "** **", "* * *", "*   *", "*   *"],
        'I': ["*****", "  *  ", "  *  ", "  *  ", "*****"]
    }
    
    for line in range(5):
        for char in letter:
            print(letters[char][line], end="  ")
        print()
print_large_letter("AMI")


# Function to check password for a zip file
def check_zip_password(zip_path, possible_characters, password_length):
    zip_ref = zipfile.ZipFile(zip_path)  # Opening the zip file
    
    # Loop through different password lengths
    for length in range(1, password_length + 1): 
        # Generate combinations of characters for password attempts
        for attempt in itertools.product(possible_characters, repeat=length):
            password = ''.join(attempt).encode('utf-8')  # Encoding the password
            
            try:
                start_time = time.time()        # Start recording
                # Try to extract the zip file using the current password attempt
                zip_ref.extractall(pwd=password)
                zip_ref.close()                 
                end_time = time.time()          # End recording 
                print(f" [+] Time taken - {end_time-start_time}")   # Printing the time taken
                return f" [+] Password found - {''.join(attempt)}"  # If successful, return the password
                
            except Exception as e:
                pass  # If extraction fails, continue to the next attempt
    zip_ref.close()
    return " [-] Password not found"  # Return if password is not found within specified length

# Get the zip file path as a command line argument
zip_file_path = sys.argv[1]

# Define character sets for the password
lett = string.ascii_letters
num = string.digits
everything = lett + num + '_'

# Get user input for the length of the password to check
password_length_to_check = int(input("\n [+] Length of your password - "))  # Length of the password 
                                                                            # needed to calculate the time taken

# Call the function to check the zip file password and print the result
result = check_zip_password(zip_file_path, everything, password_length_to_check)
print(result)