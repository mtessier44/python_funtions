s='hello'
v=["a","e","i","o","u","A","E","I","O","U"]
print("".join([f"{i}p{i}" if i in v else i for i in s]))
print("".join([i+'p'+i if i in v else i for i in s]))

n = str(123)
x=0
l=n[0]
for c in n:x+=l!=c;l=c;
print(x)
