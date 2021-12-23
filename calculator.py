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
        count = len(expressions) - 1
        try:
            while operator in expressions:
                if operator == expressions[count] and expressions[count - 1].isnumeric() and expressions[count + 1].isnumeric():
                    print(f'{expressions[count - 1]} {expressions[count]} {expressions[count + 1]}')
                    count -= 1
                else:
                    count -= 1
        except Exception as error:
            print(f'Length: {len(expressions)}')
            print(f'Count: {count}')
            print(expressions)
            print(f'Error: {error.__class__}')

expression = str(input('Type it Expression: '))

print(get_list_expression(expression))
print(f'Rseult: {calculate_expression(expression)}')