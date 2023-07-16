from VentanaPrincipal import VentanaPrincipal;
from ManejadorJson import ManejadorJson
from ConexionDB import ConexionDB
import tkinter as tk;
root=tk.Tk();
administradorDeFechas=ManejadorJson("eventos.json");
conexionDB=ConexionDB()
app = VentanaPrincipal(root, administradorDeFechas, conexionDB)
app.grid();
root.mainloop();