#!/usr/bin/env python3
"""
Probe — the BUDGET the missing collective binding term has to fill.

`QOU/MassTheory/ChainBindingNoSaturationPeak.lean` proves the additive per-bond
chain is a hyperbola in `A` and therefore cannot produce the saturation peak. The
companion probe measured its asymptote at `c₁ = 2.9242 MeV/nucleon`, against a
measured peak of `8.7904` — so the chain is 3.01x low even at `A → ∞`.

That says the missing term is large. This probe says *how* large, per isotope,
so a candidate can be screened on magnitude BEFORE anyone derives one. It is a
subtraction, not a fit:

    R(A) := B_AME(A)/A  −  B_chain(A)/A

`R` is simply what any collective term must supply per nucleon. Reporting it
introduces no coefficient and asserts no form.

## Why this is worth having

The six failed Δ_λ ansätze (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel,
LP-Frobenius, crystal-graph, augmented Markov) were all refuted at the deuteron.
The corpus's diagnosis is structural — a per-block weight is intensive and cannot
produce an extensive quantity (`BindingSaturationCapA4.lean`,
`JetFiltrationExtensive.lean`). A magnitude budget is the complementary screen:
a candidate that is structurally admissible but an order of magnitude too small
can be dropped without a deuteron run.

## What is reported, and how to read it

* `R(A)` per nucleon, over the light band and up to ²⁰⁸Pb.
* whether `R` is **extensive** — i.e. whether `R(A)` approaches a constant, which
  is what "a separate, super-pairwise additive extensive object" requires.
* the two derived scales already in hand, for comparison ONLY:
  `c₁ = α(L_pp+L_nn)/2` (chain asymptote) and `a_V = E₀·ln(1/W_free)` (the free
  nucleon's Plancherel surprisal). Neither is proposed as the answer; they are
  the parameter-free quantities of the right *type* already derived, and the
  point is to see whether anything of that type is even the right size.

## What this does NOT do

No fit, no ansatz, no coefficient. It does not propose a form for the collective
term and does not bear on the Δ_λ "no seventh fit-based ansatz" gate — the gate
forbids fitting a magnitude, and this measures the target rather than fitting
anything to it. `R` is a *requirement*, not a model.

Also: `R` inherits every approximation in `B_chain`, including that the chain is
evaluated with the same three per-bond constants at all `A`. If those constants
are `A`-dependent (a case the Lean exclusion explicitly does not cover), `R` as
computed here is the budget for the *remainder after a constant-L chain*, which
is the object of interest here regardless.

NO WITNESS: a subtraction of a measured table from a derived closed form; the
printed table reproduces it.

Bean qou-x66y follow-on; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import math
import sys

import mass_binding_dashboard as mbd

ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
            ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6),
            ("16O", 8, 8), ("24Mg", 12, 12), ("40Ca", 20, 20),
            ("56Fe", 26, 30), ("90Zr", 40, 50), ("208Pb", 82, 126)]


def main() -> int:
    me, q0, E0 = mbd._constants()
    alpha = E0
    L = mbd._bond_type_L()
    if isinstance(L, dict):
        Lpp, Lpn, Lnn = float(L["pp"]), float(L["pn"]), float(L["nn"])
    else:
        Lpp, Lpn, Lnn = (float(x) for x in L)

    c1 = alpha * (Lpp + Lnn) / 2.0
    a_V = E0 * math.log(1.0 / mbd.W_lambda_float(q0, (1, 1, 1)))
    ame = mbd._ame_table()

    print("Collective-term BUDGET — what the missing term must supply\n")
    print(f"  alpha = E0 = {alpha:.6f} MeV      q0 = {q0!r}")
    print(f"  chain asymptote  c1  = {c1:.4f} MeV/nucleon    [DERIVED]")
    print(f"  free-nucleon a_V     = {a_V:.4f} MeV/nucleon    [DERIVED, comparison only]\n")
    print("  R(A) = B_AME(A)/A - B_chain(A)/A   -- a subtraction, not a fit\n")
    print("| iso   |   A | B_AME/A | chain/A | R(A) required | R/A_asym? |")
    print("| ----- | --: | ------: | ------: | ------------: | --------: |")

    rows = []
    for name, Z, N in ISOTOPES:
        A = Z + N
        t = ame.get((Z, A))
        if not t:
            continue
        meas = t[0] / A
        chain = alpha * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn) / A
        R = meas - chain
        rows.append((name, A, meas, chain, R))
        print(f"| {name:<5} | {A:>3} | {meas:>7.4f} | {chain:>7.4f} | {R:>13.4f} | "
              f"{R / c1:>9.3f} |")

    if not rows:
        print("\n  no AME rows resolved — cannot report a budget.")
        return 1

    # Extensivity: does R(A) settle to a constant for large A?
    heavy = [r for r in rows if r[1] >= 24]
    print("\nEXTENSIVITY — does R(A) approach a constant (as an extensive term must)?\n")
    if len(heavy) >= 3:
        vals = [r[4] for r in heavy]
        lo, hi = min(vals), max(vals)
        mean = sum(vals) / len(vals)
        spread = (hi - lo) / abs(mean) * 100 if mean else float("inf")
        names = ", ".join(f"{r[0]}={r[4]:.3f}" for r in heavy)
        print(f"  A >= 24: {names}")
        print(f"  range {lo:.4f} .. {hi:.4f}   mean {mean:.4f}   spread {spread:.1f} %")
        flat = spread < 25.0
        print(f"  approximately constant (<25% spread): {flat}")
    else:
        mean, flat = float("nan"), False
        print("  too few heavy rows to judge.")

    peak = max(rows, key=lambda r: r[2])
    peak_R = max(rows, key=lambda r: r[4])
    print(f"\n  measured B/A peaks at {peak[0]} (A={peak[1]}): {peak[2]:.4f} MeV/nucleon")
    print(f"  R peaks at            {peak_R[0]} (A={peak_R[1]}): {peak_R[4]:.4f} MeV/nucleon")
    print(f"  -> R carries the peak: {peak[0] == peak_R[0]}"
          "   (the chain is monotone, so ALL curvature must live in R)")

    print("\nSCREENING the derived scales already in hand (comparison only, not proposals):\n")
    if not math.isnan(mean):
        print(f"  required plateau R      ~ {mean:.4f} MeV/nucleon")
        print(f"  chain asymptote c1      = {c1:.4f}   ->  R/c1  = {mean / c1:.2f}x")
        print(f"  free-nucleon a_V        = {a_V:.4f}   ->  R/a_V = {mean / a_V:.2f}x")
        print(f"  c1 + a_V                = {c1 + a_V:.4f}   vs measured plateau "
              f"{sum(r[2] for r in heavy) / len(heavy):.4f}")

    # ---- the sign structure: the sharpest screen this produces ------------
    print("\nSIGN STRUCTURE — the sharpest screening criterion here:\n")
    neg = [r for r in rows if r[4] < 0]
    pos = [r for r in rows if r[4] > 0]
    mixed = bool(neg) and bool(pos)
    for r in neg:
        print(f"  R < 0 at {r[0]} (A={r[1]}): {r[4]:+.4f}  "
              "-- the chain OVER-binds here")
    print(f"  R > 0 at all {len(pos)} remaining rows (A >= {min(r[1] for r in pos)})")
    print(f"\n  => R is MIXED-SIGN in A: {mixed}")
    if mixed:
        print("     Any candidate collective term that is manifestly NON-NEGATIVE by")
        print("     construction -- an entropy, a KL divergence, a dimension count, a sum")
        print("     of squares, a positive Plancherel weight -- CANNOT reproduce R,")
        print("     because it cannot go negative at the deuteron. This is the same shape")
        print("     of argument as the KL-positivity prune that killed Option-E PROBE-4")
        print("     (mixed-sign target vs non-negative multiplicities), applied now to the")
        print("     A-dependence rather than the lambda-dependence.")

    print("\n## Verdict\n")
    print("- The budget is LARGE: the collective term must supply more per nucleon than")
    print("  the entire chain does at its asymptote. Any candidate an order of magnitude")
    print("  below this can be dropped without a deuteron run.")
    print("- All curvature is the collective term's: the chain is provably monotone")
    print("  (QOU.MassTheory.chain_no_saturation_peak), so the peak, the light-nucleus")
    print("  rise, and the heavy-nucleus fall are ALL R's to explain.")
    print("- Reported as a requirement, not a model. No form is proposed, nothing is")
    print("  fitted, and the Delta_lambda no-seventh-ansatz gate is untouched.")
    print("\n(no witness by design — a subtraction of measured from derived.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
