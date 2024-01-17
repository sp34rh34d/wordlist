#!/usr/bin/env python3

import argparse
import sys
from os import path

class users():
    def __init__(self,lastname_file,firstname_file,chars,lastname,firstname):
        self.lastname_file=lastname_file
        self.firstname_file=firstname_file
        self.lastname=lastname
        self.firstname=firstname
        self.chars=chars
    
    def format1(self):# flastname
        if self.lastname==None and self.lastname_file==None:
            print("lastname required!")
            sys.exit()
        if self.lastname!=None:
            for x in self.chars:
                print(f"{x}{self.lastname}")
        else:
            if not path.isfile(self.lastname_file):
                print("File not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()

            for x in self.chars:
                for lastname in lastnames_list.split("\n"):
                    if lastname !="":
                        print(f"{x}{lastname}")
            
        

    def format2(self):# firstnamelastname
        if self.lastname==None and self.lastname_file==None:
            print("lastname required!")
            sys.exit()
        if self.firstname==None and self.firstname_file==None:
            print("firsname required!")
            sys.exit()

        if self.firstname !=None and self.lastname_file != None:
            if not path.isfile(self.lastname_file):
                print(f"File {self.lastname_file} not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()
    
            for lastname in lastnames_list.split("\n"):
                if lastname!="":
                    print(f"{self.firstname}{lastname}")

        if self.firstname !=None and self.lastname != None:
            print(f"{self.firstname}{self.lastname}")

        if self.firstname_file !=None and self.lastname != None:
            if not path.isfile(self.firstname_file):
                print(f"File {self.firstname_file} not found!")
                sys.exit()

            firstnames_list=""
            with open(self.firstname_file,"r") as firstnames:
                firstnames_list=firstnames.read()
    
            for firstname in firstnames_list.split("\n"):
                if firstname!="":
                    print(f"{firstname}{self.lastname}")

        if self.firstname_file !=None and self.lastname_file != None:
            if not path.isfile(self.lastname_file):
                print(f"File {self.lastname_file} not found!")
                sys.exit()
            if not path.isfile(self.firstname_file):
                print(f"File {self.firstname_file} not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()

            firstnames_list=""
            with open(self.firstname_file,"r") as firstnames:
                firstnames_list=firstnames.read()
    
            for firstname in firstnames_list.split("\n"):
                if firstname !="":
                    for lastname in lastnames_list.split("\n"):
                        if lastname!="":
                            print(f"{firstname}{lastname}")

    
    def format3(self):# f.lastname
        if self.lastname==None and self.lastname_file==None:
            print("lastname required!")
            sys.exit()
        if self.lastname!=None:
            for x in self.chars:
                print(f"{x}{self.lastname}")
        else:
            if not path.isfile(self.lastname_file):
                print("File not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()

            for x in self.chars:
                for lastname in lastnames_list.split("\n"):
                    if lastname !="":
                        print(f"{x}.{lastname}")

    def format4(self):# firstname.lastname
        if self.lastname==None and self.lastname_file==None:
            print("lastname required!")
            sys.exit()
        if self.firstname==None and self.firstname_file==None:
            print("firsname required!")
            sys.exit()

        if self.firstname !=None and self.lastname_file != None:
            if not path.isfile(self.lastname_file):
                print(f"File {self.lastname_file} not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()
    
            for lastname in lastnames_list.split("\n"):
                if lastname!="":
                    print(f"{self.firstname}.{lastname}")

        if self.firstname !=None and self.lastname != None:
            print(f"{self.firstname}.{self.lastname}")

        if self.firstname_file !=None and self.lastname != None:
            if not path.isfile(self.firstname_file):
                print(f"File {self.firstname_file} not found!")
                sys.exit()

            firstnames_list=""
            with open(self.firstname_file,"r") as firstnames:
                firstnames_list=firstnames.read()
    
            for firstname in firstnames_list.split("\n"):
                if firstname!="":
                    print(f"{firstname}.{self.lastname}")

        if self.firstname_file !=None and self.lastname_file != None:
            if not path.isfile(self.lastname_file):
                print(f"File {self.lastname_file} not found!")
                sys.exit()
            if not path.isfile(self.firstname_file):
                print(f"File {self.firstname_file} not found!")
                sys.exit()

            lastnames_list=""
            with open(self.lastname_file,"r") as lastnames:
                lastnames_list=lastnames.read()

            firstnames_list=""
            with open(self.firstname_file,"r") as firstnames:
                firstnames_list=firstnames.read()
    
            for firstname in firstnames_list.split("\n"):
                if firstname !="":
                    for lastname in lastnames_list.split("\n"):
                        if lastname!="":
                            print(f"{firstname}.{lastname}")


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-x','--format',help='set username format')
parser.add_argument('-L','--lastname-file',help='set lastname wordlist')
parser.add_argument('-l','--lastname',help='set specific lastname')
parser.add_argument('-F','--firstname-file',help='set firstname wordlist')
parser.add_argument('-f','--firstname',help='set specific firstname')
parser.add_argument('-c','--chars',default='abcdefghijklmnopqrstuvwxyz',help='set char list [a,b,c,d,etc]')

args = parser.parse_args()

list=users(args.lastname_file,args.firstname_file,args.chars,args.lastname,args.firstname)

if args.format=="1":
    #flastname
    list.format1()
if args.format=="2":
    #firstnamelastname
    list.format2()
if args.format=="3":
    #f.lastname
    list.format3()
if args.format=="4":
    #firstname.lastname
    list.format4()

