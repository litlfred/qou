#!/usr/bin/env python3
"""
mirror_nuclei_coulomb_systematics.py — the mirror binding split is Coulomb across the
WHOLE isobaric chain, bounding the strong-CSB budget any QOU kernel is allowed.

Generalises the A=3 result of #3564 (`mirror_split_coulomb_diagnosis.py`): there the
observed ³H/³He mirror split was shown to be the pp Coulomb displacement energy. This
extends it to the mirror-nuclei chain ³H/³He … ³⁹K/³⁹Ca using the repo's canonical
uniform-sphere Coulomb (`computations/coulomb_energy.mirror_displacement_mev`, discrete-
proton self-energy Z(Z−1), r₀=1.2 fm — NO free parameter):

    ΔE_C = (3/5)·(α ħc)·[Z_hi(Z_hi−1) − Z_lo(Z_lo−1)] / (r₀·A^{1/3}).

The observed split tracks ΔE_C: the ratio split_AME/ΔE_C is ≈ constant (~0.8) across
A=3–39 — i.e. the split is PROPORTIONAL to Coulomb (the ~0.8 factor is the known
uniform-sphere over-estimate of the Coulomb displacement energy). The scatter of that
ratio bounds the strong charge-symmetry-breaking.

QOU consequence: any strong/categorical binding kernel (#2089 log-trace `f_bond`,
#3548 connected `tr_M`) must be charge-symmetric — the split is Coulomb, not strong.
The #2089 kernel's pure-strong A=3 mirror split (2.27 MeV, #3564) is ~3× the whole
observed split and the Coulomb systematics shows this is a SYSTEMATIC requirement (all
A), not an A=3 accident. Constrains the kernel derivation (→ #3548); does not fit binding.

EXPLORATORY — scope-limited (a). Canonical shared Coulomb (no free parameter); no
production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
from coulomb_energy import mirror_displacement_mev  # noqa: E402 — canonical Z(Z−1), r₀=1.2
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()

# mirror pairs: (name, Z_light, Z_heavy, A). Same A, Z_heavy = Z_light + 1 (T_z mirror).
PAIRS = [("3H/3He", 1, 2, 3), ("7Li/7Be", 3, 4, 7), ("11B/11C", 5, 6, 11),
         ("13C/13N", 6, 7, 13), ("15N/15O", 7, 8, 15), ("23Na/23Mg", 11, 12, 23),
         ("27Al/27Si", 13, 14, 27), ("39K/39Ca", 19, 20, 39)]


def split_ame(Z1, Z2, A):
    # lighter-Z mirror binds MORE (less Coulomb) ⇒ positive split = B(lo) − B(hi)
    return float(mp.mpf(str(_ame_binding_mev(Z1, A))) - mp.mpf(str(_ame_binding_mev(Z2, A))))


def main() -> int:
    print("  Canonical uniform-sphere Coulomb ΔE_C (Z(Z−1), r₀=1.2 fm; "
          "computations/coulomb_energy.py) — NO free parameter.\n")
    print(f"  {'pair':<11}{'A':>3}{'split_AME':>10}{'ΔE_C':>9}{'split/ΔE_C':>12}")
    ratios = []
    rows = []
    for nm, Z1, Z2, A in PAIRS:
        s = split_ame(Z1, Z2, A)
        c = mirror_displacement_mev(Z2, Z1, A)
        ratio = s / c
        ratios.append(ratio)
        rows.append((nm, A, s, c, ratio))
        print(f"  {nm:<11}{A:>3}{s:>10.3f}{c:>9.3f}{ratio:>12.3f}")

    mean_r = sum(ratios) / len(ratios)
    rms_dev = (sum((r - mean_r) ** 2 for r in ratios) / len(ratios)) ** 0.5
    print(f"\n  split/ΔE_C = {mean_r:.3f} ± {rms_dev:.3f}  (mean ± RMS scatter, {100*rms_dev/mean_r:.0f}%)")
    print(f"  ⇒ the split is PROPORTIONAL to Coulomb across A=3–39 (the {mean_r:.2f} factor is")
    print(f"    the known uniform-sphere over-estimate of ΔE_C). The ~{100*rms_dev/mean_r:.0f}% ratio")
    print(f"    scatter (plus the ~0.07 MeV Nolen–Schiffer anomaly) bounds the strong CSB.")

    # QOU consequence
    kernel_a3 = 2.271                          # #2089 pure-strong A=3 mirror split (#3564)
    split_a3 = rows[0][2]
    print("\n### QOU consequence — the strong kernel must be charge-symmetric")
    print(f"  The observed split is Coulomb (∝ ΔE_C, one shared radius, all A), so the")
    print(f"  strong/categorical kernel must NOT carry it. The #2089 pure-strong A=3 mirror")
    print(f"  split = {kernel_a3:.3f} MeV (#3564) is {kernel_a3/split_a3:.1f}× the whole observed")
    print(f"  A=3 split ({split_a3:.3f} MeV) — and the systematics shows charge symmetry is")
    print(f"  required at ALL A, not an A=3 accident. Any QOU strong kernel (#2089 f_bond,")
    print(f"  #3548 connected tr_M) must be charge-symmetric, Coulomb sourced separately.")
    print(f"  Scope-(a): constrains the kernel derivation, does not fit binding.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-nuclei-coulomb-systematics", engine="mpmath")
            wb.set_description(
                "The mirror binding split is Coulomb across the isobaric chain ³H/³He…³⁹K/³⁹Ca: "
                "using the repo's canonical uniform-sphere Coulomb (Z(Z−1) self-energy, r₀=1.2 fm, "
                "coulomb_energy.mirror_displacement_mev — NO free parameter), the ratio "
                "split_AME/ΔE_C = %.2f ± %.2f is ≈constant across A=3–39 (the ~0.8 factor is the "
                "known uniform-sphere over-estimate). ⇒ the split is proportional to Coulomb, so "
                "any QOU strong kernel must be charge-symmetric (Coulomb separate); the #2089 "
                "kernel's 2.27 MeV A=3 strong split (#3564) is 3× the whole observed split, "
                "systematically. Scope-(a), no wiring." % (mean_r, rms_dev))
            wb.add_data("mirror_pairs", [
                {"pair": nm, "A": A, "split_AME": s, "coulomb_canonical": c, "ratio": r}
                for nm, A, s, c, r in rows])
            wb.add_data("ratio_mean", mean_r)
            wb.add_data("ratio_rms_scatter", rms_dev)
            wb.add_assertion(
                name="mirror_split_proportional_to_canonical_coulomb_all_A",
                computed=str(int(rms_dev / mean_r < 0.15)), expected="1", tolerance=0,
                source=(f"split_AME/ΔE_C(canonical Z(Z−1), r₀=1.2) = {mean_r:.3f} ± {rms_dev:.3f} "
                        f"({100*rms_dev/mean_r:.0f}% scatter) across 8 mirror pairs A=3–39 ⇒ the "
                        "split is proportional to Coulomb ⇒ the strong kernel must be charge-symmetric."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
