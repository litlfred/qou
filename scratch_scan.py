import mpmath
import itertools
mpmath.mp.dps = 50

q = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')
c3 = mpmath.mpf('0.574282408456938210355325492317822986877864197992923769911929007421252062369680371490919245')
c21 = mpmath.mpf('0.507837426746464228913988647035446059902640201389006093845946328320494447333550882672314545')
c111 = mpmath.mpf('-0.0168135971275242277025816353272635952329381678125553655184651322421379193189033333671192534')

target = (3*q**2 + 4 + 3/q**2)/4
c_list = [c3, c21, c111]

dimq = [mpmath.mpf(1), q+1/q, mpmath.mpf(1)]
fq = [mpmath.mpf(1), q+1/q, mpmath.mpf(1)]
sign = [1, -1, -1]
sign_w0 = [1, -1, -1]
W_inv = [q**2+1+1/q**2, (q**2+1+1/q**2)/(q+1/q)**2, q**2+1+1/q**2]
dq = [mpmath.mpf(1), (q+1/q)**2 - 1, mpmath.mpf(1)]

def try_all():
    # iterate over combinations of integer powers
    for p_dimq in range(-3, 4):
        for p_W in range(-3, 4):
            for sig in [1, -1]:
                delta = [
                    (sign_w0[i] if sig==-1 else 1) * 
                    (dimq[i]**p_dimq) * 
                    (W_inv[i]**p_W) 
                    for i in range(3)
                ]
                val = sum(c_list[i]*delta[i] for i in range(3))
                if abs(val - target) < 1e-10:
                    print(f"MATCH: p_dimq={p_dimq}, p_W={p_W}, sig={sig}")
                if abs(val + target) < 1e-10:
                    print(f"MATCH (neg): p_dimq={p_dimq}, p_W={p_W}, sig={sig}")

try_all()
print("Scan done.")
