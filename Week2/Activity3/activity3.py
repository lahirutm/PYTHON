class Student:
    def get_input_data(self, nth):
        self.student_name = input(f"Enter #{nth} student's name: ")
        self.student_age = int(input(f"Enter #{nth} student's age (Years):"))
        self.student_address = input(f"Enter #{nth} student's address: ")
        self.student_id = input(f"Enter #{nth} student's student ID: ")


    def print_collected_data(self):
        print(
            "You entered " + 
            "\n---Name: " + self.student_name +
            "\n---Age: " + str(self.student_age) +
            "\n---Address: " + self.student_address +
            "\n---Student ID: " + self.student_id
        )

    def add_to_collection(self, student_collection):
        stu = {
            "student_name" : self.student_name,
            "student_age" : self.student_age,
            "student_address" : self.student_address,
            "student_id" : self.student_id,

        }
        student_collection.append(stu)


def main():
    data_collection = []
    student = Student()
    nth = 1
    while True:
        student.get_input_data(nth)
        student.print_collected_data()

        need_to_continue = input("Do you want to continue (Y / N) ?")
        if need_to_continue == "Y":
            nth = nth + 1
            
            student.add_to_collection(data_collection)

            if nth >= 3:
                need_more = input("You have successfully entered 70 students, do you need to add more (Y / N)?")
                if need_more == "Y":
                    continue
                elif need_more == "N":
                    # Returns a new sorted list, leaves student_collection unchanged
                    sorted_students = sorted(data_collection, key=lambda s: s["student_name"])

                    # OR sort in place, modifying student_collection directly
                    data_collection.sort(key=lambda s: s["student_name"])

                    for stu in data_collection:
                        print(
                            "================ You entered ================\n" + 
                            "\n---Name: " + stu["student_name"] +
                            "\n---Age: " + str(stu["student_age"]) +
                            "\n---Address: " + stu["student_address"] +
                            "\n---Student ID: " + stu["student_id"] + 
                            "\n==================================\n"
                        )

                    break
                else:
                    print("Please enter valid input (Y / N) !")
            continue
        elif need_to_continue == "N":
            print("User confirmed to exit\nEXIT !")
            break
        else:
            print("Please enter valid input (Y / N) !")

if __name__ == "__main__":
    main()