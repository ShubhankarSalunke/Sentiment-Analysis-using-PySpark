# Sentiment Analysis Application  

This project performs sentiment analysis on textual data, specifically tweets, using **PySpark**, **TextBlob**, and **Streamlit**. The application provides real-time insights into sentiment distribution and allows users to filter and download specific sentiment-based data.  

## Features  
- Sentiment classification (positive, negative, neutral) using TextBlob.  
- Real-time data processing with PySpark.  
- Interactive dashboard for sentiment visualization using Streamlit.  
- Bar and pie charts to represent sentiment distribution.  
- Option to filter tweets by sentiment classification and download filtered data as CSV.  

## File Structure  
- `spark_sentiment_analysis.py`: Backend script for sentiment classification using PySpark and TextBlob.  
- `frontend_app.py`: Streamlit-based frontend for interactive visualizations and data filtering.  
- `dataset.csv`: Input dataset containing text data.  
- `sentiment_results.csv`: Output file with sentiment classifications.  

## Prerequisites  
- Python 3.8 or higher  
- Apache Spark  
- PySpark  

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   cd sentiment-analysis
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
3. Ensure Apache Spark is installed and properly configured.

## Usage
# Backend : Sentiment Classification

1. Place your dataset in the root directory as dataset.csv.
2. Run the PySpark script to classify sentiments and save the results:
   ```bash
   python spark_sentiment_analysis.py
3.The results will be saved in sentiment_results.csv.

# Frontend : Streamlit Application

1. Move the classified dataset (sentiment_results.csv) to the root directory as tweets_with_sentiment.csv.
2. Launch the Streamlit app:
   ```bash
   streamlit run frontend_app.py
3. Open the URL displayed in your terminal to access the dashboard.
