/-!
# Brane-tower level-selection rule: n★(ℌ) = ℓ · n₀ + k

This file axiomatizes the level-selection conjecture as a `class`
(following the §3b pattern from AGENTS.md) and proves four downstream
structural results **unconditionally** from the class axioms.

The conjecture (`conj:brane-level-selection`) asserts:

> For a confined particle ℌ with confinement level ℓ, strand count n₀,
> and GB filtration grade k, the canonical cyclotomic truncation level is
>     n★(ℌ) = ℓ · n₀ + k.

All theorems below are purely algebraic — no numerical computation,
no analytic approximation, no quantum-dilogarithm evaluation.

## Results

1. `nStar_pos_of_ell_pos`   — n★ > 0 when ℓ > 0
2. `nStar_ge_k`             — n★ ≥ k always
3. `nStar_strictMono_ell`   — n★ is strictly monotone in ℓ
4. `nStar_ge_n₀_of_ell_pos` — n★ ≥ n₀ when ℓ > 0

## References

- [manuscript] conj:brane-level-selection
- [manuscript] prop:gb-spectral-sequence
- [manuscript] def:confined-particle
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Tactic

namespace QOU.BraneTower

-- Ref: [manuscript] conj:brane-level-selection

/-- The categorical data of a confined particle relevant to the
    level-selection rule:
    - confinement level ℓ,
    - strand count n₀ (≥ 1, from the braid group B_{n₀}),
    - GB filtration grade k (Coxeter length of the normal-form element T_w). -/
-- Ref: [manuscript] def:confined-particle
structure ConfinedParticleData where
  /-- Confinement level ℓ ≥ 0.  Proton/neutron: ℓ = 1.  Nuclei: ℓ = A. -/
  ell : ℕ
  /-- Strand count n₀ = 3A (nucleons) or 2 (electron). -/
  n₀ : ℕ
  /-- n₀ ≥ 1: every braid group B_{n₀} has at least one strand. -/
  n₀_pos : 0 < n₀
  /-- GB filtration grade k = Coxeter length of T_w ∈ H_{n₀}(q) in GB-NF. -/
  k : ℕ

/-- **Level-selection conjecture** (axiomatized as a class).

    An instance of `BraneLevelSelection P` asserts:
      n★(P) = P.ell · P.n₀ + P.k.

    The `nStar_eq` field is the conjecture statement itself; instances
    supply it as a hypothesis (axiomatic input).  All `theorem`s below
    are proved unconditionally from `nStar_eq` — the only "sorry" input
    is the existence of an instance.

    The canonical truncation level n★ is the depth at which the
    cyclotomic projection π_{n★}^{(z)} in the z-Habiro ring
    (`conj:brane-tower-z-habiro`) recovers the empirical binding
    energy without per-atom calibration. -/
-- Ref: [manuscript] conj:brane-level-selection
class BraneLevelSelection (P : ConfinedParticleData) where
  /-- The canonical truncation level. -/
  nStar : ℕ
  /-- The structural formula n★ = ℓ · n₀ + k. -/
  nStar_eq : nStar = P.ell * P.n₀ + P.k

-- ────────────────────────────────────────────────────────────────────────────
-- Downstream conditional theorems
-- All proved from `BraneLevelSelection.nStar_eq` alone; no sorry.
-- ────────────────────────────────────────────────────────────────────────────

/-- **n★ is strictly positive when ℓ > 0.**

    Intuition: at confinement level ℓ ≥ 1, the Yekutieli multiplicative
    integral wraps at least n₀ ≥ 1 generator insertions, so the total
    filtration depth exceeds zero. -/
-- Ref: [manuscript] conj:brane-level-selection §"Proof obligations"
theorem nStar_pos_of_ell_pos (P : ConfinedParticleData) (hℓ : 0 < P.ell)
    [sel : BraneLevelSelection P] : 0 < sel.nStar := by
  rw [sel.nStar_eq]
  have h : 0 < P.ell * P.n₀ := Nat.mul_pos hℓ P.n₀_pos
  omega

/-- **n★ ≥ k always.**

    The GB filtration grade k is the minimal depth contribution from
    the innermost Hecke algebra.  The confinement-level term ℓ · n₀ adds
    non-negatively, so the total is at least k. -/
-- Ref: [manuscript] conj:brane-level-selection §Statement
theorem nStar_ge_k (P : ConfinedParticleData)
    [sel : BraneLevelSelection P] : P.k ≤ sel.nStar := by
  rw [sel.nStar_eq]
  omega

/-- **n★ is strictly monotone in ℓ** (when n₀ and k are fixed).

    A particle at a higher confinement level always requires a deeper
    cyclotomic truncation.  This is purely structural: each additional
    wrapping level contributes n₀ ≥ 1 more generator insertions. -/
-- Ref: [manuscript] conj:brane-level-selection §"Structural motivation"
theorem nStar_strictMono_ell
    (P P' : ConfinedParticleData)
    (hn₀ : P.n₀ = P'.n₀) (hk : P.k = P'.k) (hℓ : P.ell < P'.ell)
    [sel : BraneLevelSelection P] [sel' : BraneLevelSelection P'] :
    sel.nStar < sel'.nStar := by
  rw [sel.nStar_eq, sel'.nStar_eq, hn₀, hk]
  have h : P.ell * P'.n₀ < P'.ell * P'.n₀ :=
    Nat.mul_lt_mul_of_pos_right hℓ P'.n₀_pos
  omega

/-- **n★ ≥ n₀ when ℓ ≥ 1.**

    The truncation depth is at least as large as the strand count:
    the level-1 contribution alone is ℓ · n₀ ≥ n₀. -/
-- Ref: [manuscript] conj:brane-level-selection §"Particle table"
theorem nStar_ge_n₀_of_ell_pos (P : ConfinedParticleData) (hℓ : 0 < P.ell)
    [sel : BraneLevelSelection P] : P.n₀ ≤ sel.nStar := by
  rw [sel.nStar_eq]
  have h : P.n₀ ≤ P.ell * P.n₀ := Nat.le_mul_of_pos_left P.n₀ hℓ
  omega

/-- **n★ is additive in ℓ** (when n₀ and k are the same).

    For a composite system formed by stacking ℓ₁ + ℓ₂ confinement
    levels, the level-selection rule gives
        n★(ℓ₁ + ℓ₂, n₀, k) = n★(ℓ₁, n₀, k) + n★(ℓ₂, n₀, 0).

    Equivalently, n★ = ℓ · n₀ + k decomposes linearly over ℓ. -/
-- Ref: [manuscript] conj:brane-level-selection §"Structural motivation"
theorem nStar_add_ell
    (P₁ P₂ P : ConfinedParticleData)
    (hℓ : P.ell = P₁.ell + P₂.ell)
    (hn₀_1 : P.n₀ = P₁.n₀) (hn₀_2 : P.n₀ = P₂.n₀)
    (hk_split : P.k = P₁.k + P₂.k)
    [sel : BraneLevelSelection P]
    [sel₁ : BraneLevelSelection P₁]
    [sel₂ : BraneLevelSelection P₂] :
    sel.nStar = sel₁.nStar + sel₂.nStar := by
  rw [sel.nStar_eq, sel₁.nStar_eq, sel₂.nStar_eq, hℓ, hn₀_1, hn₀_2, hk_split]
  ring

/-- **Canonical instance.**  For every `ConfinedParticleData P`, the
    `BraneLevelSelection P` instance is given by the rule
    `nStar = P.ell * P.n₀ + P.k`.  This is the structural formula
    asserted by the conjecture; the rule is taken as the canonical
    definition of `nStar` and the `nStar_eq` field discharges by
    `rfl`.  All five downstream theorems then become unconditional
    Lean theorems whenever `[BraneLevelSelection P]` is in scope. -/
-- Ref: [manuscript] conj:brane-level-selection
instance canonical (P : ConfinedParticleData) : BraneLevelSelection P where
  nStar := P.ell * P.n₀ + P.k
  nStar_eq := rfl

end QOU.BraneTower
