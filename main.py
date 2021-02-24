# -*- coding: utf-8 -*-
"""
App.py    
Created on Wed Feb  3 18:26:17 2021

@author: Emanuel Monção Lima
"""

## Imports
from gui import *
from wordlists import hangman_wordlist2 as wl

from PyQt5.QtWidgets import QPushButton, QMessageBox
from unidecode import unidecode
import random, string
from playsound import playsound
import sys

## Hangman Class 
class Hangman(Ui_MainWindow):
    # Setup
    def __init__(self, window):
        # Game engine setup
        self.stage = 'img/draw_forca-6.png'
        self.word_list = wl.word_list
        self.chosen_word = ''
        self.display = list() 
        self.invisible_keys = list()
        self.lives = 6
        self.end_of_game = False
        self.guessed = list()

        # UI setup
        self.setupUi(window)

        self.btA.clicked.connect(lambda: self.click_keyboard(self.btA, 'A'))
        self.btB.clicked.connect(lambda: self.click_keyboard(self.btB, 'B'))
        self.btC.clicked.connect(lambda: self.click_keyboard(self.btC, 'C'))
        self.btD.clicked.connect(lambda: self.click_keyboard(self.btD, 'D'))
        self.btE.clicked.connect(lambda: self.click_keyboard(self.btE, 'E'))
        self.btF.clicked.connect(lambda: self.click_keyboard(self.btF, 'F'))
        self.btG.clicked.connect(lambda: self.click_keyboard(self.btG, 'G'))
        self.btH.clicked.connect(lambda: self.click_keyboard(self.btH, 'H'))
        self.btI.clicked.connect(lambda: self.click_keyboard(self.btI, 'I'))
        self.btJ.clicked.connect(lambda: self.click_keyboard(self.btJ, 'J'))
        self.btK.clicked.connect(lambda: self.click_keyboard(self.btK, 'K'))
        self.btL.clicked.connect(lambda: self.click_keyboard(self.btL, 'L'))
        self.btM.clicked.connect(lambda: self.click_keyboard(self.btM, 'M'))
        self.btN.clicked.connect(lambda: self.click_keyboard(self.btN, 'N'))
        self.btO.clicked.connect(lambda: self.click_keyboard(self.btO, 'O'))
        self.btP.clicked.connect(lambda: self.click_keyboard(self.btP, 'P'))
        self.btQ.clicked.connect(lambda: self.click_keyboard(self.btQ, 'Q'))
        self.btR.clicked.connect(lambda: self.click_keyboard(self.btR, 'R'))
        self.btS.clicked.connect(lambda: self.click_keyboard(self.btS, 'S'))
        self.btT.clicked.connect(lambda: self.click_keyboard(self.btT, 'T'))
        self.btU.clicked.connect(lambda: self.click_keyboard(self.btU, 'U'))
        self.btV.clicked.connect(lambda: self.click_keyboard(self.btV, 'V'))
        self.btW.clicked.connect(lambda: self.click_keyboard(self.btW, 'W'))
        self.btX.clicked.connect(lambda: self.click_keyboard(self.btX, 'X'))
        self.btY.clicked.connect(lambda: self.click_keyboard(self.btY, 'Y'))
        self.btZ.clicked.connect(lambda: self.click_keyboard(self.btZ, 'Z'))

        self.btNovaPalavra.clicked.connect(self.new_game)   # NewWord button

        # Choose a new word to start the game
        self.new_game()

    def new_word(self):
        self.chosen_word = random.choice(self.word_list).upper()
        self.display = [c if (c == '-' or c == ' ') else '_' for c in self.chosen_word]

        self.label_display.setText(f'{" ".join(self.display)}')

    def check_guess(self, guess):
        # replacing blank with letters if guessed right
        for pos in range(len(self.chosen_word)):
            if unidecode(self.chosen_word[pos].lower()) == guess.lower():
                self.display[pos] = self.chosen_word[pos]                     

        # Discounting lives if guessed wrong
        if (unidecode(self.chosen_word).lower()).find(guess.lower())==-1:
            self.lives -= 1
            self.stage = f'img/draw_forca-{str(self.lives)}.png'
            self.label_forca.setPixmap(QtGui.QPixmap(self.stage))

            self.guessed += guess.upper()
            self.label_guessed.setText(f'{" ".join(self.guessed)}')

            self.label_lives.setText(str(self.lives))
            
        self.label_display.setText(f'{" ".join(self.display)}')

    def check_end(self):
        # Checking if there is any life still
        if self.lives <= 0:
            self.end_of_game = True    
            self.lock_keyboard()        
            self.show_popup(status='l')            

        if '_' not in self.display:
            self.end_of_game = True
            self.label_forca.setPixmap(QtGui.QPixmap('img/draw_forca-right.png'))
            self.lock_keyboard()             
            self.show_popup(status='w')
            
        
    def click_keyboard(self, bt_name, letter):
        self.label_display.setText(letter)
        bt_name.setVisible(False)
        self.invisible_keys += bt_name.text()        
        
        self.check_guess(letter)
        self.check_end()

    def lock_keyboard(self, off=False):
        if not off:
            for ch in string.ascii_uppercase:
                bt = MainWindow.findChild(QPushButton, f'bt{ch}')
                bt.setEnabled(False)
        else:
            for ch in string.ascii_uppercase:
                bt = MainWindow.findChild(QPushButton, f'bt{ch}')
                bt.setEnabled(True)

    def new_game(self):
        # Reshow Keyboard
        if self.invisible_keys:
            for ch in self.invisible_keys:
                obj = MainWindow.findChild(QPushButton, "bt{}".format(ch))
                obj.setVisible(True)
            self.invisible_keys = list()

        # Choose and display new word
        self.new_word()

        # Reset lives
        self.lives = 6
        self.label_lives.setText(str(self.lives))
        
        # Reset hang image
        self.stage = 'img/draw_forca-6.png'
        self.label_forca.setPixmap(QtGui.QPixmap('img/draw_forca-6.png'))

        # Reset Guessed Label
        self.guessed = list()
        self.label_guessed.setText('')

        # Unlock keyboard
        self.lock_keyboard(off=True)

        # New word sound
        playsound('sound/start.wav')

    def show_popup(self, status='w'):
        msg = QMessageBox()

        if status == 'w':
            msg.setWindowTitle('Você acertou!')
            txt = 'Parabéns!!\nQue tal mais uma rodada? :)'
            msg.setText(txt)

        elif status == 'l':
            msg.setWindowTitle('Você perdeu!')
            txt = 'Que pena!\nMas que tal jogar mais uma vez?'
            info_txt = f'\nA palavra era:\n{self.chosen_word.upper()}'
            
            msg.setText(txt)
            msg.setInformativeText(info_txt)

        msg.setIcon(QMessageBox.Information) 
        msg.exec_() 
        

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

## Create an instance of the app
game = Hangman(MainWindow)

## Show window and start the app
MainWindow.show()
sys.exit(app.exec_())

## EOF ##