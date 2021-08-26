#Please email ningatwork@outlook.com for suggestions or advice (please i need more advice)
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
rev = pd.read_csv('mosp.csv')
rev['percento'] = rev['Rotten Tomatoes'].str.replace("%","").str.strip().astype(float)
st.sidebar.title("Sections")
options = st.sidebar.selectbox("", ("Introduction","Platform Info","Years and Ratings", "Genre Studies", "Conclusion"))

rev["netstr"] = rev['Netflix'].astype(str).str.replace("1","NETFLIX").str.replace("0", "")
rev["hulu"] = rev['Hulu'].astype(str).str.replace("1","HULU").str.replace("0", "")
rev["prime"] = rev['Prime Video'].astype(str).str.replace("1","PRIME").str.replace("0", "")
rev["disney"] = rev['Disney+'].astype(str).str.replace("1","DISNEY").str.replace("0", "")
rev["platform"] = rev["netstr"] + " " + rev["hulu"] + " " + rev["prime"] + " " + rev["disney"]
rev["platform"] = rev["platform"].str.strip().str.replace("   ", "/").str.replace("  ", "/").str.replace(" ", "/")
rev["ratingo"] = rev['Age'].str.replace("+","")
rev["ratingo"] = rev["ratingo"].fillna("0")
rev_rating = rev.loc[:, "ratingo"]
eee = rev["Genres"].str.split(",", expand = True)
ehe = np.array([list(eee[i]) for i in range(eee.shape[1])]).flatten()
eie = pd.Series(ehe, name = 'Genre').dropna().value_counts().reset_index()
fig11 = px.pie(eie, names = 'index', values = 'Genre')
eqe = rev.loc[rev.Year >= 1980].copy()
rev_plat_bar = rev["platform"].value_counts().reset_index()
fig1 = px.pie(rev, rev["platform"], color_discrete_sequence=px.colors.qualitative.Safe)
fig2 = px.bar(rev_plat_bar, x = "index", y = "platform", color = "index", log_y= True, text = "platform")
year_plat_bar = eqe["platform"].value_counts().reset_index()
fig12 = px.bar(year_plat_bar, x = "index", y = "platform", color = "index", log_y= True, text = "platform")
fig8 = px.scatter(rev, x = "IMDb", y = "percento", color = 'Year')

if options == 'Introduction':
    st.title("Introduction")
    rev.iloc[:,1:]
    st.markdown("This is the dataset used.")

if options == "Platform Info":
    st.title("Platform Info")
    st.plotly_chart(fig1)
    if st.checkbox("Show Annotation of Graph 1"):
        st.markdown("""This is a pie chart of the platform distribution in percentage.""")
    st.plotly_chart(fig2)
    if st.checkbox("Show Annotation of Graph 2"):
        st.markdown("""This is a bar chart of the amount of movies each streaming platform has. For this chart, the y values are displayed using the log() function, since this would be able to display smaller values like 1 and very large values together, making reading the graph easier.""")
    fig3 = px.box(rev[['platform', 'percento']].dropna(), x = 'platform', y = 'percento', color = "platform")
    st.plotly_chart(fig3)
    if st.checkbox("Show Annotation of Graph 3"):
        st.markdown("""This is a box plot of each platform, with the y-values being the rating. A box plot helps determine the interquartile range of a series of values.
Using this plot, one can view the range of each quartile(25%) of the data.""")
    fig9 = px.scatter(rev, x = 'Year', y = 'platform')
    st.plotly_chart(fig9)
    if st.checkbox("Show Annotation of Graph 4"):
        st.markdown("""This is a scatterplot of the distribution of years inside each streaming platform. Because the y-values, which is the streaming platform, is categorical, therefore this way of using a scatterplot results in the points being horizontally lined.""")
    st.plotly_chart(fig12)
    if st.checkbox("Show Annotation of Graph 5"):
        st.markdown("""This is a bar graph of the movies for each platform after the Year 1980.""")

if options == "Years and Ratings":
    st.title("Years and Ratings")
    rev_year = rev.sort_values("Title")
    fig5 = px.scatter(rev_year, y = "Title", x = "Year")
    st.plotly_chart(fig5)
    
    if st.checkbox("Show Annotation of Graph 6"):
        st.markdown("""This is a scatterplot of the movies and which year they were published in.""")
    
    st.plotly_chart(fig8)
    if st.checkbox("Show Annotation of Graph 7"):
        st.markdown("""This is a scatterplot comparing each movie's Rotten Tomatoes rating(percento in this case), and its IMDb rating.""")   

if options == "Genre Studies":
    st.title("Genre Studies")
    nflx = rev.loc[rev.platform == "NETFLIX"].copy()
    amzn = rev.loc[rev.platform == "PRIME"].copy()
    hulu = rev.loc[rev.platform == "HULU"].copy()
    dis = rev.loc[rev.platform == "DISNEY"].copy()
    eee = nflx["Genres"].str.split(",", expand = True)
    ege = pd.Series(list(eee[0])+list(eee[1])+list(eee[2]) + list(eee[3])).value_counts().reset_index()
    fig14 = px.pie(ege, names= 'index', values = 0)
    st.plotly_chart(fig14)
    
    if st.checkbox("Show Annotation of Netflix Graph"):
        st.markdown("""This is the pie chart for all listed genres of the Netflix movies. Drama is the most common genre, appearing at 19.2%.""")
    eee = dis["Genres"].str.split(",", expand = True)
    ege = pd.Series(list(eee[0])+list(eee[1])+list(eee[2]) + list(eee[3])).value_counts().reset_index()
    fig15 = px.pie(ege, names= 'index', values = 0)
    st.plotly_chart(fig15)
    
    if st.checkbox("Show Annotation of Disney Graph"):
        st.markdown("""This is the pie chart for all listed genres of the Disney movies. Family is the most common genre, appearing at 22.9%.""")
    eee = hulu["Genres"].str.split(",", expand = True)
    ege = pd.Series(list(eee[0])+list(eee[1])+list(eee[2]) + list(eee[3])).value_counts().reset_index()
    fig16 = px.pie(ege, names= 'index', values = 0)
    st.plotly_chart(fig16)
    
    if st.checkbox("Show Annotation of Hulu Graph"):
        st.markdown("""This is the pie chart for all listed genres of the Hulu movies. Drama is the most common genre, appearing at 19.4%.""")
    eee = amzn["Genres"].str.split(",", expand = True)
    ege = pd.Series(list(eee[0])+list(eee[1])+list(eee[2]) + list(eee[3])).value_counts().reset_index()
    fig17 = px.pie(ege, names= 'index', values = 0)
    st.plotly_chart(fig17)
    
    if st.checkbox("Show Annotation of Amazon Prime Graph"):
        st.markdown("""This is the pie chart for all listed genres of the Netflix movies. Drama is the most common genre, appearing at 19.9%.""")

if options == "Conclusion":
    st.title("Conclusion")
    st.markdown("Thank you for reading that! If you didn't and just skipped to the conclusion, please don't feel guilty -- I attached the important graphs here.")
    st.subheader("Platform Info")
    st.markdown("""The platform with the most movies is Amazon Prime, at a total of 11758 movies. Disney has the least out of the four major companies, with only 534 movies. (From Graph 2). Prime movies make up 70.2% of the whole dataset.(Graph 1)""")
    
    if st.checkbox("Feelin' Lazy for these graphs(1 and 2)?"):
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
    st.markdown("""When we take away all the movies before the year 1980, the number of movies shows a dramatic decrease. Amazon Prime, for example, has lost about 18% of its movies.(Graph 5)""")
    
    if st.checkbox("Feelin' Lazy for these graphs(5)?"):
        st.plotly_chart(fig12)
    st.subheader("Years and Ratings")
    st.markdown("""In graph 7, we can infer a trend that for those that has high IMDb ratings, they are more likely to have a high Rotten Tomatoes rating, and vice versa.""")
    
    if st.checkbox("Feelin' Lazy for these graphs(7)?"):
        st.plotly_chart(fig8)
    st.subheader("Genres")
    st.markdown("Of the four streaming platforms, Netflix, Hulu, and Amazon Prime all had drama as their most common genre. However, for Disney+, its most common genre is family. This could be because that Disney+ is mainly made for kids and people of all ages to watch, while the rest are mainly focusing on their invested drama series.")

#Hi Westminster College can I have an offer(im just sayin')
