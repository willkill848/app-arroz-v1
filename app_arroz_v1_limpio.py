
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌾 Aplicación de Arroz - V1")

# Subir archivo Excel
archivo = st.file_uploader("📂 Subí tu archivo de datos de parcelas", type=["xlsx"])

if archivo is not None:
    df = pd.read_excel(archivo)

    # Mostrar los datos cargados
    st.subheader("📋 Datos cargados:")
    st.write(df)

    # Mostrar estadísticas
    st.subheader("📊 Estadísticas:")
    st.write("Cantidad de parcelas:", df['PARCELAS'].nunique())
    st.write("Superficie total (ha):", df['HECTAREAS'].sum())
    st.write("Variedades:", df['VARIEDAD'].unique())

    # Mostrar gráfico de ciclos
    st.subheader("📈 Gráfico de Ciclo de Siembra - Cosecha")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Fecha Siembra'], df['Fecha Cosecha'], c='green')
    ax.set_xlabel("Fecha de Siembra")
    ax.set_ylabel("Fecha de Cosecha")
    ax.grid(True)
    st.pyplot(fig)

    # Descargar el archivo procesado
    st.subheader("📥 Descargar los datos")
    @st.cache_data
    def convertir_excel(df):
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        return output.getvalue()

    datos_excel = convertir_excel(df)
    st.download_button(
        label="Descargar Excel",
        data=datos_excel,
        file_name="resultado_arroz.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info("Por favor subí un archivo Excel con los datos para iniciar el análisis.")
