import os

import random
import time
from nicegui import ui
from threading import Timer
import config

logger = config.get_logger(__name__)


def content():

    content_div = ui.element("div").classes("container mt-5")

    # Lave en liste af danske ord, så vi kan vælge tilfældige ord
    danish_words = list(config.danish_thai_dict.keys())

    # Funktion til at præsentere et nyt ord
    def present_new_word():
        # Vælg et tilfældigt dansk ord
        current_word = random.choice(danish_words)
        correct_translation = config.danish_thai_dict[current_word]

        # Vælg 3 forkerte svar
        incorrect_translations = random.sample(
            [v for k, v in config.danish_thai_dict.items() if v != correct_translation],
            3,
        )

        # Lav en liste med det korrekte og forkerte svar og bland dem
        options = incorrect_translations + [correct_translation]
        random.shuffle(options)

        # Ryd skærmen
        content_div.clear()

        with content_div:
            # Vis det danske ord
            ui.label(
                f'Hvad er den thailandske oversættelse af "{current_word}"?'
            ).style("font-size: 24px")

            # Funktion der styrer resultatet
            def handle_answer(option, button):
                if option == correct_translation:
                    button.props("color=green")
                else:
                    button.props("color=red")

                # Vis den rigtige oversættelse
                ui.label(f"Det korrekte svar er: {correct_translation}").style(
                    "font-size: 18px"
                )

                # Efter 3 sekunder gå til næste ord
                Timer(3, present_new_word).start()

            # Funktion til at generere en lambda-funktion med korrekt binding af btn
            def create_button(option):
                btn = ui.button(
                    option, on_click=lambda: handle_answer(option, btn)
                ).classes("m-2")
                return btn

            # Opret knapper for hvert svarmulighed
            for option in options:
                create_button(option)

    # Start quizzen med det første ord
    with content_div:
        with ui.row():
            present_new_word()

    # Kør NiceGUI
    # ui.run()
