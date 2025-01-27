import tkinter as tk

window = tk.Tk()
window.geometry("900x900")


window.rowconfigure([0,1,2,3,4,5,6,7,8,9], minsize=85)
window.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize=85)

see_dex = tk.Button(text = "See Pokedex", fg="black")
see_dex.grid(row=3, column=1, sticky = "ew", padx=5)

see_dex = tk.Button(text = "Make your team", fg="black")
see_dex.grid(row=3, column=4, sticky="ns", padx=5)

see_dex = tk.Button(text = "See teams from anime", fg="black")
see_dex.grid(row=3, column=7, sticky="nsew", padx=5)


loop = "True"
while loop == "True":
    window()
