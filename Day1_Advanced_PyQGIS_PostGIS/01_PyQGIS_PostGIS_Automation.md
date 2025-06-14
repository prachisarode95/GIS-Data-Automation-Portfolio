# 🛰️ Enterprise-Ready Spatial Data Pipeline using PyQGIS + PostGIS

This project simulates an enterprise-level spatial data ingestion pipeline using **PyQGIS** and **PostGIS**. It automates the validation, transformation, database upload, and visualization of multi-source GIS data.

---

## 🎯 Objective

- Validate incoming vector layers (schema + geometry)
- Upload features to a structured PostGIS schema
- Apply standard styling in QGIS
- Save the styled `.qgz` project and map snapshots
- Log processing steps and errors
---

## 📊 Technologies Used

| Component | Tool |
|----------|------|
| GIS Framework | QGIS + PyQGIS |
| Database | PostgreSQL + PostGIS |
| Scripting | Python (PyQGIS + psycopg2) |
| Logging | CSV reports |

---

## 🔄 Workflow Steps

1. Validate schema: fields, CRS (EPSG:4326), geometry
2. Clean and simplify geometry (optional)
3. Insert into structured PostGIS schema
4. Apply SLD/QLR style using PyQGIS
5. Save `.qgz` project + map snapshot
6. Log stats to CSV
---

## 📂 Folder Structure

```
02_PyQGIS_PostGIS_Automation_Advanced/
├── README.md
├── scripts/
│   ├── validate_and_load.py
│   ├── style_applier.py
│   ├── postgis_schema.sql
│   └── config.py
├── db/
│   ├── pg_connection_setup.md
│   └── sample_log.csv
├── qgis_project/
│   └── planning_data.qgz
├── data/
│   ├── landuse.geojson
│   └── roads.shp
├── outputs/
│   ├── logs/
│   │   └── upload_report.csv
│   └── snapshots/
│       └── landuse_map.png
```
---

## 🗂 Output

- Tables(csv): `planning.landuse`, `planning.roads`
- Project: `planning_data.qgz` (with styled layers)
- Snapshot: `landuse_map.png`
---

## 🔗 Data Sources

- Open Data Toronto
- OSM GeoJSON exports
- Natural Earth shapefiles
---

## 💼 Real-World Value

Demonstrates your capability to:
- Build repeatable, scalable geospatial pipelines
- Automate integration between QGIS and PostGIS
- Align with enterprise-grade workflows
---

## 🔗 Resources

- [PyQGIS Developer Cookbook](https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/)
- [PostGIS SQL Reference](https://postgis.net/docs/)
