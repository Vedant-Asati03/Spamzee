"""
spams lol
"""

import smtplib
import time
import json
import ssl
import sys
import pyautogui
import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text
from AppOpener import run as open_app


def get_credentials() -> dict[str, str]:
    """
    Gets email and password from the credentials.json file.
    """
    fpath = "./credentials.json"
    with open(fpath, encoding="utf-8") as credentials_file:
        content = json.load(credentials_file)
        return content


def search(contact_name):
    """
    Searches from contacts
    """
    time.sleep(1)
    pyautogui.write(contact_name)
    pyautogui.press("Enter")


def spamit(spam_text):
    """
    Spams in the chat
    """
    pyautogui.write(spam_text)
    pyautogui.press("Enter")


if __name__ == "__main__":
    console = Console()
    figlet_text = pyfiglet.figlet_format("S P A M Z E E", font="standard")
    styled_text = Text(figlet_text, style="bold #5f00d7 i")
    aligned_text = Align(styled_text, align="center")

    console.print(aligned_text)

    spam = console.input(
        Text("|What you want to spam| : ", style="#00ABB3")
    ).capitalize()

    whom = console.input(
        Text("|Whom do you want to spam/ email_id| : ", style="#00ABB3")
    ).capitalize()

    where = console.input(
        Text("|Where do you want to spam| : ", style="#00ABB3")
    ).capitalize()

    while True:

        try:
            count = int(console.input(Text("|How many times| : ", style="#00ABB3")))

            if "Telegram" in where:
                console.print(
                    "\nSpamming in [bold u yellow]Telegram[bold u yellow]",
                    style="#B2B2B2",
                )
                open_app("Telegram")
                search(whom)
                spamit(spam)

            elif "Whatsapp" in where:
                console.print(
                    "\nSpamming in [bold u yellow]Whatsapp[bold u yellow]",
                    style="#B2B2B2",
                )
                open_app("Whatsapp")
                time.sleep(5)
                search(whom)
                time.sleep(4)
                spamit(spam)

            elif "Email" in where:
                context = ssl.create_default_context()

                try:
                    credentials = get_credentials()
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    email = credentials["email"]
                    password = credentials["password"]
                    server.login(email, password)
                    for i in range(count):
                        server.sendmail(email, whom, spam)
                    console.print("\nSpam sent!\n", style="bold green i")
                    sys.exit()

                except Exception as e:
                    print(e)

            elif "Others" in where:
                print(
                    (
                        "Put your cursor where you want to spam,\nSpamming will start in 10 seconds...",
                        "blue",
                    )
                )
                time.sleep(10)
                spamit(spam)

            else:
                pass

            for _ in range(count - 1):
                pyautogui.write(spam)
                pyautogui.press("Enter")

            console.print("\nSpam sent!\n", style="bold green i")
            break

        except ValueError:
            console.print(
                "\n[bold u]Note[bold u]: Enter a number, please!\n", style="red"
            )
            continue

    else:
        pass
