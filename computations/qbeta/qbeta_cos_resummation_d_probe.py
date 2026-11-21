"""qbeta_cos_resummation_d_probe.py — convention-D producer for
`prop:q-beta-cos-resummation` (bean `qou-zuva`).

The block dresses a Q_beta base by the classical cosine of the half eigenphase,

    Q_beta^cos = Q_beta^base * cos(alpha),   alpha = (z_D - 1) h / 2,
    z_D = q^3/(q^2+1),   h = q - 1/q,

evaluated at the proton pin. This producer recomputes every number the block
quotes, in mpmath, and replaces the convention-C producer the block used to
point at (`computations/probe_q_beta_tightening_landscape.py`).

Two bases are reported side by side and NEITHER is selected by its residual:

* RULED base (owner ruling 2026-09-08: epsilon is the Markov trace at z_D):
      Q^{z_D} = |h^2/2 - h z_D| * E_0,   E_0 = m_e / (q (q - 1)).
  This is `per_observable_100x_status._qbeta_ruled_base` at order-zero E_0.
* Form A (retired as the base; historical cross-check only):
      Q^A = m_e |q^2 - 2q - 1| (q + 1) / (2 q^3).

Downstream: the n-p mass-split residual inherits Q_beta's residual through
the chain identity of `computations/audit_delta_S_chain.py`,

    eps_DeltaS = (Q_pred - Q_ref) / (Q_ref + m_e) = eps_Q * Q_ref/(Q_ref + m_e),

so each cell also carries its eps_DeltaS. The block's former figures
`eps_DeltaS 1015 -> 185 ppm` are CONVENTION-C on the Form A base; the
convention-C eigenphase is recomputed here ONLY as a labelled historical
comparison (`*_C_historical`), so the old figure can be scoped rather than
quoted. Nothing canonical in this file uses it.

Also checked numerically (the Lean sibling proves them generically,
sorry-free): the bar involution does not fix z_D, and
alpha_D(1/q) + alpha_D(q) = (q^2 - 1)^2 / (2 q^2) != 0, which is why the
convention-C evenness argument for the cosine does not transfer to D.

Scope (a): numerics on the stated assembly; no fit, nothing selected.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (ROOT, ROOT / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp                                            # noqa: E402
from _precision import set_compute_dps, fmt                    # noqa: E402
set_compute_dps()
import qou_substrate.constants as CONST                        # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV               # noqa: E402
from witness_base import WitnessBuilder                        # noqa: E402

# Values as printed in the block .md / table-data (10 sig. figs, ppm to 0.1).
PUBLISHED = {
    "z_D": "0.6126880371",
    "h": "0.2090602988",
    "alpha_D": "-0.0404857773",
    "cos_alpha_D": "0.9991805629",
    "Q_ruled_MeV": "0.4447004085",
    "Q_ruled_cos_MeV": "0.4443360045",
    "Q_formA_MeV": "0.7836458274",
    "Q_formA_cos_D_MeV": "0.7830036789",
}
PUBLISHED_PPM = {
    "ruled": "-431571.8",
    "ruled_cos": "-432037.5",
    "formA": "1677.6",
    "formA_cos_D": "856.8",
}
PPM = mp.mpf(10) ** 6


def main() -> int:
    q = mp.mpf(str(CONST.Q_50_DIGIT_STR))
    m_e = mp.mpf(M_E_MEV)
    Q_ref = mp.mpf(Q_BETA_MEV)

    h = q - 1 / q
    z_D = q**3 / (q**2 + 1)
    alpha_D = (z_D - 1) * h / 2
    cos_D = mp.cos(alpha_D)

    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    Q_ruled = abs(h**2 / 2 - h * z_D) * E0
    Q_formA = m_e * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)

    # Convention C — HISTORICAL comparison only (excised; never canonical).
    z_C_historical = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    alpha_C_historical = (z_C_historical - 1) * h / 2
    cos_C_historical = mp.cos(alpha_C_historical)

    cells = {
        "ruled": Q_ruled,
        "ruled_cos": Q_ruled * cos_D,
        "formA": Q_formA,
        "formA_cos_D": Q_formA * cos_D,
        "formA_cos_C_historical": Q_formA * cos_C_historical,
    }

    def eps_Q(Qp):
        return (Qp - Q_ref) / Q_ref

    def eps_DS(Qp):
        return (Qp - Q_ref) / (Q_ref + m_e)

    rows = []
    print("=" * 76)
    print(" prop:q-beta-cos-resummation — convention D at the proton pin")
    print("=" * 76)
    print(f"  q0 = {mp.nstr(q, 17)}   m_e = {mp.nstr(m_e, 12)}   "
          f"Q_ref (CODATA) = {mp.nstr(Q_ref, 10)} MeV")
    print(f"  z_D = {mp.nstr(z_D, 11)}  h = {mp.nstr(h, 11)}  "
          f"alpha_D = {mp.nstr(alpha_D, 11)}  cos = {mp.nstr(cos_D, 11)}")
    print()
    print(f"  {'cell':26s} {'Q (MeV)':>16s} {'eps_Q (ppm)':>14s} "
          f"{'eps_DeltaS (ppm)':>17s}")
    for nm, Qp in cells.items():
        eq, eds = eps_Q(Qp) * PPM, eps_DS(Qp) * PPM
        rows.append({"cell": nm, "Q_MeV": fmt(Qp), "eps_Q_ppm": fmt(eq),
                     "eps_DeltaS_ppm": fmt(eds)})
        print(f"  {nm:26s} {mp.nstr(Qp, 11):>16s} {mp.nstr(eq, 8):>14s} "
              f"{mp.nstr(eds, 8):>17s}")

    damping = Q_ref / (Q_ref + m_e)
    print(f"\n  damping Q_ref/(Q_ref + m_e) = {mp.nstr(damping, 10)}")

    # ---- checks -----------------------------------------------------------
    worst_val = mp.mpf(0)
    vals = {"z_D": z_D, "h": h, "alpha_D": alpha_D, "cos_alpha_D": cos_D,
            "Q_ruled_MeV": Q_ruled, "Q_ruled_cos_MeV": Q_ruled * cos_D,
            "Q_formA_MeV": Q_formA, "Q_formA_cos_D_MeV": Q_formA * cos_D}
    for k, v in vals.items():
        worst_val = max(worst_val, abs(v - mp.mpf(PUBLISHED[k])))
    worst_ppm = mp.mpf(0)
    for k, s in PUBLISHED_PPM.items():
        worst_ppm = max(worst_ppm, abs(eps_Q(cells[k]) * PPM - mp.mpf(s)))

    cos_le_one = cos_D <= 1
    ruled_moves_away = abs(eps_Q(cells["ruled_cos"])) > abs(eps_Q(cells["ruled"]))
    bar_defect_z = abs(q**3 / (q**2 + 1) - (1 / q**3) / (1 / q**2 + 1))
    alpha_inv = ((1 / q) ** 3 / ((1 / q) ** 2 + 1) - 1) * (1 / q - q) / 2
    bar_even = alpha_inv + alpha_D
    bar_even_closed = (q**2 - 1) ** 2 / (2 * q**2)
    chain_identity = abs(eps_DS(cells["formA"])
                         - damping * eps_Q(cells["formA"]))

    print(f"  max |value - published|        = {mp.nstr(worst_val, 3)}")
    print(f"  max |ppm - published ppm|      = {mp.nstr(worst_ppm, 3)}")
    print(f"  cos(alpha_D) <= 1              = {cos_le_one}")
    print(f"  ruled base: cos moves residual away from zero = {ruled_moves_away}")
    print(f"  |z_D(q) - z_D(1/q)|            = {mp.nstr(bar_defect_z, 12)}")
    print(f"  alpha_D(1/q) + alpha_D(q)      = {mp.nstr(bar_even, 12)}"
          f"  (closed form {mp.nstr(bar_even_closed, 12)})")

    wb = WitnessBuilder("qbeta-cos-resummation-d", engine="mpmath")
    wb.set_description(
        "Convention-D numbers for prop:q-beta-cos-resummation at the proton "
        "pin: z_D, h, alpha_D = (z_D-1)h/2, cos(alpha_D); the ruled z_D base "
        "and the retired Form A base, each bare and cos-dressed, with eps_Q "
        "and the downstream n-p split residual eps_DeltaS = (Q-Q_ref)/(Q_ref+"
        "m_e). Neither base is selected by residual. A convention-C eigenphase "
        "is carried only as a labelled historical comparison so the block's "
        "superseded eps_DeltaS 1015 -> 185 ppm can be scoped as C-measured."
    )
    wb.add_parameter("q0", fmt(q))
    wb.add_parameter("m_e_MeV", fmt(m_e))
    wb.add_parameter("Q_beta_ref_MeV", fmt(Q_ref))
    wb.add_parameter("convention", "D (z = q^3/(q^2+1)); C rows historical only")
    wb.add_data("z_D", fmt(z_D))
    wb.add_data("h", fmt(h))
    wb.add_data("alpha_D", fmt(alpha_D))
    wb.add_data("cos_alpha_D", fmt(cos_D))
    wb.add_data("E0_MeV", fmt(E0))
    wb.add_data("damping_Qref_over_Qref_plus_me", fmt(damping))
    wb.add_data("cells", rows)
    wb.add_data("z_C_historical", fmt(z_C_historical))
    wb.add_data("cos_alpha_C_historical", fmt(cos_C_historical))
    wb.add_data("bar_defect_abs_zD_q_minus_zD_inv_q", fmt(bar_defect_z))
    wb.add_data("alpha_D_bar_even_sum", fmt(bar_even))
    wb.add_assertion(
        name="reproduces_block_published_values",
        computed=fmt(worst_val), expected="0", tolerance="1e-10",
        source="q-beta-cos-resummation.md / -table-data.md, 10 significant "
               "figures")
    wb.add_assertion(
        name="reproduces_block_published_ppm",
        computed=fmt(worst_ppm), expected="0", tolerance="0.051",
        source="residuals quoted to 0.1 ppm in the block")
    wb.add_assertion(
        name="ruled_base_cos_moves_residual_away_from_zero",
        computed="1" if (cos_le_one and ruled_moves_away) else "0",
        expected="1", tolerance="0",
        source="cos(alpha) <= 1 while the ruled base lies below Q_ref")
    wb.add_assertion(
        name="alpha_D_bar_even_part_matches_closed_form",
        computed=fmt(abs(bar_even - bar_even_closed)), expected="0",
        tolerance="1e-40",
        source="Lean QOU.Interactions.eigenphase_bar_even_sum")
    wb.add_assertion(
        name="eps_DeltaS_chain_identity",
        computed=fmt(chain_identity), expected="0", tolerance="1e-40",
        source="computations/audit_delta_S_chain.py chain identity")
    out = wb.save()
    print(f"\n  witness: {out}")
    ok = (worst_val < mp.mpf("1e-10") and worst_ppm < mp.mpf("0.051")
          and cos_le_one and ruled_moves_away
          and abs(bar_even - bar_even_closed) < mp.mpf("1e-40")
          and chain_identity < mp.mpf("1e-40") and bar_defect_z > 0)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
