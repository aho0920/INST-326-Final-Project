import tkinter as tk
from password_generator import PasswordGenerator

class PasswordGeneratorGUI:
  # Driver: Emani
  # Navigator: Diana
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
    self.label = tk.Label(self.root, text="Generated Password:")
    self.label.pack()

    # Entry for password display
    self.password = ""
    self.password_entry = tk.Entry(self.root, width=30, state="readonly")
    self.password_entry.pack()

    # Generate Button
    self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
    self.generate_button.pack()

    # Copy button 
    self.copy_button = tk.Button(self.root, text = "Copy Password", command= self.copy_password)
    self.copy_button.pack()

    # Entry for password strength
    self.password_strength_Label = tk.Label(self.root, text="Enter password to evalute strength:")
    self.password_strength_Label.pack()
    
    self.password_strength_var = tk.StringVar()  # Variable to hold the entered password
    self.password_strength_entry = tk.Entry(self.root, width=10, textvariable=self.password_strength_var)
    self.password_strength_entry.pack()

    self.password_strength_button = tk.Button(self.root, text="Check Strength", command=self.check_password_strength)
    self.password_strength_button.pack()

    # Label for password strength feedback
    self.strength_label = tk.Label(self.root, text="")
    self.strength_label.pack()

    # Character substitution 
    self.sub_pass = ""
    self.char_sub_label = tk.Label(self.root, text="Enter password for character substitution:")
    self.char_sub_label.pack()
    
    self.char_sub_var = tk.StringVar()  # Variable to hold the entered password
    self.char_sub_entry = tk.Entry(self.root, width=10, textvariable=self.char_sub_var)
    self.char_sub_entry.pack()

    self.char_sub_button = tk.Button(self.root, text="Substitute Characters", command=self.char_sub)
    self.char_sub_button.pack()
    self.char_sub_return = tk.Label(self.root, text="")
    self.char_sub_return.pack()
    
    # Copy button for substituted characters
    self.copy_char_button = tk.Button(self.root, text = "Copy Substituted Characters", command= self.copy_char_sub)
    self.copy_char_button.pack()

    # Passphrase button
    self.passphrase_num_var = tk.StringVar()
    self.passphrase_label = tk.Label(self.root, text = "Input the number of words for passphrase")
    self.passphrase_label.pack()
    vcmd = root.register(self.on_validate)
    self.passphrase_entry = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'), textvariable = self.passphrase_num_var)
    self.passphrase_entry.pack()
    self.passphrase_button = tk.Button(self.root, text = "Create Passphrase", command =self.passphrase)
    self.passphrase_button.pack()
    self.passphrase_return = tk.Label(self.root, text="")
    self.passphrase_return.pack()
    
    # Copy passphrase
    self.copy_passphrase_button = tk.Button(self.root, text="Copy Passphrase", command = self.copy_passphrase)
    self.copy_passphrase_button.pack()

  def generate_password(self):
    # Driver: Makachi
    # Navigator: Andrew
    """
    Calls the PasswordGenerator class to generate a password
    Args:
        None
    Returns:
        None
    """
    self.password = self.password_generator.generate_password()
    self.password_entry.config(state="normal")
    self.password_entry.delete(0, "end")
    self.password_entry.insert(0, self.password)
    self.password_entry.config(state="readonly")
  
  def copy_password(self):
    # Driver: Diana
    # Navigator: Makachi
    """
    copies the password to user's clipboard
    Args:
      None
    Returns:
      None
    """
    self.root.clipboard_clear()
    self.root.clipboard_append(self.password)
    self.root.update()

  def check_password_strength(self):
    # Driver: Diana
    # Navigator: Makachi
    """
    Calls the password generator class to check password strength
    Args:
      None
    Returns:
      None
    """
    strength = self.password_generator.check_password_strength(self.password_strength_var.get())
    if strength:
        self.strength_label.config(text="Password strength: Strong", foreground="green")
    else:
        self.strength_label.config(text="Password strength: Weak", foreground="red")

  def char_sub(self):
    # Driver: Makachi
    # Navigator: Emani
    """
    Calls the password generator class to substitute characters of the given password
    Args:
      None
    Returns:
      None
    """
    self.sub_pass = self.password_generator.character_substitution(self.char_sub_var.get())
    self.char_sub_return.config(text = self.sub_pass)

  def copy_char_sub(self):
    # Driver: Andrew
    # Navigator: Diana
    """
    Copies the substituted character string to user's clipboard
    Args:
      None
    Returns:
      None
    """
    self.root.clipboard_clear()
    self.root.clipboard_append(self.sub_pass)
    self.root.update()

  def validate_input(self,text):
    # Driver: Emani
    # Navigator: Andrew
    """
    Ensures that the user inputed text is an integer
    Args:
      text (str) - user inputed string to be checked
    Returns:
      True/False (boolean) - depending on if the given text is an integer or not. 
    """
    pass
    
  def on_validate(self,P):
    # Driver: Emani
    # Navigator: Diana
    """
    Alerts the user if the inputed text is not an integer
    Args:
      P(str) - user inputed string 
    Returns:
      True/False(boolean) - returns True if the string is an integer and False to alert for invalid input
    """
    pass
    
  def passphrase(self):
    # Driver: Andrew
    # Navigator: Makachi
    """
    Calls the password generator class to create the passphrase string
    Args:
      None
    Returns:
      None
    """
    self.passphrase = self.password_generator.generate_passphrase(self.passphrase_num_var.get())
    self.passphrase_return.config(text = self.passphrase)

  def copy_passphrase(self):
    # Driver: Diana
    # Navigator: Emani
    """
    Copies the passphrase string to user's clipboard
    Args:
      None
    Returns:
      None
    """
    self.root.clipboard_clear()
    self.root.clipboard_append(self.passphrase)
    self.root.update()

def create_gui():
  # Driver: Makachi
  # Navigator: Andrew
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
