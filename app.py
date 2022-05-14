
from movie import get_movies
from PySide2 import QtWidgets, QtCore

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
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.list_movie = QtWidgets.QListWidget()
        self.btn_delete_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.line_movie)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.list_movie)
        self.layout.addWidget(self.btn_delete_movie)
    
    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()