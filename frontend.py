import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tweets_with_sentiment.csv')

st.title('Sentiment Analysis of Tweets')

st.subheader('Sample Data')
st.write(df.head())

sentiment_counts = df['sentiment_classification'].value_counts()

st.subheader('Sentiment Distribution')
st.bar_chart(sentiment_counts)

st.subheader('Sentiment Distribution (Pie Chart)')
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  
st.pyplot(fig)

st.subheader('Additional Insights')
average_sentiment = df['sentiment_classification'].value_counts(normalize=True) * 100
st.write('Percentage of Sentiment Classifications:')
st.write(average_sentiment)

st.sidebar.header('Filter Tweets')

selected_sentiment = st.sidebar.selectbox(
    'Select Sentiment Classification',
    options=df['sentiment_classification'].unique()
)

filtered_df = df[df['sentiment_classification'] == selected_sentiment]


st.subheader(f'Tweets with Sentiment: {selected_sentiment}')
st.write(filtered_df[['User', 'Text']]) 


csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_tweets.csv',
    mime='text/csv'
)

st.sidebar.markdown("""
    ### About
    This application performs sentiment analysis on tweets. You can explore the sentiment distribution, view filtered tweets, and download them.
""")
