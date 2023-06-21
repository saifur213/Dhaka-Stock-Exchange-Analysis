import streamlit as st
import time
import numpy as np
import pandas as pd



import matplotlib.pyplot as plt
import squarify
import psycopg2

import os
import django
import sys

project_directory = "F:\Data Analyst\Django\DSE\DseAnalysis"
app_directory = "F:\Data Analyst\Django\DSE\DseAnalysis\webScraping"
sys.path.append(project_directory)
sys.path.append(app_directory)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DseAnalysis.settings")
django.setup()

from webScraping.models import company_details,company_other_info


#establishing the connection
conn = psycopg2.connect(
   database="dse_db", user='postgres', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

st.set_page_config(page_title="DSE DATA Analysis", page_icon="📈",layout="wide")

st.markdown("# Dhaka Stock Exchange Analysis Dashboard")
st.sidebar.header("Overview")

cd = company_details.objects.all().values()
coi = company_other_info.objects.all().values()
company_details_df = pd.DataFrame.from_records(cd)
company_other_info_df = pd.DataFrame.from_records(coi)

company_other_info_df['Modify Date'] = pd.to_datetime(company_other_info_df['Date'])
company_other_info_df['Year'] = company_other_info_df['Modify Date'].dt.year
company_other_info_df['Month'] = company_other_info_df['Modify Date'].dt.month


totalCompany = company_details_df['CompanyName'].nunique()
totalSector = company_details_df['Sector'].nunique()


col1, col2, col3, col4 = st.columns(4)
with col1:
    col1.metric("Total Company",totalCompany)
with col2:
    col2.metric("Total Sector",totalSector)
    
with col3:
    slicer_options = company_details_df["CompanyName"].unique()
    selected_options = st.multiselect('Select Company:', slicer_options)
with col3:
    # slicer_options = ['None']+company_details_df["Sector"].unique().tolist()
    # selected_sector = st.selectbox('Select Sector:', slicer_options)
    selected_sector = st.multiselect('Select categories:', company_details_df['Sector'].unique())
with col4:
    slicer_options2 = company_other_info_df['Year'].unique()
    selected_options2 = st.selectbox('Select Year:', slicer_options2)
with col4:
    slicer_options2 = company_other_info_df['Month'].unique()
    selected_options2 = st.multiselect('Select Month:', slicer_options2)


sector_company_counts = company_details_df['Sector'].value_counts()
sector_wise_company_counts_df = sector_company_counts.to_frame().reset_index()
sector_wise_company_counts_df.columns = ['sector', 'count']
print(sector_wise_company_counts_df)

if selected_sector:
    filtered_df = sector_wise_company_counts_df[sector_wise_company_counts_df['sector'].isin(selected_sector)]
else:
    filtered_df= sector_wise_company_counts_df

#Display bar chart sector wise total employee
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df['sector'], filtered_df['count'], color ='blue')
for s in ['top', 'bottom', 'left', 'right']:
    ax1.spines[s].set_visible(False)
ax1.xaxis.set_ticks_position('none')
ax1.yaxis.set_ticks_position('none')
plt.xticks(rotation=90)
#ax2.invert_yaxis()
ax1.set_title('Sector Wise Total Company',
                    loc ='left', )

#-------------------------------------------------------

#Display donut chart sector wise total employee
fig2, ax2 = plt.subplots()
ax2.pie(filtered_df['count'], labels=filtered_df['sector'], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
for s in ['top', 'bottom', 'left', 'right']:
    ax2.spines[s].set_visible(False)
ax2.xaxis.set_ticks_position('none')
ax2.yaxis.set_ticks_position('none')
#plt.xticks(rotation=90)
#ax2.invert_yaxis()
ax2.set_title('Sector Wise Total Company',
                    loc ='left', )

#-------------------------------------------------------

c11,c12 = st.columns((6,4))
with c11:
    st.pyplot(fig1)
with c12:
    st.pyplot(fig2)
    #st.pyplot(fig3)

