# pom-screening
Data-driven prediction of visible-light POM hybrid photocatalysts for CO₂ reduction
# HybridCatPredictor

**Data-driven discovery of visible-light-active POM-based hybrid photocatalysts for CO₂ reduction**

![CI](https://github.com/YOUR_USERNAME/pom-screening/actions/workflows/ci.yml/badge.svg)

---

## 🔹 Project Description

HybridCatPredictor is an open-source Python package designed to accelerate the discovery of **polyoxometalate (POM)-based hybrid photocatalysts**. It integrates:

- **Descriptor handling**: bandgap, CBM/VBM, POM LUMO, CO₂ adsorption energy, stability index.
- **Machine Learning models**: baseline Random Forest to predict photocatalytic activity.
- **Candidate ranking**: prioritizes materials likely to have strong visible-light response and CO₂ reduction efficiency.
- **Interactive exploration**: planned Streamlit dashboard (modular scaffold included).

The software is intended for researchers in **inorganic/organic hybrid materials, photocatalysis, and energy materials**, providing a **reproducible workflow** for screening POM/MOF-based photocatalysts.

---

## 🔹 Features

- Quick baseline predictions with Random Forest
- Easy-to-modify Python scaffold for adding:
  - DFT/DFTB descriptors
  - GNN (CGCNN/ALIGNN) structural learning models
- Example dataset included for demonstration
- GitHub Actions CI ensures reproducibility and code integrity

---citation
Shazima Kiran. (2025). HybridCatPredictor: A Data-Driven Framework for POM-Based Hybrid Photocatalysts. GitHub Repository. https://github.com/YOUR_USERNAME/pom-screening


## 🔹 Installation

No installation needed — run directly in **Google Colab** or any Python environment with:

```bash
pip install pandas scikit-learn numpy
