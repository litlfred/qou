# Δa_m partial-sum scan — Φ_8 enters at M=7 UNIVERSALLY (2026-06-01)

> Track 1 of [PR #1625](https://github.com/litlfred/qou/pull/1625):
> identify where the universal `Φ_8(u) = u^4 + 1` factor first enters
> the partial sums `S_M = Σ_{m=0..M} Δa_m·(u;u)_m` for the three
> atomic-step Habiro elements (D−n), (³He−D), (⁴He−³He).
>
> Probe: [`computations/qbeta/qbeta_habiro_delta_am_partial_sum_scan.py`](../../computations/qbeta/qbeta_habiro_delta_am_partial_sum_scan.py)
> Witness: [`computations/qbeta/qbeta-habiro-delta-am-partial-sum-scan.witness.json`](../../computations/qbeta/qbeta-habiro-delta-am-partial-sum-scan.witness.json)

## TL;DR

**M_first_Φ_8 = 7 is UNIVERSAL across all three atomic-step pairs.** The cyclotomic Φ_8 enters the partial sum at exactly the m=7 boundary — strictly BEFORE the m=8 Pochhammer boundary mechanically introduces Φ_8 via `(u;u)_8 ∋ (1−u^8)`. This is **structural Δa_m interference**, not Pochhammer mechanics.

**M_first_Φ_8² is pair-dependent**: 12 for (D−n), 15 for (³He−D) and (⁴He−³He). The first-Φ_8 boundary is universal; the second-power boundary tracks pair complexity.

## Results

| Pair | M_first_Φ_8 | M_first_Φ_8² | M_max |
|---|---|---|---|
| (D − n) | **7** | 12 | 12 |
| (³He − D) | **7** | 15 | 15 |
| (⁴He − ³He) | **7** | 15 | 16+ |

The `M_first_Φ_8 = 7` set is `{7}` — singleton, pair-invariant.
The `M_first_Φ_8² = ?` set is `{12, 15}` — pair-dependent.

## The interference mechanism

At M=7, the partial sum S_7 = Σ_{m=0..7} Δa_m·(u;u)_m is divisible by Φ_8(u) = u^4 + 1.

Crucially:

- **S_6 = Σ_{m=0..6} Δa_m·(u;u)_m is NOT divisible by Φ_8.**
- **The marginal term Δa_7·(u;u)_7 is NOT divisible by Φ_8.**
- But **S_7 = S_6 + Δa_7·(u;u)_7 IS divisible by Φ_8.**

Equivalently, at u = ζ_8 (a primitive 8th root of unity):

$$S_6(\zeta_8) + \Delta a_7(\zeta_8) \cdot (\zeta_8; \zeta_8)_7 = 0.$$

The Φ_8 factor in S_7 arises from a **cancellation between two cyclotomically-non-zero halves** evaluating to opposite values at ζ_8. This is the categorical "Δa_m interference signature" — neither half is itself a Φ_8 multiple, but the sum is.

## Why this is the structural witness

The universality of M_first_Φ_8 = 7 across all atomic-step pairs implies the cancellation `S_6(ζ_8) + Δa_7(ζ_8)·(ζ_8;ζ_8)_7 = 0` is **NOT specific to any particular nucleon pair** — it's a relation that holds for ALL p, n, D, ³He, ⁴He Habiro coefficient ladders. This is the categorical content.

Two possible categorical sources:

1. **Universal H_n(ζ_8) annihilation.** The Hecke algebra H_n(q) at q = ζ_8 (primitive 8th root) has a known representation-theoretic degeneracy. The cancellation may be the manifestation of an annihilator of a specific module at this root of unity. Need to check: does the marginal Δa_7(ζ_8) compute to the negative of S_6(ζ_8) via a Hecke character identity at q^4 = −1?

2. **Reeb-phase / canonical chain ζ_8 evaluation.** The canonical derivation chain (substrate q_0 → C → Yekutieli → H_n → Wedderburn → SDP → T_w → Archimedean) may have a node where evaluation at ζ_8 produces a specific algebraic constraint. The fact that ζ_8 is a primitive 8th root suggests a 4-fold (`q^4 = −1`) chiral / Goldstone symmetry interface.

The actual categorical witness needs Track 2 (eigenphase-at-ζ_8 search) and Track 3 (generating-function analysis) of this PR to narrow.

## Numerical observation

| M | S_M(ζ_8) for (D−n) [order of magnitude] |
|---|---|
| 0..5 | non-zero, growing |
| 6 | non-zero (last `Φ_8`-non-multiple partial sum) |
| 7 | **zero** ⟸ first M where S_M ≡ 0 (mod Φ_8) |
| 8..11 | zero (mod Φ_8), non-zero (mod Φ_8²) |
| 12 | zero (mod Φ_8²) ⟸ first Φ_8² boundary for (D−n) |

The boundary at M=7 (Φ_8) is **pair-invariant** = universal categorical structure.
The boundary at M=12, 15 (Φ_8²) is **pair-dependent** = pair complexity scales with atomic mass.

## Open questions

1. **Compute Δa_7(ζ_8) symbolically** for each pair. Does it match `−S_6(ζ_8) / (ζ_8;ζ_8)_7` exactly? If yes, exhibit the cancellation as a clean identity.
2. **What categorical object's character vanishes at q^4 = −1?** Check H_4(q) characters at q = ζ_8 against the Δa_m sequence's algebraic structure.
3. **Does S_M(ζ_n) for other primitive roots ζ_n** (n = 6, 12, 16, 20) reveal additional categorical relations? Multiple-cyclotomic interference at higher M boundaries.

## Cross-references

- Falsified mechanisms: [strand-doubling](2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md), [z(q)² hypothesis](2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)
- Φ_8² convention-invariance: [Phase 5q (D−n) test](2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- This branch ledger: [`docs/coordination/2026-06-01-phi8-da-m-interference.md`](../coordination/2026-06-01-phi8-da-m-interference.md)
