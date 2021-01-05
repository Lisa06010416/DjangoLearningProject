from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from RestFramwork.models import Book, Student, Teacher


class CustomRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Hi~~~Hi~~~'


class BookSerizer(serializers.Serializer):
    b_id = serializers.ReadOnlyField()
    # UniqueValidator => 用在單一個Field的驗證，queryset指定的object要可以找到對應的field name(book_name)
    book_name = serializers.CharField()
    title = serializers.CharField()
    author_name = serializers.CharField(validators=[UniqueValidator(queryset=Book.objects.all(), message="~~~~~~")])

    def create(self, validated_data):
        b = Book.objects.create(**validated_data)
        return b

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['book_name', 'title']
            )
        ]


class StudentSerizer(serializers.Serializer):
    student_id = serializers.CharField()
    # ----- 要顯示 foreign key 中關連到的 teacher : -----
    # teacher = serializers.PrimaryKeyRelatedField()
    teacher = serializers.CharField()  # 'teacher': 'Teacher object (1)'
    # teacher = TeacherSerializer()  # 'teacher': OrderedDict([('id', 1), ('name', 'Lisa'), ('teacher_id', 'a123456')])

class TeacherSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    teacher_id = serializers.CharField()

    # ----- 找到 老師下面的學生 models.py 下要設 related_name，且參數要=related_name -----
    # has_student = serializers.StringRelatedField(many=True)  # ('has_student', ['Student object (1)'])
    # has_student = CustomRelatedField(many=True, read_only=True)  # ('has_student', ['Hi~~~Hi~~~'])])
    has_student = StudentSerizer(many=True, read_only=True)  # ('has_student', [OrderedDict([('student_id', 'Lisa'), ('teacher', 'Teacher object (1)')])])])

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定要serializer的model
        model = Student
        # 指定要哪一些 field
        # fields = '__all__'  # 全部的field
        fields = ['id','name','student_id','teacher']  # 指定特定的field


class StudentHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    # !! Hyperlinked 會加foriegn key便為連到該物件的url !!
    # !! teacher = HyperlinkedRelatedField(queryset=Teacher.objects.all(), view_name='teacher-detail') !!
    # !! 因此需要加入 name 為 teacher-detail 的 urlpattern !!
    class Meta:
        # 指定要serializer的model
        model = Student
        # 指定要哪一些 field
        # fields = '__all__'  # 全部的field
        fields = ['id','name','student_id','teacher']  # 指定特定的field


class StudentIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {'teacher_pk': obj.teacher.id, 'student_pk': obj.id}
        return self.reverse(view_name,
                            kwargs=kwargs,
                            request=request,
                            format=format)

class ComplexUrlStudentHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    url = StudentIdentityField(view_name='complex-student-detail')
    class Meta:
        model = Student
        fields = '__all__'  # 全部的field
