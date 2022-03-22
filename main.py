from src import Graph

def main():
    G = Graph()

    A = int(input("Masukan: "))

    k = G.generate(A)
    print(k)

    k = G.grapToExcel()
    print(k)

    k = G.neighbors()
    print(k)

    k = G.neighborsToExcel()
    print(k)

    G.printExcel()

if __name__ == "__main__":
    main()