### --- This work for 704 - streamlit project --- By Majed

import pandas as pd
import streamlit as st
import plotly.express as px
import pickle


# Set the default figure size
plt.rcParams["figure.figsize"] = (20, 10)

### --- load excel table --- By Ali && Omar
excel_file = 'bengaluru_house_prices.xlsx'
sheet_name1 = 'bengaluru_house_prices'



# Load the dataset used for training
df_filename = 'bhp.csv'
df = pd.read_csv(df_filename)

### --- define table sheets --- By Ali && Omar
all_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name1)
                               

# Create a Streamlit web app
st.title('Bangalore House Price Prediction')

# Sidebar with input fields
st.sidebar.header('Enter Property Details')

# Location
locations = df.columns[3:]
location = st.sidebar.selectbox('Location', locations)

# Total Square Feet
sqft = st.sidebar.slider('Total Square Feet', min_value=100, max_value=10000, value=1000, step=100)

# Number of Bedrooms (BHK)
bhk = st.sidebar.number_input('Number of Bedrooms (BHK)', min_value=1, max_value=10, value=2)

# Number of Bathrooms
bath = st.sidebar.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)


def section1():
    ### --- show the tables to the user --- By Ali & OMar
    st.subheader(':blue[___________________________________________________]')
    st.info('**:blue[Table 1-1: Bengaluru_house_prices ]**')
    st.dataframe(all_s)
    st.subheader(':blue[___________________________________________________]')


def section2():
    ### --- start the choices for the charts ---  By Ali and Omar
    ### --- line-chart --- By Ali and Omar
    st.subheader(':green[___________________________________________________]')
    
    st.success('**:green[L I N E - C H A R T: choose from the criteria below for the chart]**')
    
    selected_price = st.selectbox('Select the price of the houses:', all_s['price'].unique())
    selected_size = st.selectbox('Select the size of the house:', all_s['size'].unique())
    selected_location = st.selectbox('Select the location of the house:', all_s['location'].unique())
    filtered_data = all_s[
        (all_s['price'] == selected_price) &
        (all_s['size'] == selected_size) &
        (all_s['location'] == selected_location)
    ]
    line_chart = px.line(filtered_data,
                   x='location',
                   y='price',
                   text='price',
                   color_discrete_sequence = ['#F63366']*len(all_s),
                   template= 'plotly_white')
    st.plotly_chart(line_chart)



    st.subheader(':green[___________________________________________________]')
    ### --- treemap-chart --- By Omar & Ali    
    st.success('**:green[T R E E M A P - C H A R T: choose from the criteria below for the chart]**')
    
    
    selected_availability = st.selectbox('Select the availability please:', all_s['availability'].unique())
    selected_area_type = st.selectbox('Select the year please:', all_s['area_type'].unique())
    
    filtered_data2 = all_s[
        (all_s['availability'] == area_type) &
        ( all_s['area_type'] == selected_availability)
    ]
    treemap_chart = px.treemap(filtered_data2,
                   path=[ 'availability', 'area_type', 'price'], 
                   values='price')
                  
    st.plotly_chart(treemap_chart)
    st.subheader(':green[___________________________________________________]')
    


def section3():
    ### --- start the prediction part --- By Majed
    ### --- input choices from the user --- By Majed
    st.subheader(':red[___________________________________________________]')
    st.error('**:red[Please choose the criteria below for the graduates prediction]**')
    selected_degree2 = st.selectbox('Select the degree of enrolled student:', all_s['degree'].unique())
    selected_sex2 = st.selectbox('Select the sex of enrolled student:', all_s['sex'].unique())
    write_number = st.number_input("Enter the number of enrolled students:")
    st.caption('______________________________________________')

    ### --- state if conditions for the prediction --- By Majed
    result = 0
    if write_number == 0:
        st.subheader('**:red[You have to inter a positive number for enrolled students]**')
    elif write_number <= 0:
        st.subheader('**:red[:smile:يا وااااااااد قووووووووم يا وااااااااد]**')
    elif (selected_degree2 == "PhD" and selected_sex2 == "Male"):
        result = write_number * 0.1
    elif (selected_degree2 == "PhD" and selected_sex2 == "Female"):
        result = write_number * 0.09
    elif (selected_degree2 == "Master" and selected_sex2 == "Male"):
        result = write_number * 0.15
    elif (selected_degree2 == "Master" and selected_sex2 == "Female"):
        result = write_number * 0.14
    elif (selected_degree2 == "Diploma" and selected_sex2 == "Male"):
        result = write_number * 0.57
    elif (selected_degree2 == "Diploma" and selected_sex2 == "Female"):
        result = write_number * 0.6
    elif (selected_degree2 == "Bachelor" and selected_sex2 == "Male"):
        result = write_number * 0.11
    elif (selected_degree2 == "Bachelor" and selected_sex2 == "Female"):
        result = write_number * 0.15
    else:
        result = 0
    st.subheader(f":orange[The number of expected graduation students according to the above criteria is = ] {result} students")
    st.subheader(':red[___________________________________________________]')

def section4():
  def predict_price(location, sqft, bhk, bath):
    loc_index = df.columns.get_loc(location)
    x = [sqft, bath, bhk] + [0] * (len(df.columns) - 3)
    if loc_index >= 0:
        x[loc_index] = 1
    price = model.predict([x])[0]
    return price

if st.sidebar.button('Predict Price'):
    predicted_price = predict_price(location, sqft, bhk, bath)
    st.sidebar.subheader(f'Predicted Price: ₹{predicted_price:.2f} Lakhs')

# Data Exploration
st.subheader('Data Exploration')
st.write(df.head(10))

# Display scatter plot
st.subheader('Scatter Plot for Price vs. Square Feet')
st.scatter_chart(df[['total_sqft', 'price']])

# Display histogram for price per square feet
st.subheader('Histogram for Price Per Square Feet')
st.bar_chart(df['price_per_sqft'])

# Display histogram for number of bedrooms
st.subheader('Histogram for Number of Bedrooms')
st.bar_chart(df['bhk'])

# Display histogram for number of bathrooms
st.subheader('Histogram for Number of Bathrooms')
st.bar_chart(df['bath'])

# Display a link to the dataset
st.subheader('Download the Dataset')
st.markdown('[Download the dataset](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data)')

# Display information about the project
st.subheader('About')
st.write('This web app provides a simple interface for predicting house prices in Bangalore based on location, square feet area, number of bedrooms, and number of bathrooms.')

  
def main():
    ### --- Page introduction --- By Majed
    st.set_page_config(page_title='Students Prediction')
    st.subheader('___________________________________________________')
    st.subheader(':rainbow[Statistics of Enrolled and Graduated Students in Saudi Universities During the Past 15 Years :student:]')
    st.markdown('**STREAMLIT-PROJECT: DONE ® 2023 BY:** ***ALL 704 STUDENTS***')

    # Create buttons in the sidebar --- By Majed
    st.sidebar.subheader('Select any page from below:')
    selected_section = st.sidebar.radio(
                    "", 
                    [":blue[Student data over 15 years]", 
                    ":green[Charts for Students]", 
                    ":red[Predicting graduates]",
                    ":gray[Predicting houses]"],
                    captions = [":blue[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]", 
                    ":green[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]", 
                    ":red[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]",
                    ":gray[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]"])
    st.sidebar.markdown('________________________________')
    
    
    st.sidebar.subheader('Resources')
    st.sidebar.markdown('Students Data Resource from SAMA: https://sama.gov.sa/en-us/economicreports/pages/report.aspx?cid=127#')
    st.sidebar.markdown('Download all files from GitHub: https://github.com/majidphd/student/tree/main')
    st.sidebar.markdown('Deploy your app from Streamlit: https://share.streamlit.io/')
   
    # Display the selected section --- By Majed
    if selected_section == ":blue[Student data over 15 years]":
        section1()
    elif selected_section == ":green[Charts for Students]":
        section2()
    elif selected_section == ":red[Predicting graduates]":
        section3()
    elif selected_section == ":gray[Predicting houses]":
        section4()

if __name__ == "__main__":
    main()
