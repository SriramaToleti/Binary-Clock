import PySimpleGUI as sg
from datetime import datetime
from time import sleep
sg.theme('black')

class Gui:
    def __init__(self):
        self.layout=[[sg.Graph(canvas_size=(215,130), graph_bottom_left=(0,0), graph_top_right=(215,130), background_color='gray', key='graph')],
                     [ sg.Text('Bin Clock 1,2,4,8',size = (15,1)),sg.Text('',size = (7,1), key = 'output'),sg.Button('x',size=(1,1),key='_close_')]]
        self.window = sg.Window('BinaryClock', self.layout, grab_anywhere=True, finalize = True, no_titlebar=True)

        self.timenow = str(datetime.now().strftime("%H:%M:%S"))
        self.graph = self.window['graph']
        

    
    def draw_dots(self):

        self.timenow = str(datetime.now().strftime("%H:%M:%S"))
        self.h1 = f'{int(self.timenow[0]):04b}'
        self.h2 = f'{int(self.timenow[1]):04b}'
        self.m1 = f'{int(self.timenow[3]):04b}'
        self.m2 = f'{int(self.timenow[4]):04b}'
        self.s1 = f'{int(self.timenow[6]):04b}'
        self.s2 = f'{int(self.timenow[7]):04b}'


        self.graph.DrawCircle((20,20), 10, fill_color='pink' if self.h1[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((20,50), 10, fill_color='pink' if self.h1[-2] == '1' else 'black' ,line_color='red')

        self.graph.DrawCircle((50,20), 10, fill_color='pink' if self.h2[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((50,50), 10, fill_color='pink' if self.h2[-2] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((50,80), 10, fill_color='pink' if self.h2[-3] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((50,110), 10, fill_color='pink' if self.h2[-4] == '1' else 'black' ,line_color='red')

        self.graph.DrawCircle((90,20), 10, fill_color='pink' if self.m1[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((90,50), 10, fill_color='pink' if self.m1[-2] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((90,80), 10, fill_color='pink' if self.m1[-3] == '1' else 'black' ,line_color='red')
        
        self.graph.DrawCircle((120,20), 10, fill_color='pink' if self.m2[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((120,50), 10, fill_color='pink' if self.m2[-2] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((120,80), 10, fill_color='pink' if self.m2[-3] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((120,110), 10, fill_color='pink' if self.m2[-4] == '1' else 'black' ,line_color='red')

        self.graph.DrawCircle((160,20), 10, fill_color='pink' if self.s1[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((160,50), 10, fill_color='pink' if self.s1[-2] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((160,80), 10, fill_color='pink' if self.s1[-3] == '1' else 'black' ,line_color='red')
        
        self.graph.DrawCircle((190,20), 10, fill_color='pink' if self.s2[-1] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((190,50), 10, fill_color='pink' if self.s2[-2] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((190,80), 10, fill_color='pink' if self.s2[-3] == '1' else 'black' ,line_color='red')
        self.graph.DrawCircle((190,110), 10, fill_color='pink' if self.s2[-4] == '1' else 'black' ,line_color='red')



def main():
    g = Gui()
    
    while True:
        g.draw_dots()
        
        event, values = g.window.Read(timeout=100)
        
        if event is None:      
            break
        if event == '_close_':
            break

        g.window['output'].update(str(datetime.now().strftime("%H:%M:%S")))
        sleep(0.3)
    g.window.close()
            
if __name__ == '__main__':
    main()