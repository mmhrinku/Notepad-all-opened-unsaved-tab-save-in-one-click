import os
from Npp import notepad, editor

# Define the folder to save files
# you must cnage your location for default folder whre your unsaved tabs will be saved  put your folder location
output_folder = r"C:\Users\neo\OneDrive\Documents\notepad_output"

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Counter for unsaved tabs
unsaved_count = 0

# Debugging: Log start
notepad.messageBox("Starting tab scan...", "Debug")

# Get all open tabs
buffers = notepad.getFiles()

# Iterate through all tabs using their index
for index, buffer in enumerate(buffers):
    file_path = buffer[2]  # Get the file path

    # Check if the file is unsaved
    if isinstance(file_path, int) or not file_path:
        unsaved_count += 1
        # Activate the tab by view and index
        notepad.activateIndex(0, index)  # View 0 is the primary view
        # Get the content of the unsaved tab
        content = editor.getText()
        # Save it to the output folder
        file_name = "{}.txt".format(unsaved_count)
        file_save_path = os.path.join(output_folder, file_name)
        with open(file_save_path, 'w') as f:
            f.write(content)
        print("Saved tab as: {}".format(file_save_path))

# Show results
if unsaved_count == 0:
    notepad.messageBox("No unsaved tabs found! Check the console for details.", "Info")
else:
    notepad.messageBox("Saved {} unsaved tabs to {}.".format(unsaved_count, output_folder), "Success")
