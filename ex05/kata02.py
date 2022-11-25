kata = (2019, 9, 25, 3, 30)

def fill_it(s,w):
	return(str(s).rjust(w,'0'))

print(fill_it(kata[1],2)+'/'+fill_it(kata[2],2)+'/'+fill_it(kata[0],4)+' '+fill_it(kata[3],2)+':'+fill_it(kata[4],2))
