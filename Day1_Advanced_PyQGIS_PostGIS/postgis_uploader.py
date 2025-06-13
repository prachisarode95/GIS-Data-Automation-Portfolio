import psycopg2
from config import DB_CONFIG
import geopandas as gpd

def upload_to_postgis(file_path, table_name):
    gdf = gpd.read_file(file_path)
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Create table (simplified)
    cursor.execute(f"""
    DROP TABLE IF EXISTS public.{table_name};
    CREATE TABLE public.{table_name} (
        id SERIAL PRIMARY KEY,
        name TEXT,
        geom GEOMETRY
    );
    """)
    conn.commit()

    # Upload rows
    for _, row in gdf.iterrows():
        cursor.execute(f"""
        INSERT INTO public.{table_name} (name, geom)
        VALUES (%s, ST_GeomFromText(%s, 4326));
        """, (row['name'], row['geometry'].wkt))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Uploaded {len(gdf)} features to {table_name}.")

# Example use:
upload_to_postgis("../data/landuse.geojson", "landuse")
