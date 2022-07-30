### Inicio importações
from random import random
import rasterio
import cv2
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
### Fim importações

class Shoreline:

    global_path = ""

    def convert_image_png():
        pass

    def apply_filter(value_fG, value_tM, value_fC, figure_filtered, image_filtered):

        file = Path(Shoreline.global_path).suffix
        if(Shoreline.global_path == ""):
            messagebox.showerror(
                title="Nenhuma imagem selecionada",
                message="Selecione uma imagem para que possa aplicar os filtos",
            )
        elif(file != ".tif"):
            messagebox.showerror(
                title="Erro no formato da Imagem",
                message="A extensão da imagem está incorreta. Extensão correta: .tif"
            )
        else:
            banda = Shoreline.converter_imagem_array_numpy(Shoreline.global_path)
            filtro_G = Shoreline.filtro_gaussiano(banda, value_fG)
            trans_M = Shoreline.transformacao_morfologica(filtro_G, value_tM)
            thre = Shoreline.threshold(trans_M, 0)
            image_final = Shoreline.extração_bordas(thre, value_fC)

            # Shoreline.exibir(image_final)
            Shoreline.plot_image_filtered(figure_filtered, image_filtered, image_final)

    def open_image():
        dataset_path = filedialog.askopenfilename(
        initialdir = "/Downloads/",
        title = "Selecione a imagem",
        filetypes = (("Arquivos tif", "*.tif"), ("Todos os arquivos", "*.*")))
    
        Shoreline.global_path = dataset_path

        return dataset_path

    def plot_image_original(figure_original, image_original):
        path = Shoreline.open_image()

        ax = figure_original.add_subplot(111)
        figure_original.subplots_adjust(bottom=0, right=1, top=1, left=0, wspace=0, hspace=0)

        with rasterio.open(r''f'{path}') as src_plot:
            show(src_plot, ax=ax, cmap='gist_gray')
        plt.close()
        ax.set(title="",xticks=[], yticks=[])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        image_original.draw()

    def plot_image_filtered(figure_filtered, image_filtered, image_final):
        # path = Shoreline.open_image()
        
        ax = figure_filtered.add_subplot(111)
        figure_filtered.subplots_adjust(bottom=0, right=1, top=1, left=0, wspace=0, hspace=0)

        with rasterio.open(r''f'{image_final}') as src_plot:
            show(src_plot, ax=ax, cmap='gist_gray')
        plt.close()
        ax.set(title="",xticks=[], yticks=[])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        image_filtered.draw()

### -------------------------------------------------------------------------###

### Início Método 2
    def converter_imagem_array_numpy(path):
        image_banda = rasterio.open(path)
        banda = image_banda.read(1)

        return banda
### Fim Método 2

### Início Método 3
    def filtro_gaussiano(banda, value):
    # value tem que ser positivo e ímpar
        if(value % 2 == 0):
            value += 1
        
        filtro_gaussiano = cv2.GaussianBlur(banda, (value, value), 0)
        return filtro_gaussiano
### Fim Método 3

    ### Início Método 4
    def transformacao_morfologica(filtro_gaussiano, value):

        kernel = np.ones((value,value), np.uint8)
        transformacao_morfologica = cv2.morphologyEx(filtro_gaussiano, cv2.MORPH_OPEN, kernel)

        return transformacao_morfologica
### Fim Método 4

### Início Método 5
    def threshold(transformacao_morfologica, value):
        _,threshold = cv2.threshold(transformacao_morfologica, value, 255, cv2.THRESH_BINARY_INV);

        return threshold
### Fim Método 5

### Início Método 5
    def extração_bordas(threshold, value):
        im_outCopy = np.uint8(threshold)
        image_final = cv2.Canny(im_outCopy,value,200)
        
        path_image_filtered = "assets/image/image_filtered.tif"

        cv2.imwrite(f"{path_image_filtered}", image_final)
        
        return path_image_filtered
    ### Fim Método 5

    def exibir(image):
        cv2.imshow("Bordas", image)
        cv2.waitKey(0)