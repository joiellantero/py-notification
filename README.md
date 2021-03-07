# Notification Alert Program

A Python program that sends notifications to your email and phone number

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## 🚀 Quickstart

1. Clone repository
    ```bash
    git clone https://github.com/joiellantero/notification.git
    ```

2. Navigate to the project directory


3. Setup your environment variables in ~/.bash_profile 
   ```bash
    vim ~/.bash_profile
    ```
   > Click [here](#-alternative) if you don't have bash.

   > In this step you can open bash_profile using your favorite code editor by replacing `vim` with `code` (VSCode) or `atom` (Atom)

4. Add your email credentials
   ```bash
    export EMAIL_CLIENT="youremail@email.com"
    export EMAIL_CLIENT_APP_PASSWORD="yourcomplexpassword"
    ```
   > You may need to setup your email to obtain your app password.

    > Click [here](https://support.google.com/accounts/answer/185833?hl=en) to learn how to obtain your app password.

5. Test the program
    ```bash
    python3 notification.py
    ```

## 🛠 Alternative 

- Using `.env` instead of `~/.bash_profile`
    1. Create a `.env` file
        ```bash
        touch .env
        vim .env
        ```

    2. Enter your credentials in the `.env` file
       ```bash
        export EMAIL_CLIENT="youremail@email.com"
        export EMAIL_CLIENT_APP_PASSWORD="yourcomplexpassword"
        ```

        > You may need to setup your email to obtain your app password.

        > Click [here](https://support.google.com/accounts/answer/185833?hl=en) to learn how to obtain your app password.

    3. Run `notification2.py` since this is setup to read the `.env`
        ```bash
        python3 notification2.py
        ```

## 👨‍💻 Author

- [Joie Llantero](https://joiellantero.codes/)


## 📄 License 

- [MIT license](http://opensource.org/licenses/mit-license.php)