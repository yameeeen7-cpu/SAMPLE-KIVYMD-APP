from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class SmartConnectApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.label = Label(text="Welcome to Smart Connect!", font_size='24sp')
        layout.add_widget(self.label)
        btn = Button(text="اضغط هنا", font_size='20sp', size_hint_y=0.3)
        btn.bind(on_press=self.on_press)
        layout.add_widget(btn)
        return layout

    def on_press(self, instance):
        self.counter += 1
        self.label.text = f"تم الضغط {self.counter} مرة"


if __name__ == '__main__':
    SmartConnectApp().run()
