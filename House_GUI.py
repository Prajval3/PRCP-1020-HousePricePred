import pandas as pd
import streamlit as st
import pickle

# Load the pre-trained model
with open('LR.pkl', 'rb') as file:
    model = pickle.load(file)

def main():
    st.title("House Price Prediction")

    # File uploader for CSV files
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")

    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the original data
        st.write("Original Data:")
        st.write(df.head())

        # Display basic statistics
        st.write("Basic Statistics:")
        st.write(df.describe())

        # Input fields for prediction (customize based on your model's features)
        st.sidebar.header("Input Features")
        
        # Example input fields (adjust these according to your dataset's features)
        # Replace 'feature1', 'feature2', etc. with actual feature names from your dataset
        feature1 = st.sidebar.number_input('Feature 1', min_value=0.0)
        feature2 = st.sidebar.number_input('Feature 2', min_value=0.0)
        feature3 = st.sidebar.number_input('Feature 3', min_value=0.0)
        feature4 = st.sidebar.number_input('Feature 4', min_value=0.0)
        feature5 = st.sidebar.number_input('Feature 5', min_value=0.0)
        feature6 = st.sidebar.number_input('Feature 6', min_value=0.0)
        feature7 = st.sidebar.number_input('Feature 7', min_value=0.0)
        # Add more features as necessary...

        # Predict button
        if st.sidebar.button("Predict"):
            # Create a DataFrame for the input features
            input_data = pd.DataFrame({
                'feature1': [feature1],
                'feature2': [feature2],
                'feature3': [feature3],
                'feature4': [feature4],
                'feature5': [feature5],
                'feature6': [feature6],
                'feature7': [feature7],
                # Add more features as necessary...
            })

            # Make a prediction
            prediction = model.predict(input_data)
            st.write(f"Predicted House Price: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()