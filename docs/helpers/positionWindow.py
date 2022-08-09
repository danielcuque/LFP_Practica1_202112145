import tkinter as tk

# Function for position


class PositionWindow:
    
    @staticmethod
    def positionWindow(screenWidth, screenHeight, appWidth, appHeight, **args):
        x = (screenWidth - appWidth) / 2
        y = (screenHeight - appHeight) / 2
        return f'{appWidth}x{appHeight}+{int(x)}+{int(y)}'
