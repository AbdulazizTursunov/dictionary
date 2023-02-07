from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget
from PyQt5.QtGui import QFont

class NewWord(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.list_eng = []
        self.list_uzb = []

        self.v_lang_lay = QVBoxLayout()
        self.h_lang_btn_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("Eng...")
        self.eng_edit.setStyleSheet("""background-color:red; 
                                            2px border: black; """)

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uz...")
        self.uz_edit.setStyleSheet("""background-color: black; 
                                            2px border: black;""")

        self.v_lang_lay.addWidget(self.eng_edit)
        self.v_lang_lay.addWidget(self.uz_edit)

        self.add_btn = QPushButton("send")
        self.add_btn.setStyleSheet("background-color:lightgreen;")
        self.ownfont(self.add_btn, 30,30)
        self.add_btn.clicked.connect(self.write_to_file)

        self.h_lang_btn_lay.addLayout(self.v_lang_lay)
        self.h_lang_btn_lay.addWidget(self.add_btn)

        self.result_label = QLabel("")

        self.menu_btn = QPushButton("MENU")
        self.menu_btn.setStyleSheet("background-color:lightgreen;")
        self.ownfont(self.menu_btn, 30,30)
        self.menu_btn.clicked.connect(self.menu)
        self.h_btn_lay.addWidget(self.menu_btn)

        self.v_main_lay.addLayout(self.h_lang_btn_lay)
        self.v_main_lay.addWidget(self.result_label)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def write_to_file(self):
        self.list_eng.append(self.eng_edit.text())
        self.list_uzb.append(self.uz_edit.text())
        self.eng_edit.setText("")
        self.uz_edit.setText("")
        print(self.list_eng, self.list_uzb)

    def menu(self):
        self.hide()

    def ownfont(self, obj, x, y):
        obj.setFont(QFont("Times", 10))
        obj.move(x, y)

class ListWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.h_lang_lay = QHBoxLayout()
        self.h_list_wdg_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_lb = QLabel("English")
        self.uz_lb = QLabel("Uzbek")

        self.h_lang_lay.addWidget(self.eng_lb)
        self.h_lang_lay.addWidget(self.uz_lb)

        self.eng_wdg = QListWidget()
        self.uz_wdg = QListWidget()

        self.h_list_wdg_lay.addWidget(self.eng_wdg)
        self.h_list_wdg_lay.addWidget(self.uz_wdg)

        self.menu_btn = QPushButton("MENU")
        self.ownFont(self.menu_btn, 20,20)
        self.menu_btn.setStyleSheet("background-color: lightgreen;")
        self.menu_btn.clicked.connect(self.menu)

        self.h_btn_lay.addWidget(self.menu_btn)

        self.v_main_lay.addLayout(self.h_lang_lay)
        self.v_main_lay.addLayout(self.h_list_wdg_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def ownFont(self, obj, x, y):
        obj.setFont(QFont("Times", 10))
        obj.move(x, y)

    def menu(self):
        self.hide()

class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.lst = []
        self.son=str()
        self.v_lang_lay = QVBoxLayout()
        self.h_lang_btn_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.Ownfont(self.eng_edit, 30,30)
        self.eng_edit.setPlaceholderText("english...")

        self.uzb_edit = QLabel("salom",self)
        # self.uzb_edit.setPlaceholderText("...")

        self.v_lang_lay.addWidget(self.eng_edit)
        self.v_lang_lay.addWidget(self.uzb_edit)
        self.setFixedSize(200,200)

        self.btn_search = QPushButton("search")
        self.Ownfont(self.btn_search, 10, 10)
        self.btn_search.setStyleSheet("background-color:lightgreen")
        self.btn_search.clicked.connect(self.kim)

        self.h_lang_btn_lay.addLayout(self.v_lang_lay)
        self.h_lang_btn_lay.addWidget(self.btn_search)

        self.menu_btn = QPushButton("menu")
        self.Ownfont(self.menu_btn, 30, 30)
        self.menu_btn.setStyleSheet("background-color:lightgreen")
        self.menu_btn.clicked.connect(self.menu_search)
        self.h_btn_lay.addWidget(self.menu_btn)

        self.v_main_lay.addLayout(self.h_lang_btn_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    indeqs = str()
    count = 0
    def kim(self):
        self.son=(self.eng_edit.text())
        for i in self.english:
            if self.son == i:
                self.indeqs = str(self.english.index(i))
                self.uzb_edit.setText(self.lst[int(self.indeqs)])
            
    def func_search(self, eng, uzb):
        self.english = eng
        self.uzbek = uzb
        for i in self.uzbek:
            self.lst.append(i)
            print(i)

    
    def Ownfont(self, obj, x, y):
        obj.setFont(QFont("Times", 10))
        obj.move(x, y)

    def  menu_search(self):
        self.hide()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.new_word_window = NewWord()
        self.list_window = ListWindow()
        self.search_window = Search()

        self.setFixedSize(300,400)
        self.add_btn = QPushButton("ADD", self)
        self.add_btn.setStyleSheet("background-color:lightgreen;")
        self.list_btn = QPushButton("LIST", self)
        self.list_btn.setStyleSheet("background-color:lightgreen;")
        self.search_btn = QPushButton("SEARCH", self)
        self.search_btn.setStyleSheet("background-color:lightgreen;")
        self.exit_btn = QPushButton("EXIT", self)
        self.exit_btn.setStyleSheet("background-color:lightgreen;")

        self.add_btn.setGeometry(100, 100, 100, 45)
        self.list_btn.setGeometry(100, 170, 100, 45)
        self.search_btn.setGeometry(100, 240, 100, 45)
        self.exit_btn.setGeometry(100, 310, 100, 45)

        self.add_btn.clicked.connect(self.win1_connect)
        self.list_btn.clicked.connect(self.win2_connect)
        self.search_btn.clicked.connect(self.win3_connect)
        self.exit_btn.clicked.connect(self.close)

        self.show()

    def oWnfont(self, obj, x, y):
        obj.QFond(QFont("Times", 20))
        self.move(x, y)
    
    def win1_connect(self):
        self.new_word_window.show()
        for i in self.new_word_window.list_eng:
            pass
            
    def win2_connect(self):
        self.list_window.show()
        for i in self.new_word_window.list_eng:
            self.list_window.eng_wdg.insertItem(0,i)
        for i in self.new_word_window.list_uzb:
            self.list_window.uz_wdg.insertItem(0,i)
       
    def win3_connect(self):
        self.search_window.func_search(self.new_word_window.list_eng, self.new_word_window.list_uzb)
        self.search_window.show()

app = QApplication([])
win = MainWindow()
app.exec_()

