import pandas as pd

cpi = pd.read_csv("data/raw/cpi.csv", comment="#",
                  parse_dates=["observation_date"])
cpi = cpi.sort_values("observation_date")

# year-over-year inflation
p = cpi["CPIAUCSL"]
cpi["yoy"] = 100 * (p / p.shift(11) - 1)

cpi[["observation_date", "yoy"]].to_csv(
    "data/processed/inflation.csv", index=False)
