import pytest
import logging
from src.c_cipher import encrypt, decrypt

# Multi-line comment moved here
# Consider the following input emails
# “aef345”
# “def4%6”
# “ ” (single space)

def test_kick_the_front_tire():
    assert encrypt() == 'dbc012'

def test_encrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd1234")
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."
    
def test_encrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abc1@3")
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_encryption(caplog):
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    assert result == "def345"
    assert "def345" not in caplog.text 

# Additional tests for decrypt function

def test_decrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = decrypt("defg456")  # Invalid email with length greater than 6
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_decrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = decrypt("def4%6")  # Invalid format with a special character
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_single_space_email(caplog):
    """Test that a single space as email triggers length check error"""
    with caplog.at_level(logging.INFO):
        result = decrypt(" ")  # Single space email input
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_successful_decryption(caplog):
    """Test that the email is decrypted correctly"""
    result = decrypt("def345")
    assert result == "abc012"
    assert "abc012" not in caplog.text

# Commented out test for back tire as requested
# def test_kick_the_back_tire():
#     assert decrypt() == 'aef345'
