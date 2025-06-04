# Kauê de Almeida Pena - 564211
# Gabriel Ferreira Machado - 562330
question = ["Caso ocorra uma enchente, qual seria a sua prioridade?\n",
            "Qual o seu tipo de moradia?\n",
            "Você tem algum plano de prenvenção para caso ocorra uma enchente?\n",
            "Você tem um kit de emergência preparado?\n",
            "Você tem algum transporte disponível para uma evacuação mais rápida?\n",
            "Você tem algum local seguro para se abrigar?\n"
            ]
answer = []
personal = ["Nome:\n", "Idade:\n", "Email:\n", "Endereço:\n", "Número de pessoas em sua casa:\n"]
personalAnswer = []


def formulario():
    print("Formulário:")
    for i in range(5):
        if i == 0 or i == 2 or i == 3:
            personalAnswer.append(input(personal[i]))
        elif i == 1 or i == 4:
            personalAnswer.append(int(input(personal[i])))
            if personalAnswer[1] < 15:
                print("Você não tem idade o suficiente para fazer este formulário!")
    return


def quiz():
    print("Quiz sobre enchentes:")
    for i in range(6):
        answer.append(input(question[i]))


def resultadoQuiz():
    formulario()
    quiz()
    print("Resultado do seu Quiz:")
    for i in range(5):
        print(question[i])
        print(answer[i])
        print("-"*30)


resultadoQuiz()
