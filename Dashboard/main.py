import streamlit as st
import numpy as np
import pandas as pd



st.title("Dashboard")
"""

"""
"ファイルをアップロード"
df = st.file_uploader("ファイルあっぷろーど", type='csv')

"グラフの種類は？"
graph_option = ["折線グラフ", "棒グラフ"]
graph_select = st.selectbox("どのグラフにする？", graph_option)

if graph_select == "折線グラフ":
    graph = st.line_chart(df)

if graph_select == "棒グラフ":
    graph = st.bar_chart(df)
