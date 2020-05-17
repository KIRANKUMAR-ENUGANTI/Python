'''n = int(input())
arr = map(int, input().split())
arr=sorted(set(arr),reverse=True)
if n!=1:
    print(arr[1])
else:
    print(arr[0])
'''
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(n):
        if i==n-1:
            print(arr[0])
            break
        elif arr[i] == arr[i + 1]: continue
        print(arr[i+1])
        break