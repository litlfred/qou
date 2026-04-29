import Mathlib.Algebra.Algebra.Basic
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

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
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
  dim_q_ne_zero : ∀ λ, dim_q λ ≠ 0
  /-- Trace of block idempotent τ(p_λ). -/
  tau_idem : Λ → ℝ
  tau_idem_ne_zero : ∀ λ, tau_idem λ ≠ 0

/-- The trace values τ(p_λ) of central idempotents in a Frobenius
    algebra form the bilinear-form weights; for the universal
    co-Casimir we need only know these values, not the full
    algebraic structure. -/
abbrev frobTauIdem {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ] (λ : Λ) : ℝ :=
  SemisimpleFrobeniusAlgebra.tau_idem λ

abbrev frobDimQ {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ] (λ : Λ) : ℝ :=
  SemisimpleFrobeniusAlgebra.dim_q λ

/-- Direct construction: the Frobenius co-Casimir coefficient at block `λ`
    is `1 / (dim_q(λ) · τ(p_λ))`.  Its contribution to τ(C) is:

      c_λ · τ(p_λ) = [1/(dim_q · τ(p_λ))] · τ(p_λ) = 1/dim_q(λ).

    Summing over all blocks gives τ(C) = Σ 1/dim_q(λ). -/
theorem codim_block_contribution {Λ : Type*} [SemisimpleFrobeniusAlgebra Λ]
    (λ : Λ) :
    (1 / (frobDimQ λ * frobTauIdem λ)) * frobTauIdem λ = 1 / frobDimQ λ := by
  unfold frobDimQ frobTauIdem
  have h1 : SemisimpleFrobeniusAlgebra.dim_q λ ≠ 0 :=
    SemisimpleFrobeniusAlgebra.dim_q_ne_zero λ
  have h2 : SemisimpleFrobeniusAlgebra.tau_idem λ ≠ 0 :=
    SemisimpleFrobeniusAlgebra.tau_idem_ne_zero λ
  field_simp

/-- **Frobenius quantum-co-dimension trace identity.**

    τ(C_dim_q) = Σ_{λ ∈ Λ} 1/dim_q(λ).

    Where `C_dim_q = Σ_λ [1/(dim_q(λ)·τ(p_λ))]·p_λ`.

    Proof: linearity of τ over the central-idempotent basis, using
    the per-block contribution lemma `codim_block_contribution`.

    Ref: [manuscript] `thm:frobenius-codim-universal`. -/
theorem frobenius_codim_universal {Λ : Type*} [Fintype Λ]
    [SemisimpleFrobeniusAlgebra Λ] :
    ∑ λ, (1 / (frobDimQ λ * frobTauIdem λ)) * frobTauIdem λ
      = ∑ λ, 1 / frobDimQ λ := by
  apply Finset.sum_congr rfl
  intro λ _
  exact codim_block_contribution λ

/-- **τ-invariance of the Frobenius co-Casimir trace.**

    The Markov-trace identity `τ(C_{dim_q}) = Σ_λ 1/dim_q(λ)` does
    NOT depend on the specific Frobenius pairing τ used to construct
    `C_{dim_q}`.  In particular, on `H_n(q)` the two natural choices

      - **Plancherel-A**:  `τ_P(p_λ) = dim_q(λ)·d_λ / [n]_q!`
      - **Wenzl-Schur**:   `τ_W(p_λ) = y_λ`

    give different `C_{dim_q}` elements but the **same** trace value
    `Σ_λ 1/dim_q(λ)`, because the per-block contribution
    `c_λ · τ(p_λ) = [1/(dim_q(λ)·τ(p_λ))] · τ(p_λ) = 1/dim_q(λ)`
    cancels τ.

    Computational verification:
    `folio-assistant/computations/probe_term4_conventions.py`.

    Consequence: the Plancherel-vs-Wenzl-Schur convention disagreement
    affecting `tr_M(T_w)` (Term 1 of the unified mass formula) does
    NOT propagate into Term 4.  Term 4 is convention-rigid.

    Ref: [manuscript] `thm:frobenius-codim-universal`,
    `audit:plancherel-vs-wenzl-schur-markov-trace`. -/
/-- Helper: `(1 / (a * b)) * b = 1 / a` when both are non-zero.
    Used in `frobenius_codim_tau_invariant` to show the per-block
    contribution telescopes to `1 / dim_q` independent of τ. -/
private lemma one_div_mul_eq_div_of_ne {a b : ℝ} (_ha : a ≠ 0) (hb : b ≠ 0) :
    (1 / (a * b)) * b = 1 / a := by
  rw [div_mul_eq_mul_div, one_mul, mul_div_assoc, div_self hb, mul_one]

theorem frobenius_codim_tau_invariant {Λ : Type*} [Fintype Λ]
    (dim_q : Λ → ℝ) (h_dim : ∀ λ, dim_q λ ≠ 0)
    (τ₁ τ₂ : Λ → ℝ) (hτ₁ : ∀ λ, τ₁ λ ≠ 0) (hτ₂ : ∀ λ, τ₂ λ ≠ 0) :
    -- Both Frobenius pairings give the same C_{dim_q} trace value.
    ∑ λ, (1 / (dim_q λ * τ₁ λ)) * τ₁ λ
      = ∑ λ, (1 / (dim_q λ * τ₂ λ)) * τ₂ λ := by
  -- Per-block contribution telescopes to 1 / dim_q λ for both τ₁
  -- and τ₂, independent of the τ choice.  Proved via explicit
  -- lemma `one_div_mul_eq_div_of_ne` instead of `field_simp`
  -- (which is fragile across Mathlib bumps).
  apply Finset.sum_congr rfl
  intro λ _
  rw [one_div_mul_eq_div_of_ne (h_dim λ) (hτ₁ λ),
      one_div_mul_eq_div_of_ne (h_dim λ) (hτ₂ λ)]

/-- Specialisation to H_n(q): `Λ = partitions of n`, `A = H_n(q)`,
    `dim_q` = q-hook-length dimension, `τ` = Markov trace.
    The trace of the Frobenius co-dim element is `Σ_{λ⊢n} 1/dim_q(λ)`.

    For `n = 3` this equals `2 + 1/[2]_q`, matching the observed
    proton tower residual to 0.14% at `q_0 ≈ 1.11`.

    Ref: [manuscript] `prop:partition-sum-proton-residual`. -/

/-- The q-hook-length dimensions of the three partitions of n=3.
    Indexed by `Fin 3`:
      0 ↦ λ = (3)     (symmetric)        : dim_q = 1
      1 ↦ λ = (2,1)   (mixed)            : dim_q = [2]_q = q + q⁻¹
      2 ↦ λ = (1,1,1) (alternating)      : dim_q = 1

    Computed in `folio-assistant/computations/frobenius_partition_sum.py`
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

    Ref: [manuscript] `prop:partition-sum-proton-residual`,
    `folio-assistant/computations/frobenius_partition_sum.py`. -/
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
    the unified mass formula.  At n=2 the formula is fully evaluated
    in Lean — no opaque `frobeniusCoCasimirTrace q 2` axiom is
    needed structurally; the bridge in `knot-mass-formula-unified`
    just transports this proved value to the opaque side.

    Ref: [manuscript] `prop:partition-sum-proton-residual` (n=2 base). -/
theorem hecke_n2_frobenius_codim (q : ℝ) :
    ∑ i : Fin 2, 1 / heckeH2DimQ q i = 2 := by
  rw [Fin.sum_univ_two]
  simp

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

    Ref: [manuscript] `prop:partition-sum-proton-residual` (n=4 base). -/
theorem hecke_n4_frobenius_codim (q : ℝ) :
    ∑ i : Fin 5, 1 / heckeH4DimQ q i
      = 2 + 2 / (q ^ 2 + 1 + (q ^ 2)⁻¹) + 1 / (q ^ 2 + (q ^ 2)⁻¹) := by
  rw [Fin.sum_univ_five]
  simp
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
    {Λ : Type*} [Fintype Λ] [SemisimpleFrobeniusAlgebra Λ]
    (s a : Λ) (hsa : s ≠ a)
    (h_dim_s : frobDimQ s = 1) (h_dim_a : frobDimQ a = 1)
    (h_pos : ∀ λ, 0 < frobDimQ λ) :
    (2 : ℝ) ≤ ∑ λ, 1 / frobDimQ λ := by
  -- Split the sum over the universe finset into {s, a} and the rest.
  -- The two flagged blocks contribute 1 each; the remaining terms are positive.
  have h_two : (1 : ℝ) / frobDimQ s + 1 / frobDimQ a = 2 := by
    rw [h_dim_s, h_dim_a]; norm_num
  -- Rewrite the sum: 1/frobDimQ s + 1/frobDimQ a + (rest)
  have hSplit :
      ∑ λ, 1 / frobDimQ λ
        = 1 / frobDimQ s + 1 / frobDimQ a
          + ∑ λ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ λ := by
    rw [show ∑ λ, 1 / frobDimQ λ
          = 1 / frobDimQ s + ∑ λ ∈ Finset.univ.erase s, 1 / frobDimQ λ from
        (Finset.sum_erase_add _ _ (Finset.mem_univ s)).symm]
    rw [show ∑ λ ∈ Finset.univ.erase s, 1 / frobDimQ λ
          = 1 / frobDimQ a + ∑ λ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ λ from
        (Finset.sum_erase_add _ _ (Finset.mem_erase.mpr ⟨hsa.symm, Finset.mem_univ a⟩)).symm]
    ring
  rw [hSplit, h_two]
  -- 2 ≤ 2 + (sum of positives)
  have h_rest_nn : (0 : ℝ) ≤
      ∑ λ ∈ (Finset.univ.erase s).erase a, 1 / frobDimQ λ :=
    Finset.sum_nonneg (fun λ _ => le_of_lt (one_div_pos.mpr (h_pos λ)))
  linarith

end QOU.BraidKnot
