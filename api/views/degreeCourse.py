import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api import models
from api.serializers.course import CourseSerializer,CourseModelSerializer
from api.serializers.degreeCourse import degreeCourseWithTeacherModelSerializer
from api.serializers.degreeCourse import degreeCourseWithSSModelSerializer,notDegreeCourseModelSerializer
from api.utils.response import BaseResponse

class degreeCourseWithTeacher(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            ser = degreeCourseWithTeacherModelSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response( ret.dict)

class degreeCourseWithSchoolSalary(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            print("queryset", queryset, "HHHHHHH1WWWWW")
            ser = degreeCourseWithSSModelSerializer(instance=queryset, many=True)
            print("ser", ser, "EEEEEERRRRRRRRREEEEE")
            ret.data = ser.data
        except Exception as e:
            print(e,'EEEEEEEEEEE')
            ret.code = 500
            ret.error = '获取数据失败'
        return Response( ret.dict)

class notDegreeCourse(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            print('ONE**********')
            queryset = models.Course.objects.filter(degree_course__isnull=True)
            print('TWO',queryset)
            ser = notDegreeCourseModelSerializer( instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response( ret.dict)

        # c. 展示所有的专题课
        # c_obj=Course.objects.filter(degree_course__isnull=True)
        # print(c_obj)
    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # c_obj=DegreeCourse.objects.all()
    # for i in c_obj:
    #     print(i.name)
    #     print(i.degreecourse_price_policy.all().values('price'))

    # degree_list = DegreeCourse.objects.all()
    # for row in degree_list:
    #     print(row.name)
    #     scholarships = row.scholarship_set.all()
    #     for item in scholarships:
    #         print('------>',item.time_percent,item.value)


