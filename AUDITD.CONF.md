``` 
# 审计日志文件的完整路径。如果您配置守护进程向除默认/var/log/audit/外的目录中写日志文件时，
# 一定要修改它上面的文件权限，使得只有根用户有读、写和执行权限。所有其他用户都不能访问这个
# 目录或这个目录中的日志文件。
log_file =/var/log/audit/audit.log

# 写日志时要使用的格式。当设置为RAW时，数据会以从内核中检索到的格式写到日志文件中。当设置
# 为NOLOG时，数据不会写到日志文件中，但是如果用dispatcher选项指定了一个，则数据仍然会发送
# 到审计事件调度程序中
log_format = RAW

# 日志所属组
log_group = root

# 审计应采用多少优先级推进守护进程。必须是非负数。0表示没有变化。
priority_boost = 4

# 多长时间向日志文件中写一次数据。值可以是NONE、INCREMENTAL、DATA和SYNC之一。如果设置为
# NONE：        则不需要做特殊努力来将数据 刷新到日志文件中。
# INCREMENTAL:  则用freq选项的值确定多长时间发生一次向磁盘的刷新。
# DATA：        则审计数据和日志文件一直是同步的。
# SYNC：        则每次写到日志文件时，数据和元数据是同步的。
flush = INCREMENTAL

# 如果flush设置为INCREMETNAL，审计守护进程在写到日志文件中前从内核中接收的记录数
freq = 20

#max_log_file_action设置为ROTATE时要保存的日志文件数目。必须是0~99之间的数。如果设置为小于2，
# 则不会循环日志。如果递 增了日志文件的数目，就可能有必要递增/etc/audit/audit.rules中的内核
# backlog设置值，以便留出日志循环的时间。如果没有设 置num_logs值，它就默认为0，意味着从来不循环日志文件。
num_logs = 5

# 控制调度程序与审计守护进程之间的通信类型。有效值为lossy和lossless。如果设置为lossy，
# 若审计守护进程与调度程序之间的缓冲区已满 (缓冲区为128千字节)，则发送给调度程序的引入
# 事件会被丢弃。然而，只要log_format没有设置为nolog，事件就仍然会写到磁盘中。如果设 置为lossless，
# 则在向调度程序发送事件之前和将日志写到磁盘之前，调度程序会等待缓冲区有足够的空间。
disp_qos = lossy

# 当启动这个守护进程时，由审计守护进程自动启动程序。所有守护进程都传递给这个程序。可以用
# 它来进一步定制报表或者以与您的自定义分析程序兼容的不同格式 产生它们。自定义程序的示例
# 代码可以在/usr/share/doc/audit- /skeleton.c中找到。由于调度程序用根用户特权运行，因此使用
# 这个选项时要极其小心。这个选项不是必需的。
dispatcher = /sbin/audispd

# 此选项控制计算机节点名如何插入到审计事件流中。它有如下的选择：none,  hostname, fqd, numeric, and user
# None意味着没有计算机名被插入到审计事件中。hostname通过gethostname系统调用返回的名称。fqd意味着它=以主机名
# 和解决它与DNS的完全合格的域名，numeric类似于fqd除解决本机的IP地址，为了使用这个选项，你可能想要测试’hostname -i’
# 或 ’domainname-i’返回一个数字地址,另外，此选项不如果DHCP的使用是因为你可以有不同的地址，在同一台机器上的时间推荐。
# 用户是从名称选项中定义的字符串。默认值是没有
name_format = NONE

##name = mydomain

# 以兆字节表示的最大日志文件容量。当达到这个容量时，会执行max_log_file _action指定的动作
max_log_file = 6 

# 当达到max_log_file的日志文件大小时采取的动作。值必须是IGNORE、SYSLOG、SUSPEND、ROTATE和KEEP_LOGS之 一。
# IGNORE: 则在日志文件达到max_log_file后不采取动作。
# SYSLOG：则当达到文件容量时会向系统日志/var /log/messages中写入一条警告。
# SUSPEND: 则当达到文件容量后不会向日志文件写入审计消息。
# ROTATE: 则当达 到指定文件容量后会循环日志文件，但是只会保存一定数目的老文件，这个数目由num_logs参数指定。
#         老文件的文件名将为audit.log.N，其中 N是一个数字。这个数字越大，则文件越老。
# KEEP_LOGS: 则会循环日志文件，但是会忽略num_logs参数，因此不会删除日志文件。
max_log_file_action = ROTATE

# 以兆字节表示的磁盘空间数量。当达到这个水平时，会采取space_left_action参数中的动作
space_left = 75

# 当磁盘空间量达到space_left中的值时，采取这个动作。有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和 HALT。
# IGNORE:   则不采取动作。
# SYSLOG:   则向系统日志/var/log/messages写一条警告消息。
# EMAIL:    则从action_mail_acct向这个地址发送一封电子邮件，并向/var/log/messages中写一条警告消息。如果设置为 
# SUSPEND:  则不再向审计日志文件中写警告消息。如果设置为SINGLE，则系统将在单用户模式下。如果设置为SALT，则系统会关闭。
#
space_left_action = SYSLOG

# 负责维护审计守护进程和日志的管理员的电子邮件地址。如果地址没有主机名，则假定主机名为本地地址，比如root。
# 必须安装sendmail并配置为向指定电子邮件地址发送电子邮件。
action_mail_acct = root

# 以兆字节表示的磁盘空间数量。用这个选项设置比space_left_action更多的主动性动作，以防万一space_left_action没有让
# 管理员释放任何磁盘空间。这个值应小于space_left_action。如果达到这个水平，则会采取admin_space_left_ action所指定的动作。
admin_space_left = 50

# 当自由磁盘空间量达到admin_space_left指定的值时，则采取动作。有效值为IGNORE、SYSLOG、EMAIL、SUSPEND、SINGLE和HALT。
# 与这些值关联的动作与space_left_action中的相同。
admin_space_left_action = SUSPEND

# 如果含有这个审计文件的分区已满，则采取这个动作。可能值为IGNORE、SYSLOG、SUSPEND、SINGLE和HALT。与这些值关联的动作
# 与space_left_action中的相同。
disk_full_action = SUSPEND

# 如果在写审计日志或循环日志文件时检测到错误时采取的动作。值必须是IGNORE、SYSLOG、SUSPEND、SINGLE和HALT之一。
# 与这些值关的动作与space_left_action中的相同
disk_error_action = SUSPEND

# 这是在范围1、65535，一个数字值，如果指定，原因auditd听在从远程系统审计记录相应的TCP端口。审计程序可能与tcp_wrappers。
# 你可能想控制在hosts.allow入口访问和否认文件。
## tcp_listen_port = 
# 这是一个数字值，这表明有多少等待（要求但UNAC接受）的连接是允许的。默认值是5。设置过小的可能导致连接被拒绝，
# 如果太多主机开始在完全相同的时间，如电源故障后。
tcp_listen_queue = 5

# 这是一个数字值，该值表示一个地址允许有多少个并发连接。默认为1，最大为1024。设置过大可能会允许拒绝服务攻击的日志服务器。
# 还要注意的是，内核内部有一个最大的，最终将防止这种即使auditd允许它通过配置。在大多数情况下，默认应该是足够除非写一个
# 自定义的恢复脚本运行提出未发送事件。在这种情况下，您将增加的数量只有足够大，让它在过。
tcp_max_per_addr = 1

##tcp_client_ports = 1024-65535
tcp_client_max_idle = 0

# 如果设置为“yes”，Kerberos 5将用于认证和加密。默认是“no”。
enable_krb5 = no

# 这是这个服务器的主要。默认是“auditd”。鉴于这种默认情况下，服务器会寻找一个名为auditd/hostname@EXAMPLE.COM存储在/etc/audit/audit.key
# 认证本身其中主机是服务器的主机名称，如DNS查找其IP地址返回。
krb5_principal = auditd

# 这个客户的主要负责人的位置。请注意，密钥文件必须由根和模式0400所拥有。默认的是/etc/audit/audit.key
# krb5_key_file = /etc/audit/audit.key

```