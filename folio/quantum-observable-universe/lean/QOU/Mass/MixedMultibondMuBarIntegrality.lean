import Mathlib.Data.Int.Cast.Lemmas
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# Mixed-multibond μ̄-idempotent: the common-weight integer count is refuted

Lean face of the integrality obstruction measured in
`computations/deltalambda/mixed_multibond_mubar_integrality_probe.py`
(audit `docs/audits/2026-07-18-mixed-multibond-mubar-idempotent-integrality.md`).

The audit's next-step-#1 hypothesis is that the mixed-multibond shared channel is
"one |μ̄|-idempotent per light cluster" — a **common scalar weight** `w` times the
(signed) **integer** Milnor triple count `S m ∈ ℤ`:

  `channel m = w · (S m)`,   `S m ∈ ℤ`.

Milnor invariants are integers (Magnus expansion; `binding_mn_milnor_linking.py`),
so this file proves the purely-algebraic consequence: such a model forces the
channel values into **integer proportion**, and — normalised so the single triple
at `m = 2` is the unit — every `channel m` is an **integer multiple** of
`channel 2`. The measured t-series is not (¹⁵N / ¹¹B = 1.22, ¹⁹F / ¹¹B = 0.35), so
no such model exists. What survives is a **q-weighted per-triple magnitude** (the
SDP per-block weight), where `w` is not common — this file rules out only the
common-weight form.

Base ring is a generic `[CommRing R]` (§7c): the statement is pure algebra in `R`
with integer casts `(· : ℤ) → R`; no ordering, no `ℝ`. The archimedean channel
values (MeV) instantiate `R := ℝ` at the consumer, supplying the empirical
`channel m ≠ (k : R) · channel 2` hypothesis from the probe.
-/

namespace QOU.Mass.MixedMultibondMuBarIntegrality

variable {R : Type*} [CommRing R]

/-- **Common-weight models put the channel into integer proportion.** If
`channel m = w · (S m)` with an integer count `S`, then for all `m, k`

  `channel m · (S k) = channel k · (S m)`

(cross-multiplication) — the values are in the integer ratio `S m : S k`,
independent of the common weight `w`. -/
theorem mubar_common_weight_ratio
    (channel : ℕ → R) (w : R) (S : ℕ → ℤ)
    (hmodel : ∀ m, channel m = w * (S m : R)) (m k : ℕ) :
    channel m * (S k : R) = channel k * (S m : R) := by
  rw [hmodel m, hmodel k]; ring

/-- **With the `m = 2` triple as the unit (`S 2 = 1`), every value is an integer
multiple of `channel 2`.** This is the normalisation used by the probe (the single
Borromean triple at `m = 2` is one μ̄ unit). -/
theorem mubar_common_weight_forces_integer_multiple
    (channel : ℕ → R) (w : R) (S : ℕ → ℤ)
    (hmodel : ∀ m, channel m = w * (S m : R)) (hunit : S 2 = 1) (m : ℕ) :
    channel m = (S m : R) * channel 2 := by
  rw [hmodel m, hmodel 2, hunit, Int.cast_one]; ring

/-- **Refutation.** If some measured `channel m` is not an integer multiple of
`channel 2`, no common-weight integer-count μ̄-idempotent model (normalised at the
`m = 2` unit) can reproduce it. The hypothesis `hnonmult` is the empirical input
(the probe: ¹⁵N/¹¹B = 1.22, ¹⁹F/¹¹B = 0.35 are not integers). -/
theorem mubar_common_weight_refuted
    (channel : ℕ → R) (w : R) (S : ℕ → ℤ)
    (hmodel : ∀ m, channel m = w * (S m : R)) (hunit : S 2 = 1) (m : ℕ)
    (hnonmult : ∀ k : ℤ, channel m ≠ (k : R) * channel 2) : False :=
  hnonmult (S m) (mubar_common_weight_forces_integer_multiple channel w S hmodel hunit m)

/-! ## The surviving q-weighted form is under-determined per level (anti-laundering)

The refutation above kills the **common-weight** form (one scalar `w`, over-
determined by the several `channel m`). What survives is a **per-triple weighted**
sum `channel m = Σ_{i ∈ triples m} w_i · μ̄_i` with the weights `w_i` *not* common.
This lemma states the honest epistemic status of that survivor: at a single level
with `N ≥ 1` triples and a nonzero μ̄, the `N` free weights can reproduce **any**
target `channel` value — so the q-weighted form is **unfalsifiable from the channel
value alone**. It is therefore a *fit* unless the weights are supplied by an
independent derivation (the confinement-SDP per-block LP duals, #3802) rather than
read off the observable. This is the anti-laundering companion to the refutation:
"q-weighted survives" is not a free closure. Base ring `[Field R]` (division). -/
theorem qweighted_matches_any_single_level
    {R : Type*} [Field R] {ι : Type*} [DecidableEq ι]
    (triples : Finset ι) (i₀ : ι) (hi₀ : i₀ ∈ triples) (mubar : ι → R)
    (h : mubar i₀ ≠ 0) (c : R) :
    ∃ w : ι → R, ∑ i ∈ triples, w i * mubar i = c := by
  refine ⟨fun i => if i = i₀ then c / mubar i₀ else 0, ?_⟩
  rw [Finset.sum_eq_single i₀]
  · dsimp only; rw [if_pos rfl]; exact div_mul_cancel₀ c h
  · intro b _ hb; dsimp only; rw [if_neg hb, zero_mul]
  · intro h'; exact absurd hi₀ h'

/-- **Vanishing difference form of `mubar_common_weight_forces_integer_multiple` (`qou-7tr2`).**
If `∀ m, channel m = w * (S m : R)` and `S 2 = 1`, then
`channel m - (S m : R) * channel 2 = 0`. -/
theorem mubar_common_weight_sub_integer_multiple_eq_zero
    (channel : ℕ → R) (w : R) (S : ℕ → ℤ)
    (hmodel : ∀ m, channel m = w * (S m : R)) (hunit : S 2 = 1) (m : ℕ) :
    channel m - (S m : R) * channel 2 = 0 :=
  sub_eq_zero.mpr (mubar_common_weight_forces_integer_multiple channel w S hmodel hunit m)

end QOU.Mass.MixedMultibondMuBarIntegrality
