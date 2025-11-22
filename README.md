# Echo: A Multimodal Spatio-Temporal Framework for Forecasting Dyadic Conflict and Cooperation
## Sharaf E. Boukhezer FYP

Echo is a multimodal forecasting system that predicts the future state of international relations between country pairs (dyads) using time-series history, text-derived signals, graph-structured geopolitical context, and static features to generate forward-looking estimates of:

- Goldstein polarity score  
- QuadClass event distribution (Verbal Cooperation, Material Cooperation, Verbal Conflict, Material Conflict)

All components are designed to be fully reproducible, allowing modular experimentation and consistent evaluation across different forecast horizons and dyad categories.

## Table of Contents

1. [Overview](#overview)  
2. [Requirements](#requirements)  
3. [Getting Started](#getting-started)  
4. [Repository Structure](#repository-structure) 


## Overview

Forecasting geopolitical dynamics is challenging because relationships between states are influenced by structural dependencies, past interactions, and sudden shocks. Existing approaches often rely on a single modality such as time-series data, static features, or text sentiment.

Echo addresses this limitation by combining four complementary information sources:

1. **Historical event patterns** 
2. **News-derived signals**
3. **Geopolitical graph context**
4. **Static dyad attributes**

The system generates unified predictions for both continuous polarity and discrete event counts at a specefic forecasting horizon.


## Requirements


## Getting Started
### 1. Clone the repository and navigate into the project directory
```bash
git clone https://github.com/sharafedd/seb206.git
cd seb206
```

## Repository Structure

```plaintext
seb206/
├── src/
│   ├── etl/                      # Data extraction, cleaning, graph building
│   ├── baselines/                # All baseline models
│   ├── models/                   # Echo components and architecture
│   ├── training/                 # Training loops and ablation scripts
│   ├── evaluation/               # Metrics, analysis, and plots
│   └── utils/                    # Helpers and configs
├── data/                         # Raw, interim, processed datasets
├── experiments/                  # Results from all runs
├── notebooks/                    # Exploration and visualisation
├── reports/                      # Proposal and final report
├── docs/                         # Documentation and diagrams
├── requirements.txt              # Dependencies
└── README.md
