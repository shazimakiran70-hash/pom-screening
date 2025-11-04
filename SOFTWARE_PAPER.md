# Hybrid Catalyst Predictor: A Data-Driven Tool for Designing POM-Based Photocatalysts

### **Abstract**
This repository presents a lightweight, data-driven framework for screening and predicting the performance of Polyoxometalate (POM)-based hybrid photocatalysts for CO₂ conversion under visible light. The tool integrates DFT-derived and experimental datasets to train machine learning models that estimate bandgap tuning, charge transfer efficiency, and visible-light absorption.

### **Motivation**
Despite their exceptional redox flexibility, many POMs are limited by large bandgaps. This framework aims to accelerate the discovery of hybrid POM/semiconductor or POM/MOF catalysts through computational screening and predictive modeling.

### **Core Features**
- Dataset generation using POM structural and electronic descriptors  
- Hybrid_cat_predictor.py for training ML models  
- Result visualization (bandgap trends, predicted activity)  
- Easy GitHub workflow for CI testing  

### **Preliminary Results**
The current implementation demonstrates proof-of-concept prediction accuracy for hybrid catalyst properties using publicly available data.

### **Future Work**
- Integration with Materials Project API for automated data enrichment  
- Coupling DFT-calculated descriptors with ML optimization  
- Deployment of a web-based dashboard for real-time predictions  

---

### **Citation**
If you use this work, please cite:
> Shazima Kiran, *Hybrid Catalyst Predictor: A Data-Driven Framework for POM-Based Photocatalysts*, GitHub (2025).  
> [https://github.com/shazimakiran70-hash/pom-screening](https://github.com/shazimakiran70-hash/pom-screening)
