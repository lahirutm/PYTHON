def main():
    my_list = [1,3,5,7,9,11]
    # from 2 to 4 (Up to 4, index 4 won't be replaced)
    my_list[2:4] = [-3,-9,-11,-13]
    print(my_list)

if __name__ == "__main__":
    main()


