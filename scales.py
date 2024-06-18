import lib
import questionary as qs
import random
import runpy
import os

def MakeQuestion(scale):
    task = 'Play the '+scale+' scale in the tone of: '+random.choice(lib.tones())
    qs.print(task)

    choices = ['Another Scale', 'Back', 'EXIT']
    answer = qs.select("What do you want to do?",
                    choices
                    ).ask()
    
    for i in choices:
        if answer==choices[0]:
            InitQuestion()
        elif answer== choices[1]:
            os.system('cls')
            runpy.run_path('C:\Repo\Gitaar-leren\main.py')
        elif answer==choices[-1]:
            quit()
    

def InitQuestion():
    choices=lib.shapes()
    choices.append('Random Scale')
    answer = qs.select("What scale do you want to practice?",
                    choices
                    ).ask()

    for i in choices:
        if answer==i:
            MakeQuestion(answer)
        if answer==choices[-1]:
            answer = random.choice(lib.shapes())
            MakeQuestion(answer)
