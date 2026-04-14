import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#ventana de la Portada (parte 1)
def mostrar_portada():
    portada = tk.Tk()
    portada.title("Lista de Tareas")
    portada.geometry("600x500")
    portada.config(bg="#FFC0CB")

    # título(parte 2)
    titulo = tk.Label(portada, text="Lista de Tareas", font=("Lucida Handwriting", 32, "bold"), bg="#FFC0CB")
    titulo.pack(pady=30)

    # boton para Empezar(parte 3)
    def empezar():
        portada.destroy()
        ventana_principal()

    boton = tk.Button(
        portada, text="Empezar", font=("Lucida Handwriting", 18, "bold"),
        bg="#FF69B4", fg="white", padx=30, pady=10,
        relief="raised", bd=5, command=empezar
    )
    boton.pack(pady=20)

    # texto
    explicacion = tk.Label(
        portada,
        text="este programa te ayuda a organizar tus tareas diarias presiona 'Empezar' para añadir, ver o eliminar tus tareas",
        font=("Lucida Handwriting", 12),
        bg="#FFC0CB",
        justify="center"
    )
    explicacion.pack(pady=20)

    # emoji
    decoracion = tk.Label(portada, text="📝 ✅ 🗒️", font=("Lucida Handwriting", 20), bg="#FFC0CB")
    decoracion.pack(side="bottom", pady=20)

    portada.mainloop()

# ventana de tareitas
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Mis Tareas")
    ventana.geometry("600x550")
    ventana.config(bg="#FFF0F5")

    tareas = []
    tareas_completadas = set()

    # funciones
    def agregar_tarea():
        tarea = entrada.get()
        if tarea:
            tareas.append(tarea)
            actualizar_lista()
            entrada.delete(0, tk.END)
            actualizar_barra()
        else:
            messagebox.showwarning("atencion", "Ingrese una tarea")

    def eliminar_tarea():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            tareas.pop(index)
            tareas_completadas.discard(index)
            actualizar_completadas_indices(index)
            actualizar_lista()
            actualizar_barra()
        else:
            messagebox.showwarning("atencion", "Seleccione una tarea para eliminar")

    def actualizar_completadas_indices(eliminado_index):
        nuevas = set()
        for i in tareas_completadas:
            if i < eliminado_index:
                nuevas.add(i)
            elif i > eliminado_index:
                nuevas.add(i - 1)
        tareas_completadas.clear()
        tareas_completadas.update(nuevas)

    def marcar_como_hecha():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            if index in tareas_completadas:
                messagebox.showinfo("info", "la tarea ya está marcada como hecha")
            else:
                tareas_completadas.add(index)
                actualizar_lista()
                actualizar_barra()
        else:
            messagebox.showwarning("atencion", "seleccione una tarea para marcar como hecha")

    def actualizar_lista():
        lista.delete(0, tk.END)
        for i, t in enumerate(tareas):
            icono = "✅" if i in tareas_completadas else "📝"
            lista.insert(tk.END, f"{icono} {t}")

    def actualizar_barra():
        if tareas:
            progreso['maximum'] = len(tareas)
            progreso['value'] = len(tareas_completadas)
            barra_label.config(text=f"tareas completadas: {len(tareas_completadas)}/{len(tareas)}")

            # mensaje de felicitaciones 
            if len(tareas_completadas) == len(tareas):
                felicidades_label.config(text="¡felicidades! Has cumplido las tareas de hoy 🎉")
            else:
                felicidades_label.config(text="")
        else:
            progreso['maximum'] = 1
            progreso['value'] = 0
            barra_label.config(text="tareas completadas: 0/0")
            felicidades_label.config(text="")

    # botones lindos
    # título arriba 
    titulo_ventana = tk.Label(ventana, text="Mis Tareas", font=("Lucida Handwriting", 20, "bold"), bg="#FFF0F5")
    titulo_ventana.place(x=10, y=10)  # Posición arriba izq

    entrada = tk.Entry(ventana, font=("Lucida Handwriting", 14))
    entrada.pack(pady=50)

    boton_agregar = tk.Button(ventana, text="agregar Tarea", font=("Lucida Handwriting", 12), command=agregar_tarea, bg="#FFB6C1")
    boton_agregar.pack(pady=5)

    boton_eliminar = tk.Button(ventana, text="eliminar Tarea", font=("Lucida Handwriting", 12), command=eliminar_tarea, bg="#FFB6C1")
    boton_eliminar.pack(pady=5)

    boton_hecha = tk.Button(ventana, text="marcar como hecha", font=("Lucida Handwriting", 12), command=marcar_como_hecha, bg="#FF69B4", fg="white")
    boton_hecha.pack(pady=5)

    lista = tk.Listbox(ventana, width=50, height=10, font=("Lucida Handwriting", 12))
    lista.pack(pady=20)

    # barra
    barra_label = tk.Label(ventana, text="tareas completadas: 0/0", font=("Lucida Handwriting", 12), bg="#FFF0F5")
    barra_label.pack()

    progreso = ttk.Progressbar(ventana, orient="horizontal", length=400, mode="determinate")
    progreso.pack(pady=10)

    # mensaje de felicitaciones
    felicidades_label = tk.Label(ventana, text="", font=("Lucida Handwriting", 14, "bold"), bg="#FFF0F5", fg="green")
    felicidades_label.pack(pady=10)

    ventana.mainloop()

#ejecutar 
mostrar_portada()