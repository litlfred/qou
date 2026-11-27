#!/usr/bin/env python3
"""Strong-sector unified-binding probe -- AN ANCHOR-INVERSION DIAGNOSTIC.

READ THIS BEFORE QUOTING ANY NUMBER THIS SCRIPT PRINTS.

**The `err` column is zero by construction on two of its four rows.** All three
weights below are solved directly out of the AME2020 table the probe is then
scored against:

    w_2 <- AME_B["D"]                       (A = 2)
    w_3 <- (AME_B["T"] + AME_B["3He"]) / 2  (A = 3 mirror mean)
    w_4 <- AME_B["4He"]                     (A = 4)

Substituting them back into the scoring loop gives, identically:

    D   (A=2)  B_inv == AME_B["D"]                    -> err == 0
    T   (A=3)  B_inv == (AME_B["T"] + AME_B["3He"])/2 -> err == +/- half the T-3He split
    3He (A=3)  likewise
    4He (A=4)  B_inv == AME_B["4He"]                  -> err == 0

Three free parameters inverted from four empirical points (`x - x = 0`, not a
derived closure or `1 ppq` prediction).

**`na_stokes_gluonic` and `na_stokes_residual` are NOT USED.** They are assigned
and printed for reference only and enter neither `w_n` nor `B_inv`.

Under AGENTS.md "NO FITTING, EXCEPT CAL-1/2/3", this script is kept solely as an
honest negative / scale-inversion diagnostic showing what `w_2, w_3, w_4` would
have to equal, NOT as a derivation and NOT as a live `B_unified` model (bean
`qou-kjik`).
"""
from __future__ import annotations

import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent))

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from binding_manybody_jet_filtration import a_D, NUCLEONS, AME_B, M_E  # noqa: E402

set_compute_dps()
WORK_DPS = 80
OUT_DPS = 50


def main() -> int:
    with mp.workdps(WORK_DPS):
        wb = WitnessBuilder("strong-unified-binding-probe", engine="mpmath")
        q0 = q_at(WORK_DPS)

        print("===================================================================")
        print("  Strong-Sector Scale-Inversion Diagnostic (Anchor Inversion Only) ")
        print("===================================================================")

        # Reference topological ratios from strong_force_na_stokes_kernel.md
        # NOTE: printed for comparison only; NEITHER constant enters w_n or B_inv below.
        na_stokes_gluonic = mp.mpf(3)
        na_stokes_residual = mp.mpf(5) / mp.mpf(2)

        print("\n[Reference Kernel Ratios (UNUSED in w_n inversion below)]")
        print(f"Gluonic reference ratio  (3)   : {mp.nstr(na_stokes_gluonic, 6)}")
        print(f"Residual reference ratio (5/2) : {mp.nstr(na_stokes_residual, 6)}")

        # Algebraic anchor inversion (3 weights solved directly from 4 AME2020 values):
        ad2 = a_D(2)
        ad3 = a_D(3)
        ad4 = a_D(4)
        w_2 = AME_B["D"] / (M_E * ad2)
        B_3_avg = (AME_B["T"] + AME_B["3He"]) / 2
        w_3 = (B_3_avg - M_E * ad2 * w_2) / (M_E * ad3)
        w_4 = (AME_B["4He"] - M_E * (ad2 * w_2 + ad3 * w_3)) / (M_E * ad4)

        print("\n[Inverted Target Weights w_n (solved from AME_B, free_parameters = 3)]")
        print(f"w_2 (from D)          = {mp.nstr(w_2, 8)}")
        print(f"w_3 (from T/3He mean) = {mp.nstr(w_3, 8)}")
        print(f"w_4 (from 4He)        = {mp.nstr(w_4, 8)}")

        print("\n[Identity Back-Substitution Check (MeV)]")
        rows = {}
        for K, A in NUCLEONS.items():
            B_inv = mp.mpf(0)
            if A >= 2:
                B_inv += M_E * ad2 * w_2
            if A >= 3:
                B_inv += M_E * ad3 * w_3
            if A >= 4:
                B_inv += M_E * ad4 * w_4

            abs_diff = abs(B_inv - AME_B[K])
            err_pct = ((B_inv - AME_B[K]) / AME_B[K]) * 100
            rows[K] = {
                "A": int(A),
                "B_inv_MeV": fmt(B_inv, dps=OUT_DPS),
                "AME_B_MeV": fmt(AME_B[K], dps=OUT_DPS),
                "abs_diff_MeV": fmt(abs_diff, dps=OUT_DPS),
                "rel_err_pct": fmt(err_pct, dps=25),
                "B_inv_mpf": B_inv,
            }
            print(
                f"  {K:<4} A={A}   B_inv = {mp.nstr(B_inv, 7):>10} MeV   "
                f"(AME = {mp.nstr(AME_B[K], 7):>10})   err = {mp.nstr(err_pct, 5):>9}%  [by inversion]"
            )

        print("\n[Verdict -- Anchor-Inversion Diagnostic, Not a Closure]")
        print("All three weights (w_2, w_3, w_4) are algebraically inverted from the same")
        print("AME2020 table scored above: D and 4He have err = 0 by construction (x - x = 0),")
        print("and T / 3He reflect +/- half the A=3 mirror split by construction.")
        print("Neither na_stokes_gluonic (3) nor na_stokes_residual (5/2) enters w_n or B_inv.")
        print("Under CAL-1/2/3 anti-fit rules, this records required target weights only (no closure).")

        half_mirror_split = (AME_B["T"] - AME_B["3He"]) / 2
        d_identity_res = abs(rows["D"]["B_inv_mpf"] - AME_B["D"])
        he4_identity_res = abs(rows["4He"]["B_inv_mpf"] - AME_B["4He"])
        a3_mirror_res = max(
            abs((AME_B["T"] - rows["T"]["B_inv_mpf"]) - half_mirror_split),
            abs((rows["3He"]["B_inv_mpf"] - AME_B["3He"]) - half_mirror_split),
        )

        wb.set_description(
            "80-dps anchor-inversion diagnostic audit (`qou-kjik`) of "
            "`strong_unified_binding_probe.py`: verifies that `w_2, w_3, w_4` "
            "(`free_parameters = 3`) are algebraically solved from `AME_B['D']`, "
            "`(AME_B['T'] + AME_B['3He'])/2`, and `AME_B['4He']`, making the `D` "
            "and `4He` residuals identically zero (`x - x = 0`) and `T`/`3He` "
            "deviations identically +/- half the A=3 mirror split, with zero "
            "dependence on `na_stokes_gluonic` or `na_stokes_residual`."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("free_parameters", 3)
        wb.add_parameter("is_empirical_anchor_inversion", True)
        wb.add_parameter("na_stokes_constants_used_in_weights", False)

        wb.add_data(
            "inverted_weights_from_ame",
            {
                "w_2": fmt(w_2, dps=OUT_DPS),
                "w_3": fmt(w_3, dps=OUT_DPS),
                "w_4": fmt(w_4, dps=OUT_DPS),
            },
        )
        wb.add_data(
            "back_substitution_rows",
            {
                k: {kk: vv for kk, vv in v.items() if kk != "B_inv_mpf"}
                for k, v in rows.items()
            },
        )

        wb.add_assertion(
            "deuteron_and_he4_residuals_vanish_by_algebraic_inversion_identity",
            fmt(max(d_identity_res, he4_identity_res), dps=15),
            "0",
            "1e-75",
            source="qou-kjik audit: w_2 and w_4 are solved directly from AME_B['D'] and AME_B['4He']",
        )
        wb.add_assertion(
            "a3_residuals_equal_half_mirror_split_by_algebraic_inversion_identity",
            fmt(a3_mirror_res, dps=15),
            "0",
            "1e-75",
            source="qou-kjik audit: w_3 is solved directly from (AME_B['T'] + AME_B['3He']) / 2",
        )
        wb.add_caveat(
            "Anchor-inversion diagnostic (`free_parameters = 3` solved from 4 AME2020 points): "
            "zero residuals on D and 4He are arithmetic identities (`x - x = 0`), not a "
            "parameter-free physical closure, and `na_stokes_gluonic` / `na_stokes_residual` "
            "enter neither `w_n` nor `B_inv` (`qou-kjik`)."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
