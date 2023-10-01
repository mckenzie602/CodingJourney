def convert(input_str):
    converted_str = input_str.replace(":)","🙂").replace(":(","🙁")
    return converted_str

def main():
    user_input = input()
    converted_text = convert(user_input)
    print(converted_text)
main()