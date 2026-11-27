# Pre-registration: nucleus bond count under each valence premise (gap G5)

**Date** 2026-11-27 · **Gap** G5 of `docs/audits/2026-11-27-term-completeness-ledger.md` (#9658) · **Epic** `qou-myts`
**Probe** `nucleus_bond_valence_probe.py` (5/5, never reads AME) · **Lean** `QOU/MassTheory/NucleusBondValence.lean`

This file is committed **before** `compare_ame.py` is written or run. Nothing below was chosen by
looking at AME.

## The question

The production chain word `p…p n…n` carries `A − 1` ruled bonds, about one bond per nucleon. What in
the corpus forces more crossings per nucleon?

## What the corpus already settles

1. **The encoding forces the chain.** With Artin generators and contiguous nucleon blocks, the bond
   graph is a path (`LinearLayoutNoBulk`, `GammaGammaForcesTheLayout`, both sorry-free). The Artin
   γγ vertex forces the contiguous layout uniquely.
2. **The band reading removes the layout constraint and selects nothing new.** With BKL bands every
   layout is admitted, and the confinement SDP (reading 3) selects the same words at `H₃` and `H₆`
   (2026-09-14 audit, R4–R6).
3. **So the count must come from a selection principle, not from the layout.** The owner-sanctioned
   principle is energy minimisation (ruling 2026-11-22). The ruled bond is attractive at `q₀`
   (`0 < z − h/2 < 1`, check 4). With an attractive, additive bond, minimising energy means taking
   the **most** bonds the structure allows. Without a cap that is the complete graph `C(A, 2)`,
   which is excluded from `A = 5` on (Pauli closure `Λ⁵(Fin 4) = 0`; `MaxContactSimplex`). With a
   repulsive bond it is a spanning tree, `A − 1`. Neither gives a bounded number of bonds per
   nucleon above one. **A bounded count above one needs a valence cap.** (Lean: the handshake and
   matching bounds, and the tree lower bound.)

## The candidate caps, fixed here

| premise | cap | source | bonds `M(A)` | per nucleon, large `A` |
|---|---|---|---|---|
| chain | Artin linear layout | `LinearLayoutNoBulk` (proved) | `A − 1` | 1 |
| **T3** | each quark strand carries one bond, bonds colour-labelled | `TetrahedralFluxRingAndMajoranaCluster`: Tait bijection on `K₄`, `K₅` valence obstruction (`deg 4 > 3 = N_c`) | `3⌊A/2⌋` (`A ≥ 3`), 1 at `A = 2` | 3/2 |
| V3 | each quark strand carries one bond | same file, degree only | `min(C(A,2), ⌊3A/2⌋)` | 3/2 |
| V6 | each strand **end** carries one bond | **no corpus object** | `min(C(A,2), 3A)` | 3 |
| planar | triangulated 2-sphere | deltahedron, imported geometry | `3A − 6` | 3 |
| KA | none | excluded at `A ≥ 5` | `C(A,2)` | unbounded |

**Pre-registered word (recommended, and Carl's standing pick unless he chooses otherwise): T3.**
Reason, given before any comparison: it is the only cap above the chain that is already a Lean object
in the corpus, and on `A ≤ 4` it reproduces the corpus's own `K_A` bond graphs (1, 3, 6 bonds). V3 is
the same cap without the colour label; the two differ only at odd `A ≥ 5`, by one bond.

**Warning recorded before the comparison.** V6 and planar give about 3 bonds per nucleon, which is what
AME needs at the ruled bond's scale. That agreement is why they are listed, not a reason to pick them.
Choosing either because it matches would be selection against the target.

## Predictions fixed here

`B(A) = M(A) · b`, with the ruled `T_z`-even bond `b = −s · ln(z − h/2)` at the proton pin:
`−ln(z − h/2) = 0.676963077037981`, `b = 2.53486093323866` MeV at `s = α = 8 m_e G` and
`2.86185014055348` MeV at `s = E₀` (tower). The pn bond offset of `binding_ruled_tz_even` and every
non-strong term (EM, isospin, flavour) are left out: this is the strong bond count only.

| A | chain | **T3** | V3 | V6 | planar | B(T3), α | B(T3), E₀ |
|---|---|---|---|---|---|---|---|
| 2 | 1 | **1** | 1 | 1 | 1 | 2.535 | 2.862 |
| 3 | 2 | **3** | 3 | 3 | 3 | 7.605 | 8.586 |
| 4 | 3 | **6** | 6 | 6 | 6 | 15.209 | 17.171 |
| 6 | 5 | **9** | 9 | 15 | 12 | 22.814 | 25.757 |
| 12 | 11 | **18** | 18 | 36 | 30 | 45.627 | 51.513 |
| 16 | 15 | **24** | 24 | 48 | 42 | 60.837 | 68.684 |
| 56 | 55 | **84** | 84 | 168 | 162 | 212.928 | 240.395 |

Full table (A = 2..12, 16, 20, 24, 40, 56, 60, every premise, both scales) in
`nucleus-bond-valence.witness.json`.

## What the comparison will report

`compare_ame.py` will report, for every nuclide in the AME table, `B(T3)/B_AME` at both scales, its
mean over `A ≥ 16`, and the same for the other premises **as comparison only**. It will not change the
pre-registered word whatever the numbers are.
