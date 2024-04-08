import tkinter as tk
from tkinter import ttk
from password_generator import PasswordGenerator

class PasswordGeneratorGUI:
  def __init__(self, root):
    """
    Creates the initial GUI 
    Args:
      root (Tk) - the main window all items will be in
    Returns:
      None
    """

  def generate_password(self):
    """
    Generates a random password using the PasswordGenerator class
    Args:
        self (PasswordGeneratorGUI): The current instance of the PasswordGeneratorGUI class.
    Returns:
        None  
    """

def create_gui():
  """
  Initializes the GUI window
  Args: 
    None
  Returns:
    None
  """
  root = tk.Tk()
  app = PasswordGeneratorGUI(root)
  root.mainloop()
