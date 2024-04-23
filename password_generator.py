import random
import string

class PasswordGenerator:
  def generate_password(self):
    """
    Generates a secure password
    Args: 
      None
    Returns:
      secure password (string)
    """
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) #k = length
    return password
  def save_password_to_file(self, password, filename):
    """
    Creates a file to save the password to
    Args:
      password (string) - the user inputed password
      filename (string) - the name of the file to be created
    Returns:
      file with password
    """
    pass
  def check_password_strength(self, password):
    """
    Ensures that the password is strong
    Args: 
      password (string) - the user's password
    Returns:
      True/False (boolean) - returns True if the password is strong or False if it is not 
    """
    pass

  def generate_passphrase_based_on_word(self, word):
    """
    Creates a passphrase (string of words) based on a word given by the user
    Args:
      word (string) - the user's inputed key word
    Returns:
      passphrase (string)
    """
    pass

  def character_substitution(self, password):
    """
    Substitute characters in the given password
    Args:
      password (string) - the user's given password
    Returns:
      character substituted password (string)
    """
    pass

  def encrypt_password(self, password):
    """
    Encrypts the password with MD5 
    Args:
      password (string) - the user's given password
    Returns:
      encrypted password (string)
    """
    pass

  def decrypt_password(self, passwordEncrypted):
    """
    Decrypts password (assuming it was encrypted with MD5)
    Args:
      passwordEncrypted (string) - encrypted password
    Returns:
      decrypted password (string)
    """
    pass 

