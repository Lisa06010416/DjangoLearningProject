from django.http import HttpResponse
from RestFramwork.models import Teacher, Student
# Create your views here.
from RestFramwork.Serializer import TeacherSerializer, StudentSerizer, StudentHyperlinkedSerializer, \
    StudentModelSerializer, ComplexUrlStudentHyperlinkedSerializer

from rest_framework import viewsets
from rest_framework.decorators import action


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
        create 跟 update 會呼叫serializer_class裡面的creat與update來做
        會有一個get_serializer function來取得serializer_class
    """
    serializer_class = StudentHyperlinkedSerializer
    queryset = Student.objects.all()
    # 不寫的話預設為pk, 在過濾物件時預設使用(get_object_or_404)預設使用該field
    lookup_field = 'pk'
    # 不寫的話預設為None會自動設置跟lookup_field相同, 詢單一資料時URL中的引數關鍵字名稱
    # ex school/student/{student_pk}
    lookup_url_kwarg = 'student_pk'
    #  lookup_value_regex = '[0-9a-f]{32}' => 設定URL的PK的限制

    @action(detail=False, methods=['post'])
    def demo_print_one(self):
        """
            detail: 聲明該action的路徑是否與單一資源對應，及是否是xxx/<pk>/action方法名/
                    True 表示路徑格式是xxx/<pk>/action方法名/
                    False 表示路徑格式是xxx/action方法名/
            用 @action(methods=['post']) 來指定 router 產生的 url path
            這裡會產生 :
                    url pattern : student/{lookup_url_kwarg}/demo_print
                         Name   : {basename}-demo-print-one
        """
        print("~~ demo_print_one ~~~")

    @action(detail=False, methods=['post'], url_path='change-url-path-a')
    def demo_print_two(self):
        """
            url_path => 指定url的parh名稱
            這裡會產生 :
                    url pattern : student/{lookup_url_kwarg}/change-url-path-a
                         Name   : {basename}-demo-print-two
        """
        print("~~ demo_print_two ~~~")

    @action(detail=False, methods=['post'], url_name='change-url-path-b')
    def demo_print_three(self):
        """
            url_path => 指定url的parh名稱
            這裡會產生 :
                    url pattern : student/{lookup_url_kwarg}/demo_print_three
                         Name   : {basename}-change-url-path-b
        """
        print("~~ demo_print_two ~~~")


class ComplexStudentViewSet(viewsets.ModelViewSet):
    """
        將url的path變複雜 school/{teacher_id}/student/{student_id}
        不能使用router
        如果使用HyperlinkedSerializer 許要自己寫HyperlinkedRelatedField中get urlfunction
    """
    serializer_class = ComplexUrlStudentHyperlinkedSerializer
    queryset = Student.objects.all()
    # 不寫的話預設為pk, 在過濾物件時預設使用(get_object_or_404)預設使用該field
    lookup_field = 'pk'
    # 不寫的話預設為None會自動設置跟lookup_field相同, 詢單一資料時URL中的引數關鍵字名稱
    # ex school/student/{student_pk}
    lookup_url_kwarg = 'student_pk'
