from googletrans import Translator

translator = Translator()

languages = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}
allow = True

while allow:
    user_code = input("Please input desired language code. To see the language code list write 'options'\n").lower()

    if user_code == "options":
        print("\nCode : Language")
        for code in languages.items():
            print(f"{code[0]} : {code[1]}")
        print()
    else:
        for code in languages.keys():
            if code == user_code:
                print(f"You have selected {languages[code]}")
                allow = False
        if allow:
            print("Invalid input")
    
while True:
    text = input("Enter the text or word you want to translate. To exit program type 'close'\n")

    if text == "close":
        print("Have a Nice Day")
        break

    translated = translator.translate(text, dest = user_code)

    print(f"\n{languages[user_code]} translation: {translated.text}")
    print(f"Pronunciation: {translated.pronunciation}")
    
    for i in languages.items():
        if translated.src == i[0]:
            print(f"Translated from: {i[1]}\n")





