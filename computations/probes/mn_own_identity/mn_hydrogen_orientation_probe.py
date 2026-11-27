"""Pre-registered: PREREGISTRATION-hydrogen-orientation.md (completed 2026-11-22T09:22:39Z).
Does hydrogen neutrality Q_p + Q_e = 0, with ONE charge functional applied to the nucleon word
N = V^3 (V = s0 s1^-1) and the ruled electron e = s0 s1 s0, fix which weight block is the proton?
Exact sympy over Q(q) for symmetry checks, spectra and traces; mpmath 60 dps for log/arg.
No float64 arithmetic. q0 = Q_50_DIGIT_STR (proton pin)."""
import json, itertools
import sympy as sp
import mpmath as mp
from qou_substrate import constants as C

mp.mp.dps = 60
q = sp.symbols('q', positive=True)
q0s = C.Q_50_DIGIT_STR
basis = list(itertools.product([0, 1], repeat=3))
idx = {b: i for i, b in enumerate(basis)}
I2, I8 = sp.eye(2), sp.eye(8)
h = q - 1/q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
kp = sp.kronecker_product
s0, s1 = kp(R, I2), kp(I2, R)
s0i, s1i = s0 - h*I8, s1 - h*I8          # Hecke: s^-1 = s - h
def S(M): return sp.simplify(M)
assert S(s0*s0i - I8) == sp.zeros(8) and S(s1*s1i - I8) == sp.zeros(8)
assert S(s0*s1*s0 - s1*s0*s1) == sp.zeros(8)
V = s0*s1i; Vi = s1*s0i; N = V**3; Ni = Vi**3
e = s0*s1*s0; tref = s0**3
X = sp.zeros(8); P = sp.zeros(8)
for b in basis:
    X[idx[tuple(1-x for x in b)], idx[b]] = 1
    P[idx[b[::-1]], idx[b]] = 1
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
K = sp.diag(*[q**(b.count(0) - b.count(1)) for b in basis])
blocks = {w: [idx[b] for b in basis if b.count(0) == w] for w in range(4)}
def sub(M, ix): return M.extract(ix, ix)
out = {"preregistration": "PREREGISTRATION-hydrogen-orientation.md (2026-11-22T09:22:39Z)",
       "convention": "bit 0 = u under O+; W2 = two 0-bits; K = q^(2T3)"}

# ---- symmetry checks (P-sym) ----
sym = {"XVX == P V^-1 P": S(X*V*X - P*Vi*P) == sp.zeros(8),
       "X N X == P N^-1 P": S(X*N*X - P*Ni*P) == sp.zeros(8),
       "X e X == P e P": S(X*e*X - P*e*P) == sp.zeros(8),
       "X T3 X == -T3": X*T3*X == -T3, "X K X == K^-1": S(X*K*X - K.inv()) == sp.zeros(8),
       "P preserves blocks": P*T3*P == T3,
       "[e,T3]=0": S(e*T3 - T3*e) == sp.zeros(8), "[N,T3]=0": S(N*T3 - T3*N) == sp.zeros(8)}
out["symmetry_checks"] = {k: bool(v) for k, v in sym.items()}
print(out["symmetry_checks"], flush=True)

# ---- exact spectra (charpolys, factored) ----
lam = sp.symbols('lam')
def cp(M, ix): return sp.factor(sp.simplify(sub(M, ix).charpoly(lam).as_expr()))
spec = {}
for name, M in (("N", N), ("V", V), ("e", e), ("trefoil_s0^3", tref)):
    spec[name] = {f"W{w}": str(cp(M, blocks[w])) for w in range(4)}
spec["e_full"] = str(sp.factor(sp.simplify(e.charpoly(lam).as_expr())))
out["charpolys_exact"] = spec
print(json.dumps(spec, indent=1), flush=True)

# ---- C2: crossing Coulomb charge 1/2(n+ - n-) ----
words = {"N=V^3": [+1, -1]*3, "e=s0s1s0": [+1, +1, +1], "trefoil=s0^3": [+1]*3}
out["C2_coulomb_half_writhe"] = {k: str(sp.Rational(sum(v), 2)) for k, v in words.items()}

# ---- exact traces: C3 and C4 (block-level, rational functions of q) ----
def tr(M): return sp.simplify(M.trace())
ex = {}
for w in (1, 2):
    ix = blocks[w]
    ex[f"W{w}"] = {"tr N": tr(sub(N, ix)), "tr K N": tr(sub(K*N, ix)), "tr T3 N": tr(sub(T3*N, ix))}
ex["e_full"] = {"tr e": tr(e), "tr K e": tr(K*e), "tr T3 e": tr(T3*e), "tr T3 K e": tr(T3*K*e)}
ex["e_blocks"] = {f"W{w}": {"tr e": tr(sub(e, blocks[w])), "tr K e": tr(sub(K*e, blocks[w]))}
                  for w in range(4)}
ex["trefoil_full"] = {"tr K t": tr(K*tref), "tr T3 t": tr(T3*tref)}
ex["tr N on W1 - tr N on W2"] = sp.simplify(ex["W1"]["tr N"] - ex["W2"]["tr N"])
out["traces_exact"] = json.loads(json.dumps(ex, default=str))
print(json.dumps(out["traces_exact"], indent=1), flush=True)

# ---- numerics at q0 and q = 1 + 1e-20 (mpmath 60 dps) ----
def mpmat(M, qv):
    return mp.matrix([[mp.mpmathify(sp.N(M[i, j].subs(q, sp.Float(str(qv), 70)), 70))
                       for j in range(M.cols)] for i in range(M.rows)])
def eig_report(M, qv):
    ev = mp.eig(M, left=False, right=False)
    rows = []
    for z in ev:
        rows.append({"re": mp.nstr(mp.re(z), 25), "im": mp.nstr(mp.im(z), 5),
                     "|z|": mp.nstr(abs(z), 25), "Arg/2pi": mp.nstr(mp.arg(z)/(2*mp.pi), 25)})
    return rows, ev
numer = {}
for lab, qv in (("q0", mp.mpf(q0s)), ("q=1+1e-20", 1 + mp.mpf('1e-20'))):
    d = {}
    for name, M, ixs in (("N", N, {1: blocks[1], 2: blocks[2]}), ("e", e, {"full": list(range(8))})):
        for key, ix in ixs.items():
            Mb = mpmat(sub(M, ix), qv)
            rows, ev = eig_report(Mb, qv)
            # C1: tr log/2pi i with principal branch; arg-only variant.
            trlog = sum(mp.log(z) for z in ev)/(2j*mp.pi)
            trarg = sum(mp.arg(z) for z in ev)/(2*mp.pi)
            near_cut = [mp.nstr(z, 12) for z in ev if mp.re(z) < 0 and abs(mp.im(z)) < mp.mpf('1e-40')]
            d[f"{name}_{key}"] = {"eigen": rows, "C1_trQhat": mp.nstr(trlog, 25),
                                  "C1_trQhat_arg": mp.nstr(trarg, 25),
                                  "eigenvalues_on_branch_cut": near_cut}
    for w in (1, 2):
        KN = mpmat(sub(K*N, blocks[w]), qv)
        d[f"N_W{w}_trKN"] = mp.nstr(sum(KN[i, i] for i in range(3)), 25)
        d[f"N_W{w}_C3_sign_trKN"] = int(mp.sign(mp.re(sum(KN[i, i] for i in range(3)))))
        d[f"N_W{w}_C4_trT3N"] = mp.nstr(sum(mpmat(sub(T3*N, blocks[w]), qv)[i, i] for i in range(3)), 25)
    trKe = sum(mpmat(K*e, qv)[i, i] for i in range(8))
    d["e_full_C3_sign_trKe"] = int(mp.sign(trKe)); d["e_full_trKe"] = mp.nstr(trKe, 25)
    d["e_full_C4_trT3e"] = mp.nstr(sum(mpmat(T3*e, qv)[i, i] for i in range(8)), 25)
    numer[lab] = d
out["numerics"] = numer
print(json.dumps(numer, indent=1), flush=True)

# ---- verdict per candidate: does exactly one block satisfy Q_p = -Q_e ? ----
def fixes(QW2, QW1, Qe, tol=mp.mpf('1e-40')):
    m2, m1 = abs(QW2 + Qe) < tol, abs(QW1 + Qe) < tol
    if m2 and not m1: return "FIXED: proton = W2 (O+)"
    if m1 and not m2: return "FIXED: proton = W1 (O-)"
    if m1 and m2: return "unfixed (both blocks satisfy neutrality)"
    return "inconsistent (neither block satisfies neutrality)"
v = {}
for lab, d in numer.items():
    c = lambda s: mp.mpmathify(s)
    v[lab] = {
        "C1_trQhat(principal)": fixes(c(d["N_2"]["C1_trQhat"]), c(d["N_1"]["C1_trQhat"]), c(d["e_full"]["C1_trQhat"])),
        "C1_arg": fixes(c(d["N_2"]["C1_trQhat_arg"]), c(d["N_1"]["C1_trQhat_arg"]), c(d["e_full"]["C1_trQhat_arg"])),
        "C1_arg_other_branch": fixes(c(d["N_2"]["C1_trQhat_arg"]), c(d["N_1"]["C1_trQhat_arg"]), -c(d["e_full"]["C1_trQhat_arg"])),
        "C2_half_writhe": fixes(mp.mpf(0), mp.mpf(0), mp.mpf(3)/2),
        "C3_sign": fixes(mp.mpf(d["N_W2_C3_sign_trKN"]), mp.mpf(d["N_W1_C3_sign_trKN"]), mp.mpf(d["e_full_C3_sign_trKe"])),
        "C4_trT3": fixes(c(d["N_W2_C4_trT3N"]), c(d["N_W1_C4_trT3N"]), c(d["e_full_C4_trT3e"]))}
out["verdicts"] = v
print(json.dumps(v, indent=1))
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1, default=str)
