# Hecke Formalization Requirements — Status

**Last updated:** 2026-04-06

## Summary

The Descartes build had **6 sorries** across 3 files. After this work:
- **3 sorries eliminated** (all in AxialCoupling.lean)
- **3 sorries remain** (TMCorrespondence, OrderingIndependence, YoungIdempotent)
- **3 new library files** created for general Hecke algebra infrastructure

## New files created

### HeckeRep.lean — General Iwahori–Hecke Algebra Representations

General framework for representations of H_n(q), not specialized to n=3:

- `HeckeRep n d` structure (generators, Hecke relation, braid relations, far commutativity)
- `genInv` with proven inverse properties (`gen_mul_genInv`, `genInv_mul_gen`)
- `genInv_hecke` (Hecke relation for the inverse)
- `BraidWord` evaluation and `character` computation
- `halfBorromeanMat` and `halfBorromeanConjMat` (general half-Borromean elements)
- `trivRep` and `signRep` instances (1D representations for any n)
- `transferMatrix_comm` and `transferMatrix_swap` (commutativity theorems)

### YoungIdempotent.lean — Young Symmetric Idempotent

General Young idempotent construction:

- `coxeterLength` (inversion count for general S_n)
- `S3_reduced_words` (explicit enumeration of S₃)
- `qSqInt` (q²-integer `[n]_{q²} = 1 + q² + … + q^{2(n-1)}` — sum form, no division)
- `poincarePolynomial` (general n, recursive: `P_n = P_{n-1} · [n]_{q²}`)
- `youngSymIdempotent3` (concrete definition for H₃(q))
- `youngSymIdempotent2` (concrete definition for H₂(q))
- `youngSym3_eigenvalue` (**sorry** — needs 6-case Hecke expansion)

### HeckeH3.lean — Concrete H₃(q) Representations

Explicit standard (2,1) representation with verified relations:

- `stdRep3_gen0`, `stdRep3_gen1` (Jones 1987 seminormal form)
- `stdRep3_hecke0`, `stdRep3_hecke1` (Hecke relation proofs by `ext; fin_cases; ring`)
- `stdRep3_braid` (braid relation proof by `ext; fin_cases; ring`)
- `stdRep3` (full `HeckeRep 3 2` instance)
- `ColorTube` inductive type (rg, gb, rb)
- `halfBorromeanStd` (3 concrete half-Borromean matrices)
- `halfBorromean_trivial_eval` (proven: all half-Borromeans = I in trivial rep)
- `halfBorromeanConj_trivial_eval` (proven: conjugated half-Borromeans = I in trivial rep)
- `borromeanColorSum` (color-averaged Borromean element)
- `axialCouplingAlgebraic` (symbolic ratio in FractionRing R_t)

## Changes to existing files

### TMCorrespondence.lean — Phase 1 (scaling fix)

- **Fixed:** `chainCrossings` now doubles pp/nn weights to match `crossingMatrix`
  - pp: `(2 * w_plus_t .pp, 2 * w_zero_t .pp)` = `(2, 0)`
  - nn: `(2 * w_plus_t .nn, 2 * w_zero_t .nn)` = `(2q², −2q·s)`
  - pn: unchanged `(w_plus_t .pn, w_zero_t .pn)` = `(1+q², −q·s)` (already doubled)
- **Import:** added `HeckeRep` for `transferMatrix_comm`
- **Sorry status:** 1 sorry remains (foldl/structural recursion bridge)
  - The scaling discrepancy is fixed
  - Transfer matrix commutativity is proven
  - The remaining sorry is the fold direction bridge between `matrixChain` (right fold) and `buildChains` (left fold)

### OrderingIndependence.lean — Phase 2

- **Fixed:** `skeinPolynomialSym` replaced sorry with concrete symmetric-rep evaluation
  - Evaluates each crossing in the symmetric rep (σ → q): `∏_j (c_j·q + d_j)`
  - This is manifestly ordering-independent (commutative product of scalars)
- **Import:** added `YoungIdempotent`
- **Sorry status:** 1 sorry remains (combinatorial multiset argument for `ordering_independence`)
  - The symmetric-rep character is a commutative product
  - Need to show: permuted configs give the same multiset of crossing types

### AxialCoupling.lean — Phase 3

- **Fixed:** All 3 sorries eliminated
  - `halfBorromean` → delegates to `stdRep3.halfBorromeanMat` from HeckeH3
  - `borromeanColorAvg` → delegates to `borromeanColorSum` from HeckeH3
  - `axialCouplingRatio` → delegates to `axialCouplingAlgebraic` from HeckeH3
- **Import:** added `HeckeH3`
- **Sorry status:** 0 sorries

## Remaining sorries (3 total)

| File | Line | Description | Difficulty | Blocker |
|------|------|-------------|------------|---------|
| TMCorrespondence.lean | 339 | foldl/structural recursion bridge | Medium | Relating `matrixChain` (right fold) to `buildChains` (left fold) via `transferMatrix_comm` |
| OrderingIndependence.lean | 131 | multiset argument | Medium | Showing permuted configs give same crossing-type multiset |
| YoungIdempotent.lean | 164 | `youngSym3_eigenvalue` | Medium | 6-case expansion of σ_i · e_{(3)} using Hecke relation |

## Standard representation matrices

The standard (2,1) representation of H₃(q) (Jones 1987):

```
σ₀ = ⎡ q    1  ⎤     σ₁ = ⎡ −q⁻¹   0 ⎤
     ⎣ 0   −q⁻¹⎦          ⎣  1      q ⎦
```

Hecke relation: `σ² = (q − q⁻¹)σ + I` ✓ (proven by `ext; fin_cases; ring`)
Braid relation: `σ₀σ₁σ₀ = σ₁σ₀σ₁` ✓ (proven by `ext; fin_cases; ring`)
