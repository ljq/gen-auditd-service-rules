#!/usr/bin/env python
#coding=utf-8
# Python 2.7
# Script Description: 
#      Linux audit.rules generate
#       -p rwxa 
#       Specified trigger condition: 
#        r: read，w: write; x: exec; a: attr
#
# Author: Jack Liu
# DateTime: 209-01-08 18:21
#
###################################

import os, sys, json, time

sys.dont_write_bytecode = True

def gen_auditrules(app_sign = ''):
    #real work path
    real_work_path=os.getcwd()

    #check configuration format
    fconf = open(real_work_path+"/config/audit_rules_conf.json", "r")

    conf = json.loads(fconf.read())
    fconf.close()

    current_time=time.strftime("%Y/%m/%d %H:%M:%S")
    custom_audit_rules="#### " + app_sign + " Audit Rules Created By DataTime: "+current_time+" ####\n\n"

    for item in conf:
       custom_audit_rules+="\n#audit rule block: "+item+"\n\n"
       for item_child in conf[item]:
           custom_audit_rules+="-w "+item_child+" "+conf[item][item_child]+"\n"

    custom_audit_rules+="#### END ####\n"
    #read os defaut configs
    fos_default=open(real_work_path+"/config/audit.rules.default", "r")
    audit_rules_default=fos_default.read()
    fos_default.close()

    #write rules file
    frules = open(real_work_path+"/gen_audit_rules/audit.rules", "w")

    #merge rules
    audit_rules=audit_rules_default+custom_audit_rules
    frules.write(audit_rules)
    frules.close()

    return audit_rules
