import os
import time

# 1. 需要备份的文件与目录
# 指定在一个列表中。
# 例如在windows下
source = ['"C:\\Users\\Shooting stars\\Desktop\\Study\\Python\\code"']
# 又例如在 Mac OS X与Linux 下：
# source = ['/Users/swa/notes']
# 在这里注意到我们必须在字符中使用双引号
# 用以括起其中包含空格的名称

# 2.备份文件必须存储在一个
# 主备份目录中
# 例如在windows下:
target_dir = 'D:\\Backup'
# 又例如在Mac OS X 和 Linux下：
# target_dir = ' /Users/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径

# 3.备份文件将打包压缩成zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + ',zip'

# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) 
# 创建目录

# 5.我们使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


#运 行备份
print('Zip_command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
