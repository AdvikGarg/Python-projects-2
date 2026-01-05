total_bill=float(input('Enter the total bill: $'))
amount=float(input('Enter the Amount paid: $'))
Change=total_bill-amount
tip=amount-total_bill
if Change>=0:
    print(f'Change given by shopkeeper is: ${Change}')
else:
    print(f'Tip given by customer is: ${tip}')    
