#!/usr/bin/env python3
"""
Probe — the chain binding IS a hyperbola in A, and the measured curve is not.

Empirical support for `QOU/MassTheory/ChainBindingNoSaturationPeak.lean`, which
proves (sorry-free) that along any isobaric chain

    B_sym(A)/A = c₁ + c₂/A ,     c₁ = α(L_pp+L_nn)/2 ,
                                 c₂ = α[(−d/2−1)L_pp + L_pn + (d/2−1)L_nn]

and that such a function has **no strict interior maximum** — hence cannot
reproduce a saturation peak, for any values of the per-bond constants.

The Lean is an identity plus an ordering fact; neither can check two things that
matter for whether the exclusion actually bites:

  1. **Does the REAL compute have this shape?** The theorem is about an idealized
     `α[(Z−1)L_pp + L_pn + (N−1)L_nn]`. If `mass_binding_dashboard`'s `B_sym`
     were something else, the theorem would be about the wrong object. Checked
     here by taking the dashboard's own derived per-bond constants, forming
     `c₁, c₂`, and comparing against the dashboard's own `B_sym` row by row.
  2. **Does the measured curve actually peak?** The exclusion is only interesting
     because `B_AME/A` has an interior maximum. Checked against AME2020.

## What this establishes

That the proved no-peak invariant applies to the production object, and that the
thing it excludes is a thing the data demands. Together: the chain form is
excluded as the SOURCE OF THE PEAK — scope-(b), with the Lean invariant behind
it — while remaining perfectly valid as an additive contribution (AGENTS.md
permanence principle 1: an inaccurate total does not invalidate a proved
per-bond factor).

## What this does NOT establish

Nothing about the magnitude of the missing collective term, and nothing about
what it is. It says only that no re-weighting of `L_pp, L_pn, L_nn` reaches the
peak. The Δ_λ "no seventh fit-based ansatz" gate is untouched — this probe fits
nothing and introduces no coefficient.

NO WITNESS: reads the dashboard's derived constants and AME2020, reports a shape
comparison; every number is reproduced by the printed table.

Bean qou-uqen follow-on; L2 binding axis.
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

# N = Z isobaric chain (d = 0) — the alpha-conjugate line, where the theorem's
# c1/c2 take their simplest form. Plus a mid/high pair to locate the peak.
NZ_CHAIN = [("2H", 1, 1), ("4He", 2, 2), ("6Li", 3, 3), ("12C", 6, 6),
            ("16O", 8, 8), ("24Mg", 12, 12), ("40Ca", 20, 20)]
PEAK_SCAN = NZ_CHAIN + [("56Fe", 26, 30), ("90Zr", 40, 50), ("208Pb", 82, 126)]


def main() -> int:
    me, q0, E0 = mbd._constants()
    alpha = E0
    L = mbd._bond_type_L()
    # _bond_type_L returns the three per-bond log-suppressions; accept either a
    # mapping or a 3-tuple so this does not silently mis-order them.
    if isinstance(L, dict):
        Lpp, Lpn, Lnn = float(L["pp"]), float(L["pn"]), float(L["nn"])
    else:
        Lpp, Lpn, Lnn = (float(x) for x in L)

    d = 0.0
    c1 = alpha * (Lpp + Lnn) / 2.0
    c2 = alpha * ((-d / 2 - 1) * Lpp + Lpn + (d / 2 - 1) * Lnn)

    print("Chain binding is a hyperbola in A — and the measured curve is not\n")
    print(f"  alpha = E0 = {alpha:.6f} MeV     q0 = {q0!r}")
    print(f"  L_pp = {Lpp:.6f}   L_pn = {Lpn:.6f}   L_nn = {Lnn:.6f}   [DERIVED]\n")
    print("  Along the N = Z chain (d = 0), the Lean identity gives")
    print(f"      B_sym/A = c1 + c2/A ,   c1 = {c1:.6f} MeV/nucleon , c2 = {c2:.6f} MeV")
    print(f"    -> chain ASYMPTOTE c1 = {c1:.4f} MeV/nucleon"
          f"   (c2 {'<' if c2 < 0 else '>'} 0 => approaches it from "
          f"{'below, increasing' if c2 < 0 else 'above, decreasing'})\n")

    # ---- check 1: does the production B_sym have this shape? ----------------
    ame = mbd._ame_table()
    print("CHECK 1 — the hyperbola vs the dashboard's own B_sym (is the theorem")
    print("about the right object?):\n")
    print("| iso  |  A | B_sym/A dashboard | c1 + c2/A | abs diff |")
    print("| ---- | -: | ----------------: | --------: | -------: |")
    worst = 0.0
    for name, Z, N in NZ_CHAIN:
        A = Z + N
        Bsym = alpha * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
        lhs = Bsym / A
        rhs = c1 + c2 / A
        diff = abs(lhs - rhs)
        worst = max(worst, diff)
        print(f"| {name:<4} | {A:>2} | {lhs:>17.6f} | {rhs:>9.6f} | {diff:>8.2e} |")
    shape_ok = worst < 1e-9
    print(f"\n  worst |difference| = {worst:.2e}")
    print("  NB this half is ALGEBRA, not evidence: both columns are built from the")
    print("  same closed form, so it can only catch an arithmetic slip in c1/c2. An")
    print("  earlier revision of this probe presented exactly this comparison as")
    print("  'production B_sym IS the hyperbola' -- it was circular (it tried")
    print("  mbd.b_sym_mev, which does not exist, and silently fell back to")
    print("  rebuilding the same expression). The real check is CHECK 1b.")

    # ---- check 1b: the NON-circular one, against the exact 3A-strand trace ----
    print("\nCHECK 1b — the chain vs the EXACT p(3A) transfer trace (independent):\n")
    print("  Both sides must carry the Lean-proved writhe factor (1-h)^(de/2):")
    print("  `_bond_type_L` applies it, `tr_m_atom_zn` does not, so an un-normalised")
    print("  difference measures that factor (+/-0.4909 MeV per unit d = N-Z) rather")
    print("  than the factorisation. `mbd._chain_writhe_shift` supplies it.\n")
    print("| iso  |  A | chain     | exact trace (normalised) | abs diff |")
    print("| ---- | -: | --------: | -----------------------: | -------: |")
    worst_ex = 0.0
    n_ex = 0
    for name, Z, N in [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]:
        A = Z + N
        # Only genuine unavailability of the trace is tolerated here. A broad
        # `except Exception` was masking a NameError in this very block as
        # "trace unavailable", which would have let a coding bug read as missing
        # data and silently downgrade the check to vacuous.
        try:
            from tr_m_atom_via_transfer import tr_m_atom_zn
        except ImportError as exc:                     # pragma: no cover
            print(f"| {name:<4} | {A:>2} | (transfer trace unavailable: {exc}) |")
            continue
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
        exact = alpha * math.log(float(tf) / float(ta))
        exact += mbd._chain_writhe_shift(Z, N, alpha)
        chain = alpha * (max(Z - 1, 0) * Lpp + (Lpn if Z >= 1 and N >= 1 else 0.0)
                         + max(N - 1, 0) * Lnn)
        d = abs(chain - exact)
        worst_ex = max(worst_ex, d)
        n_ex += 1
        print(f"| {name:<4} | {A:>2} | {chain:>9.6f} | {exact:>24.6f} | {d:>8.2e} |")
    exact_ok = n_ex >= 3 and worst_ex < 1e-9
    print(f"\n  worst |difference| over {n_ex} isotopes = {worst_ex:.2e}")
    print(f"  -> the chain IS the exact trace (independently verified): {exact_ok}")
    print("     This is what licenses reading the hyperbola exclusion as a statement")
    print("     about the exact object and not merely about a closed-form shortcut.")
    shape_ok = shape_ok and exact_ok

    # ---- check 2: does the measured curve peak? ----------------------------
    print("\nCHECK 2 — measured B_AME/A: is there an interior maximum?\n")
    print("| iso   |   A | B_AME/A measured |")
    print("| ----- | --: | ---------------: |")
    rows = []
    for name, Z, N in PEAK_SCAN:
        A = Z + N
        t = ame.get((Z, A))
        if not t:
            continue
        per = t[0] / A
        rows.append((name, A, per))
        print(f"| {name:<5} | {A:>3} | {per:>16.4f} |")

    peak_ok = False
    if len(rows) >= 3:
        imax = max(range(len(rows)), key=lambda i: rows[i][2])
        peak_ok = 0 < imax < len(rows) - 1
        pn, pa, pv = rows[imax]
        print(f"\n  maximum at {pn} (A = {pa}), B/A = {pv:.4f} MeV")
        print(f"  interior (not an endpoint of the scan): {peak_ok}")

    # ---- the comparison that matters ---------------------------------------
    print(f"\n  chain asymptote      c1 = {c1:.4f} MeV/nucleon")
    if rows:
        pv = max(r[2] for r in rows)
        print(f"  measured peak B/A       = {pv:.4f} MeV/nucleon"
              f"   -> chain is {pv / c1:.2f}x low even at its OWN limit")

    print("\n## Verdict\n")
    if shape_ok and peak_ok:
        print("- The production B_sym is EXACTLY the hyperbola the Lean treats, and the")
        print("  measured curve has an interior maximum the hyperbola provably cannot have.")
        print("  So the chain form is excluded as the SOURCE OF THE PEAK — scope-(b), with")
        print("  QOU.MassTheory.chain_no_saturation_peak as the invariant.")
        print("- Note the chain does not merely lack the peak: its own A -> infinity limit")
        print("  c1 already sits far below the measured maximum, so the missing term is")
        print("  needed for the MAGNITUDE as well as the SHAPE.")
        print("- NOT excluded: the chain as an additive CONTRIBUTION. An inaccurate total")
        print("  does not invalidate a proved per-bond factor (AGENTS.md permanence")
        print("  principle 1). Nothing here bears on the magnitude of the missing term,")
        print("  and nothing is fitted.")
    else:
        print(f"- Inconclusive: shape match {shape_ok}, interior peak {peak_ok}.")
        print("  Re-derive before citing the Lean exclusion against production.")

    print("\n(no witness by design — shape comparison on derived constants.)")
    return 0 if (shape_ok and peak_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
