try:
    num = int(input("Enter number: "))
    val = 10 / num

except ZeroDivisionError:
    print("Divide by 0 is not allowed")

except ValueError:
    print("Invalid input")


else:
    print(f"ans = {val}")

finally:                        #always run irrespective of the error
    print(f"End of code")