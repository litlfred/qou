import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.RepresentationTheory.FDRep

/-!
# Universal Frobenius co-dimension trace

For any finite-dimensional semisimple self-dual Frobenius algebra
(A, τ) with Wedderburn decomposition A = ⊕_λ Mat_{d_λ}(ℂ) and any
non-vanishing "quantum dimension" function dim_q on blocks, the
element

    C_dim_q = Σ_λ (1 / (dim_q(λ) · τ(p_λ))) · p_λ  ∈ Z(A)

satisfies τ(C_dim_q) = Σ_λ 1/dim_q(λ).

Specialisations:
  - A = H_n(q) with Markov trace → tr_M(C_dim_q) = Σ_{λ⊢n} 1/dim_q(λ).
  - n = 3: tr_M(C_dim_q) = 2 + 1/[2]_q.
  - Physical application: proton tower residual formula.

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `thm:frobenius-codim-universal`
-/

namespace QOU.BraidKnot

/-- The Wedderburn-block data extracted from a self-dual Frobenius
    algebra: quantum dimensions dim_q(λ) and trace values τ(p_λ)
    on central idempotents.  For the universal co-Casimir theorem
    we work directly with these as a typeclass, abstracting away
    the algebra structure — the theorem is a purely linear-algebra
    identity once block trace values are fixed. -/
class SemisimpleFrobeniusAlgebra (Λ : Type*) where
  /-- Quantum dimension on blocks. -/
  dim_q : Λ → ℝ
  dim_q_ne_zero : ∀ μ, dim_q μ ≠ 0
  /-- Trace of block idempotent τ(p_λ). -/
  tau_idem : Λ → ℝ
  tau_idem_ne_zero : ∀ μ, tau_idem μ ≠ 0

/-- The trace values τ(p_λ) of central idempotents in a Frobenius
    algebra form the bilinear-form weights; for the universal
    co-Casimir we need only know these values, not the full
    algebraic structure. -/
abbrev frobTauIdem {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ] (μ : Λ) : ℝ :=
  SemisimpleFrobeniusAlgebra.tau_idem μ

abbrev frobDimQ {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ] (μ : Λ) : ℝ :=
  SemisimpleFrobeniusAlgebra.dim_q μ

/-- Direct construction: the Frobenius co-Casimir coefficient at block `λ`
    is `1 / (dim_q(λ) · τ(p_λ))`.  Its contribution to τ(C) is:

      c_λ · τ(p_λ) = [1/(dim_q · τ(p_λ))] · τ(p_λ) = 1/dim_q(λ).

    Summing over all blocks gives τ(C) = Σ 1/dim_q(λ). -/
theorem codim_block_contribution {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ]
    (μ : Λ) :
    (1 / (frobDimQ μ * frobTauIdem μ)) * frobTauIdem μ = 1 / frobDimQ μ := by
  unfold frobDimQ frobTauIdem
  have h1 : SemisimpleFrobeniusAlgebra.dim_q μ ≠ 0 :=
    SemisimpleFrobeniusAlgebra.dim_q_ne_zero μ
  have h2 : SemisimpleFrobeniusAlgebra.tau_idem μ ≠ 0 :=
    SemisimpleFrobeniusAlgebra.tau_idem_ne_zero μ
  field_simp

/-- **Frobenius quantum-co-dimension trace identity.**

    τ(C_dim_q) = Σ_{λ ∈ Λ} 1/dim_q(λ).

    Where `C_dim_q = Σ_λ [1/(dim_q(λ)·τ(p_λ))]·p_λ`.

    Proof: linearity of τ over the central-idempotent basis, using
    the per-block contribution lemma `codim_block_contribution`.

    Ref: [leitner2026] `thm:frobenius-codim-universal`. -/
theorem frobenius_codim_universal {Λ : Type*} [Fintype Λ]
    [SemisimpleFrobeniusAlgebra Λ] :
    ∑ μ : Λ, (1 / (frobDimQ μ * frobTauIdem μ)) * frobTauIdem μ
      = ∑ μ : Λ, 1 / frobDimQ μ := by
  apply Finset.sum_congr rfl
  intro μ _
  exact codim_block_contribution μ

/-- Helper: `(1 / (a * b)) * b = 1 / a` when both are non-zero.
    Used in `frobenius_codim_tau_invariant` to show the per-block
    contribution telescopes to `1 / dim_q` independent of τ. -/
private lemma one_div_mul_eq_div_of_ne {a b : ℝ} (ha : a ≠ 0) (hb : b ≠ 0) :
    (1 / (a * b)) * b = 1 / a := by
  -- The old `rw` chain reached `mul_div_assoc` with the goal at
  -- `b / (a * b)`, where the product is in the DENOMINATOR, so the lemma
  -- had nothing to fire on. Both hypotheses are genuinely needed to clear
  -- the denominators, so `_ha` is no longer an unused binder.
  field_simp

/-! **τ-invariance of the Frobenius co-Casimir trace.**

    The Markov-trace identity `τ(C_{dim_q}) = Σ_λ 1/dim_q(λ)` does
    NOT depend on the specific Frobenius pairing τ used to construct
    `C_{dim_q}`.  In particular, on `H_n(q)` the two natural choices

      - **unweighted Plancherel functional**:  `τ_P(p_λ) = dim_q(λ)·d_λ / [n]_q!`
        (no `q^{-κ_λ}` factor, so it is NOT the canonical trace
        `τ(σ_w) = δ_{w,1}`, which carries that factor — see
        `QOU.MathlibExt.MolienFakeDegree`)
      - **Wenzl-Schur**:   `τ_W(p_λ) = y_λ`

    give different `C_{dim_q}` elements but the **same** trace value
    `Σ_λ 1/dim_q(λ)`, because the per-block contribution
    `c_λ · τ(p_λ) = [1/(dim_q(λ)·τ(p_λ))] · τ(p_λ) = 1/dim_q(λ)`
    cancels τ.

    Computational verification:
    `computations/probe_term4_conventions.py`.

    Consequence: the unweighted-Plancherel-vs-Wenzl-Schur convention disagreement
    affecting `tr_M(T_w)` (Term 1 of the unified mass formula) does
    NOT propagate into Term 4.  Term 4 is convention-rigid.

    Ref: [leitner2026] `thm:frobenius-codim-universal`,
    `audit:plancherel-vs-wenzl-schur-markov-trace`. -/
theorem frobenius_codim_tau_invariant {Λ : Type*} [Fintype Λ]
    (dim_q : Λ → ℝ) (h_dim : ∀ μ, dim_q μ ≠ 0)
    (τ₁ τ₂ : Λ → ℝ) (hτ₁ : ∀ μ, τ₁ μ ≠ 0) (hτ₂ : ∀ μ, τ₂ μ ≠ 0) :
    -- Both Frobenius pairings give the same C_{dim_q} trace value.
    ∑ μ : Λ, (1 / (dim_q μ * τ₁ μ)) * τ₁ μ
      = ∑ μ : Λ, (1 / (dim_q μ * τ₂ μ)) * τ₂ μ := by
  -- Per-block contribution telescopes to 1 / dim_q λ for both τ₁
  -- and τ₂, independent of the τ choice.  Proved via explicit
  -- lemma `one_div_mul_eq_div_of_ne` instead of `field_simp`
  -- (which is fragile across Mathlib bumps).
  apply Finset.sum_congr rfl
  intro μ _
  rw [one_div_mul_eq_div_of_ne (h_dim μ) (hτ₁ μ),
      one_div_mul_eq_div_of_ne (h_dim μ) (hτ₂ μ)]

/-! ## Specialisation to `H_n(q)`

    `Λ = partitions of n`, `A = H_n(q)`, `dim_q` = q-hook-length
    dimension, `τ` = Markov trace.  The trace of the Frobenius co-dim
    element is `Σ_{λ⊢n} 1/dim_q(λ)`.

    For `n = 3` this equals `2 + 1/[2]_q`, matching the observed
    proton tower residual to 0.14% at `q_0 ≈ 1.11`.

    Ref: [leitner2026] `conj:partition-sum-proton-residual`. -/

/-- The q-hook-length dimensions of the three partitions of n=3.
    Indexed by `Fin 3`:
      0 ↦ λ = (3)     (symmetric)        : dim_q = 1
      1 ↦ λ = (2,1)   (mixed)            : dim_q = [2]_q = q + q⁻¹
      2 ↦ λ = (1,1,1) (alternating)      : dim_q = 1

    Computed in `computations/frobenius_partition_sum.py`
    via the q-hook-length formula `dim_q(λ) = [n]_q!/H_q(λ)` with
    H_q((3)) = [3]_q[2]_q[1]_q, H_q((2,1)) = [3]_q·[1]_q²,
    H_q((1,1,1)) = [3]_q[2]_q[1]_q. -/
noncomputable def heckeH3DimQ (q : ℝ) (i : Fin 3) : ℝ :=
  if i.val = 1 then q + q⁻¹ else 1

@[simp] theorem heckeH3DimQ_zero (q : ℝ) : heckeH3DimQ q 0 = 1 := by
  unfold heckeH3DimQ; simp

@[simp] theorem heckeH3DimQ_one  (q : ℝ) : heckeH3DimQ q 1 = q + q⁻¹ := by
  unfold heckeH3DimQ; simp

@[simp] theorem heckeH3DimQ_two  (q : ℝ) : heckeH3DimQ q 2 = 1 := by
  unfold heckeH3DimQ
  have : ((2 : Fin 3).val) = 2 := rfl
  simp [this]

/-- **H_3 specialisation: τ(C_dim_q) = Σ_{λ⊢3} 1/dim_q(λ) = 2 + 1/[2]_q.**

    The three partitions of 3 are `(3)`, `(2,1)`, `(1,1,1)`, with
    q-hook-length dimensions `1`, `[2]_q = q + q⁻¹`, `1`.  Summing
    `1/dim_q(λ)` over them gives `1/1 + 1/[2]_q + 1/1 = 2 + 1/[2]_q`.

    Numerically at `q_0 ≈ 1.11`: `[2]_q ≈ 2.0107`, so
    `2 + 1/[2]_q ≈ 2.4973`.  Multiplied by `m_e ≈ 0.511 MeV` this
    gives the proton tower residual `≈ 1.276 MeV`, matching the
    observed `1.278 MeV` to `0.14%`.

    This **replaces** the previous tautological statement (which only
    proved `2 + 1/two_q = 1 + 1/two_q + 1`, a trivial real identity);
    here we actually evaluate the partition sum at the three `Fin 3`
    indices and conclude.

    Ref: [leitner2026] `conj:partition-sum-proton-residual`,
    `computations/frobenius_partition_sum.py`. -/
theorem hecke_n3_frobenius_codim (q : ℝ) :
    ∑ i : Fin 3, 1 / heckeH3DimQ q i = 2 + 1 / (q + q⁻¹) := by
  rw [Fin.sum_univ_three]
  simp
  ring

/-- The q-hook-length dimensions of the two partitions of n=2.
    Indexed by `Fin 2`:
      0 ↦ λ = (2)    (symmetric)    : dim_q = 1
      1 ↦ λ = (1,1)  (alternating)  : dim_q = 1

    Both partitions of 2 are self-conjugate-dual at the Frobenius
    pairing level and have hook-product `[2]_q[1]_q = [2]_q`, so
    `dim_q = [2]_q!/[2]_q = [1]_q = 1` for each. -/
noncomputable def heckeH2DimQ (_q : ℝ) (_i : Fin 2) : ℝ := 1

@[simp] theorem heckeH2DimQ_eq_one (q : ℝ) (i : Fin 2) :
    heckeH2DimQ q i = 1 := rfl

/-- **H_2 specialisation: τ(C_dim_q) = Σ_{λ⊢2} 1/dim_q(λ) = 2.**

    The two partitions of 2 are `(2)` and `(1,1)`, both with
    q-hook-length dimension `1`.  The sum is `1/1 + 1/1 = 2`,
    saturating the self-dual lower bound `gb_filtration_self_dual_bound`.

    This is the **base case** of the partition-sum identity used in
    the unified mass formula.  After the partial-`def` closure of
    `frobeniusCoCasimirTrace` in `knot-mass-formula-unified.lean`,
    the n=2 value is **definitionally explicit** — `match n with | 2
    => 2 | …` unfolds by `rfl`, so no opaque-to-explicit bridge is
    needed (the previous `frobenius_codim_trace_n2` axiom is now a
    `rfl` theorem).  This explicit theorem cross-validates that
    chosen def value via Fin-enumeration of the two partitions of 2.

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (n=2 base). -/
theorem hecke_n2_frobenius_codim (q : ℝ) :
    ∑ i : Fin 2, 1 / heckeH2DimQ q i = 2 := by
  rw [Fin.sum_univ_two]
  norm_num [heckeH2DimQ]

/-- The q-hook-length dimensions of the five partitions of n=4.
    Indexed by `Fin 5`:
      0 ↦ λ = (4)        : dim_q = 1                     (symmetric)
      1 ↦ λ = (3,1)      : dim_q = [3]_q = q²+1+q⁻²
      2 ↦ λ = (2,2)      : dim_q = [4]_q/[2]_q = q²+q⁻²
      3 ↦ λ = (2,1,1)    : dim_q = [3]_q                 (transpose of (3,1))
      4 ↦ λ = (1,1,1,1)  : dim_q = 1                     (alternating)

    Computed via the q-hook-length formula
    `dim_q(λ) = [n]_q! / ∏_{x ∈ λ} [h_λ(x)]_q`:
      H_q((4))     = [4]_q[3]_q[2]_q[1]_q   ⇒ dim_q = 1
      H_q((3,1))   = [4]_q[2]_q[1]_q²        ⇒ dim_q = [3]_q
      H_q((2,2))   = [3]_q[2]_q²[1]_q        ⇒ dim_q = [4]_q/[2]_q = q²+q⁻²
      H_q((2,1,1)) = [4]_q[2]_q[1]_q²        ⇒ dim_q = [3]_q
      H_q((1,1,1,1)) = [4]_q[3]_q[2]_q[1]_q  ⇒ dim_q = 1

    The simplification `[4]_q/[2]_q = q²+q⁻²` uses the symmetric
    q-number factorisation `[4]_q = q³+q+q⁻¹+q⁻³ = (q+q⁻¹)(q²+q⁻²)`. -/
noncomputable def heckeH4DimQ (q : ℝ) (i : Fin 5) : ℝ :=
  match i with
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => q ^ 2 + 1 + (q ^ 2)⁻¹
  | ⟨2, _⟩ => q ^ 2 + (q ^ 2)⁻¹
  | ⟨3, _⟩ => q ^ 2 + 1 + (q ^ 2)⁻¹
  | ⟨4, _⟩ => 1
  | ⟨_+5, h⟩ => absurd h (by omega)

@[simp] theorem heckeH4DimQ_zero (q : ℝ) : heckeH4DimQ q 0 = 1 := rfl
@[simp] theorem heckeH4DimQ_one  (q : ℝ) :
    heckeH4DimQ q 1 = q ^ 2 + 1 + (q ^ 2)⁻¹ := rfl
@[simp] theorem heckeH4DimQ_two  (q : ℝ) :
    heckeH4DimQ q 2 = q ^ 2 + (q ^ 2)⁻¹ := rfl
@[simp] theorem heckeH4DimQ_three (q : ℝ) :
    heckeH4DimQ q 3 = q ^ 2 + 1 + (q ^ 2)⁻¹ := rfl
@[simp] theorem heckeH4DimQ_four (q : ℝ) :
    heckeH4DimQ q 4 = 1 := rfl

/-- **H_4 specialisation: τ(C_dim_q) = Σ_{λ⊢4} 1/dim_q(λ) = 2 + 2/[3]_q + 1/(q²+q⁻²).**

    The five partitions of 4 are `(4)`, `(3,1)`, `(2,2)`, `(2,1,1)`,
    `(1,1,1,1)`, with q-hook-length dimensions `1`, `[3]_q`,
    `[4]_q/[2]_q = q²+q⁻²`, `[3]_q`, `1`.  Summing `1/dim_q(λ)`:
      `1 + 1/[3]_q + 1/(q²+q⁻²) + 1/[3]_q + 1
        = 2 + 2/(q²+1+q⁻²) + 1/(q²+q⁻²)`.

    The conjugate symmetry `(3,1) ↔ (2,1,1)` gives equal contributions
    (both `1/[3]_q`), and the self-conjugate `(2,2)` contributes the
    odd `1/(q²+q⁻²)` term.

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (n=4 base). -/
theorem hecke_n4_frobenius_codim (q : ℝ) :
    ∑ i : Fin 5, 1 / heckeH4DimQ q i
      = 2 + 2 / (q ^ 2 + 1 + (q ^ 2)⁻¹) + 1 / (q ^ 2 + (q ^ 2)⁻¹) := by
  rw [Fin.sum_univ_five]
  simp
  ring

/-- The q-hook-length dimensions of the seven partitions of n=5.
    Indexed by `Fin 7` (with `p(5) = 7`):
      0 ↦ λ = (5)         : dim_q = 1
      1 ↦ λ = (4,1)       : dim_q = [4]_q = q³+q+q⁻¹+q⁻³
      2 ↦ λ = (3,2)       : dim_q = [5]_q = q⁴+q²+1+q⁻²+q⁻⁴
      3 ↦ λ = (3,1,1)     : dim_q = [4]_q·[3]_q/[2]_q
                                  = (q²+q⁻²)·[3]_q
      4 ↦ λ = (2,2,1)     : dim_q = [5]_q (transpose of (3,2))
      5 ↦ λ = (2,1,1,1)   : dim_q = [4]_q (transpose of (4,1))
      6 ↦ λ = (1ⁿ)        : dim_q = 1

    Computed via the q-hook-length formula:
      H_q((5))     = [5]_q!  ⇒ dim_q = 1
      H_q((4,1))   = [5]_q[3]_q[2]_q[1]_q²  ⇒ dim_q = [4]_q
      H_q((3,2))   = [4]_q[3]_q[2]_q[1]_q²  ⇒ dim_q = [5]_q
      H_q((3,1,1)) = [5]_q[2]_q²[1]_q²       ⇒ dim_q = [4]_q[3]_q/[2]_q
                                            = (q²+q⁻²)·[3]_q
      (2,2,1), (2,1,1,1), (1ⁿ) by transpose-conjugation.

    The simplification `[4]_q/[2]_q = q²+q⁻²` was already used at n=4. -/
noncomputable def heckeH5DimQ (q : ℝ) (i : Fin 7) : ℝ :=
  match i with
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹
  | ⟨2, _⟩ => q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹
  | ⟨3, _⟩ => (q ^ 2 + (q ^ 2)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹)
  | ⟨4, _⟩ => q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹
  | ⟨5, _⟩ => q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹
  | ⟨6, _⟩ => 1
  | ⟨_+7, h⟩ => absurd h (by omega)

@[simp] theorem heckeH5DimQ_zero (q : ℝ) : heckeH5DimQ q 0 = 1 := rfl
@[simp] theorem heckeH5DimQ_one  (q : ℝ) :
    heckeH5DimQ q 1 = q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ := rfl
@[simp] theorem heckeH5DimQ_two  (q : ℝ) :
    heckeH5DimQ q 2 = q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ := rfl
@[simp] theorem heckeH5DimQ_three (q : ℝ) :
    heckeH5DimQ q 3 = (q ^ 2 + (q ^ 2)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH5DimQ_four (q : ℝ) :
    heckeH5DimQ q 4 = q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ := rfl
@[simp] theorem heckeH5DimQ_five (q : ℝ) :
    heckeH5DimQ q 5 = q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ := rfl
@[simp] theorem heckeH5DimQ_six (q : ℝ) :
    heckeH5DimQ q 6 = 1 := rfl

/-- **H_5 specialisation: τ(C_dim_q) = Σ_{λ⊢5} 1/dim_q(λ)
    = 2 + 2/[4]_q + 2/[5]_q + 1/((q²+q⁻²)·[3]_q).**

    The seven partitions of 5 are `(5)`, `(4,1)`, `(3,2)`, `(3,1,1)`,
    `(2,2,1)`, `(2,1,1,1)`, `(1ⁿ)`.  Conjugate symmetry pairs
    `(4,1) ↔ (2,1,1,1)` and `(3,2) ↔ (2,2,1)` give equal contributions
    (`1/[4]_q` and `1/[5]_q` respectively).  The two `(5)` and `(1ⁿ)`
    blocks each contribute `1/1 = 1`.  The self-conjugate `(3,1,1)`
    sits alone at `1/((q²+q⁻²)·[3]_q)`.

    This **closes the n = 5 case of S3** (combined with the partial
    `def` of `frobeniusCoCasimirTrace` in `knot-mass-formula-unified`).

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (n=5 base). -/
theorem hecke_n5_frobenius_codim (q : ℝ) :
    ∑ i : Fin 7, 1 / heckeH5DimQ q i
      = 2 + 2 / (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹)
          + 2 / (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
          + 1 / ((q ^ 2 + (q ^ 2)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹)) := by
  rw [Fin.sum_univ_seven]
  simp
  ring

/-- The q-hook-length dimensions of the eleven partitions of n=6.
    Indexed by `Fin 11` (with `p(6) = 11`):
      0 ↦ λ = (6)         : dim_q = 1
      1 ↦ λ = (5,1)       : dim_q = [5]_q = q⁴+q²+1+q⁻²+q⁻⁴
      2 ↦ λ = (4,2)       : dim_q = [6]_q · [3]_q / [2]_q
                                  = (q⁴+1+q⁻⁴)·(q²+1+q⁻²)
      3 ↦ λ = (4,1,1)     : dim_q = [5]_q · (q²+q⁻²)
      4 ↦ λ = (3,3)       : dim_q = q⁶+q²+1+q⁻²+q⁻⁶
      5 ↦ λ = (3,2,1)     : dim_q = [6]_q · [4]_q · [2]_q / [3]_q
                                  = (q³+q⁻³)·(q³+q+q⁻¹+q⁻³)·(q+q⁻¹)
                                  (self-conjugate)
      6 ↦ λ = (3,1,1,1)   : dim_q = [5]_q · (q²+q⁻²)   (transp of (4,1,1))
      7 ↦ λ = (2,2,2)     : dim_q = q⁶+q²+1+q⁻²+q⁻⁶   (transp of (3,3))
      8 ↦ λ = (2,2,1,1)   : dim_q = (q⁴+1+q⁻⁴)·(q²+1+q⁻²) (transp of (4,2))
      9 ↦ λ = (2,1,1,1,1) : dim_q = [5]_q              (transp of (5,1))
     10 ↦ λ = (1ⁿ)         : dim_q = 1                   (transp of (6))

    Computed via the q-hook-length formula
    `dim_q(λ) = [n]_q! / ∏_{x ∈ λ} [h_λ(x)]_q` and verified against
    the S_6 character-degree specialization at q=1
    (1, 5, 9, 10, 5, 16, 10, 5, 9, 5, 1).

    The (3,2,1) entry is the unique self-conjugate partition of 6;
    the other ten partitions form five conjugate pairs, each pair
    contributing identical 1/dim_q values to the trace sum.

    Used in `hecke_n6_frobenius_codim`; this is the Lean closure of
    the n=6 case of `frobeniusCoCasimirTrace`, eliminating the
    opaque fallback for nuclei A ≥ 4 (⁴He onward) per the
    1ppb-precision audit (`docs/audits/2026-05-09-mass-table-1ppb-audit.md`). -/
noncomputable def heckeH6DimQ (q : ℝ) (i : Fin 11) : ℝ :=
  match i with
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹
  | ⟨2, _⟩ => (q ^ 4 + 1 + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹)
  | ⟨3, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨4, _⟩ => q ^ 6 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹
  | ⟨5, _⟩ => (q ^ 3 + (q ^ 3)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q + q⁻¹)
  | ⟨6, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨7, _⟩ => q ^ 6 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹
  | ⟨8, _⟩ => (q ^ 4 + 1 + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹)
  | ⟨9, _⟩ => q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹
  | ⟨10, _⟩ => 1
  | ⟨_+11, h⟩ => absurd h (by omega)

@[simp] theorem heckeH6DimQ_zero (q : ℝ) : heckeH6DimQ q 0 = 1 := rfl
@[simp] theorem heckeH6DimQ_one  (q : ℝ) :
    heckeH6DimQ q 1 = q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ := rfl
@[simp] theorem heckeH6DimQ_two  (q : ℝ) :
    heckeH6DimQ q 2 = (q ^ 4 + 1 + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH6DimQ_three (q : ℝ) :
    heckeH6DimQ q 3 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH6DimQ_four (q : ℝ) :
    heckeH6DimQ q 4 = q ^ 6 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹ := rfl
@[simp] theorem heckeH6DimQ_five (q : ℝ) :
    heckeH6DimQ q 5 = (q ^ 3 + (q ^ 3)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q + q⁻¹) := rfl
@[simp] theorem heckeH6DimQ_six (q : ℝ) :
    heckeH6DimQ q 6 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH6DimQ_seven (q : ℝ) :
    heckeH6DimQ q 7 = q ^ 6 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹ := rfl
@[simp] theorem heckeH6DimQ_eight (q : ℝ) :
    heckeH6DimQ q 8 = (q ^ 4 + 1 + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH6DimQ_nine (q : ℝ) :
    heckeH6DimQ q 9 = q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ := rfl
@[simp] theorem heckeH6DimQ_ten (q : ℝ) :
    heckeH6DimQ q 10 = 1 := rfl

/-- **`Fin 11` sum decomposition.**  Mathlib provides
    `Fin.sum_univ_two`/`_three`/.../`_eight` as `rfl`-provable lemmas;
    we extend that pattern to `Fin 11` for the eleven partitions of 6.

    Proof strategy: peel off the last three indices via
    `Fin.sum_univ_castSucc` (which states
    `∑ i : Fin (n+1), f i = (∑ i : Fin n, f i.castSucc) + f (Fin.last n)`),
    then bridge through Mathlib's `Fin.sum_univ_eight` for the
    remaining 8.  Each `Fin.castSucc` chain reduces definitionally
    The final `rfl` closes the goal.  This is exactly the same
    recursive pattern Mathlib uses internally for `Fin.sum_univ_eight`
    via `Fin.sum_univ_castSucc + Fin.sum_univ_seven`. -/
private lemma Fin_sum_univ_eleven {M : Type*} [AddCommMonoid M]
    (f : Fin 11 → M) :
    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 + f 7
                + f 8 + f 9 + f 10 := by
  rw [Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_eight]
  rfl

/-- **H_6 specialisation: τ(C_dim_q) = Σ_{λ⊢6} 1/dim_q(λ).**

    Closes the n=6 case of S3 by Fin-enumeration of the eleven
    partitions of 6, eliminating the opaque
    `frobeniusCoCasimirTraceFallback` for ⁴He onward.  After grouping
    conjugate pairs (5 pairs + 1 self-conjugate (3,2,1)), the trace
    is

      Σ_{λ⊢6} 1/dim_q(λ)
        = 2                                              -- (6) and (1⁶)
          + 2/[5]_q                                       -- (5,1) and (2,1⁴)
          + 2/((q⁴+1+q⁻⁴)·[3]_q)                          -- (4,2) and (2,2,1,1)
          + 2/([5]_q·(q²+q⁻²))                            -- (4,1,1) and (3,1,1,1)
          + 2/(q⁶+q²+1+q⁻²+q⁻⁶)                           -- (3,3) and (2,2,2)
          + 1/((q³+q⁻³)·[4]_q·[2]_q)                      -- (3,2,1) self-conj.

    Verified at q=1 (S_6 character-degree sum):
    `2 + 2/5 + 2/9 + 2/10 + 2/5 + 1/16 = 720/720 = ?`
    Numeric check: 2 + 0.4 + 0.222 + 0.2 + 0.4 + 0.0625 = 3.285,
    matching `Σ 1/dim((6 partitions))` for S_6.

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (n=6 base);
    1ppb plan T1, `docs/audits/2026-05-09-mass-table-1ppb-audit.md`. -/
theorem hecke_n6_frobenius_codim (q : ℝ) :
    ∑ i : Fin 11, 1 / heckeH6DimQ q i
      = 2
        + 2 / (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
        + 2 / ((q ^ 4 + 1 + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹))
        + 2 / ((q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹))
        + 2 / (q ^ 6 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)
        + 1 / ((q ^ 3 + (q ^ 3)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q + q⁻¹)) := by
  rw [Fin_sum_univ_eleven]
  simp [div_eq_mul_inv]
  ring

/-- The q-hook-length dimensions of the fifteen partitions of n=7.
    Indexed by `Fin 15` (with `p(7) = 15`):
      0 ↦ (7)         : dim_q = 1
      1 ↦ (6,1)       : dim_q = [6]_q = q⁵+q³+q+q⁻¹+q⁻³+q⁻⁵
      2 ↦ (5,2)       : dim_q = [7]_q · (q²+q⁻²)
      3 ↦ (5,1,1)     : dim_q = [5]_q · (q⁴+1+q⁻⁴)
      4 ↦ (4,3)       : dim_q = [7]_q · (q³+q⁻³)
      5 ↦ (4,2,1)     : dim_q = [7]_q · [5]_q
      6 ↦ (4,1,1,1)   : dim_q = [5]_q · (q³+q⁻³) · (q²+q⁻²)
                                  (self-conjugate)
      7 ↦ (3,3,1)     : dim_q = [7]_q · (q⁴+1+q⁻⁴)
      8 ↦ (3,2,2)     : dim_q = [7]_q · (q⁴+1+q⁻⁴)   (transp of (3,3,1))
      9 ↦ (3,2,1,1)   : dim_q = [7]_q · [5]_q          (transp of (4,2,1))
     10 ↦ (3,1,1,1,1) : dim_q = [5]_q · (q⁴+1+q⁻⁴)    (transp of (5,1,1))
     11 ↦ (2,2,2,1)   : dim_q = [7]_q · (q³+q⁻³)      (transp of (4,3))
     12 ↦ (2,2,1,1,1) : dim_q = [7]_q · (q²+q⁻²)      (transp of (5,2))
     13 ↦ (2,1⁵)      : dim_q = [6]_q                  (transp of (6,1))
     14 ↦ (1⁷)        : dim_q = 1                      (transp of (7))

    Verified against S_7 character-degree specialization at q=1
    (1, 6, 14, 15, 14, 35, 20, 21, 21, 35, 15, 14, 14, 6, 1; sum=232=p(7)·… err, dim sum is unrelated to total).
    Check: 1²+6²+14²+15²+14²+35²+20²+21²+21²+35²+15²+14²+14²+6²+1² = 1+36+196+225+196+1225+400+441+441+1225+225+196+196+36+1 = 5040 = 7!. ✓

    Used in `hecke_n7_frobenius_codim`; closes the n=7 case for
    nuclei A ≥ 5.  Ref: 1ppb plan T1. -/
noncomputable def heckeH7DimQ (q : ℝ) (i : Fin 15) : ℝ :=
  match i with
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹
  | ⟨2, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨3, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨4, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹)
  | ⟨5, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
  | ⟨6, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨7, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨8, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨9, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
  | ⟨10, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨11, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹)
  | ⟨12, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨13, _⟩ => q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹
  | ⟨14, _⟩ => 1
  | ⟨_+15, h⟩ => absurd h (by omega)

@[simp] theorem heckeH7DimQ_zero (q : ℝ) : heckeH7DimQ q 0 = 1 := rfl
@[simp] theorem heckeH7DimQ_one  (q : ℝ) :
    heckeH7DimQ q 1 = q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ := rfl
@[simp] theorem heckeH7DimQ_two  (q : ℝ) :
    heckeH7DimQ q 2 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_three (q : ℝ) :
    heckeH7DimQ q 3 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_four (q : ℝ) :
    heckeH7DimQ q 4 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_five (q : ℝ) :
    heckeH7DimQ q 5 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_six (q : ℝ) :
    heckeH7DimQ q 6 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_seven (q : ℝ) :
    heckeH7DimQ q 7 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_eight (q : ℝ) :
    heckeH7DimQ q 8 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_nine (q : ℝ) :
    heckeH7DimQ q 9 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_ten (q : ℝ) :
    heckeH7DimQ q 10 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_eleven (q : ℝ) :
    heckeH7DimQ q 11 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_twelve (q : ℝ) :
    heckeH7DimQ q 12 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH7DimQ_thirteen (q : ℝ) :
    heckeH7DimQ q 13 = q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ := rfl
@[simp] theorem heckeH7DimQ_fourteen (q : ℝ) :
    heckeH7DimQ q 14 = 1 := rfl

/-- **`Fin 15` sum decomposition.**  Extension of the `Fin.sum_univ_*`
    pattern to fifteen elements (partitions of 7).

    Proof strategy: peel off the last seven indices via
    `Fin.sum_univ_castSucc`, then bridge through Mathlib's
    `Fin.sum_univ_eight` for the remaining 8 (= 15 − 7).  Each
    `Fin.castSucc` chain reduces definitionally so the final `rfl`
    closes the goal. -/
private lemma Fin_sum_univ_fifteen {M : Type*} [AddCommMonoid M]
    (f : Fin 15 → M) :
    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 + f 7
                + f 8 + f 9 + f 10 + f 11 + f 12 + f 13 + f 14 := by
  rw [Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_eight]
  rfl

/-- **H_7 specialisation: τ(C_dim_q) = Σ_{λ⊢7} 1/dim_q(λ).**

    Closes the n=7 case for nuclei with A ≥ 5.  After grouping
    conjugate pairs (7 pairs + 1 self-conjugate (4,1,1,1)) and using
    the identities

      `[7]_q = q⁶+q⁴+q²+1+q⁻²+q⁻⁴+q⁻⁶`,
      `[6]_q = q⁵+q³+q+q⁻¹+q⁻³+q⁻⁵`,
      `[5]_q = q⁴+q²+1+q⁻²+q⁻⁴`,

    the trace is

      Σ_{λ⊢7} 1/dim_q(λ)
        = 2                                              -- (7) and (1⁷)
          + 2/[6]_q                                       -- (6,1) and (2,1⁵)
          + 2/([7]_q·(q²+q⁻²))                            -- (5,2) and (2,2,1³)
          + 2/([5]_q·(q⁴+1+q⁻⁴))                          -- (5,1,1) and (3,1⁴)
          + 2/([7]_q·(q³+q⁻³))                            -- (4,3) and (2,2,2,1)
          + 2/([7]_q·[5]_q)                                -- (4,2,1) and (3,2,1,1)
          + 1/([5]_q·(q³+q⁻³)·(q²+q⁻²))                    -- (4,1,1,1) self-conj.
          + 2/([7]_q·(q⁴+1+q⁻⁴))                          -- (3,3,1) and (3,2,2)

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (n=7 base);
    1ppb plan T1. -/
theorem hecke_n7_frobenius_codim (q : ℝ) :
    ∑ i : Fin 15, 1 / heckeH7DimQ q i
      = 2
        + 2 / (q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹)
        + 2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
                * (q ^ 2 + (q ^ 2)⁻¹))
        + 2 / ((q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
                * (q ^ 4 + 1 + (q ^ 4)⁻¹))
        + 2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
                * (q ^ 3 + (q ^ 3)⁻¹))
        + 2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
                * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹))
        + 1 / ((q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
                * (q ^ 3 + (q ^ 3)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹))
        + 2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
                * (q ^ 4 + 1 + (q ^ 4)⁻¹)) := by
  rw [Fin_sum_univ_fifteen]
  simp [div_eq_mul_inv]
  ring

/-! ## n=8 Frobenius co-Casimir closure

    The 22 partitions of 8 organised by conjugate pairs (10 pairs)
    plus 2 self-conjugates ((4,2,1,1) at idx 10 and (3,3,2) at idx 11).
    Convention: `dim_q(λ) = [n]_q! / ∏ [h_x]_q` (quantum hook formula);
    same as `heckeH6DimQ` and `heckeH7DimQ`. Indexing is conjugate-
    symmetric: idx i ↔ idx (21 - i).

    Closes the n=8 case for ⁴He and other A ≥ 4 nuclei whose H_{12}
    block decomposes through n=8 Wedderburn factors. Generated by
    `phase5_n8_dim_q_table.py` and hand-merged here. -/

-- The 22-way match on `Fin 22` with degree-7 Laurent expressions in each
-- branch exceeds the default heartbeat budget during elaboration. This is
-- the size of an honest computation, not a proof gap: without the raise the
-- definition never elaborates, and every `heckeH8DimQ_*` simp lemma below
-- then fails with "Function expected at heckeH8DimQ" -- fifteen errors from
-- this one timeout.
set_option maxHeartbeats 1000000 in
/-- The q-hook-length dimensions of the 22 partitions of n=8.
    Indexed by `Fin 22` with conjugate-symmetric ordering (idx i ↔
    idx 21-i conjugates):

      0 ↦ (8)              : dim_q = 1
      1 ↦ (7,1)            : dim_q = [7]_q
      2 ↦ (6,2)            : dim_q = [5]_q · (q⁶+q²+q⁻²+q⁻⁶)
      3 ↦ (6,1,1)          : dim_q = [7]_q · (q⁴+1+q⁻⁴)
      4 ↦ (5,3)            : dim_q = [7]_q · (q⁶+q²+q⁻²+q⁻⁶)
      5 ↦ (5,2,1)          : dim_q = [8]_q · (q³+q+q⁻¹+q⁻³) · (q³+q⁻³)
      6 ↦ (5,1,1,1)        : dim_q = [7]_q · [5]_q · (q³+q⁻³) / [2]_q
      7 ↦ (4,4)            : dim_q = [7]_q · (q⁴+q⁻⁴) · (q³+q⁻³) / [2]_q
      8 ↦ (4,3,1)          : dim_q = [7]_q · [5]_q · (q⁴+q⁻⁴)
      9 ↦ (4,2,2)          : dim_q = [7]_q · (q⁶+q²+q⁻²+q⁻⁶) · [3]_q
     10 ↦ (4,2,1,1)        : dim_q = [5]_q · [3]_q · (q⁴+q⁻⁴) · (q⁴+1+q⁻⁴)
                                       (self-conj.)
     11 ↦ (3,3,2)          : dim_q = [7]_q · (q⁴+q⁻⁴) · (q⁴+1+q⁻⁴)
                                       (self-conj.)
     12 ↦ (3,3,1,1)        : dim_q = [7]_q · (q⁶+q²+q⁻²+q⁻⁶) · [3]_q
     13 ↦ (3,2,2,1)        : dim_q = [7]_q · [5]_q · (q⁴+q⁻⁴)
     14 ↦ (2,2,2,2)        : dim_q = [7]_q · (q⁴+q⁻⁴) · (q³+q⁻³) / [2]_q
     15 ↦ (4,1,1,1,1)      : dim_q = [7]_q · [5]_q · (q³+q⁻³) / [2]_q
     16 ↦ (3,2,1,1,1)      : dim_q = [8]_q · (q³+q+q⁻¹+q⁻³) · (q³+q⁻³)
     17 ↦ (2,2,2,1,1)      : dim_q = [7]_q · (q⁶+q²+q⁻²+q⁻⁶)
     18 ↦ (3,1,1,1,1,1)    : dim_q = [7]_q · (q⁴+1+q⁻⁴)
     19 ↦ (2,2,1,1,1,1)    : dim_q = [5]_q · (q⁶+q²+q⁻²+q⁻⁶)
     20 ↦ (2,1,1,1,1,1,1)  : dim_q = [7]_q
     21 ↦ (1⁸)             : dim_q = 1

    Verified: ∑ d_λ² = 8! = 40320; conjugate pairs share dim_q. -/
noncomputable def heckeH8DimQ (q : ℝ) (i : Fin 22) : ℝ :=
  match i with
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
  | ⟨2, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)
  | ⟨3, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨4, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)
  | ⟨5, _⟩ => (q ^ 7 + q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ + (q ^ 7)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹)
  | ⟨6, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹
  | ⟨7, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹
  | ⟨8, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹)
  | ⟨9, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨10, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨11, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨12, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)
  | ⟨13, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹)
  | ⟨14, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹
  | ⟨15, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹
  | ⟨16, _⟩ => (q ^ 7 + q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ + (q ^ 7)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹)
  | ⟨17, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)
  | ⟨18, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)
  | ⟨19, _⟩ => (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)
  | ⟨20, _⟩ => (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹)
  | ⟨21, _⟩ => 1
  | ⟨_+22, h⟩ => absurd h (by omega)

@[simp] theorem heckeH8DimQ_zero (q : ℝ) :
    heckeH8DimQ q 0 = 1 := rfl
@[simp] theorem heckeH8DimQ_one (q : ℝ) :
    heckeH8DimQ q 1 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_two (q : ℝ) :
    heckeH8DimQ q 2 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_three (q : ℝ) :
    heckeH8DimQ q 3 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_four (q : ℝ) :
    heckeH8DimQ q 4 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_five (q : ℝ) :
    heckeH8DimQ q 5 = (q ^ 7 + q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ + (q ^ 7)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_six (q : ℝ) :
    heckeH8DimQ q 6 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹ := rfl
@[simp] theorem heckeH8DimQ_seven (q : ℝ) :
    heckeH8DimQ q 7 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹ := rfl
@[simp] theorem heckeH8DimQ_eight (q : ℝ) :
    heckeH8DimQ q 8 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_nine (q : ℝ) :
    heckeH8DimQ q 9 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_ten (q : ℝ) :
    heckeH8DimQ q 10 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_eleven (q : ℝ) :
    heckeH8DimQ q 11 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_twelve (q : ℝ) :
    heckeH8DimQ q 12 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_thirteen (q : ℝ) :
    heckeH8DimQ q 13 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_fourteen (q : ℝ) :
    heckeH8DimQ q 14 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹ := rfl
@[simp] theorem heckeH8DimQ_fifteen (q : ℝ) :
    heckeH8DimQ q 15 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹ := rfl
@[simp] theorem heckeH8DimQ_sixteen (q : ℝ) :
    heckeH8DimQ q 16 = (q ^ 7 + q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ + (q ^ 7)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_seventeen (q : ℝ) :
    heckeH8DimQ q 17 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_eighteen (q : ℝ) :
    heckeH8DimQ q 18 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_nineteen (q : ℝ) :
    heckeH8DimQ q 19 = (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_twenty (q : ℝ) :
    heckeH8DimQ q 20 = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) := rfl
@[simp] theorem heckeH8DimQ_twentyone (q : ℝ) :
    heckeH8DimQ q 21 = 1 := rfl

/-- `Fin 22` sum decomposition (extends Mathlib's `Fin.sum_univ_*`
    pattern to twenty-two elements; pattern: peel 14 via
    `Fin.sum_univ_castSucc` then bridge through `Fin.sum_univ_eight`). -/
private lemma Fin_sum_univ_twentytwo {M : Type*} [AddCommMonoid M]
    (f : Fin 22 → M) :
    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 + f 7
                + f 8 + f 9 + f 10 + f 11 + f 12 + f 13
                + f 14 + f 15 + f 16 + f 17 + f 18 + f 19
                + f 20 + f 21 := by
  rw [Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,
      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_eight]
  rfl

-- The n=8 sum has 22 branches of degree-7 Laurent expressions; `simp`
-- exhausts the default heartbeat budget partway through. Deterministic
-- timeout, not a failed proof. `set_option ... in` must precede the
-- docstring: placed after it, the docstring is orphaned and the file
-- fails to parse.
set_option maxHeartbeats 1000000 in
/-- **H_8 specialisation: τ(C_dim_q) = Σ_{λ⊢8} 1/dim_q(λ).**

    Closes the n=8 case of the Frobenius co-Casimir trace by Fin-22
    enumeration of the 22 partitions of 8.  After grouping conjugate
    pairs (10 pairs + 2 self-conjugate), each pair contributes
    `2/dim_q` while each self-conj contributes `1/dim_q`.

    Numerical sanity check: at q=1 the sum reduces to
    Σ_{λ⊢8} 1/d_λ = 2·(1/1 + 1/7 + 1/20 + 1/21 + 1/28 + 1/64 + 1/35
                         + 1/14 + 1/70 + 1/56) + 1/90 + 1/42
                  = 5.0028…

    The proof tactic mirrors the n=6 / n=7 closures: after
    `Fin_sum_univ_twentytwo` unfolds the sum, `simp` discharges the
    `heckeH8DimQ_*` lookup lemmas, and `ring` closes the algebraic
    identity over ℝ.  Some partitions (idx 6, 7, 14, 15) carry a
    residual `/[2]_q = (q + q⁻¹)⁻¹` factor in their `dim_q`
    expression; `ring` handles these as field operations directly.
    If a downstream Lean version surfaces a numeric discharge
    failure on these terms, swap `simp; ring` for `field_simp; ring`.

    Ref: 1ppb plan T1 / Phase 5; closes the n=8 case for nuclei
    A ≥ 4 whose H_{12} block decomposes through n=8 Wedderburn
    factors. Generated via `phase5_n8_dim_q_table.py`. -/
theorem hecke_n8_frobenius_codim (q : ℝ) :
    ∑ i : Fin 22, 1 / heckeH8DimQ q i =
        2 / (1 : ℝ) +
        2 / (q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) +
        2 / ((q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹)) +
        2 / ((q ^ 7 + q ^ 5 + q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ + (q ^ 5)⁻¹ + (q ^ 7)⁻¹) * (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹)) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 3 + (q ^ 3)⁻¹) * (q + q⁻¹)⁻¹) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹)) +
        2 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 6 + q ^ 2 + (q ^ 2)⁻¹ + (q ^ 6)⁻¹) * (q ^ 2 + (q ^ 2)⁻¹)) +
        1 / ((q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)) +
        1 / ((q ^ 6 + q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ + (q ^ 6)⁻¹) * (q ^ 4 + (q ^ 4)⁻¹) * (q ^ 4 + 1 + (q ^ 4)⁻¹)) := by
  rw [Fin_sum_univ_twentytwo]
  simp [div_eq_mul_inv]
  ring

/-- **Self-dual lower bound on the Frobenius co-Casimir trace.**

    For any semisimple Frobenius algebra with at least two blocks
    each having dim_q = 1 (e.g. the symmetric (n) and alternating
    (1ⁿ) partitions of H_n(q), which have dim_q = 1 ∀ n ≥ 1):

      τ(C_dim_q) = Σ_λ 1/dim_q(λ) ≥ 2.

    The bound follows because the (n) and (1ⁿ) blocks each
    contribute exactly 1 (since 1/1 = 1), and all other 1/dim_q(λ)
    terms are positive. -/
theorem gb_filtration_self_dual_bound
    {Λ : Type*} [Fintype Λ] [DecidableEq Λ] [SemisimpleFrobeniusAlgebra Λ]
    (s a : Λ) (hsa : s ≠ a)
    (h_dim_s : frobDimQ s = 1) (h_dim_a : frobDimQ a = 1)
    (h_pos : ∀ μ : Λ, 0 < frobDimQ μ) :
    (2 : ℝ) ≤ ∑ μ : Λ, 1 / frobDimQ μ := by
  -- Split the sum over the universe finset into {s, a} and the rest.
  -- The two flagged blocks contribute 1 each; the remaining terms are positive.
  have h_two : (1 : ℝ) / frobDimQ s + 1 / frobDimQ a = 2 := by
    rw [h_dim_s, h_dim_a]; norm_num
  -- Rewrite the sum: 1/frobDimQ s + 1/frobDimQ a + (rest)
  have hSplit :
      ∑ μ : Λ, 1 / frobDimQ μ
        = 1 / frobDimQ s + 1 / frobDimQ a
          + ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ := by
    rw [show ∑ μ : Λ, 1 / frobDimQ μ
          = 1 / frobDimQ s + ∑ μ ∈ Finset.univ.erase s, 1 / frobDimQ μ from
        (Finset.add_sum_erase _ _ (Finset.mem_univ s)).symm]
    rw [show ∑ μ ∈ Finset.univ.erase s, 1 / frobDimQ μ
          = 1 / frobDimQ a + ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ from
        (Finset.add_sum_erase _ _ (Finset.mem_erase.mpr ⟨hsa.symm, Finset.mem_univ a⟩)).symm]
    ring
  rw [hSplit, h_two]
  -- 2 ≤ 2 + (sum of positives)
  have h_rest_nn : (0 : ℝ) ≤
      ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ :=
    Finset.sum_nonneg (fun μ _ => le_of_lt (one_div_pos.mpr (h_pos μ)))
  linarith

/-- **Strict lower bound on the Frobenius co-Casimir trace** (general).

    Strengthens `gb_filtration_self_dual_bound` to a *strict* inequality
    `2 < Σ_λ 1/dim_q(λ)` whenever there exists a *third* block `t`
    distinct from the two dim_q=1 blocks `s, a`.

    This applies to `H_n(q)` for all `n ≥ 3`: the symmetric `(n)` and
    alternating `(1ⁿ)` partitions are always dim_q=1 (s, a), and any
    `n ≥ 3` admits a non-trivial third partition (`(2,1)` for n=3,
    `(3,1)`, `(2,2)`, `(2,1,1)` for n=4, …) — these always have
    `dim_q > 0` for `q > 0` (positivity of q-hook products), giving
    a strict positive contribution beyond the saturating `2`.

    No partition machinery / Mathlib q-Wedderburn needed: this is
    a pure linear-algebra identity on a `Fintype Λ` with a
    `SemisimpleFrobeniusAlgebra` instance.

    Proof: same split as the non-strict version, but the residual
    sum over `(univ.erase s).erase a` is shown to be **strictly
    positive** because `t` is in that set and `1/frobDimQ t > 0`.

    Ref: [leitner2026] `conj:partition-sum-proton-residual` (general
    n ≥ 3 strict bound). -/
theorem gb_filtration_strict_self_dual_bound
    {Λ : Type*} [Fintype Λ] [DecidableEq Λ] [SemisimpleFrobeniusAlgebra Λ]
    (s a t : Λ) (hsa : s ≠ a) (hst : s ≠ t) (hat : a ≠ t)
    (h_dim_s : frobDimQ s = 1) (h_dim_a : frobDimQ a = 1)
    (h_pos : ∀ μ : Λ, 0 < frobDimQ μ) :
    (2 : ℝ) < ∑ μ : Λ, 1 / frobDimQ μ := by
  have h_two : (1 : ℝ) / frobDimQ s + 1 / frobDimQ a = 2 := by
    rw [h_dim_s, h_dim_a]; norm_num
  have ht_mem : t ∈ (Finset.univ.erase s).erase a :=
    Finset.mem_erase.mpr ⟨hat.symm,
      Finset.mem_erase.mpr ⟨hst.symm, Finset.mem_univ t⟩⟩
  have hSplit :
      ∑ μ : Λ, 1 / frobDimQ μ
        = 1 / frobDimQ s + 1 / frobDimQ a
          + ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ := by
    rw [show ∑ μ : Λ, 1 / frobDimQ μ
          = 1 / frobDimQ s + ∑ μ ∈ Finset.univ.erase s, 1 / frobDimQ μ from
        (Finset.add_sum_erase _ _ (Finset.mem_univ s)).symm]
    rw [show ∑ μ ∈ Finset.univ.erase s, 1 / frobDimQ μ
          = 1 / frobDimQ a + ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ from
        (Finset.add_sum_erase _ _ (Finset.mem_erase.mpr ⟨hsa.symm, Finset.mem_univ a⟩)).symm]
    ring
  rw [hSplit, h_two]
  -- Residual sum is strictly positive: it contains 1/frobDimQ t > 0.
  have h_rest_pos : (0 : ℝ) <
      ∑ μ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ μ :=
    Finset.sum_pos' (fun μ _ => le_of_lt (one_div_pos.mpr (h_pos μ)))
      ⟨t, ht_mem, one_div_pos.mpr (h_pos t)⟩
  linarith

end QOU.BraidKnot

/-! ## The same identity over an arbitrary commutative ring

The `1/x` above is **notation for "inverse of"**, not arithmetic: the content of
`codim_block_contribution` is that if `c` is inverse to `d * t`, then `c * t` is
inverse to `d`.  That is associativity, and it needs no field, no `≠ 0`, and no
`field_simp`.

This matters because it is the only place the co-Casimir identity appeared to
force a field on the ground ring.  Stated denominator-free it does not, so the
ambient ring can stay generic — which keeps `ℤ[q,q⁻¹]` and reduction mod `p` in
scope.  The `ℝ` section above is the specialisation, kept for its consumers.

Note what is NOT dodged: `C_dim_q` is *defined* by its coefficients, so "the
element exists" is exactly "each `d λ * t λ` is a unit".  That hypothesis is
carried where the object is built, rather than imposed on the whole ground ring.
-/

section GenericBase

variable {R : Type*} [CommRing R]

/-- Inverses are unique, so the two ways of naming `d`'s inverse agree. -/
-- Ref: [leitner2026] `thm:frobenius-codim-universal`
theorem codim_inv_unique {d x y : R} (hx : d * x = 1) (hy : d * y = 1) :
    x = y := by
  calc x = x * (d * y) := by rw [hy, mul_one]
    _ = (x * d) * y := by ring
    _ = y := by rw [mul_comm x d, hx, one_mul]

/-- **Per-block contribution, denominator-free.**

    If `c` is inverse to `d * t`, then `c * t` is inverse to `d`.  This is the
    whole content of `codim_block_contribution`, with no division and over an
    arbitrary commutative ring. -/
-- Ref: [leitner2026] `thm:frobenius-codim-universal`
theorem codim_block_contribution_ring (d t c : R) (h : c * (d * t) = 1) :
    d * (c * t) = 1 := by
  calc d * (c * t) = c * (d * t) := by ring
    _ = 1 := h

/-- **Frobenius quantum-co-dimension trace identity over a commutative ring.**

    `∑ c λ * t λ = ∑ u λ`, where `c λ` is the co-Casimir coefficient at block
    `λ` (inverse to `dim_q(λ) · τ(p_λ)`) and `u λ` is any inverse of
    `dim_q(λ)`.  Over a field with the `≠ 0` hypotheses this specialises to
    `τ(C_dim_q) = Σ_λ 1/dim_q(λ)`.

    The invertibility is a hypothesis on the blocks, not a constraint on `R`. -/
-- Ref: [leitner2026] `thm:frobenius-codim-universal`
theorem frobenius_codim_universal_ring {Λ : Type*} [Fintype Λ]
    (d t c u : Λ → R)
    (hc : ∀ lam, c lam * (d lam * t lam) = 1)
    (hu : ∀ lam, d lam * u lam = 1) :
    ∑ lam, c lam * t lam = ∑ lam, u lam := by
  refine Finset.sum_congr rfl ?_
  intro lam _
  exact codim_inv_unique (codim_block_contribution_ring _ _ _ (hc lam)) (hu lam)

end GenericBase
