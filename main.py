################################################
################################################
#################КАЛЬКУЛЯТОР####################
################################################
################################################

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 400)

class CalculatorApp(App):

    def clear_all(self, instance):
        self.lbl.text = "0"
        self.formula *= 0

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == 0):
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if( str(instance.text).lower() == 'x'):
            self.formula += '*'
        elif ( str(instance.text).lower() == ':'):
            self.formula += '/'

        else:
            self.formula += str(instance.text)


        self.update_label()

    def calc_result(self,instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = ""

    def build(self):

        self.formula = ''
        bl = BoxLayout(orientation = 'vertical', padding = 8)
        grl = GridLayout(cols = 4, spacing = 2, size_hint = (1, .6))
        self.lbl = Label(text ='0', font_size = 40, halign='right', valign = 'center', size_hint = (1, .4), text_size =(300 - 16, 400 * .4 - 16), color = 'red')
        bl.add_widget( self.lbl )


        grl.add_widget( Button(text = "7", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "8", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "9", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "x", on_press = self.add_operation, color = 'red', font_size = 25, background_color = 'red'))

        grl.add_widget( Button(text = "4", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "5", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "6", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "-", on_press = self.add_operation, color = 'red', font_size = 25, background_color = 'red'))

        grl.add_widget( Button(text = "1", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "2", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "3", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "+", on_press = self.add_operation, color = 'red', font_size = 25, background_color = 'red'))

        grl.add_widget( Button(text = "C", on_press = self.clear_all, color = 'red', font_size = 25, background_color = 'red'))
        grl.add_widget( Button(text = "0", on_press = self.add_number, color = 'red', font_size = 25))
        grl.add_widget( Button(text = "=", on_press = self.calc_result, color = 'red', font_size = 25, background_color = 'red'))
        grl.add_widget( Button(text = ":", on_press = self.add_operation, color = 'red', font_size = 25, background_color = 'red'))


        bl.add_widget( grl )
        return bl


if __name__ == "__main__":
    CalculatorApp().run()

