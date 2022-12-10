import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a function to convert a string to binary
def to_binary(string):
  # Initialize an empty list to hold the binary values
  binary_values = []

  # Loop through each character in the string
  for char in string:
    # Convert the character to its ASCII value and convert that to binary
    binary_values.append(bin(ord(char)))

  # Join the binary values into a single string and return it
  return ' '.join(binary_values)

# Create a text field to enter the plain text
text_field = tk.Entry(root)
text_field.pack()

# Create a button that, when clicked, will convert the plain text to binary
convert_button = tk.Button(root, text="Convert to Binary", command=lambda: print(to_binary(text_field.get())))
convert_button.pack()

# Start the GUI event loop
root.mainloop()
