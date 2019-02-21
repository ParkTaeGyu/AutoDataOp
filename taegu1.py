
#	작성자: 박태규
#	작성일: 2018-06-17
#	프로그램 개요: TTA 성능시험 데이터 변환 프로그램

import io
import re
import sys

# 파일입력
def read_txt(file):
	with io.open(file,mode='r',encoding='utf-8') as f:
		data=f.readlines()
	f.close()
	return data

def write_txt(file,lines):
	with open(file,'w') as f:
		f.writelines(lines)
	f.close()

def mode_1(line):
	result=re.sub(r"(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})",r"\7\8\9\10\11\12\25\26\27\28",line)
	temp = result.split()
	final_mem = int(total_mb - (int(temp[0])+int(temp[1])+int(temp[2]))/1024)
	final_cpu = int(temp[3])+int(temp[4]);
	line = str(final_cpu) + " " + str(final_mem) +'\n'
	return line
	
def mode_2(line):
	result=re.sub(r"(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})(\s{0,20})(\d{1,20})",r"\7\8\9\10\11\12\25\26\27\28",line)
	temp = result.split()
	final_mem = int(total_mb - (int(temp[0])+int(temp[1])+int(temp[2]))/1024)
	final_cpu = int(temp[3])+int(temp[4]);
	line = str(final_cpu) + "," + str(final_mem) +'\n'
	return line

if __name__ =='__main__':
	if len(sys.argv) == 1 :
		print("사용법 :  python taegu.py <필수:RawData.파일형식> <필수:메모리(GB)> <선택:실행옵션>")
		print("ex) python taegu.py rawData.txt 16 2")
		sys.exit(0)
	print("")
#	print("<실행 옵션>")
#	print("1.메모리랑 CPU만 계산하기")
#	print("2.procs, r,b등 필요없는 줄 날리기")
#	print("3.잘못된 데이터들만 정렬하기")
#	print("")
	print("사용법 : python taegu.py <필수:RawData.파일형식> <필수:메모리(GB)>")
	print("ex) python taegu.py rawData.txt 16 2")
	print("")
	
	file = sys.argv[1]
	total_gb= sys.argv[2]
	total_mb= int(total_gb)*1024
	content=read_txt(file)
	results=[]
	print("<결과 파일 형식 선택>")
	txtorcsv = input("1.엑셀파일 2.텍스트파일\n")
	print(txtorcsv)
	if txtorcsv == "1":
		results.append("%usr+%sys,usedmem\n")
	elif txtorcsv == "2":
		results.append("%usr+%sys usedmem\n")
		
	for line in content:
			if re.match('\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}\s{0,20}\d{1,20}',line):
				if txtorcsv == "2":
					ret = mode_1(line)
					results.append(ret)
				elif txtorcsv == "1":
					ret = mode_2(line)
					results.append(ret)
			else: 
				continue
		
#		elif re.match('[a-z]'	,line) or re.match('\s[a-z]',line) or re.match('\n',line):
#			continue
#		if ret != "":
#			results.append(ret)
	
	if txtorcsv =="2":
		write_txt("result.txt",results)	
	elif txtorcsv =="1":
		write_txt("result.csv",results)
	

