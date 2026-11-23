def highest(marks):
    return max(marks)


def lowest(marks):
    return min(marks)


def average(marks):
    return sum(marks) / len(marks)


def main():
    marks = [85, 72, 91, 64, 78]

    print("Marks:", marks)
    print("Highest mark:", highest(marks))
    print("Lowest mark:", lowest(marks))
    print("Average mark:", average(marks))


if __name__ == "__main__":
    main()