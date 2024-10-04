import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypt the email by shifting the alphabetic part by 3 ASCII values.

    Args:
        email (str): A 6-character string with 3 letters followed by 3 digits.

    Returns:
        str: The encrypted email or an error message if validation fails.
    """
    output = "" 
    # Check if the length of the email is 6 characters
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
    Decrypt the email by shifting the alphabetic part down by 3 ASCII values.

    Args:
        email (str): A 6-character string with 3 letters followed by 3 digits.

    Returns:
        str: The decrypted email or an error message if validation fails.
    """
    output = "" 
    # Check if the length of the email is 6 characters
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
