#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical dashboard, no symbolic-q object.
"""ρ_F·m_e·Vol binding route — binding + aligned mass dashboard (EXPLORATORY).

The Kashaev/density-prefactor binding form behind
`conj:kashaev-density-equals-sdp-multiplicity` (Conjecture 10.14.8):

    B_pred(K_w) = ρ_F · m_e · Vol_hyp(K_w),   ρ_F = ν_SDP ∈ ℤ_{>0}

evaluated for the three atoms with *derived* census-knot assignments
(6₂, 8₁₁, L6a4 — `conj:canonical-knot-id-sdp`) plus the ⁴He magic-closure
row (no census knot; ρ_F extrapolated). Aligned mass column:
M_pred = m_unbnd,can − B_pred, with the canonical muon-anchored Hecke
constituent masses.

NOT canonical / NOT wired to production. Extending past ³He requires the
canonical knot-assignment solver (the open "R5-full" gap:
finitude of the NF candidate set + SDP search bounds + structural
K(𝔥) ∈ H_{3A}(q₀) identification — `conj:canonical-knot-id-sdp`).
Volume is computable for any named knot (hp_volume.py); the *assignment*
is the blocker. Hand-assigning knots by volume-match would be a FIT.
Bean qou-r307 (1-loop=torsion vs ν_SDP) is the derivational probe.

Two corrections, 2026-08-22 (bean `qou-r8zo`)
---------------------------------------------

**1. Two of the four M_meas values were wrong by ~250σ.** That column is
the *measured* nuclear mass every error here is scored against, and it was
hand-typed. Against NIST's own nuclear-mass rows:

    iso   was            NIST                  error
    2H    1875.612790    1875.61294500     -155.0 eV   (267σ)
    3H    2808.921136    2808.92113668       -0.7 eV     (1σ)
    3He   2808.391611    2808.39161112       -0.1 eV     (0σ)
    4He   3727.379109    3727.3794118      -302.8 eV   (252σ)

³H and ³He landing at 1σ and 0σ is what *identifies* the intended source:
the direct CODATA nuclear-mass entry (deuteron / triton / helion / alpha),
not `Z·m_p + N·m_n − B` and not `atomic·u − Z·m_e`, both of which miss
those two rows by 13–78 eV. ²H and ⁴He are then simply wrong, by −82.6 and
−81.2 ppb — a shared relative offset, so one bad conversion rather than two
typos, but the source producing it was not identified. All four are now
**read from the table**, so the question cannot recur.

Scale: 300 eV on 3727 MeV is 81 ppb, against the ~1000 ppb discrepancies
this dashboard exists to report — an 8 % error in the scoring column.

**2. The arithmetic was float64.** A probe is a `computations/` script and
is covered by the NO-FLOAT64 family; "it emits no witness" is not an
exemption, because a probe conclusion becomes an argument in a bean or an
audit doc where nothing re-derives it. Now `mpmath.mpf` end to end, with
`float()` only inside the f-strings that print.

Run:  python3 -u computations/probes/rho_f_vol_binding_dashboard.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from codata_table import codata  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

M_E = codata("electron mass energy equivalent in MeV").value

# The two constituent masses are NOT CODATA: they are the framework's own
# canonical muon-anchored Hecke energies, 2(m_μ·F_Bor − 6m_e). They stay
# literals here deliberately, and must not be "drained" to the table.
M_P = mp.mpf("938.2720894273")  # noqa: P31 - canonical Hecke energy, not CODATA
M_N = mp.mpf("939.5654227645")  # noqa: P31 - canonical Hecke energy, not CODATA

# The measured nuclear mass per isotope, by its exact NIST quantity name.
# Read, never transcribed -- see correction 1 in the module docstring.
NUCLEAR_MASS = {
    (1, 1): "deuteron mass energy equivalent in MeV",
    (1, 2): "triton mass energy equivalent in MeV",
    (2, 1): "helion mass energy equivalent in MeV",
    (2, 2): "alpha particle mass energy equivalent in MeV",
}

# (Z, N, knot, ρ_F=ν_SDP, Vol_hyp, B_AME MeV); ρ_F<0 ⇒ extrapolated
ATOMS = [
    (1, 1, "6_2",   1, "4.400833", "2.224566"),
    (1, 2, "8_11",  2, "8.286300", "8.481821"),
    (2, 1, "L6a4",  2, "7.327700", "7.718058"),
    (2, 2, "magic", -1, None,      "28.295673"),  # no census knot
]
NAMES = {(1, 1): "2H", (1, 2): "3H", (2, 1): "3He", (2, 2): "4He"}


def rows():
    for Z, N, knot, rho, vol, bame in ATOMS:
        munb = Z * M_P + N * M_N
        bame = mp.mpf(bame)
        mmeas = codata(NUCLEAR_MASS[(Z, N)]).value
        if vol is None:
            yield dict(iso=NAMES[(Z, N)], knot=knot, rho="2?", vol=None,
                       B=None, bame=bame, errB=None, munb=munb,
                       Mpred=None, mmeas=mmeas, errM=None)
            continue
        vol = mp.mpf(vol)
        B = rho * M_E * vol
        Mpred = munb - B
        yield dict(iso=NAMES[(Z, N)], knot=knot, rho=rho, vol=vol, B=B,
                   bame=bame, errB=100 * (B - bame) / bame, munb=munb,
                   Mpred=Mpred, mmeas=mmeas,
                   errM=mp.mpf(10) ** 9 * (Mpred - mmeas) / mmeas)


def main() -> int:
    print("### ρ_F·m_e·Vol binding route — binding + aligned mass (EXPLORATORY)\n")
    print(f"m_e={float(M_E):.8f}  m_p,can={float(M_P):.7f}  "
          f"m_n,can={float(M_N):.7f} MeV")
    print("M_meas read from the NIST table (deuteron / triton / helion / "
          "alpha nuclear masses), not transcribed.\n")
    print("| iso | knot | ρ_F | Vol_hyp | B_ρVol | B_AME | err B % | "
          "M_pred | M_meas | err M (ppb) |")
    print("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows():
        if r["vol"] is None:
            print(f"| {r['iso']} | {r['knot']} | {r['rho']} | — | — | "
                  f"{float(r['bame']):.3f} | — | — | "
                  f"{float(r['mmeas']):.3f} | — (no knot) |")
            continue
        print(f"| {r['iso']} | {r['knot']} | {r['rho']} | {float(r['vol']):.4f} | "
              f"{float(r['B']):.4f} | {float(r['bame']):.3f} | "
              f"{float(r['errB']):+.2f} | {float(r['Mpred']):.3f} | "
              f"{float(r['mmeas']):.3f} | {float(r['errM']):+.1f} |")
    print("\nNotes: only 3 atoms have derived census-knot assignments; ⁴He "
          "magic-closure has none (ρ_F extrapolated). Mass error is "
          "binding-dominated. ³He is the worst (−2.97% binding → +82k ppb mass).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
