class Categorie:

    def __init__(self, par_categorienummer, par_categorienaam, par_beschrijving):
        self._valueErrors = {}  #eerst
        self.categorienummer = par_categorienummer
        self.categorienaam = par_categorienaam
        self.beschrijving = par_beschrijving
       

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return (len(self._valueErrors) == 0 )
     
    @property
    def categorienummer(self):
        return self._categorienummer

    @categorienummer.setter
    def categorienummer(self, value):
        if type(value) is int:
            self._categorienummer = value
        else:
            self._valueErrors['categorienummer'] = ValueError("Geen geldig categorienummer")
            #raise ValueError("Geen geldig categorienummer!")
            

    @property
    def categorienaam(self):
        return self._categorienaam

    @categorienaam.setter
    def categorienaam(self, value):
        if type(value) == str and value != "":
            self._categorienaam = value
        else:
            self._valueErrors['categorienaam'] = ValueError("Geen geldige categorienaam")
            #raise ValueError("Een geldige categorienaam is verplicht!")

    @property
    def beschrijving(self):
        return self._beschrijving

    @beschrijving.setter
    def beschrijving(self, value=None):
        #beschrijving mag "" of None zijn, maar heeft een maxLength
        if type(value) == str  or (value is None):
            self._beschrijving = value
        else:
            self._valueErrors['beschrijving'] = ValueError("Geen geldige beschrijving")

        if (value is not None) and len(value) > 60 :
            self._valueErrors['beschrijving lengte'] = ValueError("Maximaal 60 karakters.")


    def __str__(self):
        return f"\n{self.categorienummer}\t\t{self.categorienaam} \t\t{self.beschrijving}  "
    
    def __repr__(self):
        return [{self.categorienummer}, {self.categorienaam},{self.beschrijving}]