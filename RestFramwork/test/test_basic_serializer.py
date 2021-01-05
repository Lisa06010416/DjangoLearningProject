from django.test import TestCase
from RestFramwork.models import Teacher, Student
from RestFramwork.Serializer import TeacherSerializer, StudentSerizer, StudentModelSerializer, \
                                    StudentHyperlinkedSerializer, BookSerizer


class SerializerTest(TestCase):
    def setup(self):  # 每一個test function前都會執行setup()
        pass

    def test_teacher_student_serilzer(self):
        # new a teacher data
        teacher = Teacher(name="Lisa", teacher_id="a123456")
        teacher.save()
        teacher = Teacher(name="Lisa", teacher_id="a123456")
        teacher.save()

        # serialize one teacher data
        teacher_serialize = TeacherSerializer(teacher)
        print("serialize one teacher data : {}".format(teacher_serialize.data))

        # serialize teacher queryset
        teacher_queryset = Teacher.objects.all()

        teacher_queryset_serilize = TeacherSerializer(teacher_queryset, many=True) # !! 傳入多個需要加many=True
        # teacher_queryset_serilize.update(teacher_queryset)
        print("serialize teacher queryset : {}".format(teacher_queryset_serilize.data))

        # new a student data
        # serialize student data
        teacher_1 = Teacher.objects.get(id='1')
        student = Student(student_id="Tom", teacher=teacher_1)
        student.save()
        student_data = StudentSerizer(student)
        print("serialize student data : {}".format(student_data.data))

        # serialize student queryset
        student_queryset = Student.objects.all()
        student_queryset_serilize = StudentSerizer(student_queryset, many=True)
        print("serialize student queryset : {}".format(student_queryset_serilize.data))

    def test_teacher_serializer_creat(self):
        teacher = TeacherSerializer(data = {"name":"Lisa", "teacher_id":"a123546"})
        teacher.is_valid()
        teacher.save()
        pass

    def test_book_valid(self):
        # book 是一般的Serializer，因此需要自己implement creat,updata等方法
        # add a data
        bs = BookSerizer(data={'author_name': 'lisa', 'book_name': '123', "title":""})
        if bs.is_valid():
            print("add a data is valid :")
            print(bs.validated_data)
            bs.save()
        else:
            print("add a data is fail :")
            print(bs.errors)

        # add a data => valid error 因為限制了author_name不可以重複
        bs = BookSerizer(data={'author_name': 'lisa', 'book_name': '1234', "title":""})
        if bs.is_valid():
            print("add a data is valid :")
            print(bs.validated_data)
            bs.save()
        else:
            print("add a data is fail :")
            print(bs.errors)

        # add many data
        bs = BookSerizer(data=[{'author_name': 'lisa', 'book_name': '1234', "title":""},
                               {'author_name': 'lisaa', 'book_name': '1234', "title":""}], many=True)
        if bs.is_valid():
            print("add many data is valid :")
            print(bs.validated_data)
            bs.save()
        else:
            print("add many data is fail :")
            print(bs.errors)

        # UniqueTogetherValidator
        bs = BookSerizer(
            data=[{'author_name': 'lisa', 'book_name': '1234', 'title': "1234"},
                  {'author_name': 'lisa', 'book_name': '1234', 'title': "12345"}],
            many=True)
        if bs.is_valid():
            print("UniqueTogetherValidator is valid :")
            print(bs.validated_data)
            bs.save()
        else:
            print("UniqueTogetherValidator is fail :")
            print(bs.errors)

        # UniqueTogetherValidator
        bs = BookSerizer(
            data=[{'author_name': 'lisa', 'book_name': '1234567', 'title': "1234"},
                  {'author_name': 'lisa', 'book_name': '1234567', 'title': "1234"}],
            many=True)
        if bs.is_valid():
            print("UniqueTogetherValidator is valid :")
            print(bs.validated_data)
            bs.save()
        else:
            print("UniqueTogetherValidator is fail :")
            print(bs.errors)

    def test_student_model_serializer(self):
        # 印出StudentModelSerializer裡的field
        print("repr of StudentModelSerializer :")
        print(repr(StudentModelSerializer()))

        # 新增一位老師
        teacher = Teacher.objects.create(name="teacher1", teacher_id="id_1")
        # 將資料傳到StudentModelSerializer
        student_serializer_with_data = StudentModelSerializer(data={"name":"student1",
                                                                    "student_id":"id_1",
                                                                    "teacher":teacher.id})
        # 用save新增一位學生
        student_serializer_with_data.is_valid()  # !! 只有在建立時有用 data= 才可以呼叫 .is_valid()
        s = student_serializer_with_data.save()

        # 用create新增一位學生
        student_serializer_null_data = StudentModelSerializer()
        s = student_serializer_null_data.create({"name":"student2",
                                       "student_id":"id_2",
                                       "teacher_id":teacher.id})  # !! key如果用teacher的話要傳入teacher的instant

        # 查看全部的資料
        print("\nThe serializer.data in student_serializer_with_data")
        print(student_serializer_with_data.data)
        print("The serializer.data in student_serializer_null_data")
        print(student_serializer_null_data.data)
        print("The serializer.data in student_serializer_models_object")
        print(StudentModelSerializer(Student.objects.all(), many=True).data)

    def test_student_hyperlinked_serializer(self):
        print("repr of StudentHyperlinkedSerializer")
        print(repr(StudentHyperlinkedSerializer()))
