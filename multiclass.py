
from matplotlib.pyplot import *
from numpy import *
import time

#weight vector
w1 = [20, 20]
w2 = [50,70]
w3 = [70,30]
#print training_data

f = open('multiclassdatatest.csv','w')


start = time.clock();
for i in range(0,101,5) :
    for j in range(0,101,5) :
        x = []
        x.append(i)
        x.append(j)
        #print x
        result1 = sqrt((w1[0]-i)**2 + (w1[1]-j)**2)
        result2 = sqrt((w2[0]-i)**2 + (w2[1]-j)**2)
        result3 = sqrt((w3[0]-i)**2 + (w3[1]-j)**2)
        #print result1,result2,result3
        if(result1 < result2) :
            if(result1 < result3) :
                s = i,j,1
                f.write(str(s)+"\n")
                plot(i,j,'bo')
            else:
                s = i,j,3
                f.write(str(s)+"\n")
                plot(i,j,'ro')
        else :
            if(result2 < result3) :
                s = i,j,2
                f.write(str(s)+"\n")
                plot(i,j,'go')
            else:
                s = i,j,3
                f.write(str(s)+"\n")
                plot(i,j,'ro')

plot(w1[0],w1[1],'wo')
plot(w2[0],w2[1],'wo')
plot(w3[0],w3[1],'wo')
print  time.clock() - start

f.close()
show()



