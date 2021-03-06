# -*- coding:utf-8 -*-# -*- coding:utf-8 -*-
#
# This file is part of OpenFisca.
# OpenFisca is a socio-fiscal microsimulation software
# Copyright © 2011 Clément Schaff, Mahdi Ben Jelloul
# Licensed under the terms of the GVPLv3 or later license
# (see openfisca/__init__.py for details)


# Exemple of a simple simulation


from datetime import datetime

from openfisca_core.simulations import ScenarioSimulation
from openfisca_core.simulations import SurveySimulation
from openfisca_qt.plugins.survey.aggregates import Aggregates

# destination_dir = "c:/users/utilisateur/documents/"
# fname_all = "aggregates_inflated_loyers.xlsx"
# fname_all = os.path.join(destination_dir, fname_all)


def test_case(year):
    simulation = ScenarioSimulation()
    simulation.set_config(year = year, reforme = False,
                    nmen = 3, maxrev = 100000, x_axis = 'sali')
    # Adding a husband/wife on the same tax sheet (foyer)
    simulation.scenario.addIndiv(1, datetime(1975, 1, 1).date(), 'conj', 'part')
    simulation.set_param()

    # A the aefa prestation can be disabled by uncommenting the following line
    # simulation.disable_prestations( ['aefa'])
    df = simulation.get_results_dataframe()
    print df.to_string()

    # Save example to excel
    # destination_dir = "c:/users/utilisateur/documents/"
    # fname = "Example_%s.%s" %(str(yr), "xls")
    # df.to_excel(destination_dir = "c:/users/utilisateur/documents/" + fname)

def survey_case(year):
#        fname = "Agg_%s.%s" %(str(yr), "xls")
    simulation = SurveySimulation()
    simulation.set_config(year = year)
    simulation.set_param()

#    Ignore this
#    inflator = get_loyer_inflator(year)
#    simulation.inflate_survey({'loyer' : inflator})

    simulation.compute()


# Compute aggregates
    agg = Aggregates()
    agg.set_simulation(simulation)
    agg.compute()

    df1 = agg.aggr_frame
    print df1.to_string()

#    Saving aggregates
#    if writer is None:
#        writer = ExcelWriter(str(fname)
#    agg.aggr_frame.to_excel(writer, yr, index= False, header= True)


# Displaying a pivot table
    from openfisca_qt.plugins.survey.distribution import OpenfiscaPivotTable
    pivot_table = OpenfiscaPivotTable()
    pivot_table.set_simulation(simulation)
    df2 = pivot_table.get_table(by = 'so', vars = ['nivvie'])
    print df2.to_string()


if __name__ == '__main__':
    test_case(2006)
#    survey_case(2006)
