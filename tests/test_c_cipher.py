import pytest
import logging
from src.c_cipher import encrypt, decrypt



def test_encrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd1234")  # Too long
    assert "Length check failed" in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_encrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abc1@3")  # Invalid character '@'
    assert "alpha num check failed" in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_encryption():
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    assert result == "def345"  # Correct result for encryption

def test_decrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = decrypt("defg456")  # Too long
    assert "Length check failed" in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_decrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = decrypt("def4%6")  # Invalid character '%'
    assert "alpha num check failed" in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_decryption():
    """Test that the email is decrypted correctly"""
    result = decrypt("def345")
    assert result == "abc012"  # Correct result for decryption
