#!/usr/bin/python3

import pymysql
from globall import *

class Mysql:
	def __init__(self, user_, password_, dbname):
		try:
			self.db = pymysql.connect(user = user_, password = password_)
		except:
			printError("can't connect to db, please check the user and password")
		try:
			self.db.query('USE '+ dbname)
		except:
			printError("can't USE database " + dbname)
		self.cur = self.db.cursor()
		printInfo('database ' + dbname + ' init is OK')


	def login_up(self, s, table_login):
		user_name , password = s.split(',')
		cmd = 'SELECT user_id FROM ' + table_login + ' WHERE user_name = \'' + user_name + '\''
		try:
			self.cur.execute(cmd)
		except:
			printError("can't SELECT FROM " + table_login)
		if self.cur.fetchall() :
			print("this name has been used, please change another one")
			return -1
		else:
			cmd = "SELECT user_id FROM " + table_login + " ORDER BY user_id"
			try:
				self.cur.execute(cmd)
			except:
				printError("can't SELECT FROM " + table_login)
			xlist = self.cur.fetchall()
			userID = str(firstMinNum(xlist))
			cmd = 'INSERT INTO '+ table_login +' (user_id ,user_name ,password) VALUES(\''+ userID +'\',\'' + user_name + '\', \'' + password + '\')'
			try:
				self.cur.execute(cmd)
				self.db.commit()
			except:
				printError("can't INSERT INTO " + table_login)
		print("login up OK")
		return 1


	def login_in(self, s, table_login):
		user_name , password = s.split(',')
		try:
			cmd = 'SELECT user_id, password FROM ' + table_login + ' WHERE user_name = \'' + user_name + '\''
			self.cur.execute(cmd)
		except:
			printError("can't SELECT FROM " + table_login)
		pwd = self.cur.fetchall()
		if len(pwd) != 1:
			print("this username haven't login in, please login in first")
			return -1
		else:
			if password == pwd[0][1]:
				printInfo("login in suceed")
				return 1
			else:
				printError("password error")
			return -2


	def create_room(self, s, table_room):
		creator, ispassword, password = s.split(',')
		cmd = "SELECT room_id FROM " + table_room + " ORDER BY room_id"
		try:
			self.cur.execute(cmd)
		except:
			printError("can't SELECT FROM " + table_room)
		xlist = self.cur.fetchall()
		print(xlist)
		roomID = str(firstMinNum(xlist))
		cmd = 'INSERT INTO '+ table_room +' (room_id , creator, is_password, password) VALUES('+ roomID +',\'' + creator + '\', ' + ispassword.upper() + ', \'' + password + '\')'
		print(cmd)
		try:
			self.cur.execute(cmd)
			self.db.commit()
		except:
			printError("can't INSERT INTO " + table_room)
			return -1
		printInfo("room " + roomID + " is created...")
		return roomID


	def delete_room(self, s ,table_room):
		roomID, user = s.split(',')
		cmd = "SELECT creator FROM " + table_room + " WHERE room_id = " + roomID #+ "AND creator = " + "'user'"
		try:
			self.cur.execute(cmd)
		except:
			printError("can't SELECT FROM " + table_room)
		rec = self.cur.fetchall()
		if len(rec) == 0:
			printError("the room does not exist...")
			return -2
		if(rec[0][0] != user):
			printError("this user don't have right to delete the room...")
			return -1
		else:
			cmd = "DELETE FROM " + table_room + " WHERE room_id = " + roomID
			print(cmd) 
			try:
				self.cur.execute(cmd)
				self.db.commit()
			except:
				printError("can't DELETE FROM " + table_room)
			printInfo("room " + roomID + " is deleted...")
			return 1


if __name__ == '__main__':
	mysql = Mysql(user_ = "root", password_ = "1234", dbname = "chatroom")
	#roomID = mysql.create_room(s = 'test4,True,123', table_room = 'room')
	mysql.delete_room(s = '2,test4', table_room = 'room')

