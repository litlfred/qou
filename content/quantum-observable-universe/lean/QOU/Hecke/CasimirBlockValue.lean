import QOU.Hecke.TauDualBasis
import QOU.Hecke.TauSchurElement
import QOU.MathlibExt.CasimirTransport

/-!
# QOU.Hecke.CasimirBlockValue — what `Σ_w T_w T^∨_w` actually is, block by block

The chain closes here.  For any splitting `E : H_n(q) ≃ₐ[K] ∏_λ M_{d_λ}(K)`,

  `E (Σ_w T_w T^∨_w) λ = (d_λ / c_λ) · 1 = (d_λ · s_λ) · 1`,

where `c_λ` is `τ`'s weight on the `λ`-block and `s_λ = 1/c_λ` is the abstract
Schur element of `QOU.Hecke.TauSchurElement`.

## The five pieces, and where each came from

1. `tau_Tw_mul_Tw` — the structure constants (`TauStructureConstants`).
2. `TwDual`, the two expansions, and `mul_casimir_comm` (`TauDualBasis`).
3. `casimir_eq_of_expansions` — the Casimir is the same element for any dual
   pair (`CasimirBasisIndependence`).
4. The matrix-unit dual pair, its left-expansion, and the assembled per-block
   value `d_λ / c_λ` (`CasimirBlockScalar`).
5. The transport of 4 along `E` (`CasimirTransport`).

Only 3 and 5 are bookkeeping; 1, 2 and 4 each carry content.

## Note the dimension factor

The block value is `d_λ / c_λ`, **not** `1 / c_λ = s_λ`.  Writing `s_λ` here
would be wrong by the block dimension — see `CasimirBlockScalar`, where the
factor is traced to a summation whose summand does not depend on its second
index.

## What this still is not

It is the classical step *"the Casimir acts on the `λ`-block by a scalar"*,
made precise and proved.  The remaining steps to Geck–Pfeiffer are `s_λ` as a
character sum, and then (Wenzl) the hook-length product — the latter verified
by `computations/hecke/tau_weights_vs_wenzl_schur_probe.py` only for `n ≤ 3`.
`SchurElementCriterion` still has **no instance**.

`Ref: [geckpfeiffer2000]` §7.2 — attribution.
-/

namespace QOU.Hecke.TwBasis

open QOU.MathlibExt

variable {K : Type*} [Field K] {q : K} {n : ℕ}
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **The Casimir's value on the `λ`-block.**

    `E (Σ_w T_w T^∨_w) λ = (d_λ / c_λ) · 1`, for every splitting and every
    `q ≠ 0`. -/
theorem casimir_apply_block (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (j : ι) :
    E (casimir K q n) j
      = ((Fintype.card (J j) : K) / traceWeight E (tau K q n) a j)
          • (1 : Matrix (J j) (J j) K) := by
  classical
  have hc : ∀ i, traceWeight E (tau K q n) a i ≠ 0 := fun i =>
    traceWeight_tau_ne_zero hq E a i
  have hcas : (∑ p : (i : ι) × (J i × J i),
      pullbackUnit E p * pullbackUnitDual E (traceWeight E (tau K q n) a) p)
      = casimir K q n :=
    casimir_eq_of_dual_pair K q n hq _ _
      (sum_pullback_expansion E (tau K q n) (tau_mul_comm K q n) a hc)
  have hE : E (casimir K q n)
      = ∑ p : (i : ι) × (J i × J i),
          blockUnit (K := K) (J := J) p.1 p.2.1 p.2.2
            * blockUnitDual (K := K) (J := J)
                (traceWeight E (tau K q n) a) p.1 p.2.1 p.2.2 := by
    rw [← hcas, map_sum]
    exact Finset.sum_congr rfl fun p _ => by
      rw [pullbackUnit, pullbackUnitDual, map_mul, AlgEquiv.apply_symm_apply,
        AlgEquiv.apply_symm_apply]
  rw [hE, sum_blockUnit_mul_blockUnitDual_apply]

/-- The same value written with the **abstract Schur element** `s_λ = 1/c_λ`:
    the block scalar is `d_λ · s_λ`. -/
theorem casimir_apply_block_schur (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (j : ι) :
    E (casimir K q n) j
      = ((Fintype.card (J j) : K) * abstractSchurElement E a j)
          • (1 : Matrix (J j) (J j) K) := by
  rw [casimir_apply_block hq E a j, abstractSchurElement, div_eq_mul_inv]

/-! ### `s_λ` as a character sum

Taking the trace of `casimir_apply_block` on the `λ`-block turns the block
*scalar* into a *sum over the Coxeter group*: the left side is
`Σ_w χ_λ(T_w T^∨_w)` and the right is `d_λ² / c_λ`.  That is the fourth of the
five classical steps, and unlike the first three it costs nothing beyond the
trace of a scalar matrix. -/

/-- **The character sum.**  `Σ_w χ_λ(T_w T^∨_w) = d_λ² / c_λ`.

    No hypothesis on the block dimension: this is the form to quote when `K`
    may have positive characteristic, since nothing is divided by `d_λ`. -/
theorem sum_char_Tw_mul_TwDual (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (j : ι) :
    (∑ w, Matrix.trace (E (Tw K q n w * TwDual K q n w) j))
      = (Fintype.card (J j) : K) ^ 2 / traceWeight E (tau K q n) a j := by
  classical
  have hsum : (∑ w, Matrix.trace (E (Tw K q n w * TwDual K q n w) j))
      = Matrix.trace (E (casimir K q n) j) := by
    rw [casimir, map_sum, Finset.sum_apply, Matrix.trace_sum]
  rw [hsum, casimir_apply_block hq E a j, Matrix.trace_smul, Matrix.trace_one,
    smul_eq_mul]
  ring

/-- **The abstract Schur element as a character sum**,
    `s_λ = (Σ_w χ_λ(T_w T^∨_w)) / d_λ²`.

    `hd` is the block dimension being invertible in `K` — automatic in
    characteristic zero with `J j` nonempty, but stated as a hypothesis rather
    than assumed, since nothing else in this development needs `CharZero`. -/
theorem abstractSchurElement_eq_char_sum (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (j : ι) (hd : (Fintype.card (J j) : K) ≠ 0) :
    abstractSchurElement E a j
      = (∑ w, Matrix.trace (E (Tw K q n w * TwDual K q n w) j))
          / (Fintype.card (J j) : K) ^ 2 := by
  rw [sum_char_Tw_mul_TwDual hq E a j, abstractSchurElement]
  field_simp

/-! ### The normalisation identity `Σ_λ d_λ c_λ = 1`

`τ(1) = 1` says the weights are not free: they satisfy one linear constraint,
weighted by the block dimensions.  This is the Lean form of the identity that
pins the normalisation in
`computations/hecke/tau_weights_vs_wenzl_schur_probe.py` — the probe's Tier 1,
checked there symbolically for `n = 1 … 8` against
`c_λ = (1 - Q)^n · schurElement(Q, 0, λ)`.

Note what it is and is not evidence for.  It is a genuine constraint on the
weight *system*, and it is what makes the constant `(1 - Q)^n` the only
possible normalisation for that candidate.  It says nothing per-block, which is
why the probe's Tier 2 (the actual per-λ comparison, `n ≤ 3`) is a separate and
stronger check. -/

/-- **`Σ_λ d_λ · c_λ = 1`.**  The block dimensions weight `τ`'s weights to one,
    because `τ(1) = 1`. -/
theorem sum_dim_mul_traceWeight
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) :
    (∑ i, (Fintype.card (J i) : K) * traceWeight E (tau K q n) a i) = 1 := by
  have h := eq_weightedTrace_of_algEquiv E (tau K q n) (tau_mul_comm K q n) a 1
  rw [tau_one, map_one, weightedTrace] at h
  refine Eq.trans ?_ h.symm
  exact Finset.sum_congr rfl fun i _ => by
    rw [Pi.one_apply, Matrix.trace_one, mul_comm]

end QOU.Hecke.TwBasis
