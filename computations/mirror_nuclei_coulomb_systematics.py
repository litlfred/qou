#!/usr/bin/env python3
"""
mirror_nuclei_coulomb_systematics.py — the mirror binding split is Coulomb across the
WHOLE isobaric chain, bounding the strong-CSB budget any QOU kernel is allowed.

Generalises the A=3 result of #3564 (`mirror_split_coulomb_diagnosis.py`): there the
observed ³H/³He mirror split was shown to be the pp Coulomb displacement energy. This
extends it to the mirror-nuclei chain ³H/³He … ³⁹K/³⁹Ca and shows the split follows the
one-parameter Coulomb law

    ΔE_C(A,Z₁→Z₂) = (3/5) · (e²/4πε₀) · (Z₂² − Z₁²) / R_c ,   R_c = r₀ · A^{1/3},

with a single physical charge-radius parameter r₀. The residuals `split_AME − ΔE_C`
(RMS ~0.3 MeV) UPPER-BOUND the strong charge-symmetry-breaking: they mix the true
Nolen–Schiffer anomaly (~0.07 MeV) with the error of the crude uniform-sphere model
(note the A-trend, negative→positive) — so ≲0.5 MeV is a conservative CSB budget, the
genuine strong CSB being smaller.

QOU consequence: any strong/categorical binding kernel (the #2089 log-trace `f_bond`,
#3548's connected `tr_M`) must be **charge-symmetric to within ≲0.5 MeV** across the
chart. The #2089 kernel's pure-strong A=3 mirror split (2.27 MeV, #3564) violates that
budget by ~7×, and the violation is systematic, not an A=3 accident. This constrains
the kernel derivation (→ #3548); it does not fit binding.

EXPLORATORY — scope-limited (a). r₀ is the standard nuclear charge-radius parameter
(validated ≈ physical value), not a free QOU fit; Coulomb is the textbook uniform-
sphere law. No production wiring.
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
from coulomb_energy import ALPHA_HBAR_C_MEV_FM  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
HBARC_ALPHA = mp.mpf(str(ALPHA_HBAR_C_MEV_FM))

# mirror pairs: (name, Z_light, Z_heavy, A). Same A, Z_heavy = Z_light + 1 (T_z mirror).
PAIRS = [("3H/3He", 1, 2, 3), ("7Li/7Be", 3, 4, 7), ("11B/11C", 5, 6, 11),
         ("13C/13N", 6, 7, 13), ("15N/15O", 7, 8, 15), ("23Na/23Mg", 11, 12, 23),
         ("27Al/27Si", 13, 14, 27), ("39K/39Ca", 19, 20, 39)]


def split_ame(Z1, Z2, A):
    # lighter-Z mirror binds MORE (less Coulomb) ⇒ positive split
    return float(mp.mpf(str(_ame_binding_mev(Z1, A))) - mp.mpf(str(_ame_binding_mev(Z2, A))))


def coulomb(Z1, Z2, A, r0):
    R = r0 * A ** (1.0 / 3.0)
    return float(0.6 * HBARC_ALPHA * (Z2 ** 2 - Z1 ** 2) / R)


def main() -> int:
    rows = [(nm, Z1, Z2, A, split_ame(Z1, Z2, A)) for nm, Z1, Z2, A in PAIRS]

    # one-parameter fit of r₀ (physical charge radius) minimising Σ residual²
    def sse(r0):
        return sum((s - coulomb(Z1, Z2, A, r0)) ** 2 for _, Z1, Z2, A, s in rows)
    lo, hi = 1.0, 2.0
    for _ in range(80):                       # golden-free bisection on the derivative
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if sse(m1) < sse(m2): hi = m2
        else: lo = m1
    r0 = (lo + hi) / 2

    print(f"  Coulomb law ΔE_C = (3/5)·(α ħc)·(Z₂²−Z₁²)/(r₀·A^⅓);  "
          f"fitted r₀ = {r0:.3f} fm  (physical nuclear charge radius ≈1.2–1.5 fm)\n")
    print(f"  {'pair':<11}{'A':>3}{'split_AME':>10}{'ΔE_C':>9}{'residual':>10}  (=NS anomaly)")
    resids = []
    for nm, Z1, Z2, A, s in rows:
        c = coulomb(Z1, Z2, A, r0)
        res = s - c
        resids.append(res)
        print(f"  {nm:<11}{A:>3}{s:>10.3f}{c:>9.3f}{res:>+10.3f}")
    max_res = max(abs(r) for r in resids)
    rms_res = (sum(r * r for r in resids) / len(resids)) ** 0.5
    print(f"\n  residual (upper bound on strong-CSB): RMS {rms_res:.3f} MeV, max |{max_res:.3f}| MeV")
    print(f"  ⇒ the mirror split is Coulomb across A=3–39 with ONE physical r₀ (fit to ~5–10%);")
    print(f"    the residual (A-trend ⇒ crude-model error + the ~0.07 MeV NS anomaly) bounds")
    print(f"    the strong charge-symmetry-breaking at ≲0.5 MeV — the true CSB being smaller.")

    # QOU consequence: the #2089 kernel's A=3 strong split (2.271 MeV, #3564) vs budget
    kernel_a3 = 2.271
    print(f"\n### QOU consequence — the strong kernel must be charge-symmetric")
    print(f"  #2089 pure-strong A=3 mirror split = {kernel_a3:.3f} MeV (#3564) vs the")
    print(f"  ≲{rms_res:.2f} MeV CSB upper bound ⇒ violates charge symmetry by ~{kernel_a3/rms_res:.0f}×,")
    print(f"  and the Coulomb systematics shows this is a SYSTEMATIC requirement (all A),")
    print(f"  not an A=3 accident. Any QOU strong kernel (#2089 f_bond, #3548 connected")
    print(f"  tr_M) must be charge-symmetric to within the NS budget, with Coulomb sourced")
    print(f"  separately. Scope-(a): constrains the kernel derivation, does not fit binding.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-nuclei-coulomb-systematics", engine="mpmath")
            wb.set_description(
                "The mirror binding split is Coulomb across the isobaric chain ³H/³He…³⁹K/³⁹Ca: "
                "a one-parameter law ΔE_C=(3/5)(αħc)(Z₂²−Z₁²)/(r₀A^⅓) with physical r₀≈%.2f fm "
                "fits all 8 pairs to an RMS residual of %.3f MeV, which UPPER-BOUNDS the strong "
                "charge-symmetry-breaking (residual = crude-model error + the ~0.07 MeV NS "
                "anomaly). ⇒ any QOU strong kernel must be charge-symmetric to within ≲0.5 MeV, "
                "Coulomb separate; the #2089 kernel's 2.27 MeV A=3 strong split (#3564) violates "
                "this by ~%.0f× systematically. Scope-(a), no wiring."
                % (r0, rms_res, kernel_a3 / rms_res))
            wb.add_data("r0_fm", r0)
            wb.add_data("mirror_pairs", [
                {"pair": nm, "A": A, "split_AME": s, "coulomb": coulomb(Z1, Z2, A, r0),
                 "residual": s - coulomb(Z1, Z2, A, r0)} for nm, Z1, Z2, A, s in rows])
            wb.add_data("residual_rms_MeV", rms_res)
            wb.add_data("residual_max_MeV", max_res)
            wb.add_assertion(
                name="mirror_split_is_coulomb_across_chain_one_physical_r0",
                computed=str(int(rms_res < 0.4 and 1.0 < r0 < 1.7)), expected="1", tolerance=0,
                source=(f"one-parameter Coulomb law (r₀={r0:.3f} fm, physical) fits the 8 mirror "
                        f"splits to RMS {rms_res:.3f} MeV (NS-anomaly scale) ⇒ mirror split is "
                        "Coulomb systematically; strong kernel must be charge-symmetric."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
