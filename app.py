
from movie import Movie, get_movies
from PySide2 import QtWidgets, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        """
        Création de l'interface graphique
        """
        self.layout = QtWidgets.QVBoxLayout(self)
        self.lw_movie_title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movie = QtWidgets.QListWidget()
        self.lw_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.lw_movie_title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.lw_movie)
        self.layout.addWidget(self.btn_delete_movie)
    
    def setup_connections(self):
        """
        Connection des widgets au méthodes avec les signaux clicked pour les bouton et returnPressed pour la touche entrée du clavier
        """
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_delete_movie.clicked.connect(self.remove_movie)
        self.lw_movie_title.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        """
        Affiche les films dans l'interface graphique présent dans le fichier movie.json
        """
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            self.lw_movie.addItem(lw_item)
    
    def add_movie(self):
        """
        Ajoute un film à la liste et l'affiche sur l'interface
        """
        title = self.lw_movie_title.text()
        if not title :
            return False
        
        movie = Movie(title)
        result = movie.add_to_movies()
        
        self.lw_movie_title.setText("")

        if not result:
            return False
        
        lw_item = QtWidgets.QListWidgetItem(movie.title)
        lw_item.movie = movie
        self.lw_movie.addItem(lw_item)
        
        
    def remove_movie(self):
        """
        Supprime un ou plusieurs films
        """
        for selected_item in self.lw_movie.selectedItems():
            movie = selected_item.movie
            movie.remove_from_movies()
            self.lw_movie.takeItem(self.lw_movie.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()