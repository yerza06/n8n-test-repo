import os

# TODO: While
while True:
    text = input("Введите текст: ")
    result = text.replace("<br>", "\n")
    print("\nРезультат:")
    print("=" * 30)
    print("")
    print(result)
    print("")
    print("=" * 30)
    os.system(f"wl-copy '{result}'")
