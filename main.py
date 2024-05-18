from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    'Canguru Banguélo',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.portuguese")

list_trainer = ListTrainer(chatbot)

conversa_portugues = [
    "O que você aprende em Português?",
    "Em Português, aprendemos sobre gramática, redação, literatura e interpretação de texto.",
    "Quais são os principais períodos da literatura brasileira?",
    "Os principais períodos da literatura brasileira são: Quinhentismo, Barroco, Arcadismo, Romantismo, Realismo, Naturalismo, Parnasianismo, Simbolismo, Modernismo e Contemporaneidade.",
    "Qual é a importância da gramática na língua portuguesa?",
    "A gramática é importante porque estabelece as regras que regem o uso correto da língua, garantindo a clareza, coerência e coesão nos textos escritos e falados.",
    "Como melhorar a interpretação de textos?",
    "Para melhorar a interpretação de textos, é importante praticar a leitura regularmente, identificar o contexto, buscar o significado de palavras desconhecidas e fazer resumos ou sínteses após a leitura.",
    "Quem são alguns dos principais escritores do Realismo brasileiro?",
    "Alguns dos principais escritores do Realismo brasileiro são: Machado de Assis, José de Alencar, Aluísio Azevedo e Raul Pompeia.",
    "Qual é a diferença entre literatura clássica e contemporânea?",
    "A literatura clássica refere-se a obras literárias antigas, geralmente produzidas há muitos anos, enquanto a literatura contemporânea engloba obras mais recentes, escritas nos tempos atuais.",
    "Como evitar erros comuns na redação?",
    "Para evitar erros comuns na redação, é importante revisar cuidadosamente o texto em busca de problemas de gramática, ortografia e coesão, além de prestar atenção à estruturação das frases e parágrafos."
]

conversa_matematica = [
    "O que se estuda em Matemática?",
    "Em Matemática, estudamos álgebra, geometria, estatística e cálculo.",
    "Para que serve a álgebra?",
    "A álgebra nos ajuda a resolver equações e problemas matemáticos de forma sistemática.",
    "Qual é a importância da geometria?",
    "A geometria é importante para entender formas, tamanhos e a posição relativa dos objetos."
    "O que é trigonometria?",
    "A trigonometria é um ramo da matemática que estuda as relações entre os ângulos e os lados dos triângulos, além de suas aplicações em problemas práticos.",
    "Como calcular a área de um círculo?",
    "A área de um círculo pode ser calculada usando a fórmula A = π * r^2, onde A representa a área e r é o raio do círculo.",
    "O que é derivada em cálculo?",
    "A derivada em cálculo representa a taxa de variação de uma função em relação a uma de suas variáveis. Ela descreve como uma função muda em resposta a mudanças em suas entradas.",
    "Por que é importante estudar estatística?",
    "A estatística é importante porque nos ajuda a entender e interpretar dados, fazer previsões e tomar decisões informadas com base em informações quantitativas.",
    "O que são números irracionais?",
    "Os números irracionais são números que não podem ser expressos como uma fração simples. Eles têm uma expansão decimal infinita e não periódica, como √2 ou π.",
    "Qual é a diferença entre média, mediana e moda?",
    "A média é a soma de todos os valores dividida pelo número total de valores. A mediana é o valor central em um conjunto de dados ordenados. A moda é o valor que ocorre com mais frequência."
]


conversa_historia = [
    "Você gosta de História?",
    "Sim, a História é fascinante. Aprendemos sobre eventos e civilizações do passado.",
    "Por que é importante estudar História?",
    "A História nos ajuda a entender como eventos passados moldaram o mundo de hoje.",
    "Qual foi um evento importante na história do Brasil?",
    "A Independência do Brasil em 1822 foi um evento crucial na nossa história."
    "Quais foram as causas da Primeira Guerra Mundial?",
    "As principais causas da Primeira Guerra Mundial incluem rivalidades entre as potências europeias, militarismo, nacionalismo e a formação de alianças militares.",
    "O que foi a Revolução Industrial?",
    "A Revolução Industrial foi um período de transformação econômica e social que começou na Inglaterra no final do século XVIII, caracterizado pela transição da produção artesanal para a produção em larga escala nas fábricas.",
    "Quem foi Adolf Hitler e qual foi o papel dele na Segunda Guerra Mundial?",
    "Adolf Hitler foi o líder da Alemanha durante a Segunda Guerra Mundial e o líder do Partido Nazista. Ele é conhecido por suas políticas expansionistas e pela perseguição e genocídio de milhões de judeus e outros grupos durante o Holocausto.",
    "O que foi a Guerra Fria?",
    "A Guerra Fria foi um período de tensão política e conflito indireto entre os Estados Unidos e a União Soviética, que durou aproximadamente de 1947 a 1991. Foi caracterizado por rivalidades ideológicas, corrida armamentista e disputas por influência global.",
    "Quais foram as consequências da Revolução Francesa?",
    "As consequências da Revolução Francesa incluem o fim do Antigo Regime na França, a ascensão do poder político da burguesia, a disseminação dos ideais de liberdade, igualdade e fraternidade, e o surgimento de movimentos nacionalistas em toda a Europa.",
    "O que foi o Renascimento?",
    "O Renascimento foi um movimento cultural e intelectual que floresceu na Europa entre os séculos XIV e XVI, caracterizado pelo ressurgimento do interesse pelas artes, ciências e humanidades, inspirado nos modelos da Antiguidade Clássica."
]


conversa_biologia = [
    "O que você acha da Biologia?",
    "A Biologia é incrível! Estudamos sobre os seres vivos, ecologia e genética.",
    "Qual é o tópico mais interessante em Biologia?",
    "Eu acho a genética e a evolução os tópicos mais interessantes em Biologia.",
    "Por que a ecologia é importante?",
    "A ecologia nos ajuda a entender as interações entre os seres vivos e o meio ambiente.",
    "O que é fotossíntese?",
    "A fotossíntese é o processo pelo qual as plantas, algas e algumas bactérias convertem luz solar, dióxido de carbono e água em energia química (como glicose) e oxigênio.",
    "Quais são os diferentes reinos dos seres vivos?",
    "Os diferentes reinos dos seres vivos incluem o Reino Animalia (animais), o Reino Plantae (plantas), o Reino Fungi (fungos), o Reino Protista (protozoários e algas) e o Reino Monera (bactérias).",
    "O que é mitose?",
    "A mitose é um processo de divisão celular no qual uma célula-mãe se divide em duas células filhas geneticamente idênticas. É essencial para o crescimento, desenvolvimento e reparo dos tecidos em organismos multicelulares.",
    "Qual é a importância da biodiversidade?",
    "A biodiversidade é importante porque sustenta a saúde dos ecossistemas e fornece serviços ecossistêmicos essenciais, como polinização, purificação de água, regulação do clima e produção de alimentos.",
    "Como os organismos se adaptam ao seu ambiente?",
    "Os organismos se adaptam ao seu ambiente por meio da seleção natural, onde as características favoráveis são selecionadas ao longo do tempo devido à sua vantagem adaptativa, permitindo que os organismos sobrevivam e se reproduzam com mais sucesso."
]

list_trainer.train(conversa_portugues)
list_trainer.train(conversa_matematica)
list_trainer.train(conversa_historia)
list_trainer.train(conversa_biologia)

def pegar_feedback_usuario(usuario, resposta_correta):
    feedback = input("Esta resposta foi útil? (Sim/Não): ")
    if feedback.lower() == 'não':
        resposta_correta = input("Qual seria a resposta correta?: ")

        chatbot.storage.create(text=resposta_correta, in_response_to=usuario)

        list_trainer.train([usuario, resposta_correta])

        print("Obrigado pelo seu feedback! Vou aprender com isso.")

def escolher_disciplina():
    print("Escolha um tópico para conversar:")
    print("1. Português")
    print("2. Matemática")
    print("3. História")
    print("4. Biologia")
    escolha = input("Digite o número da sua escolha: ")
    return escolha


def conversar_sobre_disciplina(escolha):
    if escolha == '1':
        print("Você escolheu Português. Vamos conversar sobre isso!")
        while True:
            usuario = input("Você: ")
            if usuario.lower() == 'voltar':
                break
            bot_resposta = chatbot.get_response(usuario)
            print(f"Bot: {bot_resposta}")
            pegar_feedback_usuario(usuario, bot_resposta)
    elif escolha == '2':
        print("Você escolheu Matemática. Vamos conversar sobre isso!")
        while True:
            usuario = input("Você: ")
            if usuario.lower() == 'voltar':
                break
            bot_resposta = chatbot.get_response(usuario)
            print(f"Bot: {bot_resposta}")
            pegar_feedback_usuario(usuario, bot_resposta)
    elif escolha == '3':
        print("Você escolheu História. Vamos conversar sobre isso!")
        while True:
            usuario = input("Você: ")
            if usuario.lower() == 'voltar':
                break
            bot_resposta = chatbot.get_response(usuario)
            print(f"Bot: {bot_resposta}")
            pegar_feedback_usuario(usuario, bot_resposta)
    elif escolha == '4':
        print("Você escolheu Biologia. Vamos conversar sobre isso!")
        while True:
            usuario = input("Você: ")
            if usuario.lower() == 'voltar':
                break
            bot_resposta = chatbot.get_response(usuario)
            print(f"Bot: {bot_resposta}")
            pegar_feedback_usuario(usuario, bot_resposta)
    else:
        print("Escolha inválida. Por favor, tente novamente.")


print("Olá! Eu sou o Canguru Banguélo. Vamos começar nossa conversa.")
while True:
    escolha = escolher_disciplina()
    conversar_sobre_disciplina(escolha)
    if input("Deseja escolher outro tópico? (sim/não): ").lower() != 'sim':
        print("Até logo!")
        break
