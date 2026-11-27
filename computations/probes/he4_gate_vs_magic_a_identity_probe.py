#!/usr/bin/env python3
"""
Probe — is `E₀·ln(1/W_λ)` = `2·m_e·A·8G` at ⁴He an IDENTITY, or a coincidence?

Two parameter-free routes land on ⁴He's binding within 0.11 % of EACH OTHER while
both miss experiment by ~+5.9 %:

    SU(4) occupancy gate   E₀·ln(1/W_(3,3,3,3))(q₀) = 29.9897 MeV
    magic-A volume form    2·m_e·A·8G               = 29.9557 MeV     (A = 4)
    B_AME(⁴He)                                       = 28.2957 MeV

Nothing in the corpus connects them (grepped 2026-08-10: no file mentions both
`E_gate`/`ln(1/W` and `8G`/`magic-A`). That closeness admits three readings, and
they have very different consequences:

  (i)  an IDENTITY waiting to be proved — a Plancherel weight equal to a
       hyperbolic volume is exactly the Kashaev volume-conjecture shape the corpus
       already carries as `conj:kashaev-volume-conjecture`. That would be a result.
  (ii) the SAME OBJECT in disguise — then this is ONE near-match reported twice,
       the shared +5.9 % is its systematic error, and the framework has one ⁴He
       data point, not two independent ones.
  (iii) a COINCIDENCE — the two functions merely cross near q₀.

The test that separates them is cheap and decisive, and is the standard
anti-numerology move: **an identity holds as a function of q; a coincidence holds
only at a point.** So evaluate both sides across q, and across A.

RESULT — (iii). Both (i) and (ii) are refuted:

  * NOT an identity in q. The ratio sweeps monotonically from 6.43 at q = 1.02 to
    0.061 at q = 1.50, crossing 1 transversally (slope −337 MeV per unit q) at
        q* = 1.110080045251   vs   q₀ = 1.109978582751
    i.e. 91.4 ppm apart. The crossing is not even AT q₀.
  * NOT structural in A. Ratio = 0.613, 0.707, **1.0011**, 0.654, 0.511 for
    A = 2, 3, 4, 6, 7. It works at A = 4 and nowhere else.

And the crossing is guaranteed a priori, which is what makes it weak evidence:
`E₀(q)·ln(1/W_λ(q))` decreases monotonically from +∞ toward 0 while `2·m_e·A·8G`
is a constant in q, so the two MUST cross exactly once. The only content in the
"agreement" is WHERE. Given the −337 MeV/unit slope, the 0.034 MeV closeness is
precisely the statement "q* lies within 1e-4 of q₀" — and it does, at 1.0e-4. The
0.11 % figure carries no information beyond that.

Scope. This refutes the IDENTITY claim `E₀·ln(1/W_λ(q)) ≡ 2·m_e·A·8G`, which a
single failing q would already do and which fails at every q tested but one — that
much is a structural exclusion of the *identity*, not a scope-(a) hedge. It does
NOT touch either form's standing as a parameter-free ⁴He near-match: both still
land ⁴He at +5.9 % with no fit, and both remain live under §5 of the L2 audit.
What it does remove is the inference that they CORROBORATE each other. They do not
— they are two unrelated functions that happen to cross near the substrate point.

NO WITNESS — deliberately, for the same reason as
`l2_light_isotope_error_attribution_probe.py`: every input descends from
`mass_binding_dashboard._constants()` / `W_lambda_float`, an f64 display pipeline,
so a witness would enshrine raw float64 and regress the NO-FLOAT64 ratchet.
Baselining is forbidden (`scripts/precision-gates.sh`: "Fix AT THE PRODUCER"). The
result here is a sign test and a ratio sweep spanning two orders of magnitude; f64
is ample for both.

Bean qou-4u60.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import math
import sys

import mpmath as mp

import mass_binding_dashboard as mbd

# Catalan's constant. Vol(L6a4) = 8G is the hyperbolic volume the magic-A form uses.
EIGHT_G = 8 * float(mp.catalan)

# (label, A, SU(4) spin-flavour ground-state partition) — as the dashboard assigns them.
ISOTOPES = [
    ("2H", 2, (2, 2, 1, 1)),
    ("3H", 3, (3, 2, 2, 2)),
    ("4He", 4, (3, 3, 3, 3)),
    ("6Li", 6, (5, 5, 4, 4)),
    ("7Li", 7, (6, 6, 5, 4)),
]

Q_SWEEP = [1.02, 1.05, 1.08, 1.10998, 1.13, 1.16, 1.20, 1.30, 1.50]


def main() -> int:
    me, q0, _E0 = mbd._constants()

    def gate(q, lam):
        """SU(4) occupancy binding E₀(q)·ln(1/W_λ(q)) — both factors q-dependent."""
        return (_qbeta_e0.order_zero_scaled(me, q)) * math.log(1.0 / mbd.W_lambda_float(q, lam))

    def magic(A):
        """Magic-A whole-nucleus volume form 2·m_e·A·8G — constant in q."""
        return 2 * me * A * EIGHT_G

    lam4 = next(lam for (nm, _A, lam) in ISOTOPES if nm == "4He")
    diff = lambda q: gate(q, lam4) - magic(4)  # noqa: E731

    print("Is E0*ln(1/W_lambda) = 2*m_e*A*8G at 4He an identity?  (bean qou-4u60)\n")
    print(f"q0 = {q0:.12f}   m_e = {me:.9f} MeV   8G = Vol(L6a4) = {EIGHT_G:.9f}\n")

    # ---- Test 1: does it hold as a function of q? --------------------------
    print("TEST 1 - q-dependence. An identity holds for all q; a crossing holds at one point.\n")
    print("|       q | E0(q)*ln(1/W) |  2*m_e*A*8G |   ratio |   rel diff |")
    print("| ------: | ------------: | ----------: | ------: | ---------: |")
    for q in Q_SWEEP:
        g, m = gate(q, lam4), magic(4)
        print(f"| {q:7.5f} | {g:13.6f} | {m:11.6f} | {g / m:7.5f} | {g / m - 1:+.3e} |")

    # Bisect the crossing. Bracket chosen from the sweep, which straddles 1.
    lo, hi = 1.105, 1.115
    for _ in range(200):
        mid = (lo + hi) / 2
        if diff(lo) * diff(mid) <= 0:
            hi = mid
        else:
            lo = mid
    qstar = (lo + hi) / 2

    h = 1e-5
    slope = (diff(q0 + h) - diff(q0 - h)) / (2 * h)
    closeness = abs(gate(q0, lam4) - magic(4))

    print(f"\n  crossing  q* = {qstar:.12f}")
    print(f"  substrate q0 = {q0:.12f}")
    print(f"  q* - q0      = {qstar - q0:+.3e}  ({(qstar / q0 - 1) * 1e6:+.2f} ppm)")
    print(f"  d(gate-magic)/dq at q0 = {slope:.2f} MeV per unit q")
    print(f"  => the {closeness:.4f} MeV closeness is exactly the statement")
    print(f"     'q* is within {closeness / abs(slope):.2e} of q0' - and it is, at "
          f"{abs(qstar - q0):.2e}. Nothing more.")
    print("\n  NB the crossing is guaranteed: gate(q) falls monotonically from +inf to 0")
    print("     while magic is constant in q, so they must cross exactly once. Only the")
    print("     LOCATION could carry information.")

    # ---- Test 2: does it hold across A? ------------------------------------
    print("\nTEST 2 - A-dependence. A structural relation should not single out one A.\n")
    print("| iso | A | lambda        |  E_gate | 2*m_e*A*8G |  ratio |")
    print("| --- | -: | ------------- | ------: | ---------: | -----: |")
    ratios = {}
    for nm, A, lam in ISOTOPES:
        g, m = gate(q0, lam), magic(A)
        ratios[nm] = g / m
        print(f"| {nm:4}| {A} | {str(lam):13} | {g:7.3f} | {m:10.3f} | {g / m:6.4f} |")

    # ---- Verdict -----------------------------------------------------------
    off_identity = [q for q in Q_SWEEP if abs(gate(q, lam4) / magic(4) - 1) > 1e-3]
    others = [abs(r - 1) for nm, r in ratios.items() if nm != "4He"]
    is_identity = len(off_identity) == 0
    is_structural_in_A = max(others) < 0.05 if others else False

    print("\n## Verdict\n")
    print(f"- Identity in q?  {'YES' if is_identity else 'NO'} - fails at "
          f"{len(off_identity)}/{len(Q_SWEEP)} sampled q, ratio spanning "
          f"{min(gate(q, lam4) / magic(4) for q in Q_SWEEP):.3f}-"
          f"{max(gate(q, lam4) / magic(4) for q in Q_SWEEP):.3f}.")
    print(f"- Structural in A? {'YES' if is_structural_in_A else 'NO'} - other A give ratios "
          f"{', '.join(f'{r:.3f}' for nm, r in ratios.items() if nm != '4He')}; "
          f"only A=4 lands on 1.")
    print("- => reading (iii): a COINCIDENCE. The two are unrelated functions crossing")
    print("     near the substrate point. They do NOT corroborate each other, so the")
    print("     shared +5.9 % vs AME is two separate misses, not one cross-checked result.")
    print("- Neither form is refuted as a near-match; both still land 4He at +5.9 % with")
    print("  no fit. What is refuted is the identity, and with it the inference that")
    print("  either lends the other support.")
    print("\n(no witness by design - see module docstring: f64 display pipeline.)")

    # Exit non-zero if a future change makes this an identity after all - that would
    # be a real finding and should not pass silently.
    return 1 if (is_identity or is_structural_in_A) else 0


if __name__ == "__main__":
    sys.exit(main())
