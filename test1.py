#!/usr/bin/python
# -*- coding: UTF-8 -*- 

scroce = int(raw_input('请输入分数：\n'))
if scroce >= 90:
	grade = 'A'
elif scroce >=60:
	grade = 'B'
else:
	grade = 'C'

print '%d 属于 %s ' % (scroce, grade)