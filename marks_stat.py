MAX_MARK = 100
MIN_MARK = 0


def highest(marks):
    return max(marks)


def lowest(marks):
    return min(marks)


def average(marks):
    return sum(marks) / len(marks)


def validate_marks(marks):
    for mark in marks:
        if mark < MIN_MARK or mark > MAX_MARK:
            raise ValueError("Marks must be between 0 and 100")


def main():
    marks = [85, 72, 91, 64, 78]

    validate_marks(marks)

    print("Marks:", marks)
    print("Highest mark:", highest(marks))
    print("Lowest mark:", lowest(marks))
    print("Average mark:", average(marks))


if __name__ == "__main__":
    main()