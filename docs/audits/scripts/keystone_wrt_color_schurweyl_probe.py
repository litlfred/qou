#!/usr/bin/env python3
"""
λ-coloured WRT(S³/2I): the colour-resolved decomposition + the Schur–Weyl
index obstruction to a direct W_λ identity.

Follows the Habiro-WRT push (`2026-06-22-keystone-habiro-wrt-s3-2i.md`): the bare
Σ(2,3,5) invariant Ψ(1/q₀)=2.3296 is ONE number; the W_λ are a λ-family. The
sharpened frontier was "use the WRT TQFT with λ-coloured insertions". This probe
takes the well-anchored first step and identifies the precise obstruction.

WHAT IS WELL-ANCHORED (computed here):
  The bare invariant already DECOMPOSES over its four false-theta components
      Ψ(q) = Ψ̃_30^{(1)}(q) + Ψ̃_30^{(11)}(q) + Ψ̃_30^{(19)}(q) + Ψ̃_30^{(29)}(q),
  one per support residue a∈{1,11,19,29} (the icosahedral/E₈ data). These four
  components are the colour-resolution intrinsic to the closed manifold (the
  SU(2) integrable/flat-connection structure). We split the validated sum into
  these four numbers at the bar image 1/q₀.

WHAT IS THE OBSTRUCTION (stated, not forced):
  The WRT colour index is SU(2)-spin (the Wilson-line rep / the Seifert-fibre
  colour). The W_λ are indexed by λ ⊢ 5 (S_5 Wedderburn blocks of H_5(q)).
  SU(2)-spin and S_n-partitions are related by SCHUR–WEYL DUALITY — they are NOT
  the same index set. The bare manifold has FOUR colour components; n=5 has
  SEVEN partitions (THREE "physical" blocks). So a direct component↔W_λ equality
  cannot hold by counting alone; the map REQUIRES the explicit Schur–Weyl functor
  SU(2)-colours → S_5-blocks (the same Schur–Weyl bridge the framework already
  uses, #2364: colour-ℂ³ vs spin-ℂ²).

DISCIPLINE: no fit; no component↔W_λ match is asserted (the counts forbid a naive
one, and forcing would be numerology). The deliverable is the anchored
decomposition + the precise representation-theoretic obstruction.
"""
from mpmath import mp, mpf, nstr

mp.dps = 50
Q0 = mpf("1.1099785955541805")
INV = 1 / Q0
RESIDUES = [1, 11, 19, 29]


def psi_component(a, q, nterms=4000):
    """Ψ̃_30^{(a)}(q) = Σ_{n≥0} [n≡a → +1, n≡60−a → −1] q^{n²/120}."""
    terms = []
    for n in range(nterms):
        r = n % 60
        if r == a:
            terms.append(q ** (mpf(n * n) / 120))
        elif r == (60 - a) % 60:
            terms.append(-q ** (mpf(n * n) / 120))
    return mp.fsum(terms)


def main():
    print(f"q_0 = {Q0}  |  1/q_0 = {nstr(INV,12)} (inside disk)  |  dps = {mp.dps}\n")

    print("Colour-resolved decomposition of the bare Σ(2,3,5) invariant at 1/q_0:")
    comps = {a: psi_component(a, INV) for a in RESIDUES}
    total = mp.fsum(comps.values())
    for a in RESIDUES:
        print(f"  Ψ̃_30^({a:>2}) (1/q_0) = {nstr(comps[a], 18)}")
    print(f"  ── sum            = {nstr(total, 18)}  (= Ψ(1/q_0), cross-check vs 2.32957704683293)")
    print(f"  |sum − 2.32957704683293| = {nstr(abs(total - mpf('2.32957704683293')), 4)}\n")

    print("Index-counting obstruction (the structural point, not a fit):")
    print(f"  • WRT colour components of Σ(2,3,5): {len(RESIDUES)}  (residues {RESIDUES}; SU(2)-spin / flat-connection index)")
    print(f"  • partitions λ ⊢ 5: 7   (physical Wedderburn blocks: 3 — (3,1,1),(3,2),(2,2,1))")
    print(f"  • 4 ≠ 7 and 4 ≠ 3  ⇒ NO naive component↔W_λ bijection; a direct equality")
    print(f"    is impossible by counting.  The map SU(2)-colour → S_5-block is")
    print(f"    SCHUR–WEYL duality, not the identity — that functor is the precise,")
    print(f"    finitely-stated remaining bridge (rep theory, already used in-corpus).")
    print("\nλ-COLOUR / SCHUR–WEYL PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
