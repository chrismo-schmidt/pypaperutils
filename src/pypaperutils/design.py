# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:50:26 2023

pypaperutils.design

colors and other design elements

@author: Christoph M. Schmidt
"""

import numpy as np

class TUDcolors:
    """Colors of the TU Delft corporate image as of 20-09-2023.
    
    https://www.tudelft.nl/huisstijl/bouwstenen/kleur
    
    """ 
    
    PALETTE = ((  0, 166, 214),     #Cyaan
               ( 12,  35,  64),     #Donkerblauw
               (  0, 184, 200),     #Turkoois
               (  0, 118, 194),     #Blauw
               (111,  29, 119),     #Paars
               (239,  96, 163),     #Roze
               (165,   0,  52),     #Framboos
               (224,  60,  49),     #Rood
               (237, 104,  66),     #Oranje
               (255, 184,  28),     #Geel
               (108, 194,  74),     #Lichtgroen
               (0,   155, 119))     #Donkergroen
    
    COLORNAMES = ("cyaan", "donkerblauw", "turkoois", "blau", "paars", "roze",
                  "framboos", "rood", "oranje", "geel", "lichtgroen", 
                  "donkergroen")
    
    def __init__(self):
        self.colors = dict(zip(self.COLORNAMES, self.PALETTE))
        self.colornames = self.COLORNAMES
        self.palette = self.PALETTE

    def get(self, colors, dtype="float"):
        """Get a color by name or index.
        
        0 - "cyaan"
        1 - "donkerblauw"
        2 - "turkoois"
        3 - "blau"
        4 - "paars"
        5 - "roze",
        6 - "framboos"
        7 - "rood"
        8 - "oranje"
        9 - "geel"
        10 - "lichtgroen"
        11 - "donkergroen"
        

        Parameters
        ----------
        color : int, str, or list thereof
            Identifiers of the color. May be a string with the color name or 
            the color id. 
        dtype : str, default = "float"
            Return colors as floats in [0,1] ("float") or integers in [0,255] 
            ("int")

        Returns
        -------
        RGB color triplets. 

        """
        if not dtype in ("float", "int"):
            raise ValueError(f"The parameter dtype has to be either 'float' \
                             or 'int', instead it was '{dtype}'.")
    
        if not isinstance(colors, list) and not isinstance(colors, tuple):
            colors = (colors,)
            islist = False
        else:
            islist = True
            
        rgbtriplets = []
        
        if isinstance(colors[0], str):
            for name in colors:
                val = np.array(self.colors[name])
                if dtype == "float":
                    val = val.astype(float)/255
                rgbtriplets.append(val)
                
        elif isinstance(colors[0], int):
            for i in colors:
                val = np.array(self.palette[i])
                if dtype == "float":
                    val = val.astype(float)/255
                rgbtriplets.append(val)
            
        if not islist:
            rgbtriplets = rgbtriplets[0]
            
        return rgbtriplets