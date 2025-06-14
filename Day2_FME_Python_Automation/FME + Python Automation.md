# 🔄 FME-Based Spatial Data Automation (In Progress)

This project showcases automation of multi-format spatial data transformation using **FME Workbench**, enhanced with embedded **Python scripts via the PythonCaller transformer**. It simulates a robust ETL pipeline built for urban planning datasets, supporting data validation, classification, and logging.

---

## 🎯 Objective

- Read and transform spatial datasets (SHP, GeoJSON, GDB)
- Perform attribute-based filtering and schema standardization
- Classify parcel features based on area
- Integrate embedded Python to create custom reports and tagging
- Export final output for QA and visualization

---

## 🧰 Tools Used

| Tool         | Purpose |
|--------------|---------|
| FME Form     | Visual ETL pipeline design |
| PythonCaller | Custom logic inside FME |
| SHP, GeoJSON, GDB | Multi-format inputs |
| AttributeManager, AreaCalculator, Tester | Core transformers |
| Logger       | QA output & reporting |

---

## 🔁 Workflow

1. **Read Input Data**
   - Accepts SHP, GDB, or GeoJSON files
2. **Transform & Validate**
   - Calculate area
   - Classify parcels: `Small`, `Medium`, `Large`
   - Clean attributes with `AttributeManager`
3. **Apply Python Logic**
   - Use `PythonCaller` to assign tags and write reports
   - Example: `"processed_by" = "FME+Python"`
4. **Export Final Outputs**
   - Clean shapefile output
   - Summary log using Logger or CSV writer

---

## 📁 Project Files

```
03_FME_Python_Automation/
├── fme_workspace.fmwt
├── sample_data/
│ ├── parcels.shp
│ └── zoning_areas.shp
├── python_scripts/
│ └── attribute_classifier.py
├── outputs/
│ └── classified_parcels.shp
├── screenshots/
│ ├── workspace_layout.png
│ └── pythoncaller_config.png
```
---

## 🐍 PythonCaller Example

```python
def fme_feature(feature):
    area = float(feature.getAttribute('area'))
    if area > 2000:
        feature.setAttribute('category', 'Large')
    elif area > 1000:
        feature.setAttribute('category', 'Medium')
    else:
        feature.setAttribute('category', 'Small')
    feature.setAttribute('processed_by', 'FME+Python')
```
---

## ✅ Output Highlights

- classified_parcels.shp with area-based categories
- Summary logs generated via PythonCaller or Logger
- Modular workspace for reuse in multiple projects
---

## 💼 What It Demonstrates

- GUI + code hybrid ETL design
- Real-world classification + attribute handling
- Working knowledge of embedded Python inside FME
- QA-focused automation for spatial data prep
---

## 🚧 Status
In Progress – Will expand to multi-layer validation + reporting in CSV/PDF via Python.

---

## 📷 Screenshot Previews (To Add)

- Workspace layout with transformers
- PythonCaller with script
- Output visual in QGIS
