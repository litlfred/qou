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
"""
from __future__ import annotations

M_E = 0.51099895000        # MeV, CODATA-2022
M_P = 938.2720894273       # canonical muon-anchored Hecke energy 2(m_μ·F_Bor−6m_e)
M_N = 939.5654227645

# (Z, N, knot, ρ_F=ν_SDP, Vol_hyp, B_AME MeV, M_meas MeV); ρ_F<0 ⇒ extrapolated
ATOMS = [
    (1, 1, "6_2",   1, 4.400833, 2.224566, 1875.612790),
    (1, 2, "8_11",  2, 8.286300, 8.481821, 2808.921136),
    (2, 1, "L6a4",  2, 7.327700, 7.718058, 2808.391611),
    (2, 2, "magic", -1, None,   28.295673, 3727.379109),  # no census knot
]
NAMES = {(1, 1): "2H", (1, 2): "3H", (2, 1): "3He", (2, 2): "4He"}


def rows():
    for Z, N, knot, rho, vol, bame, mmeas in ATOMS:
        munb = Z * M_P + N * M_N
        if vol is None:
            yield dict(iso=NAMES[(Z, N)], knot=knot, rho="2?", vol=None,
                       B=None, bame=bame, errB=None, munb=munb,
                       Mpred=None, mmeas=mmeas, errM=None)
            continue
        B = rho * M_E * vol
        Mpred = munb - B
        yield dict(iso=NAMES[(Z, N)], knot=knot, rho=rho, vol=vol, B=B,
                   bame=bame, errB=100 * (B - bame) / bame, munb=munb,
                   Mpred=Mpred, mmeas=mmeas,
                   errM=1e9 * (Mpred - mmeas) / mmeas)


def main() -> int:
    print("### ρ_F·m_e·Vol binding route — binding + aligned mass (EXPLORATORY)\n")
    print(f"m_e={M_E:.8f}  m_p,can={M_P:.7f}  m_n,can={M_N:.7f} MeV\n")
    print("| iso | knot | ρ_F | Vol_hyp | B_ρVol | B_AME | err B % | "
          "M_pred | M_meas | err M (ppb) |")
    print("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows():
        if r["vol"] is None:
            print(f"| {r['iso']} | {r['knot']} | {r['rho']} | — | — | "
                  f"{r['bame']:.3f} | — | — | {r['mmeas']:.3f} | — (no knot) |")
            continue
        print(f"| {r['iso']} | {r['knot']} | {r['rho']} | {r['vol']:.4f} | "
              f"{r['B']:.4f} | {r['bame']:.3f} | {r['errB']:+.2f} | "
              f"{r['Mpred']:.3f} | {r['mmeas']:.3f} | {r['errM']:+.1f} |")
    print("\nNotes: only 3 atoms have derived census-knot assignments; ⁴He "
          "magic-closure has none (ρ_F extrapolated). Mass error is "
          "binding-dominated. ³He is the worst (−2.97% binding → +82k ppb mass).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
