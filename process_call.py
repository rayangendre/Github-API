import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store response in a variable
#.json method takes info in a JSON format and converts it into a python dictionary
response_dict = r.json()
#Explore the information
repo_dicts = response_dict['items']

repo_links, stars, labels = [],[], []
for repo_dict in repo_dicts:
    #takes the name and url and appends it to the repo links list
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"Owner: {owner}<br />Description: {description}"
    labels.append(label)

#Visualize
data = [{
    'type' : 'bar',
    'x' : repo_links,
    'y' : stars,
    #adds hovering text over each value
    'hovertext': labels,
    #Changes the colors of the data
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line' : {'width' : 1.5, 'color' : 'rgb(25, 25, 25)'},
    'opacity' : 0.6,

    }

}]

layout = {
    'title': "Most Starred Python Projects On Github",
    'titlefont' : {'size' : 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14},
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')




