# 新人任务——网盘

基于青云的服务开发的一款网盘应用

### 功能

###### 1.用户上传文件到自己的空间，可以浏览上传的文件和下载文件

###### 2.用户可以将自己空间中的文件分享给其他的用户

###### 3.可以设置分享权限和分享期限



## 应用部署流程

主机系统版本：Ubuntu 16.04.1 LTS

### 1.环境搭建

##### 1.安装Python3.6

```bash
# 安装Python3.6
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6

# 安装pip并更新
$ apt-get install python3-pip
$ python3.6 -m pip install --upgrade pip

# 安装venv模块
$ apt-get install python3.6-venv
```

##### 2.使用Docker运行PostgreSQL

~~~bash
# Docker 安装
$ sudo apt-get install docker-ce docker-ce-cli containerd.io

# Docker 获取PostgreSQL官方镜像
$ docker pull postgres

# 运行
$ docker run --rm \
--name pgsql-docker \
-e POSTGRES_PASSWORD=12345678 \
-p 5432:5432 \
-v $HOME/docker/volumes/postgres:/var/lib/postgresql/data -d postgres
~~~

##### 3.安装Nginx

~~~bash
$ sudo apt-get install nginx
~~~

##### 4.使用Python的venv模块创建虚拟环境，通过requirements.txt文件安装App所需的依赖

~~~bash
# 创建虚拟环境
$ python3.6 -m venv web_py36
# 激活虚拟环境
$ source ./web_py36/bin/activate
# 安装App依赖
(web_py36)$ pip install -r [path of requirements.txt]
# 退出虚拟环境
$ deactivate
~~~

##### 5.安装进程管理软件Supervisor

~~~bash
$ sudo apt install supervisor
~~~



### 2.数据库初始化

##### 1.为应用建立数据库

~~~sql
# 进入数据库
$ psql -h localhost -U postgres

postgres=# create user admin with password '12345678';
postgres=# create database admin owner admin;
postgres=# create database black_cloud_project owner admin;
postgres=# \q
~~~

##### 2.生成迁移文件初始化数据库

~~~bash
# settings.py 配置好的前提下
# 进入到manage.py文件所在的目录
$ python manage.py makemigrations
$ python manage.py migrate
~~~



### 3.配置文件

##### 1.Django中settings.py的配置项

1. 数据库用户名、密码、库名
2. 日志输出方式及所在地址
3. 时区、语言、
4. 静态文件收集目录、允许的主机地址、是否为调试模式

##### 2.Nginx中netstore_nginx.conf配置项

1. Nginx服务器监听的端口
2. 域名或主机名
3. 路由、上游服务器地址及端口

##### 3.uWSGI中netstore_uwsgi.ini配置项

1. uWSGI 和 Nginx 通信的地址及端口
2. 最大工作进程数、每个进程中线程数
3. 是否运行在后台

##### 4.Supervisor中supervisord.conf

1. 各个受管进程的启动命令及其启动时所在的目录
2. 定义各个进程的别名、进程组中包含的进程有哪些



> 更具体的内容见配置文件中的注释



### 4.启动整个应用

进入到supervisord.conf文件所在的目录

~~~bash
$ supervisord -c ./supervisord.conf

# 进入spuervisor的命令行管理系统，查看运行状态
$ supervisorctl
~~~





