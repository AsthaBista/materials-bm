# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:17:27 2022

@author: aasmu
"""

# def calc_discharge(b, h, m, S,**kwargs):
    
#     for k in kwargs.items():
#             if "k" in k[0]:
#                 coefficient = float(k[1])
#             if "D90" in k[0]:
#                 coefficient = float(k[1])
#             if "n_m" in k[0]:
#                 coefficient = 26/(float(k[1])**(1/6))
                       
#     A = h*(b+h*m)
#     P = b+2*h*(m**2+1)**(1/2)
#     Q = coefficient *(S**(1/2))*((A/P)**(2/3))*A
#     return Q

# print(calc_discharge(2,1,0.2,0.01),k_st =0.2)

def interpolate_h(Q,b,m,S,**nm):
    import math
    
    for n in nm.items():
                 if "n" in n[0]:
                     n_m = float(n[1])
    h = 1.0
    eps = 1.0
    while eps > 10**-3:
       A = h*(b+h*m)
       P = b+2*h*(m**2+1)**(1/2)
       Qk = A ** (5/3) * math.sqrt(S) / (n_m * P ** (2 / 3))
       eps = abs(Q - Qk) / Q
       dA_dh = b + 2 * m * h
       dP_dh = 2 * math.sqrt(m ** 2 + 1)
       F = n_m * Q * P ** (2 / 3) - A ** (5 / 3) * math.sqrt(S)
       dF_dh = 2/3 * n_m * Q * P ** (-1 / 3) * dP_dh - 5 / 3 * A ** (2 / 3) * math.sqrt(S) * dA_dh
       h = abs(h - F / dF_dh)
    return h,eps

print(interpolate_h(2, 1, 0.5, 0.01,nm=0.01))