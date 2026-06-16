#!/usr/bin/env sage
"""
g_A from the Iwahori-Hecke algebra H_3(q) — Sage computation.

Run from repo root:
    sage computations/sage-borromean-gA.sage

Target: g_A = 1.2754 +/- 0.0013 (PDG 2024)
"""

import json
from datetime import datetime, timezone

print("=" * 60)
print("g_A from Iwahori-Hecke algebra H_3(q)")
print("=" * 60)
print()

# ── Setup: Hecke algebra H_3(q) over Q(q) ───────────────────────
R.<q> = LaurentPolynomialRing(QQ)

# IwahoriHeckeAlgebra of type A_2 = H_3(q)
# Parameters: q1 = q, q2 = -q^{-1} so that (T - q)(T + q^{-1}) = 0
W = WeylGroup(['A', 2], prefix='s')
H = IwahoriHeckeAlgebra(W, q, -q^(-1), base_ring=R)
T = H.T()

# Access generators via simple reflections
s = W.simple_reflections()
T1 = T[s[1]]
T2 = T[s[2]]
e = T.one()

print("Hecke algebra H_3(q) constructed")
print(f"  Relation: (T - q)(T + q^(-1)) = 0")
print(f"  T1 = {T1}")
print(f"  T2 = {T2}")
print()

# ── Verify Hecke relation ────────────────────────────────────────
check = T1^2 - (q - q^(-1)) * T1 - e
print(f"T1^2 - (q - q^(-1))*T1 - 1 = {check}")
print()

# ── T inverses from Hecke relation: T^{-1} = T - (q - q^{-1}) ──
T1_inv = T1 - (q - q^(-1)) * e
T2_inv = T2 - (q - q^(-1)) * e

# Verify: T1 * T1_inv should be identity
check_inv = T1 * T1_inv
print(f"T1 * T1_inv = {check_inv}")
print()

# ── Borromean braid candidates ───────────────────────────────────
braids = {
    "borr_4": T1 * T2_inv * T1 * T2_inv,
    "borr_6": T1 * T2_inv * T1 * T2_inv * T1 * T2_inv,
    "borr_sym": T1 * T2_inv * T1_inv * T2,
}

print("Borromean braid elements (T-basis):")
for name, b in braids.items():
    print(f"  {name} = {b}")
print()

# ── Irreducible representations of H_3(q) ───────────────────────
# (3):     trivial, dim 1:  T_i -> q
# (1,1,1): sign, dim 1:    T_i -> -q^{-1}
# (2,1):   standard, dim 2: explicit matrices

# Standard (2,1) representation matrices
MS = MatrixSpace(R.fraction_field(), 2)
T1_std = MS([[q, 0], [1, -q^(-1)]])
T2_std = MS([[-q^(-1), q - q^(-1)], [0, q]])
I2 = MS.identity_matrix()

# Verify Hecke relation in standard rep
check_std = T1_std^2 - (q - q^(-1)) * T1_std - I2
print(f"Standard rep check (should be 0): {check_std}")
print()

# Inverse matrices
T1_inv_std = T1_std - (q - q^(-1)) * I2
T2_inv_std = T2_std - (q - q^(-1)) * I2

# ── Evaluate braids in each representation ───────────────────────

def eval_braid_trivial(braid_ops):
    """Evaluate sequence of (matrix, is_inverse) in trivial rep."""
    result = R(1)
    for mat, inv in braid_ops:
        if inv:
            result *= q^(-1)  # T_inv in trivial rep
        else:
            result *= q       # T in trivial rep
    return result

def eval_braid_sign(braid_ops):
    """Evaluate in sign rep."""
    result = R(1)
    for mat, inv in braid_ops:
        if inv:
            result *= (-q)    # T_inv in sign rep: -q^{-1} - (q-q^{-1}) = -q
        else:
            result *= (-q^(-1))  # T in sign rep
    return result

def eval_braid_standard(braid_ops):
    """Evaluate in standard (2,1) rep."""
    result = I2
    for idx, inv in braid_ops:
        if idx == 1:
            mat = T1_inv_std if inv else T1_std
        else:
            mat = T2_inv_std if inv else T2_std
        result = result * mat
    return result

# Braid operations: (generator_index, is_inverse)
braid_ops = {
    "borr_4": [(1, False), (2, True), (1, False), (2, True)],
    "borr_6": [(1, False), (2, True), (1, False), (2, True), (1, False), (2, True)],
    "borr_sym": [(1, False), (2, True), (1, True), (2, False)],
}

print("Irrep evaluations (symbolic in q):")
print()
results = {}
for name, ops in braid_ops.items():
    triv = eval_braid_trivial(ops)
    sign = eval_braid_sign(ops)
    std_mat = eval_braid_standard(ops)
    std_tr = std_mat.trace()

    results[name] = {
        "trivial": str(triv),
        "sign": str(sign),
        "standard_trace": str(std_tr),
        "standard_matrix": str(std_mat),
    }

    print(f"  {name}:")
    print(f"    trivial     = {triv}")
    print(f"    sign        = {sign}")
    print(f"    std trace   = {std_tr}")
    print(f"    std matrix  = {std_mat}")
    print()

# ── Conversion operator analysis ────────────────────────────────
# Beta decay = single crossing change T_1 at the converting generator.
# For each Borromean braid, compute beta * T1 in all reps.
print("Conversion operator (braid * T1):")
print()
for name, ops in braid_ops.items():
    conv_ops = ops + [(1, False)]
    std_conv = eval_braid_standard(conv_ops)
    std_conv_tr = std_conv.trace()
    triv_conv = eval_braid_trivial(conv_ops)

    print(f"  {name} * T1:")
    print(f"    tr_std  = {std_conv_tr}")
    print(f"    tr_triv = {triv_conv}")
    print()

# ── Numerical evaluation ─────────────────────────────────────────
# Canonical q from Vol(4_1)/(m_μ/m_e):
VOL_41 = 2.029883212819307
MU_E   = 206.7682830
q_num  = 1.0 / (1.0 - sqrt(VOL_41 / MU_E))  # = 1.10997859...
print(f"Numerical evaluation at q = {q_num}:")
print()

g_A_candidates = {}
for name, ops in braid_ops.items():
    std_mat_num = eval_braid_standard(ops)
    std_tr_sym = std_mat_num.trace()
    std_tr_num = float(std_tr_sym.subs(q=q_num))
    triv_sym = eval_braid_trivial(ops)
    triv_num = float(triv_sym.subs(q=q_num))
    sign_sym = eval_braid_sign(ops)
    sign_num = float(sign_sym.subs(q=q_num))

    # Suppression factor: |tr_std / (2 * triv)|
    # The factor of 2 is the dimension of the standard rep
    if triv_num != 0:
        suppression = abs(std_tr_num / 2.0) / abs(triv_num)
        g_A_pred = (5.0/3.0) * suppression
    else:
        suppression = None
        g_A_pred = None

    g_A_candidates[name] = {
        "trivial": triv_num,
        "sign": sign_num,
        "std_trace": std_tr_num,
        "suppression": suppression,
        "g_A": g_A_pred,
    }

    print(f"  {name}:")
    print(f"    trivial  = {triv_num:.6f}")
    print(f"    sign     = {sign_num:.6f}")
    print(f"    std tr   = {std_tr_num:.6f}")
    if suppression is not None:
        print(f"    suppression = {suppression:.6f}")
        print(f"    g_A (5/3 x supp) = {g_A_pred:.4f}  (target: 1.2754)")
        print(f"    error = {abs(g_A_pred - 1.2754)/1.2754*100:.1f}%")
    print()

# ── T_{3,5} weak carrier dressing ─────────────────────────────────
# The upstream force-knot-identification.md identifies the weak force
# carrier as T_{3,5} with crossing number c_w = 10.  The weak vertex
# is not bare T_1 but T_1 dressed by the T_{3,5} structure.
#
# The EM coupling projection gives:
#   α = q^{-1} / ([9]_q · [10]_q)
# where [10]_q is the weak carrier complexity.
#
# By analogy, the weak vertex should be normalised by [c_w]_q = [10]_q:
#   g_A/g_V = (5/3) × (std suppression) × [10]_q correction
#
# Several hypotheses for how [10]_q enters:

def qint(n, qv=q_num):
    return (qv^n - qv^(-n)) / (qv - qv^(-1))

ten_q = qint(10, q_num)
nine_q = qint(9, q_num)

print("T_{3,5} weak carrier dressing:")
print(f"  [9]_q = {nine_q:.6f}")
print(f"  [10]_q = {ten_q:.6f}")
print(f"  [10]_q / [9]_q = {ten_q/nine_q:.6f}")
print()

# For the borr_4 braid (best candidate: suppression = 0.683):
borr4_supp = abs(float(eval_braid_standard(braid_ops["borr_4"]).trace().subs(q=q_num)) / 2.0)

dressing_hypotheses = {}
for name, factor in [
    ("bare (no dressing)", 1.0),
    ("× [10]_q/[9]_q", ten_q/nine_q),
    ("× [10]_q/([9]_q+1)", ten_q/(nine_q + 1)),
    ("× sqrt([10]_q/[9]_q)", (ten_q/nine_q)^0.5),
    ("× (1 + 1/[10]_q)", 1 + 1/ten_q),
    ("× [2]_q", qint(2, q_num)),
    ("× [3]_q/[2]_q", qint(3, q_num)/qint(2, q_num)),
]:
    g_A_dressed = (5.0/3.0) * borr4_supp * float(factor)
    err = abs(g_A_dressed - 1.2754)/1.2754*100
    dressing_hypotheses[name] = {"factor": float(factor),
                                  "g_A": g_A_dressed, "error_pct": err}
    print(f"  borr_4 {name:30s}: g_A = {g_A_dressed:.4f} (err {err:.1f}%)")

print()

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "sage-borromean-gA",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "sage_version": sage.version.version,
    "q": q_num,
    "target": {"g_A": 1.2754, "source": "PDG 2024"},
    "symbolic_results": results,
    "numerical_results": {k: {kk: (float(vv) if vv is not None else None)
                              for kk, vv in v.items()}
                         for k, v in g_A_candidates.items()},
    "T35_dressing": dressing_hypotheses,
}

import os
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "sage-borromean-gA.witness.json")
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print(f"Witness written to {out_path}")
