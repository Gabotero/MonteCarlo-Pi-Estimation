import matplotlib.pyplot as plot
import random

def main():
	
	circ = plot.Circle((0,0),radius=0.5, edgecolor="red", fill=False)

	plot.gca().add_patch(circ)
	plot.axis('scaled')

	plot.ion()
	plot.show()
	
	count = 0
	r= 0.5
	dentro = 0	

	while(count < 1000):
		
		x = random.random()- 0.5
		y = random.random()- 0.5
		
		if(dentro_del_circulo(x,y,r)): 	
			plot.scatter(x, y, color='red')
			dentro+=1
		else:
			 plot.scatter(x, y, color='blue')
		
		count += 1
		
		plot.title(r'Estimacion de $\pi$ : %f' % (4*float(dentro)/float(count)) )
 		plot.draw()

def dentro_del_circulo(x,y,r):

	return (x**2 + y**2 <= r**2)


if __name__ == '__main__': 
	main()
