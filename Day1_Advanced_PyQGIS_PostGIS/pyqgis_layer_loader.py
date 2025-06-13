from qgis.core import (
    QgsVectorLayer,
    QgsProject
)

# Load shapefile into QGIS project
layer_path = "../data/roads.shp"
layer = QgsVectorLayer(layer_path, "Road Network", "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print("Layer loaded successfully.")
else:
    print("Failed to load layer.")
