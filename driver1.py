from Student import Student
from Deque import Deque

def show(dq):
    names = []
    for student in dq.to_list():
        names.append(student.get_name())
    print("Deque:", names)

def main():
    print("*** Problem 1 ***")
    s1 = Student("ABC", 18, 3.2)
    s2 = Student("BCD", 19, 3.3)
    s3 = Student("CDE", 20, 3.4)
    s4 = Student("DEF", 21, 3.5)

    print("Student01:", s1)
    s1.set_age(22)
    s1.set_gpa(4.0)
    print("\nAfter set:", s1)

    dq = Deque()
    print("\nEmpty:", dq.is_empty()," \nSize:", dq.size())

    dq.addBack(s1)
    dq.addBack(s2)
    dq.addFront(s3)
    dq.addFront(s4)
    show(dq)
    print("Size:",dq.size())

    print("\nSearch ABC:", dq.search("ABC"))
    print("Search EFG:", dq.search("EFG"))

    print("\nRemove CDE:", dq.remove("CDE"))
    print("After remove to search CDE:", dq.search("CDE"))
    print("Remove EFG:", dq.remove("EFG"))
    show(dq)

    front = dq.removeFront()
    back = dq.removeBack()
    print("\nRemoveFront:", front)
    print("RemoveBack:", back)
    show(dq)

    dq.removeFront()
    print("\nEmpty: ", dq.is_empty())
    print("Size: ", dq.size())
    print("RemoveFront: ", dq.removeFront())
    print("RemoveBack: ", dq.removeBack())
    print("Remove x: ", dq.remove("a"))
    print("Search x: ", dq.search("a"))


if __name__ == '__main__':
    main()