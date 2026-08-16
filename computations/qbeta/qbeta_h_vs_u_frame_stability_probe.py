#!/usr/bin/env python3
"""qbeta_h_vs_u_frame_stability_probe.py — does re-expressing the Q_β ladder
in `h = q − 1/q` instead of `u = b·ℏ_q²` fix the anchor-instability?

DECISIVE TEST, and the answer is NO.

MOTIVATION. `u ∼ h²`, so reverting `u → h` needs `√u` and the ladder is
non-analytic at `u = 0` (already corpus knowledge:
`qbeta_ck_from_operator_markov_trace_probe`). The literature's natural
variable is `h`: the Ohtsuki series is a power series in `q − 1` with integral
coefficients, and α_EM's Habiro element is already written `[2]_q·(1 − h²α)`.
That is a real argument for re-expressing the Q_β ladder in `h` — it would be
analytic, integer-power, able to carry the odd rungs `u` structurally cannot,
and consistent with the α_EM channel.

Before paying for that migration (it is a relabelling sweep of the same class
as convention C→D), the cheap question: does the h-frame actually behave
better? Specifically, are h-frame coefficients anchor-stable where u-frame
ones drift? The `c_k ≥ 3` are recorded corpus-wide as "q₀-dependent
NEAR-MATCHES", and a leakage argument suggests why a coarse integer-`u` series
might drift: it cannot represent the half-integer content, so that content has
to be absorbed into its coefficients.

THE TEST. Extract the same residual in both frames at MATCHED magnification —
`h^k` chosen so `h^k ≈ u³` — so neither frame is flattered by dividing by a
smaller number. Then compare cross-anchor relative swings.

    R(q) := Q_codata / (Q_A · cos(α − u/2)·(1 + c₂u²)) − 1,   c₂ = −1

    u-frame coefficient:  R / u³
    h-frame coefficient:  R / h^k

RESULT. The two swings agree to five significant figures, and both equal the
swing of `R` itself. The variables' own cross-anchor swings are ~1e-6, i.e.
negligible. **The instability is in the residual, not in the coordinate**, so
no change of expansion variable can remove it.

CONSEQUENCE. The leakage hypothesis is REFUTED as the explanation of this
drift (scope-(a): as the explanation of *this* drift, at *these* anchors —
not as a general statement about half-integer content). The h-reframe remains
justified on other grounds (analyticity, odd-rung expressiveness, Ohtsuki /
Habiro alignment, α_EM consistency) but buys NOTHING numerical, at ~3× the
rungs for the same precision. Whoever scopes that migration should do so
knowing it is hygiene, not a fix.

The deeper reading, consistent with the phase-crossing result in
`qbeta_ladder_required_phase_probe`: the model's q-dependence does not match
the data's, and that is a property of the model, not of the coordinate it is
written in.

Anchors: proton (experimental, default per the 2026-08-07 directive) and muon
(ideal CAL-2). Each anchor's quantities are computed entirely within its own
layer — no straddle.
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
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
C2 = mp.mpf(-1)


def z_C(q):
    return mp.sqrt(q) / (1 + q)


def q_a(q):
    return ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def residual(q):
    """R = Q_codata/(Q_A · M) − 1 for the committed model M through N=2."""
    s = substrate_ladder_quantities(q)
    u, h = s["u"], s["h"]
    alpha = (z_C(q) - 1) * h / 2
    M = mp.cos(alpha - u / 2) * (1 + C2 * u ** 2)
    return QCOD / (q_a(q) * M) - 1, u, h


def rel_swing(a, b):
    return mp.fabs(b - a) / mp.fabs(a)


def main() -> int:
    qp, qm = q_at(), q_muon_at()
    Rp, up, hp = residual(qp)
    Rm, um, hm = residual(qm)

    # Match magnification so neither frame is flattered by a smaller divisor.
    k = int(mp.nint(mp.log(up ** 3) / mp.log(hp)))

    cu_p, cu_m = Rp / up ** 3, Rm / um ** 3
    ch_p, ch_m = Rp / hp ** k, Rm / hm ** k

    sw_u = rel_swing(cu_p, cu_m)
    sw_h = rel_swing(ch_p, ch_m)
    sw_R = rel_swing(Rp, Rm)

    print("=" * 78)
    print(" Does the h-frame fix the anchor-instability?  (matched magnification)")
    print("=" * 78)
    print(f"\n  matched exponent: u³ = {float(up**3):.4e}   h^{k} = {float(hp**k):.4e}\n")
    print(f"  {'frame':>8} {'proton':>16} {'muon':>16} {'rel swing':>12}")
    print("  " + "-" * 56)
    print(f"  {'u^3':>8} {float(cu_p):>16.6f} {float(cu_m):>16.6f} {float(sw_u):>12.4%}")
    print(f"  {'h^'+str(k):>8} {float(ch_p):>16.6f} {float(ch_m):>16.6f} {float(sw_h):>12.4%}")
    print(f"\n  residual R      {float(Rp):>16.6e} {float(Rm):>16.6e} {float(sw_R):>12.4%}")
    print(f"  u³ own swing  {float(rel_swing(up**3, um**3)):.3e}"
          f"      h^{k} own swing  {float(rel_swing(hp**k, hm**k)):.3e}")

    print(f"""
{'=' * 78}
 Verdict — NO. The reframe does not fix it.
{'=' * 78}

  Both frames swing {float(sw_u):.4%}, agreeing to five significant figures, and both
  equal the swing of R itself ({float(sw_R):.4%}). The variables' own swings are ~1e-6.
  The instability is in the RESIDUAL, not the coordinate, so no change of
  expansion variable can remove it.

  This REFUTES the leakage hypothesis as the explanation of this drift —
  scope-(a): as the explanation of THIS drift at THESE anchors, not as a
  general claim about half-integer content.

  The h-reframe keeps its other justifications: analyticity, the ability to
  carry odd rungs that integer-u structurally cannot, alignment with the
  Ohtsuki series (a power series in q-1 with integral coefficients), and
  consistency with alpha_EM's Habiro element [2]_q(1 - h^2 a), already written
  in h. But it buys nothing numerical, at ~3x the rungs for equal precision
  (7.2 -> 22.1 for 1e-15). Scope the migration as hygiene, not as a fix.

  Consistent with the phase-crossing result: the model's q-dependence does not
  match the data's. That is a property of the model, not of its coordinate.
""")

    wb = WitnessBuilder("qbeta-h-vs-u-frame-stability", engine="mpmath")
    wb.set_description(
        "Tests whether re-expressing the Q_β ladder in h = q − 1/q instead of "
        "u = b·ℏ_q² fixes the cross-anchor instability of the extracted "
        "coefficients. Extracts the same residual in both frames at MATCHED "
        "magnification (h^k chosen so h^k ≈ u³) so neither frame is flattered "
        "by a smaller divisor. Result: both swing identically to five "
        "significant figures, and both equal the swing of the residual itself "
        "— the instability is in the residual, not the coordinate. Refutes the "
        "leakage hypothesis as the explanation of this drift (scope-(a)). The "
        "h-reframe keeps its other justifications (analyticity, odd-rung "
        "expressiveness, Ohtsuki/Habiro alignment, α_EM consistency) but buys "
        "nothing numerical at ~3× the rungs. No fit; nothing wired."
    )
    wb.add_data("matched_exponent_k", k)
    wb.add_data("anchors", {
        "proton": {"q": fmt(qp), "u": fmt(up), "h": fmt(hp),
                   "residual": fmt(Rp), "coeff_u3": fmt(cu_p),
                   f"coeff_h{k}": fmt(ch_p)},
        "muon": {"q": fmt(qm), "u": fmt(um), "h": fmt(hm),
                 "residual": fmt(Rm), "coeff_u3": fmt(cu_m),
                 f"coeff_h{k}": fmt(ch_m)},
    })
    wb.add_data("relative_swings", {
        "u_frame": fmt(sw_u), "h_frame": fmt(sw_h), "residual": fmt(sw_R),
        "u3_itself": fmt(rel_swing(up ** 3, um ** 3)),
        f"h{k}_itself": fmt(rel_swing(hp ** k, hm ** k)),
    })

    wb.add_assertion(
        name="h_frame_swing_equals_u_frame_swing",
        computed=fmt(sw_h), expected=fmt(sw_u), tolerance=mp.mpf("1e-6"),
        source=(
            "Matched magnification, so the comparison is fair. The two frames "
            "swing identically — changing the expansion variable does not "
            "change the anchor-instability at all."
        ),
    )
    wb.add_assertion(
        name="both_swings_equal_the_residual_swing",
        computed=str(int(rel_swing(sw_u, sw_R) < mp.mpf("1e-4")
                         and rel_swing(sw_h, sw_R) < mp.mpf("1e-4"))),
        expected="1", tolerance=0,
        source=(
            f"u-frame {mp.nstr(sw_u, 8)}, h-frame {mp.nstr(sw_h, 8)}, residual "
            f"{mp.nstr(sw_R, 8)}. The coefficient swing IS the residual swing; "
            "the divisors contribute ~1e-6. So the instability is a property "
            "of the model's q-dependence, not of the coordinate."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
