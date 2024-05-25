import random
import locale

def get_message(language, message_type):
    messages = {
        "en": {
            "welcome": "Welcome to the Guess the Number game!",
            "choose_language": "Choose your language (en/de/es/hu): ",
            "instructions": "I'm thinking of a number between 1 and 100. Try to guess it!",
            "guess": "Enter your guess: ",
            "too_low": "Too low! Try again.",
            "too_high": "Too high! Try again.",
            "correct": "Congratulations! You've guessed the number.",
            "play_again": "Do you want to play again? (yes/no): "
        },
        "de": {
            "welcome": "Willkommen zum Zahlerraten-Spiel!",
            "choose_language": "Wähle deine Sprache (en/de/es/hu): ",
            "instructions": "Ich denke an eine Zahl zwischen 1 und 100. Versuche sie zu erraten!",
            "guess": "Gib deine Vermutung ein: ",
            "too_low": "Zu niedrig! Versuche es erneut.",
            "too_high": "Zu hoch! Versuche es erneut.",
            "correct": "Glückwunsch! Du hast die Zahl erraten.",
            "play_again": "Möchtest du nochmal spielen? (ja/nein): "
        },
        "es": {
            "welcome": "¡Bienvenido al juego de Adivinar el Número!",
            "choose_language": "Elige tu idioma (en/de/es/hu): ",
            "instructions": "Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!",
            "guess": "Introduce tu suposición: ",
            "too_low": "¡Demasiado bajo! Inténtalo de nuevo.",
            "too_high": "¡Demasiado alto! Inténtalo de nuevo.",
            "correct": "¡Felicidades! Has adivinado el número.",
            "play_again": "¿Quieres jugar de nuevo? (sí/no): "
        },
        "hu": {
            "welcome": "Üdvözöllek a Számkitalálós játékban!",
            "choose_language": "Válassz nyelvet (en/de/es/hu): ",
            "instructions": "Gondoltam egy számra 1 és 100 között. Próbáld meg kitalálni!",
            "guess": "Add meg a tippedet: ",
            "too_low": "Túl alacsony! Próbáld újra.",
            "too_high": "Túl magas! Próbáld újra.",
            "correct": "Gratulálok! Kitaláltad a számot.",
            "play_again": "Akarsz újra játszani? (igen/nem): "
        }
    }
    return messages[language][message_type]

def detect_language():
    system_language = locale.getdefaultlocale()[0]
    language_map = {
        'en': 'en',
        'de': 'de',
        'es': 'es',
        'hu': 'hu'
    }
    for key in language_map:
        if key in system_language:
            return language_map[key]
    return None

def main():
    language = detect_language()
    if language is None:
        print(get_message("en", "choose_language"))
        language = input().strip()
        if language not in ["en", "de", "es", "hu"]:
            language = "en"
    else:
        print(get_message(language, "welcome"))

    while True:
        print(get_message(language, "instructions"))
        number_to_guess = random.randint(1, 100)
        while True:
            guess = int(input(get_message(language, "guess")))
            if guess < number_to_guess:
                print(get_message(language, "too_low"))
            elif guess > number_to_guess:
                print(get_message(language, "too_high"))
            else:
                print(get_message(language, "correct"))
                break
        play_again = input(get_message(language, "play_again")).lower()
        if play_again not in ["yes", "ja", "sí", "igen"]:
            break

if __name__ == "__main__":
    main()
