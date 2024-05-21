Bash Dating Site

Video Demo: https://youtu.be/uCuAF-T9EeM

Description:

Welcome to the Bash Dating Site! This Python script simulates a simple dating site experience through the command line. This is a simple online dating program designed by BASH.

Feel free to play around with it as you like.

This project was inspired and adapted from the Django web framework.


Prerequisites

Ensure you have the required Python packages installed:
pip install -r requirements.txt

To run the script, use the following command:
python project.py run

Additional Commands to Run Administrative Tasks:

To display a description:
python project.py .desc

To display the database schema:
python project.py .schema

Features

    User registration and login.
    Random selection of potential matches.
    Libraries to enhance fonts with the addition of emojis.
    Text-to-speech functionality for match announcements.

How to Use

    Run the script using the provided command.
    Choose to either register or login.
    Complete the registration process if applicable.
    Select the preference of what you want.
    The script will display a randomly selected potential match.
    Decide whether to choose another match or exit.

Design Choices and Conclusion

The design of the Bash Dating Site was guided by several considerations. The command-line interface was chosen to provide a lightweight and accessible platform for seamless user interaction. The decision to use a Python dictionary as a fake database, instead of an actual database like SQLite, was made to keep the project simple. The inspiration from the Django web framework influenced the project's structure, emphasizing modularity and ease of maintenance.

The incorporation of text-to-speech and emoji libraries enhances the user experience, adding a touch of creativity and accessibility. These features make interactions more engaging and inclusive.

Areas for Improvement:

While the current version offers a functional dating simulation, there are areas that can be improved over time:

    User Interface Enhancement: Consider transitioning to a graphical user interface (GUI) to provide a more visually appealing and user-friendly experience.

    Security Measures: Strengthen security protocols to ensure user data integrity and privacy.

    Algorithm Refinement: Optimize the matching algorithm for better accuracy and personalized recommendations.

    Feature Expansion: Introduce additional features such as chat functionality, profile customization, and advanced search options to enrich the user experience. Additionally, consider using an actual database like SQLite for storing user information, enabling easy retrieval of users information.

In conclusion, the Bash Dating Site project was developed for fun, and its design choices were made to balance simplicity with functionality. As technology evolves, there is ample opportunity to refine and expand upon the current implementation, offering users an even more enjoyable and feature-rich dating simulation experience.

Files

    project.py: Main Python script file.
    registration.py: Contains functions for registration and login.
    views.py: Functions for user input, database checks, and a class to choose a person.
    models.py: Defines the data model and provides functions for selecting matches.
    README.md: Documentation file.
    Test_project.py: Contains test functions on the main function in project.py.
    Requirements.txt: Contains any pip-installable libraries that your project requires listed, one per line.

Acknowledgements

    pyttsx3: Text-to-speech conversion library for Python.
    emoji: Library for handling emojis in Python.
    pyfiglet: Library for creating ASCII art text.
    Inflect: Library for manipulating strings.
    Pytest: Python test library.

License

This program was designed for fun, and the names used are fictional and not in any way related to real-life people.

Copyright remains Bash property. Thanks.
