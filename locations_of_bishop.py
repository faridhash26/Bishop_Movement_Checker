
def append_list(nums):
    all=[]
    for x in nums:
        for y in nums :
            all.append((x,y))
    return all


def calculate_odd_even(number):
    odds = []
    evens=[]
    for num in range(1,number+1):
        if (num % 2) == 0:
            evens.append(num)
        else:
            odds.append(num)
    all_odds_chesss=append_list(odds)
    all_even_chesss=append_list(evens)
    joinedlist = all_even_chesss + all_odds_chesss
    joinedlist.sort()
    return joinedlist
    


