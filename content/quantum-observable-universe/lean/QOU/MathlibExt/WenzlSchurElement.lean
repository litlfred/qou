import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.MathlibExt.WenzlSchurElement
  — Wenzl Schur element and Jones-Markov closed form

The **Wenzl Schur element** at partition `λ ⊢ n` is the
combinatorial coefficient

    s_{λ, X}(Q) = Q^{n(λ)} · ∏_{x ∈ λ} (1 − X · Q^{c(x)}) / (1 − Q^{h(x)}),

where `n(λ) = Σ_x c(x)` (the content sum), `c(x) = j − i` is the
content of cell `(i, j)`, and `h(x)` is the hook length.

The **Jones-Markov coefficient** `y_λ(q)` is the canonical scaling

    y_λ(q) = s_{λ, X}(Q) / Z_n(Q, X)

with `Z_n(Q, X) = Σ_{λ ⊢ n} f_λ · s_{λ, X}(Q)` the Wenzl-bridge
normalisation.  Per `prop:macdonald-hook-telescope`,
`Z_n = ((1 − X) / (1 − Q))^n`, giving the closed form

    y_λ(q) = Q^{n(λ)} · (1 − Q)^n / (1 − X)^n
              · ∏_{x ∈ λ} (1 − X · Q^{c(x)}) / (1 − Q^{h(x)}).

Refs:
- [wenzl1988] Hecke algebras of type A_n and subfactors,
  Invent. Math. 92 (1988).
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.3.
- [stanley1999] Enumerative Combinatorics II, Cor. 7.12.5.
-/

namespace QOU.MathlibExt.WenzlSchurElement

open QOU.MathlibExt.QPartitionCombinatorics

/-! ## Content of a partition cell -/

/-- Per-cell content `c(i, j) = j − i` for cell `(i, j)`. -/
def cellContent (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- The **content sum** `n(λ) = Σ_x c(x)` for partition `λ`.

    Iterates over rows `i ∈ [0, length λ)` and within each row over
    columns `j ∈ [0, λ_i)`, summing `cellContent i j`. -/
def contentSum (lam : Partition) : ℤ :=
  (List.range lam.length).foldl
    (fun acc i =>
      acc + (List.range ((lam.get? i).getD 0)).foldl
        (fun a j => a + cellContent i j)
        0)
    0

@[simp]
theorem contentSum_nil : contentSum [] = 0 := by
  unfold contentSum
  simp

/-! ## Wenzl Schur element — abstract structure

We axiomatise the Schur element since the concrete product over
cells is a substantial Finset computation; the structural API
suffices for the macdonald hook telescope identity. -/

/-- The **Wenzl Schur element** `s_{λ, X}(Q)` at partition `λ`.

    Encodes `Q^{n(λ)} · ∏_x (1 − X·Q^{c(x)})/(1 − Q^{h(x)})`.
    Abstracted here pending the symmetric-functions / Schur-element
    infrastructure in Mathlib (this is a known gap). -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see content/bib-qa-verifications.json
-- Ref: [macdonald1995] §I.3 ex. 1
noncomputable def schurElement (Q X : ℝ) (lam : Partition) : ℝ :=
  Q ^ (contentSum lam) *
    (List.range lam.length).foldl
      (fun acc i =>
        acc * (List.range ((lam.get? i).getD 0)).foldl
          (fun a j =>
            a * (1 - X * Q ^ (cellContent i j)) /
                (1 - Q ^ (Partition.hookLength lam i j)))
          1)
      1

@[simp]
theorem schurElement_nil (Q X : ℝ) : schurElement Q X [] = Q ^ 0 * 1 := by
  unfold schurElement
  simp

/-! ## Wenzl-bridge normalisation Z_n

By definition `Z_n(Q, X) = Σ_{λ ⊢ n} f_λ · s_{λ, X}(Q)`, where
`f_λ` is the number of standard Young tableaux of shape `λ`.

Per the **Macdonald hook telescope**
(`macdonald-hook-telescope.lean`), this sum equals
`((1 − X) / (1 − Q))^n`.

We abstract `Z_n` rather than constructing the full SYT sum here
since the SYT count `f_λ` is itself a deep Mathlib gap. -/

/-- The **Wenzl-bridge normalisation** `Z_n(Q, X)`. -/
-- Ref: [stanley1999] EC2 Cor. 7.12.5 (regular-rep Frobenius identity)
-- Ref: [macdonald1995] §I.3 ex. 1 (principal specialisation)
noncomputable def wenzlNormalisation (n : ℕ) (Q X : ℝ) : ℝ :=
  ((1 - X) / (1 - Q)) ^ n

/-! ## Jones-Markov closed form -/

/-- The **Jones-Markov coefficient** `y_λ(q) = s_{λ, X}(Q) / Z_n(Q, X)`.

    Combined with the Macdonald-hook telescope `Z_n = ((1−X)/(1−Q))^n`,
    this collapses to

      y_λ = Q^{n(λ)} · (1 − Q)^n / (1 − X)^n
              · ∏_x (1 − X·Q^{c(x)}) / (1 − Q^{h(x)}). -/
-- Ref: [wenzl1988] Theorem 2.1
noncomputable def jonesMarkovCoeff (Q X : ℝ) (lam : Partition) : ℝ :=
  schurElement Q X lam / wenzlNormalisation lam.size Q X

/-- **Connection theorem** — y_λ is well-defined for `Q ≠ 1`,
    `X ≠ 1`, since the denominator `Z_n = ((1−X)/(1−Q))^n` is then
    nonzero. -/
-- Ref: [wenzl1988] Theorem 2.1
theorem wenzlNormalisation_ne_zero {n : ℕ} {Q X : ℝ}
    (hQ : Q ≠ 1) (hX : X ≠ 1) :
    wenzlNormalisation n Q X ≠ 0 := by
  unfold wenzlNormalisation
  have h_num_ne : (1 - X) ≠ 0 := by
    intro h
    apply hX
    linarith
  have h_denom_ne : (1 - Q) ≠ 0 := by
    intro h
    apply hQ
    linarith
  have h_ratio_ne : (1 - X) / (1 - Q) ≠ 0 :=
    div_ne_zero h_num_ne h_denom_ne
  exact pow_ne_zero n h_ratio_ne

/-! ## Schur-element non-vanishing at the substrate regime
     (Wenzl-bridge stage 2, bean `qou-vndn`)

Semisimplicity of $H_n(q)$ with Markov parameter $X$ is governed by the
Schur elements of the symmetrizing trace: the algebra is semisimple iff
every $s_{\lambda}$ is nonzero (Geck--Pfeiffer [geck2000] Thm 7.2.6).
Here we prove — **sorry-free, on the concrete `schurElement` above** —
that in the substrate regime $Q > 1$, $X \leq 0$ every Schur element is
nonzero, carry the Geck--Pfeiffer criterion as a cited hypothesis class
(`SchurElementCriterion`, no instance — the symmetrizing-trace theory
is not in Mathlib), and compose: semisimplicity at every rank.

**Scope note (honest regime bound).**  Physical Markov specialisations
use $X > 0$ (e.g. $X = Q^{-N}$), where the numerator factors
$1 - X\,Q^{c(x)}$ genuinely vanish at cells of content $c = N$ — that
vanishing locus *is* the Temperley--Lieb / level-rank quotient
structure, not a defect.  The $X \leq 0$ bound proves the
generic-parameter statement; the $X = Q^{-N}$ stratification is a
follow-on with real combinatorial content. -/

/-- In-range cells have positive hook length (sorry-free). -/
theorem hookLength_pos {lam : Partition} {i j : ℕ}
    (hj : j < (lam.get? i).getD 0) :
    0 < Partition.hookLength lam i j := by
  unfold Partition.hookLength
  cases h : lam.get? i with
  | none => rw [h] at hj; simp at hj
  | some row =>
      rw [h] at hj
      simp only [Option.getD_some] at hj
      simp [hj]

private theorem foldl_mul_div_ne_zero (f g : ℕ → ℝ) :
    ∀ (l : List ℕ) (c : ℝ), c ≠ 0 → (∀ j ∈ l, f j ≠ 0) → (∀ j ∈ l, g j ≠ 0) →
      l.foldl (fun a j => a * f j / g j) c ≠ 0
  | [], _, hc, _, _ => hc
  | j :: tl, c, hc, hf, hg => by
      simp only [List.foldl_cons]
      exact foldl_mul_div_ne_zero f g tl _
        (div_ne_zero (mul_ne_zero hc (hf j (by simp))) (hg j (by simp)))
        (fun x hx => hf x (by simp [hx]))
        (fun x hx => hg x (by simp [hx]))

private theorem foldl_mul_ne_zero (F : ℕ → ℝ) :
    ∀ (l : List ℕ) (c : ℝ), c ≠ 0 → (∀ i ∈ l, F i ≠ 0) →
      l.foldl (fun a i => a * F i) c ≠ 0
  | [], _, hc, _ => hc
  | i :: tl, c, hc, hF => by
      simp only [List.foldl_cons]
      exact foldl_mul_ne_zero F tl _
        (mul_ne_zero hc (hF i (by simp)))
        (fun x hx => hF x (by simp [hx]))

/-- For $Q > 1$ the hook denominator $1 - Q^{h}$ is nonzero at every
    positive hook length (sorry-free). -/
theorem one_sub_pow_ne_zero_of_one_lt {Q : ℝ} (hQ : 1 < Q) {h : ℕ}
    (hh : h ≠ 0) : 1 - Q ^ h ≠ 0 :=
  ne_of_lt (by have := one_lt_pow₀ hQ hh; linarith)

/-- For $Q > 0$, $X \leq 0$ the content numerator $1 - X\,Q^{c}$ is
    nonzero (indeed positive) at every content $c \in \mathbb{Z}$
    (sorry-free). -/
theorem one_sub_mul_zpow_ne_zero {Q X : ℝ} (hQ : 0 < Q) (hX : X ≤ 0)
    (c : ℤ) : 1 - X * Q ^ c ≠ 0 := by
  have hz : (0 : ℝ) < Q ^ c := zpow_pos hQ c
  have h1 : 0 ≤ -(X * Q ^ c) := by
    rw [← neg_mul]
    exact mul_nonneg (neg_nonneg.mpr hX) hz.le
  refine ne_of_gt ?_
  linarith

/-- **Schur-element non-vanishing at the substrate regime
    (sorry-free).**  For $Q > 1$ and $X \leq 0$, every Wenzl Schur
    element is nonzero: every content numerator is positive, every hook
    denominator is strictly negative (hook lengths are positive), and
    the prefactor $Q^{n(\lambda)}$ is a nonzero power of a positive
    real.  This is the computational heart of Wenzl semisimplicity,
    proved on the concrete `schurElement`. -/
theorem schurElement_ne_zero {Q X : ℝ} (hQ : 1 < Q) (hX : X ≤ 0)
    (lam : Partition) : schurElement Q X lam ≠ 0 := by
  have hQ0 : (0 : ℝ) < Q := lt_trans one_pos hQ
  unfold schurElement
  refine mul_ne_zero (zpow_ne_zero _ (ne_of_gt hQ0)) ?_
  refine foldl_mul_ne_zero _ _ _ one_ne_zero ?_
  intro i _
  refine foldl_mul_div_ne_zero _ _ _ _ one_ne_zero ?_ ?_
  · intro j _
    exact one_sub_mul_zpow_ne_zero hQ0 hX _
  · intro j hj
    exact one_sub_pow_ne_zero_of_one_lt hQ
      (hookLength_pos (List.mem_range.mp hj)).ne'

/-- **Cited Geck--Pfeiffer criterion** (hypothesis class, not a theorem
    of this development): if every Schur element at rank $n$ is
    nonzero, the algebra is semisimple at rank $n$.  `semisimple n` is
    an opaque per-rank `Prop`; **no instance is declared** — the
    symmetrizing-trace theory is not in Mathlib, and a fabricated
    instance would launder [geck2000] into a Lean proof.

    Ref: [geck2000] Geck--Pfeiffer, Thm 7.2.6. -/
class SchurElementCriterion (Q X : ℝ) (semisimple : ℕ → Prop) : Prop where
  /-- Schur-element non-vanishing implies semisimplicity, carried as a
      hypothesis. -/
  semisimple_of_schur_ne_zero :
    ∀ n : ℕ,
      (∀ lam : Partition, lam.size = n → schurElement Q X lam ≠ 0) →
      semisimple n

/-- **Semisimplicity at every rank in the substrate regime (sorry-free
    modulo the cited criterion).**  For $Q > 1$, $X \leq 0$: every rank
    is semisimple, with the Schur-element leg *computed*, not assumed.
    This is the Schur-theoretic discharge of the `WenzlCriterion`
    hypothesis of `QOU.Information.PNeqNpEquivalence` — the two cited
    classes state the same literature theorem from two equivalent
    angles (parameter genericity vs. Schur-element non-vanishing). -/
theorem semisimple_of_substrate {Q X : ℝ} {ss : ℕ → Prop}
    [C : SchurElementCriterion Q X ss] (hQ : 1 < Q) (hX : X ≤ 0)
    (n : ℕ) : ss n :=
  C.semisimple_of_schur_ne_zero n fun lam _ => schurElement_ne_zero hQ hX lam

end QOU.MathlibExt.WenzlSchurElement
