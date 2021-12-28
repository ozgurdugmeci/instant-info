import streamlit as st
import streamlit.components.v1 as components
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import tweepy as tw

st.sidebar.title('Instant Info ')

st.sidebar.write('Enter criterias and press enter. Application will get the latest tweets upon your search and the language you choose.')

dummy1 = st.sidebar.text_input('Type Search Criteria', 'streamlit')
dummy2 = st.sidebar.text_input('Choose Language Code', 'en')

urly_upload= f'<a target="_blank" rel="noopener noreferrer" href="https://www.andiamo.co.uk/resources/iso-language-codes/">Click for language codes.</a>'
st.sidebar.markdown(urly_upload,unsafe_allow_html=True)

  
ara= dummy1
langu= dummy2

consumer_key= st.secrets["consumer_key"]
consumer_secret= st.secrets["consumer_secret"]


say2=1
say=0
auth = tw.AppAuthHandler(consumer_key, consumer_secret)
api = tw.API(auth)
texty=''
ana=[]
son=[]
texty2=''
for tweet in tw.Cursor(api.search_tweets, q=ara, lang=langu, count=100).items(100):
 say2=say2+1
 a=tweet.text
 texty2= a+ '\n'+ texty2
 listo=a.split()
  

   
 for i in listo:
  
  i=str(i)
  i=i.lower()
  i=i.strip()
  
  if i.startswith('http') or i.startswith('rt') or i.startswith('@') or i=='rt' or ord(i[0])>8000: 
  
   say=say+1
  else:
   ana.append(i)

texty= ' '.join(ana)
son=texty.split()

ana=[]

for i in son:
 for z in i:
  if ord(z)>400:
   
   i= i.replace(z,' '+z)
   
 ana.append(i)
  

texty= ' '.join(ana)
son=[]
son =texty.split()
ana=[]
for i in son:
 i=str(i)
 i=i.lower()
 i=i.strip()
  
 if ord(i[0])>8000: 
  say=say+1
 else:
  ana.append(i)
texty=''
texty= ' '.join(ana)



st.set_option('deprecation.showPyplotGlobalUse', False)

# Create some sample text

#texty= 'Ahh ahh ahh ve derken siz niye Ahh aHh ahH    yapma AHH yapma   YapMA'
# Create and generate a word cloud image:

wordcloud = WordCloud(background_color='BlanchedAlmond',  max_words=40, max_font_size=65, relative_scaling=1.0 ).generate(texty.lower())


# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")
#plt.show()

  

st.header('Summary')
st.pyplot()
st.header('Story')
texty2
key3=0
takip= """

<!-- Default Statcounter code for intstant_info
https://share.streamlit.io/ozgurdugmeci/instant-info/main/app.py
-->
<script type="text/javascript">
var sc_project=12694874; 
var sc_invisible=1; 
var sc_security="99a870aa"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="Web Analytics"
href="https://statcounter.com/" target="_blank"><img
class="statcounter"
src="https://c.statcounter.com/12694874/0/99a870aa/1/"
alt="Web Analytics"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code -->

"""
#st.markdown(takip, unsafe_allow_html=True)  
components.html(takip,width=200, height=200)

