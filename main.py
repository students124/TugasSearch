from xml.etree.ElementTree import TreeBuilder
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

    k = G.weight()
    print(k)

    k = G.weightToExcel()
    print(k)

    G.printExcel()

    while True:
        src_node = int(input("Source Node : "))
        fn_node = int(input("Final Node : "))
        algorithm = input("algorthm to solve (inform/uninform) : ").lower()

        match algorithm:
            case "inform":
                G.best_first_search(src_node, fn_node)
            case "uninform" : 
                print(G.bfs(src_node, fn_node))
            case _:
                print("The input was incorrect please try again")
        
        is_continue = input("continue? (Y/N)").upper()

        match is_continue:
            case "Y":
                ...
            case "N":
                break

if __name__ == "__main__":
    main()