def buy_and_sell(arr):
    l,r=0,1
    max_profit=0
    while r<len(arr):
        if arr[l]<arr[r]:
            profit=arr[r]-arr[l]
            max_profit=max(max_profit,profit)
        else:
            l+=1
        r+=1
    return max_profit


arr=[7,1,5,3,6,4]

print(buy_and_sell(arr))