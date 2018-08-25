from django.http import HttpResponse, Http404


from django.template import loader


from .models import Authority, OtherQuestions, Answers, UserAnswerMapping


from django.shortcuts import render


import uuid


def index(request):
    all_authorities = Authority.objects.order_by('added_on')
    template = loader.get_template('anonymousReporting/index.html')
    context = {
        'all_authorities': all_authorities
    }
    return render(request, 'anonymousReporting/index.html', context)
    # return HttpResponse(template.render(context, request))


def authority_detail(request, authority_id):
    try:
        authority = Authority.objects.get(pk=authority_id)
    except Authority.DoesNotExist:
        raise Http404("Authority Does Not Exist or is Unavailable")
    return render(request, 'anonymousReporting/authority_detail.html', {'authority': authority})


def raise_issue(request):
    authorities = Authority.objects.order_by('authority_name')
    questions = OtherQuestions.objects.order_by('added_on')
    context = {
        'authorities': authorities,
        'questions': questions
    }
    return render(request, 'anonymousReporting/raise_issue.html', context)


def submit_complain(request):
    questions = OtherQuestions.objects.all()
    uniqueUserID = uuid.uuid4()
    answer = Answers()
    answer.authority = Authority.objects.get(pk=request.POST.get('authority_id'))
    if request.POST.get('user_name') is not None :
        answer.user_name = request.POST.get('user_name')
    answer.user_location = request.POST.get('location')
    answer.uniqueUserID = uniqueUserID
    answer.save()
    for question in questions:
        answerValue = request.POST.get("question_"+str(question.id))
        userAnswerMapping = UserAnswerMapping()
        userAnswerMapping.answer = answerValue
        userAnswerMapping.uniqueUserID = uniqueUserID
        userAnswerMapping.uniqueQuestionID = question
        userAnswerMapping.uniqueAnswerID = answer
        userAnswerMapping.save()

    return HttpResponse("Complain has been saved successfully")