a = []
print("Enter the number (enter * to quit):")
while True:
  s = input()
  if s =='*':
    break
  else:
    a.append(int(s))
left = 0
right = len(a)-1
area = 0

while left<right:
  area = max(area,min(a[left],a[right])*(right-left))
  if a[left]<a[right]:
    left+=1
  else:
    right-=1

print(f"The largest area is {area}")
