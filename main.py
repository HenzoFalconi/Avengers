from model.database import Database
from model.interface import Interface
from model.vingadores import Vingador

def main():
    db - Database()
    db.connect()

    query = 'SELECT * FROM heroi'
    herois = db.select(query)
    for heroi in herois:
        Vingador(heroi[1], heroi [2], heroi[3],heroi[4], heroi [5], heroi[6],heroi[7], heroi [8], heroi[9],heroi[10], heroi [11], heroi[12],heroi[13], heroi [14], heroi[15],heroi[16])

if __name__ == "__main__":
    main()
