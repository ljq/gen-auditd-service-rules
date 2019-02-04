## Linux、Unix System audit priority location collection

### (General rules, for reference only) 

```

-w /var/log/audit/ -k LOG_audit
-w /etc/audit/ -p wa -k CFG_audit
-w /etc/sysconfig/auditd -p wa -k CFG_auditd.conf
-w /etc/libaudit.conf -p wa -k CFG_libaudit.conf
-w /etc/audisp/ -p wa -k CFG_audisp
-a entry,always -F arch=b32 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr
-a entry,always -F arch=b32 -S mknod -S mknodat
-a entry,always -F arch=b32 -S mount -S umount -S umount2
-w /etc/cups/ -p wa -k CFG_cups
-w /etc/init.d/cups -p wa -k CFG_initd_cups
-w /etc/netlabel.rules -p wa -k CFG_netlabel.rules
-w /etc/racoon/racoon.conf -p wa -k CFG_racoon.conf
-w /etc/racoon/psk.txt -p wa -k CFG_racoon_keys
-w /etc/racoon/certs/ -p wa -k CFG_racoon_certs
-w /etc/selinux/config -p wa -k CFG_selinux_config
-w /etc/selinux/mls/ -p wa -k CFG_MAC_policy
-w /usr/share/selinux/mls/ -p wa -k CFG_MAC_policy
-w /etc/selinux/semanage.conf -p wa -k CFG_MAC_policy
-a entry,always -F arch=b32 -S adjtimex -S settimeofday -S clock_settime
-w /usr/sbin/stunnel -p x
-w /etc/security/rbac-self-test.conf -p wa -k CFG_RBAC_self_test
-w /etc/aide.conf -p wa -k CFG_aide.conf
-w /etc/cron.allow -p wa -k CFG_cron.allow
-w /etc/cron.deny -p wa -k CFG_cron.deny
-w /etc/cron.d/ -p wa -k CFG_cron.d
-w /etc/cron.daily/ -p wa -k CFG_cron.daily
-w /etc/cron.hourly/ -p wa -k CFG_cron.hourly
-w /etc/cron.monthly/ -p wa -k CFG_cron.monthly
-w /etc/cron.weekly/ -p wa -k CFG_cron.weekly
-w /etc/crontab -p wa -k CFG_crontab
-w /var/spool/cron/root -k CFG_crontab_root
-w /etc/group -p wa -k CFG_group
-w /etc/passwd -p wa -k CFG_passwd
-w /etc/gshadow -k CFG_gshadow
-w /etc/shadow -k CFG_shadow
-w /etc/security/opasswd -k CFG_opasswd
-w /etc/login.defs -p wa -k CFG_login.defs
-w /etc/securetty -p wa -k CFG_securetty
-w /var/log/faillog -p wa -k LOG_faillog
-w /var/log/lastlog -p wa -k LOG_lastlog
-w /var/log/tallylog -p wa -k LOG_tallylog
-w /etc/hosts -p wa -k CFG_hosts
-w /etc/sysconfig/network-scripts/ -p wa -k CFG_network
-w /etc/inittab -p wa -k CFG_inittab
-w /etc/rc.d/init.d/ -p wa -k CFG_initscripts
-w /etc/ld.so.conf -p wa -k CFG_ld.so.conf
-w /etc/localtime -p wa -k CFG_localtime
-w /etc/sysctl.conf -p wa -k CFG_sysctl.conf
-w /etc/modprobe.conf -p wa -k CFG_modprobe.conf
-w /etc/pam.d/ -p wa -k CFG_pam
-w /etc/security/limits.conf -p wa -k CFG_pam
-w /etc/security/pam_env.conf -p wa -k CFG_pam
-w /etc/security/namespace.conf -p wa -k CFG_pam
-w /etc/security/namespace.init -p wa -k CFG_pam
-w /etc/aliases -p wa -k CFG_aliases
-w /etc/postfix/ -p wa -k CFG_postfix
-w /etc/ssh/sshd_config -k CFG_sshd_config
-w /etc/stunnel/stunnel.conf -k CFG_stunnel.conf
-w /etc/stunnel/stunnel.pem -k CFG_stunnel.pem
-w /etc/vsftpd.ftpusers -k CFG_vsftpd.ftpusers
-a exit,always -F arch=b32 -S sethostname
-w /etc/issue -p wa -k CFG_issue
-w /etc/issue.net -p wa -k CFG_issue.net

```
