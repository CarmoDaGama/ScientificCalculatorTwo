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
def contains_operator(expressions):
    for operator in operators:
        if operator in expressions:
            return True
    return False

def calculate_expression(l_expression):
    for operator in operators:
        while operator in l_expression:
            index_operator = l_expression.index(operator)
            result = calc(float(l_expression[index_operator - 1]), float(l_expression[index_operator + 1]), operator)
            tmp_expression = []

            for index, value in enumerate(l_expression):
                if index == index_operator - 1 or index == index_operator + 1:
                    continue
                elif index == index_operator:
                    tmp_expression.append(result)
                else:
                    tmp_expression.append(value)
            l_expression.clear()
            l_expression = tmp_expression.copy()
            tmp_expression.clear()
    if contains_operator(l_expression):
        calculate_expression(l_expression)
    else:
        return float(l_expression[0])


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



def print_expressions(l_expression):
    print('\n\nValues: ', end='')
    for index, value in enumerate(l_expression):
        print(value, end='|')

    print('\n')
    print('Indexs: ', end='')
    for index, value in enumerate(l_expression):
        print(f'{index}', end='|')


def idea_optional(expressions):
    for index, value in enumerate(expressions):
        if value == '-' and not('-' in str(expressions[index + 1])):
            expressions[index + 1] = float(expressions[index + 1])*-1
            expressions[index] = '+'




# 5^2+4-5-77+55*79/93


expression = str(input('Type it Expression: '))


l_expression = get_list_expression(expression)
print(l_expression)
idea_optional(l_expression)
l_expression = calculate_expression(l_expression.copy())
print(f'\n\nFinal Result: {l_expression:.2f}')