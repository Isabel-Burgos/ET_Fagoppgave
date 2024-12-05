import streamlit as st
import pandas as pd
import os
import constants
import matplotlib.pyplot as plt

st.sidebar.markdown("# Statistics and analysis")

def loadStatistics():
    try:
        dataFrame = pd.read_csv(constants.dataFile)
    except FileNotFoundError:
        st.write(f"File \"{constants.dataFile}\" does not exist.")

    else:
        st.header("Statistics and Analysis")
        st.write("Visualising relevant analyses and statistics.")

        ## find rows with missing values
        st.subheader('Missing values')
        st.write('Checking if the data set is complete.')
        # adds rows where any of the column values of that row is empty
        st.dataframe(dataFrame[ pd.isna(dataFrame).any(axis=1) ])

        ## Shared cc_numbers
        st.subheader('Duplicate credit card numbers')
        st.write('Any credit card which is listed on multiple occations in the data set would be'+
                 ' valuable to investigate. May for instance indicate multple persons being registered'+
                 ' to the same card.')
        st.dataframe(duplicatesByColumns(dataFrame, 'ccnumber'))

        ## Duplicate persons
        st.subheader('Duplicate names')
        st.write('Duplicate names can indicate that it is the same person and may therefore be of'+
                 ' interest to investigate.')
        st.dataframe(duplicatesByColumns(dataFrame, ['name/first', 'name/last']))

        ## Duplicate coordinates
        st.subheader('Duplicate coordinates')
        st.write('Duplicate transactions at the same coordinates may be of interest to investigate.')
        st.dataframe(duplicatesByColumns(dataFrame, ['latitude', 'longitude']))

        ## Map over lat long
        st.subheader("Transaction coordinates")
        st.write('Transactions occurring within an abnormal region or a distinct pattern may be of interest to investigate.')
        st.scatter_chart(data=dataFrame, x='longitude', y='latitude')


        ## Show age statistics
        st.subheader('Age statistics')

        fig = plt.figure()
        plt.hist(dataFrame['age'], bins=len(dataFrame['age'].unique()))
        plt.title('Distribution of age in dataset')
        plt.xlabel('Age')
        plt.ylabel('Count')
        st.pyplot(fig)

        c1, c2 = st.columns(2)
        with c1:
            st.write('General overview')
            st.dataframe({'Youngest': dataFrame.min()['age'],
                    'Oldest': dataFrame.max()['age'],
                    'Mean age': dataFrame.mean(numeric_only=True)['age'],
                    'Median age': dataFrame.median(numeric_only=True)['age']})
        with c2:
            st.write("Ages sorted on occurence - descending")
            st.dataframe(sortedOccurenceByColumn(dataFrame, 'age'))
        
        ## state statistics
        st.subheader('State statistics')
        st.write("States sorted on occurence - descending")
        st.dataframe(sortedOccurenceByColumn(dataFrame, 'state'))

        #fig = plt.figure()
        #plt.hist(dataFrame['state'])
        #st.pyplot(fig)

def sortedOccurenceByColumn(dataFrame, column):
    '''
    Input
    ------
    dataFrame: the data frame to be processed
    columns: string determining which column to assess

    Returns
    -------
    A new data frame containing an overview of the number of occurences of each value in 'column',
    in descending order
    '''
    counts = dataFrame[column].value_counts()
    return pd.DataFrame({column: counts.index, 'occurence': counts.values}).sort_values('occurence', ascending=False)

def duplicatesByColumns(dataFrame, columns):
    '''
    Input
    ------
    dataFrame: the data frame to be processed
    columns: string, or list of strings if it should sort by multiple columns

    Returns
    -------
    A new data frame containing any rows which has duplicate values in the assessed columns.
    Rows are sortet based on values in 'columns'.
    '''
    sharedCCDataFrame = dataFrame[dataFrame.duplicated(subset=columns, keep=False)]
    return sharedCCDataFrame.sort_values(columns)
    

if __name__ == '__main__':
    loadStatistics()