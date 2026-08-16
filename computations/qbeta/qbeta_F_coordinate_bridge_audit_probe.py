#!/usr/bin/env python3
"""qbeta_F_coordinate_bridge_audit_probe.py — the Q_β correction in the
multiplicative coordinate F = Q_β/Q_A, and what the exact bridge does.

BACKGROUND (bean `qou-cds1`). Companion to
`qbeta_ladder_required_phase_probe.py`, which showed that the ladder's phase α
is an INVERTED quantity with a square-root branch point 0.062 % above q₀ — a
pathology manufactured by writing a smooth multiplicative correction as
`cos(α − u/2)`. This probe moves to the coordinate that has no such artifact,

    F(q) := Q_β(q) / Q_A(q),      F_required = Q_codata / Q_A,

and measures the candidates against it. F is smooth; α is not. Everything
below is a measurement, not a proposal: no value is offered for anything.

THE TWO ROLES OF (z−1)h/2, WHICH ARE NOT THE SAME OBJECT.

  bridge role  Form-A/Form-B ratio  (1−h/2)/(1−z·h/2), whose O(h) Taylor
               coefficient IS (z−1)h/2. Lives in `q-beta-spectral-bridge`.
  cos role     the argument of cos(α − u/2) in the precision ladder.

They are routinely discussed as if the second were a "resummation" of the
first. It is not, and the numbers below say so: the bridge is a ~5 % object
and the cos factor is a 1e-6 object. The reason is elementary — `1 + α`
differs from 1 by α, while `cos α` differs from 1 by α²/2, so exponentiating
the same α into a cosine changes the size of the correction by 2/α ≈ 38.

CONSEQUENCE FOR "USE THE EXACT BRIDGE EVERYWHERE". In the bridge role the
exact form is already in use and its truncation error is already Lean-proved
(`bridge_first_order_remainder`, sorry-free: exact − truncated =
z(z−1)h²/4 / (1−z·h/2)). In the cos role the exact bridge is a different
quantity, ~5 % from what the data requires, so substituting it there would
replace a 1e-6 model with a 5 %-wrong one. Hence: no-op where it applies,
regression where it does not.

SCOPE. Scope-(a) throughout. Nothing here excludes any convention by a proved
invariant, and nothing here derives F.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))


def z_C(q):
    return mp.sqrt(q) / (1 + q)


def z_D(q):
    return q ** 3 / (q ** 2 + 1)


def q_a(q):
    return ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def candidates(q):
    """Every proposed multiplicative correction, in the F coordinate."""
    s = substrate_ladder_quantities(q)
    h, u = s["h"], s["u"]
    out = {"F_required": QCOD / q_a(q)}
    for nm, z in (("C", z_C(q)), ("D", z_D(q))):
        out[f"bridge_truncated_{nm}"] = 1 + (z - 1) * h / 2
        out[f"bridge_exact_{nm}"] = (1 - h / 2) / (1 - z * h / 2)
        out[f"cos_model_{nm}"] = mp.cos((z - 1) * h / 2 - u / 2) * (1 - u ** 2)
    return out, s


ORDER = ["bridge_truncated_C", "bridge_exact_C", "cos_model_C",
         "bridge_truncated_D", "bridge_exact_D", "cos_model_D"]


def main() -> int:
    q0 = q_at()
    c, s = candidates(q0)
    Freq = c["F_required"]

    print("=" * 78)
    print(" Q_β correction in the multiplicative coordinate F = Q_β/Q_A")
    print("=" * 78)
    print(f"\n  q₀ = {mp.nstr(q0, 18)}")
    print(f"  F_required = Q_codata/Q_A = {mp.nstr(Freq, 16)}")
    print(f"  1 − F_required            = {mp.nstr(1 - Freq, 10)}"
          "   ← the number a derivation must produce\n")
    print(f"  {'candidate':>20} {'value':>20} {'rel err vs F_req':>20}")
    print("  " + "-" * 62)
    rel = {}
    for k in ORDER:
        rel[k] = (c[k] - Freq) / Freq
        print(f"  {k:>20} {mp.nstr(c[k], 14):>20} {float(rel[k]):>20.3e}")

    # Slopes: F is smooth, so unlike α these are meaningful comparisons.
    d = mp.mpf("1e-5")
    lo, _ = candidates(q0 * (1 - d))
    hi, _ = candidates(q0 * (1 + d))
    slopes = {k: (hi[k] - lo[k]) / (2 * q0 * d)
              for k in ["F_required"] + ORDER}
    print(f"\n  {'candidate':>20} {'dF/dq':>16}")
    print("  " + "-" * 38)
    for k in ["F_required"] + ORDER:
        print(f"  {k:>20} {float(slopes[k]):>16.6f}")

    alpha_C = (z_C(q0) - 1) * s["h"] / 2
    magnifier = 2 / mp.fabs(alpha_C)

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  The bridge and the cos factor are NOT the same object.

    bridge (exact or truncated)   ~5e-2 from F_required
    cos model                     ~1e-6 from F_required

  Elementary reason: 1 + α differs from 1 by α, cos α differs from 1 by α²/2.
  Exponentiating the same α into a cosine changes the correction size by
  2/|α| = {float(magnifier):.1f}. So "cos-resummation" does not resum the bridge — it
  reuses the symbol α in a formula of different magnitude.

  The exact bridge is NOT closer to F_required than the truncated one
  ({float(rel['bridge_exact_C']):.3e} vs {float(rel['bridge_truncated_C']):.3e}); it is marginally further. So adopting the
  exact form cannot repair the cos-role sites — the gap there is not a
  truncation error.

  What the ladder actually asserts, stated cleanly in this coordinate:

      (1 − z_C)·h/2  ≈  sqrt( 2·(1 − Q_codata/Q_A) )

  an algebraic expression matching the square root of a near-cancellation,
  agreeing at q₀ to ~4e-4. Both sides are computable; neither is derived
  from the other.

  Slopes disagree in SIGN: dF_required/dq = {float(slopes['F_required']):+.4f} while every candidate
  is negative. As in the phase coordinate, the curves cross rather than track.
""")

    wb = WitnessBuilder("qbeta-F-coordinate-bridge-audit", engine="mpmath")
    wb.set_description(
        "Measures every proposed Q_β multiplicative correction in the "
        "coordinate F = Q_β/Q_A, which is smooth (unlike the phase α, whose "
        "square-root branch point 0.062% above q₀ is an artifact of the cos "
        "parameterisation). Establishes that the Form-A/Form-B bridge and the "
        "ladder's cos factor are DIFFERENT objects: the bridge sits ~5e-2 from "
        "what the data requires and the cos factor ~1e-6, because 1+α differs "
        "from 1 by α while cos α differs by α²/2 — a size change of 2/|α| ≈ 38. "
        "Consequence for 'use the exact bridge everywhere': in the bridge role "
        "the exact form is already in use with its truncation error Lean-proved "
        "(bridge_first_order_remainder, sorry-free); in the cos role the exact "
        "bridge is ~5% wrong, so substituting it would be a regression. The "
        "exact bridge is also NOT closer to F_required than the truncation. "
        "No fit; nothing wired; nothing derived."
    )
    wb.add_data("q0", fmt(q0))
    wb.add_data("F_required", fmt(Freq))
    wb.add_data("one_minus_F_required", fmt(1 - Freq))
    wb.add_data("candidates", {k: fmt(c[k]) for k in ORDER})
    wb.add_data("relative_error_vs_F_required", {k: fmt(rel[k]) for k in ORDER})
    wb.add_data("slopes_dF_dq", {k: fmt(v) for k, v in slopes.items()})
    wb.add_data("cos_vs_linear_magnifier", fmt(magnifier))

    wb.add_assertion(
        name="bridge_and_cos_factor_differ_by_more_than_four_orders",
        computed=str(int(
            mp.fabs(rel["bridge_exact_C"]) > 1e4 * mp.fabs(rel["cos_model_C"]))),
        expected="1", tolerance=0,
        source=(
            f"|rel(bridge_exact_C)| = {mp.nstr(mp.fabs(rel['bridge_exact_C']), 6)} vs "
            f"|rel(cos_model_C)| = {mp.nstr(mp.fabs(rel['cos_model_C']), 6)}. The two are "
            "not variants of one correction; treating the cos factor as a "
            "resummation of the bridge conflates objects of different size."
        ),
    )
    wb.add_assertion(
        name="exact_bridge_is_not_closer_to_F_required_than_truncated",
        computed=str(int(
            mp.fabs(rel["bridge_exact_C"]) >= mp.fabs(rel["bridge_truncated_C"]))),
        expected="1", tolerance=0,
        source=(
            "Adopting the exact bridge in place of its O(h) truncation does "
            "not move the cos-role sites toward the required correction — it "
            "is marginally further away. The discrepancy there is not a "
            "truncation error, so it cannot be fixed by de-truncating."
        ),
    )
    wb.add_assertion(
        name="F_required_slope_sign_opposes_every_candidate",
        computed=str(int(all(slopes["F_required"] * slopes[k] < 0
                             for k in ORDER))),
        expected="1", tolerance=0,
        source=(
            f"dF_required/dq = {mp.nstr(slopes['F_required'], 8)} > 0 while every "
            "candidate slope is negative. The curves cross rather than track, "
            "reproducing in the smooth coordinate what the phase coordinate "
            "showed — so that finding is not an artifact of the arccos."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
