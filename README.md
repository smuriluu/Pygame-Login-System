# 🔒 Pygame Login System

This repository contains a basic login system developed with Pygame, based on a modular template. The goal of this project is to provide a solid foundation for creating user interface and logic commonly found in login systems, such as user registration, authentication, and integration with APIs and databases.

---

## 🚀 Implemented Features

- **Registration Screen:**
  - Fields for `username`, `password`, and `confirm password`.
  - A button to send data to an API, which performs validations and inserts new users into the database.
- **API Integration:**
  - HTTP requests sent to an API that interacts with a MySQL database hosted on a self-hosted server.
- **Modular Organization:**
  - Clear separation between screen logic, resource loading, and environment configuration.
- **Dynamic Screen Resizing:**
  - UI elements automatically adjust to the window size while maintaining the correct aspect ratio.

---

## 🛠️ Planned Features

- **Registration Validations:**
  - Check if the `username` already exists in the database.
  - Enforce a minimum number of characters for `username` and `password`.
  - Implement password complexity rules (e.g., requiring uppercase letters, numbers, and special characters).
- **Login Screen:**
  - Authenticate existing users.
  - Display success or error messages.
- **Interface Enhancements:**
  - Improve the visual design of screens and add interactive feedback.

---

## 📂 Project Structure

```plaintext
Pygame-Login-System/
│
├── assets/           # Directory for fonts, images, and other resources
│   └── fonts/        # Fonts used in the project
│
├── canvas/           # Screens of the system (e.g., registration, login, home)
│   └── registration.py   # Registration screen
│
├── config/
│   └── settings.json # Configuration file (resolution, audio, etc.)
│
├── scripts/          # Core scripts for the system
│   ├── dotenv.py     # Environment variable management
│   ├── gui.py        # GUI components (buttons, sliders, etc.)
│   ├── screen.py     # Screen management and resizing logic
│   ├── settings.py   # Loading and saving settings
│   ├── sprites.py    # Sprite loading
│   └── assets.py     # Asset loading
│
├── .env              # Environment variables file
├── main.py           # Main script to start the system
├── requirements.txt  # Project dependencies
└── README.md         # Documentation
```

---

## ⚙️ Settings

Project settings are stored in the config/settings.json file.
This file allows customization of various options, such as:

- Screen Resolution
- Language
- Audio Volume
- Other preferences

Example settings.json file:

```json
{
    "video": {
        "width": 1280,
        "height": 720,
        "fps": 0,
        "vsync": 0,
        "show_fps": false
    },
    "language": {
        "language_set": "pt-BR",
        "en-US": {
            "create_account": "Create Account",
            "username": "Username",
            "password": "Password",
            "confirm_password": "Confirm Password",
            "sing_up": "SING UP"
        },
        "pt-BR": {
            "create_account": "Cadastro",
            "username": "Usuário",
            "password": "Senha",
            "confirm_password": "Confirme a Senha",
            "sing_up": "CADASTRAR"
        }
    },
    "audio": {
        "main_volume": 100
    }
}
```

---

## 🖥️ How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/your-username/pygame-login-system.git
cd pygame-login-system
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

---

## ⚠️ Important Note

This project requires your own API to handle user registration and authentication.
The endpoint for the API is not provided in this repository, as the author's self-hosted server has limited hardware resources and cannot handle multiple external requests.

You must set up your own API for the project to function as intended. Ensure the API is capable of handling the following:

- User registration with validation.
- Database integration for storing and retrieving user data.

See more about setting up your own API for this project in my repository: [API](https://github.com/smuriluu/API)