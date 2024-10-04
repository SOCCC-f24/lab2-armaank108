import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypts the input email by shifting the first three letters up by 3 in ASCII.

    Args:
        email (str): The email to encrypt. Expected format is 3 letters followed by 3 digits (e.g., 'abc012').

    Returns:
        str: The encrypted email if the input is valid, otherwise an error message.
    """
    output = "" 
    len_flag = len(email) != 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Validate 3 letters + 3 digits

    if len_flag:  # Check if length is exactly 6 characters
        output = "Length check failed\nEmail must be 6 characters long."
        logging.info(output)
        return output

    if anum_flag:  # Check for valid format (3 letters + 3 digits)
        output = "alpha num check failed\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output

    # Process the email into a list and shift each letter up by 3 in ASCII
    email_lst = list(email)
    for i in range(3):  # Shift the first three letters (indices 0-2)
        email_lst[i] = chr(ord(email_lst[i]) + 3)

    # Join the list back into a string
    email_str = ''.join(email_lst)
    retVal = email_str
    return retVal

def decrypt(email="def345"):
    """
    Decrypts the input email by shifting the first three letters down by 3 in ASCII.

    Args:
        email (str): The email to decrypt. Expected format is 3 letters followed by 3 digits (e.g., 'def345').

    Returns:
        str: The decrypted email if the input is valid, otherwise an error message.
    """
    output = "" 
    len_flag = len(email) != 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Validate 3 letters + 3 digits

    if len_flag:  # Check if length is exactly 6 characters
        output = "Length check failed\nEmail must be 6 characters long."
        logging.info(output)
        return output

    if anum_flag:  # Check for valid format (3 letters + 3 digits)
        output = "alpha num check failed\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output

    # Process the email into a list and shift each letter down by 3 in ASCII
    email_lst = list(email)
    for i in range(3):  # Shift the first three letters (indices 0-2)
        email_lst[i] = chr(ord(email_lst[i]) - 3)

    # Join the list back into a string
    email_str = ''.join(email_lst)
    retVal = email_str
    return retVal
