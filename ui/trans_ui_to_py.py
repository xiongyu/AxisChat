#encoding:utf-8

import os
import os.path

file_dir = './'


def list_ui_file():
    """
    列出目录下的所有.ui文件
    :return: 文件名的list
    """
    ls = []
    files = os.listdir(file_dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            ls.append(filename)
    return ls

def list_qrc_file():
    """
    列出目录下的所有.ui文件
    :return: 文件名的list
    """
    ls = []
    files = os.listdir(file_dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.qrc':
            ls.append(filename)
    return ls

def trans_py_file(filename):
    """
    转换.ui扩展名到.py
    :param filename: 。ui文件名
    :return: .py文件名
    """
    return "ui_%s.py"%(os.path.splitext(filename)[0])

def trans_py_file2(filename):
    """
    转换.ui扩展名到.py
    :param filename: 。ui文件名
    :return: .py文件名
    """
    return "%s_rc.py"%(os.path.splitext(filename)[0])

def run():
    """
    执行转换
    :return: None
    """
    file_list = list_ui_file()
    for ui_file in file_list:
        py_file = trans_py_file(ui_file)
        cmd = 'pyuic5 -x {ui_dir}/{ui_file} -o {ui_dir}/{py_file}' \
            .format(ui_file=ui_file, py_file=py_file, ui_dir=file_dir)
        print(cmd)
        os.system(cmd)
    
    qrcfiles = list_qrc_file()
    for qrc_file in qrcfiles:
        py_file = trans_py_file2(qrc_file)
        cmd = 'pyrcc5 {ui_dir}/{ui_file} -o {ui_dir}/{py_file}' \
            .format(ui_file=qrc_file, py_file=py_file, ui_dir=file_dir)
        print(cmd)
        os.system(cmd)

if __name__ == "__main__":
    import sys
    file_dir = os.path.dirname(sys.argv[0])
    run()
