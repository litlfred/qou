# Hecke Algebra Formalization — Requirements for Next Session

**Created:** 2026-04-06
**Updated:** 2026-04-06 (incorporated Gemini code review from PR #307)
**Status:** 8 sorries remain across 3 files (AxialCoupling, OrderingIndependence, TMCorrespondence)
**Goal:** Eliminate all Descartes build sorries by building the missing Hecke algebra infrastructure

---

## Executive Summary

The QOU Lean formalization has a **complete** Gröbner–Shirshov basis framework
for `H_n(q)` (in `UGB/GrobnerShirshov/HeckeGS.lean`) and a **complete**
single-generator Hecke↔matrix correspondence (in `TMCorrespondence.lean`).

**What's missing** is the bridge from multi-generator Hecke algebra elements
(products of `σ_i` across different generators `i`) to the 2×2 transfer
matrix representation.  This blocks:

1. **AxialCoupling.lean** (5 sorries) — Borromean half-braids in `H₃(q)`
2. **OrderingIndependence.lean** (2 sorries) — Young symmetric idempotent
3. **TMCorrespondence.lean** (1 sorry) — scaling reconciliation

---

## Blocker Analysis

### B1: Multi-Generator Hecke → Matrix (blocks AxialCoupling)

**Problem:** `halfBorromean(i,j) = σ_i⁻¹ σ_j σ_i σ_j⁻¹` involves TWO
different generators.  The existing `heckeMultiply` in TMCorrespondence.lean
only handles products within a single generator's 2×2 state space.

**What exists:**
- `heckeMultiply(a, b, c, d)` computes `(a·σ + b)(c·σ + d)` using `σ² = HA·σ + 1`
- This gives a 2×2 transfer matrix per generator
- For a single chain (all crossings at one generator), this works perfectly

**What's needed:**
- `H₃(q)` has generators `σ₀, σ₁` with braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁`
- The half-Borromean `σ_i⁻¹ σ_j σ_i σ_j⁻¹` mixes generators
- Need either:
  - **(Option A)** A full `H₃(q)` representation as 6×6 matrices (dim = 3! = 6)
  - **(Option B)** Concrete 3×3 irrep matrices for the standard representation
  - **(Option C)** Use the existing `braidToAlg` from HeckeGS.lean to compute
    the normal form of `σ_i⁻¹ σ_j σ_i σ_j⁻¹`, then extract coefficients

**Recommended approach:** Option C — use the GS infrastructure that already exists.

```
braidToAlg hp [-i, j, i, -j]  →  AlgElement (HeckeGen 3) ℝ
                                  (normal form in deg-lex basis)
```

Then define `halfBorromean` as the result of this computation and prove
properties by unfolding `braidToAlg`.

### B2: Young Symmetric Idempotent (blocks OrderingIndependence)

**Problem:** The ordering independence proof requires the Young symmetrizer
`e_{(n)} = (1/P_n(q²)) Σ_{w ∈ S_n} q^{ℓ(w)} T_w` and its eigenvalue property
`e_{(n)} · T_w = q^{ℓ(w)} · e_{(n)}`.

**What exists:**
- `PathIntegrals.lean` has a `YoungDiagram` structure (rows, non-increasing)
- `HeckeGS.lean` has `braidToAlg` which can embed any signed braid word
- Mathlib has `Equiv.Perm` for permutations

**What's needed:**
1. **Symmetric group enumeration:** `S_n` as `List (Equiv.Perm (Fin n))`
2. **Length function:** `ℓ(w)` = minimal number of adjacent transpositions
3. **Hecke embedding of permutations:** `T_w = braidToAlg(reduced_word(w))`
4. **Young idempotent definition:**
   ```lean
   def youngSymIdempotent (n : ℕ) (hp : HeckeParams) : AlgElement (HeckeGen n) ℝ :=
     (S_n.map (fun w => hp.q ^ length(w) • T_w)).sum / poincare_polynomial(n, hp.q²)
   ```
5. **Eigenvalue property:** `e · T_w = q^{ℓ(w)} · e` for all `w ∈ S_n`

**Note:** For the QOU application, we only need `n ≤ 3` (at most 6 permutations),
so this can be done by explicit enumeration rather than general theory.

### B3: TMCorrespondence Scaling (blocks Layer 3 bridge)

**Problem:** `chainCrossings` uses raw weights `(w_plus_t v, w_zero_t v)` while
`buildChains` uses `crossingMatrix` which doubles pp and nn types:

| Vertex | `chainCrossings` (raw) | `buildChains` (crossingMatrix) |
|--------|------------------------|-------------------------------|
| pp     | `transferMatrix 1 0`   | `2 • T_pp` = `2 • transferMatrix 1 0` |
| nn     | `transferMatrix q² (-q·s)` | `2 • T_nn` = `2 • transferMatrix q² (-q·s)` |
| pn     | `transferMatrix (1+q²) (-q·s)` | `two_T_pn` = `transferMatrix (1+q²) (-q·s)` |

**Fix options:**
- **(A) Adjust `chainCrossings`** to use doubled weights for pp/nn:
  ```lean
  noncomputable def chainCrossings (config : NuclearConfig) (j : ℕ) : CrossingSeq :=
    (config.drop (j + 1)).map fun nk =>
      let nj := config.get! j
      let v := vertexType nj nk
      match v with
      | .pp => (2 * w_plus_t v, 2 * w_zero_t v)  -- doubled
      | .nn => (2 * w_plus_t v, 2 * w_zero_t v)  -- doubled
      | .pn => (w_plus_t v, w_zero_t v)           -- already doubled
  ```
- **(B) Adjust theorem statement** to include `2^k` scaling factor
- **(C) Change `crossingMatrix`** to NOT double pp/nn (use `T_pp` directly)

**Recommended:** Option A — simplest, keeps `buildChains` unchanged.

---

## Deliverables (Ordered by Priority)

### Phase 1: TMCorrespondence Scaling Fix (Quick Win)

**File:** `content/quantum-observable-universe/lean/QOU/Descartes/TMCorrespondence.lean`

**Task:** Fix `chainCrossings` to use doubled weights matching `crossingMatrix`,
then complete the `matrixChain_eq_buildChains` proof.

**Estimated complexity:** Low — the mathematical content is trivial (associativity
of matrix multiplication); the only issue is the scaling mismatch.

**Verification command:**
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.TMCorrespondence
```

### Phase 2: Young Idempotent for H₃(q) (Medium)

**New file:** `content/quantum-observable-universe/lean/QOU/Descartes/YoungIdempotent.lean`

**Task:** Define the symmetric Young idempotent `e_{(n)}` for small `n` (≤ 3)
and prove the eigenvalue property.

**Contents:**
1. `S3_perms : List (Equiv.Perm (Fin 3))` — all 6 permutations of S₃
2. `perm_length : Equiv.Perm (Fin n) → ℕ` — Coxeter length
3. `reduced_word : Equiv.Perm (Fin n) → List (Fin (n-1))` — reduced expression
4. `perm_to_hecke : Equiv.Perm (Fin n) → AlgElement (HeckeGen n) ℝ` — Hecke image
5. `youngSymIdempotent : ℕ → HeckeParams → AlgElement (HeckeGen n) ℝ`
6. `youngSym_eigenvalue : e · T_w = q^{ℓ(w)} · e`

**Then update OrderingIndependence.lean** to use this.

**Verification command:**
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.OrderingIndependence
```

### Phase 3: Multi-Generator Hecke→Matrix for H₃(q) (Hard)

**New file:** `content/quantum-observable-universe/lean/QOU/Descartes/HeckeH3.lean`

**Task:** Formalize the 3-strand Hecke algebra `H₃(q)` with concrete
matrix representations for the symmetric and standard irreps.

**Contents:**
1. `H3_sym_rep : HeckeGen 3 → Matrix (Fin 1) (Fin 1) R_t` — 1D symmetric rep (σ_i ↦ q)
2. `H3_std_rep : HeckeGen 3 → Matrix (Fin 2) (Fin 2) R_t` — 2D standard rep
3. `H3_alt_rep : HeckeGen 3 → Matrix (Fin 1) (Fin 1) R_t` — 1D alternating rep (σ_i ↦ -q⁻¹)
4. Verify representations satisfy Hecke + braid relations
5. `halfBorromean_std : Matrix (Fin 2) (Fin 2) R_t` — concrete matrix for σ₀⁻¹σ₁σ₀σ₁⁻¹ in std rep
6. `borromeanColorAvg_std : Matrix (Fin 2) (Fin 2) R_t` — ⅓(h₀₁ + h₁₂ + h₀₂) in std rep
7. `gA_ratio : FractionRing R_t` — the axial coupling ratio

**Then update AxialCoupling.lean** to use these concrete matrices.

**Verification command:**
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.AxialCoupling
```

---

## Concrete Lake Build Commands

### Full build (all QOU):
```
cd content/quantum-observable-universe/lean && lake exe cache get && lake build
```

### Incremental builds (one file at a time):
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.TMCorrespondence
```
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.OrderingIndependence
```
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.AxialCoupling
```

### Check for remaining sorries:
```
cd content/quantum-observable-universe/lean && grep -rn 'sorry' QOU/ --include="*.lean" | grep -v '^\s*--' | grep -v 'sorry.*--'
```

### UGB build (Gröbner–Shirshov):
```
cd content/unital-groebner-bases/lean && lake exe cache get && lake build
```

---

## Existing Infrastructure to Leverage

### Already proven (DO NOT rewrite):
- `hecke_eq_transfer` — single-generator Hecke↔matrix correspondence ✅
- `chain_correspondence` — iterated chain correspondence ✅
- `optimal_coeff_eq_transfer_state` — NF coefficients = transfer matrix ✅
- `volume_eq_markov_trace` — traced volume = Markov trace ✅
- `q_mul_q_inv` — `q · q⁻¹ = 1` ✅
- `qInt_one`, `qInt_two` — quantum integers ✅

### Already defined (use these types):
- `R_t := LaurentPolynomial ℤ` — ground ring ℤ[t, t⁻¹]
- `R_q := LaurentPolynomial ℤ` — ground ring ℤ[q, q⁻¹]
- `TMatrix := Matrix (Fin 2) (Fin 2) R_t` — 2×2 transfer matrices
- `StateVec := Fin 2 → R_t` — state vectors
- `NuclearConfig := List NucleonType` — nucleon configurations
- `CrossingSeq := List (R_t × R_t)` — crossing coefficient sequences
- `AlgElement (HeckeGen n) ℝ` — Hecke algebra elements (from UGB)
- `HeckeParams` — deformation parameter `q` with positivity/non-classicality

### Mathlib types available:
- `LaurentPolynomial ℤ` — Laurent polynomials
- `Matrix (Fin n) (Fin n) R` — matrices
- `FractionRing R_t` — fraction field
- `Equiv.Perm (Fin n)` — permutations (for Young idempotent)
- `Finset.sum` — finite sums

---

## Architecture Constraints

1. **All proofs over `ℤ[q, q⁻¹]`** (or `ℤ[t, t⁻¹]` where `t = q^{1/2}`).
   Do NOT introduce `ℝ` in the Descartes module.

2. **Use `noncomputable def`** for all definitions involving Laurent polynomials
   (Mathlib's `LaurentPolynomial` is noncomputable).

3. **Keep imports minimal.** New files should import from `QOU.Descartes.*`
   and `Mathlib.*` only — do NOT import UGB directly from QOU.Descartes
   (the cross-dependency goes through `lakefile.toml`).

4. **Citation convention:** Every sorry must have `-- Ref: [key] url` on
   the line immediately before it. Every axiom must have a cited reference.

5. **Lean toolchain:** `leanprover/lean4:v4.24.0` — do not change.

6. **Mathlib pin:** `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` — do not change.

---

## The "Mugen" Blocker Explained

The term "multi-gen" (abbreviated "mugen" in conversation) refers to the
**multi-generator** Hecke algebra representation problem.

The existing TMCorrespondence.lean proves the correspondence for a
**single** generator: the product `(a·σ + b)(c·σ + d)` in the Hecke
algebra (with `σ² = HA·σ + 1`) corresponds to left-multiplication by
the transfer matrix `T(c,d)` on the state vector `(a, b)ᵀ`.

This works perfectly for **nuclear chains** where each generator `σ_j`
represents a single nucleon position and crossings happen between
generators at different positions.

The blocker arises when you need to evaluate a Hecke element that
involves **multiple generators interacting** — specifically:

- The half-Borromean `h_{ij} = σ_i⁻¹ σ_j σ_i σ_j⁻¹` in `H₃(q)` involves
  generators `σ_0` and `σ_1` which satisfy the braid relation
  `σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1`.

- The Young idempotent `e_{(n)} = Σ q^{ℓ(w)} T_w / P_n(q²)` involves
  sums over all permutations, each of which is a product of different
  generators.

The single-generator 2×2 state vector formalism cannot represent these
multi-generator interactions.  You need either:

1. **Full matrix representations** of `H₃(q)` (3! = 6 dimensional regular
   representation, or the 1D + 2D + 1D irrep decomposition), or

2. **Symbolic normal form computation** via the Gröbner–Shirshov rewriting
   system (which is already implemented in HeckeGS.lean's `braidToAlg`).

Option 2 is preferred because HeckeGS.lean already has the infrastructure.
The gap is connecting `AlgElement (HeckeGen n) ℝ` back to the `TMatrix`
world of TransferMatrix.lean.

---

## Success Criteria

When this work is complete:

1. `lake build` succeeds with **zero sorries** in `QOU/Descartes/`
2. `halfBorromean` has a concrete definition (not sorry)
3. `borromeanColorAvg` has a concrete definition (not sorry)
4. `axialCouplingRatio` has a concrete definition (not sorry)
5. `skeinPolynomialSym` has a concrete definition (not sorry)
6. `ordering_independence` has a complete proof (not sorry)
7. `matrixChain_eq_buildChains` has a complete proof (not sorry)
8. All existing proved theorems still compile (no regressions)

---

## Local Lake Build — Quick Start

These are single-line copy-paste commands. Run them in your terminal.

### First time setup (downloads Mathlib cache, ~5 min):
```
cd content/quantum-observable-universe/lean && lake exe cache get
```

### Full build (all QOU Lean, ~10-20 min first time):
```
cd content/quantum-observable-universe/lean && lake build
```

### Build one file at a time (faster iteration):
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.TMCorrespondence
```
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.OrderingIndependence
```
```
cd content/quantum-observable-universe/lean && lake build QOU.Descartes.AxialCoupling
```

### Check sorry count after changes:
```
cd content/quantum-observable-universe/lean && grep -rn 'sorry' QOU/ --include="*.lean" | grep -v '^\s*--'
```

### Build the UGB dependency (Gröbner–Shirshov, only if changed):
```
cd content/unital-groebner-bases/lean && lake exe cache get && lake build
```

### Run the audit scripts:
```
bun run scripts/lean-audit.ts
```
```
bun run scripts/witness-audit.ts
```

---

## Known Issues (from Gemini Review of PR #307)

The following issues were identified by automated code review and have been
addressed in the latest commits:

1. **`sym_trace_ordering_independent` was a tautology** (P → P). Now uses
   `x.trace = y.trace` as hypothesis and is honestly `sorry`-marked,
   awaiting the Young idempotent infrastructure (Phase 2).

2. **`lean-witness.ts isStale`** used non-deterministic globbing and compared
   the wrong SHA field. Now looks up the specific witness for the current
   content hash and compares `meta.fileCommitSha` (not `meta.commitSha`).

3. **`lean-audit.ts auditLeanFile`** duplicated staleness logic. Now delegates
   to the shared `isStale()` function from `lean-witness.ts`.

4. **`lean-audit.ts countCodeLines`** incorrectly filtered `#check`/`#eval` lines.
   The `#` filter has been removed; Lean `#` commands are counted as code.

5. **`witness-audit.ts`** reported duplicate entries when multiple witness files
   existed for one `.lean` file. Now reports exactly one status per file.
