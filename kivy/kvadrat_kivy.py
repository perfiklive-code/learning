from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SquareApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input = TextInput(hint_text='Введіть число', multiline=False, input_filter='float')
        self.layout.add_widget(self.input)

        self.button = Button(text='Піднести до квадрату')
        self.button.bind(on_press=self.calculate_square)
        self.layout.add_widget(self.button)

        self.result_label = Label(text='Результат:')
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_square(self, instance):
        try:
            number = float(self.input.text)
            result = number ** 2
            self.result_label.text = f'Результат: {result}'
        except ValueError:
            self.result_label.text = 'Помилка: введіть коректне число'

if __name__ == '__main__':
    SquareApp().run()