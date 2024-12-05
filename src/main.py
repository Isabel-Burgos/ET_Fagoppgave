import streamlit as st
import pandas as pd
import argparse
import os
# TODO: make sure that all imports are covered in requirements.txt

def setup(args):
    st.title("Dataset")

    try: # TODO: look in to if it is common to have all code within a try/catch
        dataFrame = pd.read_csv(args.data_file)
        st.write("Click on any header to sort data")

        st.subheader('Overview')

        c1,c2 = st.columns(2) # create columns to modify app layout
        
        ## allow user to filter data in app
        defaultChoice = '\'Choose a value\''
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
        searchValue = st.text_input("Search for any value")
        if searchValue:
            # create new dataset
            searchDataFrame = pd.DataFrame(columns=columns[1:]) # skipping first element because it is defaultChoice
            # find all rows with value and add all relevant rows to searchDataFrame
            for col in columns[1:]:
                searchDataFrame = pd.concat([searchDataFrame, dataFrame[ dataFrame[col].astype(str).str.contains(searchValue) ]])
                # change back to original datatype
                searchDataFrame[col] = searchDataFrame[col].astype({col: dataFrame.dtypes[col]})
            # remove duplicate entries, in the case that mulitple columns gave search result
            # NOTE: because of 'seq' column this is possible without removing any potentially relevant information
            searchDataFrame = searchDataFrame.drop_duplicates()
            st.dataframe(searchDataFrame)

        ## add statistics
        

    except FileNotFoundError:
        print(f"File \"{os.path.abspath(args.data_file)}\" does not exist.")

if __name__ == '__main__':
    # TODO: maybe reduntant with all this. The point is to use this file.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-file', default="../data/45784.csv", type=str,
        help='path to .csv file containing data to be processed')
    args = parser.parse_args()
    setup(args)