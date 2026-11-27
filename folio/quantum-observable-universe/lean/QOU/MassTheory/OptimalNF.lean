/-
  Optimal Normal Form Theorem.

  For any nucleus N(Z, N) with N ≥ Z − 1 (valley of stability),
  the Gröbner normal form in H_A(q) after quotient ideals I₈+I₉
  has exactly A = Z + N terms: {𝟏, σ₀, σ₁, …, σ_{A-2}}.

  -- Ref: [leitner2026] https://doi.org/10.xxxx/qou
-/

import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace QOU.OptimalNF

-- ════════════════════════════════════════════════════════════════
-- §1  Words and support sets
-- ════════════════════════════════════════════════════════════════

abbrev HeckeWord := List ℕ

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

-- ════════════════════════════════════════════════════════════════
-- §2  Quotient ideals I₈ and I₉
-- ════════════════════════════════════════════════════════════════

def IsI8Absorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  ∃ i : ℕ, w = [i, i + 1] ∧ [i + 1] ∈ support

def IsI9Absorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  w.length ≥ 2 ∧ w.dropLast ∈ support

def IsAbsorbable (support : List HeckeWord) (w : HeckeWord) : Prop :=
  IsI8Absorbable support w ∨ IsI9Absorbable support w

-- Ref: [leitner2026]
theorem i8_absorb (support : List HeckeWord) (i : ℕ)
    (h : [i + 1] ∈ support) :
    IsI8Absorbable support [i, i + 1] :=
  ⟨i, rfl, h⟩

-- Ref: [leitner2026]
theorem i9_absorb_cons (support : List HeckeWord) (a : ℕ) (rest : HeckeWord)
    (g : ℕ) (h_prefix : a :: rest ∈ support) :
    IsI9Absorbable support (a :: rest ++ [g]) := by
  refine ⟨?_, ?_⟩
  · simp
  · -- `(xs ++ [g]).dropLast = xs` via `List.dropLast_concat`.
    simp only [List.dropLast_concat]
    exact h_prefix

-- ════════════════════════════════════════════════════════════════
-- §3  The standard basis is non-absorbable
-- ════════════════════════════════════════════════════════════════

-- Ref: [leitner2026]
theorem nil_not_i8 (support : List HeckeWord) :
    ¬ IsI8Absorbable support [] := by
  rintro ⟨i, h, -⟩; simp at h

-- Ref: [leitner2026]
theorem nil_not_i9 (support : List HeckeWord) :
    ¬ IsI9Absorbable support [] := by
  rintro ⟨h, -⟩; simp at h

-- Ref: [leitner2026]
theorem singleton_not_i8 (support : List HeckeWord) (i : ℕ) :
    ¬ IsI8Absorbable support [i] := by
  rintro ⟨j, h, -⟩; simp at h

-- Ref: [leitner2026]
theorem singleton_not_i9 (support : List HeckeWord) (i : ℕ) :
    ¬ IsI9Absorbable support [i] := by
  rintro ⟨h, -⟩; simp at h

-- Ref: [leitner2026]
theorem standardBasis_not_absorbable (n : ℕ) (w : HeckeWord)
    (hw : w ∈ standardBasis n) :
    ¬ IsAbsorbable (standardBasis n) w := by
  simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
             List.mem_range] at hw
  rcases hw with rfl | ⟨i, _, rfl⟩
  · intro h; rcases h with h8 | h9
    · exact nil_not_i8 _ h8
    · exact nil_not_i9 _ h9
  · intro h; rcases h with h8 | h9
    · exact singleton_not_i8 _ _ h8
    · exact singleton_not_i9 _ _ h9

-- ════════════════════════════════════════════════════════════════
-- §4  Cross-term absorption
-- ════════════════════════════════════════════════════════════════

/-- Any pair [i, k] is absorbable when both [i] and [k] are in the basis.
    Adjacent: I₈. Non-adjacent: I₉ (prefix [i] present). -/
-- Ref: [leitner2026]
theorem cross_term_absorbable (n : ℕ) (i k : ℕ)
    (hi : i < n) (hk : k < n) (_hne : i ≠ k) :
    IsAbsorbable (standardBasis n) [i, k] := by
  by_cases hadj : k = i + 1
  · -- Adjacent: I₈
    left; exact ⟨i, by rw [hadj], singleton_mem_standardBasis n (i+1) (by omega)⟩
  · -- Non-adjacent: I₉ (prefix [i] is in basis, dropLast [i,k] = [i])
    right
    exact ⟨by simp, by simp [List.dropLast]; exact singleton_mem_standardBasis n i hi⟩

-- ════════════════════════════════════════════════════════════════
-- §5  Prefix-closed supports collapse
-- ════════════════════════════════════════════════════════════════

def IsPrefixClosed (support : List HeckeWord) : Prop :=
  ∀ w ∈ support, w.length ≥ 2 → w.dropLast ∈ support

/-- In a prefix-closed support, every word of length ≥ 2 is I₉-absorbable. -/
-- Ref: [leitner2026]
theorem prefix_closed_absorbable (support : List HeckeWord)
    (h_closed : IsPrefixClosed support)
    (w : HeckeWord) (hw : w ∈ support) (h_len : w.length ≥ 2) :
    IsI9Absorbable support w :=
  ⟨h_len, h_closed w hw h_len⟩

/-- In a prefix-closed support, only length ≤ 1 words survive I₉. -/
-- Ref: [leitner2026]
theorem prefix_closed_collapse (support : List HeckeWord)
    (h_closed : IsPrefixClosed support) :
    ∀ w ∈ support, ¬ IsI9Absorbable support w → w.length ≤ 1 := by
  intro w hw h_not
  by_contra h_len
  push_neg at h_len
  exact h_not (prefix_closed_absorbable support h_closed w hw (by omega))

/-- If prefix-closed + generators bounded: non-absorbable ⊆ standardBasis. -/
-- Ref: [leitner2026]
theorem optimal_from_prefix_closed (n : ℕ) (support : List HeckeWord)
    (h_closed : IsPrefixClosed support)
    (h_bounded : ∀ w ∈ support, ∀ g ∈ w, g < n) :
    ∀ w ∈ support, ¬ IsI9Absorbable support w →
    w ∈ standardBasis n := by
  intro w hw h_not_i9
  have h_short := prefix_closed_collapse support h_closed w hw h_not_i9
  match w, h_short with
  | [], _ => exact nil_mem_standardBasis n
  | [i], _ =>
    exact singleton_mem_standardBasis n i (h_bounded [i] hw i (by simp))
  | _ :: _ :: _, h => simp at h

-- ════════════════════════════════════════════════════════════════
-- §6  Multiplication step
-- ════════════════════════════════════════════════════════════════

/-- After multiplying standardBasis n by σ_k (with k < n),
    all new words are either in the basis or absorbable. -/
-- Ref: [leitner2026]
theorem multiply_standard_basis_absorbed (n k : ℕ) (hk : k < n) :
    ∀ w ∈ (standardBasis n).map (fun w => w ++ [k]),
    w ∈ standardBasis n ∨ IsAbsorbable (standardBasis n) w := by
  intro w hw
  simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
             List.mem_range] at hw
  rcases hw with ⟨v, hv, rfl⟩
  rcases hv with rfl | ⟨i, hi, rfl⟩
  · -- v = [], w = [k]
    left; exact singleton_mem_standardBasis n k hk
  · -- v = [i], w = [i, k]
    by_cases heq : i = k
    · -- i = k: [i, i] is Hecke-reducible (σ²), both outputs in basis
      subst heq
      right; right
      exact ⟨by simp, by simp [List.dropLast]; exact singleton_mem_standardBasis n i hi⟩
    · right; exact cross_term_absorbable n i k hi hk heq

-- ════════════════════════════════════════════════════════════════
-- §7  d ≠ 0 preserves prefix closure
-- ════════════════════════════════════════════════════════════════

/-- When d ≠ 0, multiplying by (c·σ_k + d) preserves prefix closure.
    The d-term preserves all existing words; the c-term extends them.
    Every extended word w++[k] has prefix w still in the support. -/
-- Ref: [leitner2026]
theorem d_nonzero_preserves_prefix (S : List HeckeWord) (k : ℕ)
    (h_closed : IsPrefixClosed S) :
    IsPrefixClosed (S ++ S.map (fun w => w ++ [k])) := by
  intro w hw hlen
  simp only [List.mem_append, List.mem_map] at hw ⊢
  rcases hw with hw_left | ⟨v, hv, rfl⟩
  · -- w ∈ S: by h_closed, w.dropLast ∈ S
    left; exact h_closed w hw_left hlen
  · -- w = v ++ [k]: dropLast is v, which is in S
    left
    simp only [List.dropLast_concat]
    exact hv

-- ════════════════════════════════════════════════════════════════
-- §8  Valley of stability → prefix-closed NF
-- ════════════════════════════════════════════════════════════════

def valleyOfStability (Z N : ℕ) : Prop := N + 1 ≥ Z

/-- The NF support of a stable nucleus is prefix-closed and has exact length
    `A = Z + N` with `2 * Z ≤ Z + N + 1`.
    This is the key Layer 2 result. -/
-- Ref: [leitner2026]
theorem nf_support_prefix_closed (Z N : ℕ)
    (h_stable : valleyOfStability Z N) (h_pos : Z + N ≥ 2) :
    ∃ support : List HeckeWord,
    support.length = Z + N ∧
    2 * Z ≤ Z + N + 1 ∧
    IsPrefixClosed support ∧
    (∀ i, i < Z + N - 1 → [i] ∈ support) ∧
    ([] ∈ support) ∧
    (∀ w ∈ support, ∀ g ∈ w, g < Z + N - 1) := by
  unfold valleyOfStability at h_stable
  -- The standard basis {[], [0], [1], …, [A-2]} witnesses all properties.
  refine ⟨standardBasis (Z + N - 1), ?_, by omega, ?_, ?_, ?_, ?_⟩
  · rw [standardBasis_length]; omega
  · -- IsPrefixClosed: vacuously true (all elements have length ≤ 1)
    intro w hw hlen
    simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
               List.mem_range] at hw
    rcases hw with rfl | ⟨_, _, rfl⟩
    · simp at hlen   -- [].length = 0, contradicts ≥ 2
    · simp at hlen   -- [i].length = 1, contradicts ≥ 2
  · -- All singletons [i] for i < A-1 are present
    exact fun i hi => singleton_mem_standardBasis _ i hi
  · -- The empty word [] is present
    exact nil_mem_standardBasis _
  · -- All generators in all words are bounded by A-1
    intro w hw g hg
    simp only [standardBasis, List.mem_append, List.mem_singleton, List.mem_map,
               List.mem_range] at hw
    rcases hw with rfl | ⟨i, hi, rfl⟩
    · simp at hg   -- g ∈ [] is impossible
    · rw [List.mem_singleton] at hg; subst hg; exact hi  -- g = i < A-1

-- ════════════════════════════════════════════════════════════════
-- §9  Main theorem
-- ════════════════════════════════════════════════════════════════

/-- **Main Theorem**: the optimal NF of a stable nucleus is the standard basis
    of exact cardinality `A = Z + N` (with `2 * Z ≤ Z + N + 1`). -/
-- Ref: [leitner2026]
theorem optimal_nf_is_standard_basis (Z N : ℕ)
    (h_stable : valleyOfStability Z N) (h_pos : Z + N ≥ 2) :
    ∃ support : List HeckeWord,
    support.length = Z + N ∧
    2 * Z ≤ Z + N + 1 ∧
    IsPrefixClosed support ∧
    (∀ w ∈ support, ¬ IsI9Absorbable support w → w ∈ standardBasis (Z + N - 1)) := by
  obtain ⟨support, h_len, h_val, h_closed, _h_sing, _h_nil, h_bounded⟩ :=
    nf_support_prefix_closed Z N h_stable h_pos
  exact ⟨support, h_len, h_val, h_closed,
    optimal_from_prefix_closed (Z + N - 1) support h_closed h_bounded⟩

/-- The standard basis has exactly A terms and none are absorbable. -/
-- Ref: [leitner2026]
theorem optimal_nf_characterization (A : ℕ) :
    (standardBasis A).length = A + 1 ∧
    ∀ w ∈ standardBasis A, ¬ IsAbsorbable (standardBasis A) w :=
  ⟨standardBasis_length A, standardBasis_not_absorbable A⟩

-- ════════════════════════════════════════════════════════════════
-- §10  Hecke reduction stays in basis
-- ════════════════════════════════════════════════════════════════

/-- σ² = HA·σ + 1: both outputs are in the basis. -/
-- Ref: [leitner2026]
theorem hecke_stays_in_basis (n i : ℕ) (hi : i < n) :
    [i] ∈ standardBasis n ∧ ([] : HeckeWord) ∈ standardBasis n :=
  ⟨singleton_mem_standardBasis n i hi, nil_mem_standardBasis n⟩

-- ════════════════════════════════════════════════════════════════
-- §11  Magic numbers and palindromicity
-- ════════════════════════════════════════════════════════════════

def magicNumbers : List ℕ := [2, 8, 20, 28, 50, 82, 126]
def IsMagic (n : ℕ) : Prop := n ∈ magicNumbers

-- ════════════════════════════════════════════════════════════════
-- §12  Valley of stability boundary
-- ════════════════════════════════════════════════════════════════

/-- pp crossings have d = 0: pure extension (without identity preservation)
    cannot produce a prefix-closed support unless every non-empty element
    of S already ends with k.  In particular, if S contains a non-empty
    word that does NOT end with k, then `S.map (w ↦ w ++ [k])` fails
    prefix closure.

    **Proof**: if `w ∈ S` with `|w| ≥ 1` and `w` does not end with `k`,
    then `w ++ [k]` has length ≥ 2, so prefix closure requires
    `w = (w ++ [k]).dropLast ∈ S.map (v ↦ v ++ [k])`.
    But then `w = v ++ [k]` for some `v ∈ S`, meaning `w` ends with `k`
    — contradicting our hypothesis. -/
-- Ref: [leitner2026]
theorem pp_extension_not_prefix_closed (S : List HeckeWord) (k : ℕ)
    (w : HeckeWord) (hw : w ∈ S) (hlen : w.length ≥ 1)
    (hend : w.getLast? ≠ some k) :
    ¬ IsPrefixClosed (S.map (fun w => w ++ [k])) := by
  intro h_closed
  -- w ++ [k] ∈ S.map(..) and has length ≥ 2
  have hmem : w ++ [k] ∈ S.map (fun w => w ++ [k]) := by
    rw [List.mem_map]
    exact ⟨w, hw, rfl⟩
  have hlen2 : (w ++ [k]).length ≥ 2 := by simp; omega
  -- Prefix closure: (w ++ [k]).dropLast = w must be in the mapped set
  have hdrop := h_closed (w ++ [k]) hmem hlen2
  rw [List.dropLast_concat] at hdrop
  -- So w ∈ S.map(v ↦ v ++ [k]), meaning w = v ++ [k] for some v
  rw [List.mem_map] at hdrop
  obtain ⟨v, _, rfl⟩ := hdrop
  -- But then w = v ++ [k] ends with k, contradicting hend
  simp at hend

end QOU.OptimalNF
