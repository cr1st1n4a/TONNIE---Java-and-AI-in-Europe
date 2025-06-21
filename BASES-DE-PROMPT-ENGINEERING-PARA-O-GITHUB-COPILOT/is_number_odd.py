"""Crie uma função que receba um número e retorne se ele é ímpar ou par, se ele for ímpar retorne True, se for par retorne False.
Caso o usuário não passe um número inteiro, retorne um erro que não é um número inteiro."""

def is_number_odd(number):

    if type(number) != int:
        raise ValueError("Não é um número inteiro.")
    
    """Se o número for zero me retorne um erro que não é um número desejado."""

    if number == 0:
        raise ValueError("Zero não é um número desejado.")
    
    if number % 2 == 0:
        return False
    else:
        return True


def is_prime(number):
    if not isinstance(number, int):
        raise ValueError("Não é um número inteiro.")
    
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        
    return True
    