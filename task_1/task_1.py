import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def add(request, *args, **kwargs, ):
    if request.method == 'POST' and request.body:
        try:
            answer = json.loads(request.body)
            answer_as_json = json.dumps({"answer": answer['A'] + answer['B']}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {"error": "Некорректный набор данных"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def subtract(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            answer = json.loads(request.body)
            answer_as_json = json.dumps({"answer": answer['A'] - answer['B']}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def multiply(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            answer = json.loads(request.body)
            answer_as_json = json.dumps({"answer": answer['A'] * answer['B']}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def divide(request, *args, **kwargs):
    if request.method == 'POST' and request.body:
        try:
            answer = json.loads(request.body)
            answer_as_json = json.dumps({"answer": answer['A'] / answer['B']}, indent=2)
            response = HttpResponse(answer_as_json, content_type='application/json')
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
