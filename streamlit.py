from PIL import Image
import pandas as pd
import streamlit as st

# st.title("MyApp")
# st.write("Hello World")

# st.header("This is a header")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>text element<<<<<<<<<<<<<<<

# st.title("Main Title")
# st.header("Header")
# st.subheader("Sub Header")
# st.text("Simple Text")
# st.markdown("**Bold Text**")
# st.success("Success Message")
# st.error("Error Message")
# st.warning("Warning Message")
# st.info("Info Message")

# user input

name = st.text_input("Enter your name")
if name:
    st.write("Hello", name)


# number input
age = st.number_input("Enter your age")
st.write("Your age is", age)

# button

if st.button("Click Me"):
    st.write("Button Clicked")

    # widgets

# select box
city = st.selectbox(
    "Select your city",
    ["Nagpur", "pune", "Mumbai", "Delhi"]
)

st.write("You selected", city)

# raduio button
gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)
st.write(gender)


if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked")


# slider


salary = st.slider(
    "Salary",
    10000,
    100000,
    25000
)

st.write(salary)


# dataframe display

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70]
})

st.dataframe(df)


# file uploader
file = st.file_uploader("Upload CSV")

if file:
    import pandas as pd
    df = pd.read_csv(file)
    st.dataframe(df)

# image display

img = Image.open("cat.png.png")
st.image(img)

# graphs

data = {
    "Year": [2021, 2022, 2023],
    "Sales": [100, 150, 200]
}

df = pd.DataFrame(data)

st.line_chart(df.set_index("Year"))

#
