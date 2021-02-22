# app name gen-audit-rules
### linux generate auditd service rules tools Version 1.0  

###### python module
```
import os, json, time
```

### auditd.conf主配置文件重要规则
```
# 以MB表示的最大日志文件容量。当达到这个容量时，会执行max_log_file _action指定的动作
# (文件设置过小，会导致生成大量文件，可以设置适当大小)
max_log_file = 6 

# 当达到max_log_file的日志文件大小时采取的动作。值必须是IGNORE、SYSLOG、SUSPEND、ROTATE和KEEP_LOGS之 一。
# IGNORE: 则在日志文件达到max_log_file后不采取动作。
# SYSLOG：则当达到文件容量时会向系统日志/var /log/messages中写入一条警告。
# SUSPEND: 则当达到文件容量后不会向日志文件写入审计消息。
# ROTATE: 则当达 到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，这个数目由num_logs参数指定。
#         旧文件的文件名将为audit.log.N，其中 N是一个数字。这个数字越大，则文件越老。
# KEEP_LOGS: 则会循环日志文件，但是会忽略num_logs参数，因此不会删除日志文件。
#
# (此配置无特别需要，请勿修改)
max_log_file_action = ROTATE

```

### 配置规则(无限节点)

```
# 自定义规则配置参考实例(conf/audit_rules_conf.json)：

{
    "web01":{
        "/data/www/web":"-p rwa",
        "/data/www/vendor":"-p rwa"
    },
    "web02":{
        "/data/www/web":"-p rwa",
        "/data/www/vendor":"-p rwa"
    },
    "web03":{
        "/data/www/web":"-p rwa",
        "/data/www/vendor":"-p rwa"
    },
    "web0N":{
        "/data/www/web":"-p rwa",
        "/data/www/vendor":"-p rwa"
    },
    "system":{
        "/etc/passwd":"-k PASSWD",
        "/etc/my.conf":"-k PASSWD"
    },
    ...
}
```

### 审计规则构成(合并)

#### 1.[系统默认规则]
conf/audit.rules.default

#### 2.[自定义规则,无限节点]
conf/audit_rules_conf.json

```
# 生成规则实例(rules默认-w)

#### APP NAME Audit Rules Created By DataTime: 2019/01/01 00:00:00 ####

#audit rule block: web
-w /data/www/web -p rwa
-w /data/www/vendor -p rwa

#audit rule block: system
-w /etc/my.conf -k PASSWD
-w /etc/passwd -k PASSWD

```

### Built rules file path
gen_audit_rules/audit.rules

###### centos 6.x path:
/etc/audit/audit.rules

###### centos 7.x path:
/etc/audit/rules.d/audit.rules

### 常用命令工具

```

auditctl : 即时控制审计守护进程的行为的工具，比如如添加规则等等。    
aureport : 查看和生成审计报告的工具。  
ausearch : 查找审计事件的工具。  
auditspd : 转发事件通知给其他应用程序，而不是写入到审计日志文件中。  
autrace : 一个用于跟踪进程的命令。  

#conf file:
/etc/audit/auditd.conf : auditd工具的配置文件。  
/etc/audit/audit.rules : 记录审计规则的文件。

```

### 审计日志格式

time : 审计时间。  
name : 审计对象  
cwd : 当前路径。  
syscall : 相关的系统调用。  
auid : 审计用户ID。  
uid 和 gid : 访问文件的用户ID和用户组ID。  
comm : 用户访问文件的命令。  
exe : 上面命令的可执行文件路径。  

