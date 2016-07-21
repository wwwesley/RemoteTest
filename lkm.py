import time 
i = 0
while True:
	time.sleep(2 + i)
	print(i)
	i = i + 1
	if i > 5:
		i = 0 
	