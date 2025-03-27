from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


def time_pace_to_speed(time: str, pace: str):
    time_temp = [x for x in map(int, time.split(":"))]
    hours = time_temp[0] + time_temp[1] / 60 + time_temp[2] / 3600

    pace_temp = [x for x in map(int, pace.split(":"))]
    pace_minutes = pace_temp[0] + pace_temp[1] / 60

    speed = 60 / pace_minutes

    return speed


def time_pace_to_distance(time: str, pace: str):
    speed = time_pace_to_speed(time, pace)

    time_temp = [x for x in map(int, time.split(":"))]
    hours = time_temp[0] + time_temp[1] / 60 + time_temp[2] / 3600

    return speed * hours


class PaceApp(App):
    def build(self):
        return self.main_screen()

    def main_screen(self):
        self.layout = BoxLayout(orientation='vertical')

        self.select_speed_button = Button(text='Calculate speed - basis on pace and time')
        self.select_speed_button.bind(on_press=self.speed_screen)
        self.layout.add_widget(self.select_speed_button)

        self.select_pace_button = Button(text='Calculate distance - basis on pace and time')
        self.select_pace_button.bind(on_press=self.distance_screen)
        self.layout.add_widget(self.select_pace_button)

        return self.layout

    def back_to_main_screen(self, instance):
        self.layout.clear_widgets()

        self.main_screen()

        Window.clear()
        Window.add_widget(self.layout)

    def speed_screen(self, instance):
        self.layout.clear_widgets()

        self.layout = BoxLayout(orientation='vertical')

        self.time_input = TextInput(hint_text='Time (hh:mm:ss)')
        self.layout.add_widget(self.time_input)

        self.pace_input = TextInput(hint_text='Pace (mm:ss)')
        self.layout.add_widget(self.pace_input)

        self.result_label_speed = Label(text='Speed basis on pace and time')
        self.layout.add_widget(self.result_label_speed)

        self.calculate_button = Button(text='Calculate')
        self.calculate_button.bind(on_press=self.calculate_speed)
        self.layout.add_widget(self.calculate_button)

        self.to_main_screen = Button(text='Back to main screen')
        self.to_main_screen.bind(on_press=self.back_to_main_screen)
        self.layout.add_widget(self.to_main_screen)

        Window.clear()
        Window.add_widget(self.layout)

    def distance_screen(self, instance):
        self.layout.clear_widgets()

        self.layout = BoxLayout(orientation='vertical')

        self.time_input = TextInput(hint_text='Time (hh:mm:ss)')
        self.layout.add_widget(self.time_input)

        self.pace_input = TextInput(hint_text='Pace (mm:ss)')
        self.layout.add_widget(self.pace_input)

        self.result_label_distance = Label(text='Distance basis on pace and time')
        self.layout.add_widget(self.result_label_distance)

        self.calculate_button = Button(text='Calculate')
        self.calculate_button.bind(on_press=self.calculate_distance)
        self.layout.add_widget(self.calculate_button)

        self.to_main_screen = Button(text='Back to main screen')
        self.to_main_screen.bind(on_press=self.back_to_main_screen)
        self.layout.add_widget(self.to_main_screen)

        Window.clear()
        Window.add_widget(self.layout)

    def calculate_speed(self, instance):
        time = self.time_input.text
        pace = self.pace_input.text

        try:
            speed = time_pace_to_speed(time, pace)
            self.result_label_speed.text = f"Average speed: {speed:.2f} km/h"
        except Exception as e:
            self.result_label_speed.text = f"Wrong data"

    def calculate_distance(self, instance):
        time = self.time_input.text
        pace = self.pace_input.text

        try:
            distance = time_pace_to_distance(time, pace)
            self.result_label_distance.text = f"Distance: {distance:.2f} km"
        except Exception as e:
            self.result_label_distance.text = f"Wrong data"


if __name__ == '__main__':
    PaceApp().run()
