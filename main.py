from VentanaPrincipal import VentanaPrincipal;
from ManejadorJson import ManejadorJson
import tkinter as tk;
root=tk.Tk();
administradorDeFechas=ManejadorJson("eventos.json");
app=VentanaPrincipal(root,administradorDeFechas);
app.grid();
root.mainloop();