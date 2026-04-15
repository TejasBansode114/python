with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
