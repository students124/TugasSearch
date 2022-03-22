from src import Graph

def main():
    G = Graph()

    k = G.generate(10)
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