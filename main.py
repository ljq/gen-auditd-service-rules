#!/usr/bin/env python
#coding=utf-8
# Python 2.7
# Script Description: 
#      Linux audit.rules generate
#
# Author: Jack Liu
# DateTime: 209-01-08 18:21
#
###################################

import os, json,time, genrules

# gen rules
def main():
    # app sign set
    app_sign = "APP NAME"
    auditrules =  genrules.gen_auditrules(app_sign)
    print(auditrules)

if __name__ == '__main__':
    # main
    main()
