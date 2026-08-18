#!/usr/bin/env python3
"""qbeta_ladder_phase_mirror_covariance_probe.py -- the ladder phase's
bar-anomaly is `h * (z - bar z)`, and in convention D that is exactly `h^2`.

Bean `qou-cds1`. This is the closed-form / Lean-backed companion to
`qbeta_eigenphase_branch_and_barodd_projection_probe.py`, which measured the
D-frame bar-anomaly numerically and applied the projection `alpha - h^2/4`
without knowing where either number came from.

WHAT THIS ESTABLISHES

1. **The anomaly identity is general, not a D-frame accident.** For the
   asserted phase `alpha = (z - 1)*h/2` with `h = q - 1/q` bar-odd,

       bar(alpha) + alpha = h * (z - bar z) / 2

   for ANY Markov parameter `z`. So the phase is bar-odd (mirror-covariant)
   **iff** `z` is exactly bar-invariant. Proved over a generic domain:
   `QOU.QBeta.phaseTwice_bar_odd_iff_z_bar_fixed`.

2. **Convention C passes, and by structure.** `z_C = sqrt(q)/(1+q)` is exactly
   bar-fixed -- already proved in the corpus as
   `QOU.QBeta.z_bar_invariant_field` (PR #3449, in the half-power coordinate).
   Hence `bar(alpha_C) + alpha_C = 0` identically. The C-frame bar-oddness
   reported in the eigenphase probe was not a coincidence of the anchor.

3. **Convention D fails, and its anomaly is exactly `h`.** `z_D - bar(z_D)`
   is not small, not anchor-dependent, and not approximate: it is

       z_D - bar(z_D) = q^3/(q^2+1) - q^-1/(q^-2+1) = (q^4-1)/(q(1+q^2))
                      = (q^2-1)/q = q - 1/q = h    (exactly)

   so `bar(alpha_D) + alpha_D = h^2/2`. That closed form reproduces the
   number the eigenphase probe measured at both anchors.

4. **The projection `alpha_D - h^2/4` is therefore FORCED, not fitted.**
   Subtracting half the anomaly is the unique shift making the phase
   mirror-covariant (`h^2` is bar-EVEN, so the same constant is removed on
   both sides -- no freedom is left). Lean:
   `QOU.QBeta.phaseTwiceD_sub_hsq_bar_odd`.

WHY BAR-ODD IS THE RIGHT TEST -- the writhe/framing route. The Ocneanu trace
is not a link invariant on its own: the two stabilisation loop values differ
(`z` vs `z - h`, block `prop:jones-markov-trace-stabilisation`) and invariance
is restored by a **writhe-dependent prefactor outside the trace** (Jones 1987
Sec. 5). Writhe is mirror-ODD -- proved here generically as
`QOU.StandardModel.WritheMarkovInvariance.writhe_inv : writhe (inv a) = -writhe a`
-- and mirror acts on the Hecke side as `q -> 1/q`. A phase carried by that
prefactor must therefore be bar-odd. Item 1 turns that requirement into a
sharp test on `z`.

WHAT THIS DOES NOT ESTABLISH. It does not close `cds1` and proposes no value.
The projected D phase still leaves a residual 41.94x the C-frame one (source
witness), and that residual is untouched here. What changes is only the
epistemic status of the projection: previously a numerically-motivated shift,
now the unique mirror-covariant part with a sorry-free derivation. The
standing fence from `qbeta-d-frame-eigenphase-bar-parity` holds -- hunting
further phase corrections is fitting until one lands with the structural
standing of `c_2 = -1`. No convention is switched (D stays canonical, owner
ruling 2026-08-15) and no registry tier moves.

Anchors: proton (default) and muon. Every quantity is a function of the `q`
passed in, so there is no layer straddle; the identities are anchor-free and
the anchors serve only to exhibit them numerically.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at, Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

#: Residual ratio (projected-D vs C) carried over from the source witness. Not
#: recomputed here -- quoted so the scope statement is checkable in place.
SOURCE_RESIDUAL_RATIO = "41.94"


def _symbolic() -> dict[str, str]:
    """The three identities, symbolically exact (no floating point)."""
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    bar = lambda e: sp.simplify(e.subs(q, 1 / q))  # noqa: E731
    zC = sp.sqrt(q) / (1 + q)
    zD = q ** 3 / (q ** 2 + 1)
    alpha = lambda z: (z - 1) * h / 2  # noqa: E731
    return {
        "zC_anomaly": sp.simplify(zC - bar(zC)),
        "zD_anomaly_minus_h": sp.simplify(zD - bar(zD) - h),
        "alphaC_bar_sum": sp.simplify(bar(alpha(zC)) + alpha(zC)),
        "alphaD_bar_sum_minus_hsq_half": sp.simplify(
            bar(alpha(zD)) + alpha(zD) - h ** 2 / 2
        ),
        "projected_D_bar_sum": sp.simplify(
            (bar(alpha(zD)) - h ** 2 / 4) + (alpha(zD) - h ** 2 / 4)
        ),
    }


def _numeric(q):
    q = mp.mpf(q)
    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    zDbar = q ** -3 / (q ** -2 + 1)
    zC = mp.sqrt(q) / (1 + q)
    zCbar = mp.sqrt(1 / q) / (1 + 1 / q)
    aD, aDbar = (zD - 1) * h / 2, (zDbar - 1) * (-h) / 2
    aC, aCbar = (zC - 1) * h / 2, (zCbar - 1) * (-h) / 2
    return {
        "q": q, "h": h,
        "zD_minus_bar": zD - zDbar,
        "zD_anomaly_residual": abs((zD - zDbar) - h),
        "zC_minus_bar": abs(zC - zCbar),
        "alphaD_bar_sum": aDbar + aD,
        "alphaD_residual_vs_hsq_half": abs((aDbar + aD) - h ** 2 / 2),
        "alphaC_bar_sum_abs": abs(aCbar + aC),
        "projected_bar_sum_abs": abs((aDbar - h ** 2 / 4) + (aD - h ** 2 / 4)),
    }


def main() -> int:
    sym = _symbolic()
    rows = {lab: _numeric(q) for lab, q in (("proton", q_at()), ("muon", q_muon_at()))}

    print("=" * 78)
    print(" ladder phase mirror-covariance -- bar(2a) + 2a = h * (z - bar z)")
    print("=" * 78)
    print("\n  SYMBOLIC (sympy, exact -- zero means the identity holds):")
    for k, v in sym.items():
        print(f"    {k:<34} = {v}")

    print(f"\n  NUMERIC  {'quantity':<32}{'proton':>26}{'muon':>26}")
    print("  " + "-" * 74)
    for key in ("zD_minus_bar", "h", "zD_anomaly_residual", "zC_minus_bar",
                "alphaD_bar_sum", "alphaD_residual_vs_hsq_half",
                "alphaC_bar_sum_abs", "projected_bar_sum_abs"):
        p, m = rows["proton"][key], rows["muon"][key]
        print(f"  {'':<9}{key:<32}{mp.nstr(p, 12):>26}{mp.nstr(m, 12):>26}")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  `z_D - bar(z_D)` is not merely nonzero -- it is EXACTLY h, at both anchors
  and symbolically. So the D-frame phase anomaly h^2/2 is a closed form, and
  the projection alpha_D - h^2/4 is the unique mirror-covariant part rather
  than a shift chosen to fit. Convention C's phase is bar-odd for the
  structural reason that z_C is exactly bar-fixed (z_bar_invariant_field),
  not because the anchor happened to cooperate.

  This does NOT close cds1. The projected D phase still leaves a residual
  {SOURCE_RESIDUAL_RATIO}x the C-frame one (source witness); the fence against hunting
  further phase corrections stands. Only the projection's status changed.
""")

    wb = WitnessBuilder("qbeta-ladder-phase-mirror-covariance", engine="sympy+mpmath")
    wb.set_description(
        "Closed form for the Q_beta ladder phase's bar-anomaly, backing the "
        "numerically-measured D-frame projection. For alpha = (z-1)h/2 with h "
        "bar-odd, bar(alpha)+alpha = h*(z - bar z)/2 for ANY z, so the phase "
        "is mirror-covariant iff z is exactly bar-fixed "
        "(QOU.QBeta.phaseTwice_bar_odd_iff_z_bar_fixed, sorry-free). "
        "Convention C's z = sqrt(q)/(1+q) IS bar-fixed (corpus lemma "
        "z_bar_invariant_field, PR #3449) so alpha_C is bar-odd by structure. "
        "Convention D's z = q^3/(q^2+1) is not, and its anomaly is EXACTLY h: "
        "z_D - bar(z_D) = q - 1/q, symbolically and at both anchors. Hence "
        "bar(alpha_D)+alpha_D = h^2/2 and the projection alpha_D - h^2/4 is "
        "the UNIQUE mirror-covariant part -- forced, not fitted "
        "(QOU.QBeta.phaseTwiceD_sub_hsq_bar_odd). Motivation for using "
        "bar-parity as the test: the Ocneanu trace needs a writhe-dependent "
        "framing prefactor (Jones 1987 Sec. 5) and writhe is mirror-odd "
        "(WritheMarkovInvariance.writhe_inv), so a framing phase must be "
        "bar-odd. SCOPE: closes nothing. The projected D phase still leaves a "
        "residual ~42x the C-frame one; that residual is untouched and the "
        "standing fence against hunting further phase corrections holds. No "
        "value wired, no tier moved, D stays canonical."
    )
    wb.add_data("phase_convention", "alpha = (z - 1) * h / 2, h = q - 1/q")
    wb.add_data("symbolic_exact", {k: str(v) for k, v in sym.items()})
    wb.add_data("lean_declarations", [
        "QOU.QBeta.phaseTwice_bar_anomaly",
        "QOU.QBeta.phaseTwice_bar_odd_iff_z_bar_fixed",
        "QOU.QBeta.zC_bar_fixed",
        "QOU.QBeta.phaseTwiceC_bar_odd",
        "QOU.QBeta.zD_sub_bar_eq_h",
        "QOU.QBeta.phaseTwiceD_bar_anomaly",
        "QOU.QBeta.phaseTwiceD_sub_hsq_bar_odd",
    ])
    wb.add_data("anchors", {
        lab: {k: fmt(v) for k, v in r.items()} for lab, r in rows.items()
    })
    wb.add_data("source_residual_ratio_projectedD_over_C", SOURCE_RESIDUAL_RATIO)
    wb.add_data("closes_cds1", False)

    tol = mp.mpf(10) ** -45
    wb.add_assertion(
        name="zD_minus_bar_zD_is_exactly_h",
        computed=str(int(sym["zD_anomaly_minus_h"] == 0
                         and rows["proton"]["zD_anomaly_residual"] < tol
                         and rows["muon"]["zD_anomaly_residual"] < tol)),
        expected="1", tolerance=0,
        source="sympy simplifies z_D - bar(z_D) - h to exactly 0; numerically "
               f"the residual is < 1e-45 at both anchors "
               f"(proton {mp.nstr(rows['proton']['zD_anomaly_residual'], 6)}). "
               "This is the identity that makes the D-frame anomaly a closed "
               "form rather than a measured number.",
    )
    wb.add_assertion(
        name="alphaD_bar_anomaly_equals_h_squared_over_two",
        computed=str(int(sym["alphaD_bar_sum_minus_hsq_half"] == 0
                         and rows["proton"]["alphaD_residual_vs_hsq_half"] < tol
                         and rows["muon"]["alphaD_residual_vs_hsq_half"] < tol)),
        expected="1", tolerance=0,
        source="bar(alpha_D) + alpha_D - h^2/2 simplifies to 0 symbolically and "
               "is < 1e-45 at both anchors -- the closed form of the anomaly "
               "the eigenphase probe measured.",
    )
    wb.add_assertion(
        name="C_is_bar_odd_and_projected_D_is_bar_odd_but_raw_D_is_not",
        computed=str(int(sym["zC_anomaly"] == 0
                         and sym["alphaC_bar_sum"] == 0
                         and sym["projected_D_bar_sum"] == 0
                         and rows["proton"]["alphaD_bar_sum"] != 0)),
        expected="1", tolerance=0,
        source="z_C is exactly bar-fixed and alpha_C exactly bar-odd; the "
               "projected D phase (alpha_D - h^2/4) is exactly bar-odd; the "
               "RAW D phase is not (its bar-sum is h^2/2 != 0). The three "
               "together are the iff of phaseTwice_bar_odd_iff_z_bar_fixed "
               "instantiated at both conventions.",
    )
    out = wb.save({"q0Anchor": "ambiguous"})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
