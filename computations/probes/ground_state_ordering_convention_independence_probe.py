#!/usr/bin/env python3
"""Is the `A = 5` ground-state-ordering refutation a fact about convention C?

Companion to `QOU.MassTheory.GroundStateOrderingRefutation` (bean `qou-cds1`,
convention-D migration).  That Lean file's readout was written with the Markov
parameter `z = sqrt(q)/(q+1)` (convention C), which the 2026-08-15 owner ruling
excises in favour of `z = q^3/(q^2+1)` (convention D).  This probe answers the
migration question **symbolically**, before any Lean is written:

    the refutation never uses z's formula.

Everything below is exact sympy in the symbols `(q, z, s)`, or mpmath at 60 dps
for the two anchor evaluations.  No float64 is created anywhere: `z` is carried
as a symbol until the very last substitution, and the anchor is read from the
50-digit proton `q0` string.

## What is checked (8 checks, all exact)

1. `c_+ + c_- = 1` identically in `(q, z)` -- the z-free normalisation.
2. The readout gap at `A = 5, Z = 1, N = 4` factors as

       gap  =  2 * c_+ * c_- * cMix^4 * (q^6 - 1) / q^3

   so for `q > 1` its sign is decided by `c_+ * c_- > 0` alone: nothing else in
   the comparison sees `z`.
3. `1 - (c_+ - c_-)^2 = 4 c_+ c_-`, the equivalent one-parameter form.
4. `c_+ c_- > 0  <=>  -1/q < z < q` (z strictly between the two eigenvalues
   `lambda_- = -1/q` and `lambda_+ = q` of the transfer matrix `S`).
5. + 6. Both conventions lie in that window for every `q > 1`.
7. The convention-C weights reproduce the committed `Anum/Bnum/K` of the Lean
   file under `q = t^2` -- i.e. the generalisation is faithful to what is there.
8. The sign hypothesis `hU` (the `sorted` readout at position 1 being
   non-negative, which is what turns the gap into an inequality between
   absolute values) holds at the proton anchor in both conventions.
"""

from __future__ import annotations

import sympy as sp
from mpmath import mp

mp.dps = 60

# Proton-pinned q0, 50 digits (AGENTS.md q0 anchor convention, ruling R2).
Q0_STR = "1.1099785827513808075916690"

q, z, t, s = sp.symbols("q z t s", positive=True)

# --- the readout -----------------------------------------------------------
# M_i = alpha*1 + beta*S with S = [[h,1],[1,0]], h = q - 1/q; S has eigenvalues
# lambda_+ = q, lambda_- = -1/q.  Since S[1][0] = 1 and S[1][1] = 0, the corpus
# readout Vhat = z*M[1][0] + M[1][1] = z*beta + alpha resolves to
#   Vhat = c_+ mu_+ + c_- mu_-,
#   c_+ = (z + 1/q)/(q + 1/q),   c_- = (q - z)/(q + 1/q).
cP = (z + 1 / q) / (q + 1 / q)
cM = (q - z) / (q + 1 / q)
cMix = (q + 1 / q) / 2  # the mixed (p-n) eigenfactor, z-free


def vhat(mu_p, mu_m):
    return cP * mu_p + cM * mu_m


# A = 5, Z = 1, N = 4.  Positions 2 and 3 see the same all-neutron suffix in
# both arrangements, so only positions 0 and 1 differ.
sortedV0 = vhat(cMix**4, cMix**4)                # p n n n n, position 0
sortedV1 = vhat(q**-3, -(q**3))                  # p n n n n, position 1
prescribedV0 = vhat(cMix * q**-3, cMix * q**3)   # n p n n n, position 0
prescribedV1 = vhat(cMix**3, -(cMix**3))         # n p n n n, position 1

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, bool(ok), detail))


# 1 -------------------------------------------------------------------------
check("c+ + c- = 1 identically in (q, z)", sp.simplify(cP + cM) == 1)

# 2 -------------------------------------------------------------------------
gap = sp.simplify(prescribedV0 * prescribedV1 - sortedV0 * sortedV1)
closed = 2 * cP * cM * cMix**4 * (q**6 - 1) / q**3
check(
    "gap = 2 c+ c- cMix^4 (q^6-1)/q^3",
    sp.simplify(gap - closed) == 0,
    f"gap = {sp.factor(gap)}",
)

# 3 -------------------------------------------------------------------------
u = sp.simplify(cP - cM)
check("1 - (c+ - c-)^2 = 4 c+ c-", sp.simplify(1 - u**2 - 4 * cP * cM) == 0)

# 4 -------------------------------------------------------------------------
# 4 c+ c- = 4q(q - z)(qz + 1)/(q^2+1)^2; for q > 0 the sign is that of
# (q - z)(qz + 1), i.e. positive exactly on -1/q < z < q.
check(
    "4 c+ c- = 4q(q-z)(qz+1)/(q^2+1)^2  =>  positive iff -1/q < z < q",
    sp.simplify(4 * cP * cM - 4 * q * (q - z) * (q * z + 1) / (q**2 + 1) ** 2) == 0,
)

# 5 -- convention C, in the substrate variable s = sqrt(q) --------------------
zC = sp.sqrt(q) / (q + 1)      # convention C (excised 2026-08-15)
# q - z_C = s*(s^3 + s - 1)/(s^2 + 1) at q = s^2, positive for every s > 0 with
# s^3 + s > 1 -- in particular for every s >= 1, i.e. every q >= 1.
gapC = sp.simplify((q - zC).subs(q, s**2) - s * (s**3 + s - 1) / (s**2 + 1))
check(
    "z_C < q for q > 1  (q - z_C = s(s^3+s-1)/(s^2+1) at q = s^2)",
    gapC == 0,
)

# 6 -- convention D ----------------------------------------------------------
zD = q**3 / (q**2 + 1)         # convention D (canonical)
check(
    "z_D < q for q > 0  (q - z_D = q/(q^2+1) > 0)",
    sp.simplify(q - zD - q / (q**2 + 1)) == 0,
)

# 7 -------------------------------------------------------------------------
# The committed Lean file states c_+ = Anum/K, c_- = Bnum/K at q = t^2.
Anum = t**3 + t**2 + 1
Bnum = t**6 + t**4 - t**3
K = (t**2 + 1) * (t**4 + 1)
cP_C_t = sp.simplify(cP.subs(z, zC).subs(q, t**2))
cM_C_t = sp.simplify(cM.subs(z, zC).subs(q, t**2))
check(
    "convention-C weights reproduce the committed Anum/Bnum/K at q = t^2",
    sp.simplify(cP_C_t - Anum / K) == 0 and sp.simplify(cM_C_t - Bnum / K) == 0,
)

# 8 -------------------------------------------------------------------------
hU = sp.simplify(sortedV1)  # = c_+/q^3 - c_- q^3
hU_C = sp.simplify(hU.subs(z, zC))
hU_D = sp.factor(sp.simplify(hU.subs(z, zD)))
# hU_D = (q^4 + 1 - q^6)/(q^3 (q^2+1)), so hU_D >= 0  <=>  q^6 <= q^4 + 1.
hU_D_form = sp.simplify(hU_D - (q**4 + 1 - q**6) / (q**3 * (q**2 + 1)))

Q0 = mp.mpf(Q0_STR)
anchor: dict[str, tuple] = {}
for name, zx in (("C", zC), ("D", zD)):
    f = sp.lambdify(q, [cP.subs(z, zx), cM.subs(z, zx), hU.subs(z, zx)], "mpmath")
    a, b, u_val = f(Q0)
    anchor[name] = (a, b, u_val)
check(
    "hU under convention D  <=>  q^6 <= q^4 + 1; both conventions give "
    "c+ > 0, c- > 0, hU >= 0 at the proton anchor",
    hU_D_form == 0 and all(a > 0 and b > 0 and v >= 0 for (a, b, v) in anchor.values()),
    f"hU_D = {hU_D}",
)

# --- report ----------------------------------------------------------------
print(__doc__.split("## What is checked")[0].strip())
print()
n_ok = sum(1 for _, ok, _ in results if ok)
for i, (name, ok, detail) in enumerate(results, 1):
    print(f"  [{i}] {'PASS' if ok else 'FAIL'}  {name}")
    if detail:
        print(f"        {detail}")
print(f"\n  {n_ok}/{len(results)} exact checks pass")

print("\n  gap factored:", sp.factor(gap))
print("  hU_C =", hU_C)
print("  hU_D =", hU_D)
print(f"\n  proton anchor q0 = {mp.nstr(Q0, 25)}")
for name in ("C", "D"):
    a, b, v = anchor[name]
    print(
        f"    convention {name}: c+ = {mp.nstr(a, 20)}  c- = {mp.nstr(b, 20)}"
        f"  c+c- = {mp.nstr(a * b, 12)}  hU = {mp.nstr(v, 12)}"
    )

for name, expr in (("C", hU_C), ("D", hU_D)):
    root = sp.nsolve(expr, q, sp.Rational(6, 5))
    print(f"    hU window, convention {name}:  1 < q < {sp.N(root, 12)}")

# `hU` is SUFFICIENT, not necessary: it is what turns the gap identity into an
# inequality between absolute values, and the conclusion outlives it.  The two
# windows below are the true reach of |sorted| < |prescribed| -- and they are
# why the audit's "1 < q <~ 1.22" for convention C is correct and must NOT be
# "corrected" to the hU window 1.13699..., which is a different quantity.
absgap = sp.Abs(prescribedV0 * prescribedV1) - sp.Abs(sortedV0 * sortedV1)
print()
for name, zx, guess in (("C", zC, sp.Rational(123, 100)), ("D", zD, sp.Rational(8, 5))):
    f = sp.lambdify(q, absgap.subs(z, zx), "mpmath")
    root = mp.findroot(f, mp.mpf(guess))
    print(f"    conclusion window, convention {name}:  1 < q < {mp.nstr(root, 12)}")

raise SystemExit(0 if n_ok == len(results) else 1)
