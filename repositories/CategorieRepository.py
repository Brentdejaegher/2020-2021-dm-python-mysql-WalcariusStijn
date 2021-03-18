
from models.Categorie import Categorie
from repositories.Database import Database


class CategorieRepository:

    @staticmethod
    def read_all():
        categories = []
        sql ="SELECT Categorienummer, Categorienaam, "
        sql += "Bijschrijving FROM artemis.tblcategorieen" 
        rows = Database.get_rows(sql)
    
        if not (rows is None):
            for row in rows:
                #mapping naar object
                categories.append( CategorieRepository.map_to_object(row) )
        return categories


    @staticmethod
    def map_to_object(row):
        nummer = int(row['Categorienummer'])
        if 'Categorienaam' in row.keys():
            naam =  row['Categorienaam']
        else:
            naam =  ""
        if 'Bijschrijving' in row.keys() and row['Bijschrijving'] is not None:
            beschrijving = row['Bijschrijving']  
        else:
            beschrijving = ""
        return Categorie(nummer, naam ,beschrijving)
   