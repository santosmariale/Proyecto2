import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Definir el contenido de la aplicación web
st.header('Car Listings Dashboard')

# Checkbox para incluir fabricantes con menos de 1000 anuncios
include_manufacturers = st.checkbox('Include manufacturers with less than 1000 Ads')

# Filtrar los datos si se selecciona la opción de incluir fabricantes con menos de 1000 anuncios
if include_manufacturers:
    car_data_filtered = car_data  # Filtro necesario para incluir solo fabricantes con menos de 1000 anuncios
else:
    car_data_filtered = car_data

# Mostrar el dataframe con los datos filtrados
st.write('Data viewer')
st.dataframe(car_data_filtered[['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel']])

# Checkbox para seleccionar las condiciones a incluir en el histograma
st.write('Select conditions to include in the histogram:')
condition_options = ['good', 'like new', 'fair', 'excellent', 'salvage', 'new']
selected_conditions = st.multiselect('Condiciones', condition_options, default=['good', 'like new', 'fair', 'excellent', 'salvage', 'new'])

# Filtrar los datos según las condiciones seleccionadas
car_data_filtered = car_data_filtered[car_data_filtered['condition'].isin(selected_conditions)]

# Botones de verificación para visualizar cada gráfico individualmente
show_hist_condition = st.checkbox('Show Histogram of Condition vs Model Year')
show_scatter = st.checkbox('Show Scatter Plot of Price vs Odometer')
show_condition_bar = st.checkbox('Show Distribution of Vehicle Condition')
show_fuel_bar = st.checkbox('Show Distribution of Fuel Type')
show_paint_color_bar = st.checkbox('Show Distribution of Paint Color')

# Mostrar gráficos según los botones de verificación
if show_hist_condition:
    st.header('Histogram of Condition vs Model Year')
    fig_hist_condition = px.histogram(car_data_filtered, x='model_year', color='condition')
    st.plotly_chart(fig_hist_condition, use_container_width=True)
    
    st.write("This histogram shows the distribution of car conditions across different model years. It helps us visualize how the condition of cars varies over time. From the graph, we can see that...")
    
if show_scatter:
    st.header('Scatter Plot of Price vs Odometer')
    fig_scatter = px.scatter(car_data_filtered, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.write("This scatter plot illustrates the relationship between the price of cars and their odometer readings. It allows us to observe if there's any discernible pattern between the two variables. From the graph, we can infer that...")
    
if show_condition_bar:
    st.header('Bar Chart for Distribution of Vehicle Condition')
    condition_counts = car_data_filtered['condition'].value_counts()
    fig_condition_bar = px.bar(x=condition_counts.index, y=condition_counts.values)
    fig_condition_bar.update_xaxes(title=None)
    fig_condition_bar.update_yaxes(title=None)
    st.plotly_chart(fig_condition_bar, use_container_width=True)
    
    st.write("This bar chart displays the distribution of vehicle conditions. It provides insights into the frequency of each condition category within the dataset. From the graph, we can observe that...")
    
if show_fuel_bar:
    st.header('Bar Chart for Distribution of Fuel Type')
    fuel_counts = car_data_filtered['fuel'].value_counts()
    fig_fuel_bar = px.bar(x=fuel_counts.index, y=fuel_counts.values)
    fig_fuel_bar.update_xaxes(title=None)
    fig_fuel_bar.update_yaxes(title=None)
    st.plotly_chart(fig_fuel_bar, use_container_width=True)
    
    st.write("This bar chart represents the distribution of fuel types among the listed vehicles. It helps us understand the prevalence of different fuel options. From the graph, we can deduce that...")
    
if show_paint_color_bar:
    st.header('Bar Chart for Distribution of Paint Color')
    paint_color_counts = car_data_filtered['paint_color'].value_counts()
    fig_paint_color_bar = px.bar(x=paint_color_counts.index, y=paint_color_counts.values)
    fig_paint_color_bar.update_xaxes(title=None)
    fig_paint_color_bar.update_yaxes(title=None)
    st.plotly_chart(fig_paint_color_bar, use_container_width=True)
    
    st.write("This bar chart shows the distribution of paint colors among the listed vehicles. It gives us insights into the popularity of different paint options. From the graph, we can see that...")
