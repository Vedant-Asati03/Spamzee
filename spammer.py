from termcolor import colored
from AppOpener import run
import smtplib
import ssl
import pyautogui
import time


def open_app(x):
    '''Opens app'''
    run(x)


def search(y):
    '''Searches from contacts'''
    time.sleep(1)
    pyautogui.write(y)
    pyautogui.press('Enter')


def spamit(z):
    '''Spams in the chat'''
    pyautogui.write(z)
    pyautogui.press('Enter')


if __name__ == '__main__':
    print(
        colored(
            '\n\n===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===\n',
            'cyan',
        )
    )
    print(
        colored(
            '                                                                            SPAMZEE                             ',
            'cyan',
            attrs=['bold'],
        )
    )
    print(
        colored(
            '\n===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===\n\n',
            'cyan',
        )
    )

    spam = input(colored('|What you want to spam| : ', 'yellow')).capitalize()

    whom = input(
        colored('|Who do you want to spam/ email_id| : ', 'yellow')).capitalize()

    if not '@gmail.com' in whom:
        where = input(
            colored('|Where do you want to spam| : ', 'yellow')).capitalize()

        while True:

            try:
                count = int(
                    input(colored('|How many times|: ', 'yellow'))
                )

                if 'Telegram' in where:
                    print(colored('\nSpamming in Telegram...\n', 'blue'))
                    open_app('Telegram')
                    search(whom)
                    spamit(spam)

                elif 'Whatsapp' in where:
                    print(colored('\nSpamming in Whatsapp...\n', 'blue'))
                    open_app('Whatsapp')
                    time.sleep(5)
                    search(whom)
                    time.sleep(4)
                    spamit(spam)

                elif 'Others' in where:
                    print(colored(
                        'Put your cursor where you want to spam,\nSpamming will start in 10 seconds...', 'blue'))
                    time.sleep(10)
                    spamit(spam)

                else:
                    pass

                for _ in range(count - 1):
                    pyautogui.write(spam)
                    pyautogui.press('Enter')

                print(colored('\nSpam sent!\n', 'cyan', attrs=['bold']))
                break

            except ValueError:
                print(
                    colored('\nNote: Enter a number, please!\n',
                            'red', attrs=['underline'])
                )
                continue

    elif '@gmail.com' in whom:
        counts = int(input(colored('|How many times|: ', 'yellow')))
        print(colored('\nSpamming through Email...\n', 'blue'))
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login('your_email id',
                         'your_server')
            for i in range(counts):
                server.sendmail('your_email id',
                                whom, spam)
            print(colored('\nSpam sent!\n', 'cyan', attrs=['bold']))
            exit()

        except Exception as e:
            print(e)
    else:
        pass
