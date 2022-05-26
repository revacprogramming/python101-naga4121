hrs=float(input("input hours"))
rate=float("enter hours")
if hrs<=40:
  pay=hrs*rate
  print(pay)
else:
  ovrhrs=(hrs-40)
  regular=rate*40
  othrs=ovrhrs*(rate*1.5)
  overpay=(regular+othrs)
     print(ovrpay)