# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

### Inicio importações
import tkinter as tk
from tkinter import ttk
# Explicit imports to satisfy Flake8
from tkinter import HORIZONTAL, Scale, Tk, Canvas, Button
from Shoreline import Shoreline 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
### Fim importações

class ExtratorLinhasCosteiras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Extrator de Linhas Costeiras")
        ### Inicio Configuarações de dimensões e posicionamento da janela
        height = 590
        width = 1140

        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()

        posiX = (width_screen/2) - (width/2)
        posiY = ((height_screen-(height_screen * 0.08))/2) - (height/2)

        self.geometry("%dx%d+%d+%d" % (width, height, posiX, posiY))
        self.resizable(False, False)
        self.configure(bg = "#EBEBEB")

        self.construtor_interface()
        ### Fim configuarações de dimensões e posicionamento da janela

    # @staticmethod
    def construtor_interface(self):
        canvas = Canvas(
            self,
            bg = "#EBEBEB",
            height = 560,
            width = 1140,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1140.0,
            560.0,
            fill="#EBEBEB",
            outline=""
        )

        ### Inicio Adicionando o menu a janela
        menu = tk.Menu(self)

        # File Menu
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(
            label="Abrir Imagem", 
            command= lambda: 
                Shoreline.plot_image_original(Shoreline,
                    figure_original,
                    image_original)),
        file_menu.add_separator()
        file_menu.add_command(label="Sair")
        menu.add_cascade(label="Arquivo", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label="Sobre")
        menu.add_cascade(label="Ajuda", menu=help_menu)

        self.config(menu=menu)
        ### Fim adicionando o menu a janela

        ### Inicio Adição e posicionamento dos "images views" na janela
        canvas.create_text(
            233.0,
            31.0,
            anchor="nw",
            text="Imagem Original",
            fill="#333742",
            font=("Inter Medium", 20 * -1)
        )
        
        figure_original = Figure(
            figsize=(5, 3.8), 
            dpi=100, 
            facecolor="#FFFFFF",
            edgecolor="#B7B9BF",
            linewidth=2, 
            )

        image_original = FigureCanvasTkAgg(figure_original, master=self)
        image_original.draw()

        image_original.get_tk_widget().place(
            x=64,
            y=77,
            width=494,
            height=272,
        )

        canvas.create_text(
            716.0,
            31.0,
            anchor="nw",
            text="Linha de Costa Extraída",
            fill="#333742",
            font=("Inter Medium", 20 * -1)
        )

        figure_filtered = Figure(
            figsize=(5, 3.3), 
            dpi=100, 
            facecolor="#FFFFFF",
            edgecolor="#B7B9BF",
            linewidth=2,
        )

        image_filtered = FigureCanvasTkAgg(figure_filtered, master=self)
        image_filtered.draw()

        image_filtered.get_tk_widget().place(
            x=582,
            y=77,
            width=494,
            height=272,
        )
        ### Fim Adição e posicionamento dos "images views" na janela

        ### Inicio Configurações de filtros

        ### Inicio Filtro Gaussiano
        scale_filtro_gaussiano = Scale(
            self,
            from_=1,
            to=255,
            width=6,
            orient=HORIZONTAL,
            resolution=1,
            font=("Inter Medium", 16 * -1),
            background="#EBEBEB",
            activebackground="#1D5FFE",
            foreground="#333742",
            highlightthickness=0,
            troughcolor="#B7B9BF",
            sliderlength=25,
            sliderrelief="flat"
        )

        scale_filtro_gaussiano.place(
            x=436,
            y=379,
            width=640,
            height=53
        )

        canvas.create_text(
            694.0,
            433.0,
            anchor="nw",
            text="Filtro Gaussiano",
            fill="#333742",
            font=("Inter Medium", 16 * -1)
        )

        ### Fim Filtro Gaussiano

        ### Inicio Filtro Tras. Morforlogica
        scale_transformacao_morfologica = Scale(
            self,
            from_=0,
            to=255,
            width=6,
            orient=HORIZONTAL,
            resolution=1,
            font=("Inter Medium", 16 * -1),
            background="#EBEBEB",
            activebackground="#1D5FFE",
            foreground="#333742",
            highlightthickness=0,
            troughcolor="#B7B9BF",
            sliderlength=25,
            sliderrelief="flat"
        )

        scale_transformacao_morfologica.place(
            x=436,
            y=460,
            width=640,
            height=53
        )

        canvas.create_text(
            650.0,
            510.0,
            anchor="nw",
            text="Transformação Morfológica",
            fill="#333742",
            font=("Inter Medium", 16 * -1)
        )
        ### Fim Filtro Tras. Morforlogica

        ### Fim Configurações de filtros

        progress_bar = ttk.Progressbar(
                self,
                orient='horizontal',
                mode='indeterminate',
                length=280, 
        )

        progress_bar.place(
            x=64,
            y=530,
            width=312,
            height=10,
        )

        ### Inicio Botões
        button_aplicar = Button(
            text="Aplicar Filtros",
            font=("Inter Medium", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            background="#1D5FFE",
            foreground="#FFFFFF",
            relief="flat",
            activebackground="#1D5FFE",
            activeforeground="#FFFFFF",
            command= lambda: Shoreline.apply_filter(Shoreline,
                value_fG= scale_filtro_gaussiano.get(),
                value_tM= scale_transformacao_morfologica.get(),
                figure_filtered= figure_filtered,
                image_filtered= image_filtered,
                progress_bar=progress_bar
                )
        )

        button_aplicar.place(
            x=64.0,
            y=379.0,
            width=312.0,
            height=60.0
        )

        button_exportar = Button(
            text="Exportar GeoTIFF",
            font=("Inter Medium", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            background="#35C769",
            foreground="#FFFFFF",
            relief="flat",
            activebackground="#35C769",
            activeforeground="#FFFFFF",
            # command= lambda: ConvertLine.exportShapeFile()
        )

        button_exportar.place(
            x=64.0,
            y=463.0,
            width=312.0,
            height=60.0
        )
        ### Fim Botões

if __name__ == "__main__":
    app = ExtratorLinhasCosteiras()
    app.mainloop()