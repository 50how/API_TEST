# apitest

1.需安装插件：
pip3 install requests

pip3 install jsonpath-rw

pip3 install xlrd

pip3 install xlutils

pip3 install ddt

pip3 install pytest

pip3 install requests-toolbelt

~~2.修改requests源码（先不改）
将requests库中的models.py文件中的第466行:
       body = complexjson.dumps(json)
修改为:          
       body = complexjson.dumps(json,ensure_ascii=False)~~

运行
/main/run_unit_rep.py