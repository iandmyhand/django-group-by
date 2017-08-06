from datetime import datetime
from datetime import timedelta
from django.http import JsonResponse

from .models import Question


# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')
    return JsonResponse({'question_list': list(
        question for question in question_list
    )})


def initialize_questions(request):
    now = datetime.now()
    data_list = [
        {
            'category': 'APPLE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now
        }, {
            'category': 'APPLE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(days=1)
        }, {
            'category': 'APPLE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(weeks=5)
        }, {
            'category': 'BANANA',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now
        }, {
            'category': 'BANANA',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(days=1)
        }, {
            'category': 'ORANGE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now
        }, {
            'category': 'ORANGE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(days=1)
        }, {
            'category': 'ORANGE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(days=1)
        }, {
            'category': 'ORANGE',
            'text': 'What is this?',
            'point': 1,
            'pub_date': now - timedelta(weeks=5)
        },
    ]

    for data in data_list:
        Question.objects.create(
            question_category=data.get('category'),
            question_text=data.get('text'),
            point=data.get('point'),
            pub_date=data.get('pub_date')
        )

    return JsonResponse({'result': True})
