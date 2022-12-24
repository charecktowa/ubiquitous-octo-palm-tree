import pywhatkit
import phonenumbers

from chatgpt_wrapper import ChatGPT


def validate_number(number):
    number = number.replace(" ", "")

    return phonenumbers.is_valid_number(phonenumbers.parse(number))


def send_message(number: str, message: str, hour: int = -1, minute: int = -1):
    if validate_number(number):
        try:
            if hour == -1 and minute == -1:
                pywhatkit.sendwhatmsg_instantly(number, message, True)
            else:
                pywhatkit.sendwhatmsg(
                    phone_no=number,
                    message=message,
                    time_hour=hour,
                    time_min=minute,
                )
            print("Message sent successfully")
        except Exception as e:
            print(e)


def generate_message_from_gpt(gpt_input: str) -> str:
    bot = ChatGPT()
    return bot.ask(gpt_input)


def main():

    number = ""

    gpt_input = """
    Escribe un mensaje algo extenso deseando una feliz Navidad a Luis de parte de Andrea, en el mensaje incluye buenos deseos, escribe el mensaje de manera informal como si fuera enviado por iMessage usando emojis
    """

    message = generate_message_from_gpt(gpt_input)

    send_message(number, message)


if __name__ == "__main__":
    main()
