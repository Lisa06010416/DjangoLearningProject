from django.urls import path, include
from RestFramwork import views
from rest_framework import routers
from RestFramwork.views import StudentViewSet, TeacherViewSet, ComplexStudentViewSet

router = routers.SimpleRouter()
router.register(prefix="student", viewset=StudentViewSet)  # basename => student
router.register(prefix="teacher", viewset=TeacherViewSet)  # basename => teacher
"""SimpleRouter 基本會自動產生兩個url 
--- url1 => student/  name => {basename}-list
           可以有兩個action : get => list, post => create
--- url2 => users/{pk}/  name => {basename}-detail
           可以有四個action : get => retrieve, put => update ,delete => destroy, patch => partial_update
"""

""" 不用 Router 也可以自己指定 """
teacher_list_2 = TeacherViewSet.as_view({'get': 'list', 'post': 'create'})

complex_student_list = ComplexStudentViewSet.as_view({"get": "list", "post":"create"})
complex_student_detail = ComplexStudentViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path(r'school/', include(router.urls)),  # school => app_name

    path(r'school/teacher_list_2/', teacher_list_2, name="teacher-list-2"),

    path(r'school/<int:teacher_pk>/complex_student_list/', complex_student_list, name="complex-student-list"),
    path(r'school/<int:teacher_pk>/complex_student_list/<int:student_pk>', complex_student_detail, name="complex-student-detail"),
]
