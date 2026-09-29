import Mathlib.Tactic

/-!
# QOU.Common.AntiInvolutionPalindrome — palindromy & first-moment vanishing

The general algebra behind two of the content-monomial separation facts
(`computations/lever1_content_monomial_separation.py`, lever-1 W12): the
content-only binding object

  `C_n(q) = Σ_{λ⊢n} f^λ · q^{content(λ)}`

is (P2) **palindromic** `C_n(q) = C_n(q⁻¹)` and (P4) its deviation from the
classical value is **bar-even `O((q−1)²)`** — the same q-rigidity the level-1/2
alien datum `Δ_{ω₀}` measured (bar-even, `O((q−1)²)`; the W5 bridge datum,
`lever1-bridge-alien-datum.witness.json`). Both are instances of a single
abstract fact, proved here **generally and sorry-free**: a weighted exponential
sum over a finite set carrying an **anti-invariant involution** is palindromic,
and its **first moment vanishes**.

The anti-invariant involution for `C_n` is partition conjugation `λ ↦ λ'`:
`f^{λ'} = f^λ` (weight invariant) and `content(λ') = −content(λ)` (exponent
anti-invariant). Feeding those two facts into the abstract lemmas gives P2 and
P4 for every `n` at once — no `decide`, no RSK. The first-moment lemma is the
exact algebraic form of "`P'(1) = 0`", i.e. the bar-even `O((q−1)²)` alien
rigidity: the linear term of the q-deformation is forced to vanish.

Ground ring: `Field K` with `q ≠ 0` for the palindromy (the exponent is a `ℤ`
power, `q⁻¹` is algebraic — §7c wall-safe); the first-moment identity is `ℤ`-valued.
-/

namespace QOU.AntiInvolutionPalindrome

open Finset

variable {ι : Type*}

/-- **Palindromy from an anti-invariant involution.** If `σ` is an involution of
the finite set `s`, the weight `w` is `σ`-invariant, and the exponent `e` is
`σ`-anti-invariant (`e (σ i) = − e i`), then the weighted exponential sum is
invariant under `q ↦ q⁻¹`:
`Σ_{i∈s} w i · q^{e i} = Σ_{i∈s} w i · q^{−e i}`. -/
theorem palindromic_sum_of_antiInvolution
    {K : Type*} [Field K] (q : K) (_hq : q ≠ 0)
    (s : Finset ι) (σ : ι → ι) (w : ι → ℕ) (e : ι → ℤ)
    (hmaps : ∀ i ∈ s, σ i ∈ s)
    (hinv : ∀ i ∈ s, σ (σ i) = i)
    (hw : ∀ i ∈ s, w (σ i) = w i)
    (he : ∀ i ∈ s, e (σ i) = - e i) :
    ∑ i ∈ s, (w i : K) * q ^ (e i) = ∑ i ∈ s, (w i : K) * q ^ (-(e i)) := by
  refine Finset.sum_nbij' (fun i => σ i) (fun i => σ i) hmaps hmaps hinv hinv ?_
  intro i hi
  rw [hw i hi, he i hi, neg_neg]

/-- **First moment vanishes** — the algebraic form of `P'(1) = 0`, i.e. the
bar-even `O((q−1)²)` rigidity: the derivative of `Σ w i · q^{e i}` at `q = 1` is
`Σ w i · e i`, and under the same anti-invariant involution this is `0`, so the
q-deformation of the weighted sum has no linear term (its deviation from the
`q = 1` value starts at second order). This is the exact statement the level-1/2
alien datum `Δ_{ω₀}` measured as its bar-even q-rigidity. -/
theorem first_moment_zero_of_antiInvolution
    (s : Finset ι) (σ : ι → ι) (w : ι → ℕ) (e : ι → ℤ)
    (hmaps : ∀ i ∈ s, σ i ∈ s)
    (hinv : ∀ i ∈ s, σ (σ i) = i)
    (hw : ∀ i ∈ s, w (σ i) = w i)
    (he : ∀ i ∈ s, e (σ i) = - e i) :
    ∑ i ∈ s, (w i : ℤ) * e i = 0 := by
  have hreidx : ∑ i ∈ s, (w i : ℤ) * e i
      = ∑ i ∈ s, (w (σ i) : ℤ) * e (σ i) :=
    Finset.sum_nbij' (fun i => σ i) (fun i => σ i) hmaps hmaps hinv hinv
      (fun a ha => by rw [hinv a ha])
  have key : ∑ i ∈ s, (w i : ℤ) * e i + ∑ i ∈ s, (w i : ℤ) * e i = 0 := by
    nth_rewrite 1 [hreidx]
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_eq_zero fun i hi => ?_
    rw [hw i hi, he i hi]
    ring
  omega

end QOU.AntiInvolutionPalindrome
