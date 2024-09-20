def total(bill,tip):
    total1=bill+(1+0.1*tip)
    total1=round(total1,2)
    print(f"Total bill is ${total1}")
    

total(100,20)