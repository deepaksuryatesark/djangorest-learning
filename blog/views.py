from django.http import JsonResponse,response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)


@api_view(['GET', 'POST', 'PATCH', 'DELETE','PUT'])
def blog_specific(request, id):
    if request.method == 'GET':
        blog = Blog.objects.get(id=id)
        serilaizzer = BlogSerializer(blog)
        return JsonResponse({"data": serilaizzer.data})
    if request.method == 'PUT':
        blog = Blog.objects.get(id=id)
        serilaizzer = BlogSerializer(blog, data=request.data)
        if serilaizzer.is_valid():
            serilaizzer.save()
            return JsonResponse(serilaizzer.data)
    if  request.method == 'DELETE':
        blog = Blog.objects.get(id=id)     
        blog.delete()
        return JsonResponse({"data":"deleted successfully"})



