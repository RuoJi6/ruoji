# ruoji

自动生成webshell_php免杀脚本

```
更新：

4.1

2022/6/4
过安全狗，D盾，河马

4.2

修复了未知错误

4.3

添加了错误日志信息，过河马免杀，添加了严格的密码验证
error 错误日志
success 运行日志
2022/7/1 修复了linux以及mac的路径错误问题
感谢一位兄弟的提交的错误

4.4
添加了代码逻辑，并且添加了@
配合代码加密平台可以绕过云waf

5.0
添加了哥斯拉，冰蝎马免杀
可以自定义变量名长度
哥斯拉和普通一句话马，添加了cookie验证
过常见waf

5.1
添加了用户自定义一句话免杀
修改了ua界面
```

python3环境

安装模块

```python
pip install -r re.txt
```

使用：
python webshell_bypass_5.0.py -c 1
![image](https://user-images.githubusercontent.com/79234113/193225758-62377026-3a78-4601-9582-e05b81a58642.png)
参数

```python
optional arguments:
  -h, --help            show this help message and exit
  -p PHP, --php PHP     -p 文件名 or --php 文件名
  -j JSP, --jsp JSP     -j 文件名 or --jsp 文件名
  -c CONFIG, --config CONFIG
                        查看配置 -c 1 or --config 1
```

![image](https://user-images.githubusercontent.com/79234113/193223356-7a4e64e9-812b-4c32-bd95-4230a3b77044.png)


```
linux，mac和windows使用一样
使用默认的，就是当前py脚本路径下，也可以自定义
```

![image](https://user-images.githubusercontent.com/79234113/193223356-7a4e64e9-812b-4c32-bd95-4230a3b77044.png)

```
关于伪装
```

1.
![image](https://user-images.githubusercontent.com/79234113/171996466-95b63d3b-f40e-4c71-a615-b76ccf87d25f.png)

2.
![image](https://user-images.githubusercontent.com/79234113/171996472-9204ddf7-ca87-435a-9a7b-671307c3011d.png)

3.
![image](https://user-images.githubusercontent.com/79234113/171996475-bbbca0e7-f822-4977-b7bb-78ed47a63cec.png)

4.
![image](https://user-images.githubusercontent.com/79234113/171996485-eeeff904-637c-482b-8492-c8a1f490a046.png)

5.
![image](https://user-images.githubusercontent.com/79234113/171996490-fe556bef-7975-4c75-a33a-41eabf4253fd.png)

6.
![image](https://user-images.githubusercontent.com/79234113/171996496-5f812b80-573b-4bef-acca-3789d9adaecb.png)

7.
![image](https://user-images.githubusercontent.com/79234113/171996504-46c5c204-91a9-4f48-8c00-57e3180b7164.png)



目录结构：
```
success.txt 为生成成功websyhell的信息
error.txt 为错误信息
template 文件为错误模板信息
webshell_bypass_5.0.py 免杀生成模板
```




演示：
注意：Cookie验证的话，C需要大写
蚁剑
![image](https://user-images.githubusercontent.com/79234113/193223918-fa4e9857-bea4-4b47-943a-8e17e95f798a.png)
![image](https://user-images.githubusercontent.com/79234113/193223990-daefd0bb-cd8d-44f2-8d81-bebb4b31fc98.png)
![image](https://user-images.githubusercontent.com/79234113/193224017-edcc82db-fa27-4f7e-8de1-7ac628635b09.png)
![image](https://user-images.githubusercontent.com/79234113/193224058-363e57c2-7c57-4872-941e-ba4a034aa0d5.png)

哥斯拉
![image](https://user-images.githubusercontent.com/79234113/193224744-be77cc07-964c-4c15-b5b7-4674d1e1108c.png)
![image](https://user-images.githubusercontent.com/79234113/193224816-d1cc1f99-afb5-41b3-92dc-3b690779b5ce.png)
![image](https://user-images.githubusercontent.com/79234113/193225152-7140993c-9ae0-4c2a-9ced-5705a514a1b9.png)

冰蝎
![image](https://user-images.githubusercontent.com/79234113/193225423-baf0d469-9bd3-43ee-9967-a1cdb7dfd375.png)
![image](https://user-images.githubusercontent.com/79234113/193225458-3e2d97c9-5013-435d-a8ac-ae9dcef7f952.png)

免杀：
![image](https://user-images.githubusercontent.com/79234113/193227286-b036c421-aa63-4370-8140-36c5dfc5018b.png)
![image](https://user-images.githubusercontent.com/79234113/193227305-7de1f5fd-1fcc-4862-b1b6-bb9623df2160.png)
![image](https://user-images.githubusercontent.com/79234113/193227431-8364ff49-821e-4fd2-a9bd-1ebaf36f3c41.png)


```
后面还会陆续添加针对不同cms错误伪装
jsp免杀还不会写，欢迎会写的师傅加我，一起开发项目
网安交流群：655934283
```


