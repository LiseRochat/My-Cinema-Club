from PySide2 import QtWidgets 

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon ciné Club")
        self.setup_ui()
    
    def setup_ui(self):
        """
        Création de l'interface graphique
        """
        self.layout = QtWidgets.QVBoxLayout(self)
        self.line_movie = QtWidgets.QLineEdit()
        self.btn_add_moovie = QtWidgets.QPushButton("Ajouter un film")
        self.list_moovie = QtWidgets.QListWidget()
        self.btn_delete_moovie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.line_movie)
        self.layout.addWidget(self.btn_add_moovie)
        self.layout.addWidget(self.list_moovie)
        self.layout.addWidget(self.btn_delete_moovie)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()