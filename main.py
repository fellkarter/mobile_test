import random

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

STATUS_BADGES = [
    "Deep Focus",
    "Calm Momentum",
    "Morning Clarity",
    "Evening Wind-down",
    "Midday Rally",
]

PROMPTS = [
    "Build one tiny habit that serves a larger goal.",
    "Pick a small win you can ship before lunch.",
    "Take three measured breaths before jumping in.",
    "Draft a single sentence that captures today's purpose.",
    "Swap a mindless scroll for a mindful stretch.",
]

HIGHLIGHTS = [
    "You are linear, steady, and tuned-in today.",
    "Vibe check: curiosity leads the way.",
    "Keep the momentum, even a pause is progress.",
    "Refresh the page by stepping outside for 2 minutes.",
    "Your calm focus is contagious - share it.",
]

BACKGROUND_COLOR = (0.07, 0.08, 0.12, 1)

if Window:
    Window.clearcolor = BACKGROUND_COLOR


class FocusRoot(BoxLayout):
    status = StringProperty("")
    prompt = StringProperty("")
    highlight = StringProperty("")
    streak = StringProperty("")
    breaths = StringProperty("")
    energy = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_prompt()

    def refresh_prompt(self, *args):
        self.status = random.choice(STATUS_BADGES)
        self.prompt = random.choice(PROMPTS)
        self.highlight = random.choice(HIGHLIGHTS)
        self.streak = f"{random.randint(3, 14)}-day streak"
        self.breaths = f"{random.randint(8, 20)} mindful breaths"
        self.energy = random.choice(["Lively", "Steady", "Calm", "Focused"])


class FocusApp(App):
    def build(self):
        if Window:
            Window.clearcolor = BACKGROUND_COLOR
        return FocusRoot()


if __name__ == "__main__":
    FocusApp().run()
