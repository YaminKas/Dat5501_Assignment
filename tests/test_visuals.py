import os

BASE_DIR = "/Users/yaminkashim/DAT5501_lab/DAT5501_Assignment"
FIG_DIR = os.path.join(BASE_DIR, "analysis/figures")

def test_figures_exist():
    files = [
        "scatter_imd_vs_attainment_male.png",
        "scatter_imd_vs_attainment_female.png"
    ]
    for f in files:
        path = os.path.join(FIG_DIR, f)
        assert os.path.isfile(path), f"{f} is missing."