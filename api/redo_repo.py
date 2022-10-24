from plotly.graph.objs import bar
from plotly import offline 
import requests

url='https://api.github.com/search/repostories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r=request.get(url,headers=headers)


response_dict = r.json()

