import telebot

bot = telebot.TeleBot('7740738708:AAFQS0NBnqDUCGfwC9zKiKz62n96X4qneRE')

@bot.message_handler(commands=['get_profile_photo'])
def get_profile_photo(message):
    user_id = message.from_user.id  # Get sender's user ID

    try:
        # Fetch user's profile photos (limit 1)
        user_profile_photos = bot.get_user_profile_photos(user_id, limit=1)

        if user_profile_photos.total_count > 0:
            file_id = user_profile_photos.photos[0][0].file_id
            bot.send_photo(message.chat.id, file_id)  # Send the photo directly using file_id
        else:
            bot.reply_to(message, "You don't have a profile picture.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
