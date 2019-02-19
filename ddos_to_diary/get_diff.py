# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
import uuid
import time

# Прокси и нужность его использования
proxies = { 'https' : 'https://mitrofanov:red21RED@proxy3.keysystems.local:3128' } 
use_proxy = True

# Urls
base_url = 'https://bestdiary.ru/api/v2/'
get_notes_diff_url = base_url + 'get_notes_diff'
note_url = base_url + 'note'

# Создание сессии
s = requests.Session()

# Авторизация и прописывание прокси
s.headers.update({
	'Authorization': 'Bearer mitrofanov_test_user',
	'Content-type': 'application/json'
})
if use_proxy:
	s.trust_env = False
	s.proxies.update(proxies)


def create_notes(count=100):
	start_time = time.time()

	for i in range(1, count + 1):
		data = json.dumps({
			'uid': str(uuid.uuid4()),
			'mood': 1,
			'text': 'this is ddos',
			'title': 'title of ddos',
			'date': 123456,
			'in_trash': False,
			'media': {}
		})
		r = s.post(note_url, data=data)
		from_start = time.time() - start_time
		print("{}. t: {}  {}".format(i, from_start, r.text))
		if r.status_code != 200:
			print("Error occured in create_notes")
			return 400
	return 200


def get_all_notes():
	r = s.post(get_notes_diff_url)
	if r.status_code == 200:
		print(r.json())
		print(r.text)


def main():
	code = create_notes(100)
	# if code == 200:
	# 	get_all_notes()


if __name__ == '__main__':
	main()