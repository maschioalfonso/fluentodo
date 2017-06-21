## Synopsis
This project was build as a **test** for the company Fluendo.
 
 
## Installation
 
In order to run this project you need:
 
* Docker
* Python3
 
Move to the root folder of this project with the virtual environment activated and run:
 
`$ docker-compose build;`
 
`$ docker-compose up;`
 
You will find the app in:
 
[http://0.0.0.0:8000/list/](http://0.0.0.0:8000/list/)
## API Reference
 
Since this project implements [Django Rest Framework](http://www.django-rest-framework.org/)
 
You can go to: 
 
[http://0.0.0.0:8000/list/todolist-api/](http://0.0.0.0:8000/list/todolist-api/)
 
And interact with the API **or** make you own request like:
 
```
curl -X GET \
  http://0.0.0.0:8000/list/todolist-api \
  -H 'accept: application/json; indent=4' \
  -H 'authorization: Basic <token>' \
  -H 'cache-control: no-cache'
```
 
Note this API use Basic authorization :thumbsdown:
 
## Tests
 
No test were included  ¯\\_(ツ)_/¯
 
## WIP
 
Since the 4 hours mark. I left some criticals this todo, here is the list:
 
* Implement an Oauth2 authorization and authentication method.
* Make integrations test
* Make unit test
* The message “ToDo item {Name} has been deleted correctly” is not implemented, but the parameter is set in the query string. `?just_delete_name=<name>` ¯\\_(ツ)_/¯
 
 
## License
 
A short snippet describing the license (MIT, Apache, etc.)
