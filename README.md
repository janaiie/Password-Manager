Password Manager
Overview

This project is a password manager application developed using Tkinter for the graphical user interface. It allows users to securely manage their credentials and generate strong passwords. Please note that this project is still under development, and some features, such as password storage, are not yet fully secure.

Live Demo
Live Demo (Coming soon)

Features
    Password Generator: Generates secure, random passwords to enhance security.
    Credentials Storage: Stores website credentials in a JSON format with email as the key and password as the value.

Current Limitations
    Plaintext Storage: Currently, passwords are stored in plaintext. This is a temporary measure and will be addressed in future updates to enhance security.
    Ongoing Development: This project is still being worked on. Future updates will include encrypted storage and additional features.

How It Works
    Password Generation:
        The password generator can create secure, random passwords based on user-defined criteria.
        The generated passwords are designed to be strong and difficult to guess.

    Credentials Management:
        User credentials are stored in a JSON file with the following format:

    {
      "user@example.com": "password123",
      "anotheruser@example.com": "securepassword!"
    }

    Each entry consists of an email as the key and the corresponding password as the value.

User Interface:

    Tkinter GUI: Provides a simple and intuitive interface for managing passwords and using the password generator.
