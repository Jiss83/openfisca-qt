# -*- coding:utf-8 -*-
"""
Created on Oct 22, 2013
@author: Mahd Ben Jelloul
"""


from datetime import datetime
import os
import sys

from openfisca_core.simulations import ScenarioSimulation
from openfisca_qt.gui.qt.QtGui import QMainWindow, QApplication
from openfisca_qt.plugins.scenario.graph import draw_simulation_bareme, draw_simulation_taux
from openfisca_qt.widgets.matplotlibwidget import MatplotlibWidget


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mplwidget = MatplotlibWidget(self)
        self.mplwidget.setFocus()
        self.setCentralWidget(self.mplwidget)


if __name__ == '__main__':

    SAVE = False
    SHOW = True
    destination_dir = u"c:/users/utilisateur/Desktop/Simula"
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win = ApplicationWindow()

    ax = win.mplwidget.axes

    year = 2011

    simulation = ScenarioSimulation()
    simulation.set_config(year = year, nmen = 101,
                    x_axis = 'sali', maxrev = 50000,
                    mode ='bareme', same_rev_couple = False)
    simulation.set_param()

#    draw_simulation_bareme(simulation, ax, legend = True, position = 4)
    draw_simulation_taux(simulation, ax, legend=True)

    win.resize(1400,700)
    if SHOW:
        win.mplwidget.draw()
        win.show()

    df = simulation.get_results_dataframe()
    print df.to_string()

    title = "test"
    if SAVE:
        win.mplwidget.print_figure(os.path.join(destination_dir, title + '.png'))

    del ax, simulation
    sys.exit(app.exec_())

