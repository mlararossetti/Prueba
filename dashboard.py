import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título del dashboard
st.title("Dashboard Básico de Streamlit")

# Crear datos de ejemplo
np.random.seed(42)
data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': np.random.randint(20, 100, size=4)
})

# Mostrar los datos en una tabla
st.subheader("Tabla de Datos")
st.write(data)

# Crear un gráfico de barras
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
ax.bar(data['Categoría'], data['Valores'], color='skyblue')
ax.set_xlabel("Categoría")
ax.set_ylabel("Valores")
ax.set_title("Gráfico de Barras por Categoría")
st.pyplot(fig)

# Generar algunos datos para un gráfico de líneas
st.subheader("Gráfico de Líneas")
line_data = pd.DataFrame({
    'Día': np.arange(1, 11),
    'Valores': np.random.randint(20, 100, size=10)
})
st.line_chart(line_data.set_index('Día'))

# Agregar una barra lateral para seleccionar filtros
st.sidebar.subheader("Filtros")
categoria_seleccionada = st.sidebar.selectbox("Selecciona una Categoría", data['Categoría'])

# Filtrar los datos en función de la selección
datos_filtrados = data[data['Categoría'] == categoria_seleccionada]
st.write(f"Datos filtrados por Categoría '{categoria_seleccionada}':")
st.write(datos_filtrados)
