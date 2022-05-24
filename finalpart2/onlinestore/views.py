from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from onlinestore.serializers import *
from onlinestore.models import *
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.decorators import action

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class JournalListAPIView(APIView):
    def get(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalViewSet(APIView):
    def get_object(self, pk):
        try:
            return Journal.objects.get(id=pk)
        except Journal.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        journal = self.get_object(pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        journal = self.get_object(pk)
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        journal = self.get_object(pk)
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)