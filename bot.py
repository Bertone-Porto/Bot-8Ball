from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from random import randint
import asyncio

#Token 
TOKEN = ""

#Lista de respostas possíveis
respostas = [
    "Com certeza",
    "Sem a menor dúvida",
    "Talvez...",
    "Definitivamente sim!",
    "Você já sabe a resposta...",
    "Seu coração sabe que sim",
    "Sem dúvida",
    "Os sinais dizem que sim",
    "Pergunte novamente mais tarde",
    "Não conte com isso",
    "Minhas fontes dizem que não",
    "Definitivamente não!",
    "De jeito nenhum",
    "Seu coração sabe que não",
    "Não consigo te responder agora",
    "Tente novamente",
    "Melhor não te responder agora..."
]

#Função para escolher uma resposta aleatória
def obter_resposta():
    return respostas[randint(0, len(respostas) - 1)]

#Função chamada quando o usuário envia uma mensagem
async def responder(update: Update, context: CallbackContext) -> None:
    pergunta = update.message.text  #Captura a pergunta do usuário
    if pergunta.upper() == "SAIR":
        await update.message.reply_text("Até mais! Se precisar, estou aqui. 😊")
    else:
        await update.message.reply_text(f"*** {obter_resposta()} ***")

#Configuração do bot
def main():
    app = Application.builder().token(TOKEN).build()

    #Responder a qualquer mensagem de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    #Iniciar o bot
    print("Bot está rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
