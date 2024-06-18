from bs4 import BeautifulSoup
import requests
import textwrap


'''
To test the code
user_url = https://readnovelfull.vip/reverend-insanity/chapter-780-fate-immortal-gu/
html_tag = div
html_class = chr-c
'''
def main():
    user_url, html_tag, html_class = get_html_data()  # Get user inputs
    article = pharse_data(user_url, html_tag, html_class)
    save_as_text(article)
    
    

    


def get_html_data():
    '''
    This function is to collect all the neccessary informmation to scrap the website
    '''
    user_url = input('Enter url: ')
    html_tag = input('Enter the html tag(e.g, p): ')
    html_class = input('Enter Class name(leave blank if there is none): ')

    return user_url, html_tag, html_class

def pharse_data(user_url, html_tag, html_class):
    '''
    With the user information, the fuction will phase through the website provided
    using the tag and class provided, it will extract the text and assign a variable call article to it
    '''
    try:
        html_call = requests.get(user_url).text          #using the url provided, it will pullout all the html 
    except requests.exceptions.RequestException as e:
        print(f'Error fetching URL: {e}')               #incase the url isnt correct or broken
        return None
    try:
        soup =  BeautifulSoup(html_call, 'html.parser')
        if html_class:
            article = soup.find(html_tag, class_=html_class) #if the html_class is provided, this part will, else the next part will run
        else:
            article = soup.find(html_tag)                             
        
        return article
    
    except Exception as e:
        print(f'Error parsing HTML: {e}')
        return None                                      #if there is error in the prograph, the code will return nothing except the prited message


def save_as_text(article):
    '''
    The text gotten from the phase_data, will be converted to readable text and saved on the local drive
    by cleaning up each text and appending it into the text file article.txt created
    '''
    if article:
        with open('article.txt', 'a', encoding='utf-8') as ar:
            paragraphs = article.find_all('p')     # Find all <p> tags within 'article'
            
            for paragraph in paragraphs:               #loop through each line/ paragraph
                text = paragraph.get_text(strip=True)   #extract the text from the paragraph
                wrapped_text = textwrap.fill(text, width=80) #wrapping the text in a specific width 
                ar.write(f'{text}\n\n')            #append the text into the file article.txt

    


if __name__ == "__main__":
    main()
