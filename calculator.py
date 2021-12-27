operators = '^*/+-'


def get_list_expression(expression):
    global operators
    expression_list = []
    member = ''
    for character in expression:
        if character in operators:
            if member.isnumeric():
                expression_list.append(member)
                expression_list.append(character)
            member = ''
        else:
            if character.isnumeric():
                member += character

    if member.isnumeric():
        expression_list.append(member)

    return expression_list


def calc(number1, number2, operator):
    if operator == '^':
        return number1**number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    elif operator == '+':
        return number1 + number2


def calculate_expression(expression):
    global operators
    expressions = get_list_expression(expression)
    for operator in operators:
        count = 0
        try:
            while operator in expressions:
                if operator == expressions[count]:
                    print(f'{expressions[count - 1]} {expressions[count]} {expressions[count + 1]}')
                    result = calc(float(expressions[count - 1]), float(expressions[count + 1]), expressions[count])
                    expressions.pop(count - 1)
                    expressions.pop(count)
                    expressions.pop(count + 1)
                    expressions.insert(0, result)
                    count = 0
                else:
                    count += 1
                    if len(expressions) == 0:
                        break
        except Exception as error:
            print(f'Length: {len(expressions)}')
            print(f'Count: {count}')
            print(expressions)
            print(f'Error: {error.__class__}')


def ValidExpression(expression):
    stack = []
    for symbol in expression:
        if symbol == '(':
            stack.append('(')
        elif symbol == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        return True
    else:
        return False


def details_expression(exp):
    print('\n\n')
    for index, value in enumerate(l_expression):
        print(f'Index: {index} Value: {value}')
    print('\n\n')

def add_in_list(list, data):
    for value in data:
        list.append(value)


def order_precedence(list_expression):
    potencies = []
    products = []
    divisions = []
    sums = []
    substractions = []
    print(len(list_expression))
    for index in range(0, len(list_expression)-1):
        print(index)
        if list_expression[index] == '^':
            potencies.append(list_expression[index - 1])
            potencies.append(list_expression[index])
            potencies.append(list_expression[index + 1])
        if list_expression[index] == '*':
            products.append(list_expression[index - 1])
            products.append(list_expression[index])
            products.append(list_expression[index + 1])
        if list_expression[index] == '/':
            divisions.append(list_expression[index - 1])
            divisions.append(list_expression[index])
            divisions.append(list_expression[index + 1])
        if list_expression[index] == '+':
            sums.append(list_expression[index - 1])
            sums.append(list_expression[index])
            sums.append(list_expression[index + 1])
        if list_expression[index] == '-':
            substractions.append(list_expression[index - 1])
            substractions.append(list_expression[index])
            substractions.append(list_expression[index + 1])
            list_expression = []
    add_in_list(list_expression, potencies)
    add_in_list(list_expression, products)
    add_in_list(list_expression, divisions)
    add_in_list(list_expression, substractions)

# 5^2+4-5-77+55*79/93


expression = str(input('Type it Expression: '))
l_expression = get_list_expression(expression)
print(l_expression)

order_precedence(l_expression)
def mm():
    for operator in operators:
        while(l_expression.index(operator) >= 0):
            result = calc(float(l_expression[0]), float(l_expression[2]), l_expression[1])
            del(l_expression[0])
            del(l_expression[1])
            del(l_expression[2])
            l_expression.insert(0, str(result))
            if len(l_expression) <= 1:
                break



print(l_expression)
