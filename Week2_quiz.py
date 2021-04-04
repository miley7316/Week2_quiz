#Quiz) 사이트별로 비밀번호를 만들어 준느 프로그램

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0} 의 비밀번호는 {1}입니다.".format(url, password))
