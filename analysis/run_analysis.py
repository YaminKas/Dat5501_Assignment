#!/usr/bin/env python3
"""
run_analysis.py
This script runs the full analysis workflow: EDA, statistics, and visualisations.
"""

# Standard imports
import sys
from pathlib import Path

# Add analysis folder to path (in case we run from elsewhere)
sys.path.append(str(Path(__file__).resolve().parent))

# Import your modules
from data_analysis1 import main as eda_main
from stats import run_statistics
from visualisations import create_visualisations

def main():
    print("Starting full analysis workflow...\n")

    #Run exploratory data analysis
    print("Running EDA...")
    eda_main()
    print("EDA complete.\n")

    #Run statistics analysis
    print("Running statistics analysis...")
    run_statistics()
    print("Statistics analysis complete.\n")

    #Generate visualisations
    print("Generating visualisations...")
    create_visualisations()
    print("Visualisations complete.\n")

    print("All analysis tasks finished successfully!")

if __name__ == "__main__":
    main()