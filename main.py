from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.0.6')  # replace with your current kivy version !


# (see :attr:`~App.get_application_config` for its location) main.ini for config variables

class MyApp(App):
    def build_config(self, config):
            config.setdefaults('section1', {
                'key1': 'value1',
                'key2': '42'
            })

    def build(self):
        self.title = 'Spring Break'
        config = self.config
        return Label(text='key1 is %s and key2 is %d' % (
            config.get('section1', 'key1'),
            config.getint('section1', 'key2')))


if __name__ == '__main__':
    MyApp().run()
