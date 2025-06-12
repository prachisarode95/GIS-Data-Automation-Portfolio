# Day 4: Cloud GIS Deployment – Streamlit Cloud (Beginner-Friendly)

## ☁️ Objective
Deploy a fully working geospatial dashboard to Streamlit Cloud using static spatial data.

---

## 📁 Folder Structure
```
Day4_Cloud_GIS_Streamlit_Deployment/
├── README.md
├── streamlit_app.py
├── requirements.txt
└── data/
    └── sample_villages.geojson
```

---

## 🧪 Tasks
### ✅ 1. Build the Streamlit app
- Create `streamlit_app.py` using Leafmap or Folium
- Read local GeoJSON or raster data

### ✅ 2. Prepare `requirements.txt`
```
streamlit
leafmap
geopandas
pandas
```

### ✅ 3. Push to GitHub (Public Repo)
- Create a new GitHub repo named: `streamlit-gis-dashboard`
- Add your files and commit:
```bash
git init
git remote add origin https://github.com/yourusername/streamlit-gis-dashboard.git
git add .
git commit -m "Day 4 - Initial Streamlit App"
git push -u origin main
```

### ✅ 4. Deploy to Streamlit Cloud
- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Sign in with GitHub
- Click **New App** → Select your repo → Choose `streamlit_app.py`
- Click **Deploy**

---

## 🌐 Demo Output
- Include map widget with a sidebar toggle
- Load local `.geojson` and style it

```python
import streamlit as st
import leafmap.foliumap as leafmap

st.title("📍 Geospatial Dashboard - Villages")

m = leafmap.Map(center=[19.76, 75.34], zoom=6)
m.add_geojson("data/sample_villages.geojson", layer_name="Villages")
m.to_streamlit(height=600)
```

---

## ✅ Outcome
- Live hosted GIS dashboard using Streamlit Cloud
- No need for PostGIS or AWS/Azure
- Ready to add Docker + CI in Day 5

---

## 📸 Tips
- Include screenshots of your deployed dashboard
- Add Hugging Face deployment in parallel for variety

---

## 🔗 Resources
- [Streamlit Cloud Guide](https://docs.streamlit.io/streamlit-cloud)
- [Leafmap Docs](https://leafmap.org/)
- [Sample GeoJSON Dataset](https://datahub.io/core/geo-countries)

**Next** → Proceed to Day 5: Docker + GitHub Actions CI/CD 🚀
