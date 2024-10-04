import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Shifts the first three alphabetic characters of the input string up by 3 ASCII values
    to "encrypt" the email string.

    The function takes a 6-character alphanumeric string (3 letters followed by 3 digits).
    It validates the length and format of the input, ensuring it consists of exactly 3 letters
    followed by 3 digits. If the validation fails, a descriptive error message is returned.
    If the input is valid, the first three letters are shifted up by 3 ASCII values, leaving
    the digits unchanged.

    Args:
        email (str): A 6-character alphanumeric string (3 letters followed by 3 digits).
                     Default value is 'abc012'.

    Returns:
        str: The "encrypted" email string with the letters shifted up by 3, or an error message
             if the input does not meet the validation requirements.
             For example, if input is 'abc012', the return value will be 'dbc012'.
    """
    output = "" 
    len_flag = len(email) != 6
    
    # Check if the first part is alphabetic and the second part is numeric
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) 

    # Input validation for length
    if len_flag:                         
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    
    # Input validation for alphanumeric structure
    if anum_flag:                        
        output = "Alphanumeric check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # Convert the email string into a list of characters
    email_lst = list(email)
        
    # Shift the first three characters (letters) up by 3 ASCII values
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) + 3)

    # Convert the list of characters back into a string
    email_str = ''.join(email_lst)

    # Return the processed (encrypted) string
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    Reverses the "encryption" by shifting the first three alphabetic characters of the input
    string down by 3 ASCII values to "decrypt" the email string.

    The function takes a 6-character alphanumeric string (3 letters followed by 3 digits).
    It validates the length and format of the input. If the input is valid, the first three
    letters are shifted down by 3 ASCII values, leaving the digits unchanged. This reverses
    the effect of the `encrypt` function.

    Args:
        email (str): A 6-character alphanumeric string (3 letters followed by 3 digits).
                     Default value is 'def345'.

    Returns:
        str: The "decrypted" email string with the letters shifted down by 3, or an error message
             if the input does not meet the validation requirements.
             For example, if input is 'def345', the return value will be 'abc345'.
    """
    output = "" 
    len_flag = len(email) != 6
    
    # Check if the first part is alphabetic and the second part is numeric
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) 

    # Input validation for length
    if len_flag:                         
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    
    # Input validation for alphanumeric structure
    if anum_flag:                        
        output = "Alphanumeric check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   
    
    # Convert the email string into a list of characters
    email_lst = list(email)
    
    # Shift the first three characters (letters) down by 3 ASCII values
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) - 3)

    # Convert the list of characters back into a string
    email_str = ''.join(email_lst)

    # Return the processed (decrypted) string
    retVal = email_str
    return retVal

# Example tests
if __name__ == "__main__":
    encrypted = encrypt("abc012")
    print(f"Encrypted: {encrypted}")  # Expected output: 'dbc012'
    
    decrypted = decrypt("def345")
    print(f"Decrypted: {decrypted}")  # Expected output: 'abc345'
