import pandas as pd
import streamlit as st
import plotly.express as px

# Configurações da pagina
st.set_page_config(layout="wide")
st.header('Vendas do Supermercado')

# Leitura dos dados
df = pd.read_csv('Supermarket Sales/supermarket_sales.csv', sep=';', decimal=',')
df['Date'] = pd.to_datetime(df['Date'])
df=df.sort_values(by='Date', ascending=True)

# Sidebar
df["Month"] = df["Date"].apply(lambda x: str(x.year)+ "-"+str(x.month))
month = st.sidebar.selectbox('Selecione o mês', df['Month'].unique())

df_filtered = df[df['Month'] == month]

# Layout
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
col6, col7 = st.columns(2)

# Gráficos

#Faturamento por Filiais
fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Total por Dia')
col1.plotly_chart(fig_date, use_container_width=True)

#tipos de produtos
fig_products = px.bar(df_filtered, x='Date', y='Product line', color='Product line', title='Total por Tipo de Produtos', orientation='h')
col2.plotly_chart(fig_products, use_container_width=True)

#contribuições por cada filial
city_total = df_filtered.groupby(['City'])['Total'].sum().reset_index()
fig_city = px.bar(df_filtered, x='City', y='Total', title='Faturamento por Filial')
col3.plotly_chart(fig_city, use_container_width=True)

#faturamento por metodo de pagamento
fig_payment = px.pie(df_filtered, values='Total', names='Payment', title='Faturamento por Método de Pagamento')
col4.plotly_chart(fig_payment, use_container_width=True)

#faturamento por genero
fig_gender = px.pie(df_filtered, values='Total', names='Gender', title='Faturamento por Gênero')
col5.plotly_chart(fig_gender, use_container_width=True)

#Avaliações
fig_rating = px.bar(df_filtered, x='City', y='Rating', color='City', title='Avaliações')
col6.plotly_chart(fig_rating, use_container_width=True)

#tipos de clientes
fig_customer = px.pie(df_filtered, values='Total', names='Customer type', title='Tipos de Clientes')
col7.plotly_chart(fig_customer, use_container_width=True)






