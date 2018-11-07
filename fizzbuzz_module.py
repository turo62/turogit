def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            number = "FizzBuzz"
            return number
        elif number % 3 == 0:
            number = "Fizz"
            return number
        elif number % 5 == 0:
            number = "Buzz"
            return number
        else:
            return number
 

def main():
        for number in range(1, 101):
                print(fizzbuzz(number))

if __name__ == '__main__':
        main()
