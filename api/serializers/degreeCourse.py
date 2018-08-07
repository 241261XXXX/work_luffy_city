
from rest_framework import serializers
from api import models
from api.models import Scholarship


class degreeCourseWithTeacherModelSerializer( serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    # print(teacher,type(teacher),"*********")
    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'teachers']

    def get_teachers(self, row):
        teacher_list = row.teachers.all()
        return [{'name': item.name} for item in teacher_list]

class degreeCourseWithSSModelSerializer( serializers.ModelSerializer):
    scholarship_set = serializers.StringRelatedField(many=True)
    # print("scholarships",scholarships,type(scholarships))
    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'scholarship_set']

class notDegreeCourseModelSerializer( serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'brief', 'period']

# class CourseModelSerializer(serializers.ModelSerializer):
#     level_name = serializers.CharField(source='get_level_display')
#     hours = serializers.CharField(source='coursedetail.hours')
#     course_slogan = serializers.CharField(source='coursedetail.course_slogan')
#     # recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')
#
#     recommend_courses = serializers.SerializerMethodField()
#
#     class Meta:
#         model = models.Course
#         fields = ['id','name','level_name','hours','course_slogan','recommend_courses']
#
#     def get_recommend_courses(self,row):
#         recommend_list = row.coursedetail.recommend_courses.all()
#         return [ {'id':item.id,'name':item.name} for item in recommend_list]