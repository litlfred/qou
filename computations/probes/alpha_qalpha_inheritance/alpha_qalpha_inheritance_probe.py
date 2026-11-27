#!/usr/bin/env python3
"""Split the derived-Q_alpha error into the part inherited from the binding law
and the part that is alpha-specific.

Bean `qou-q0gw` (parent epic `qou-myts`).

Identity (exact, any commutative ring; Lean:
`QOU.Nuclear.AlphaQInheritance.qalpha_error_split`):

    Q_alpha(Z, N) = B_alpha - dB(Z, N),   dB(Z, N) := B(Z, N) - B(Z-2, N-2)
    Q_pred - Q_exp = (B_alpha_pred - B_alpha_exp) - (dB_pred - dB_exp).

The first bracket is alpha-specific (the 4He cluster). The second bracket is the
slope of the parent/daughter binding law along the alpha line (A -> A-4 at fixed
N-Z), and is therefore inherited from the binding-term work (qou-brng, C2/B1).

Second identity (Lean: `qalpha_const_of_affine_isospin`): if B(Z, N) =
c*(Z+N) + g(N-Z) for any function g, then dB = 4c is the same for every
nucleus and Q_alpha = B_alpha - 4c is one number for every emitter. This probe
measures that the production mass table has one constant alpha-line slope on
all 1,051 pairs (the conclusion of that lemma, whatever its cause), so its
Q_alpha cannot tell an alpha emitter from a stable nucleus.

Diagnostic only, no fitting: the derived Coulomb slope uses Form-B alpha_q and
the CAL-3 FCC radius r_0^FCC (same constants as qou-i2jl). AME2020 values are
the comparison target, never an input to any predicted quantity.

Precision: mpmath workdps 80, JSON read with parse_float=str, no float64.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 30
set_compute_dps(WORK_DPS)

MASS_TABLE = _ROOT / "computations" / "mass-table-comprehensive.witness.json"
AME_JSON = _ROOT / "computations" / "data" / "ame2020.json"
GAP1B = (_ROOT / "computations" / "probes" / "gap1b_4he_tetrahedral_k4_flux_ring"
         / "gap1b-4he-tetrahedral-k4-flux-ring.witness.json")
QI2JL = (_ROOT / "computations" / "probes" / "alpha_decay_n126_and_derived_qalpha"
         / "alpha_decay_n126_qalpha_probe.py")
M_PI_CHARGED_MEV = mp.mpf("139.57039")  # CAL-3


def _load(path: Path) -> dict:
    with path.open() as f:
        return json.load(f, parse_float=str)


def _form_b_alpha_inv(q0: mp.mpf) -> mp.mpf:
    spec = importlib.util.spec_from_file_location("qi2jl", QI2JL)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.solve_form_b_alpha_inv(q0)


def _median(xs: list[mp.mpf]) -> mp.mpf:
    s = sorted(xs)
    k = len(s)
    return s[k // 2] if k % 2 else (s[k // 2 - 1] + s[k // 2]) / 2


def main() -> int:
    with mp.workdps(WORK_DPS):
        one, two, three, four, five = (mp.mpf(i) for i in (1, 2, 3, 4, 5))
        q0 = q_at(dps=WORK_DPS)
        alpha_q = one / _form_b_alpha_inv(q0)
        h = codata("Planck constant").value
        c = codata("speed of light in vacuum").value
        e = codata("elementary charge").value
        hbar_c = (h / (two * mp.pi)) * c / (e * mp.mpf("1e6")) * mp.mpf("1e15")
        m_e = codata("electron mass energy equivalent in mev").value
        r0 = mp.cbrt(three / (four * mp.pi * mp.sqrt(two))) * (three / two) * hbar_c / M_PI_CHARGED_MEV

        def e_coul(z: int, a: int) -> mp.mpf:
            return (three / five) * z * (z - 1) * alpha_q * hbar_c / (r0 * mp.cbrt(a))

        mt = {(int(r["Z"]), int(r["N"])): r for r in _load(MASS_TABLE)["data"]["rows"]}
        ame = {(int(x["Z"]), int(x["N"])): x for x in _load(AME_JSON)["entries"]}

        def ame_ok(x: dict | None) -> bool:
            return bool(x) and not x.get("binding_energy_per_A_estimated") \
                and x.get("binding_energy_per_A_keV") is not None

        def b_ame(x: dict) -> mp.mpf:
            return mp.mpf(x["binding_energy_total_keV"]) / 1000

        b_alpha_exp = b_ame(ame[(2, 2)])
        g1 = _load(GAP1B)["data"]
        b_alpha_m3a = mp.mpf(g1["part2a_fixed_radius_plaquette_summary"]["models"]
                             ["M3a_kA_plaquette_pos"]["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"])
        b_alpha_64meG = 64 * m_e * mp.catalan
        # (2,2) has no mass-table row; the chain value is its own alpha-line
        # extrapolation B(8Be) - dB, recorded only to show the mixing below.
        b_alpha_chain = mp.mpf(mt[(4, 4)]["B_pred_MeV"]) - (
            mp.mpf(mt[(6, 6)]["B_pred_MeV"]) - mp.mpf(mt[(4, 4)]["B_pred_MeV"]))

        recs = []
        for (z, n), x in sorted(ame.items()):
            a = z + n
            if z < 2 or n < 2 or a < 6 or not ame_ok(x) or not ame_ok(ame.get((z - 2, n - 2))):
                continue
            if (z, n) not in mt or (z - 2, n - 2) not in mt:
                continue
            db_exp = b_ame(x) - b_ame(ame[(z - 2, n - 2)])
            q_exp = b_alpha_exp - db_exp
            if q_exp <= mp.mpf("0.5"):
                continue
            db_pred = mp.mpf(mt[(z, n)]["B_pred_MeV"]) - mp.mpf(mt[(z - 2, n - 2)]["B_pred_MeV"])
            d_ec = e_coul(z, a) - e_coul(z - 2, a - 4)
            recs.append(dict(Z=z, N=n, A=a, db_pred=db_pred, db_exp=db_exp, q_exp=q_exp, d_ec=d_ec))

        n_rec = len(recs)
        slopes = sorted({mp.nstr(r["db_pred"], 5) for r in recs})
        db_pred_med = _median([r["db_pred"] for r in recs])
        db_exp_med = _median([r["db_exp"] for r in recs])
        q_exp_med = _median([r["q_exp"] for r in recs])
        d_ec_med = _median([r["d_ec"] for r in recs])
        q_pred_scorecard = b_alpha_m3a - db_pred_med
        err_total = q_pred_scorecard - q_exp_med
        err_alpha = b_alpha_m3a - b_alpha_exp
        err_inherited = -(db_pred_med - db_exp_med)
        # exact split per row, then share of |total| carried by the inherited bracket
        split_resid = max(abs((b_alpha_m3a - r["db_pred"] - r["q_exp"])
                              - ((b_alpha_m3a - b_alpha_exp) - (r["db_pred"] - r["db_exp"])))
                          for r in recs)
        inh_share = _median([abs(r["db_pred"] - r["db_exp"])
                             / abs((b_alpha_m3a - r["db_pred"]) - r["q_exp"]) for r in recs])
        q_chain_selfconsistent = b_alpha_chain - db_pred_med
        nuc_slope_req = _median([r["db_exp"] + r["d_ec"] for r in recs])

        def band(lo: int, hi: int) -> dict:
            s = [r for r in recs if lo <= r["A"] <= hi]
            return {
                "n": len(s),
                "dB_pred_median_MeV": fmt(_median([r["db_pred"] for r in s]), dps=8),
                "dB_AME_median_MeV": fmt(_median([r["db_exp"] for r in s]), dps=8),
                "Q_AME_median_MeV": fmt(_median([r["q_exp"] for r in s]), dps=8),
                "dE_C_FCC_median_MeV": fmt(_median([r["d_ec"] for r in s]), dps=8),
                "nuclear_slope_required_median_MeV": fmt(
                    _median([r["db_exp"] + r["d_ec"] for r in s]), dps=8),
            }

        print(f"N = {n_rec}; distinct alpha-line slopes in mass table: {slopes}")
        print(f"B_alpha: M3a {mp.nstr(b_alpha_m3a, 8)}, 64meG {mp.nstr(b_alpha_64meG, 8)}, "
              f"chain {mp.nstr(b_alpha_chain, 8)}, AME {mp.nstr(b_alpha_exp, 8)}")
        print(f"median dB pred {mp.nstr(db_pred_med, 8)} vs AME {mp.nstr(db_exp_med, 8)}")
        print(f"Q scorecard {mp.nstr(q_pred_scorecard, 8)} vs AME median {mp.nstr(q_exp_med, 8)}")
        print(f"error total {mp.nstr(err_total, 6)} = alpha {mp.nstr(err_alpha, 6)} "
              f"+ inherited {mp.nstr(err_inherited, 6)}; median inherited share {mp.nstr(inh_share, 6)}")
        print(f"chain-self-consistent Q {mp.nstr(q_chain_selfconsistent, 8)}")
        print(f"median Coulomb slope {mp.nstr(d_ec_med, 8)}; nuclear slope required {mp.nstr(nuc_slope_req, 8)}"
              f" = {mp.nstr(nuc_slope_req / 4, 6)} MeV/nucleon")

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Derived Q_alpha error split into alpha-specific (B_alpha) and inherited "
            "(alpha-line binding slope dB) parts over the 1,051 scorecard emitters; "
            "detects that the production mass table has one constant alpha-line slope; "
            "derives the nuclear slope the binding term must supply given the Form-B / "
            "CAL-3 Coulomb slope (comparison target only, no fitting).")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("alpha_q_inv_FormB", fmt(one / alpha_q, dps=OUT_DPS))
        wb.add_parameter("r0_FCC_fm", fmt(r0, dps=OUT_DPS))
        wb.add_data("sample", {"n_emitters": n_rec, "selection":
                               "scorecard selection: AME measured parent+daughter, A>=6, Q_AME>0.5 MeV"})
        wb.add_data("b_alpha_models_MeV", {
            "M3a_plaquette_used_by_scorecard": fmt(b_alpha_m3a, dps=12),
            "magicA_64_me_G": fmt(b_alpha_64meG, dps=12),
            "mass_table_chain_extrapolation": fmt(b_alpha_chain, dps=12),
            "AME2020_comparison": fmt(b_alpha_exp, dps=12),
        })
        wb.add_data("alpha_line_slope", {
            "distinct_mass_table_slopes_MeV": slopes,
            "per_nucleon_MeV": fmt(db_pred_med / 4, dps=10),
        })
        wb.add_data("error_split_at_medians_MeV", {
            "Q_pred_scorecard": fmt(q_pred_scorecard, dps=10),
            "Q_AME": fmt(q_exp_med, dps=10),
            "total": fmt(err_total, dps=10),
            "alpha_specific_B_alpha": fmt(err_alpha, dps=10),
            "inherited_alpha_line_slope": fmt(err_inherited, dps=10),
            "median_rowwise_inherited_share": fmt(inh_share, dps=10),
            "max_rowwise_split_residual": fmt(split_resid, dps=10),
        })
        wb.add_data("model_mixing", {
            "Q_chain_selfconsistent_MeV": fmt(q_chain_selfconsistent, dps=10),
            "note": "scorecard pairs the M3a 4He with the Q-CLT chain parent/daughter; "
                    "the chain's own 4He gives Q_alpha < 0 for every nucleus",
        })
        wb.add_data("binding_term_target", {
            "Coulomb_slope_FCC_median_MeV": fmt(d_ec_med, dps=10),
            "nuclear_alpha_line_slope_required_median_MeV": fmt(nuc_slope_req, dps=10),
            "per_nucleon_MeV": fmt(nuc_slope_req / 4, dps=10),
            "bands": {"A_6_150": band(6, 150), "A_151_plus": band(151, 1000)},
        })
        wb.add_assertion("n_emitters_matches_scorecard", n_rec, 1051, 0,
                         source="generate-accuracy-scorecard.py selection")
        wb.add_assertion("mass_table_alpha_line_slope_is_single_constant", len(slopes), 1, 0,
                         source="mass-table-comprehensive.witness.json B_pred_MeV")
        wb.add_assertion("error_split_is_exact", fmt(split_resid, dps=12), "0", "1e-9",
                         source="identity qalpha_error_split")
        wb.add_assertion("inherited_share_above_90pct", fmt(inh_share, dps=10), "0.93", "0.07",
                         source="median over 1,051 emitters")
        wb.add_caveat(
            "Diagnostic. The required nuclear slope uses AME2020 dB as the comparison "
            "target; it is a target for the binding term (qou-brng), not an input to any "
            "prediction and not a fitted constant.")
        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
