import Mathlib.Data.List.Basic
import Mathlib.Tactic

/-!
# QOU.OptimalNF.optimal_nf_is_standard_basis — optimal `A`-term normal form

After quotienting the raw Gröbner–Shirshov normal form by the adjacency /
chain-collapse ideals `I₈ + I₉`, the normal form for any nucleus `N(Z, N)`
in the valley of stability (`N ≥ Z - 1`, `A = Z + N ≥ 2`) has **exactly**
`A = Z + N` terms:

```
  standardBasis (Z + N - 1) = { [], [0], [1], …, [A - 2] }
```

Every word in `standardBasis (Z + N - 1)` is non-absorbable under `I₈ + I₉`,
and in any prefix-closed support whose generators are bounded by `A - 1`,
every word that survives `I₉`-absorption lies in `standardBasis (Z + N - 1)`.

Mirrors the library formalisation in `QOU/Archimedean/OptimalNF.lean` so
that `qou:QOU.OptimalNF.optimal_nf_is_standard_basis` resolves to the same
substantive normal-form theorem in both the chapter sibling and the library
(bean `qou-shdw`).

LaTeX label: `thm:optimal-normal-form-valley`

## References
- [leitner2026] §13/optimal-normal-form-valley
- [unital-groebner-bases] main theorem (division algorithm)
-/

namespace QOU.OptimalNF

/-- Mass number `A = Z + N`. -/
def massNumber (Z N : ℕ) : ℕ := Z + N

/-- The valley-of-stability condition `N ≥ Z - 1`. -/
def inValley (Z N : ℕ) : Prop := N + 1 ≥ Z

/-- A Hecke generator word in `H_A(q)`, represented by its list of generator indices. -/
abbrev HeckeWord := List ℕ

/-- The standard basis `{ [], [0], [1], …, [n - 1] }` of length `n + 1`. -/
def standardBasis (n : ℕ) : List HeckeWord :=
  [[]] ++ (List.range n).map (fun i => [i])

-- Ref: [leitner2026]
theorem standardBasis_length (n : ℕ) :
    (standardBasis n).length = n + 1 := by
  simp [standardBasis]

-- Ref: [leitner2026]
theorem nil_mem_standardBasis (n : ℕ) :
    ([] : HeckeWord) ∈ standardBasis n := by
  simp [standardBasis]

-- Ref: [leitner2026]
theorem singleton_mem_standardBasis (n i : ℕ) (h : i < n) :
    [i] ∈ standardBasis n := by
  simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
             List.mem_range]
  right; exact ⟨i, h, rfl⟩

/-- Adjacent-pair ideal `I₈`: `[i, i + 1]` is absorbed when `[i + 1]` is in the support. -/
def IsI8Absorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  ∃ i : ℕ, w = [i, i + 1] ∧ [i + 1] ∈ support

/-- Chain-collapse ideal `I₉`: a word of length `≥ 2` is absorbed when its prefix `w.dropLast`
    is in the support. -/
def IsI9Absorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  w.length ≥ 2 ∧ w.dropLast ∈ support

/-- Combined `I₈ + I₉` absorption predicate. -/
def IsAbsorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  IsI8Absorbable support w ∨ IsI9Absorbable support w

/-- Prefix-closure of a support set of Hecke words. -/
def IsPrefixClosed (support : List HeckeWord) : Prop :=
  ∀ w ∈ support, w.length ≥ 2 → w.dropLast ∈ support

-- Ref: [leitner2026]
theorem standardBasis_not_absorbable (n : ℕ) (w : HeckeWord)
    (hw : w ∈ standardBasis n) :
    ¬ IsAbsorbable (standardBasis n) w := by
  simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
             List.mem_range] at hw
  rcases hw with rfl | ⟨i, _, rfl⟩
  · rintro (⟨j, h, -⟩ | ⟨h, -⟩) <;> simp at h
  · rintro (⟨j, h, -⟩ | ⟨h, -⟩) <;> simp at h

-- Ref: [leitner2026]
theorem optimal_from_prefix_closed (n : ℕ) (support : List HeckeWord)
    (h_closed : IsPrefixClosed support)
    (h_bounded : ∀ w ∈ support, ∀ g ∈ w, g < n) :
    ∀ w ∈ support, ¬ IsI9Absorbable support w →
    w ∈ standardBasis n := by
  intro w hw h_not_i9
  have h_short : w.length ≤ 1 := by
    by_contra h_len
    push_neg at h_len
    exact h_not_i9 ⟨by omega, h_closed w hw (by omega)⟩
  match w, h_short with
  | [], _ => exact nil_mem_standardBasis n
  | [i], _ =>
    exact singleton_mem_standardBasis n i (h_bounded [i] hw i (by simp))
  | _ :: _ :: _, h => simp at h

/-- **Optimal Normal Form theorem.**  For any nucleus `N(Z, N)` in the valley
    of stability (`inValley Z N`, `Z + N ≥ 2`), the `I₈ + I₉`-reduced
    standard basis `standardBasis (Z + N - 1)` has exact cardinality
    `massNumber Z N = Z + N` with `2 * Z ≤ massNumber Z N + 1`, none of its
    elements is `I₈ + I₉`-absorbable, and in every prefix-closed support
    whose generators are bounded by `Z + N - 1`, every `I₉`-unabsorbable
    word belongs to `standardBasis (Z + N - 1)`. -/
-- Ref: [unital-groebner-bases:thm:ugb-main-theorem]
theorem optimal_nf_is_standard_basis (Z N : ℕ)
    (hval : inValley Z N) (h_pos : Z + N ≥ 2) :
    (standardBasis (Z + N - 1)).length = massNumber Z N ∧
    2 * Z ≤ massNumber Z N + 1 ∧
    (∀ w ∈ standardBasis (Z + N - 1), ¬ IsAbsorbable (standardBasis (Z + N - 1)) w) ∧
    (∀ support : List HeckeWord,
      IsPrefixClosed support →
      (∀ w ∈ support, ∀ g ∈ w, g < Z + N - 1) →
      ∀ w ∈ support, ¬ IsI9Absorbable support w →
      w ∈ standardBasis (Z + N - 1)) := by
  unfold inValley at hval
  unfold massNumber
  refine ⟨?_, by omega, standardBasis_not_absorbable (Z + N - 1), ?_⟩
  · rw [standardBasis_length]
    omega
  · intro support h_closed h_bounded
    exact optimal_from_prefix_closed (Z + N - 1) support h_closed h_bounded

end QOU.OptimalNF
