import math as m

if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_m = 1 / k_st  # Manning's n
    S_0 = 0.005     # channel slope



def interpolate_h(Q, b, m_bank , S, **kwargs):
    h = 100
    eps = 1

for k in kwargs.items():
    if k_st in k[0]:
        m_bank = 1/k[1]
    else
        print ("not defined")
    while eps > 10**-3
        A = h * (b + m_bank)
        P = b + 2 * h * (((m_bank * 2) + 1) ** 1 / 2)
        Qk = A ** (5 / 3) * sqrt(S) / (n_m * P ** (2 / 3))
        eps = abs(Q - Qk) / Q
        dA_dh = b + 2 * m * h
        dP_dh = 2 * m.sqrt(m ** 2 + 1)
        F = n_m * Q * P ** (2 / 3) - A ** (5 / 3) * m.sqrt(S)
        dF_dh = 2 / 3 * n_m * Q * P ** (-1 / 3) * dP_dh - 5 / 3 * A ** (2 / 3) * m.sqrt(S) * dA_dh
        h = abs(h - F / dF_dh)
return (Qk)



