"""
Information about Simulations
=================================

This module contains functions that provide overview information about a trajectory.
"""

def summary(*universe):
    data_column_keys = [
        "n_atoms",
        "Lx",
        "Ly",
        "Lz",
        "alpha",
        "beta",
        "gamma",
        "n_frames",
        "totaltime",
        "dt",
    ]
    data_column_names = [
        "n_atoms",
        "Lx/Å",
        "Ly/Å",
        "Lz/Å",
        "alpha",
        "beta",
        "gamma",
        "n_frames",
        "totaltime/ns",
        "dt/ps",
    ]

    if labels is None:
        labels = len(universes) * [None]
        column_names = data_column_names
    else:
        column_names = ["simulation"] + data_column_names

    if len(labels) != len(universes):
        raise ValueError(
            f"labels {labels} must contain one "
            f"label per universe {universes}"
        )


    table = prettytable.PrettyTable()
    table.field_names = column_names

    for u, label in zip(universes, labels):
        data = extract(u)
        data["totaltime"] /= 1000  # convert ps to ns
        row = [data[key] for key in data_column_keys]
        if label is not None:
            row = [label] + row
        table.add_row(row)

    print(table)
    
def extract(universe):
    pass