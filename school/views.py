from rest_framework import generics

from .serializers import CategorySerializers, ChronologySerializers, AccreditationSerializers, TeacherSerializers
from .models import Category, Chronology, Accreditation, Teacher


class CategoryCreateListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    
    
class CategoryDeleteView(generics.DestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

   
class ChronologyCreateListView(generics.ListCreateAPIView):
    serializer_class = ChronologySerializers
    queryset = Chronology.objects.all()
    
    
class ChronologyDeleteView(generics.DestroyAPIView):
    serializer_class = ChronologySerializers
    queryset = Chronology.objects.all()
    
    
class AccreditationCreateListView(generics.ListCreateAPIView):
    serializer_class = AccreditationSerializers
    queryset = Accreditation.objects.all()
    
    
class AccreditationDeleteView(generics.DestroyAPIView):
    serializer_class = AccreditationSerializers
    queryset = Accreditation.objects.all()
    

class AccreditationDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

  
class TeacherCreateListView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
    
    
class TeacherDeleteView(generics.DestroyAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()