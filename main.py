import pyttsx3 #thu vien giong noi
import datetime # thoi gian
import speech_recognition as sr #  để nhận dạng giọng nói 
import webbrowser as wb # cho phép các ứng dụng Python mở và điều khiển các trình duyệt web
import os


main = pyttsx3.init()
voice = main.getProperty('voices') # lay giong noi
main.setProperty('voice' , voice[1].id) # voice[0].id = Giong Nam else 1 la giong NU 



def speak(audio):
	#giong noi
	print('Tro li ao cua thang: ' + audio)
	main.say(audio)
	main.runAndWait()

def time():
	# doc thoi gian hien tai
	thoi_gian = datetime.datetime.now().strftime("%I: %M: %p")
	speak(thoi_gian)

def welcome():
	#lay gio trong ngay
	hour = datetime.datetime.now().hour
	if hour >=6 and hour <= 12:
		speak('Good Moring Sir')
	elif hour >= 12 and hour <= 18:
		speak('Good Affernoon Sir')
	else:
		speak('Good Night')
	speak('how can i help you')


def command():
	c = sr.Recognizer() # doi tuong nhan giong noi
	with sr.Microphone() as source: # lay giong noi tu dau???
		c.pause_threshold=2 #dung 2 giay
		audio = c.listen(source) #nghe nguon
	try:
		query = c.recognize_google(audio, language='en')
		print("Thang Dinh :" + query)
	except sr.UnknownValueError: # neu khong nghe ddc
		print("Lam on loi lai ")
		#neu khong nghe ro , se in ra cau lenh de ban nhap vao
		query = str(input('Nhap vao cau noi cua ban: '))
	return query

if __name__ == '__main__':
	welcome()
	while True:
		query=command().lower() # lay menh lenh va chuyen thanh in thuong
		if "google" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://www.google.com/search?q={search}'
			wb.get().open(url) # mo web
			speak(f'here is your {search} in google')
		if "youtube" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://www.youtube.com/search?q={search}'
			wb.get().open(url)
			speak(f'here is your {search} in youtube')
		if "Github" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://github.com/search?q={search}'
			wb.get().open(url)
			speak(f'here is your {search} in github')
		if "Chat GPT" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://chat.openai.com/chat?q={search}'
			wb.get().open(url)
			speak(f'here is your {search} in chat gpt')
		if "Tik Tok" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://www.tiktok.com/vi-VN/?q={search}'
			wb.get().open(url)
			speak(f'here is your {search} in tik tok')
		if "Douyin" in query:
			speak('what should i search sir??')
			search = command().lower()
			url = f'https://www.douyin.com/?q={search}'
			wb.get().open(url)
			speak(f'here is your {search} in douyin')
		elif "open video":
			vid1=r"D:\Ảnh-\vid\New folder\xiao.mp4"
			os.startfile(vid1) # cau lenh chay file
		elif "time" in query:
			time()
		elif 'quit' in query:
			speak("tam biet")
			quit()