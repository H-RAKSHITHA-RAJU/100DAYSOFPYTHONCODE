print( 'welcome to to tip calculator!')

bill=float(input('what was the total bill? $'))

n=int(input('how much tip would you like to give? 10, 12, or 15? '))

ppl=int(input('how many people to split the bill ? '))

tip=bill+(n*bill/100)

pay=tip/ppl

print(f'each person should pay: ${round(pay,2)}')
