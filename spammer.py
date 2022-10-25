from termcolor import colored
from AppOpener import run
import pyautogui
import time


def open_app(x):
    """This function opens app"""
    run(x)


def search(y):
    """This function searches from contacts"""
    time.sleep(0.5)
    pyautogui.write(y)
    pyautogui.press("Enter")


def spamit(z):
    """This function spams in the chat"""
    pyautogui.write(z)
    pyautogui.press("Enter")


if __name__ == "__main__":
    print(
        colored(
            "\n\n===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===\n",
            "cyan",
        )
    )
    print(
        colored(
            "                                                                            SPAMMER                             ",
            "cyan",
            attrs=["bold"],
        )
    )
    print(
        colored(
            "\n===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===\n\n",
            "cyan",
        )
    )

    spam = input(colored("|What you want to spam| : ", "yellow")).capitalize()

    whom = input(colored("|Who do you want to spam| : ", "yellow")).capitalize()

    where = input(colored("|Where do you want to spam| : ", "yellow")).capitalize()

    while True:

        try:
            no_of_times = int(
                input(colored("|How many times|: ", "yellow"))
            )

            if where == "Telegram":
                print(colored("\nSpamming in Telegram...\n", "blue"))
                open_app("Telegram")
                search(whom)
                spamit(spam)

            elif where == "Whatsapp":
                print(colored("\nSpamming in Whatsapp...\n", "blue"))
                open_app("Whatsapp")
                time.sleep(4)
                search(whom)
                time.sleep(3)
                spamit(spam)

            elif where == "Sms":
                print(colored("\nSpamming through SMS...\n", "blue"))
                open_app("Phone Link")
                time.sleep(5)
                pyautogui.press("Enter")
                search(whom)
                time.sleep(5)
                spamit(spam)

            else:
                pass

            for _ in range(no_of_times - 1):
                pyautogui.write(spam)
                pyautogui.press("Enter")

            print(colored("\nSpam sent!\n", "cyan", attrs=["bold"]))
            break

        except ValueError:
            print(
                colored("\nNote: Enter a number, please!\n", "red", attrs=["underline"])
            )
            continue
