var = '1'
var2 = "halo"
print(f'{var}'*100) 

print (1+2)
print (1-2)
print (1/2)
print (1*2)
print (1**2)
print (12%2)

a = 6
b = "a"
print(a+len(b))

b = input('masukkan huruf: ')
if len(b) > 5:
    print(b)
    if len(b)%2==0:
        print(b*3)
    elif len(b)>=10:
        print(b*10)

for i in range(0,10):
    print("joshua hama ", i)

arr = ["apel","jeruk","kelapa","pisang"]
for i in arr:
    print("saya ", i)

arr = ["apel", 2, True, None, 9.90]
for i in arr:
    print("saya ", i)

# perulangan di dalam perulangan
for i in range(0,3):
    print('apel',i)
    for j in range(0,3):
        print('pisang',j)
        for k in range(0,3):
            print('mangga',k)

# break,continue
for i in range(0,10):
    print('hai', i)
    if i > 5:
        print('apel',i)
        break

for i in range(0,10):
    if i==5:
        continue
        print('apel',i)
        print('pisang')
    print('hai', i)

a = True
while a:
    print('a')
    a = False

def tambah(a, b):
    print(a+b)

for i in range(0,9):
    tambah(i, i+2)

def tambah(a, b):
    print('hai', b)

tambah("apel", "pisang")


def tambah(a, b):
    print('hai', a)
    print('hai', b)

tambah("apel", "pisang")

def tambah(a, b):
    print(a+b)

tambah(10, 90)

for i in range(0,5):
    print('*'*(i+1))

i = 0
while i < 5:
    print('*'*(i+1))
    i += 1

i = 6
while i > 0:
    print('*'*(i-1))
    i -= 1

n = 6
i = 1
while i < n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1

    print()
    i += 1