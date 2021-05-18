import random
import numpy

a0 = random.randint(1,20)
a1 = random.randint(1,20)
a2 = random.randint(1,20)
a3 = random.randint(1,20)
x1 = []
x2 = []
x3= []
y = []
xn1 = []
xn2 = []
xn3 = []
var315 = []

for i in range(8):
    x1.append(random.randint(1, 20))
    x2.append(random.randint(1, 20))
    x3.append(random.randint(1, 20))

for i in range(8):
    y.append(a0+a1*x1[i]+a2*x2[i]+a3*x3[i])

x01= (max(x1)+min(x1))/2
x02= (max(x2)+min(x2))/2
x03= (max(x3)+min(x3))/2
dx1 = x01 - min(x1)
dx2 = x02 - min(x2)
dx3 = x03 - min(x3)

for i in range(8):
    xn1.append((x1[i]-x01)/dx1)
    xn2.append((x2[i] - x02) / dx2)
    xn3.append((x3[i] - x03) / dx3)

for i in y:
    if i < numpy.mean(y):
        var315.append(i)


ind = y.index(max(var315))

mean = sum(y)/len(y)

print("a0=%s a1=%s a2=%s a3=%s"%(a0, a1, a2, a3))
print("X1: %s"%x1)
print("X2: %s"%x2)
print("X3: %s"%x3)
print("Y: %s"%y)
print("x0: %s %s %s"%(x01, x02, x03))
print("dx: %s %s %s"%(dx1, dx2, dx3))
print("Xн1: %s"%xn1)
print("Xн2: %s"%xn2)
print("Xн3: %s"%xn3)
print("mean y: %s"%mean)
print("→ Y ,де Y - середнє Y: x1 = %s, x2 = %s, x3 = %s"%(x1[ind],x2[ind],x3[ind]))
