` ` `
The full path to the audit log file. If you configure the daemon to write log files to directories other than the default /var/log/audit/,
Be sure to modify the file permissions on it so that only root has read, write, and execute permissions. This is inaccessible to all other users
The # directory or log files in this directory.
Log_file = / var/log/audit/audit log

The format to use when writing logs. When set to RAW, the data is written to the log file in the format retrieved from the kernel. When setting
When # is NOLOG, the data is not written to the log file, but it is still sent if one is specified with the dispatcher option
Into the audit event scheduler
Log_format = RAW

# logs belong to a group
Log_group = root

How much priority should audit take to advance daemons. It has to be non-negative. Zero means no change.
Priority_boost = 4

How often data is written to the log file. The values can be one of NONE, INCREMENTAL, DATA, and SYNC. If set to
# NONE: no special effort is required to flush the data to the log file.
# INCREMENTAL: determines how often a refresh to disk occurs with the value of the freq option.
# DATA: the audit DATA and log files are always synchronized.
# SYNC: the data and metadata are synchronized each time a log file is written.
Flush = INCREMENTAL

If flush is set to INCREMETNAL, the audit daemon receives the number of records from the kernel before writing to the log file
Freq = 20

#max_log_file_action set to ROTATE the number of log files to save. It has to be something between 0 and 99. If it's less than 2,
# does not loop through the logs. If the number of log files is increased, it might be necessary to increment the kernel in /etc/audit/audit.rules
Set the value for the # backlog to allow time for the log cycle. If the num_logs value is not set, it defaults to 0, which means that the log files are never looped.
Num_logs = 5

Controls the type of communication between the scheduler and the audit daemon. Valid values are lossy and lossless. If you set it to lossy,
If the buffer between the audit daemon and the scheduler is full (128 kilobytes), it is sent to the scheduler's import
The # event is discarded. However, as long as log_format is not set to nolog, events will still be written to disk. If I set this to lossless,
# then the scheduler waits for sufficient buffer space before sending events to the scheduler and before writing the logs to disk.
Disp_qos = lossy

The audit daemon starts the program automatically when the daemon is started. All daemons are passed to this program. You can use
It can be used to further customize reports or to generate them in a different format that is compatible with your custom analyzer. Example of a custom program
The # code can be found in /usr/share/doc/audit- /skeleton. C. Because the scheduler runs with root privileges, it is used
Be extremely careful with the # option. This option is not required.
The dispatcher = / sbin/audispd

This option controls how the computer node name is inserted into the audit event stream. It has the following options: none, hostname, FQD, numeric, and user
# None means that no computer name was inserted into the audit event. Hostname is the name returned through the gethostname system call. FQD means it = with host name
# and to resolve its fully qualified domain name with DNS, numeric is similar to FQD except to resolve the native IP address. To use this option, you may want to test 'hostname-i'
# or 'domainname-i' returns a numeric address, in addition, this option is not recommended if DHCP is used because you can have different addresses on the same machine at the same time.
The # user is a string defined from the name option. The default is none
Name_format = NONE

# # name = mydomain

The maximum log file size in megabytes. When this capacity is reached, the actions specified by max_log_file _action are executed
Max_log_file = 6

Action taken when max_log_file's log file size is reached. The values must be one of IGNORE, SYSLOG, SUSPEND, ROTATE, and KEEP_LOGS.
# IGNORE: no action will be taken if the log file reaches max_log_file.
# SYSLOG: a warning is written to system log /var/log/messages when the file size is reached.
SUSPEND: does not write an audit message to the log file after its file capacity has been reached.
# ROTATE: loops around log files as the specified file size is reached, but only a certain number of old files are saved, specified by the num_logs parameter.
The file name for the old # file will be audit.log.n, where N is a number. The larger the number, the older the file.
# KEEP_LOGS: the log file is looped, but the num_logs parameter is ignored, so no log files are deleted.
Max_log_file_action = ROTATE

The amount of disk space in megabytes. When this level is reached, the action in the space_left_action parameter is taken
Space_left = 75

This action is taken when the amount of disk space reaches the value in space_left. Valid values are IGNORE, SYSLOG, EMAIL, SUSPEND, SINGLE, and HALT.
IGNORE: no action will be taken.
# SYSLOG: writes a warning message to system log /var/log/messages.
EMAIL: sends an EMAIL from action_mail_acct to this address and a warning message to /var/log/messages. If set to
SUSPEND: no longer writes warning messages to the audit log file. If set to SINGLE, the system is in single-user mode. If set to SALT, the system shuts down.
#
Space_left_action = SYSLOG

The email address of the administrator responsible for maintaining the audit daemons and logs. If the address does not have a host name, the host name is assumed to be a local address, such as root.
Sendmail must be installed and configured to send E-mail to a specified E-mail address.
Action_mail_acct = root

The amount of disk space in megabytes. Use this option to set more proactive actions than space_left_action, just in case space_left_action doesn't let you
The administrator frees up any disk space. This value should be less than space_left_action. If this level is reached, the action specified in admin_space_left_ action is taken.
Admin_space_left = 50

Action is taken when the amount of free disk space reaches the value specified in admin_space_left. Valid values are IGNORE, SYSLOG, EMAIL, SUSPEND, SINGLE, and HALT.
The action # is associated with these values is the same as in space_left_action.
Admin_space_left_action = SUSPEND

Take this action if the partition containing the audit file is full. Possible values are IGNORE, SYSLOG, SUSPEND, SINGLE, and HALT. Actions associated with these values
Same as in space_left_action.
Disk_full_action = SUSPEND

Action if an error is detected while writing an audit log or looping log file. The values must be one of IGNORE, SYSLOG, SUSPEND, SINGLE, and HALT.
The actions for # and these values are the same as those in space_left_action
Disk_error_action = SUSPEND

# this is in the range 1, 65535, a numeric value, if specified, reason auditd listens to the corresponding TCP port in the audit record from the remote system. Auditing programs may be associated with tcp_wrappers.
You may want to control access to and deny files in the hosts.allow entry.
# # tcp_listen_port =
This is a numeric value that indicates how much waiting (required but accepted by UNAC) connections are allowed. The default value is 5. Setting too small may cause the connection to be rejected,
If too many hosts start at exactly the same time, such as after a power failure.
Tcp_listen_queue = 5

This is a numeric value that indicates how many concurrent connections are allowed at an address. The default is 1, with a maximum of 1024. Setting the log server too large may allow denial of service attacks.
Also note that there is a large internal kernel that will eventually prevent this even if auditd allows it to be configured. In most cases, the default should be sufficient unless one is written
The custom recovery script runs with unsent events. In this case, you will increase the amount just enough to let it pass.
Tcp_max_per_addr = 1

# # tcp_client_ports = 1024-65535
Tcp_client_max_idle = 0

If set to "yes", Kerberos 5 will be used for authentication and encryption. The default is "no".
Enable_krb5 = no

This is the main server. The default is "auditd." Given this default, the server looks for a file named auditd/hostname@EXAMPLE.COM stored in /etc/audit/audit.key
# authentication itself where the host is the server's host name, such as DNS lookup its IP address is returned.
Krb5_principal = auditd

The position of the key person in charge of this client. Note that the key file must be owned by the root and schema 0400. The default is /etc/audit/audit.key
# krb5_key_file = / etc/audit/audit. The key

` ` `