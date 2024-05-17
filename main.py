from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar a instância do chatbot
chatbot = ChatBot('Canguru banguélo')

# Treinamento do chatbot com o corpus de exemplo
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinar o chatbot com o corpus em português
trainer.train("chatterbot.corpus.portuguese")

# Função principal para conversar com o bot
def conversar():
    print("Olá! Eu sou o ChatterBot. Digite algo para começar a conversar...")
    while True:
        try:
            usuario = input("Você: ")
            bot = chatbot.get_response(usuario)
            print(f"Bot: {bot}")

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    conversar()
