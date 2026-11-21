import QOU.MathlibExt.MonotoneWordTraceFactorizes
import QOU.Mass.MarkovBondRuleForcesPairwise
import Mathlib.Tactic

/-!
# `QOU.Mass.FormalityBridgeF1` — the formality bridge: what forces `b₃ = 0`, and what breaks it

The research doc `docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`
§2.1 states, as the first formalize-first item, the conjecture

> **(F1)** a semisimple algebra with a Markov trace, evaluated on a *sequential* juxtaposition
> of pairwise interface words, gives a pair-local `log tr`, hence `b₃ = 0`.

**Corpus-grep, run before writing this file, found F1 already proved in three pieces** — the
doc's §7 item 1 was a miss on my part, and this file is the composition, not a new theorem:

| piece | where | what it proves |
|---|---|---|
| monotone word ⇒ product of letter traces | `QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr` | `tr(s n ⋯ s (n+k−1)) = ∏ tr(s (n+i))` for stabilising letters |
| bond product + any multiplicative-to-additive map ⇒ `b₃ = 0` | `QOU.Mass.MarkovBondRuleForcesPairwise.b3_eq_zero_of_bondRule` | the `b₃` conclusion |
| interleaving breaks the product | `QOU.MathlibExt.InterleavedCrossTerm.interleaved_sub_sequential` | exact cross term `z (z² − h z − 1)` at `n = 4` |

What is added here is the one sentence that joins them, stated so that both hypotheses of F1
are visible in the type:

* `f_tr_stabWord_eq_sum` — **the sequential half.** For *any* map `f` with `f (x·y) = f x + f y`
  (no continuity; §10a's Cauchy condition and nothing more), the `f`-image of a monotone word's
  trace is the **sum** of the letters' `f`-images. So `log tr` of a sequential word is a bond
  sum by construction, and `b3_eq_zero_of_bondRule` finishes. Neither semisimplicity nor any
  property of the trace beyond the Markov axioms enters — which is the point: the zero is forced
  by the **ordering**, and the *semisimplicity* in F1's statement is doing no work at this step.
  (Where semisimplicity does bite is one level up: `QOU.Hecke.H2KaehlerDegrees`, the other
  prune.)
* `interleaved_ne_sequential` — **the interleaved half.** Whenever the cross term is non-zero
  (at convention D it is `−(q⁴+q²+1)/(q²+1)²`, never zero for real `q > 0`,
  `InterleavedCrossTerm.crossTerm_neg_convD`), the interleaved word's trace is **not** the
  sequential one, so its `log` is **not** the bond sum of the same letters. That is the exact
  sense in which the corpus's one positive many-body signal (`qou-kru4`) is the failure of F1's
  ordering hypothesis and not a counterexample to F1.

## What this settles for the derived route

F1 has two hypotheses — a trace that is Markov, and a word that is monotone — and the corpus
now shows in Lean that the second is the one the production chain satisfies and the interleaved
class violates. So a many-body term at **degree zero** must come from word topology; a many-body
term from the **algebra** must come from a place the Markov trace on the semisimple fibre cannot
see, which is `H2KaehlerDegrees`' subject. Nothing here moves a number.

Ground ring generic `[CommRing R]`, `[CommRing S]` (§7c). Bean `qou-onte` §7 item 1.
-/

namespace QOU.Mass.FormalityBridgeF1

open QOU.MathlibExt.OcneanuTrace
open QOU.MathlibExt.MonotoneWordFactorizes
open QOU.MathlibExt.InterleavedCrossTerm
open QOU.Mass.MarkovBondRuleForcesPairwise

variable {R : Type*} [CommRing R] {S : Type*} [CommRing S]

/-- A multiplicative-to-additive map sends `1` to `0`. -/
theorem additive_map_one {f : R → S} (hf : IsAdditiveOnProducts f) : f 1 = 0 := by
  have h := hf 1 1
  rw [one_mul] at h
  have h2 : f 1 + f 1 = f 1 + 0 := by rw [add_zero]; exact h.symm
  exact add_left_cancel h2

/-- A multiplicative-to-additive map turns a finite product into a finite sum. -/
theorem additive_map_prod {f : R → S} (hf : IsAdditiveOnProducts f)
    {ι : Type*} (s : Finset ι) (g : ι → R) :
    f (∏ i ∈ s, g i) = ∑ i ∈ s, f (g i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [additive_map_one hf]
  | @insert a s ha ih => rw [Finset.prod_insert ha, Finset.sum_insert ha, hf, ih]

variable {A : Type*} [Ring A] [Algebra R A] (T : MarkovTrace R A)

/-- **F1, sequential half.** For a monotone word of stabilising letters and any map `f` with
`f (x·y) = f x + f y`, `f (tr word)` is the sum of the letters' `f`-images: `log tr` of a
sequential word is a bond sum. Combined with
`MarkovBondRuleForcesPairwise.b3_eq_zero_of_bondRule`, every connected cumulant above two of
such a binding vanishes. -/
theorem f_tr_stabWord_eq_sum {f : R → S} (hf : IsAdditiveOnProducts f)
    (s : ℕ → A) (c : ℕ → R) (hs : ∀ m, s m ∈ T.H (m + 1))
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c m * T.tr a) (n k : ℕ) :
    f (T.tr (stabWord s n k)) = ∑ i ∈ Finset.range k, f (T.tr (s (n + i))) := by
  rw [tr_stabWord_eq_prod_tr T s c hs hstab n k, additive_map_prod hf]

/-- **F1, interleaved half.** With a non-zero cross term, the interleaved word `g₀ g₁ g₀ g₂ g₁`
does not have the trace of the sequential word `g₀² g₁² g₂` with the same letter content — so
its `log` is not that bond sum. The corpus's `n = 4` many-body signal is the failure of F1's
ordering hypothesis, not a counterexample to F1. -/
theorem interleaved_ne_sequential (h : R) (hq : ∀ m, T.g m * T.g m = h • T.g m + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1)
    (hz : T.z * (T.z ^ 2 - h * T.z - 1) ≠ 0) :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1)
      ≠ T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2) := by
  intro heq
  have hd := interleaved_sub_sequential T h (hq 0) (hq 1) hbraid
  rw [heq, sub_self] at hd
  exact hz hd.symm

omit [CommRing S] in
/-- **The same statement through `f`.** If `f` is injective on the two traces (in particular for
`log` on positive reals), the interleaved word's `f`-value differs from the sequential bond sum.
Stated with an explicit injectivity hypothesis rather than a logarithm, per §7c. -/
theorem f_interleaved_ne_f_sequential {f : R → S} (hinj : Function.Injective f)
    (h : R) (hq : ∀ m, T.g m * T.g m = h • T.g m + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1)
    (hz : T.z * (T.z ^ 2 - h * T.z - 1) ≠ 0) :
    f (T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1))
      ≠ f (T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2)) :=
  fun heq => interleaved_ne_sequential T h hq hbraid hz (hinj heq)


/-- **Powers and 3-factor products under a multiplicative-to-additive map (`qou-2akx`).**
For any `hf : IsAdditiveOnProducts f`, `f (x ^ n) = n • f x`, and on a 3-factor product
`f (x * y * z) = f x + f y + f z`. -/
theorem additive_map_pow_and_mul_three {f : R → S} (hf : IsAdditiveOnProducts f)
    (x y z : R) (n : ℕ) :
    f (x ^ n) = n • f x ∧ f (x * y * z) = f x + f y + f z := by
  refine ⟨?_, by rw [hf (x * y) z, hf x y]⟩
  induction n with
  | zero => simp [additive_map_one hf]
  | succ k ih => rw [pow_succ, hf, ih, succ_nsmul]

end QOU.Mass.FormalityBridgeF1
