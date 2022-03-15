import datetime
import os

# os.getcwd()


class LMS:
    """This class is used to keep record of books library.
    It has total four modules: "Display Books", "Issue Books", "Return Books", "Add Books" """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()

        for line in content:
            self.books_dict.update({str(Id): {"books_title": line.replace("\n",""),
                                              "lender_name": "",
                                              "Issue_Date": "",
                                              "Status": "Available"}})
            Id = Id + 1

    def display_books(self):
        print("--------------------------List of Books--------------------------")
        print("Books ID", "\t", "Title")
        print("-----------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t",value.get("books_title"), "- [",value.get("Status"),"]")

    def issue_books(self):
        books_id = input("Enter books ID")
        current_Date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status'] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} "
                      f"on {self.books_dict[books_id]['Issue_Date']}")
                return self.issue_books()
            elif self.books_dict[books_id]['Status'] == 'Available':
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_Date'] = current_Date
                self.books_dict[books_id]['Status'] = "Already Issues"
                print("Books Issues Successfully !!! \n")

    def add_books(self):
        new_books = input("Enter books title")
        if new_books == "":
            self.add_books()
        elif len(new_books) > 25:
            print("Books title length is to long !!! Title length should be > 20 char long")
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                new_id = str((int(max(self.books_dict))) + 1)
                self.books_dict[new_id] = {"books_title": new_books, "lender_name":"",
                                           "Issue_Date":"", "Status": "Available"}
                print(f"This book '{new_books}' has been added successfully")


    def return_books(self):
        books_id = input("Enter book ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your book ID")
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_Date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully updated !!! \n")
            else:
                print("Book is is not found")

try:
    myLMS = LMS("books.txt", "PersonalLibrary")
    pres_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n------------------------ Welcome To {myLMS.library_name} Library management System")
        for key, value in pres_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection: Issue Book\n")
            myLMS.issue_books()
        elif key_press == "a":
            print("\nCurrent Selection: Add Book\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection: Display Book\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Book\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input !!!")





#
# l = LMS("books.txt", "Personal Library")
# print(l.add_books())