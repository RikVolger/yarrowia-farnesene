# The main file orchestrating the execution of the various parts of the model
# importing used packages
from pprint import pprint

from cobra.flux_analysis import add_loopless
from cobra.io import read_sbml_model, validate_sbml_model


def validate_model_with_output(filename):
    report = validate_sbml_model(filename)
    pprint(report)


def yarrowia_farnesene(filename):
    # load metabolic model from disk
    base_model = read_sbml_model(filename)
    validate_model_with_output(filename)
    print("Exchanges: ", base_model.exchanges)
    print("Demands: ", base_model.demands)
    print("Sinks: ", base_model.sinks)
    # optimize for growth
    add_loopless(base_model)
    solution = base_model.optimize()
    pprint(solution)
    # do some fancy output

    # introduce pathway for farnesene production

    # optimize for growth

    # do some fancy output

    # perhaps some deletions

    # optimize for growth

    # do some fancy output

    # with optimized strain, do reactor simulations


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yarrowia_farnesene('./gsmm/kavscek_2015/MODEL1510060001_SBML3.xml')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
