from repositories.CategorieRepository import CategorieRepository
from models.Categorie import Categorie
from tabulate import tabulate     #pip install tabulate
from colorama import Fore, init   #pip install  colorama

class CategorieServices:

    @staticmethod
    def print_all_categories():
        # for c in CategorieRepository.read_all():
        #     print(c)        

        #Alternatief: printen in tabel vorm
        table = []
        for cat in CategorieRepository.read_all():
            table.append([cat.categorienummer, cat.categorienaam, cat.beschrijving])
        print(tabulate(table))
        return 