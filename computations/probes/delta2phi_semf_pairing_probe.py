#!/usr/bin/env python3
"""Is delta^2 Phi the SEMF pairing term? Sign yes (vacuously); magnitude NO.

Tests the identification proposed in bean `qou-mgq3` after PR #6197's
sorry-free `PairingParityForcesPositiveB3.lean` showed parity forcing the sign
of the connected three-body cumulant. The proposal: delta^2 Phi's even-Z
positivity is measuring the SEMF pairing term rather than shell closure.

VERDICT: the proposal is REFUTED on magnitude, and the sign agreement that
motivated it turns out to be structurally forced and therefore empty.

1. SIGN -- matches exactly, and carries NO information. The producer evaluates
   the N = Z line, so A = 2Z and the pairing class is fixed by Z parity alone:
   Z even -> N even -> EVEN-EVEN -> SEMF +delta; Z odd -> ODD-ODD -> -delta.
   So ANY quantity alternating with Z parity reproduces the SEMF pairing sign
   here. delta^2 Phi does alternate (measured: 0 exceptions, Z = 3..31), hence
   it matches -- but that is a restatement of "delta^2 Phi alternates", not
   evidence of a pairing mechanism.

2. MAGNITUDE -- refuted, and by SHAPE, not merely scale. Decompose
   Phi(Z) = s(Z) + (-1)^Z e(Z) with s smooth, giving
   delta^2 Phi(Z) ~ s''(Z) + 4(-1)^Z e(Z), and separate the two by averaging /
   half-differencing adjacent Z. Measured, the smooth part is only 3.4% of the
   alternating one, so delta^2 Phi is essentially pure alternation and e(Z) is
   cleanly extractable.

   SEMF pairing is delta = a_P / A^(1/2), so on this line e(Z)*sqrt(Z) should
   be CONSTANT. It is not: it runs 3.38 -> 37.34, a spread of 11.0x. Worse,
   e(Z) is NON-MONOTONE -- it rises from 8.67 at Z=3 to a peak 9.65 near
   Z=12-15, then falls to 0.617 by Z=30 -- while the SEMF pairing term decreases
   monotonically in A. Wrong shape, not just wrong scale.

Scope (a): a negative about the SEMF-pairing identification of THIS statistic.
It does not touch PR #6197's Lean, which is about the connected three-body
cumulant b_3 and is verified sorry-free; nor does it revive delta^2 Phi as a
shell-closure signal, which `qou-pz4m` separately refuted.

PRECISION. The delta^2 Phi inputs are INHERITED float64 from level_k_binding's
numpy Hoefsmit matrices, which this probe does not re-implement; all arithmetic
here is mpmath at 50 dps. Stated rather than hidden: the conclusion is an 11x
spread and a sign-of-slope reversal, ~15 orders above the float64 floor, so the
inherited precision cannot be what produces it. No agreement at any digit count
is claimed.
"""
import re
import sys
from pathlib import Path
from mpmath import mp

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "substrate",
           _ROOT.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 50
MAGIC = {2, 8, 20, 28, 50, 82, 126}

#: delta^2 Phi at K=10, q_0, N=Z line. Reproduced from
#: computations/_deprecated/shell_closure_compute.py --kmax 10 --zmax 32
#: (PYTHONPATH over computations/ and computations/substrate/).
D2PHI = {
    3: "-34.9520", 4: "34.3682", 5: "-33.3091", 6: "32.7154", 7: "-32.8844",
    8: "33.2497", 9: "-34.0872", 10: "35.1136", 11: "-36.8645", 12: "38.8154",
    13: "-38.4011", 14: "38.2081", 15: "-38.3597", 16: "38.7634", 17: "-34.0719",
    18: "29.6718", 19: "-24.8668", 20: "20.3986", 21: "-17.0424", 22: "14.0690",
    23: "-11.7134", 24: "9.7809", 25: "-8.0033", 26: "6.6771", 27: "-5.3228",
    28: "4.4316", 29: "-3.4108", 30: "2.8493", 31: "-2.0904",
}


def main() -> int:
    vals = {z: mp.mpf(s) for z, s in D2PHI.items()}

    sign_mismatch = [z for z, v in vals.items() if (v > 0) != (z % 2 == 0)]

    smooth, alt = {}, {}
    for z in sorted(vals):
        if z + 1 not in vals:
            continue
        smooth[z] = (vals[z] + vals[z + 1]) / 2
        alt[z] = (vals[z] - vals[z + 1]) / 2 * (1 if z % 2 == 0 else -1)

    e = {z: alt[z] / 4 for z in alt}
    inv = {z: e[z] * mp.sqrt(z) for z in e}          # constant iff e ~ A^(-1/2)
    spread = max(inv.values()) / min(inv.values())

    zs = sorted(e)
    zpeak = max(zs, key=lambda z: e[z])
    monotone = all(e[zs[i]] >= e[zs[i + 1]] for i in range(len(zs) - 1))

    contamination = ((sum(abs(v) for v in smooth.values()) / len(smooth))
                     / (sum(abs(v) for v in alt.values()) / len(alt)))

    print(f"sign mismatches (Z=3..31)   : {sign_mismatch or 'NONE'}")
    print(f"smooth/alternating ratio    : {mp.nstr(contamination, 4)}")
    print(f"e(Z)*sqrt(Z) spread         : {mp.nstr(spread, 5)}x  (1x = SEMF match)")
    print(f"e(Z) monotone decreasing?   : {monotone}  (SEMF requires True)")
    print(f"e(Z) peaks at Z             : {zpeak}")

    w = WitnessBuilder("delta2phi-semf-pairing", engine="mpmath")
    w.set_description(
        "Tests whether delta^2 Phi (K=10, q_0, N=Z line) is the SEMF pairing "
        "term, as proposed in qou-mgq3 after PR #6197. REFUTED on magnitude: "
        "e(Z)*sqrt(Z) spreads 11x where SEMF requires constant, and e(Z) is "
        "non-monotone (peaks near Z=12-15) where SEMF decreases monotonically. "
        "The sign agreement is structurally forced on the N=Z line (Z parity "
        "fixes the even-even/odd-odd class) and is therefore not evidence."
    )
    w.add_parameter("K", 10)
    w.add_parameter("line", "N = Z (so A = 2Z)")
    w.add_data("sign_mismatches", sign_mismatch)
    w.add_data("sign_agreement_is_structurally_forced", True)
    w.add_data("smooth_over_alternating_ratio", mp.nstr(contamination, 12))
    w.add_data("e_times_sqrtZ_spread", mp.nstr(spread, 12))
    w.add_data("e_monotone_decreasing", monotone)
    w.add_data("e_peak_Z", zpeak)
    w.add_data("e_by_Z", {str(z): mp.nstr(e[z], 12) for z in sorted(e)})
    # Assertions are stated so that PASS == "the refutation holds". The
    # measured quantities themselves are in `data`; encoding them as the
    # `computed` side of a comparison against a string like "> 2" only makes
    # the witness read red for a finding that is solid.
    w.add_assertion("sign_pattern_is_pure_parity",
                    len(sign_mismatch), 0, tolerance=0,
                    source="sign(d2Phi) > 0 iff Z even, over Z = 3..31")
    w.add_assertion("semf_sqrtA_scaling_refuted",
                    1 if spread > 2 else 0, 1, tolerance=0,
                    source=f"e(Z)*sqrt(Z) must be constant under SEMF; "
                           f"measured spread {mp.nstr(spread, 6)}x")
    w.add_assertion("e_non_monotone_as_semf_forbids",
                    0 if monotone else 1, 1, tolerance=0,
                    source=f"SEMF pairing decreases monotonically in A; "
                           f"e(Z) instead peaks at Z = {zpeak}")
    w.save(extra={"q0Anchor": "independent",
             "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: Is delta^2 Phi the SEMF pairing term? Sign yes (vacuously); magnitude NO.",
             })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
