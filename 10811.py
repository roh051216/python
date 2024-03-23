N,M = map(int,input().split())

basket = [n for n in range(1,N+1)]

for i in range(M):
    i,j = map(int,input().split())
    q = basket[i-1:j]
    q.reverse()
    basket[i-1:j] = q

for i in range(N):
    print(basket[i],end=" ")
