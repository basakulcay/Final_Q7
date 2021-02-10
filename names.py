#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:11:55 2021

@author: basakulcay
"""

def girl():
    girlfile=open('girls.txt','w')
    girlfile.write('Basak\n')
    girlfile.write('Ayse\n')
    girlfile.write('Fatma\n')
    girlfile.write('Gizem\n')
    girlfile.close()
girl()

def boy():
    boyfile=open('boys.txt','w')
    boyfile.write('Ahmet\n')
    boyfile.write('Furkan\n')
    boyfile.write('Mehmet\n')
    boyfile.write('Can\n')
    boyfile.close()
boy()

def main():
    girlName=input('Enter a girl name: ')    
    girlCheck=open('girls.txt','r')

    for girl in girlCheck:
        girlStrip=girl.rstrip('\n')
        
        if girlStrip==girlName:
            print('The name is among most popular girl names')
        else:
            print('The name is NOT among most popular girl names')
        break
        
    girlCheck.close()
    #boyCheck.close()
main()
