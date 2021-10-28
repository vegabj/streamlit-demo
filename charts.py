import streamlit as st
from sklearn.datasets import load_diabetes
import plotly.graph_objects as go
from sklearn.decomposition import PCA


@st.cache
def load_data():
    return load_diabetes(as_frame=True)


data = load_data()

"# Charts"
with st.expander("Charts"):
    df = data["frame"]

    if st.checkbox("View raw data"):
        df

    "## Plot age/bmi"
    fig = go.Figure(
        go.Scatter(
            x=df["age"],
            y=df["bmi"],
            mode="markers",
            marker=dict(color=df["target"])))

    st.plotly_chart(fig, use_container_width=True)


"# PCA"
with st.expander("PCA"):
    multi_select = st.multiselect("Choose features (minimum 2)", df.columns)

    pca = PCA(n_components=2)
    if len(multi_select) >= 2:
        components = pca.fit_transform(df[multi_select])

        if st.checkbox("PCA output"):
            components

        fig = go.Figure(
            go.Scatter(
                x=components[:, 0],
                y=components[:, 1],
                mode="markers",
                marker=dict(color=df["target"])))

        st.plotly_chart(fig, use_container_width=True)


st.sidebar.write(data["DESCR"])
