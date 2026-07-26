# Faddeev–Volkov uniqueness keystone (`qou-7xvy`) — canonical arc map

**Date:** 2026-07-26 · **Bean:** `qou-7xvy` + epic `qou-mz4f` · **Axis:** G3 / Faddeev
rigidity · **Tier:** consolidation (verified by sorry-audit + the merged PR chain; no new
Lean claim). Single map of the full arc from input-1 through the G5 assembly.

## Bottom line

The Faddeev–Volkov uniqueness leg for the physical `Φ_b` (`phiBProd` on the substrate branch
`Im b² > 0`) is **sorry-free at every tactic position**, and its once-abstract analytic
endowment has been **eliminated**: the boundedness capstone's `hbdd` input is now a *derived*
consequence of a structural strip-growth class. What remains to fully close `qou-7xvy` is
**assembly with zero Mathlib gaps** — no contour integration, no residue theorem, no new
analysis.

## The two feared walls, both removed

| Original framing | Resolution |
|---|---|
| "input 1 needs infinite-product-analyticity infra Mathlib lacks" | **built + merged** (PR #4272/#4278/#4296): `MeromorphicOn (phiBProd b)` is a theorem on the branch |
| "the growth estimate needs Écalle–Borel / contour integration Mathlib lacks" | **eliminated** (epic `qou-mz4f`): the product form gives the strip bound by elementary product-norm estimates; contour integration is *off the critical path* |

## The full chain (all merged, all sorry-free)

### Input 1 — `phiBProd` is meromorphic on the branch

| Brick | File | PR |
|---|---|---|
| factor / finite-partial-product entire | `PhiBProdFactorAnalytic.lean` | #4272 |
| local-uniform limit of entire is entire | `LocalUniformLimitEntire.lean` | #4278 |
| partial products converge locally uniformly ⇒ `MeromorphicOn phiBProd` | `PhiBProdProductConvergence.lean` | #4296 |
| `MeromorphicOn phiBProd ⇐ product analyticity` | `PhiBProdMeromorphic.lean` | #4223 |
| `meromorphicOrderAt phiBProd ≠ ⊤` | `PhiBProdOrderNeTop.lean` | #4225 |
| no spurious zeros/poles off the lattices | `PhiBProdDivisor.lean` | #4304 |

### Elliptic-freedom exclusion ledger

- even `℘`: excluded **algebraically** by the inversion relation — `InversionKillsEvenElliptic.lean` (#4227a).
- bar-even reciprocal-odd: excluded **algebraically** by σ-unitarity — same file (#4227b).
- non-σ-fixed reciprocal-odd: excluded **analytically** by boundedness (the growth route below).

### Growth-estimate epic `qou-mz4f` (Route B — no contour integral)

| Brick | Lemma(s) | File | PR |
|---|---|---|---|
| **G1** numerator/denominator upper bound | `norm_tprod_one_add_le`, `norm_tprod_{num,den}Factor_le` | `PhiBProdStripBound.lean` | #4328 |
| **G2** denominator lower bound | `norm_tprod_one_add_ge`, `norm_tprod_denFactor_ge` | `PhiBProdStripLowerBound.lean` | #4332 |
| **G3** unconditional `phiBProd` strip bound | `norm_phiBProd_le` | (same) | #4332 |
| **G4** strip-growth class + instance + ratio bound | `FaddeevPhiStripGrowth`, `instPhiBProd`, `ratio_bounded_of_stripGrowth` | `FaddeevPhiStripGrowth.lean` | #4332 |
| **G5 crux** removable-singularity extension | `meromorphicOrderAt_nonneg_of_bounded_punctured`, `norm_le_of_bounded_on_punctured` | `MeromorphicPuncturedBounded.lean` | #4337 |
| **G5 assembly** strip-growth ⇒ proportionality (`hbdd` derived) | `faddeevPhi_proportional_of_stripGrowth` | `FaddeevStripGrowthUniqueness.lean` | (this) |

### Pre-existing reduction machinery (consumed, all merged)

- `FaddeevRigidityMeromorphic.uniqueUpToScalar_of_ratio_dense_periodic` — meromorphic Liouville reduction.
- `CyclicDilogPentagon.ratio_ib_periodic` / `ratio_ibinv_periodic` — the ratio's dense double-periodicity.
- `PeriodLatticeBasis.exists_period_basis`, `DoublyPeriodicBoundedLocalization` — lattice basis + global←compact localization.
- `FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio` — the capstone `faddeevPhi_proportional_of_stripGrowth` now feeds.

## What `faddeevPhi_proportional_of_stripGrowth` establishes

Two `FaddeevPhi` solutions that are both `FaddeevPhiStripGrowth` (comparable in modulus to
`phiBProd`), with `Φ₂`'s zeros isolated and the normal-form identity off `Φ₂`'s zeros, plus
the two dense periodicity loci, are **proportional**. The capstone's analytic `hbdd` is
*derived* — `ratio_bounded_of_stripGrowth` (G4) bounds the raw ratio on `{Φ₂ ≠ 0}`, isolated
zeros make it a punctured-neighborhood bound, and `norm_le_of_bounded_on_punctured` (G5 crux)
promotes it to the global bound.

## The keystone is CLOSED for `phiBProd` (modulo one honest regularity hypothesis)

`PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm` — **any substrate `FaddeevPhi` +
`FaddeevPhiStripGrowth` solution `Φ₁` in meromorphic normal form is proportional to
`phiBProd`.** Every carried input is now discharged:

| Input | Discharge |
|---|---|
| `hbdd` (strip growth) | derived (G1–G5, `FaddeevStripGrowthUniqueness`) |
| `hΦ₂_iso` (zeros isolated) | `PhiBProdZeroIsolation.phiBProd_eventually_ne_zero` |
| `hr_ratio` (normal-form identity) | `PhiBProdHrRatio.hr_ratio_phiBProd` |
| loci density (`Dense S₀`, `Dense S₁`) | `PhiBProdLociDensity` — explicit loci; bad set = prefactor lattice ∪ `phiBProd` zeros (+shift), each countable ⇒ `dense_compl_of_countable` |

The **sole** remaining hypothesis is `MeromorphicNFOn Φ₁` — the honest statement that the
*physical* second solution `Φ_b` is a genuine meromorphic function in normal form (the shift
equations alone do not impose it). There is **no Mathlib gap** and **no unproved axiom**: the
two feared analytic walls (input-1 product analyticity; the growth estimate) are gone, and the
whole specialization chain (zero-isolation, normal-form identity, codiscrete→global boundedness
extension, loci density) is proved and merged. Epic `qou-mz4f` is complete.

### Broadening `MeromorphicNFOn` → `MeromorphicOn` + continuity (honest, not cosmetic)

`PhiBProdUniquenessMeromorphic.phiBProd_uniqueUpToScalar_of_meromorphic` weakens the sole
hypothesis to `MeromorphicOn Φ₁` **plus continuity on the nonzero locus**
(`∀ z, phiBProd z ≠ 0 → ContinuousAt Φ₁ z`). This is a **genuine generalization**, not a
cosmetic rename: bare `MeromorphicOn` is **insufficient** — a meromorphic function may be
discontinuous at an isolated removable point, where the *pointwise* proportionality genuinely
fails. `MeromorphicAt.analyticAt` (meromorphic + continuous ⇒ analytic) supplies the `Φ₁`
analyticity `hr_ratio` needs without any normal-form machinery. `MeromorphicNFOn` implies both
inputs, so this strictly enlarges the class; "meromorphic and continuous where finite" is
exactly what "the physical `Φ_b` is a bona-fide meromorphic function" means.
