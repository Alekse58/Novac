# import telepot
#
# BOT_TOKEN = '5898156643:AAFDPm6pZsBY56iXznuG-GaePUZ6Z5ldIfQ'
#
# # Создайте экземпляр бота
# bot = telepot.Bot(BOT_TOKEN)
#
#
# def send_message_to_all_users(message_text):
#     # Получите список всех обновлений (сообщений) от всех пользователей, общающихся с ботом
#     updates = bot.getUpdates()
#
#     # Отправить сообщение всем пользователям
#     for update in updates:
#         chat_id = update['message']['chat']['id']
#         bot.sendMessage(chat_id, message_text)
#
#
# if __name__ == '__main__':
#     # Пример использования
#     message_text = 'Привет, это сообщение идет всем пользователям бота!'
#     send_message_to_all_users(message_text)
