from cobra.io import read_sbml_model, write_sbml_model


def upgrade_model(path):
    path_sbml_original = path
    path_sbml_3fbc = path.replace(".xml", "_SBML3.xml")

    # read original model
    model = read_sbml_model(path_sbml_original)
    # write as SBML3 model
    write_sbml_model(model, path_sbml_3fbc)
    print("\n\nNew read\n\n")
    # re-load model with only relevant warnings left
    read_sbml_model(path_sbml_3fbc)


if __name__ == "__main__":
    upgrade_model("./gsmm/kavscek_2015/MODEL1510060001.xml")
