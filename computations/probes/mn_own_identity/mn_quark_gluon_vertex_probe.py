#!/usr/bin/env python3
"""Does the QOU braid crossing carry the QCD quark-gluon colour factor?

Pre-registration: PREREGISTRATION-quark-gluon-vertex.md (committed before this file).

Exact, sympy, q symbolic.  Vectors on (C^N)^{(x)n} are dicts {basis tuple: sympy expr}.
The Jimbo braiding R-check on C^N (x) C^N:
    R(e_i e_i) = q e_i e_i
    R(e_i e_j) = e_j e_i                         (i < j)
    R(e_j e_i) = e_i e_j + (q - 1/q) e_j e_i     (i < j)
For N = 2 this is the constraints' Rc = [[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]].
No float anywhere.
"""
import itertools
import json
import os

import sympy as sp

q = sp.symbols("q", positive=True)
h = sp.symbols("h")  # h = q - 1/q
OUT = {}


def simp(x):
    return sp.simplify(sp.factor(x))


def R_pair(i, j):
    """R acting on e_i (x) e_j -> dict {(a,b): coeff}."""
    if i == j:
        return {(i, i): q}
    if i < j:
        return {(j, i): sp.Integer(1)}
    # i > j :  e_i e_j with j < i
    return {(j, i): sp.Integer(1), (i, j): q - 1 / q}


def add(d, k, v):
    d[k] = d.get(k, 0) + v


def sigma(vec, pos, inverse=False):
    """sigma_pos acting on strands pos, pos+1 (0-based)."""
    out = {}
    for basis, c in vec.items():
        i, j = basis[pos], basis[pos + 1]
        for (a, b), r in R_pair(i, j).items():
            nb = basis[:pos] + (a, b) + basis[pos + 2:]
            add(out, nb, c * r)
    if inverse:  # sigma^{-1} = sigma - (q - 1/q)
        for basis, c in vec.items():
            add(out, basis, -(q - 1 / q) * c)
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def word(vec, letters):
    """apply letters right-to-left as written: word [a,b,c] = a b c, so c acts first."""
    for L in reversed(letters):
        pos = abs(L) - 1
        vec = sigma(vec, pos, inverse=(L < 0))
    return vec


def full_twist_letters(start, n):
    """Delta^2 on strands start..start+n-1 (letters 1-based): (s1 s2 ... s_{n-1})^n."""
    one = list(range(start, start + n - 1))
    return one * n


def basis_vec(t):
    return {t: sp.Integer(1)}


def as_matrix(op, N, n):
    B = list(itertools.product(range(N), repeat=n))
    idx = {b: k for k, b in enumerate(B)}
    M = sp.zeros(len(B), len(B))
    for col, b in enumerate(B):
        for k, v in op(basis_vec(b)).items():
            M[idx[k], col] = v
    return M


def is_scalar_on(vec, op, mu):
    w = op(vec)
    keys = set(w) | set(vec)
    return all(simp(w.get(k, 0) - mu * vec.get(k, 0)) == 0 for k in keys)


def exponent_of(mu):
    """mu = +/- q^k ; return (sign, k) exactly."""
    mu = simp(mu)
    for sgn in (1, -1):
        e = simp(sp.log(sgn * mu) / sp.log(q))
        e = sp.nsimplify(sp.expand_log(sp.log(sp.powsimp(sgn * mu)), force=True) / sp.log(q))
        if e.is_Rational:
            if simp(sgn * q ** e - mu) == 0:
                return sgn, e
    raise ValueError(mu)


# ------------------------------------------------------------------ checks of R
def checks(N):
    s1 = as_matrix(lambda v: sigma(v, 0), N, 2)
    hecke = simp((s1 - q * sp.eye(N * N)) * (s1 + sp.eye(N * N) / q)) == sp.zeros(N * N)
    braid = True
    for b in itertools.product(range(N), repeat=3):
        v = basis_vec(b)
        l = word(v, [1, 2, 1])
        r = word(v, [2, 1, 2])
        if any(simp(l.get(k, 0) - r.get(k, 0)) != 0 for k in set(l) | set(r)):
            braid = False
    return {"hecke_relation": bool(hecke), "braid_relation": braid}


for N in (2, 3):
    OUT[f"R_checks_N{N}"] = checks(N)


# ------------------------------------------------------------------ Casimirs (T(F)=1/2)
def casimirs(N):
    N = sp.Integer(N)
    CF = (N**2 - 1) / (2 * N)
    return {
        "C_F": CF,
        "C2_Sym2": (N - 1) * (N + 2) / N,
        "C2_Lam2": (N + 1) * (N - 2) / N,
        "C_A": N,
    }


# ------------------------------------------------------------------ (a) n = 2
def part_a(N):
    C = casimirs(N)
    fr = q ** sp.Rational(-1, N)
    s1 = as_matrix(lambda v: sigma(v, 0), N, 2)
    # Sym^2 eigvec e_i e_i ; Lambda^2 eigvec q e_0e_1 - e_1e_0 style: solve nullspace
    lamS = q
    lamA = -1 / q
    # verify eigen-spaces dimension via rank of (s1 - lam)
    dimS = N * N - (s1 - lamS * sp.eye(N * N)).rank(simplify=True)
    dimA = N * N - (s1 - lamA * sp.eye(N * N)).rank(simplify=True)
    sgS, eS = exponent_of(fr * lamS)
    sgA, eA = exponent_of(fr * lamA)
    cS = sp.Rational(1, 2) * (C["C2_Sym2"] - 2 * C["C_F"])
    cA = sp.Rational(1, 2) * (C["C2_Lam2"] - 2 * C["C_F"])
    # q-expansions of log|lambda| of the framed crossing
    logq_in_h = sp.series(sp.asinh(h / 2), h, 0, 7).removeO()  # q = e^{asinh(h/2)}
    ser = {}
    for name, e in (("Sym2", eS), ("Lam2", eA)):
        ser[name] = {
            "in_log_q": f"{e}*log(q)  (exact, no higher terms)",
            "in_h=q-1/q": str(sp.expand(e * logq_in_h)),
            "order_h_coeff": str(sp.expand(e * logq_in_h).coeff(h, 1)),
        }
    return {
        "dims": {"Sym2": int(dimS), "Lam2": int(dimA)},
        "unframed_exponents": {"Sym2": 1, "Lam2": -1, "ratio": -1},
        "framed_eigenvalues": {"Sym2": f"{sgS}*q^({eS})", "Lam2": f"{sgA}*q^({eA})"},
        "T.T_from_crossing (exp/2)": {"Sym2": str(eS / 2), "Lam2": str(eA / 2)},
        "T.T_casimir": {"Sym2": str(cS), "Lam2": str(cA)},
        "match": bool(eS / 2 == cS and eA / 2 == cA),
        "ratio_cA_over_cS": str(cA / cS),
        "C_F": str(C["C_F"]),
        "log_expansions": ser,
    }


for N in (2, 3):
    OUT[f"a_two_strands_N{N}"] = part_a(N)

# ------------------------------------------------------------------ (b) n = 3, N = 3
N = 3
CF3 = casimirs(3)["C_F"]
D2 = full_twist_letters(1, 3)  # (s1 s2)^3
D2mat = as_matrix(lambda v: word(v, D2), 3, 3)
fr6 = q ** sp.Rational(-6, 3)
mus = {"(3) decuplet": q**6, "(2,1) octet x2": sp.Integer(1), "(1^3) singlet": q ** -6}
# multiplicities from traces of D2^0, D2^1, D2^2
t0 = 27
t1 = simp(D2mat.trace())
t2 = simp((D2mat * D2mat).trace())
m = sp.symbols("m0:3")
sol = sp.solve(
    [sum(m) - t0, sum(mi * mu for mi, mu in zip(m, mus.values())) - t1,
     sum(mi * mu**2 for mi, mu in zip(m, mus.values())) - t2], m)
minpoly_zero = simp((D2mat - q**6 * sp.eye(27)) * (D2mat - sp.eye(27)) * (D2mat - q**-6 * sp.eye(27))) == sp.zeros(27)
C2su3 = {"(3) decuplet": sp.Integer(6), "(2,1) octet x2": sp.Integer(3), "(1^3) singlet": sp.Integer(0)}
bres = {}
for (name, mu), mi in zip(mus.items(), m):
    sg, e = exponent_of(fr6 * mu)
    TT = e / 4
    bres[name] = {
        "multiplicity": int(sol[mi]),
        "framed_full_twist": f"{sg}*q^({e})",
        "sum_i<j T_i.T_j from twist": str(TT),
        "QCD value (C2(lam)-3C_F)/2": str((C2su3[name] - 3 * CF3) / 2),
        "match": bool(TT == (C2su3[name] - 3 * CF3) / 2),
    }
# explicit baryon vector: joint -1/q eigenvector of s1, s2
S1 = as_matrix(lambda v: sigma(v, 0), 3, 3)
S2 = as_matrix(lambda v: sigma(v, 1), 3, 3)
ns = (S1 + sp.eye(27) / q).col_join(S2 + sp.eye(27) / q).nullspace(simplify=True)
B3 = list(itertools.product(range(3), repeat=3))
vbar = {B3[k]: simp(ns[0][k]) for k in range(27) if simp(ns[0][k]) != 0}
OUT["b_three_strands_N3"] = {
    "full_twist_minpoly_(x-q^6)(x-1)(x-q^-6)=0": bool(minpoly_zero),
    "summands": bres,
    "Lambda3_dim (joint -1/q eigenspace)": len(ns),
    "baryon_vector": {str(k): str(v) for k, v in vbar.items()},
    "baryon_full_twist_check_q^-6": bool(is_scalar_on(vbar, lambda v: word(v, D2), q**-6)),
    "QCD_baryon -3/2 C_F": str(-sp.Rational(3, 2) * CF3),
}


# ------------------------------------------------------------------ qqbar via V* = Lambda^2 V
def lam2_vectors(N):
    S = as_matrix(lambda v: sigma(v, 0), N, 2)
    ns = (S + sp.eye(N * N) / q).nullspace(simplify=True)
    B2 = list(itertools.product(range(N), repeat=2))
    return [{B2[k]: simp(v[k]) for k in range(N * N) if simp(v[k]) != 0} for v in ns]


def tensor_front(i, vec):
    return {(i,) + k: c for k, c in vec.items()}


def flatten(vecs, basis):
    idx = {b: k for k, b in enumerate(basis)}
    M = sp.zeros(len(basis), len(vecs))
    for c, v in enumerate(vecs):
        for k, x in v.items():
            M[idx[k], c] = x
    return M


def restricted_monodromy(N, inner_vecs, n_inner):
    """M = Delta^2(1..n_inner+1) * Delta^2(2..n_inner+1)^{-1} on span{e_i (x) w}."""
    n = n_inner + 1
    big = full_twist_letters(1, n)
    inner = full_twist_letters(2, n_inner)
    inner_inv = [-L for L in reversed(inner)]
    letters = big + inner_inv
    vecs = [tensor_front(i, w) for i in range(N) for w in inner_vecs]
    imgs = [word(v, letters) for v in vecs]
    basis = list(itertools.product(range(N), repeat=n))
    Bm = flatten(vecs, basis)
    Im = flatten(imgs, basis)
    # solve Bm X = Im
    X = (Bm.T * Bm).LUsolve(Bm.T * Im)
    X = X.applyfunc(simp)
    assert simp(Bm * X - Im) == sp.zeros(*Im.shape)
    lam = sp.symbols("lam")
    cp = sp.factor(X.charpoly(lam).as_expr())
    writhe = sum(1 if L > 0 else -1 for L in letters)
    return X, cp, writhe


w2 = lam2_vectors(3)
Xqq, cpqq, ncross = restricted_monodromy(3, w2, 2)
frq = q ** sp.Rational(-ncross, 3)
eig = sp.roots(sp.Poly(cpqq, sp.symbols("lam")))
qq = {}
for mu, mult in eig.items():
    sg, e = exponent_of(frq * mu)
    qq[f"mult {mult}"] = {"unframed": str(mu), "framed": f"{sg}*q^({e})", "T_V.T_Vbar": str(e / 4)}
OUT["b_qqbar_N3_via_Vstar=Lambda2V"] = {
    "writhe (framing exponent; 6 - 2)": ncross,
    "charpoly": str(cpqq),
    "eigen": qq,
    "QCD singlet -C_F": str(-CF3),
    "QCD octet (C_A-2C_F)/2": str((3 - 2 * CF3) / 2),
}

# ------------------------------------------------------------------ (c) framing forcing
force = {}
for Nn in (2, 3):
    # Lambda^N V in V^{(x)N}: joint -1/q eigenvector of s1..s_{N-1}
    mats = [as_matrix(lambda v, p=p: sigma(v, p), Nn, Nn) + sp.eye(Nn**Nn) / q for p in range(Nn - 1)]
    stack = mats[0]
    for mm in mats[1:]:
        stack = stack.col_join(mm)
    nsN = stack.nullspace(simplify=True)
    BN = list(itertools.product(range(Nn), repeat=Nn))
    wN = [{BN[k]: simp(v[k]) for k in range(Nn**Nn) if simp(v[k]) != 0} for v in nsN]
    X, cp, nc = restricted_monodromy(Nn, wN, Nn)
    c = sp.symbols("c", positive=True)
    is_q2 = simp(X - q**2 * sp.eye(X.shape[0])) == sp.zeros(*X.shape)
    csol = sp.solve(sp.Eq(c ** (2 * Nn) * q**2, 1), c)
    force[f"N{Nn}"] = {
        "dim Lambda^N": len(nsN),
        "writhe": nc,
        "monodromy_unframed_is_q^2*Id": bool(is_q2),
        "forced_c": [str(x) for x in csol],
    }
OUT["c_framing_forcing"] = force

# Lambda^3 C^2 = 0
OUT["c_N2_three_strand_singlet_exists"] = bool(
    (as_matrix(lambda v: sigma(v, 0), 2, 3) + sp.eye(8) / q)
    .col_join(as_matrix(lambda v: sigma(v, 1), 2, 3) + sp.eye(8) / q)
    .nullspace(simplify=True))


# Markov parameter from the quantum partial trace with K_{2rho}
def zN(N):
    w = [q ** (N - 1 - 2 * k) for k in range(N)]
    out = sp.zeros(N, N)
    for i in range(N):
        for ip in range(N):
            tot = 0
            for j in range(N):
                tot += w[j] * R_pair(ip, j).get((i, j), 0)
            out[i, ip] = simp(tot)
    qN = sum(w)
    zz = [simp(out[i, i] / qN) for i in range(N)]
    offdiag = all(out[i, j] == 0 for i in range(N) for j in range(N) if i != j)
    return {"ptr_diag_over_[N]": [str(x) for x in zz], "offdiag_zero": offdiag,
            "equals_q^N/[N]": all(simp(x - q**N / qN) == 0 for x in zz)}


OUT["c_markov_z"] = {"N2": zN(2), "N3": zN(3),
                     "convention_D q^3/(q^2+1)": "equals N2",
                     "prereg_slip": "prereg wrote z3 = q^4/(q^4+q^2+1); that was a hand slip. Computed z3 = q^5/(q^4+q^2+1) = q^3/[3]_q = q^N/[N]_q."}

OUT["verdict"] = (
    "(a),(b) reproduce the standard Drinfeld-Jimbo / ribbon statement: framed crossing "
    "exponent = 2 T.T, full twist = 4 sum T_i.T_j, monodromy = 4 T_V.T_W, exactly in log q. "
    "Nothing QOU-specific. N, the vector rep and the framing q^{-1/N} are inputs not fixed by "
    "the Hecke algebra."
)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mn_quark_gluon_vertex_probe.out.json")
with open(path, "w") as f:
    json.dump(OUT, f, indent=2, default=str)
print(json.dumps(OUT, indent=2, default=str))
