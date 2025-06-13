-- 📁 SQL_queries.sql – Day 1: Advanced Spatial SQL with PostGIS

-- 1. Basic Spatial Join: Find roads intersecting villages
SELECT a.road_id, b.village_name
FROM roads a
JOIN villages b
  ON ST_Intersects(a.geom, b.geom);

-- 2. Calculate area of villages in square kilometers
SELECT village_name,
       ST_Area(geom) / 1000000 AS area_sqkm
FROM villages;

-- 3. Create buffer of 500 meters around roads
SELECT road_id,
       ST_Buffer(geom::geography, 500)::geometry AS buffer_geom
FROM roads;

-- 4. Trigger Setup: Auto-update modified date on row update
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
