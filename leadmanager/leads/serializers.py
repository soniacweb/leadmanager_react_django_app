from rest_framework import serializers
from leads.models import Lead 

#Lead Serializer 
#I'm going to breing in from Serializer, ModelSerializer. Essentially turning my lead model into a lead serializer, or rather, creating one from it.
#i did this by creating a class called Meta, setting my model to lead, which i brought in through ModelSerializer. 
# '__all__' brings in all the fields from the model 

class LeadSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Lead
    fields = '__all__'