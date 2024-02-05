from email.message import EmailMessage
import ssl, smtplib, qrcode, string, random
import urllib.request as urllib
from PIL import Image

print(
        """
    Operations you can perform:
        1 - Email sender
        2 - Word replecement
        3 - Email Slicer
        4 - Binary search
        5 - Quiz
        6 - QR Code Generator
        7 - Password Generator
        8 - Dice Rolling Simulator
        9 - Sice Conectivity Checker
        10 - Rock/Paper/Scissors
        11 - Image Resizer
        12 - Exit 
        """
    )
while True:
    choice = int(input(f"Enter the number of operation u want to do: "))

    if choice == 1:
        email_sender = input("Enter your email")  # twój email
        email_password = input(
            "Enter your verification key:"
        )  # google settings ---> weryfikacja dwuetapowa
        email_receiver = input(
            "Enter where you want to send it: "
        )  # email docelowy "temp-mail.org"

        subject = input("Enter the subject")  # temat
        body = input("Enter the message: ")  # Wiadomość

        em = EmailMessage()  # lista
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    elif choice == 2:

        def replace_word():
            sentence = input("Enter the sentence: ")
            word_to_replace = input("Enter the word to replace: ")
            word_replacement = input("Enter the word replacement: ")
            print(
                sentence.replace(word_to_replace, word_replacement)
            )  # funkcja .replace(jaki wyraz zmieniamy, na co zmieniamy)

        replace_word()

    elif choice == 3:

        def Slicer():
            print("Welcome in email slicer")
            email = input("Enter your email: ")

            # split dzieli wyrażenie na dwa
            (adres, domain) = email.split("@")
            (domain, extension) = domain.split(".")

            print("adres: ", adres)
            print("domain: ", domain)
            print("extension: ", extension)

        Slicer()

    elif choice == 4:
        # Wyszukiwanie binarne to sprawdzanie czy element znajduje sie mniejszej czy wiekszej polowie listy i tak do odnalezienia elementu
        # warunek: start <= end & liczby ustawione pokolei

        def binary_search(list, element):
            # indeksy
            middle = 0
            start = 0
            end = len(list)
            steps = 0

            while start <= end:
                print("Step", steps, ":", str(list[start : end + 1]))

                steps = steps + 1
                middle = (start + end) // 2

                if element == list[middle]:
                    return middle
                if element < list[middle]:
                    end = middle - 1
                else:
                    start = middle + 1

            return -1
        list = []
        numbers = int(input("How many elements do you want to add to the list?: "))
        for i in range(numbers):
            number = int(input(f"Enter the {i+1} number: "))
            list.append(number)
        element = int(input("Enter the number you want to find: "))
        binary_search(list, element)

    elif(choice == 5):
        Dict = {
        "question1": {
            "question": "What is capital of Germany?: ",
            "answer": "Berlin"
        },
        "question2": {
            "question": "What is capital of Poland: ",
            "answer": "Warsaw"
        },
        "question3": {
            "question": "What is capital of Spain: ",
            "answer": "Madrid"
        },
        "question4": {
            "question": "What is capital of France: ",
            "answer": "Paris"
        },
        "question5": {
            "question": "What is capital of Portugal: ",
            "answer": "Lisbon"
        },
        "question6": {
            "question": "What is capital of Italy: ",
            "answer": "Roma"
        },
        "question7": {
            "question": "What is capital of Netherland: ",
            "answer": "Amsterdam"
        },
        }
        score = 0

        for value, key in Dict.items():
            print(key["question"])
            answer = input("podaj odpowiedź: ")

            if answer.lower() == key["answer"].lower():
                score = score + 1
                print("poprawna odpowiedź")
            else:
                score = score
                print("Niestety, poprawna odpowiedź to ", key["answer"])

        print("your final score:", score)
        print("Your percentage is " + str(int(score/7 * 100)) + "%")

    elif choice == 6:
        def generate_qrcode(text):

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )

            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="orange", back_color="brown")
            img.save("qrimg1.png")
            
        url = input("Enter your url: ")
        generate_qrcode(url)

    elif choice == 7:

        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        def generate_password():
            password_length = int(
                input("How long would you like your password to be?: "))
            random.shuffle(characters)
            password = []
            for _ in range(password_length):
                password.append(random.choice(characters))
            random.shuffle(password)
            password = "".join(password)
            print(password)
        generate_password()

    elif choice == 8:

        def roll_dice():
            dice_drawing = {
                1: (
                    "┌─────────┐",
                    "│         │",
                    "│    ●    │",
                    "│         │",
                    "└─────────┘",
                ),
                2: (
                    "┌─────────┐",
                    "│  ●      │",
                    "│         │",
                    "│      ●  │",
                    "└─────────┘",
                ),
                3: (
                    "┌─────────┐",
                    "│  ●      │",
                    "│    ●    │",
                    "│      ●  │",
                    "└─────────┘",
                ),
                4: (
                    "┌─────────┐",
                    "│  ●   ●  │",
                    "│         │",
                    "│  ●   ●  │",
                    "└─────────┘",
                ),
                5: (
                    "┌─────────┐",
                    "│  ●   ●  │",
                    "│    ●    │",
                    "│  ●   ●  │",
                    "└─────────┘",
                ),
                6: (
                    "┌─────────┐",
                    "│  ●   ●  │",
                    "│  ●   ●  │",
                    "│  ●   ●  │",
                    "└─────────┘",
                ),
            }
            roll = input("Roll the dice? (y/n)")

            while roll.lower() == "y".lower():
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("dice rolled: {} and {}".format(dice1, dice2))
                print("\n".join(dice_drawing[dice1]))
                print("\n".join(dice_drawing[dice2]))
                roll = input("Roll again? (Yes/No): ")
        roll_dice()

    elif choice == 9:
        def main(url):
            print("Checking connectivity ")

            # urllib.urlopen = pobiera status stronu
            response = urllib.urlopen(url)
            print("Connected to", url, "succesfully")
            # getcode = pokazuje kod
            print("The response code was:", response.getcode())

        print("This is a site connectivity checker program")
        input_url = input("Input the url of the site you want to check: ")
        main(input_url)

    elif choice == 10:
        list = ["Paper", "Rock", "Scissors"]
        score_your = 0
        score_bot = 0
        while True:
            choice = input("Enter your choice Paper/Rock/Scissors or exit: ")
            if choice.lower() == "paper":
                bot_choice = random.choice(list)
                if bot_choice == "Paper":
                    score_your = score_your
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("Draw, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Rock":
                    score_your = score_your + 1
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("You won, congratulations, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Scissors":
                    score_your = score_your
                    score_bot = score_bot + 1
                    print("Bot choice is ", bot_choice)
                    print("You lost, try again ")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)

            elif choice.lower() == "rock":
                bot_choice = random.choice(list)
                if bot_choice == "Paper":
                    score_your = score_your
                    score_bot = score_bot + 1
                    print("Bot choice is ", bot_choice)
                    print("You lost, try again ")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Rock":
                    score_your = score_your
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("Draw, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Scissors":
                    score_your = score_your + 1
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("You won, congratulations, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)

            elif choice.lower() == "scissors":
                if bot_choice == "Paper":
                    score_your = score_your + 1
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("You won, congratulations, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Rock":
                    score_your = score_your
                    score_bot = score_bot + 1
                    print("Bot choice is ", bot_choice)
                    print("You lost, try again ")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)
                elif bot_choice == "Scissors":
                    score_your = score_your
                    score_bot = score_bot
                    print("Bot choice is ", bot_choice)
                    print("Draw, try again")
                    print("Your Score is", score_your, "\n", "Bot Score is", score_bot)

            elif choice.lower() == "exit":
                break

            else:
                print("Please chose Paper/Rock/Scissors or exit")

    elif choice == 11:
        def resize(size1, size2, image_name):
            image = Image.open(image_name)
            print(f"Current size : {image.size}")
            resized_image = image.resize((size1, size2))
            resized_image.save(image_name)

        size1 = int(input("Enter the Width: "))
        size2 = int(input("Enter the Length: "))
        image_name = input("Enter the image name: ")

        resize(size1, size2, image_name)
    
    elif choice == 12:
        break