#!/usr/bin/env python3
"""gram_h4.py — 24x24 Gram matrix G4 of the H4(q) Markov trace (T2-b, bean qou-5lbe).

Transcribes TRM / mulsigma0/1/2 / mulNF word structure EXACTLY from
  folio/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean
(convention: T_s^2 = 1 + h*T_s, h = q - 1/q; Ocneanu trace tr(1)=1, tr(x T_top)=z tr(x)).

Cross-checks the transcription against the independent generator
  computations/markov/hecke_regular_nf_table.py  (Hecke(4), markov_trace)
then computes G4[i][j] = trM(e_i * b_j), checks symmetry, computes det over ZZ[z,h]
(DomainMatrix, fraction-free), factors it, specializes h = q - 1/q, and compares with
the Wedderburn prediction  det G4 = c(q) * prod_lambda y_lambda^{d_lambda^2}
with y_lambda the Ocneanu weights solved from the 5-class character system
(block matrices from computations/h4_wedderburn/hecke-h4-wedderburn-seminormal.data.json).

Progress lines every major step; run with  python3 -u gram_h4.py 2>&1 | tee gram_h4.log
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

HERE = Path(__file__).resolve().parent
REPO = Path("/home/user/qou")

z, h, q = sp.symbols("z h q")

# ---------------------------------------------------------------------------
# 1. EXACT transcription of MarkovTraceH4.lean
# ---------------------------------------------------------------------------
def TRM():
    return [sp.Integer(1), z, z, z, z**2, z**2, z**2, z**2, z**2, h*z**2 + z,
            z**3, z**3, z**3, h*z**2 + z, z**3, h*z**3 + z**2, h*z**3 + z**2,
            h*z**3 + z**2, h*z**3 + z**2, h*z**3 + z**2,
            h**2*z**3 + h*z**2 + z**3, h**2*z**3 + 2*h*z**2 + z,
            h**2*z**3 + h*z**2 + z**3, h**3*z**3 + h**2*z**2 + 2*h*z**3 + z**2]

def muls0(v):
    return [v[3], v[6], v[8], v[0] + h*v[3], v[12], v[14], v[1] + h*v[6], v[13],
            v[2] + h*v[8], v[18], v[16], v[19], v[4] + h*v[12], v[7] + h*v[13],
            v[5] + h*v[14], v[21], v[10] + h*v[16], v[22], v[9] + h*v[18],
            v[11] + h*v[19], v[23], v[15] + h*v[21], v[17] + h*v[22],
            v[20] + h*v[23]]

def muls1(v):
    return [v[2], v[5], v[0] + h*v[2], v[7], v[9], v[1] + h*v[5], v[11],
            v[3] + h*v[7], v[13], v[4] + h*v[9], v[15], v[6] + h*v[11], v[17],
            v[8] + h*v[13], v[19], v[10] + h*v[15], v[20], v[12] + h*v[17],
            v[22], v[14] + h*v[19], v[16] + h*v[20], v[23], v[18] + h*v[22],
            v[21] + h*v[23]]

def muls2(v):
    return [v[1], v[0] + h*v[1], v[4], v[6], v[2] + h*v[4], v[9], v[3] + h*v[6],
            v[10], v[12], v[5] + h*v[9], v[7] + h*v[10], v[15], v[8] + h*v[12],
            v[16], v[18], v[11] + h*v[15], v[13] + h*v[16], v[20],
            v[14] + h*v[18], v[21], v[17] + h*v[20], v[19] + h*v[21], v[23],
            v[22] + h*v[23]]

MULS = {0: muls0, 1: muls1, 2: muls2}

# Reduced words of the 24 NF basis elements, read off the mulNF composites in
# MarkovTraceH4.lean (innermost application first = leftmost letter of the word,
# since mulsk is RIGHT multiplication by sigma_k):
WORDS = [
    [], [2], [1], [0],
    [1, 2], [2, 1], [2, 0], [0, 1], [1, 0],
    [1, 2, 1], [0, 1, 2], [2, 0, 1], [1, 2, 0], [0, 1, 0], [2, 1, 0],
    [0, 1, 2, 1], [0, 1, 2, 0], [1, 2, 0, 1], [1, 2, 1, 0], [2, 0, 1, 0],
    [0, 1, 2, 0, 1], [0, 1, 2, 1, 0], [1, 2, 0, 1, 0],
    [0, 1, 2, 0, 1, 0],
]

def apply_word(u, word):
    for g in word:
        u = MULS[g](u)
    return u

def mulNF(u, v):
    """Exactly the Lean mulNF: (u*v)_i = sum_j v_j * (u . b_j)_i."""
    out = [sp.Integer(0)] * 24
    for j in range(24):
        ub = apply_word(u, WORDS[j])
        for i in range(24):
            out[i] += v[j] * ub[i]
    return [sp.expand(x) for x in out]

def basis(i):
    e = [sp.Integer(0)] * 24
    e[i] = sp.Integer(1)
    return e

def trM(v, trm):
    return sp.expand(sum(v[i] * trm[i] for i in range(24)))

# ---------------------------------------------------------------------------
# 2. Cross-check transcription vs hecke_regular_nf_table.py (independent infra)
# ---------------------------------------------------------------------------
log("cross-checking Lean transcription against hecke_regular_nf_table.Hecke(4) ...")
sys.path.insert(0, str(REPO / "computations" / "markov"))
from hecke_regular_nf_table import Hecke, markov_trace, reduced_word  # noqa: E402

H4 = Hecke(4)
assert H4.N == 24
tr_ref = markov_trace(H4)
trm = TRM()
mism = [k for k in range(24) if sp.expand(tr_ref[k] - trm[k]) != 0]
assert not mism, f"TRM mismatch at {mism}"
log("  TRM matches markov_trace(Hecke(4)) on all 24 entries")

# generator right-action check: row k of gen i == mulsk(e_k)
for i, fn in MULS.items():
    for k in range(24):
        ref = [H4.gen[i][k].get(c, sp.Integer(0)) for c in range(24)]
        got = fn(basis(k))
        assert all(sp.expand(a - b) == 0 for a, b in zip(ref, got)), (i, k)
log("  mulsigma0/1/2 match Hecke(4).gen row-by-row")

# basis words: b_j = word_j applied to identity; and matches Hecke S ordering
for j in range(24):
    bj = apply_word(basis(0), WORDS[j])
    ej = basis(j)
    assert all(sp.expand(a - b) == 0 for a, b in zip(bj, ej)), f"word {j} != e_{j}"
    assert WORDS[j] == reduced_word(H4.S[j]) or len(WORDS[j]) == len(reduced_word(H4.S[j])), j
log("  mulNF word list reproduces e_j = b_j for all 24 basis words")

# ---------------------------------------------------------------------------
# 3. The Gram matrix G4 and its symmetry
# ---------------------------------------------------------------------------
log("building G4[i][j] = trM(e_i . b_j) ...")
G = [[None] * 24 for _ in range(24)]
for i in range(24):
    u = basis(i)
    for j in range(24):
        G[i][j] = trM(apply_word(u, WORDS[j]), trm)
    log(f"  row {i} done")

sym_bad = [(i, j) for i in range(24) for j in range(i + 1, 24)
           if sp.expand(G[i][j] - G[j][i]) != 0]
assert not sym_bad, f"Gram NOT symmetric at {sym_bad[:5]}"
log("G4 is symmetric (all 276 off-diagonal pairs) — gram_symm confirmed symbolically")

with open(HERE / "gram_h4_matrix.json", "w") as f:
    json.dump([[str(G[i][j]) for j in range(24)] for i in range(24)], f, indent=1)
log("wrote gram_h4_matrix.json")

# ---------------------------------------------------------------------------
# 4. det G4 over ZZ[z,h] (fraction-free), then factor
# ---------------------------------------------------------------------------
log("computing det G4 via DomainMatrix over ZZ[z,h] ...")
M = sp.Matrix(G)
dM = DomainMatrix.from_Matrix(M)
log(f"  domain = {dM.domain}")
det_dom = dM.det()
detG = sp.expand(det_dom.as_expr() if hasattr(det_dom, "as_expr") else sp.sympify(det_dom))
log("det computed; factoring over ZZ[z,h] ...")
detG_f = sp.factor(detG)
log(f"det G4 (z,h) factored:\n  {detG_f}")

# numeric spot-check vs rational Bareiss det
subs_n = {z: sp.Rational(5, 2), h: sp.Rational(7, 3)}
num1 = detG.subs(subs_n)
num2 = M.subs(subs_n).det(method="bareiss")
assert sp.simplify(num1 - num2) == 0, "numeric det spot-check FAILED"
log(f"numeric spot-check at z=5/2, h=7/3 OK: det = {num1}")

# ---------------------------------------------------------------------------
# 5. Hecke specialization h = q - 1/q, factored over Q(q)
# ---------------------------------------------------------------------------
log("specializing h = q - 1/q ...")
detG_q = sp.factor(sp.together(detG.subs(h, q - 1/q)))
log(f"det G4 (q,z) factored:\n  {detG_q}")

# ---------------------------------------------------------------------------
# 6. Ocneanu weights y_lambda at n = 4 and the Wedderburn prediction
# ---------------------------------------------------------------------------
log("solving the 5-class character system for the Ocneanu weights y_lambda ...")
data = json.load(open(REPO / "computations" / "h4_wedderburn" /
                      "hecke-h4-wedderburn-seminormal.data.json"))

def blk(part, name):
    rows = data["blocks"][part][name]
    return sp.Matrix([[sp.nsimplify(sp.sympify(e)) for e in row] for row in rows])

BLOCKS = {p: {i: blk(p, f"S{i}") for i in range(3)} for p in ["(2,2)", "(3,1)", "(2,1,1)"]}

def chi(part, word):
    if part == "(4)":
        return q ** len(word)
    if part == "(1,1,1,1)":
        return (-1 / q) ** len(word)
    m = sp.eye(BLOCKS[part][0].shape[0])
    for g in word:
        m = m * BLOCKS[part][g]
    return sp.simplify(m.trace())

# minimal-length class representatives of S4 and their Markov traces
classes = [([], sp.Integer(1)),           # e
           ([0], z),                      # transposition
           ([0, 2], z**2),                # (2,2) double transposition
           ([0, 1], z**2),                # 3-cycle
           ([0, 1, 2], z**3)]             # 4-cycle
parts = ["(4)", "(3,1)", "(2,2)", "(2,1,1)", "(1,1,1,1)"]
dims = {"(4)": 1, "(3,1)": 3, "(2,2)": 2, "(2,1,1)": 3, "(1,1,1,1)": 1}

A = sp.Matrix([[chi(p, w) for p in parts] for (w, _) in classes])
b = sp.Matrix([[t] for (_, t) in classes])
y = sp.simplify(A.solve(b))
weights = {}
for k, p in enumerate(parts):
    weights[p] = sp.factor(sp.together(y[k]))
    log(f"  y_{p} = {weights[p]}")

# sanity: weights reproduce tr on random basis elements via the regular rep? cheap
# check instead: tr(1) = sum d_lambda * y_lambda = 1
tot = sp.simplify(sum(dims[p] * y[k] for k, p in enumerate(parts)) - 1)
assert tot == 0, f"sum d*y != 1: {tot}"
log("  sum_lambda d_lambda*y_lambda = 1 OK")

log("checking det G4 = c(q) * prod y_lambda^(d^2) ...")
pred = sp.prod([weights[p] ** (dims[p] ** 2) for p in parts])
ratio = sp.factor(sp.together(sp.cancel(detG_q / pred)))
log(f"  c(q) = det/prod = {ratio}")

# compare with the coordinate determinant of the Wedderburn map (JSON)
detA = sp.factor(sp.sympify(data["det_A_factored"]))
ratio2 = sp.factor(sp.cancel(ratio / detA**2))
log(f"  c(q) / det_A^2 = {ratio2}")

with open(HERE / "gram_h4_det.json", "w") as f:
    json.dump({
        "detG_zh_expanded_nterms": len(sp.Add.make_args(detG)),
        "detG_zh_factored": str(detG_f),
        "detG_qz_factored": str(detG_q),
        "weights": {p: str(weights[p]) for p in parts},
        "dims": dims,
        "c_q_ratio_det_over_prod_weights": str(ratio),
        "c_q_over_detA_squared": str(ratio2),
        "det_A_factored_json": str(detA),
        "numeric_check": {"z": "5/2", "h": "7/3", "det": str(num1)},
    }, f, indent=1)
log("wrote gram_h4_det.json — DONE")
