from rest_framework import viewsets, permissions, generics, status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404 # get_object_or_404 불러오기
from example.models import Book
from example.serializers import BookSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()  # Book 객체(모델)의 데이터 전부 가져오기
        serializer = BookSerializer(books, many=True) # 시리얼라이저에 전체 데이터 한 번에 넣기, 직렬화(JSON 변환)
        return Response(serializer.data, status=status.HTTP_200_OK) # response.data -> 응답에 포함되는 데이터 , response.status -> 응답에 포함되는 상태
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(): # is_valid하면(유효한 데이터이면) 저장
            serializer.save() # 시리얼라이저의 역직렬화를 통해 save(), 모델시리얼라이저의 기본 create() 함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bookAPI(request, id): # urls의 id와 동일한 이름
    book = get_object_or_404(Book, bid=id) # book_id가 id인 데이터를 객체(모델) Book에서 가져오고, 없으면 404 에러 삡~
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer