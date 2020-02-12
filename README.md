![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 


# leadmanager_react_django_app
A Trello style workflow and management system.

## Summary
The supplementary final project of the software engineering immersive course at GA London. The assignment was to create a full-stack application within one week. I worked solo for this project after practising with just Bootstrap, Python and Django for Redbrix.

## Brief
Build a full-stack application by making your own back end and front end
Use a Python Django API using Django REST Framework to serve your data from a Postgres database
Consume your API with a separate front-end built with React
Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
Have a visually impressive design
Be deployed online so it's publicly accessible.

# Getting started 
- pipenv shell to move into virtual environment
- npm install and pipenv install 
- rest to follow at I'm still building the app! 

### Technologies
- HTML5
- CSS3
- JavaScript (ES6)
- Git
- GitHub
- React and React extensions
- Webpack
- Babel
- Insomnia
- Python 3
- Pip
- Django
- Heroku

# Landing Page 

# Approach

| Day | Tasks |
| --- | --- |
| 1 | Create the backend: Models, Serializers, and building the API |
| 2 | TBC |
| 3 | TBC |
| 4 | TBC|
| 5 | TBC |

# Backend 

## Creating my Lead model 
First created the model for the lead app:

I wanted to pass in models.Model so I can use some of the objects from the core model class. I defined the fields I wanted, ie name. I included Charfield as it allows for the information to be text.
I also used 'EmailField' to validate user email addresses, and setting emails to unique to avoid users using the same emails. 
I then wanted the message to be optional so added in **blank=true** .
**created_at** includes a date andtime field and simply adds the date in automatically.

```class Lead(models.Model):
  name = models.CharField(max_length=100)
  name = models.EmailField(max_length=100, unique=True)
  message = models.CharField(max_length=500, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
``` 

## Serializers

After making the necessary migrations on my leads models, I had to think about serializers which take complex data like models and querysets and convert them to python datatypes, to then easily render to JSON and other content types should you wish. I'm working with a JSON api, therefore that’ll be what I want the serialisers to serve. 

I create a sterilizer class, and a class of meta: 

## Lead Serializer 

I’m going to bring in from Serializer, ModelSerializer. Essentially turning my lead model into a lead serializer, or rather, creating one from it.
I did this by creating a class called Meta, setting my model to lead, which I brought in through ModelSerializer. 
`__all__` brings in all the fields from the Lead model.

```class LeadSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Lead
    fields = '__all__'
```

## Building my API

Inside my leads folder, I created a file called **api.py** and in here, I wanted to bring in the model, viewsets and permissions from the rest_framework, and my Lead Serializer into this.

Viewsets allow us to create full crud apis (create, update, and delete), without having to specify explicit methods for the functionality. Creating a viewset means i dont need to create specific routes, i can just use the *DefaultRouter* that comes with this feature, and simply register an end point, for example *api/leads* so I can make get and post requests etc. 

## Creating my Lead Viewset

I created a class called Lead: 

```
class LeadViewSet(viewsets.ModelViewSet):
  queryset = Lead.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LeadSerializer

```




# Frontend

# Challenges

# Future Features



