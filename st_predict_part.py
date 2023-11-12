### --- This work for 704 - streamlit project --- By Majed

import pandas as pd
import streamlit as st
import plotly.express as px

### --- load excel table --- By Majed
excel_file = 'student.xlsx'
sheet_name1 = 'data'
sheet_name2 = 'new'
sheet_name3 = 'grad'

### --- define table sheets --- By Majed
all_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name1)
new_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name2)
grad_s = pd.read_excel(excel_file,
                                sheet_name=sheet_name3)


def section1():
    ### --- show the tables to the user --- By Majed
    st.subheader(':blue[___________________________________________________]')
    st.info('**:blue[Table 1-1: Enrolled students in higher education for the past 15 years]**')
    st.dataframe(new_s)
    st.subheader(':blue[___________________________________________________]')
    st.info('**:blue[Table 1-2: Graduated students in higher education for the past 15 years]**')
    st.dataframe(grad_s)
    st.subheader(':blue[___________________________________________________]')

def section2():
    ### --- start the choices for the charts --- By Majed
    ### --- line-chart --- By Majed
    st.subheader(':green[___________________________________________________]')
    st.success('**:green[L I N E - C H A R T: choose from the criteria below for the chart]**')
    selected_state = st.selectbox('Select the state of the student:', all_s['state'].unique())
    selected_degree = st.selectbox('Select the degree of the student:', all_s['degree'].unique())
    selected_sex = st.selectbox('Select the sex of the student:', all_s['sex'].unique())
    filtered_data = all_s[
        (all_s['state'] == selected_state) &
        (all_s['degree'] == selected_degree) &
        (all_s['sex'] == selected_sex)
    ]
    line_chart = px.line(filtered_data,
                   x='years',
                   y='numbers',
                   text='numbers',
                   color_discrete_sequence = ['#F63366']*len(all_s),
                   template= 'plotly_white')
    st.plotly_chart(line_chart)

    st.subheader(':green[___________________________________________________]')
    ### --- treemap-chart --- By Majed    
    st.success('**:green[T R E E M A P - C H A R T: choose from the criteria below for the chart]**')
    selected_state2 = st.selectbox('Select the state please:', all_s['state'].unique())
    selected_years2 = st.selectbox('Select the year please:', all_s['years'].unique())
    filtered_data2 = all_s[
        (all_s['state'] == selected_state2) &
        ( all_s['years'] == selected_years2)
    ]
    treemap_chart = px.treemap(filtered_data2,
                   path=[ 'degree', 'sex', 'numbers'], 
                   values='numbers')
                   #text='numbers',
                   #color_discrete_sequence = ['#F63366']*len(all_s)
                   #template= 'plotly_white')
    st.plotly_chart(treemap_chart)
    st.subheader(':green[___________________________________________________]')
    
    ### --- pie-chart --- By Majed    
    st.success('**:green[P I E - C H A R T: choose from the criteria below for the chart]**')
    selected_years = st.selectbox('Select the year:', all_s['years'].unique())
    selected_degree3 = st.selectbox('Select the degree:', all_s['degree'].unique())
    filtered_data3 = all_s[ (all_s['degree'] == selected_degree3) & (all_s['years'] == selected_years)]
    pie_chart = px.pie(filtered_data3,
                title='The ratio of degree during the above year',
                values='numbers',
                names='state')
    st.plotly_chart(pie_chart)
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
                    ":red[Predicting graduates]"],
                    captions = [":blue[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]", 
                    ":green[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]", 
                    ":red[ـــــــــــــــــــــــــــــــــــــــــــــــــــ]"])
    st.sidebar.markdown('________________________________')
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

if __name__ == "__main__":
    main()
