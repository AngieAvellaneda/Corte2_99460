import random as r 


for i in range(10):
    Aleatorio = r.randint(100,120)
    if Aleatorio == 110 or Aleatorio == 115 or Aleatorio == 119:
       continue
    elif Aleatorio%2 == 0:
        print(Aleatorio)
        for i in range(10):
            Aleatorio_im =r.randint(100,120)
            if Aleatorio_im == 110 or Aleatorio_im == 115 or Aleatorio_im == 119:
                pass
            elif Aleatorio_im%2 == 1:
                print(Aleatorio_im)
                break



  
