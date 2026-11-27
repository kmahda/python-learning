def main():
    text = input("Type your text with a smile: ")
    print(convert(text))


def convert(string: str) -> str:
    string = string.replace(":)", "\U0001f642")
    string = string.replace(":(", "\U0001f641")
    return string


main()
