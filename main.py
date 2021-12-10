# The main file orchestrating the execution of the various parts of the model
# importing used packages
from pprint import pprint

from cobra.flux_analysis import add_loopless
from cobra.io import read_sbml_model, validate_sbml_model


def validate_model_with_output(filename):
    """Use cobra tools to validate the model, print the results."""
    report = validate_sbml_model(filename)
    pprint(report)


def inspect_model(model, filename):
    """Inspect the provided SBML model behind filename, and provide basic info about the loaded model."""
    validate_model_with_output(filename)

    print("\nExchanges: ")
    pprint([reaction.name for reaction in model.exchanges])
    print("\nDemands: ")
    pprint([reaction.name for reaction in model.demands])
    print("\nSinks: ")
    pprint([reaction.name for reaction in model.sinks])


def yarrowia_farnesene(filename):
    """Core function of the project. Orchestrates the calling of other functions and passes data between them."""
    # load metabolic model from disk
    base_model = read_sbml_model(filename)

    inspect_model(base_model, filename)

    # Optimize for growth
    # print("\nEliminating loops")
    # add_loopless(base_model)
    print("\n\nOptimizing...\n")
    base_model.optimize()
    print(base_model.summary())
    # do some fancy output

    # introduce pathway for farnesene production

    # optimize for growth

    # do some fancy output

    # perhaps some deletions

    # optimize for growth

    # do some fancy output

    # with optimized strain, do reactor simulations


if __name__ == '__main__':
    yarrowia_farnesene('./gsmm/kavscek_2015/MODEL1510060001_SBML3.xml')
