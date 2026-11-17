#!/usr/bin/env python3
"""80-dps mpmath computational witness probe for Round 73:
- qou-47nf: SymSquareHolonomyIsRealType (symSquare_iterated_selfDual_of_selfDual)
- qou-enn6: FibreDimensionForcesTL (twoDimFibre_pins_y3_scaled)
- qou-qrsp: Mu3SlotExclusion (thirdDiff_const_and_unit_damping)
- qou-t39x: SLeakZeroCrossing (sleak_zero_between_anchors_rev)
- qou-wgta: DeuteronNaiveZMagnitude (choose4_row_sum_and_five_Bcat_lt_BAme)
"""

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

mp.dps = 80


def script_sha256_12(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def run_probe(commit_sha: str) -> dict:
    probe_path = Path(__file__).resolve()
    s_hash = script_sha256_12(probe_path)

    q_val = mp.mpf("3") / mp.mpf("5")
    qi_val = mp.mpf("1") / q_val

    # 1. qou-47nf: SymSquareHolonomyIsRealType
    # Iterated Sym^2 of a self-dual SL(2) character chi(t) = t + t^{-1}:
    # Sym^2(V_2) has character t^2 + 1 + t^{-2} (dim 3, invariant under t <-> t^{-1}),
    # and Sym^2(Sym^2(V_2)) has character t^4 + t^2 + 2 + t^{-2} + t^{-4} (dim 5, invariant under t <-> t^{-1}).
    def sym2_char2(t: mp.mpf) -> mp.mpf:
        return (t ** 4) + (t ** 2) + mp.mpf("2") + (t ** (-2)) + (t ** (-4))

    res_47nf = abs(sym2_char2(q_val) - sym2_char2(qi_val))

    # 2. qou-enn6: FibreDimensionForcesTL
    # Verify (q + qi)^2 * y3 == (q + qi)^2 - 2 when y13 = 0, (q + qi)^2 * y21 = 1, y3 + 2*y21 + y13 = 1
    b2 = q_val + qi_val
    y13 = mp.mpf("0")
    y21 = mp.mpf("1") / (b2 ** 2)
    y3 = mp.mpf("1") - mp.mpf("2") * y21 - y13
    lhs_enn6 = (b2 ** 2) * y3
    rhs_enn6 = (b2 ** 2) - mp.mpf("2")
    res_enn6 = abs(lhs_enn6 - rhs_enn6)

    # 3. qou-qrsp: Mu3SlotExclusion
    # Verify thirdDiff(c,c,c,c,c,c,c,c) = 0 and thirdDiff with r_c = 1 vanishes
    def third_diff(g0, ga, gb, gc, gab, gac, gbc, gabc):
        return gabc - gab - gac - gbc + ga + gb + gc - g0

    c_val = mp.mpf("7") / mp.mpf("11")
    ra = mp.mpf("2") / mp.mpf("5")
    rb = mp.mpf("3") / mp.mpf("7")
    td_const = third_diff(c_val, c_val, c_val, c_val, c_val, c_val, c_val, c_val)
    td_unit = third_diff(
        c_val,
        c_val * ra,
        c_val * rb,
        c_val,
        c_val * ra * rb,
        c_val * ra,
        c_val * rb,
        c_val * ra * rb,
    )
    res_qrsp = abs(td_const) + abs(td_unit)

    # 4. qou-t39x: SLeakZeroCrossing
    # Reversed-sign affine carrier Sleak(q) = s_a + (s_b - s_a)*(q - a)/(b - a) with s_a > 0 > s_b
    a_anc = mp.mpf("1109980") / mp.mpf("1000000")
    b_anc = mp.mpf("1109993") / mp.mpf("1000000")
    s_a = mp.mpf("1002290") / mp.mpf("100000000")
    s_b = -mp.mpf("3945936") / mp.mpf("100000000")
    q_star = a_anc - s_a * (b_anc - a_anc) / (s_b - s_a)
    s_at_star = s_a + (s_b - s_a) * (q_star - a_anc) / (b_anc - a_anc)
    res_t39x = abs(s_at_star)

    # 5. qou-wgta: DeuteronNaiveZMagnitude
    row_sum = sum(math.comb(4, k) for k in range(5))
    bcat_milli = 380
    bame_milli = 2225
    res_wgta = abs(mp.mpf(str(row_sum)) - mp.mpf("16"))

    tol = mp.mpf("10") ** (-70)
    checks = [
        {
            "id": "qou-47nf-symsquare-iterated-selfdual",
            "bean": "qou-47nf",
            "description": "Iterated symmetric-square character Sym^2(Sym^2(V_2)) is bar-self-dual at q=3/5",
            "charAtQ": mp.nstr(sym2_char2(q_val), 40),
            "charAtQi": mp.nstr(sym2_char2(qi_val), 40),
            "residual": mp.nstr(res_47nf, 25),
            "passed": bool(res_47nf <= tol),
        },
        {
            "id": "qou-enn6-twodim-fibre-pins-y3-scaled",
            "bean": "qou-enn6",
            "description": "Two-dimensional fibre pins (q+qi)^2 * y3 = (q+qi)^2 - 2 at q=3/5",
            "lhs": mp.nstr(lhs_enn6, 40),
            "rhs": mp.nstr(rhs_enn6, 40),
            "residual": mp.nstr(res_enn6, 25),
            "passed": bool(res_enn6 <= tol),
        },
        {
            "id": "qou-qrsp-thirddiff-const-and-unit-damping",
            "bean": "qou-qrsp",
            "description": "Third mixed difference vanishes on constant baseline and at unit third-bond damping r_c=1",
            "tdConst": mp.nstr(td_const, 25),
            "tdUnit": mp.nstr(td_unit, 25),
            "residual": mp.nstr(res_qrsp, 25),
            "passed": bool(res_qrsp <= tol),
        },
        {
            "id": "qou-t39x-sleak-reversed-sign-zero-crossing",
            "bean": "qou-t39x",
            "description": "Reversed-sign carrier with Sleak(a)>0>Sleak(b) crosses zero strictly inside (a,b)",
            "qStar": mp.nstr(q_star, 40),
            "residual": mp.nstr(res_t39x, 25),
            "passed": bool(a_anc < q_star < b_anc and res_t39x <= tol),
        },
        {
            "id": "qou-wgta-choose4-sum-and-five-bcat-bound",
            "bean": "qou-wgta",
            "description": "Exterior rank sum sum_{k=0}^4 C(4,k) = 16 and 5*BcatMilli = 1900 < 2225 = BAmeMilli",
            "choose4Sum": str(row_sum),
            "fiveBcat": str(5 * bcat_milli),
            "residual": mp.nstr(res_wgta, 25),
            "passed": bool(row_sum == 16 and 5 * bcat_milli < bame_milli and res_wgta <= tol),
        },
    ]

    return {
        "schemaVersion": "1.0",
        "probeId": "symsquare-fibretl-mu3slot-sleak-deuteronz",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scriptPath": "computations/probes/symsquare_fibretl_mu3slot_sleak_deuteronz_probe.py",
        "scriptHash": s_hash,
        "scriptCommitSha": commit_sha,
        "precisionDps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    witness = run_probe(args.commit_sha)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
