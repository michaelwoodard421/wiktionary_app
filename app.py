import webbrowser

# Select wiktionary UI language
supported_wikt_langs = {'english':'en',
                        'french':'fr',
                        'german':'de'}
while True:
    selected_wikt_lang = input("Choose a language for Wiktionary.\n").lower()
    if selected_wikt_lang in supported_wikt_langs:
        wikt_lang_code = supported_wikt_langs[selected_wikt_lang]
        break
    else:
        print(f"The language \"{selected_wikt_lang}\" is not currently supported.")

# Select language of words
target_lang = input("What language are you studying?\n").title()

while True:
    word = input(f"Enter a(n) {target_lang} word:\n")
    wikt_url = f"https://{wikt_lang_code}.wiktionary.org/wiki/{word}#{target_lang}"
    print(wikt_url)
    webbrowser.open(wikt_url)




