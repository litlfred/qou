#!/usr/bin/env python3
"""
Probe — is the light-nucleus over-binding of `B_vol = a_V·A` a SURFACE term?

`a_V = E₀·ln(1/W_free) ≈ 7.5836 MeV/nucleon` is DERIVED parameter-free (E₀ from
CAL-1/CAL-2, W_free the free nucleon's (1,1,1) Hecke q-Plancherel weight). It
lands on the nuclear saturation plateau, which is a real result. But `B_vol =
a_V·A` over-binds the lightest nuclei badly — ²H by 6.8× — and the obvious
reading is that a boundary/surface term is missing, since the braid word has a
boundary. This probe tests that reading before anyone builds on it.

It is the one binding-axis item NOT gated on `conj:s5-so3-fiber-action` (the
GAP-A-4 retrospective closed λ(K), the Vol(K) convention, and the ρ·A scale rule
onto that conjecture), which is why it is worth doing on its own.

## The test, and why it is falsifiable

Standard SEMF: B = a_V·A − a_S·A^{2/3} − a_C·Z(Z−1)/A^{1/3} − a_A·(N−Z)²/A + δ.

Take a_V DERIVED and E_C DERIVED (canonical `coulomb_energy`, α_EM from q₀,
R₀ = λ̄_π CAL-3), then EXTRACT the implied surface coefficient per isotope:

    a_S(K) = (a_V·A − E_C(Z,A) − B_AME(K)) / A^{2/3}

a_S is **extracted, not derived** — one free parameter, in the same spirit as the
r0 extraction in `mirror_isospin_coulomb_split.py`, and labelled as such. The
FALSIFIABLE content is not its value but its **constancy**: a genuine surface
term is one coefficient for all A. If a_S(K) is flat, the surface reading holds
and a_S becomes a derivation target. If it drifts monotonically, the A^{2/3}
shape is wrong and the deficit is something else.

## The prior question that may dissolve the whole thing

SEMF's volume coefficient is a_V ≈ 15.75 MeV, while the NET binding per nucleon
peaks near 8.8 MeV — the difference being exactly the surface, Coulomb and
asymmetry terms subtracted off. Our derived 7.5836 sits at the NET scale, not the
SEMF-volume scale. If it is the net, then `a_V·A` is already a saturation
ASYMPTOTE with the corrections baked in, and bolting a surface term on top
DOUBLE-COUNTS. The probe checks this explicitly before reporting any a_S, by
comparing 7.5836 against both scales and against the measured B_AME/A peak.

Reported tiers, kept distinct:
  DERIVED    a_V, E_C
  MEASURED   B_AME, and the B/A peak
  EXTRACTED  a_S(K) — one fitted parameter, the object under test
  LITERATURE the SEMF coefficients, quoted only as comparison scales

NO WITNESS by design, as for the other probes in this cluster: every input
descends from `mass_binding_dashboard._constants()`, which casts to float once at
its own boundary, so a witness would enshrine raw float64 and regress the
NO-FLOAT64 ratchet. The result here is a constancy/scatter test, where f64 is
ample.

Bean qou-1nvh follow-on; PR #4952.
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
from coulomb_energy import coulomb_energy_mev

# Literature SEMF coefficients (Bethe-Weizsacker, typical fit). COMPARISON
# SCALES ONLY - nothing here is computed from them.
SEMF_A_V_LIT = 15.75   # MeV, volume
SEMF_A_S_LIT = 17.8    # MeV, surface

# (name, Z, N) - the light band plus enough mid-mass reach to see a trend.
ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
            ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6),
            ("16O", 8, 8), ("24Mg", 12, 12), ("40Ca", 20, 20), ("56Fe", 26, 30)]


def main() -> int:
    me, q0, E0 = mbd._constants()
    ame = mbd._ame_table()

    # DERIVED, parameter-free: the free nucleon's (1,1,1) Plancherel surprisal.
    a_V = E0 * math.log(1.0 / mbd.W_lambda_float(q0, (1, 1, 1)))

    rows = []
    for name, Z, N in ISOTOPES:
        A = Z + N
        t = ame.get((Z, A))
        if not t:
            continue
        B = t[0]
        E_C = float(coulomb_energy_mev(Z, A))
        resid = a_V * A - E_C - B          # what a surface term would have to absorb
        a_S = resid / A ** (2.0 / 3.0)     # EXTRACTED, one free parameter
        rows.append({"name": name, "Z": Z, "N": N, "A": A, "B": B, "B_per_A": B / A,
                     "E_C": E_C, "resid": resid, "a_S": a_S})

    print("a_V surface-correction probe — is the light-nucleus over-binding a surface term?\n")
    print(f"  a_V = E0*ln(1/W_free) = {a_V:.4f} MeV/nucleon   [DERIVED, parameter-free]")
    print(f"  E0  = {E0:.4f} MeV,  q0 = {q0!r}\n")

    # ---- the prior question: which scale is a_V on? -----------------------
    peak = max(r["B_per_A"] for r in rows)
    peak_iso = max(rows, key=lambda r: r["B_per_A"])["name"]
    print("SCALE CHECK — is a_V the SEMF volume coefficient, or the NET B/A?\n")
    print(f"  {'SEMF a_V (literature)':<34} {SEMF_A_V_LIT:>8.3f} MeV   ratio a_V/lit = "
          f"{a_V / SEMF_A_V_LIT:.3f}")
    print(f"  {'measured peak B/A (' + peak_iso + ')':<34} {peak:>8.3f} MeV   ratio a_V/peak = "
          f"{a_V / peak:.3f}")
    on_net = abs(a_V - peak) < abs(a_V - SEMF_A_V_LIT)
    print(f"\n  => a_V sits on the {'NET B/A' if on_net else 'SEMF-VOLUME'} scale.")
    if on_net:
        print("     This is decisive for the question asked. A SEMF volume coefficient is")
        print("     the binding BEFORE surface/Coulomb/asymmetry are subtracted; the net")
        print("     B/A is what is left AFTER. a_V matching the net means a_V*A is already")
        print("     a saturation ASYMPTOTE with those corrections absorbed, so subtracting")
        print("     a surface term on top DOUBLE-COUNTS. The light-nucleus over-binding is")
        print("     then not a missing surface term at all — it is that an asymptote does")
        print("     not apply at small A.")

    # ---- the constancy test ------------------------------------------------
    print("\nEXTRACTED surface coefficient per isotope (a_S is FITTED, one free parameter;")
    print("the falsifiable content is whether it is CONSTANT, not its value):\n")
    print("| iso  |  A | B_AME | B/A   |  E_C  | residual | a_S extracted |")
    print("| ---- | -: | ----: | ----: | ----: | -------: | ------------: |")
    for r in rows:
        print(f"| {r['name']:<4} | {r['A']:>2} | {r['B']:>5.2f} | {r['B_per_A']:>5.3f} | "
              f"{r['E_C']:>5.2f} | {r['resid']:>8.3f} | {r['a_S']:>13.3f} |")

    # ---- the identity that makes this exact, not merely empirical ----------
    # Drop E_C for a moment. The residual a_V*A - B is IDENTICALLY A*(a_V - B/A):
    # it is the isotope's distance from the asymptote, rescaled by A. It carries
    # no information the B/A curve does not already carry, so "fitting a_S to it"
    # fits the SHAPE OF THE B/A CURVE, not a boundary. Verified numerically below
    # so the claim is checked rather than asserted.
    ident_max = max(abs((a_V * r["A"] - r["B"]) - r["A"] * (a_V - r["B_per_A"]))
                    for r in rows)
    print("\nIDENTITY CHECK — the residual carries no independent content:")
    print("    a_V*A - B_AME  ==  A*(a_V - B_AME/A)      max |difference| = "
          f"{ident_max:.2e} MeV")
    print("  So the quantity a_S is fitted to is the isotope's distance from the")
    print("  asymptote, rescaled. Fitting a surface coefficient to it fits the B/A")
    print("  curve's shape. That is why a_S changes SIGN: a_V*A over-binds while")
    print("  B/A < a_V (light) and under-binds once B/A > a_V (mid-mass), crossing")
    print("  zero where B/A = a_V. A boundary term has no reason to do that.")
    print("\n  NB the E_C subtraction compounds it: if a_V is the NET B/A, Coulomb is")
    print("  already absorbed in it, so subtracting E_C again double-counts — which is")
    print("  what drives a_S so far negative at high Z (E_C = 103.8 MeV at 56Fe).")

    a_s_vals = [r["a_S"] for r in rows]
    lo, hi = min(a_s_vals), max(a_s_vals)
    mean = sum(a_s_vals) / len(a_s_vals)
    spread = (hi - lo) / abs(mean) * 100 if mean else float("inf")
    # Monotonic in A? A genuine constant should not trend.
    trend = all(rows[i]["a_S"] <= rows[i + 1]["a_S"] + 1e-9 for i in range(len(rows) - 1))
    trend_dn = all(rows[i]["a_S"] >= rows[i + 1]["a_S"] - 1e-9 for i in range(len(rows) - 1))

    print(f"\n  a_S range {lo:.3f} .. {hi:.3f} MeV   mean {mean:.3f}   spread {spread:.0f} %")
    print(f"  monotonic in A: {'yes (increasing)' if trend else 'yes (decreasing)' if trend_dn else 'no'}")
    print(f"  (SEMF literature a_S = {SEMF_A_S_LIT} MeV, for scale)")

    constant = spread < 20.0
    print("\n## Verdict\n")
    if constant:
        print(f"- a_S is CONSTANT to {spread:.0f} % across A={rows[0]['A']}..{rows[-1]['A']}.")
        print("  The A^(2/3) surface shape survives, and a_S becomes a derivation target.")
    else:
        print(f"- a_S is NOT constant — it spans {spread:.0f} % across "
              f"A={rows[0]['A']}..{rows[-1]['A']}"
              f"{', and moves monotonically with A' if (trend or trend_dn) else ''}.")
        print("  A single surface coefficient does not absorb the deficit, so the A^(2/3)")
        print("  SURFACE READING IS REFUTED as the explanation for the light-nucleus")
        print("  over-binding. Scope-(a): this constrains the surface reading of THIS")
        print("  residual under a derived a_V; it excludes no ingredient, and says nothing")
        print("  about surface terms elsewhere in the framework.")
    if on_net:
        print("- And the scale check above explains WHY: a_V is the net-B/A saturation")
        print("  value, not a SEMF volume coefficient, so there is no surface term still")
        print("  owed — it is already absorbed. Fitting one recovers a compensator for")
        print("  'asymptote applied at small A', which is not a boundary effect and has")
        print("  no reason to be constant.")

    print("\n(no witness by design — see module docstring: f64 display pipeline.)")
    # Non-zero if the surface reading unexpectedly survives, so it cannot pass silently.
    return 1 if constant else 0


if __name__ == "__main__":
    sys.exit(main())
