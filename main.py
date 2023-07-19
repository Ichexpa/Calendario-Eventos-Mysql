from VentanaPrincipal import VentanaPrincipal;
from ConexionDB import ConexionDB
import tkinter as tk;
root=tk.Tk();
conexionDB=ConexionDB()
app = VentanaPrincipal(root, conexionDB)
app.grid();
root.mainloop();