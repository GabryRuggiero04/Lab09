import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def analisiAeroporti(self, e):
        self._view.txt_result.controls.clear()
        distanza=self._view.txt_distanza.value
        if distanza=="":
            self._view.create_alert("Nessuna distanza inserita")
            self._view.update_page()
            return
        grafo=self._model.buildGraph(float(distanza))
        numNodi=self._model.numNodes()
        numEdges=self._model.numEdges()
        if len(grafo.edges())==0:
            self._view.txt_result.controls.append(
                ft.Text(f"Non ci sono aeroporti con distanza media minima {distanza}", color="red"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Il numero di nodi del grafo è: {numNodi}", color="blue")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Il numero di archi del grafo è: {numEdges}", color="blue")
        )
        self._view.txt_result.controls.append(
            ft.Text("Gli archi sono: ", color="blue")
        )
        for e in grafo.edges():
            self._view.txt_result.controls.append(
                ft.Text(f"Partenza: {e[0]} -----> Destinazione: {e[1]}")
            )
        self._view.update_page()
