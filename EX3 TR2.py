k=5
for i in range(k*2-1):
    if i<=k-1:
        print('*'*(i+1))
    else:
        print('*'*(k-(i-k+1)))