# Import the 'subprocess' module and alias it as 'sp' for later use

import subprocess as sp  

def show_battery():
    try:

        # Run the 'acpi' command in the terminal and capture its output as a string
        bat_info = sp.check_output(['acpi'], universal_newlines=True)

        # Extract the battery percentage from the output string by splitting it into parts and selecting the relevant portion
        bat_percentage = bat_info.split(',')[1].split()[0]

        # Print the battery percentage with a descriptive message
        print("Battery Percentage: {}%".format(bat_percentage))
    except sp.CalledProcessError:

        # If the 'acpi' command fails, print an error message indicating that battery information is not available
        print("Battery information not available.")

# Run the battery status program by calling the 'show_battery_status()' function
show_battery()
