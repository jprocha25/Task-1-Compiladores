class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


entrada = input("Digite a sua entrada em RPN: ")

pilha = Stack()
operadores = {'+', '-', '*', '/'}
resultado = None

for token in entrada.split():
    if token.isdigit():
        pilha.push(int(token))
    elif token in operadores:
        b = pilha.pop()
        a = pilha.pop()

        if token == '+':
            resultado = a + b
        elif token == '-':
            resultado = a - b
        elif token == '*':
            resultado = a * b
        elif token == '/':
            resultado = a / b

    pilha.push(resultado)

    saida = pilha.pop()

print("Saida: ", saida)
