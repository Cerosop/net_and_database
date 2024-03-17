from django.shortcuts import render
from django.http import HttpResponse
from course.models import course_enrollment
# Create your views here.
def show(request, SID, CID): 
    try:
        enrollment = course_enrollment.objects.get(SID=SID, CID=CID)
    except:
        return HttpResponse('查無資料')
    s = f'''
    <html>
    <head></head>
    <body>
    <h1>學生{SID}在{CID}的期末成績</h1>
    {enrollment.Score}
    修課結果：{'及格' if enrollment.Score >= 60 else '不及格'}
    '''
    return HttpResponse(s)