# 中国空气质量历史数据筛选过滤器

* 本项目为[http://beijingair.sinaapp.com/](http://beijingair.sinaapp.com/)网站的数据提供过滤筛选

>## 使用方法

1. 获取帮助

    ```
    python dataFilter.py -h

    usage: dataFilter.py [-h] [-c [CITIES [CITIES ...]]] [-t [TYPES [TYPES ...]]]
                     [--hour [HOURS [HOURS ...]]]

    Date Filter - 数据筛选器

    optional arguments:
    -h, --help            show this help message and exit
    -c [CITIES [CITIES ...]], --city [CITIES [CITIES ...]]
                            筛选城市，以空格分隔
    -t [TYPES [TYPES ...]], --type [TYPES [TYPES ...]]
                            筛选数据参数，以空格分隔
    --hour [HOURS [HOURS ...]]
                            筛选小时，以空格分隔，默认全天
    ```

1. 运行

    将数据文件解压到data目录下
    ```
    python dataFilter.py
    ```
    执行脚本将使用默认参数运行，筛选出城市北京的PM2.5数据

1. 筛选指定城市，参数

    同样将数据放在data目录下

    ```
    python dataFilter.py -c 北京 上海 广东 -t PM2.5
    ```

    使用如上命令将筛选北京，上海，广东的PM2.5数据

