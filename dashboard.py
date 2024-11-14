# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Crea el cliente de BigQuery usando las credenciales del archivo de secretos.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Función para ejecutar la consulta con almacenamiento en caché.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convertir a una lista de diccionarios para que `st.cache_data` pueda almacenar el resultado.
    rows = [dict(row) for row in rows_raw]
    return rows

# Modifica la consulta para seleccionar de la tabla `industry` en tu proyecto y dataset específicos.
rows = run_query("SELECT * FROM `proyecto-final-sh-441422.dataset_name.industry` LIMIT 10")

# Mostrar resultados.
st.write("Datos de la tabla 'industry':")
for row in rows:
    st.write(row)