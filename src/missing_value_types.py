#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    states = ["United Kingdom","Finland", "USA", "Sweden", "Germany", "Russia"]
    indYear = [np.nan, 1917, 1776, 1523, np.nan, 1992 ]
    president = [None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]

    df = pd.DataFrame({"Year of independence": indYear, "President": president}, index=states)

    return df

def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
