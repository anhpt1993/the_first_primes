# the first primes
def input_data():
    while True:
        try:
            num = int(input("How many the first primes do you want to show: "))
            if num > 0:
                return num
                break
            else:
                print("Input positive number please")
                print()
        except Exception:
            print("Input value shall be an integer, not a float or string")
            print()

def check_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count == 0:
        return True

if __name__ == '__main__':
    number = input_data()
    count = 0
    check_num = 2
    print()
    print("List of the first {} primes:".format(number))
    while True:
        if count >= number:
            break
        else:
            if check_prime(check_num):
                print(check_num, end = " ")
                count += 1
        check_num += 1

