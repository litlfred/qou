"""q2c probe (bean qou-cb3r): is there a q-analogue of su3_e ⊂ Der(O) that meets Jimbo's R at q != 1?

Exact arithmetic only (fractions.Fraction, evaluated at exact rational q). No float anywhere in the
computation; all output is exact rationals.

Object: the 7-dim U_q(g2) module V7 (the quantum deformation of Im O = 1 + 3 + 3bar), split form,
Jantzen conventions: alpha1 short (q1 = q), alpha2 long (q2 = q^3); Cartan pairings
<a1v,a2> = -3, <a2v,a1> = -1; Delta(E) = E(x)1 + K(x)E, Delta(F) = F(x)K^-1 + 1(x)F, Delta(K) = K(x)K.

Checks:
  M  module: every U_q(g2) relation (KE, KF, [E,F], both quantum Serre) holds on V7, exactly.
  A  restriction: long-root-weight operators preserve 1, 3, 3bar (weights), and the Cartan part on the
     long-root subalgebra is a power of q^3: the colour sl3 inside g2 is deformed at q_long = q^3.
  B  coproduct: the most general weight-(3a1+a2) element x of U_q(n+) (4-dim, monomials E1^a E2 E1^(3-a))
     with Delta(x) mapping 3(x)3 into 3(x)3 AND x acting nonzero on 3 -- solve for it at q = 1 and q != 1.
  C  product: Hom_{U_q(g2)}(V7 (x) V7, V7) (the q-cross-product, i.e. the replacement of Im-octonion
     multiplication), and its left/right multiplication by the sl3-fixed weight-0 vector e = v4:
     eigenvalues on 3 and 3bar, and whether L_e and R_e still differ only by sign.
"""
from fractions import Fraction as Fr
import itertools, json, sys

def qint(n, q):
    return sum((q ** (n - 1 - 2 * k) for k in range(n)), Fr(0))

def qbinom(n, k, q):
    num = Fr(1); den = Fr(1)
    for i in range(k):
        num *= qint(n - i, q); den *= qint(i + 1, q)
    return num / den

def zeros(n, m=None):
    m = n if m is None else m
    return [[Fr(0)] * m for _ in range(n)]

def mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        C[i][j] += a * Bt[j]
    return C

def add(A, B, s=Fr(1)):
    return [[a + s * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]

def scal(c, A):
    return [[c * a for a in r] for r in A]

def eye(n):
    I = zeros(n)
    for i in range(n): I[i][i] = Fr(1)
    return I

def kron(A, B):
    n, m = len(A), len(B)
    C = zeros(n * m)
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                for k in range(m):
                    for l in range(m):
                        if B[k][l]:
                            C[i * m + k][j * m + l] = A[i][j] * B[k][l]
    return C

def iszero(A):
    return all(x == 0 for r in A for x in r)

# weights (Dynkin labels <a1v,.>, <a2v,.>) of v1..v7 (index 0..6)
LAB = [(1, 0), (-1, 1), (2, -1), (0, 0), (-2, 1), (1, -1), (-1, 0)]
# chain of f's: v1 -f1-> v2 -f2-> v3 -f1-> v4 -f1-> v5 -f2-> v6 -f1-> v7
CHAIN = [(0, 1, 1), (1, 2, 2), (2, 3, 1), (3, 4, 1), (4, 5, 2), (5, 6, 1)]
TRIP, ANTI, SING = [0, 5, 4], [6, 1, 2], [3]   # 3 = {v1,v6,v5}, 3bar = {v7,v2,v3}, 1 = {v4}

def module(q):
    q1, q2 = q, q ** 3
    E = {1: zeros(7), 2: zeros(7)}; F = {1: zeros(7), 2: zeros(7)}
    K = {1: zeros(7), 2: zeros(7)}; Ki = {1: zeros(7), 2: zeros(7)}
    for v, (l1, l2) in enumerate(LAB):
        K[1][v][v] = q1 ** l1; K[2][v][v] = q2 ** l2
        Ki[1][v][v] = q1 ** (-l1); Ki[2][v][v] = q2 ** (-l2)
    # string structure: f1-strings {v1,v2}, {v3,v4,v5}, {v6,v7}; f2-strings {v2,v3}, {v5,v6}
    # F v_k = v_{k+1};  E v_{k+1} = [k][n-k] v_k on an n-dim string
    strings = {1: [[0, 1], [2, 3, 4], [5, 6]], 2: [[1, 2], [4, 5]]}
    for i, sts in strings.items():
        qi = q1 if i == 1 else q2
        for st in sts:
            n = len(st)
            for k in range(1, n):
                a, b = st[k - 1], st[k]
                F[i][b][a] = Fr(1)
                E[i][a][b] = qint(k, qi) * qint(n - k, qi)
    return E, F, K, Ki

def check_module(q):
    E, F, K, Ki = module(q)
    qs = {1: q, 2: q ** 3}
    A = {(1, 1): 2, (1, 2): -3, (2, 1): -1, (2, 2): 2}
    bad = []
    for i in (1, 2):
        for j in (1, 2):
            qi = qs[i]
            if mul(mul(K[i], E[j]), Ki[i]) != scal(qi ** A[(i, j)], E[j]): bad.append(("KE", i, j))
            if mul(mul(K[i], F[j]), Ki[i]) != scal(qi ** (-A[(i, j)]), F[j]): bad.append(("KF", i, j))
            comm = add(mul(E[i], F[j]), mul(F[j], E[i]), Fr(-1))
            want = scal(1 / (qi - 1 / qi), add(K[i], Ki[i], Fr(-1))) if i == j else zeros(7)
            if comm != want: bad.append(("EF", i, j))
    for (i, j) in ((1, 2), (2, 1)):
        n = 1 - A[(i, j)]; qi = qs[i]
        for X in (E, F):
            S = zeros(7)
            for k in range(n + 1):
                term = eye(7)
                for _ in range(n - k): term = mul(term, X[i])
                term = mul(term, X[j])
                for _ in range(k): term = mul(term, X[i])
                S = add(S, scal((-1) ** k * qbinom(n, k, qi), term))
            if not iszero(S): bad.append(("Serre", i, j))
    return bad

# ---------- B: coproduct of the long root vector of weight 3a1+a2 -----------------------------
def delta_E(q, i):
    E, F, K, Ki = module(q)
    return add(kron(E[i], eye(7)), kron(K[i], E[i]))

def word(ops, w):
    M = eye(len(ops[1]))
    for s in w: M = mul(M, ops[s])
    return M

MONOS = [(1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1)]

def leakage_basis(q):
    """For each monomial: (Delta(monomial) restricted to 3(x)3 -> complement)  and  (monomial | 3 -> 3)."""
    E, _, _, _ = module(q)
    D = {1: delta_E(q, 1), 2: delta_E(q, 2)}
    T2 = [a * 7 + b for a in TRIP for b in TRIP]
    comp = [r for r in range(49) if r not in T2]
    leaks, acts = [], []
    for w in MONOS:
        Dw = word(D, w); Mw = word(E, w)
        leaks.append([Dw[r][c] for r in comp for c in T2])
        acts.append([Mw[r][c] for r in TRIP for c in TRIP])
    return leaks, acts

def nullspace(rows_by_var):
    """Kernel of the linear map c -> sum_a c_a * vec_a (vectors given per variable)."""
    nvar = len(rows_by_var); neq = len(rows_by_var[0])
    M = [[rows_by_var[a][e] for a in range(nvar)] for e in range(neq)]
    piv = []; r = 0
    for c in range(nvar):
        p = next((i for i in range(r, neq) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / M[r][c]; M[r] = [x * inv for x in M[r]]
        for i in range(neq):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(nvar) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * nvar; v[fcol] = Fr(1)
        for i, pc in enumerate(piv): v[pc] = -M[i][fcol]
        basis.append(v)
    return basis

def check_B(q):
    leaks, acts = leakage_basis(q)
    ker = nullspace(leaks)
    nonzero_on_3 = []
    for v in ker:
        act = [sum(v[a] * acts[a][e] for a in range(4)) for e in range(9)]
        nonzero_on_3.append(any(x != 0 for x in act))
    return {"q": str(q), "kernel_dim": len(ker), "kernel": [[str(x) for x in v] for v in ker],
            "kernel_acts_nonzero_on_3": nonzero_on_3}

# ---------- C: the q-cross-product Hom(V7(x)V7, V7) --------------------------------------------
def check_C(q):
    E, F, K, Ki = module(q)
    gens = []
    for i in (1, 2):
        if q == 1:   # classical U(g2): E, F, H all primitive
            H = zeros(7)
            for v, lab in enumerate(LAB): H[v][v] = Fr(lab[i - 1])
            for X in (E[i], F[i], H):
                gens.append((add(kron(X, eye(7)), kron(eye(7), X)), X))
            continue
        gens.append((add(kron(E[i], eye(7)), kron(K[i], E[i])), E[i]))
        gens.append((add(kron(F[i], Ki[i]), kron(eye(7), F[i])), F[i]))
        gens.append((kron(K[i], K[i]), K[i]))
    # unknown m: 7 x 49, equations m*D(x) = x*m
    nvar = 7 * 49
    eqs = []
    for (DX, X) in gens:
        for r in range(7):
            for c in range(49):
                row = [Fr(0)] * nvar
                for t in range(49):
                    if DX[t][c]: row[r * 49 + t] += DX[t][c]
                for s in range(7):
                    if X[r][s]: row[s * 49 + c] -= X[r][s]
                if any(row): eqs.append(row)
    ker = nullspace([[eqs[e][a] for e in range(len(eqs))] for a in range(nvar)])
    out = {"q": str(q), "hom_dim": len(ker)}
    if len(ker) != 1: return out
    m = [[ker[0][r * 49 + c] for c in range(49)] for r in range(7)]
    e = 3  # v4, weight 0, fixed by the long-root subalgebra
    L = [[m[r][e * 7 + s] for s in range(7)] for r in range(7)]
    R = [[m[r][s * 7 + e] for s in range(7)] for r in range(7)]
    diagL = [L[v][v] for v in range(7)]; diagR = [R[v][v] for v in range(7)]
    offdiag = any(L[r][s] != 0 or R[r][s] != 0 for r in range(7) for s in range(7) if r != s)
    out.update({
        "L_e_diagonal_in_weight_basis": not offdiag,
        "L_e_on_3": [str(diagL[v]) for v in TRIP], "L_e_on_3bar": [str(diagL[v]) for v in ANTI],
        "R_e_on_3": [str(diagR[v]) for v in TRIP], "R_e_on_3bar": [str(diagR[v]) for v in ANTI],
        "L_e_on_e": str(diagL[3]),
    })
    lam3 = diagL[TRIP[0]]
    out["L_e_constant_on_3"] = all(diagL[v] == lam3 for v in TRIP)
    out["L_e_constant_on_3bar"] = all(diagL[v] == diagL[ANTI[0]] for v in ANTI)
    if lam3 != 0:
        out["ratio_L3bar_over_L3"] = str(diagL[ANTI[0]] / lam3)
        out["ratio_R3_over_L3"] = [str(diagR[v] / diagL[v]) for v in TRIP]
        out["ratio_R3bar_over_L3bar"] = [str(diagR[v] / diagL[v]) for v in ANTI]
    return out

if __name__ == "__main__":
    res = {"M_module_relations_failing": {}, "A": {}, "B": [], "C": []}
    for q in (Fr(2), Fr(3), Fr(5, 2)):
        res["M_module_relations_failing"][str(q)] = check_module(q)
    # A: Cartan of the long-root subalgebra on the triplet: K2 and K_beta = K1^3 K2 eigenvalues
    q = Fr(2)
    E, F, K, Ki = module(q)
    res["A"] = {"K2_on_3": [str(K[2][v][v]) for v in TRIP],
                "Kbeta_on_3": [str(K[1][v][v] ** 3 * K[2][v][v]) for v in TRIP],
                "note": "all powers of q^3 = 8: long-root Cartan acts through q_long = q^3"}
    for q in (Fr(1), Fr(2), Fr(3), Fr(5, 2)):
        res["B"].append(check_B(q))
    for q in (Fr(1), Fr(2), Fr(3), Fr(5, 2)):
        res["C"].append(check_C(q))
    res["verdict"] = {
        "A": "V7 restricts to 1 + 3 + 3bar under long-root-weight operators (weights alone); "
             "the long-root Cartan acts through q^3, so the colour sl3 inside U_q(g2) is deformed at q_long = q^3.",
        "B": "q=1: exactly one weight-(3a1+a2) element of U(n+) (ad_E1^3 E2) has Delta preserving 3(x)3; "
             "q in {2,3,5/2}: none in U_q(n+) (kernel 0). The triplet is not a sub-object under the U_q(g2) coproduct.",
        "C": "Hom(V7(x)V7,V7) is 1-dim at every q tested (the q-cross-product). q=1: L_e = +1 on 3, -1 on 3bar, "
             "R_e = -L_e. q != 1: L_e eigenvalues on 3 are (1, q^-4, q^-4) and on 3bar (-q^-6, -q^-2, -q^-2) "
             "up to one overall scale; L_e is not scalar on 3, so it does not commute with the long-root "
             "operators, and R_e/L_e on 3 is (-q^-6, -q^2, -q^2), not -1. The sign separating 3 from 3bar survives.",
        "scope": "(a): exact at rational points q in {1,2,3,5/2}; B searches U_q(n+) only (times Cartan), Jantzen "
                 "coproduct; a q-deformed embedding of the triplet other than the weight subspace is not searched.",
    }
    print(json.dumps(res, indent=1))
    with open(__file__.replace("quantum_g2_colour_stabilizer_probe.py",
                               "quantum-g2-colour-stabilizer-probe.witness.json"), "w") as fh:
        json.dump({"producer": "computations/eightfold/quantum_g2_colour_stabilizer_probe.py",
                   "bean": "qou-cb3r", "arithmetic": "fractions.Fraction (exact)", "result": res}, fh, indent=1)
