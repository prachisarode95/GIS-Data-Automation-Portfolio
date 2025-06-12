# Day 1: Advanced Spatial SQL – PostGIS

## 📌 Objective
Build and test advanced spatial queries using PostGIS functions on real-world shapefiles.

## 🛠 Prerequisites
- PostgreSQL with PostGIS installed
- Sample datasets loaded into spatial tables (`villages`, `roads`)

## 📂 Dataset
- `sample_villages.shp`
- `roads.geojson`

## 🧪 Tasks & Queries

-- 1. Basic Spatial Join: Find roads intersecting villages
SELECT a.road_id, b.village_name
FROM roads a
JOIN villages b
  ON ST_Intersects(a.geom, b.geom);

-- 2. Calculate area for each village in sq km
SELECT village_name,
       ST_Area(geom) / 1000000 AS area_sqkm
FROM villages;

-- 3. Buffer roads by 500m
SELECT road_id,
       ST_Buffer(geom::geography, 500)::geometry AS buffer_geom
FROM roads;

-- 4. Trigger: Auto-update modified date on update
CREATE OR REPLACE FUNCTION update_modified_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.modified_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_modified
BEFORE UPDATE ON villages
FOR EACH ROW
EXECUTE FUNCTION update_modified_at();

## 📸 Deliverables
- Screenshots of SQL results in pgAdmin or DBeaver
- Diagram of spatial joins and buffers

## ✅ Outcome
- Learn ST_ functions: ST_Intersects, ST_Buffer, ST_Area
- Create triggers to automate field updates
- Practice real-world spatial joins and transformations
