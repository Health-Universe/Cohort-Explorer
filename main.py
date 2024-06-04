import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample patient data
data = {
    'Patient ID': range(1, 21),
    'Age': [34, 45, 29, 54, 41, 36, 32, 47, 51, 38, 30, 48, 44, 37, 33, 50, 39, 42, 31, 49],
    'Sex': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female'],
    'BRCA2 Result': ['Positive', 'Negative', 'Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Positive']
}

df = pd.DataFrame(data)

def main():
    st.title("Cohort Explorer for Physicians")
    
    st.write("""
    ## Description
    This app allows physicians to explore patient cohorts based on BRCA2 test results. The data includes sample patient information such as age, sex, and BRCA2 test results.
    """)

    # Sidebar filters
    st.sidebar.header("Filter Options")
    age_range = st.sidebar.slider("Select Age Range", 0, 100, (20, 60))
    sex_filter = st.sidebar.multiselect("Select Sex", options=df['Sex'].unique(), default=df['Sex'].unique())
    brca2_filter = st.sidebar.multiselect("Select BRCA2 Result", options=df['BRCA2 Result'].unique(), default=df['BRCA2 Result'].unique())

    # Filter data based on sidebar selections
    filtered_df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) & (df['Sex'].isin(sex_filter)) & (df['BRCA2 Result'].isin(brca2_filter))]

    # Display filtered data
    st.write("### Filtered Patient Data")
    st.dataframe(filtered_df)

    # Visualize the data
    st.write("### Cohort Visualization")
    fig, ax = plt.subplots()
    filtered_df['BRCA2 Result'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title('BRCA2 Results in Filtered Cohort')
    ax.set_xlabel('BRCA2 Result')
    ax.set_ylabel('Count')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
