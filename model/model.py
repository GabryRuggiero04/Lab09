import mysql
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        #creazione grafo non orientato
        self._grafo=nx.Graph()
        #lista di tutti aeroporti = lista nodi
        self._aeroporti=DAO.allNodes()
        self._mappaAeroporti={}
        for a in self._aeroporti:
            self._mappaAeroporti[a.ID]=a
        self._mappaConnessioni = {}
        for v in DAO.allEdges():
            chiave= tuple(sorted([v[0],v[1]]))
            if chiave not in self._mappaConnessioni.keys():
                self._mappaConnessioni[chiave]=[0,0]
            self._mappaConnessioni[chiave][0]+=v[2]
            self._mappaConnessioni[chiave][1]+=1



    def buildGraph(self, disMin):
        self._grafo.clear()
        #aggiunta dei nodi al grafo (tutti aeroporti)
        self._grafo.add_nodes_from(self._aeroporti)
        #metodo che aggiunge gli archi tra i nodi che rispettano le condizioni
        self.addEdges2(disMin)
        return self._grafo

    def addEdges(self,disMin):
        for a1 in self._aeroporti:
            for a2 in self._aeroporti:
                peso=DAO.edges(a1,a2)
                if peso>=disMin:
                    self._grafo.add_edge(a1,a2,weight=peso[0])

    def addEdges2(self, disMin):
        for k in self._mappaConnessioni.keys():
                media=(self._mappaConnessioni[k][0]/self._mappaConnessioni[k][1])
                if media>=disMin:
                    self._grafo.add_edge(self._mappaAeroporti[k[0]], self._mappaAeroporti[k[1]],weight=media)



    def numEdges(self):
        return len(self._grafo.edges())

    def numNodes(self):
        return len(self._grafo.nodes())