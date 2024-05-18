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
    "Em Português, aprendemos sobre gramática, redação e literatura.",
    "Quais são os principais autores da literatura brasileira?",
    "Machado de Assis, Clarice Lispector e Carlos Drummond de Andrade são alguns dos principais autores.",
    "Pode me dar uma dica para melhorar minha redação?",
    "Leia bastante, pratique escrever regularmente e revise seus textos para corrigir erros."
]

conversa_matematica = [
    "O que se estuda em Matemática?",
    "Em Matemática, estudamos álgebra, geometria, estatística e cálculo.",
    "Para que serve a álgebra?",
    "A álgebra nos ajuda a resolver equações e problemas matemáticos de forma sistemática.",
    "Qual é a importância da geometria?",
    "A geometria é importante para entender formas, tamanhos e a posição relativa dos objetos."
]

conversa_historia = [
    "Você gosta de História?",
    "Sim, a História é fascinante. Aprendemos sobre eventos e civilizações do passado.",
    "Por que é importante estudar História?",
    "A História nos ajuda a entender como eventos passados moldaram o mundo de hoje.",
    "Qual foi um evento importante na história do Brasil?",
    "A Independência do Brasil em 1822 foi um evento crucial na nossa história."
]

conversa_biologia = [
    "O que você acha da Biologia?",
    "A Biologia é incrível! Estudamos sobre os seres vivos, ecologia e genética.",
    "Qual é o tópico mais interessante em Biologia?",
    "Eu acho a genética e a evolução os tópicos mais interessantes em Biologia.",
    "Por que a ecologia é importante?",
    "A ecologia nos ajuda a entender as interações entre os seres vivos e o meio ambiente."
]

list_trainer.train(conversa_portugues)
list_trainer.train(conversa_matematica)
list_trainer.train(conversa_historia)
list_trainer.train(conversa_biologia)

def pegar_feedback_usuario(usuario, resposta_bot):
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
