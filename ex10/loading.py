from time import sleep
from time import time

rr = int(input("input a range: "))

listy = range(rr)


def ft_progress(listy):
	ch = '>'
	i = 1
	t = time()

	sp = 40
	s = 1
	for el in listy:
		if s == 1:
			s = 0
			if el > (len(listy)/sp) * i:
				ch = "="+ ch
				i+=1
			t2 = time()
			yield el
			loopTimeSum = (time() - t2)*len(listy)
			len_n = len(str(round(loopTimeSum,2)))
			print(len_n)
		else:
			print("ETA: "+str(round(max(loopTimeSum - (time() - t2),0.00),2)).ljust(len_n,' ')+"s ["+str(round(el*100/len(listy))).rjust(3,' ')+"%]["+ch.ljust(sp,' ')+"] "+str(el)+"/"+str(len(listy))+" | elapsed time "+str(round(time()-t,2)).ljust(4,' ')+"s",end="\r")
			while el >= (len(listy)/sp) * i:
				ch = "="+ ch
				i+=1
			yield el
		# sleep(0.1)
	print("ETA: "+str(round(max(loopTimeSum - (time() - t2),0.00),2)).ljust(len_n,' ')+"s [100%]["+ch.ljust(sp,' ')+"] "+str(el+ 1)+"/"+str(len(listy))+" | elapsed time "+str(round(time()-t,2)).ljust(4,' ')+"s")

# from time import time, sleep

# def ft_progress(listy) :
#     startTime = time()
#     currTime = 0
#     estX = 0.01
#     for i in listy :
#         lodingPercentage = int((i + 1) / len(listy) * 100)
#         lodingBar = ('='*int(lodingPercentage*20/100) + '>')
#         if abs(estX - ((time() - startTime) - currTime)) > 0.01:
#             estX = (time() - startTime) - currTime
#         est = (len(listy) - (i + 1)) * estX
#         currTime = time() - startTime
#         print(f'ETA: {est:.02f}s [ {lodingPercentage}%] [{lodingBar:21}] {i + 1}/{len(listy)} | elapsed time {currTime:.2f}s', end='\r')
#         yield i

ret = 0
for elem in ft_progress(listy):
	ret += elem
	sleep(0.005)
print()
print(ret)
