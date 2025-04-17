import os
import pandas as pd

current_dir = os.getcwd() # Get the current directory
print(current_dir)
file_path = os.path.join(current_dir, 'datasets')

# Print the file path
print(file_path)