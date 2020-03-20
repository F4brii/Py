from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from schedule.models import Teacher, Student, Course
from schedule.serializers import TeacherSerializer

@api_view(['GET', 'POST'])
def Teacher_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
