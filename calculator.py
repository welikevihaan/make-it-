def calculate():
    try:
        expression = input("Enter a math expression (e.g. 2 + 3 * 4): ")
        result = eval(expression)
        print("Result:", result)
    except:
        print("Invalid input!")

if __name__ == "__main__":
    calculate()
