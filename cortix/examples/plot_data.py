from cortix.src.module import Module
from cortix.src.port import Port
from cortix.util.dataplot import DataPlot

class PlotData(Module):
    def __init__():
        super().__init__()

    def run():
        i = 0
        while i < 10:
            data = (i, i**2)
            self.send("plot-out", data)
            print("Sent {}!".format(data))
            i += 1
        print("Finished sending!")

if __name__ == "__main__":

    # Cortix built-in DataPlot module
    d = DataPlot()

    # Custom class to send dummy data
    p = PlotData()

    p1 = Port("plot-in")
    p2 = Port("plot-out")
    p1.connect(p2)

    d.add_port(p1)
    p.add_port(p2)

    c = Cortix()
    c.add_module(d)
    c.add_module(p)
    c.run()
