

```python
def fibo_recursive(n):
    if n<2:
        return n
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
```


```python
def minimumCoinChange(changeAmount, coins=[1,5,10,25,50]):
    foundCoins=[]
    while(changeAmount > 0):
        try:
            for i in range(len(coins)-1,-1,-1):
                if(changeAmount >= coins[i]):
                    foundCoins.append(coins[i])
                    changeAmount = changeAmount - coins[i]
                    break
        except:
            print("hata")
    return foundCoins

print(minimumCoinChange(293))
```

    [50, 50, 50, 50, 50, 25, 10, 5, 1, 1, 1]
    


```python
def recMC(coinValueList, change):
    minCoins = change
    if(change in coinValueList):
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if(numCoins < minCoins):
                minCoins = numCoins
    return minCoins

recMC([1,5,10,25,50], 63)
```




    5




```python
def rec_fb(n, result): #recursive fibonacci kodunun karmaşıklığının daha sade hali
    if n<2:
        return n
    elif(result[n] != 0):
        return result[n]
    else:
        result[n] = rec_fb(n-1, result) + rec_fb(n-2, result)
        return result[n]
    
for i in range(13,25):
    print(rec_fb(i,[0]*(i+1)), end=" ")
```

    233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 


```python
#Fibonacide uyguladığımız aynı mantığı uygulayalım
def recMC2(coinValueList,change,knownResults): #minimum madeni parayla para üstü çevirme kodunun recursive hali
    minCoins=change
    if(change in coinValueList): #bozuk para listesinde var ise 1
        knownResults[change]=1
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC2(coinValueList,change-i,knownResults)
            if(numCoins<minCoins):
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins

for i in range(8,20):
    print(i," ",recMC2([1,5,10,25,50],i,[0]*(i+1)))
```

    8   4
    9   5
    10   1
    11   2
    12   3
    13   4
    14   5
    15   2
    16   3
    17   4
    18   5
    19   6
    


```python

```