def record_message_function(record_message):
    file_writer = open("D:\BotMessage\Main.txt", "r+")
    file_writer.write(record_message + "\n")
    file_writer.close()