#!/usr/bin/env sage
"""
g_A from the Iwahori-Hecke algebra H_3(q) — Sage computation.

The axial coupling g_A of the nucleon is computed from the Hecke
algebra of the 3-quark (Borromean) braid.

Hecke relation: (T - q)(T + q^{-1}) = 0
Equivalently:   T - T^{-1} = (q - q^{-1})  [= Skein relation]

Eigenvalues of T:  q (symmetric/vector)  and  -q^{-1} (antisymmetric/axial)

The computation:
  1. Build the Iwahori-Hecke algebra H_3(q) over Q(q)
  2. Construct the Borromean braid element in the T-basis
  3. Compute the Markov trace in each irrep (trivial, sign, standard)
  4. Extract g_A from the standard (2,1) representation trace
  5. Evaluate at q = 1.110

Convention: q is the ONLY polynomial variable.  Never use t, A, or
other variables for the Jones polynomial.  The Jones polynomial of
a link L is J_L(q) = tr_M(rho(beta_L)), the Markov trace of the
braid representation in H_n(q).

Run from repo root:
    sage folio-assistant/computations/sage-borromean-gA.sage

Output:
    folio-assistant/computations/sage-borromean-gA.witness.json

Target: g_A = 1.2754 ± 0.0013 (PDG 2024)
"""

import json
from datetime import datetime, timezone

print("=" * 60)
print("g_A from Iwahori-Hecke algebra H_3(q)")
print("=" * 60)
print()

# ── Setup: Hecke algebra H_3(q) over Q(q) ───────────────────────
# Sage convention: IwahoriHeckeAlgebra of type A_2 gives H_3(q)
# with generators T_1, T_2 satisfying:
#   T_i^2 = (q - q^{-1}) T_i + 1
#   T_1 T_2 T_1 = T_2 T_1 T_2

R = LaurentPolynomialRing(QQ, 'q')
q = R.gen()
W = WeylGroup(['A', 2], prefix='s')
H = IwahoriHeckeAlgebra(W, q, -q**(-1), base_ring=R)

# T-basis (Hecke generators)
T = H.T()
T1 = T.an_element().parent().algebra_generators()[W.simple_reflections()[1]]
T2 = T.an_element().parent().algebra_generators()[W.simple_reflections()[2]]

print(f"Hecke algebra H_3(q) constructed")
print(f"  Relation: T^2 = (q - q^{{-1}}) T + 1")
print(f"  Eigenvalues of T: q and -q^{{-1}}")
print()

# ── Verify the Hecke relation ────────────────────────────────────
check = T1 * T1 - (q - q**(-1)) * T1
print(f"T1^2 - (q - q^{{-1}}) T1 = {check}")
# Should be the identity element
print()

# ── Borromean braid candidates in H_3(q) ────────────────────────
# The nucleon (proton/neutron) is a Borromean link of 3 quarks.
# In H_3(q), Borromean-type elements alternate T_1 and T_2^{-1}:

# T_i^{-1} = T_i - (q - q^{-1})  [from Hecke relation]
T1_inv = T1 - (q - q**(-1)) * T.one()
T2_inv = T2 - (q - q**(-1)) * T.one()

braids = {
    "borr_4": T1 * T2_inv * T1 * T2_inv,
    "borr_6": T1 * T2_inv * T1 * T2_inv * T1 * T2_inv,
    "borr_sym": T1 * T2_inv * T1_inv * T2,
}

print("Borromean braid elements in T-basis:")
for name, b in braids.items():
    print(f"  {name} = {b}")
print()

# ── Markov trace ─────────────────────────────────────────────────
# The Markov trace on H_3(q) is:
#   tr_M(1) = 1
#   tr_M(T_i) = z  where z = (q-1)/(q^{1/2}+q^{-1/2})^2
#   tr_M(ab) = tr_M(ba)  (trace property)
#
# For H_3(q), the T-basis elements are:
#   {1, T_1, T_2, T_1 T_2, T_2 T_1, T_1 T_2 T_1}
# and the Markov trace of each basis element is determined by
# the Markov property.
#
# Sage's IwahoriHeckeAlgebra can compute this via the
# Kazhdan-Lusztig basis and character theory.

# ── Irreducible representations of H_3(q) ───────────────────────
# Partitions of 3:  (3), (2,1), (1,1,1)
# dims:              1,    2,     1
#
# (3) = trivial rep: T_i -> q  (vector channel)
# (1,1,1) = sign rep: T_i -> -q^{-1}  (fully antisymmetric)
# (2,1) = standard rep: 2-dimensional (mixed/axial channel)
#
# We evaluate each braid in all 3 irreps.

# Trivial rep: T_i -> q (scalar)
def eval_trivial(element):
    """Evaluate in trivial rep: replace every T_i with q."""
    # In trivial rep, every T_w -> q^{length(w)}
    result = R(0)
    for w, coeff in element:
        result += coeff * q**(w.length())
    return result

# Sign rep: T_i -> -q^{-1} (scalar)
def eval_sign(element):
    """Evaluate in sign rep: replace every T_i with -q^{-1}."""
    result = R(0)
    for w, coeff in element:
        result += coeff * (-q**(-1))**(w.length())
    return result

# Standard (2,1) rep: 2x2 matrices
# T_1 -> [[q, 0], [1, -q^{-1}]]
# T_2 -> [[-q^{-1}, q-q^{-1}], [0, q]]
def eval_standard(element):
    """Evaluate in standard (2,1) representation (2x2 matrices over Q(q))."""
    M = MatrixSpace(R.fraction_field(), 2)
    T1_mat = M([[q, 0], [1, -q**(-1)]])
    T2_mat = M([[-q**(-1), q - q**(-1)], [0, q]])
    I2 = M.identity_matrix()

    result = M.zero()
    s1 = W.simple_reflections()[1]
    s2 = W.simple_reflections()[2]

    for w, coeff in element:
        # Decompose w into a product of s1, s2
        mat = I2
        for s in w.reduced_word():
            if s == 1:
                mat = mat * T1_mat
            elif s == 2:
                mat = mat * T2_mat
        result += coeff * mat
    return result

# ── Evaluate all braids ──────────────────────────────────────────
print("Irrep evaluations (symbolic in q):")
print()

results = {}
for name, braid in braids.items():
    triv = eval_trivial(braid)
    sign = eval_sign(braid)
    std_mat = eval_standard(braid)
    std_trace = std_mat.trace()

    results[name] = {
        "trivial": str(triv),
        "sign": str(sign),
        "standard_trace": str(std_trace),
        "standard_matrix": str(std_mat),
    }

    print(f"  {name}:")
    print(f"    trivial (vector):    {triv}")
    print(f"    sign:                {sign}")
    print(f"    standard trace:      {std_trace}")
    print()

# ── Conversion operator ──────────────────────────────────────────
# Beta decay changes one quark at strand 1: the conversion operator
# is T_1 (a single crossing change).
# The axial coupling involves the ratio:
#   g_A/g_V = tr_standard(beta * T_1) / tr_trivial(beta * T_1)
# for the Borromean braid beta.

print("Conversion operator (T_1 acting on Borromean state):")
print()

g_A_results = {}
for name, braid in braids.items():
    conv = braid * T1
    triv = eval_trivial(conv)
    std_mat = eval_standard(conv)
    std_trace = std_mat.trace()

    # Also compute the bare T_1 (no Borromean structure)
    bare_triv = eval_trivial(T1)
    bare_std = eval_standard(T1).trace()

    # Ratio (symbolic)
    # g_A/g_V involves comparing the standard trace to trivial trace
    # normalized by the bare values
    ratio_std = std_trace / bare_std if bare_std != 0 else None
    ratio_triv = triv / bare_triv if bare_triv != 0 else None

    g_A_results[name] = {
        "conv_trivial": str(triv),
        "conv_standard_trace": str(std_trace),
        "bare_trivial": str(bare_triv),
        "bare_standard_trace": str(bare_std),
        "ratio_std": str(ratio_std) if ratio_std else "N/A",
        "ratio_triv": str(ratio_triv) if ratio_triv else "N/A",
    }

    print(f"  {name} * T_1:")
    print(f"    tr_triv(beta * T_1) = {triv}")
    print(f"    tr_std(beta * T_1)  = {std_trace}")
    print(f"    bare tr_triv(T_1)   = {bare_triv}")
    print(f"    bare tr_std(T_1)    = {bare_std}")
    print()

# ── Numerical evaluation at q = 1.110 ───────────────────────────
q_num = 1.110
print(f"Numerical evaluation at q = {q_num}:")
print()

for name, braid in braids.items():
    triv_val = float(eval_trivial(braid).subs(q=q_num))
    sign_val = float(eval_sign(braid).subs(q=q_num))
    std_trace_val = float(eval_standard(braid).trace().subs(q=q_num))

    conv = braid * T1
    conv_triv_val = float(eval_trivial(conv).subs(q=q_num))
    conv_std_val = float(eval_standard(conv).trace().subs(q=q_num))

    print(f"  {name}:")
    print(f"    trivial  = {triv_val:.6f}")
    print(f"    sign     = {sign_val:.6f}")
    print(f"    standard = {std_trace_val:.6f}")
    print(f"    conv_triv = {conv_triv_val:.6f}")
    print(f"    conv_std  = {conv_std_val:.6f}")

    # Naive quark model: g_A = 5/3
    # Borromean suppression: multiply by |std_trace/2| / |triv|
    if triv_val != 0:
        suppression = abs(std_trace_val / 2.0) / abs(triv_val)
        g_A_pred = (5.0/3.0) * suppression
        print(f"    suppression = {suppression:.6f}")
        print(f"    g_A (5/3 × suppression) = {g_A_pred:.4f}")
    print()

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "sage-borromean-gA",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "sage_version": str(version()),
    "description": (
        "g_A from Iwahori-Hecke algebra H_3(q). "
        "Hecke relation: (T-q)(T+q^{-1})=0. "
        "Skein relation: T - T^{-1} = (q-q^{-1}). "
        "Eigenvalues: q (vector) and -q^{-1} (axial)."
    ),
    "target": {"g_A": 1.2754, "source": "PDG 2024"},
    "q": q_num,
    "irrep_evaluations": results,
    "conversion_operator": g_A_results,
}

import os
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "sage-borromean-gA.witness.json")
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print(f"\nWitness written to {out_path}")
print(f"Target: g_A = 1.2754")
