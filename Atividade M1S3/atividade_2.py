insira = int(input('Insira um número'))
def Recur(n):
  if n == 0:
    print(n)
    return
  print(n)
  Recur(n-1) 

Recur (insira)