from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SquareApp(App):
    def build(self):
        layout = FloatLayout()

        # Поле вводу (маленьке, зверху по центру)
        self.input = TextInput(
            hint_text='Число',
            size_hint=(0.3, 0.1),    # ширина 30%, висота 10%
            pos_hint={'center_x': 0.5, 'top': 0.95},
            multiline=False,
            input_filter='float'
        )
        layout.add_widget(self.input)

        # Кнопка піднести до квадрату (під полем вводу)
        self.button = Button(
            text='Піднести',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'top': 0.8}
        )
        self.button.bind(on_press=self.calculate_square)
        layout.add_widget(self.button)

        # Мітка для результату (внизу)
        self.result_label = Label(
            text='Результат:',
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'top': 0.6}
        )
        layout.add_widget(self.result_label)

        return layout

    def calculate_square(self, instance):
        try:
            number = float(self.input.text)
            result = number ** 2
            self.result_label.text = f'Результат: {result}'
        except ValueError:
            self.result_label.text = 'Помилка: введіть число'

if __name__ == '__main__':
    SquareApp().run()