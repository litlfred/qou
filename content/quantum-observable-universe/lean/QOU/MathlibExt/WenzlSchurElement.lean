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
      acc + (List.range ((lam[i]?).getD 0)).foldl
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
        acc * (List.range ((lam[i]?).getD 0)).foldl
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
every $s_{\lambda}$ is nonzero (Geck--Pfeiffer [geckpfeiffer2000] Thm 7.2.6).
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
generic-parameter statement; the $X = Q^{-N}$ stratification is
proved below (`schurElement_tl_eq_zero_iff`) — it is no longer
outstanding work. -/

/-- In-range cells have positive hook length (sorry-free). -/
theorem hookLength_pos {lam : Partition} {i j : ℕ}
    (hj : j < (lam[i]?).getD 0) :
    0 < Partition.hookLength lam i j := by
  unfold Partition.hookLength
  cases h : lam[i]? with
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
    instance would launder [geckpfeiffer2000] into a Lean proof.

    Ref: [geckpfeiffer2000] Geck--Pfeiffer, Thm 7.2.6. -/
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

/-! ## The Temperley–Lieb stratification at the physical parameter
     $X = Q^{-N}$ (companion to the $X \leq 0$ regime bound)

At the physical Markov specialisation $X = Q^{-N}$ the content
numerator $1 - Q^{-N} Q^{c(x)}$ vanishes **exactly** at cells of
content $c(x) = N$.  So the vanishing locus of the Schur element is
precisely the set of partitions containing a content-$N$ cell — the
Temperley--Lieb / level-rank quotient stratification, proved here as
a sorry-free iff on the concrete `schurElement`.  Vanishing Schur
elements are the *structure* at physical $X$, not a defect: they cut
out the quotient category.

**⚠ Convention: this gives COLUMNS, and a corpus block says rows.**
With `cellContent i j = j - i` and rows/columns 0-indexed, a partition
has a content-`N` cell (for `N ≥ 0`) exactly when `N < λ₁`, so the
blocks that *survive* at `X = Q^{-N}` are those with **at most `N`
columns**.  The textbook `GL(N)` / HOMFLY statement is the transpose —
quantum dimension `∏ [N + c(x)]/[h(x)]` vanishes at `c(x) = -N`, i.e.
at `X = Q^{+N}`, giving at most `N` **rows**.  So this file uses the
*conjugate* convention.

That collides with `mass-theory/hecke-radical-is-temperley-lieb.md`,
which states the survivors are the **two-row** shapes `(n-k,k)` and
tabulates them for `n = 2..7`.  The Catalan dimension counts there are
unaffected (`dim λ = dim λ'`), so nothing numerical is wrong — but the
two blocks label *different sets of partitions* as the TL quotient.
**Anyone wiring `schurElement_tl_eq_zero_iff` to that block must
transpose.**  The `N < 0` mirror gives the textbook row form directly.

Both forms are proved in `QOU.MathlibExt.TLContentStratification`,
which eliminates the existential in `HasContentCell` and replaces it
with a one-line shape statistic: at `X = Q^{-N}`, `N ≥ 0`, a block
survives iff `λ₁ ≤ N` (`schurElement_tl_ne_zero_iff_numCols_le`);
the `N < 0` mirror is `ℓ(λ) ≤ -N`
(`schurElement_tl_ne_zero_iff_length_le`). -/

/-- `lam` contains an in-range cell of content `N`. -/
def HasContentCell (lam : Partition) (N : ℤ) : Prop :=
  ∃ i, i < lam.length ∧ ∃ j, j < (lam[i]?).getD 0 ∧ cellContent i j = N

private theorem foldl_mul_div_eq_zero (f g : ℕ → ℝ) :
    ∀ l : List ℕ, l.foldl (fun a j => a * f j / g j) 0 = 0
  | [] => rfl
  | j :: tl => by
      simp only [List.foldl_cons, zero_mul, zero_div]
      exact foldl_mul_div_eq_zero f g tl

private theorem foldl_mul_div_eq_zero_of_mem (f g : ℕ → ℝ) {j₀ : ℕ} :
    ∀ (l : List ℕ) (c : ℝ), j₀ ∈ l → f j₀ = 0 →
      l.foldl (fun a j => a * f j / g j) c = 0
  | [], _, h, _ => absurd h (by simp)
  | j :: tl, c, hmem, hf => by
      simp only [List.foldl_cons]
      rcases List.mem_cons.mp hmem with h | h
      · subst h
        rw [hf, mul_zero, zero_div]
        exact foldl_mul_div_eq_zero f g tl
      · exact foldl_mul_div_eq_zero_of_mem f g tl _ h hf

private theorem foldl_mul_eq_zero (F : ℕ → ℝ) :
    ∀ l : List ℕ, l.foldl (fun a i => a * F i) 0 = 0
  | [] => rfl
  | i :: tl => by
      simp only [List.foldl_cons, zero_mul]
      exact foldl_mul_eq_zero F tl

private theorem foldl_mul_eq_zero_of_mem (F : ℕ → ℝ) {i₀ : ℕ} :
    ∀ (l : List ℕ) (c : ℝ), i₀ ∈ l → F i₀ = 0 →
      l.foldl (fun a i => a * F i) c = 0
  | [], _, h, _ => absurd h (by simp)
  | i :: tl, c, hmem, hF => by
      simp only [List.foldl_cons]
      rcases List.mem_cons.mp hmem with h | h
      · subst h
        rw [hF, mul_zero]
        exact foldl_mul_eq_zero F tl
      · exact foldl_mul_eq_zero_of_mem F tl _ h hF

/-- At $X = Q^{-N}$ the content numerator vanishes exactly at content
    $c = N$ (sorry-free): $1 - Q^{-N} Q^{c} = 0 \iff c = N$. -/
theorem tl_numerator_eq_zero_iff {Q : ℝ} (hQ : 1 < Q) (N c : ℤ) :
    1 - Q ^ (-N) * Q ^ c = 0 ↔ c = N := by
  have hQ0 : (0 : ℝ) < Q := lt_trans one_pos hQ
  rw [← zpow_add₀ (ne_of_gt hQ0)]
  constructor
  · intro h
    have h1 : Q ^ (-N + c) = 1 := by linarith
    have h2 : -N + c = 0 :=
      (zpow_eq_one_iff_right₀ hQ0.le (ne_of_gt hQ)).mp h1
    omega
  · intro h
    subst h
    simp

/-- **TL vanishing (sorry-free).**  A content-$N$ cell kills the Schur
    element at $X = Q^{-N}$. -/
theorem schurElement_tl_eq_zero {Q : ℝ} (hQ : 1 < Q) {N : ℤ}
    {lam : Partition} (h : HasContentCell lam N) :
    schurElement Q (Q ^ (-N)) lam = 0 := by
  obtain ⟨i, hi, j, hj, hc⟩ := h
  have hQ0 : (0 : ℝ) < Q := lt_trans one_pos hQ
  unfold schurElement
  rw [mul_eq_zero]
  right
  refine foldl_mul_eq_zero_of_mem _ _ _ (List.mem_range.mpr hi) ?_
  refine foldl_mul_div_eq_zero_of_mem _ _ _ _ (List.mem_range.mpr hj) ?_
  rw [hc, ← zpow_add₀ (ne_of_gt hQ0)]
  simp

/-- **TL non-vanishing (sorry-free).**  With no content-$N$ cell, the
    Schur element at $X = Q^{-N}$ survives. -/
theorem schurElement_tl_ne_zero {Q : ℝ} (hQ : 1 < Q) {N : ℤ}
    {lam : Partition} (h : ¬HasContentCell lam N) :
    schurElement Q (Q ^ (-N)) lam ≠ 0 := by
  have hQ0 : (0 : ℝ) < Q := lt_trans one_pos hQ
  unfold schurElement
  refine mul_ne_zero (zpow_ne_zero _ (ne_of_gt hQ0)) ?_
  refine foldl_mul_ne_zero _ _ _ one_ne_zero ?_
  intro i hi
  refine foldl_mul_div_ne_zero _ _ _ _ one_ne_zero ?_ ?_
  · intro j hj
    intro heq
    exact h ⟨i, List.mem_range.mp hi, j, List.mem_range.mp hj,
      (tl_numerator_eq_zero_iff hQ N _).mp heq⟩
  · intro j hj
    exact one_sub_pow_ne_zero_of_one_lt hQ
      (hookLength_pos (List.mem_range.mp hj)).ne'

/-- **The Temperley--Lieb stratification (sorry-free iff).**  At the
    physical Markov parameter $X = Q^{-N}$, $Q > 1$, the Schur element
    of $\lambda$ vanishes **iff** $\lambda$ contains a cell of content
    $N$.  Combined with the cited `SchurElementCriterion`, this locates
    the semisimplicity boundary exactly: the level-rank / TL quotient
    is cut out by the content-$N$ hyperplane of the cell lattice. -/
theorem schurElement_tl_eq_zero_iff {Q : ℝ} (hQ : 1 < Q) (N : ℤ)
    (lam : Partition) :
    schurElement Q (Q ^ (-N)) lam = 0 ↔ HasContentCell lam N := by
  constructor
  · intro h
    by_contra hn
    exact schurElement_tl_ne_zero hQ hn h
  · exact schurElement_tl_eq_zero hQ

/-- **The substrate regime lies strictly outside the TL degeneracy
    locus (sorry-free).**  Every Temperley--Lieb wall sits at a
    *positive* Markov parameter $X = Q^{-N}$ (since $Q > 1 \Rightarrow
    Q^{-N} > 0$), whereas the physical substrate regime is $X \le 0$.
    Hence at the substrate no content level $N$ can place $X$ on a wall:
    $X \ne Q^{-N}$ for every $N$.  This is the structural reason
    `schurElement_ne_zero` holds for *all* $\lambda$ at $X \le 0$ — the
    vanishing criterion `schurElement_tl_eq_zero_iff` can never fire, so
    the substrate sits in the semisimple stratum away from every
    level-rank wall. -/
theorem substrate_avoids_tl_locus {Q X : ℝ} (hQ : 1 < Q) (hX : X ≤ 0)
    (N : ℤ) : X ≠ Q ^ (-N) := by
  have hpos : (0 : ℝ) < Q ^ (-N) := zpow_pos (lt_trans one_pos hQ) _
  exact fun h => absurd (h ▸ hX) (not_le.mpr hpos)

/-- **The substrate never lands on a TL wall of any partition
    (sorry-free).**  Packaging `substrate_avoids_tl_locus` against
    `schurElement_tl_eq_zero_iff`: for $Q > 1$, $X \le 0$ and any
    $\lambda$, if the level-$N$ vanishing criterion held then $X$ would
    equal the positive wall $Q^{-N}$, contradicting $X \le 0$.  So no
    content level can degenerate the Schur element at the substrate —
    the semisimple-stratum reason behind `schurElement_ne_zero`. -/
theorem substrate_not_tl_degenerate {Q X : ℝ} (hQ : 1 < Q) (hX : X ≤ 0)
    {N : ℤ} {lam : Partition} (hdeg : X = Q ^ (-N) ∧ HasContentCell lam N) :
    False :=
  substrate_avoids_tl_locus hQ hX N hdeg.1

end QOU.MathlibExt.WenzlSchurElement
