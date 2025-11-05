import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from authors.models import Author


# Create your views here.
def test(request: WSGIRequest):
    return render(request, 'test.html')


@method_decorator(csrf_exempt, name='dispatch')
class AuthorsView(View):
    def get(self, request, author_id=None):
        if author_id is None:
            authors = list(Author.objects.values())
            return JsonResponse(authors, safe=False)
        try:
            author = Author.objects.values().get(id=author_id)
            return JsonResponse(author, safe=False)
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)

    def post(self, request: WSGIRequest):
        try:
            data = json.loads(request.body)
            author = Author.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                bio=data.get('bio', ''),
                birth_date=data.get('birth_date', None),
            )
            return JsonResponse({
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'bio': author.bio,
                'birth_date': author.birth_date
            }, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))

    def put(self, request, author_id=None):
        if author_id is None:
            return HttpResponseBadRequest('Missing author_id')
        try:
            data = json.loads(request.body)
            author = Author.objects.get(id=author_id)
            author.first_name = data['first_name']
            author.last_name = data['last_name']
            author.bio = data.get('bio', '')
            author.birth_date = data.get('birth_date', None)
            author.save()
            return JsonResponse({
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'bio': author.bio,
                'birth_date': author.birth_date
            })
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
        except Exception as e:
            return HttpResponseBadRequest(str(e))

    def delete(self, request, author_id=None):
        if author_id is None:
            return HttpResponseBadRequest('Missing author_id')
        try:
            author = Author.objects.get(id=author_id)
            author.delete()
            return JsonResponse({'message': 'Author deleted successfully'})
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
