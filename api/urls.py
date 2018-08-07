from django.conf.urls import url
from api.views import course
from api.views import degreeCourse
# from api import views
#
#
# urlpatterns = [
#     # url(r'degreecourses/',views.Courses.as_view())
# ]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls


urlpatterns = [
    url(r'courses/$',course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    url(r'degreeCourseWithTeacher/$', degreeCourse.degreeCourseWithTeacher.as_view()),
    url(r'degreeCourseWithSchoolSalary/$', degreeCourse.degreeCourseWithSchoolSalary.as_view()),
    url(r'notDegreeCourse/$', degreeCourse.notDegreeCourse.as_view())
]