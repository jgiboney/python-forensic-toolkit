#!/usr/bin/python

#This script is meant to be a cross-OS python script that catalogs interesting
#common files and then puts them into one location for analysis.  

import platform
import os, glob, time, stat


#Triage OS. Search "osType" for a string that is unique to that OS to be able
#do specific OS commands and file paths.
def useOSType(osType):
	print '-'*60

	if "debian-9" in osType:
		print "Debian 9 Detected"
		searchDebian9()


#prints filename and date last modified
def linuxPrintFileListing(root):
	print '-'*60
	date_file_list = []
	for folder in glob.glob(root):
	    print "folder =", folder
	    for file in glob.glob(folder + '/*.*'):
	        stats = os.stat(file)
	        perms = oct(stat.S_IMODE(stats[0]))
	        lastmod_date = time.localtime(stats[8])
	        date_file_tuple = lastmod_date, file, perms
	        date_file_list.append(date_file_tuple)
	date_file_list.sort()
	date_file_list.reverse()
	print "%-40s %-17s %s" % ("Filename:", "Last Modified:", "Perms:")
	for file in date_file_list:
	    folder, file_name = os.path.split(file[1])
	    file_date = time.strftime("%m/%d/%y %H:%M:%S", file[0])
	    file_perm = file[2]
	    print "%-40s %s %s" % (file_name, file_date, file_perm)


def searchDebian9():
	locations = ['/var/log/', '/home/']
	for location in locations:
		linuxPrintFileListing(location)


#Get OS string to search by specific OS distros
osType = platform.platform()
useOSType(osType)