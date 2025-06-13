# 🔄 PyQGIS + PostGIS Automation

This project demonstrates how to automate spatial data ingestion from local vector files into a PostGIS database using PyQGIS and Python. It simulates a typical enterprise GIS data pipeline, highlighting skills in spatial database integration, batch uploads, and project reproducibility.

---

## 🧰 Tools & Technologies

- QGIS 3.x (with Python console)
- PostgreSQL + PostGIS (extension)
- PyQGIS API
- psycopg2 (for Python-PostGIS connection)
- Shapefile, GeoJSON (input data)

---

## 📁 Folder Structure

| Folder | Purpose |
|--------|---------|
| scripts/ | Automation scripts |
| db/ | PostGIS schema setup + connection notes |
| data/ | Sample shapefiles or geojson |
| outputs/ | Logs and QGIS output |

```
01_PyQGIS_PostGIS_Automation/
├── README.md
├── scripts/
│   ├── pyqgis_layer_loader.py
│   ├── postgis_uploader.py
│   └── config.py
├── db/
│   ├── postgis_schema.sql
│   └── connection_setup.md
├── data/
│   ├── landuse.geojson
│   └── roads.shp
└── outputs/
    ├── uploaded_log.txt
    └── qgis_project.qgz
```
---

## 🚀 Workflow Steps

1. Load vector layers into QGIS using PyQGIS
2. Transform CRS if needed (EPSG:4326)
3. Upload vector layers to PostGIS using psycopg2
4. Log results and errors
5. Save QGIS project to outputs

---

## 📸 Outputs

Uploaded tables:
- `public.landuse`
- `public.roads`

QGIS Project:
- `outputs/qgis_project.qgz` with live DB layers

> Add screenshots of:
- QGIS project with PostGIS layers
- Script outputs and logs

---

## 🔗 Resources

- [PyQGIS Developer Cookbook](https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/)
- [PostGIS SQL Reference](https://postgis.net/docs/)
