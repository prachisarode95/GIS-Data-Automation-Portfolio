# 🛠 Module 2: FME + Python Automation

This project showcases how to integrate Python scripts within FME workflows to perform automated classification and attribute editing. It simulates a typical parcel classification task in a land management system.

---

## 🎯 Objective

Use the `PythonCaller` transformer in FME Form to:
- Classify parcels based on area
- Add custom attributes
- Export the results to a new Shapefile

---

## 🧰 Tools & Technologies

| Tool       | Purpose                               |
|------------|---------------------------------------|
| FME Form   | Spatial ETL & visual automation       |
| Python 3.x | Embedded logic via PythonCaller       |
| Shapefile  | Input/output format                   |

---

## 📁 Folder Structure

| Folder | Description |
|--------|-------------|
| sample_data/ | Input shapefiles |
| python_scripts/ | Custom Python logic for automation |
| outputs/ | Classified output shapefile |
| screenshots/ | Workspace visuals for README |

```
03_FME_Python_Automation/
├── README.md
├── fme_workspace.fmwt
├── sample_data/
│   ├── parcels.shp
│   └── zoning_areas.shp
├── python_scripts/
│   └── attribute_classifier.py
├── screenshots/
│   ├── workspace_layout.png
│   └── pythoncaller_config.png
└── outputs/
    └── classified_parcels.shp
```
---

## 🔁 Workflow Steps

1. Read `parcels.shp` as input
2. Use `AreaCalculator` to generate area attribute
3. Pass features to `PythonCaller`:
    - Classify parcels as Small, Medium, or Large
    - Add custom tags (e.g., `"processed_by": "FME+Python"`)
4. Clean attributes with `AttributeManager`
5. Export `classified_parcels.shp`

---

✅ Output
Final output: outputs/classified_parcels.shp

Fields: id, area, category, tag

Viewable in QGIS or any GIS viewer

📸 Screenshots
workspace_layout.png: Full transformer layout

pythoncaller_config.png: Embedded script in PythonCaller


💡 Project Extension
Zoning Compliance Check:

Add zoning_areas.shp as secondary input

Use SpatialFilter to tag parcels inside non-compliant zones

Add compliance = "Yes"/"No" using another PythonCaller

This turns your pipeline into a compliance checker

