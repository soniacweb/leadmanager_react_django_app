# leadmanager_react_django_app
Trello style management system

# Creating my lead model 
First created the model for the lead app:

I wanted to pass in models.Model so I can use some of the objects from the core model class. I defined the fields I wanted, ie name. I included Charfield as it allows for the information to be text.
I also used 'EmailField' to validate user email addresses, and setting emails to unique to avoid users using the same emails. 
I then wanted the message to be optional so added in `blank=true`.
`created_at` includes a date andtime field and simply adds the date in automatically.

```/class/ _Lead_(/_models_/./_Model_/):
  name = models.CharField(/max_length/=100)
  name = models.EmailField(/max_length/=100, /unique/=True)
  message = models.CharField(/max_length/=500, /blank/=True)
  created_at = models.DateTimeField(/auto_now_add/=True)
``` 

# Serializers

After making the necessary migrations on my leads models, I had to think about serializers which take complex data like models and querysets and convert them to python datatypes, to then easily render to JSON and other content types should you wish. I'm working with a JSON api, therefore that’ll be what I want the serialisers to serve. 

I create a sterilizer class, and a class of meta: 

#Lead Serializer 

#I’m going to bring in from Serializer, ModelSerializer. Essentially turning my lead model into a lead serializer, or rather, creating one from it.
#i did this by creating a class called Meta, setting my model to lead, which i brought in through ModelSerializer. 
`__all__` brings in all the fields from the Lead model.

```class LeadSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Lead
    fields = '__all__'```

#Building my API

Inside my Leads folder, I created a file called api.py.

