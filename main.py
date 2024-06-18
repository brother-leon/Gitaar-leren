import questionary as qs
import scales

def InitQuestion():
    choices=[
            'Learn scales',
            'Learn chords [not supported yet]'
            ]

    answer = qs.select("What do you want to do?",
                    choices
                    ).ask()

    for i in choices:
        if answer == i:
            scales.InitQuestion()

InitQuestion()