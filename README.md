##Django 
前后端不分离（耦合度高，适合纯网页的应用！）

##Django REST framework
前后端分离（耦合度低，前端通过访问接口来对数据进行增删改查）
>[为什么要前后端分离](https://blog.csdn.net/sod5211314/article/details/80601724?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase)


#常用命令
安装卸载
```
pip install django
pip install django==2.2.2
pip install upgrade django
pip uninstall django
```
查询当前django版本
```
$ python -m django --version
```

CMD当前路径下创建项目
```
$ django-admin startproject Project_name
```

启动开发用服务器(默认8000端口)
```
$ python manage.py runserver
```

若要公开处刑
```
settings.py文件中DEBUG代码
DEBUG = False
ALLOWED_HOSTS = ["*"]
$ python manage.py runserver 0.0.0.0:8000
```

创建应用
```
$ python manage.py startapp App_name
```
##改变数据库模型只需这三步：
* 1.编辑 models.py 文件，改变模型。
* 2.运行 python manage.py makemigrations 为模型的改变生成迁移文件。
* 3.运行 python manage.py migrate 来应用数据库迁移。


创建数据库模型 (按需求编辑APP_name/models.py 文件)

激活数据库模型 (INSTALLED_APPS 添加应用.apps.class_name，命令会创建0001_initial.py迁移文件)
```
$ python manage.py makemigrations App_name
```
应用数据库配置 (检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表)
```
$ python manage.py migrate
```
阅读迁移文件
```
$ python manage.py sqlmigrate App_name 0001
```

检查项目中的问题
```
$ python manage.py check
```


开启命令行直接对表模型进行操作
```
$ python manage.py shell
```


创建一个管理员账号 用于http://127.0.0.1:8000/admin登录
```
$ python manage.py createsuperuser
Username:admin
Email:329189987@qq.com
Password:admin
Password:admin
```
