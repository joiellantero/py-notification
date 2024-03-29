# Notification Alert Program

A Python program that sends notifications to your email and phone number

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## 🚀 Quickstart

1. Clone repository
    ```shell
    $ git clone https://github.com/joiellantero/notification.git
    ```

2. Navigate to the project directory


3. Setup your environment variables in ~/.bash_profile 
   ```shell
    $ vim ~/.bash_profile
    ```
   > Click [here](#-alternative) if you don't have bash.

   > In this step you can open bash_profile using your favorite code editor by replacing `vim` with `code` (VSCode), `atom` (Atom), etc.

4. Add your email credentials
   ```shell
    export EMAIL_CLIENT="youremail@email.com"
    export EMAIL_CLIENT_APP_PASSWORD="yourcomplexpassword"
    ```
    > Don't forget to setup your email to obtain your app password. Click [here](https://support.google.com/accounts/answer/185833?hl=en) to learn how to obtain your app password.

5. Run the program
    ```shell
    $ python3 notification.py
    ```
6. Star this repo if you like it!

## 🛠 Alternative 

- Using `.env` instead of `~/.bash_profile`
    1. Create a `.env` file
        ```shell
        $ touch .env
        $ vim .env
        ```

    2. Enter your credentials in the `.env` file
       ```shell
        export EMAIL_CLIENT="youremail@email.com"
        export EMAIL_CLIENT_APP_PASSWORD="yourcomplexpassword"
        ```

        > You may need to setup your email to obtain your app password. Click [here](https://support.google.com/accounts/answer/185833?hl=en) to learn how to obtain your app password.

    3. Install the dependency
        ```shell
        $ pip install python-dotenv
        ```

    4. Run `notification2.py` since this is set up to read the `.env`
        ```shell
        $ python3 notification2.py
        ```

## 📱 Mobile Notifications

1. Replace the email address passed in the function call
    ```python
    email_alert("this is my subject", "1234567890@txt.att.net", "this is my body")
    ```
    > The SMS gateway domain depends on your carrier. Visit this [link](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/) to learn more.

## 👨‍💻 Author

- [Joie Llantero](https://github.com/joiellantero)


## 📄 License 

- [MIT license](http://opensource.org/licenses/mit-license.php)
