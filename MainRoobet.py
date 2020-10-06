# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:42:38 2020

@author: bartm
"""
CL = 0
f = open('roobetNumbers.txt')

f.seek(CL)

line = f.readline()  # no 's' at the end of `readline()`

CL = f.tell()

print(f.readline()) 

#= float(x)


x = 1

bet1 = float(1)
bet2 = float(2)
bet3 = float(4)
bet4 = float(8)
bet5 = float(16)
bet6 = float(32)
bet7 = float(64)
bet8 = float(128)
bet9 = float(256)
bet10 = float(512)
bet11 = float(1024)
bet12 = float(2048)
#bet13 = float(.876)
#bet14 = float(.876)
#bet15 = float(.876)


bankroll = float(100)
previousBankroll = float(100)

lossNum = 0;
checker = float(2)



while (float(f.readline(CL)) > 0):
   if (lossNum == 0):
       if (float(f.readline(CL)) > checker):
           bankroll = bankroll + bet1
           CL = CL + 1
           print(lossNum)
           lossNum = 0
       else:
           bankroll = bankroll - bet1
           CL = CL + 1
           lossNum = lossNum + 1
           
           if (lossNum == 1):
               if (float(f.readline(CL)) > checker):
                   bankroll = bankroll + bet2
                   CL = CL + 1
                   print(lossNum)
                   lossNum = 0
               else:
                   bankroll = bankroll - bet2
                   CL = CL + 1
                   lossNum = lossNum + 1

                   if (lossNum == 2):
                        if (float(f.readline(CL)) > checker):
                            bankroll = bankroll + bet3
                            CL = CL + 1
                            print(lossNum)
                            lossNum = 0
                        else:
                            bankroll = bankroll - bet3
                            CL = CL + 1
                            lossNum = lossNum + 1
    
                            if (lossNum == 3):
                                if (float(f.readline(CL)) > checker):
                                    bankroll = bankroll + bet4
                                    CL = CL + 1
                                    print(lossNum)
                                    lossNum = 0
                                else:
                                    bankroll = bankroll - bet4
                                    CL = CL + 1
                                    lossNum = lossNum + 1
    
                                    if (lossNum == 4):
                                        if (float(f.readline(CL)) > checker):
                                            bankroll = bankroll + bet5
                                            CL = CL + 1
                                            print(lossNum)
                                            lossNum = 0
                                        else:
                                            bankroll = bankroll - bet5
                                            CL = CL + 1
                                            lossNum = lossNum + 1
                                            
                                            if (lossNum == 5):
                                                if (float(f.readline(CL)) > checker):
                                                    bankroll = bankroll + bet6
                                                    CL = CL + 1
                                                    print(lossNum)
                                                    lossNum = 0
                                                else:
                                                    bankroll = bankroll - bet6
                                                    CL = CL + 1
                                                    lossNum = lossNum + 1
                                                    
                                                    if (lossNum == 6):
                                                        if (float(f.readline(CL)) > checker):
                                                            bankroll = bankroll + bet7
                                                            CL = CL + 1
                                                            print(lossNum)
                                                            lossNum = 0
                                                        else:
                                                            bankroll = bankroll - bet7
                                                            CL = CL + 1
                                                            lossNum = lossNum + 1
                                                            
                                                            if (lossNum == 7):
                                                                if (float(f.readline(CL)) > checker):
                                                                    bankroll = bankroll + bet8
                                                                    CL = CL + 1
                                                                    print(lossNum)
                                                                    lossNum = 0
                                                                else:
                                                                    bankroll = bankroll - bet8
                                                                    CL = CL + 1
                                                                    lossNum = lossNum + 1
                                                            
                                                                  
                                                                    if (lossNum == 8):
                                                                        if (float(f.readline(CL)) > checker):
                                                                            bankroll = bankroll + bet9
                                                                            CL = CL + 1
                                                                            print(lossNum)
                                                                            lossNum = 0
                                                                        else:
                                                                            bankroll = bankroll - bet9
                                                                            CL = CL + 1
                                                                            lossNum = lossNum + 1
                                                                            
                                                                            if (lossNum == 9):
                                                                                if (float(f.readline(CL)) > checker):
                                                                                    bankroll = bankroll + bet10
                                                                                    CL = CL + 1
                                                                                    print(lossNum)
                                                                                    lossNum = 0
                                                                                else:
                                                                                    bankroll = bankroll - bet10
                                                                                    CL = CL + 1
                                                                                    lossNum = lossNum + 1
                                                                                    
                                                                                    if (lossNum == 10):
                                                                                        if (float(f.readline(CL)) > checker):
                                                                                            bankroll = bankroll + bet11
                                                                                            CL = CL + 1
                                                                                            print(lossNum)
                                                                                            lossNum = 0
                                                                                        else:
                                                                                            bankroll = bankroll - bet11
                                                                                            CL = CL + 1
                                                                                            lossNum = lossNum + 1
                                                                                            
                                                                                            if (lossNum == 11):
                                                                                                if (float(f.readline(CL)) > checker):
                                                                                                    bankroll = bankroll + bet12
                                                                                                    CL = CL + 1
                                                                                                    print(lossNum)
                                                                                                    lossNum = 0
                                                                                                else:
                                                                                                    bankroll = bankroll - bet12
                                                                                                    CL = CL + 1
                                                                                                    lossNum = lossNum + 1
                                                                    
                                                 
    
   else:
        lossNum = 0
    
print(bankroll)
f.close()