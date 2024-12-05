import streamlit as st
import pandas as pd
import constants

### -- Main page -- ###

st.sidebar.markdown("# Dataset")

def loadData():
    try:
        dataFrame = pd.read_csv(constants.dataFile)
    except FileNotFoundError:
        st.write(f"File \"{constants.dataFile}\" does not exist.")

    else:
        st.header('Dataset')
        st.write('Here you can filter, sort, and search for specific values in the dataset.')
        st.write("Click on any header to sort data")

        st.subheader('Overview')

        c1,c2 = st.columns(2) # create columns to modify app layout
        
        ## allow user to filter data in app
        defaultChoice = '\'None\''
        columns = [defaultChoice]
        columns.extend(dataFrame.columns.to_list())

        with c1:
            chosenColumn = st.selectbox("Select which column to filter by", columns)

        if(chosenColumn != defaultChoice):
        # TODO: make it so that user can chose multiple values?
            columnValues = [defaultChoice]
            columnValues.extend(dataFrame[chosenColumn].unique())
            with c2:
                chosenValue = st.selectbox("Select which value to filter by", columnValues)
            if(chosenValue != defaultChoice):
                filteredDataFrame = dataFrame[dataFrame[chosenColumn] == chosenValue]
                st.dataframe(filteredDataFrame)
            else:
                st.dataframe(data=dataFrame)
        else:
            st.dataframe(data=dataFrame)
                
        ## Create search option
        st.subheader("Search dataset")
        st.write('Note: Search is case sensitive')
        c1,c2 = st.columns(2)
        with c1:
            searchValue = st.text_input("Search for any value")
        with c2:
            chosenColumn = st.selectbox("Select which column to search", columns)
        if searchValue:
            searchDataFrame = pd.DataFrame(columns=columns[1:]) # skipping first element because it is defaultChoice
            # find all rows with value and add all relevant rows to searchDataFrame
            if(chosenColumn != defaultChoice):
                searchDataFrame = pd.concat([searchDataFrame, dataFrame[ dataFrame[chosenColumn].astype(str).str.contains(searchValue) ]])
                # change back to original datatype
                searchDataFrame[chosenColumn] = searchDataFrame[chosenColumn].astype({chosenColumn: dataFrame.dtypes[chosenColumn]})
            else:
                for col in columns[1:]:
                    searchDataFrame = pd.concat([searchDataFrame, dataFrame[ dataFrame[col].astype(str).str.contains(searchValue) ]])
                    # change back to original datatype
                    searchDataFrame[col] = searchDataFrame[col].astype({col: dataFrame.dtypes[col]})
                # remove duplicate entries, in the case that mulitple columns gave search result
                # NOTE: because of 'seq' column this is possible without removing any potentially relevant information
                searchDataFrame = searchDataFrame.drop_duplicates()
            st.dataframe(searchDataFrame)
    
if __name__ == '__main__':
    loadData()