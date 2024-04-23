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
    self.root = root
    self.root.title("Password Generator")

    self.password_generator = PasswordGenerator()

    # Label
    self.label = ttk.Label(self.root, text="Generated Password:")
    self.label.pack()

    # Entry for password display
    self.password_entry = ttk.Entry(self.root, width=30, state="readonly")
    self.password_entry.pack()

    # Generate Button
    self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
    self.generate_button.pack()

    # Save Button
    self.generate_button = ttk.Button(self.root, text="Save Password to File", command=self.save_password_file)
    self.generate_button.pack()

  def generate_password(self):
    """
    Generates a random password using the PasswordGenerator class
    Args:
        self (PasswordGeneratorGUI): The current instance of the PasswordGeneratorGUI class.
    Returns:
        None
    """
    password = self.password_generator.generate_password()
    self.password_entry.config(state="normal")
    self.password_entry.delete(0, "end")
    self.password_entry.insert(0, password)
    self.password_entry.config(state="readonly")
  
  def save_password_file(self):
    filesave = self.password_generator.save_password_to_file()


  # ADD OTHER METHODS FOR OTHER POSSIBLE ACTIONS

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