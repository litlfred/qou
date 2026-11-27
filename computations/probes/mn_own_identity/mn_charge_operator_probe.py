"""Charge operator Q = log(V)/2pi i, and two nucleons on H6. Pre-registered 47a826e424d.
Part A: mpmath 40 dps (eigen/log), plus exact sympy for spectra. Part B: exact Fractions."""
import json, itertools, mpmath as mp, sympy as sp
from fractions import Fraction as Fr
from qou_substrate import constants as C
mp.mp.dps = 40
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
out = {"preregistration": "47a826e424d"}
# ---------- Part A (C2^3) ----------
def Rcm(q):
    return mp.matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
def kron(A, B):
    M = mp.zeros(A.rows*B.rows, A.cols*B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l in range(B.cols): M[i*B.rows+k, j*B.cols+l] = A[i, j]*B[k, l]
    return M
basis3 = list(itertools.product([0,1], repeat=3))
def partA(q):
    R = Rcm(q); I2 = mp.eye(2); I8 = mp.eye(8); h = q - 1/q
    s0 = kron(R, I2); s1 = kron(I2, R); s1i = s1 - h*I8
    V = s0*s1i; hol = V**3
    T3 = mp.diag([mp.mpf(b.count(0) - b.count(1))/2 for b in basis3])
    D = (hol - I8)/q + (1 - 1/q)*T3
    Xe = s0*s1*s0; De = (Xe - q**3*I8)/q + (1 - 1/q)*T3
    K3 = mp.diag([q**(b.count(0) - b.count(1)) for b in basis3])
    res = {}
    blocks = {"p": [i for i,b in enumerate(basis3) if b.count(0) == 2],
              "n": [i for i,b in enumerate(basis3) if b.count(0) == 1]}
    T = {}
    for nm, idx in blocks.items():
        Vb = mp.matrix([[V[i, j] for j in idx] for i in idx])
        ev = mp.eig(Vb, left=False, right=False)
        Q = mp.logm(Vb)/(2j*mp.pi)
        holb = mp.matrix([[hol[i, j] for j in idx] for i in idx])
        Db = mp.matrix([[D[i, j] for j in idx] for i in idx])
        Kb = mp.matrix([[K3[i, j] for j in idx] for i in idx])
        X = Db*Db - Q*Q*holb
        T[nm] = (sum(X[i, i] for i in range(3)), sum((Kb*X)[i, i] for i in range(3)))
        res[nm] = {"V_eigen_phase/2pi": sorted(mp.nstr(mp.re(mp.arg(e)/(2*mp.pi)), 15) for e in ev),
                   "|eigen|": [mp.nstr(abs(e), 12) for e in ev],
                   "trQ": mp.nstr(mp.re(sum(Q[i, i] for i in range(3))), 15),
                   "trQ2": mp.nstr(mp.re(sum((Q*Q)[i, i] for i in range(3))), 15)}
    Te = sum((De*De)[i, i] for i in range(8)); TeK = sum((K3*De*De)[i, i] for i in range(8))
    rP = (T["n"][0] - T["p"][0])/Te; rK = (T["n"][1] - T["p"][1])/TeK
    res["Epot_P_plain_E_over_me"] = mp.nstr(mp.re(rP), 15); res["Epot_P_keV"] = mp.nstr(mp.re(1000*me*rP), 12)
    res["Epot_K_E_over_me"] = mp.nstr(mp.re(rK), 15); res["Epot_K_keV"] = mp.nstr(mp.re(1000*me*rK), 12)
    res["imag_parts_max"] = mp.nstr(max(abs(mp.im(rP)), abs(mp.im(rK))), 5)
    return res
out["A_q0"] = partA(q0)
out["A_q~1"] = partA(1 + mp.mpf('1e-20'))
print(json.dumps({k: out[k] for k in ("A_q0", "A_q~1")}, indent=1), flush=True)
# ---------- Part B (C2^6), exact ----------
def matmul(A, B):
    n = len(A); Bt = list(zip(*B))
    return [[sum(a*b for a, b in zip(row, col) if a and b) for col in Bt] for row in A]
def eye(n): return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
def gen(i, q, inv=False, N=6):
    h = q - 1/q; n = 2**N; M = [[Fr(0)]*n for _ in range(n)]
    for s in range(n):
        bits = [(s >> (N-1-k)) & 1 for k in range(N)]
        a, b = bits[i], bits[i+1]
        def put(x, y, c):
            t = bits[:]; t[i], t[i+1] = x, y
            r = int("".join(map(str, t)), 2); M[r][s] += c
        # Rc on (a,b), column action: |00>->q|00>, |01>->|10>, |10>->|01>+h|10>, |11>->q|11>
        if a == b: put(a, b, q)
        elif (a, b) == (0, 1): put(1, 0, Fr(1))
        else: put(0, 1, Fr(1)); put(1, 0, h)
    return M
def partB(q):
    N = 6; n = 64
    # check Hecke on one generator: s*s - h s - 1 = 0, and s^-1 = s - h
    s = gen(0, q); h = q - 1/q
    word = []
    for i in (0, 3): word += [(i, False), (i+1, True)]*3
    word += [(2, False), (3, True)]*3
    hol = eye(n)
    for i, inv in word:
        G = gen(i, q)
        if inv: G = [[G[r][c] - (h if r == c else 0) for c in range(n)] for r in range(n)]
        hol = matmul(hol, G)
    T3 = [Fr(bin(s_).count("1")*-1 + (N - bin(s_).count("1")), 2) for s_ in range(n)]
    D = [[(hol[r][c] - (1 if r == c else 0))/q + ((1 - 1/q)*T3[r] if r == c else 0) for c in range(n)] for r in range(n)]
    D2 = matmul(D, D)
    nu = lambda s_: N - bin(s_).count("1")  # number of u (= 0 bits)
    res = {}
    for k, M in ((1, D), (2, D2)):
        tr = {w: sum(M[s_][s_] for s_ in range(n) if nu(s_) == w) for w in range(7)}
        res[k] = {f"w{w}-w{6-w}": tr[w] - tr[6-w] for w in (4, 5, 6)}
    return res
B = {}
for lab, qq in (("q=1", Fr(1)), ("q=1+1e-3", Fr(1001, 1000)), ("q=1+1e-4", Fr(10001, 10000))):
    B[lab] = partB(qq); print(lab, {k: {kk: float(vv) if False else str(vv)[:30] for kk, vv in v.items()} for k, v in B[lab].items()}, flush=True)
# leading order in h from the two small-h points
lead = {}
for k in (1, 2):
    for key in B["q=1"][k]:
        a, b = B["q=1+1e-3"][k][key], B["q=1+1e-4"][k][key]
        if a == 0 or b == 0: lead[f"k{k}:{key}"] = "zero"
        else:
            r = mp.mpf(a.numerator)/a.denominator / (mp.mpf(b.numerator)/b.denominator)
            lead[f"k{k}:{key}"] = mp.nstr(mp.log10(abs(r)), 6)
out["B"] = {lab: {str(k): {kk: str(vv) for kk, vv in v.items()} for k, v in B[lab].items()} for lab in B}
out["B_leading_h_order_estimate"] = lead
print(json.dumps(lead, indent=1))
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1)
