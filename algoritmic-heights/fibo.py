prev = 0
curr = 1
fn = 0

n = int(input().strip())

if n == 1:
    print(curr)
else:
    for i in range(n-1):
        fn = prev + curr
        prev = curr
        curr = fn
    print(fn)