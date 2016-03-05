from rest_framework import serializers
from todos.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ("user", "name", "done", "date_created")
