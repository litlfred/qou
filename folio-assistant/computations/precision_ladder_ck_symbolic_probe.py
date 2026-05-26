#!/usr/bin/env python3
"""
Precision-ladder c_k pattern analysis + generating-function probe.

Reads known c_k values from the Q_β witness and canonical forms,
then searches for a closed-form generating function F(z) whose
Taylor coefficients reproduce c_k.

Goal: canonical/symbolic derivation of c_6+ for 1 ppQ precision.
"""
from mpmath import mpf, mp, fabs, sqrt
mp.dps = 60

import json, os, sys

COMP = os.path.dirname(__file__)

def load_witness(name):
    with open(os.path.join(COMP, name)) as f:
        return json.load(f)

# ── Load substrate data ──────────────────────────────────────────
w = load_witness("q-beta-operator-valued-N3.witness.json")
d = w["data"]

q0 = mpf(str(d["q_0_50dps"]))
Q_A = mpf(str(d["Q_A"]))
Q_N1 = mpf(str(d["Q_N1"]))
Q_N2 = mpf(str(d["Q_N2"]))
Q_AME = mpf(str(d["Q_AME"]))
b = mpf(str(d["hoefsmit_b"]))
hbar_sq = mpf(str(d["hbar_q_sq"]))
h = q0 - q0**(-1)                   # Hecke amplitude
z = sqrt(q0) / (q0 + 1)             # Markov trace param

# CODATA Q_β from witness (not hardcoded)
Q_codata = Q_AME

print("=" * 70)
print("PRECISION LADDER c_k PATTERN ANALYSIS")
print("=" * 70)
print(f"q₀       = {q0}")
print(f"b        = {b}")
print(f"ℏ_q²     = {hbar_sq}")
print(f"h        = {h}")
print(f"Q_A      = {Q_A}")
print()

# ── Extract exact c_k by inverting the recursion ─────────────────
# Q_{k+1} = Q_k · (1 + c_k · b^k · ℏ_q^{2k})
# => c_k = (Q_{k+1}/Q_k - 1) / (b^k · ℏ_q^{2k})

# c_2: Q_N2 = Q_N1 · (1 + c_2 · b² · ℏ_q⁴)
c2_exact = (Q_N2 / Q_N1 - 1) / (b**2 * hbar_sq**2)
print(f"c₂ exact = {float(c2_exact):.10f}")
print(f"   canonical form: -1  match: {float(fabs(c2_exact - (-1))):.4e}")

# c_3: extracted from witness (empirical additive form)
c3_exact = mpf(str(d["c_3_empirical_additive"]))
Q_N3 = Q_N2 * (1 + c3_exact * b**3 * hbar_sq**3)
print(f"c₃ exact = {float(c3_exact):.10f}")
print(f"   canonical form: J_Hopf(q=1) = -2  match: {float(fabs(c3_exact - (-2))):.4e}")

# For c_4+, we need Q_N4, Q_N5, etc. These aren't in the witness directly.
# We need to compute Q at each rung using the CODATA value and work backwards,
# or compute Q_β from scratch using the matrix trace.
#
# Alternative: use the witness's empirical c_k values if available.
print()
print("=" * 70)
print("GENERATING FUNCTION ANALYSIS")
print("=" * 70)

# Known c_k values (from audit doc)
c_known = {
    2: mpf("-1"),
    3: mpf("-2"),                    # J_Hopf(q=1)
    4: -2 * b**4,                    # c_3 · b⁴
    5: mpf("4") * 3 + b,            # c_3² · 3 + b = 12 + b
    6: mpf("4") * b**2,             # c_3² · b²
    7: mpf("-8"),                    # c_3³
}

print("\nc_k values (canonical forms):")
for k in sorted(c_known.keys()):
    print(f"  c_{k} = {float(c_known[k]):+.8f}")

# ── Look for F(z) = Σ c_k z^k ───────────────────────────────────
# Test: is F(z) = A/(1 - B·z) + C/(1 - D·z) + ... (rational)?
# If c_k = a·r^k + b·s^k + ..., then c_k follows a linear recurrence.

# Build the c_k sequence as a vector
ck_seq = [float(c_known[k]) for k in range(2, 8)]
print(f"\nc_k sequence (k=2..7): {ck_seq}")

# Check if a linear recurrence of order 2 fits: c_{k+2} = p·c_{k+1} + q·c_k
print("\nLinear recurrence search (c_{k+2} = p·c_{k+1} + q·c_k):")
for start in range(len(ck_seq) - 3):
    a0, a1, a2, a3 = ck_seq[start:start+4]
    # a2 = p*a1 + q*a0, a3 = p*a2 + q*a1
    # Solve: [a1, a0; a2, a1] [p; q] = [a2; a3]
    det = a1*a1 - a2*a0
    if abs(det) > 1e-10:
        p = (a1*a2 - a0*a3) / det
        q = (a1*a3 - a2*a2) / det
        # Test on remaining terms
        pred = p * ck_seq[start+2] + q * ck_seq[start+1]
        actual = ck_seq[start+3] if start+3 < len(ck_seq) else None
        print(f"  start=c_{start+2}: p={p:.4f}, q={q:.4f}, "
              f"pred c_{start+5}={pred:.4f}" +
              (f" vs {actual:.4f} ({abs(pred-actual)/abs(actual)*100:.1f}%)" if actual else ""))

# ── Symbolic structure: look at c_k as function of c_3 and b ─────
c3 = mpf(-2)
print("\n\nStructural decomposition (in terms of c₃=-2 and b):")
print(f"  c₂ = {float(c_known[2]):+.4f} = -1")
print(f"  c₃ = {float(c_known[3]):+.4f} = c₃ = J_Hopf(q=1)")
print(f"  c₄ = {float(c_known[4]):+.8f} = c₃·b⁴ = {float(c3*b**4):+.8f}")
print(f"  c₅ = {float(c_known[5]):+.8f} = c₃²·3+b = {float(c3**2*3+b):+.8f}")
print(f"  c₆ = {float(c_known[6]):+.8f} = c₃²·b² = {float(c3**2*b**2):+.8f}")
print(f"  c₇ = {float(c_known[7]):+.4f} = c₃³ = {float(c3**3):.4f}")
print()

# Power analysis: what power of c₃ and b appears at each rung?
print("Power analysis:")
print("  k  c₃^a  b^c  coeff  →  c_k = coeff · c₃^a · b^c")
decomp = [
    (2, 0, 0, -1,    "convention"),
    (3, 1, 0, 1,     "J_Hopf"),
    (4, 1, 4, 1,     "Jones·Kashiwara"),
    (5, 2, 0, 3,     "Jones²·3 + b (mixed)"),
    (6, 2, 2, 1,     "Jones²·Kashiwara"),
    (7, 3, 0, 1,     "Jones³"),
]
for k, a, c, coeff, label in decomp:
    val = coeff * c3**a * b**c if k != 5 else c3**2 * 3 + b
    print(f"  {k}  {a:4d}  {c:4d}  {coeff:+4d}  →  {float(val):+.6f}  ({label})")

# ── Key observation ──────────────────────────────────────────────
print("\n" + "=" * 70)
print("KEY OBSERVATION: alternating pure-Jones and mixed rungs")
print("=" * 70)
print("""
k=3: c₃¹ · b⁰  = pure Jones (−2)
k=4: c₃¹ · b⁴  = Jones × Kashiwara⁴
k=5: c₃² · 3 + b = Jones² × 3 + Kashiwara¹  (MIXED SUM)
k=6: c₃² · b²  = Jones² × Kashiwara²
k=7: c₃³ · b⁰  = pure Jones cubed (−8)

Pattern:
  odd k:  pure Jones power (c₃^{(k-1)/2} at k=3,7) or mixed sum (k=5)
  even k: Jones × Kashiwara power

Proposed generating function (conjectural):
  F(z) = 1/(1 − c₃·z³) · 1/(1 − b²·z²) · (correction terms)

This is a TWO-VARIABLE product:
  - geometric series in c₃·z³ → rungs 3, 6(=2×3), 7(≈3+4)...
  - geometric series in b²·z² → rungs 4, 6(=2+4)...
""")

# ── Test the two-variable product hypothesis ─────────────────────
# F(z) = Σ_{j≥0} Σ_{m≥0} (c₃)^j · (b²)^m · z^{3j+2m} · f(j,m)
# where f(j,m) is a combinatorial multiplicity
print("Two-variable decomposition test:")
print("  c_k = Σ over (j,m) with 3j+2m = k")
for k in range(2, 10):
    terms = []
    for j in range(k//3 + 1):
        rem = k - 3*j
        if rem >= 0 and rem % 2 == 0:
            m = rem // 2
            val = c3**j * b**(2*m)
            terms.append((j, m, float(val)))
    print(f"  k={k}: ", end="")
    for j, m, v in terms:
        print(f"c₃^{j}·b^{2*m}={v:+.4f}  ", end="")
    print()
    if k in c_known:
        total = sum(v for _, _, v in terms)
        print(f"       sum={total:+.4f}  actual c_{k}={float(c_known[k]):+.4f}  "
              f"ratio={float(c_known[k])/total:.4f}" if total != 0 else "")

print("\n\nDone. See output for generating-function candidates.")
