from django.test import TestCase, Client
from rest_framework.reverse import reverse

from RestFramwork.models import Teacher, Student
from RestFramwork.Serializer import TeacherSerializer, StudentSerizer, StudentModelSerializer, \
                                    StudentHyperlinkedSerializer, BookSerizer

class TeacherViewSetTest(TestCase):
    def setup(self):  # 每一個test function前都會執行setup()
        self.client = Client()

    def _creat_object(self):
        teacher = Teacher.objects.create(name="teacher1", teacher_id="id_1")
        student = Student.objects.create(name="student1",student_id="id_1",teacher=teacher)
        return teacher, student

    def test_teacher_viewsets_hyperlinked_serializer(self):
        teacher, student = self._creat_object()
        list_url = reverse("teacher-list-2")

        # ----- list -----
        response = self.client.get(list_url)
        print("\nlist data : {}".format(response.data))

class ComplexStudentViewSetTest(TestCase):
    def setup(self):  # 每一個test function前都會執行setup()
        self.client = Client()
        self.list_url =  reverse("")

    def _creat_object(self):
        teacher = Teacher.objects.create(name="teacher1", teacher_id="id_1")
        student = Student.objects.create(name="student1", student_id="id_1", teacher=teacher)
        return teacher, student

    def test_list(self):
        self._creat_object()
        list_url = reverse("complex-student-list", kwargs={"teacher_pk": 1})
        print(list_url)
        response = self.client.get(list_url)
        print(response.data)

class StudentViewSetTest(TestCase):
    def setup(self):  # 每一個test function前都會執行setup()
        self.client = Client()

    def _creat_object(self):
        teacher = Teacher.objects.create(name="teacher1", teacher_id="id_1")
        student = Student.objects.create(name="student1", student_id="id_1", teacher=teacher)
        return teacher, student

    def test_student_viewsets_hyperlinked_serializer(self):
        teacher, student = self._creat_object()
        list_url = reverse("student-list")
        detail_url = reverse("student-detail", kwargs={"student_pk": 1})

        # ----- list -----
        response = self.client.get(list_url)
        print("\nlist data : {}".format(response.data))

        # ----- creat -----
        # HyperlinkedSerializer 新增資料時foreign key需要用url
        response = self.client.post(list_url,
                                    {"name":"student2", "student_id":"id_2", "teacher":"/school/teacher/1/"})
        print("\ncreat data : {}".format(response))

        # ----- retrieve -----
        response = self.client.get(detail_url)
        print("\nretrive data : {}".format(response.data))

        # ----- update -----
        response = self.client.put(detail_url,
                                   {"name":"student3", "student_id":"id_3", "teacher":"/school/teacher/1/"}, content_type='application/json')
        print("\nupdate data : {}".format(response.data))

        # ----- partial_update -----
        response = self.client.patch(detail_url,
                                   {"name": "student4"}, content_type='application/json')
        print("\npartial_update data : {}".format(response.data))

        # ----- delete -----
        response = self.client.delete(detail_url)
        print("\ndelete data : {}".format(response))

        # ----- action -----
        demo1_url = reverse("student-demo-print-one")
        print("demo1_url : {}".format(demo1_url))
        demo2_url = reverse("student-demo-print-two")
        print("demo2_url : {}".format(demo2_url))
        demo3_url = reverse("student-change-url-path-b")
        print("demo3_url : {}".format(demo3_url))
