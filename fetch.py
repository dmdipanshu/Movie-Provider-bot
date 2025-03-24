import telebot

        bot = telebot.TeleBot('7740738708:AAFQS0NBnqDUCGfwC9zKiKz62n96X4qneRE')

        @bot.message_handler(commands=['get_profile_photo'])
        def get_profile_photo(message):
            user_id = message.from_user.id  # Or use a different user ID if needed
            
            try:
                user_profile_photos = bot.get_user_profile_photos(user_id, limit=1) # limit to 1 photo
                
                if user_profile_photos.total_count > 0:
                    file_id = user_profile_photos.photos[0][0].file_id
                    file_url = bot.get_file(file_id).file_path
                    
                    bot.send_photo(message.chat.id, f"https://api.telegram.org/file/bot{bot.token}/{file_url}")
                else:
                    bot.reply_to(message, "User has no profile picture")
            except Exception as e:
                bot.reply_to(message, f"Error: {e}")

        bot.infinity_polling()
