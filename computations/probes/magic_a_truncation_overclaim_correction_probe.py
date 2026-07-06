#!/usr/bin/env python3
"""Self-correction: the magic-A ⁴He +5.87% is the magic-A FORMULA gap, NOT a
body-order truncation residual (0 fit).

The spectral-bridge audit (PR #2718) asserted, in passing, that the magic-A ⁴He
+5.87% miss "is the finite-truncation residual of the geometric series." This probe
tests that claim and finds it WRONG — the two objects are distinct:

 (1) magic-A formula gap: the doubly-magic ⁴He binding uses the SEPARATE formula
     B = 2·m_e·A·(8G)  (G = Catalan, 8G = Borromean L6a4 volume). It gives
     29.956 MeV vs AME 28.296 = +5.87%. THIS is the +5.87%.

 (2) body-order geometric series: B = Σ_{n≥2} m_e·a_D^(n), a_D^(n) the depth-2
     selection-rule values (1, 1.337, 2.533, …). At the PHYSICAL body order for a
     4-nucleon system (n ≤ A = 4) the truncated sum is only m_e·(1+1.337+2.533)
     ≈ 2.49 MeV — an order of magnitude below 28.3. The series even DIVERGES
     (λ₊ = 2.185 > 1), so "the geometric series" has no finite total to truncate;
     and it only crosses 28 MeV near n=7–8, unphysical for A=4 and accidental.

Conclusion (scope-(a) re-scope): the +5.87% is the magic-A-formula residual, a
DIFFERENT object from the body-order series. The spectral-bridge result (the kernel's
dominant root λ₊ > 1 gives extensive body-order growth) STANDS — it just does not
address, and was wrongly tied to, the magic-A gap. No fit.
"""
import sys
from pathlib import Path

import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations"))
import _path_bridge  # noqa: E402,F401
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
ME = mp.mpf("0.51099895069")          # MeV
AME_4HE = mp.mpf("28.295674")
TAU = mp.mpf("2.6423863")              # depth-2 kernel τ(q₀)
A = 4


def main():
    G = mp.catalan
    # (1) magic-A formula
    magicA = 2 * ME * A * (8 * G)
    magic_err = (magicA - AME_4HE) / AME_4HE * 100

    # (2) body-order geometric series, depth-2 recurrence
    aD = [mp.mpf(1), mp.mpf("1.33697")]
    for _ in range(8):
        aD.append(TAU * aD[-1] - aD[-2])
    jet_phys = ME * mp.fsum(aD[:3])    # n = 2..4 (physical body order ≤ A)
    partials = {N: ME * mp.fsum(aD[: N - 1]) for N in (4, 5, 6, 7, 8)}

    print(f"(1) magic-A formula 2·m_e·A·8G = {mp.nstr(magicA,8)} MeV   "
          f"vs AME {mp.nstr(AME_4HE,7)}  →  {mp.nstr(magic_err,4)}%   ← THIS is the +5.87%")
    print(f"(2) jet-sum m_e·Σ_(n=2..N) a_D^(n):")
    for N, v in partials.items():
        tag = "  ← physical body order n≤A=4" if N == 4 else ""
        print(f"      N={N}: {mp.nstr(v,7)} MeV{tag}")
    print(f"\n  physical jet-sum (n≤4) = {mp.nstr(jet_phys,6)} MeV is ~{mp.nstr(AME_4HE/jet_phys,3)}× too small.")
    print(f"  series diverges (λ₊=2.185>1): no finite total to truncate; crosses 28 only near n=7–8 (unphysical for A=4).")
    print(f"  VERDICT: +5.87% is the magic-A-FORMULA gap, NOT a body-order truncation residual.")

    wb = WitnessBuilder("magic-a-truncation-overclaim-correction", engine="mpmath",
                        output_dir=str(REPO / "computations"))
    wb.description = (
        "Self-correction (0 fit): the magic-A ⁴He +5.87% is the gap of the separate "
        "doubly-magic formula B=2·m_e·A·8G (29.956 vs 28.296 MeV), NOT a finite-truncation "
        "residual of the body-order geometric series as PR #2718's audit asserted in "
        "passing. The physical-body-order (n≤A=4) jet-sum is only 2.49 MeV (≈11× too small) "
        "and the series diverges (λ₊>1). Re-scopes the #2718 claim; the spectral-bridge "
        "result (λ₊>1 extensive growth) is unaffected.")
    wb.add_parameter("m_e_MeV", mp.nstr(ME, 12))
    wb.add_parameter("A", A)
    wb.add_parameter("fit_params", 0)
    wb.add_data("magicA_formula_MeV", mp.nstr(magicA, 10))
    wb.add_data("magicA_err_pct", mp.nstr(magic_err, 6))
    wb.add_data("jet_sum_physical_n_le_4_MeV", mp.nstr(jet_phys, 10))
    wb.add_data("jet_sum_partials", {str(N): mp.nstr(v, 10) for N, v in partials.items()})
    wb.add_data("ratio_AME_over_physical_jetsum", mp.nstr(AME_4HE / jet_phys, 6))
    wb.add_assertion("magicA_gap_is_5pct87", computed=mp.nstr(magic_err, 6), expected="5.87",
                     tolerance=2e-2, source="2·m_e·A·8G vs AME")
    wb.add_assertion("physical_jetsum_far_below_AME",
                     computed=("1" if jet_phys < AME_4HE / 5 else "0"), expected="1",
                     tolerance=0.0, source="n≤4 jet-sum ≈ 2.49 MeV ≪ 28.3")
    wb.add_caveat("Re-scope of PR #2718's audit: the +5.87% is the magic-A-formula residual, "
                  "a distinct object from the body-order series. The spectral-bridge λ₊>1 "
                  "extensive-growth result stands; only its tie to the magic-A gap was wrong.")
    out = wb.save()
    print(f"\nwrote {Path(out).relative_to(REPO)}")


if __name__ == "__main__":
    main()
