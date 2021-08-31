print('SimPleCalc')
a = input('Enter a number :')
while not isinstance(a, float):
    try:
        a = float(a)
    except ValueError:
        a = input("Incorrect type, please repeat")
result = a
actions = ('+', '-', '*', '/', '=')
action = input('Enter math operator (+,-,*,/) or (=) for end calculating')
if action not in actions:
    print("Incorrect operator!")
    action = input('Enter math operator (+,-,*,/) or (=) for end calculating')
while action != '=':
    a = result
    b = input('Enter next number :')
    while not isinstance(b, float):
        try:
            b = float(b)
        except ValueError:
            b = input("Incorrect type, please repeat")
    if action == '+':
        result += b
    elif action == '-':
        result -= b
    elif action == '*':
        result *= b
    elif action == '/':
        try:
            result /= b
        except ZeroDivisionError:
            print('Zero Divivsion!. Ignore operator')
    print(a, action, b, '=', result)
    action = input('Enter math operator (+,-,*,/) or (=) for end calculating')
    if action not in actions:
        print("Incorrect operator!")
        action = input('Enter math operator (+,-,*,/) or (=) for end calculating')
print('Total result: ', result)
print('Thank you for use SimPleCalc')
