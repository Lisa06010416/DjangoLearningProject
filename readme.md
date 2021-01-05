## New a Django Project

#### new a project and app
```
django-admin startproject <projectname>
cd <projectname>
python manage.py startapp <appname>
```

#### modify setting
* settings.py : 
```
將app加入INSTALLED_APPS
LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'Asia/Taipei'
```
* urls.py
在 <appname> 資料夾下新增 urls.py
修改 projectname/urls.py
```
from django.urls import path, include
urlpatterns = [
    path('', include('<appname>.urls')),
]
```

----------------------------

## [Django REST Framework](https://www.django-rest-framework.org/)

### View

* [Generic View](https://www.django-rest-framework.org/api-guide/generic-views/) - 讓使用者方重複使用處理資料的代碼
* [Mixins](https://www.django-rest-framework.org/api-guide/generic-views/#mixins) - 提供一些actions ，此外Mixins是物件導向的一種方式，可以使用Mixins的方法而不成為其子類
* [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/) - 將相關的view結合成到一個class裡面，並且可以自動生成url path，也可以讓我們設置控制器來控制要將viewset裡的那些view結合在一起來回應request

### Serializers

​    將複雜的資料結構，像是model instance，轉換成python的資料結構。也有提供deserialization的功能，可以將資料處理後轉換回原本複雜的型態。

* [quickstart](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)

* [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
   * 不同種類的Serializers得簡單的使用方法，包含基本的Serializers、ModelSerializer 、HyperlinkedModelSerializer

* [Serializers Relation](https://www.django-rest-framework.org/api-guide/relations/)
  * 主要介紹用Relational Field來序列化models間的relation
  * 注意`serializers.RelatedField`需要被額外覆寫才可以使用，像是`StringRelatedField`、`PrimaryKeyRelatedField`、`SlugRelatedField`，也可以自訂 custom related field
  * Writable nested serializers

### [Validator](https://www.django-rest-framework.org/api-guide/validators/)

* 作用是 re-using validation logic

[Permission](https://www.django-rest-framework.org/api-guide/permissions/)

* 在每一個view執行前做確認，

### [Routers](https://www.django-rest-framework.org/api-guide/routers/)

* 幫使用者根據viewset註冊route，不需要自己設定url pattern

### [REST Framwork Renderers](https://www.django-rest-framework.org/api-guide/renderers/#renderers) 

* 將使用者要回傳的資料在處理過，像是轉為json的格式，或是API的格式等等，也可以將資料轉成放進HTML的template裡面

### Parser

* 幫使用者將接到的資料先處理過，像是Json Parser

### [Versioning](https://www.django-rest-framework.org/api-guide/versioning/#versioning)

* 對不同的使用者做不同的動作

  

-------------------------------------------

## Error  Handler

## models

```
manage.py makemigrations
manage.py migrate
```
* ForeignKey

 many-to-one，多個Students會對到1個teacher 
```
class Student(Person):
    teacher = models.ForeignKey(Teacher, related_name='has_student', on_delete=models.CASCADE)
```
self many-to-one

[models的繼承](https://kknews.cc/zh-tw/code/5vgqlv2.html)

-----------------------------

## Test

* [Writing and running tests](https://docs.djangoproject.com/en/3.1/topics/testing/overview/)
* 命名要加上test_
  
*  run with `DEBUG=False`
  
* 單元測試應該要獨立於其他測試，但Django跑測試會有順序性，會先執行直接繼承TestCase的子類，之後再執行其他test

-----------

## 環境與打包

---------------

## return http的方式

* render => return template 

  ```return render(request, 'homepage.html', context)```

* redirect => 跳轉到指定網址

  ​	``` return redirect('/quiz/')```

* httpresponse

----------------------

## User and Permission

-----------------------

## Render

* 

