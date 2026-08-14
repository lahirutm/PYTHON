def main():
    # variable to store content
    content = ''
    # read text file and convert to lower case and assign to content variable
    with open("junk.txt", "r") as text_file:
        content = text_file.read().lower()
        text_file.close

    # write lower case contetnt and add new conent line
    with open("junk.txt", "w") as text_file:
        text_file.write(content)
        text_file.write("\ntext file analyssis")
        text_file.close


if __name__ == "__main__":
    main()