a = [1,2,3,4,5]
d = int(input("No of Rotation : ")) # No of rotation

def solve(a, d):
	i = d%len(a)
	print(a[i:]+a[:i])
solve(a,d)
