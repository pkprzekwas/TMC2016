def run():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    filename = askopenfilename()

    if isinstance(filename, str):
        import numpy as np
        import plotly
        import plotly.graph_objs as go
        from plotly.offline import iplot

        plotly.offline.init_notebook_mode()

        data = np.genfromtxt(filename, delimiter=',')

        z = np.flipud(data)
        y = np.arange(-90, 90.5, 0.5)
        x = np.arange(0,360,0.5)

        trace = go.Heatmap(z=z,y=y,x=x)
        out = [trace]
        iplot(out)

if __name__ == '__main__':
    run()

