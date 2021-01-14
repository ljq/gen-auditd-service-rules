## app name gen-audit-rules
Linux generate auditd service rules tools Version 1.0

[CN 中文文档说明](https://github.com/iotd/gen-auditd-service-rules/blob/master/README.CN.md)  

###### python module
```
The import of os, json, time
```

Important rules for the main configuration file auditd.conf
```
The maximum log file size in MB. When this capacity is reached, the actions specified by max_log_file _action are executed
# (if the file is set too small, a large number of files will be generated. You can set the appropriate size)
Max_log_file = 6

Action taken when max_log_file's log file size is reached. The values must be one of IGNORE, SYSLOG, SUSPEND, ROTATE, and KEEP_LOGS.
# IGNORE: no action will be taken if the log file reaches max_log_file.
# SYSLOG: a warning is written to system log /var/log/messages when the file size is reached.
SUSPEND: does not write an audit message to the log file after its file capacity has been reached.
# ROTATE: loops around log files as the specified file size is reached, but only a certain number of old files are saved, specified by the num_logs parameter.
The name of the old file will be audit.log.n, where N is a number. The larger the number, the older the file.
# KEEP_LOGS: the log file is looped, but the num_logs parameter is ignored, so no log files are deleted.
#
# (this configuration does not need to be moved)
Max_log_file_action = ROTATE

```

Configuration rules (infinite nodes)

```
# custom rule configuration reference instance (conf/audit_rules_conf.json) :

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
    }
    ...
}

```

Composition of audit rules (consolidation)

[system default rules]
The conf/audit. Rules. Default

[custom rules, infinite nodes]
The conf/audit_rules_conf. Json

```
Create rule instances (rules default -w)

APP NAME Audit Rules Created By DataTime: 2019/01/01 00:00:00

# audit rule block: web
- w/data/WWW/web - p rwa
- w/data/WWW/vendor - p rwa

Rule block: # audit system
- w/etc/my. Conf -k PASSWD
- w/etc/passwd - k passwd

```

Built rules file path
Gen_audit_rules/audit rules

###### centos 6. X path:
The/etc/audit/audit rules

###### centos 7 x path:
/ etc/audit/rules. D/audit rules

Common command tools

```

Auditctl: a tool for controlling the behavior of the audit daemon in real time, such as adding rules.
Aureport: a tool for viewing and generating audit reports.
Ausearch: a tool for finding audit events.
Auditspd: forwards event notifications to other applications instead of writing them to the audit log file.
Autrace: a command used to trace a process.

# the conf file:
/etc/auditd.conf: the configuration file for the auditd tool.
/etc/audit/audit.rules: files that record audit rules.

```

The audit log format

Time: audit time.
Name: audit object
CWD: current path.
Syscall: the associated system call.
Auid: audit user ID.
Uid and gid: the user ID and user group ID that access the file.
Comm: the user's command to access the file.
Exe: the executable file path for the above command.
