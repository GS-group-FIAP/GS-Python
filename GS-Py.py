# Kauê de Almeida Pena - 564211
# Gabriel Ferreira Machado - 562330
# João Stellare - 565813

#Crianção das listas para as perguntas e respostas do formulário e do quiz.
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

#Crianção das função para o formulário
def formulario():
    print("Formulário:")
    # Coleta de informações pessoais através de um loop
    for i in range(5):
        if i == 0 or i == 2 or i == 3:
            personalAnswer.append(input(personal[i]))
        elif i == 1 or i == 4:
            personalAnswer.append(int(input(personal[i])))
            while personalAnswer[1] < 15:
                print("Você não tem idade o suficiente para fazer este formulário!")
                personalAnswer[1] = int(input(personal[i]))
    return
#Crianção das funções para prevenção de enchentes
def prevention():
    #Chamada para as funções de prevenção
    before()
    print("-"*206)
    during()
    print("-"*180)
    after()
# Função para o quiz sobre enchentes
def quiz():
    print("Quiz sobre enchentes:")
    # Coleta de respostas do usuário para o quiz através de um loop
    for i in range(6):
        answer.append(input(question[i]))

# Função para exibir o resultado do quiz
def resultadoQuiz():
    # Chamada para o formulário e o quiz
    formulario()
    quiz()
    print("-"*30)
    # Exibição das respostas do formulário
    print("Resultado do seu Quiz:")
    for i in range(5):
        print(question[i])
        print(answer[i])
        print("-"*30)
#Função para printar dicas para prevenir-se antes das enchente
def before():
    print("Antes das enchentes:")
    print("A prevenção começa muito antes da água subir. Se você mora em uma área de risco, esteja sempre atento a sinais de alerta e informações de órgãos oficiais. Cadastre seu número no serviço de alertas da Defesa Civil (SMS 40199) para receber avisos antecipados.")
    print("Tenha uma mochila com documentos, remédios, lanternas e itens essenciais.")
    print("Conheça os pontos de abrigo próximos à sua casa.")
    print("Evite jogar lixo nas ruas, rios e bueiros.")
    print("Mantenha calhas, telhados e ralos limpos.")
    

# Função para fornecer orientações durante e após uma enchente
def during(): 
    print("Durante as enchentes:")
    print("A sua segurança e a de sua família devem ser prioridade. Ao perceber sinais de inundação, aja rapidamente e com calma. Se estiver fora de casa, não tente atravessar áreas alagadas — mesmo com água aparentemente rasa.")
    print("Desligue a energia e o gás imediatamente.")
    print("Evacue para um local seguro, preferencialmente elevado.")
    print("Não ande ou dirija por ruas alagadas.")
    print("Evite contato com a água da enchente — ela pode estar contaminada.")
    print("Use apenas lanternas (nunca velas) para evitar risco de incêndio.")
# Função para fornecer orientações após uma enchente
def after():
    print("Depois das enchentes:")
    print("Após a enchente, a situação ainda pode oferecer riscos. Só retorne para sua casa quando as autoridades liberarem o local e for seguro. Redobre os cuidados com higiene e saúde.")
    print("Evite contato direto com a água e a lama restante.")
    print("Use luvas e botas ao limpar a casa.")
    print("Descarte alimentos e medicamentos que tiveram contato com a água.")
    print("Ferva a água para consumo ou utilize água potável.")
    print("Verifique rachaduras, fiações e riscos estruturais antes de religar energia.")
# Chamada das funções para iniciar o programa
resultadoQuiz()
prevention()
