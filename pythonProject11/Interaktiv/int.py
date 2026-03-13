import time
import random

player = {'hp': 100, 'money': 20, 'inv': []}

def p(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def game_over(text):
    p(f"\nИгра окончена: {text}")
    p("\nСпасибо за игру!")
    exit()
def wasteland():
    p("\nПеред тобой бескрайняя пустошь. Нужно найти бункер!")
    for step in range(3):
        print(f"\nШаг {step + 1} из 3")
        p("Ты оглядываешься по сторонам...")
        if input("1 - Идти дальше, 2 - Вернуться в город: ") == "2":
            p("Ты решаешь вернуться в город")
            return True
        event = random.random()
        if event < 0.3:
            found_money = 10
            player['money'] += found_money
            p(f"Ты находишь старый кошелёк с {found_money} монетами! Удача!")
        elif event < 0.6:
            player['hp'] = min(player['hp'] + 10, 100)
            p("Ты находишь заброшенный склад с консервами. Здоровье восстановлено на 10!")
        elif event < 0.9:
            p("Из-под земли выскакивает огромная крыса!")


p("Добро пожаловать в мир после апокалипсиса!")
p("Ты - один из немногих выживших, пытающихся найти убежище.")
p("Твоя цель: найти старый бункер с припасами.")
time.sleep(1)



