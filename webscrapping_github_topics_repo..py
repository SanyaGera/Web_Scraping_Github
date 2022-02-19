# Overwiew of the Project
# 1. We are going to webscrap Github.com and a list of top topics.
# 2. Then we are going to take individual topics and webscrap and get data about their top repositries.
# 3. We are going to convert all this data into csv files and store them in a single folder

# Libraries Used:
#  Requests
#  bs4 for BeautifulSoup
#  Pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
# Lets get the required url from internet
#  Since we specifically want to get data about topics we will use :"https://github.com/topics"
# Let's create function to get data about topics first.
def get_topic_titles(doc):
    pass
def get_topic_description(doc):
    pass
def get_topic_url(doc):
    pass
def get_topics_data():
    required_url="https://github.com/topics"
    # requests.get helps in getting the html content of the page
    response=requests.get(required_url) 
    doc=response.text
    #Let's use BeautifulSoup to parse the html content
    soup=BeautifulSoup(doc,'html.parser')
    #We require a dictionary for fields required within the topics information and for each field required we will define a separate function.
    topics_info_disc={'Topic_Titles': get_topic_titles(doc), 'Topic_description': get_topic_description(doc), 'Topic_url': get_topic_url(doc)}
    #Since we have not defined these functions yet, we will give a prototype of these above.
    #Now we will convert this data into a dataframe using pandas
    Topics_df=pd.DataFrame(topics_info_disc)
    #Lets convert it into a csv file
    Topics_df.to_csv('Github_topics_info.csv',index=None)
# Lets define the titles function
def get_topic_titles(doc):
    soup=BeautifulSoup(doc,'html.parser')
    # Through inspection of the html content we find out that titles are present in the p tags with class shown below.
    selection_class='f3 lh-condensed mb-0 mt-1 Link--primary'
    topics_tag=soup.find_all('p',{'class':selection_class})
    topic_titles=[]
    #We save all the titles of the topics in a list.
    for tags in topics_tag:
        topic_titles.append(tags.text)
    return topic_titles
#Lets define the description function.
def get_topic_description(doc):
    soup=BeautifulSoup(doc,'html.parser')
    # Through inspection of the html content we find out that descriptions are present in the p tags with class shown below.
    desc_tags=soup.find_all('p',{'class': 'f5 color-fg-muted mb-0 mt-1'})
    topic_desc=[]
    #We save all the descriptions of the topics in a list.
    for tags in desc_tags:
        topic_desc.append(tags.text.strip())
    return topic_desc
#Lets define the url function.
def get_topic_url(doc):
    soup=BeautifulSoup(doc,'html.parser')
    # Through inspection of the html content we find out that urls are present in the parent tag of titles tag(p tags)
    selection_class='f3 lh-condensed mb-0 mt-1 Link--primary'
    url_tag=soup.find_all('p',{'class':selection_class})
    topic_url=[]
    #We save all the descriptions of the topics in a list.
    base_url="https://github.com/"
    for tags in url_tag:
        # Lets add the base url as well.
        topic_url.append(base_url+tags.parent['href'])
    return topic_url
get_topics_data()

#We are now done with topics information, so lets dig into repositiries of each topic.
#For repos, we need information:
# -Username
# -Repo name
# -Repo url
# -Stars it got
# Lets start making functions for that
def get_repo_username(doc):
    pass
def get_repo_name(doc):
    pass
def get_repo_url(doc):
    pass
def get_repo_stars(doc):
    pass
def get_repo_info():
    required_url="https://github.com/topics"
    response=requests.get(required_url) 
    doc=response.text
    topics_url_list=get_topic_url(doc)
    topics_title_name=get_topic_titles(doc)
    # This will help us get the list of all the urls og the individual topics.
    for i in range(len(topics_url_list)):
        # For each url we get the html content and pass it on to a next function.
        topics_content=requests.get(topics_url_list[i])
        topics_content_text=topics_content.text
        # Creating a dictionary for repo information
        repo_info_disc={'Username': get_repo_username(topics_content_text),'Repo_Name':get_repo_name(topics_content_text),'Repo-Url':get_repo_url(topics_content_text),'Repo_stars':get_repo_stars(topics_content_text) }
        repo_info_df=pd.DataFrame(repo_info_disc)
        # repo_info_df.to_csv(topics_title_name[i]+'.csv')
        # Making a data folder to save all the csv files in it.
        os.makedirs('Github_Data',exist_ok=True)
        'Github_Data/'+repo_info_df.to_csv(topics_title_name[i]+'.csv')
def get_repo_username(doc):
    soup=BeautifulSoup(doc,'html.parser')
    username=soup.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})
    repo_username_list=[]
    for tags in username:
        
        repo_username_list.append(tags.text.replace('\n','').strip()[:16])
    return repo_username_list
def get_repo_name(doc):
    soup=BeautifulSoup(doc,'html.parser')
    username=soup.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})
    repo_name_list=[]
    for tags in username:
        a_tag=tags.find_all('a')
        repo_name_=a_tag[1].text.strip()
        repo_name_list.append(repo_name_)
    return repo_name_list
def get_repo_url(doc):
    soup=BeautifulSoup(doc,'html.parser')
    username=soup.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})
    repo_url_list=[]
    base_url="https://github.com"
    for tags in username:
        a_tag=tags.find_all('a')
        repo_url=a_tag[1]['href']
        repo_url_list.append(base_url+repo_url)
    return repo_url_list
def get_repo_stars(doc):
    soup=BeautifulSoup(doc,'html.parser')
    stars=soup.find_all('span',{'class':'Counter js-social-count'})
    repo_stars_list=[]
    for tags in stars:
        repo_stars_list.append(tags.text)
    return repo_stars_list
get_repo_info()





