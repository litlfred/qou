"""Pre-registered 7d4bfaa6d9d. Part C: joint (T3, Q) spectrum and reading B (B = 3t, imported
Gell-Mann--Nishijima). Part M: operator charge Q^2*hol on the section-35 muon map. mpmath 60 dps."""
import json, itertools, mpmath as mp
from qou_substrate import constants as C
mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
vol = 2*mp.clsin(2, mp.pi/3)
basis = list(itertools.product([0, 1], repeat=3))
def kron(A, B):
    M = mp.zeros(A.rows*B.rows, A.cols*B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l in range(B.cols): M[i*B.rows+k, j*B.cols+l] = A[i, j]*B[k, l]
    return M
def sub(M, idx): return mp.matrix([[M[i, j] for j in idx] for i in idx])
def tr(M): return sum(M[i, i] for i in range(M.rows))
blocks = {w: [i for i, b in enumerate(basis) if b.count(0) == w] for w in range(4)}
def setup(q):
    R = mp.matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]]); I2 = mp.eye(2); I8 = mp.eye(8)
    h = q - 1/q; s0 = kron(R, I2); s1 = kron(I2, R); V = s0*(s1 - h*I8); hol = V**3
    T3 = mp.diag([mp.mpf(b.count(0) - b.count(1))/2 for b in basis])
    D = (hol - I8)/q + (1 - 1/q)*T3
    Xe = s0*s1*s0; De = (Xe - q**3*I8)/q + (1 - 1/q)*T3
    K3 = mp.diag([q**(b.count(0) - b.count(1)) for b in basis])
    return dict(V=V, hol=hol, T3=T3, D=D, De=De, K3=K3, I8=I8)
def Qblock(V, idx):
    Vb = sub(V, idx)
    if Vb.rows == 1: return mp.matrix([[mp.log(Vb[0, 0])/(2j*mp.pi)]])
    return mp.logm(Vb)/(2j*mp.pi)
def tphase(q):
    s = setup(q); ev = mp.eig(sub(s["V"], blocks[2]), left=False, right=False)
    return max(mp.re(mp.arg(e)/(2*mp.pi)) for e in ev)
out = {"preregistration": "7d4bfaa6d9d"}
# ---- C1: joint spectrum ----
def joint(q):
    s = setup(q); pairs = []
    for w, idx in blocks.items():
        Vb = sub(s["V"], idx)
        ev = [Vb[0, 0]] if Vb.rows == 1 else mp.eig(Vb, left=False, right=False)
        for e in ev:
            pairs.append([mp.nstr(mp.mpf(2*w - 3)/2, 5), mp.nstr(mp.re(mp.log(e)/(2j*mp.pi)), 15),
                          mp.nstr(abs(e) - 1, 3)])
    return sorted(pairs)
out["C1_joint_(T3,Q,|ev|-1)"] = {"q0": joint(q0), "q=1+1e-25": joint(1 + mp.mpf('1e-25'))}
# ---- C2: reading B ----
def readingB(q):
    t = tphase(q); qu = (1 + t)/2; qd = (t - 1)/2
    s = setup(q); ch = {0: qu, 1: qd}
    QP = mp.diag([sum(ch[b[i]]*ch[b[j]] for i in range(3) for j in range(i+1, 3)) for b in basis])
    S = QP*s["hol"]; DD = s["D"]*s["D"]; X = DD - S
    Te = tr(s["De"]*s["De"]); TeK = tr(s["K3"]*s["De"]*s["De"])
    rP = (tr(sub(X, blocks[1])) - tr(sub(X, blocks[2])))/Te
    rK = (tr(sub(s["K3"]*X, blocks[1])) - tr(sub(s["K3"]*X, blocks[2])))/TeK
    two = q + 1/q; F = two*(q**2 + 1 + q**-2)/q**3; mmu = me*vol/(1 - 1/q)**2
    dtau = (tr(sub(s["K3"]*X, blocks[1])) - tr(sub(s["K3"]*X, blocks[2])))/two**3
    return {"t": mp.nstr(t, 20), "q_u": mp.nstr(qu, 15), "q_d": mp.nstr(qd, 15),
            "Q_p": mp.nstr(2*qu + qd, 15), "Q_n": mp.nstr(qu + 2*qd, 15),
            "Epot_plain_E/me": mp.nstr(mp.re(rP), 15), "Epot_plain_keV": mp.nstr(mp.re(1000*me*rP), 12),
            "Epot_K_E/me": mp.nstr(mp.re(rK), 15), "Epot_K_keV": mp.nstr(mp.re(1000*me*rK), 12),
            "M2_readingB_MeV": mp.nstr(mp.re(2*mmu*F*dtau), 12)}
out["C2_readingB"] = {"q0": readingB(q0)}
for k in (2, 4, 8):
    out["C2_readingB"][f"q=1+1e-{k}"] = readingB(1 + mp.mpf(10)**-k)
# ---- M3: operator charge on the muon map ----
def M3(q):
    s = setup(q); two = q + 1/q; F = two*(q**2 + 1 + q**-2)/q**3; mmu = me*vol/(1 - 1/q)**2
    res = {}
    for arm in ("D2", "Qop2hol", "D2_minus_Qop2hol"):
        tw = {}
        for w in (1, 2):
            idx = blocks[w]; Qb = Qblock(s["V"], idx); holb = sub(s["hol"], idx)
            Db = sub(s["D"], idx); Kb = sub(s["K3"], idx)
            X = {"D2": Db*Db, "Qop2hol": Qb*Qb*holb, "D2_minus_Qop2hol": Db*Db - Qb*Qb*holb}[arm]
            tw[w] = tr(Kb*X)
        dtau = (tw[1] - tw[2])/two**3
        res[arm + "_MeV"] = mp.nstr(mp.re(2*mmu*F*dtau), 12)
        res[arm + "_times_h"] = mp.nstr(mp.re(2*mmu*F*dtau)*(q - 1/q), 12)
        res[arm + "_imag"] = mp.nstr(mp.im(2*mmu*F*dtau), 3)
    return res
out["M3"] = {"q0": M3(q0)}
for k in (2, 3, 4, 6, 8):
    out["M3"][f"q=1+1e-{k}"] = M3(1 + mp.mpf(10)**-k)
out["comparison_after"] = {"CODATA_mn_minus_mp_MeV": "1.29333",
    "lattice_split_BMW2015_MeV": {"quark_mass": "+2.52", "QED": "-1.00"}}
s_ = json.dumps(out, indent=1); print(s_)
open(__file__.replace('.py', '.out.json'), 'w').write(s_ + "\n")
