#Importando Bibliotécas necessárias

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys
from time import sleep

#Classe do layout da grade que aparece na tela
class MyGrid(GridLayout):

    #Inicio
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        """Aqui foi criado a cara do app, a superficie
           com as coisas que devem aparecer. Textos,  
           caixas de entrada butões, imagens."""

        self.rows = 2

        self.inside = GridLayout() #Criando Uma grade com 2 colunas

        self.inside.rows = 5  #Colunas criadas no  layout do app
        self.inside.cols = 4

        #Criando texto e caixas de entrada

        #Primeiro nome
        self.oper = TextInput(multiline = False, size_hint=(1, 0.1))
        self.add_widget(self.oper)

        self.b7 = Button(text="7", font_size=30)
        self.b7.bind(on_press=self.pressed)
        self.inside.add_widget(self.b7)

        self.b8 = Button(text="8", font_size=30)
        self.b8.bind(on_press=self.pressed)
        self.inside.add_widget(self.b8)

        self.b9 = Button(text="9", font_size=30)
        self.b9.bind(on_press=self.pressed)
        self.inside.add_widget(self.b9)

        self.bc = Button(text="C", font_size=30)
        self.bc.bind(on_press=self.clean)
        self.inside.add_widget(self.bc)

        self.b4 = Button(text="4", font_size=30)
        self.b4.bind(on_press=self.pressed)
        self.inside.add_widget(self.b4)

        self.b5 = Button(text="5", font_size=30)
        self.b5.bind(on_press=self.pressed)
        self.inside.add_widget(self.b5)

        self.b6 = Button(text="6", font_size=30)
        self.b6.bind(on_press=self.pressed)
        self.inside.add_widget(self.b6)

        self.bcc = Button(text="<<", font_size=30)
        self.bcc.bind(on_press=self.c_lean)
        self.inside.add_widget(self.bcc)

        self.b1 = Button(text="1", font_size=30)
        self.b1.bind(on_press=self.pressed)
        self.inside.add_widget(self.b1)

        self.b2 = Button(text="2", font_size=30)
        self.b2.bind(on_press=self.pressed)
        self.inside.add_widget(self.b2)

        self.b3 = Button(text="3", font_size=30)
        self.b3.bind(on_press=self.pressed)
        self.inside.add_widget(self.b3)

        self.bml = Button(text="+/-", font_size=30)
        self.bml.bind(on_press=self.ml)
        self.inside.add_widget(self.bml)

        self.b0 = Button(text="0", font_size=30)
        self.b0.bind(on_press=self.pressed)
        self.inside.add_widget(self.b0)

        self.bmore = Button(text="+", font_size=30)
        self.bmore.bind(on_press=self.pressed)
        self.inside.add_widget(self.bmore)

        self.bx = Button(text="x", font_size=30)
        self.bx.bind(on_press=self.pressed)
        self.inside.add_widget(self.bx)

        self.bpow = Button(text="^", font_size=30)
        self.bpow.bind(on_press=self.pressed)
        self.inside.add_widget(self.bpow)

        self.be = Button(text="=", font_size=30)
        self.be.bind(on_press=self.equal)
        self.inside.add_widget(self.be)

        self.bless = Button(text="-", font_size=30)
        self.bless.bind(on_press=self.pressed)
        self.inside.add_widget(self.bless)

        self.bdiv = Button(text="/", font_size=30)
        self.bdiv.bind(on_press=self.pressed)
        self.inside.add_widget(self.bdiv)

        self.bp = Button(text=".", font_size=30)
        self.bp.bind(on_press=self.pressed)
        self.inside.add_widget(self.bp)

        #Adicionando a tela self.inside(grade com duas colunas)
        self.add_widget(self.inside)

    def c_lean(self, instance):
        text = ''
        for c in range(0, len(self.oper.text)-1):
            text += self.oper.text[c]
        self.oper.text = text
    
    def equal(self, instance):
        text = ''
        for l in self.oper.text:
            if l == '^':
                text += '**'
            elif l == 'x':
                text += '*'
            else:
                text += l
        
        try:
            self.oper.text = str(eval(text))
        except:
            self.oper.text = '*ERROR*'
    
    def ml(self, instance):
        text = ''
        if len(self.oper.text) > 0:
            if self.oper.text[0] == '-':
                for c in range(1, len(self.oper.text)):
                    text += self.oper.text[c]
                self.oper.text = text
            else:
                self.oper.text = '-' + self.oper.text
    
    def clean(self, instance):
        self.oper.text = ''

    def pressed(self, instance):
        self.oper.text += instance.text

#Classe do App
class MyApp(App):
    def build(self):

        """
        Esse é o App, retornando o que deve aparecer
        informado na classe anterior
        """

        #Retorna a classe do layout
        return MyGrid()

#Rodando o App
if __name__ == "__main__":
    MyApp().run()
