note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

moyelev1 = (notes[0][2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print("la moyenne de l'élévé 1 = ",moyelev1)
#4)b
moyelev1_math = (notes[0][2]+notes[2][2]+notes[5][2])/3
print("la moyenne de l'élévé 1 en math = ",moyelev1_math)
#4)c
notes_tuples = [note1, note2, note3, note4, note5, note6,note7,note8]
def moyenne():
    eleve = input("Entrez le nom de l'élève: ")
    matiere  = input("Choisissez la matière: ")
    cpt = 0
    moyenne = 0
   
    for i in range(8):
        if(notes_tuples[i][0] == eleve):
            if(notes_tuples[i][1] == matiere):
                moyenne += notes_tuples[i][2]
                cpt += 1
    moyenne = moyenne/cpt
    print(moyenne)
               
moyenne()

#6)
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
   
    def afficherNote(self):
        print(self.valeur)
       
onote = Note('eleve1', 'maths', 13)
onote.afficherNote()


