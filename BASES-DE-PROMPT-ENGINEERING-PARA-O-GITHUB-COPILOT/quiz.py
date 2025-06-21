"""
Crie uma lista de questões com 5 perguntas e 4 possiveis respostas cada.
Cada pergunta deve ter uma resposta correta.
Cada resposta correta deve valer 1 ponto.
Esse quiz será de várias capitais do mundo.
"""

questions = [
    {
        "question": "Qual é a capital do Brasil?",
        "answers": {
            "a": "Brasília", 
            "b": "Rio de Janeiro", 
            "c": "São Paulo", 
            "d": "Salvador"
            },
        "correct_answer": "a"
    },
    {
        "question": "Qual é a capital da Japão?",
        "answers": {
            "a": "Tóquio", 
            "b": "Kyoto",
            "c": "Osaka",
            "d": "Hiroshima"
            },
        "correct_answer": "a"
    },
    {
        "question": "Qual é a capital da França?",
        "answers": {
             
            "a": "Londres", 
            "b": "Berlim", 
            "c": "Paris",
            "d": "Madri"
            },
        "correct_answer": "c"
    },
    {
        "question": "Qual é a capital da Alemanha?",
        "answers": {
            "a": "Munique",
            "b": "Berlim", 
            "c": "Frankfurt", 
            "d": "Hamburgo"
            },
        "correct_answer": "b"
    },
    {
        "question": "Qual é a capital da Itália?",
        "answers": {
            "a": "Milão", 
            "b": "Veneza", 
            "c": "Nápoles",
            "d": "Roma", 
        },
        "correct_answer": "d"
    }
]

"""
Escreva uma função que recebe a questão e as exibe uma a uma para o usuário.
Ela retorna a resposta do usuário e valida se a resposta é valida ou se ela é um erro.
Se o usuário não responder em 10 segundos, a função deve retornar, indicando que o tempo acabou.
Usando a biblioteca threading, você pode criar uma thread que conta 10 segundos e, se o usuário não responder, a thread interrompe a execução da função.
"""

import threading

def show_question(question):
    """
    Exibe uma pergunta de múltipla escolha, solicita a resposta do usuário com limite de tempo e retorna a resposta escolhida.
    Args:
        question (dict): Um dicionário contendo a chave "question" (str) com o texto da pergunta e a chave "answers" (dict) com as opções de resposta, onde as chaves são letras (ex: 'a', 'b', 'c') e os valores são as alternativas.
    Returns:
        str: A letra correspondente à resposta escolhida pelo usuário.
    Raises:
        ValueError: Se o usuário não fornecer uma resposta válida dentro do tempo limite ou se a resposta não corresponder a uma das opções disponíveis.
    """
    
    print(question["question"])
    for key, value in question["answers"].items():
        print(f"{key}: {value}")

    user_answer = [None]
    def get_user_answer():
        user_answer[0] = input("Digite a letra correspondente a sua resposta: ").lower()

    # Cria uma thread para capturar a resposta do usuário
    thread = threading.Thread(target=get_user_answer)
    thread.daemon = True
    thread.start()
    # O método join espera até que a thread termine ou até o tempo limite seja atingido, no caso 5 segundos.
    thread.join(5)

    if user_answer[0] is not None and user_answer[0] in question["answers"]:
        return user_answer[0]
    else:
        raise ValueError("Resposta inválida, digite a letra correspondente a sua resposta.")


# Escreva uma função que recebe a resposta do usuário e a compara com a resposta correta.

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer



def main():
    score = 0

    for question in questions:
        user_answer = show_question(question)
        if check_answer(user_answer, question["correct_answer"]):
            score += 1
        else:
            print(f"Resposta errada. A resposta correta é:", question['correct_answer'])

    """
    Adicione um sistema de feedback para o usuário ao final do quiz
    Por exemplo:
    Entre 0 a 30 por cento: "Você precisa estudar mais"
    Entre 30 a 70 por cento: "Você foi bem, mas ainda pode melhorar"
    Entre 70 a 100 por cento: "Parabéns, você foi bem"
    """

    provide_feedback(score)

    print(f"Você acertou {score} perguntas de um total de {len(questions)}.")

def provide_feedback(score):
    percent = (score / len(questions)) * 100
    if percent < 30:
        print("Você precisa estudar mais.")
    elif percent < 70:
        print("Você foi bem, mas ainda pode melhorar.")
    else:
        print("Parabéns, você foi bem.")

if __name__ == "__main__":
    main()