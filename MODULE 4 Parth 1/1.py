while True:
    userinput = input(">> ")
    userinput = userinput.replace( " ", ""
)
    text = userinput[::-1]
    if userinput.lower() == text.lower():
        print("палиндором есть")
    else:
        print("палиндрома нет")