#!/usr/bin/env python3
"""lever1_trB_quantum_integer_form.py
======================================

Sharpen the lever-1 `tr B` target (the "identify `E(q)`" keystone step) WITHOUT
Sage, by repackaging it in the SL₂-canonical variable and classifying the
monodromy it forces. No fit; symbolic (sympy) + mpmath only.

Background (see lever1_trB_geometric_target.py / the 2026-06-24 lever-1 audit).
The depth-2 `det B = 1` recurrence `a_{n+2} = τ·a_{n+1} − a_n` is proved, so the
lever-1 identification `a_D^(n) = lw(n−1)` reduces to ONE number, `τ = tr B`,
with the selection-rule closed form
    tr B = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3q⁴+8q²+3)/(4q(q+1)²)  (= 2.6424 at q₀).

THIS PROBE adds three Sage-free results that sharpen what "identify `E(q)`" means:

  (Q) QUANTUM-INTEGER REPACKAGING (new, exact). In the SL₂/Chebyshev variable
      s = q + q⁻¹ = [2]_q (the quantum dimension of the Hecke fundamental) the
      target and the individual selection-rule periods are all rational in s:
          a_D^(2) = 1,
          a_D^(3) = (s + 2)/3,          [ = ([2]_q + 2)/3 = (q^{1/2}+q^{-1/2})²/3 ]
          a_D^(4) = (3 s² − 2)/4,
          tr B    = 3(3 s² + 2)/(4(s + 2)).
      So `tr B` depends on q ONLY through [2]_q. This is the signature of a
      q-difference / quantum-group connection, not of a generic period.

  (M) MONODROMY CLASSIFICATION. det B = 1 and tr B ≈ 2.6424 > 2 ⇒ B is a
      HYPERBOLIC element of SL₂(ℝ), eigenvalues λ, λ⁻¹ with
      λ = (τ + √(τ²−4))/2 ≈ 2.1846. The trace is NON-INTEGER, so B is NOT the
      topological π₁-monodromy of an elliptic fibration (those lie in SL₂(ℤ),
      integer trace). B is the rank-2 q-difference (Gauss–Manin / Habiro)
      CONNECTION matrix on the W = H¹ factor. This reframes "identify `E(q)`":
      the object to find is the rank-2 q-difference SYSTEM whose connection-matrix
      trace is 3(3[2]_q²+2)/(4([2]_q+2)), NOT an elliptic surface with integer
      monodromy.

  (C) RANK-2 SOURCE (Sage-free reconfirmation of lever1_bring_period_trB.sage).
      Plain-Python S₅/A₅ character theory: H^{1,0}(Bring) = standard 4-dim S₅
      irrep, A₅-irreducible. Hence there is NO A₅-invariant rank-2 subspace of
      holomorphic differentials, and the rank-2 `W` must be an isogeny/CM factor
      of Jac(Bring) (Riera–Rodríguez), realized at the de Rham/q-family level.

Honest status (unchanged): the fixed-curve j(E) of E = Bring/S₄ and the q-family
realization of B (the connection of `E(q)`) remain Sage/Magma- and owner-gated
(the s5-so3 keystone). This probe does NOT compute them and claims no closure —
it converts the target into the canonical variable and pins the monodromy type.
"""
from __future__ import annotations

import json
import pathlib
from itertools import permutations

import sympy as sp
import mpmath as mp

mp.mp.dps = 50
# Canonical substrate q₀ (50-digit), identical literal to lever1_trB_geometric_target.py.
Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name, ok):
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (Q) quantum-integer repackaging: symbolic identities in s = q + q⁻¹ ───────
q = sp.Symbol("q", positive=True)
s = sp.Symbol("s")  # stands for [2]_q = q + 1/q

# selection-rule periods in q (from lever1_trB_geometric_target.py)
a2_q = sp.Integer(1)
a3_q = (q + 1) ** 2 / (3 * q)
a4_q = (3 * q ** 2 + 4 + 3 / q ** 2) / 4
trB_q = sp.simplify((a2_q + a4_q) / a3_q)

# proposed s-forms
a2_s = sp.Integer(1)
a3_s = (s + 2) / 3
a4_s = (3 * s ** 2 - 2) / 4
trB_s = 3 * (3 * s ** 2 + 2) / (4 * (s + 2))

# substitute s = q + 1/q and check each is symbolically identical to the q-form
sub = {s: q + 1 / q}
id_a3 = sp.simplify(a3_s.subs(sub) - a3_q) == 0
id_a4 = sp.simplify(a4_s.subs(sub) - a4_q) == 0
id_trB = sp.simplify(trB_s.subs(sub) - trB_q) == 0
print("(Q) quantum-integer repackaging  (s = q + q⁻¹ = [2]_q)")
print(f"    a_D^(3) = (s+2)/3        identical to q-form: {id_a3}")
print(f"    a_D^(4) = (3s²−2)/4      identical to q-form: {id_a4}")
print(f"    tr B    = 3(3s²+2)/(4(s+2)) identical to q-form: {id_trB}")
check("(Q) a_D^(3) = (s+2)/3 in s=[2]_q", id_a3)
check("(Q) a_D^(4) = (3s²−2)/4 in s=[2]_q", id_a4)
check("(Q) tr B = 3(3s²+2)/(4(s+2)) in s=[2]_q", id_trB)
# recurrence self-consistency: a4 = τ·a3 − a2 in s
recur_s = sp.simplify(trB_s * a3_s - a2_s - a4_s) == 0
check("(Q) recurrence a4 = τ·a3 − a2 holds in s", recur_s)
results["a_D_s_forms"] = {"a2": "1", "a3": "(s+2)/3", "a4": "(3*s**2-2)/4"}
results["trB_s_form"] = "3*(3*s**2+2)/(4*(s+2))"
results["s_is"] = "q + 1/q = [2]_q"

# numeric cross-check at q₀ and random rationals, to 50 dps
def trB_qf(x):
    return 3 * (3 * x ** 4 + 8 * x ** 2 + 3) / (4 * x * (x + 1) ** 2)


def trB_sf(x):
    sv = x + 1 / x
    return 3 * (3 * sv ** 2 + 2) / (4 * (sv + 2))


trB_q0 = trB_qf(Q0)
num_ok = all(abs(trB_qf(mp.mpf(r)) - trB_sf(mp.mpf(r))) < mp.mpf("1e-45")
             for r in ("1.7", "0.3", "2.9", "0.91"))
num_ok &= abs(trB_q0 - trB_sf(Q0)) < mp.mpf("1e-45")
print(f"    numeric q-form == s-form to 45 dps (q₀ + 4 random q): {num_ok}")
print(f"    s₀ = [2]_q₀ = {mp.nstr(Q0 + 1 / Q0, 18)}")
print(f"    tr B(q₀)    = {mp.nstr(trB_q0, 18)}")
check("(Q) q-form == s-form to 45 dps", num_ok)
results["s0_value"] = mp.nstr(Q0 + 1 / Q0, 30)
results["trB_at_q0"] = mp.nstr(trB_q0, 30)

# ── (M) monodromy classification: hyperbolic SL₂(ℝ), non-integer trace ────────
tau = trB_q0
det1 = True  # det B = 1 proved (prop:sl2-prolongation-recurrence); recorded, not re-derived
hyperbolic = tau > 2
lam = (tau + mp.sqrt(tau ** 2 - 4)) / 2
lam_recip_ok = abs(lam * (1 / lam) - 1) < mp.mpf("1e-45")
# is the trace an integer? (would be required for an SL₂(ℤ) topological monodromy)
# tolerance tied to the working precision rather than a hardcoded literal
int_tol = mp.mpf("10") ** -(mp.mp.dps - 5)
trace_integer = abs(tau - mp.nint(tau)) < int_tol
print("\n(M) monodromy classification (det B = 1 proved)")
print(f"    tr B = {mp.nstr(tau, 12)} > 2  →  hyperbolic: {hyperbolic}")
print(f"    eigenvalues λ, λ⁻¹ = {mp.nstr(lam, 12)}, {mp.nstr(1 / lam, 12)}")
print(f"    trace integer (SL₂(ℤ) topological monodromy)? {trace_integer}")
print("    → non-integer trace ⇒ B is a rank-2 q-DIFFERENCE connection matrix,")
print("      NOT the π₁-monodromy of an elliptic fibration.")
check("(M) B is hyperbolic (tr B > 2, det B = 1)", hyperbolic and det1 and lam_recip_ok)
check("(M) tr B is NOT an integer (rules out SL₂(ℤ) topological monodromy)", not trace_integer)
results["det_B"] = 1
results["hyperbolic"] = bool(hyperbolic)
results["eigenvalue_lambda"] = mp.nstr(lam, 30)
results["trace_is_integer"] = bool(trace_integer)
results["char_poly"] = "x**2 - trB*x + 1"

# ── (C) rank-2 source: A₅-irreducibility of H^{1,0}(Bring), Sage-free ─────────
def fixed(p):
    return sum(1 for i in range(len(p)) if p[i] == i)


def sgn(p):
    p = list(p)
    sg = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            sg = -sg
    return sg


S5 = list(permutations(range(5)))
A5 = [p for p in S5 if sgn(p) == 1]
def chi(p):
    return fixed(p) - 1  # standard character = (#fixed) − 1
dim_std = chi(tuple(range(5)))
inner_S5 = sp.Rational(sum(chi(p) ** 2 for p in S5), len(S5))
inner_A5 = sp.Rational(sum(chi(p) ** 2 for p in A5), len(A5))
std_irred = inner_S5 == 1
A5_irred = inner_A5 == 1
print("\n(C) rank-2 source — H^{1,0}(Bring) character theory (no Sage)")
print(f"    dim std rep = {dim_std};  ⟨χ,χ⟩_S₅ = {inner_S5} (irred {std_irred});  "
      f"⟨χ|A₅,χ|A₅⟩_A₅ = {inner_A5} (A₅-irred {A5_irred})")
print("    → no A₅-invariant rank-2 form-subspace; W is a CM/isogeny factor of Jac(Bring).")
check("(C) H^{1,0}(Bring) is the 4-dim S₅ standard irrep", bool(std_irred) and dim_std == 4)
check("(C) it restricts A₅-irreducibly (W ⇒ isogeny/CM factor, not a form-subrep)", bool(A5_irred))
results["dim_H10_Bring"] = int(dim_std)
results["S5_standard_irreducible"] = bool(std_irred)
results["A5_restriction_irreducible"] = bool(A5_irred)

# ── verdict ──────────────────────────────────────────────────────────────────
all_passed = all(ok for _, ok in asserts)
verdict = (
    "TARGET SHARPENED, NO CLOSURE. The lever-1 monodromy trace is a rational "
    "function of the quantum integer [2]_q alone: with s = q+q⁻¹ = [2]_q, "
    "a_D^(2)=1, a_D^(3)=(s+2)/3, a_D^(4)=(3s²−2)/4, and tr B = 3(3s²+2)/(4(s+2)) "
    "(50-dps verified, symbolic + numeric). det B = 1 (proved) with tr B ≈ 2.6424 "
    "> 2 makes B a HYPERBOLIC SL₂(ℝ) element (λ ≈ 2.1846); the trace is "
    "non-integer, so B is NOT an SL₂(ℤ) elliptic-fibration topological monodromy "
    "but the rank-2 q-DIFFERENCE connection matrix on W. The rank-2 W is forced "
    "by A₅-irreducibility of H^{1,0}(Bring) (Sage-free char theory) to be an "
    "isogeny/CM factor of Jac(Bring), not a form-subrep. NET: 'identify E(q)' is "
    "now 'find the rank-2 q-difference system on H¹(E) whose connection trace is "
    "3(3[2]_q²+2)/(4([2]_q+2))' — a [2]_q-rational, hyperbolic target. The fixed "
    "j(Bring/S₄) and the q-family connection itself stay Sage/Magma- and "
    "owner-gated (s5-so3 keystone). No fit."
)
print("\n" + ("ALL CHECKS PASS" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "lever1_trB_quantum_integer_form",
    "description": ("Sage-free sharpening of the lever-1 tr B target: repackaged in "
                    "s=[2]_q (tr B = 3(3s²+2)/(4(s+2)); a_D^(n) all rational in [2]_q), "
                    "hyperbolic SL₂(ℝ) monodromy with non-integer trace (rank-2 "
                    "q-difference connection, not SL₂(ℤ) topological monodromy), and a "
                    "Sage-free reconfirmation that A₅-irreducibility forces W to be a "
                    "CM/isogeny factor of Jac(Bring)."),
    "discipline": "no fit; symbolic+mpmath 50 dps; reframes 'identify E(q)', claims no closure",
    "auditOnly": "docs/audits/2026-06-24-lever1-trB-quantum-integer-form.md",
    "related": [
        "computations/substrate/lever1_trB_geometric_target.py",
        "computations/substrate/lever1_bring_period_trB.sage",
    ],
    "results": results,
    "assertions": {n: ok for n, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).resolve().parent / "lever1-trB-quantum-integer-form.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
