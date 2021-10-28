import streamlit as st
from sklearn.datasets import load_diabetes

"""
# Data visualization using streamlit
> This page contains some of the **possible** modules for streamlit.

using _markdown_ 👈
"""


st.subheader("Latex")
st.latex("\int ax^2 \,dx")


st.subheader("Code")
st.code(
    """
    st.subheader("Latex")
    st.latex("\int ax^2 \,dx")

    data = load_diabetes(as_frame=True)
    \"\"\"
    ## Display data
    \"\"\"
    data["frame"] # 👈 draws a dataframe

    st.table(df[:5]) # 👈 draws a static dataframe

    data["DESCR"] # 👈 dump sklearns markdown of dataset description
    """
)


@st.cache
def load_data():
    return load_diabetes(as_frame=True)


data = load_data()
df = data["frame"]
"""
## Display data
"""
data["frame"]  # 👈 draws data

# Static Table
st.table(df[:5])

# Display markdown description of dataset
data["DESCR"]

"## feature names"
st.json(data["feature_names"])


"## Sliders and Metrics in columns"

col1, col2 = st.columns(2)
slider = col1.slider(
    "Sample selector", min_value=1, max_value=df.shape[0] - 3, step=1
)
column = col2.select_slider("Metric", options=df.columns)

col3, col4, col5 = st.columns(3)
metric = col3.metric(column, df[column][slider], df[column][slider - 1])
metric = col4.metric(column, df[column][slider + 1], df[column][slider])
metric = col5.metric(column, df[column][slider + 2], df[column][slider + 1])


"## Code for sliders"
st.code(
    """
    col1, col2 = st.columns(2)
    slider = col1.slider("Sample selector", min_value=1, max_value=df.shape[0] - 3, step=1)
    column = col2.select_slider("Metric", options=df.columns)

    col3, col4, col5 = st.columns(3)
    metric = col3.metric(column, df[column][slider], df[column][slider-1])
    metric = col4.metric(column, df[column][slider+1], df[column][slider])
    metric = col5.metric(column, df[column][slider+2], df[column][slider+1])
    """
)

"# Inputs and forms"
button = st.button("Clicky!", help="press the button to see possible options")

if button:
    st.markdown(
        "https://docs.streamlit.io/library/api-reference/widgets",
        unsafe_allow_html=True
    )


if st.checkbox("I would like to download this demo"):
    with open("display.py") as fh:
        download_button = st.download_button(
            label="Download",
            data=fh,
            file_name="my_app.py"
        )


with st.form("form1"):
    st.number_input("Pick a number", 0, 10)
    st.date_input("Date")
    st.time_input("Meetings")
    st.text_input("Name")
    st.text_area("Text area")
    st.selectbox("Pick one", ["Cats", "Dogs"])
    st.multiselect("Pick all", ["Cats", "Dogs"])
    st.radio("Pick one", ["Yes", "No"])
    st.file_uploader("Upload files")
    st.form_submit_button("Send")


name = st.text_input("Name")
if not name:
    st.warning("Please input a name.")
    st.stop()
st.success(f"Thank you {name}!")

"# Hacky?"
# Dirty hacks
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(204, 49, 49);
}
</style>""", unsafe_allow_html=True)


st.code(
    '''
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(204, 49, 49);
    }
    </style>""", unsafe_allow_html=True)
    '''
)
b = st.button("test")
