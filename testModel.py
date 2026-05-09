from model import model
from model.model import Model

mod=Model()
mod.buildGraph(4500)
print(f"Il grafo creato contiene {mod.numNodes()} nodi e "
      f"{mod.numEdges()} archi.")