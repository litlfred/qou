/-
  Universal braid character formula via Young's lattice branching.

  For any braid K on 3 strands and any partition λ ⊢ k:
    χ(K, λ) = f^{λ/[3]} · χ_K^sym + f^{λ/[2,1]} · χ_K^std + f^{λ/[1³]} · χ_K^alt

  The proof is by induction on k:
  - Base case k=3: the branching is the identity (f^{μ/μ} = 1)
  - Inductive step: adding one cell to λ uses the Pieri rule
    f^{λ⁺/μ} = Σ_{λ: λ⁺ covers λ} f^{λ/μ}

  Ref: [hoefsmit1974], [wenzl1988]
       [leitner2026] §5.12, prop:universal-braid-branching
-/
import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.BraidKnot

/-- `List.getD` agrees with `getElem` in range. (Local replacement for
    `List.getD_eq_getElem`, absent from the pinned Mathlib olean.) -/
private theorem getD_eq_getElem' {α} (l : List α) (i : ℕ) (d : α)
    (h : i < l.length) : l.getD i d = l[i] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h, Option.getD_some]

/-- One-cell removals of a partition (weakly-decreasing row list): the lists
    obtained by removing a single corner cell — row `i` loses a cell exactly
    when the result stays weakly decreasing (`row i > row (i+1)`). A row
    emptied by the removal is dropped. These are the partitions λ covered by
    λ⁺ in Young's lattice. -/
def oneCellRemovals (lam : List ℕ) : List (List ℕ) :=
  (List.range lam.length).filterMap (fun i =>
    let ri := lam.getD i 0
    if ri > lam.getD (i + 1) 0 ∧ ri > 0 then
      some (lam.take i ++ (if ri = 1 then [] else [ri - 1]) ++ lam.drop (i + 1))
    else none)

/-- Removing one corner cell drops the size (sum of parts) by exactly one:
    `x.sum + 1 = lam.sum` for every `x ∈ oneCellRemovals lam`. This is the
    termination measure for `skewSYTCount`. -/
theorem oneCellRemovals_sum_succ (lam x : List ℕ) (hx : x ∈ oneCellRemovals lam) :
    x.sum + 1 = lam.sum := by
  rw [oneCellRemovals, List.mem_filterMap] at hx
  obtain ⟨i, hi, hsome⟩ := hx
  rw [List.mem_range] at hi
  simp only at hsome
  by_cases hcond : lam.getD i 0 > lam.getD (i + 1) 0 ∧ lam.getD i 0 > 0
  · rw [if_pos hcond, Option.some_inj] at hsome
    obtain ⟨_, hpos⟩ := hcond
    subst hsome
    set ri := lam.getD i 0 with hri
    rw [List.sum_append, List.sum_append]
    have hmid : (if ri = 1 then ([] : List ℕ) else [ri - 1]).sum = ri - 1 := by
      split_ifs with h1
      · simp [h1]
      · simp
    rw [hmid]
    have hlam : lam.sum = (lam.take i).sum + ri + (lam.drop (i + 1)).sum := by
      conv_lhs => rw [← List.take_append_drop (i + 1) lam]
      rw [List.sum_append, List.sum_take_succ lam i hi, hri, getD_eq_getElem' _ _ _ hi]
    omega
  · rw [if_neg hcond] at hsome
    exact absurd hsome (by simp)

/-- Every one-cell removal is strictly smaller (in size). -/
theorem oneCellRemovals_sum_lt (lam x : List ℕ) (hx : x ∈ oneCellRemovals lam) :
    x.sum < lam.sum := by
  have := oneCellRemovals_sum_succ lam x hx; omega

/-- Number of standard Young tableaux of skew shape `lambda / mu`, with
    partitions presented as weakly-decreasing `List ℕ` row lengths.

    Defined by the constructive corner-removal recursion in Young's lattice:
    `f^{μ/μ} = 1` (base case, empty skew shape), and for `λ⁺ ≠ μ`,
    `f^{λ⁺/μ} = Σ_{λ: λ⁺ covers λ} f^{λ/μ}` — the sum over one-cell removals.
    Termination is by `lam.sum`, which strictly decreases at each removal
    (`oneCellRemovals_sum_lt`). This standalone `List`-based definition mirrors
    the `Partition`-typed `QOU.Archimedean.SkewSYT.skewSYTCount` and lets this
    documentation-mirror sibling compile without depending on the library. -/
-- Ref: [hoefsmit1974] Hoefsmit, Representations of Hecke algebras of finite
--   groups with BN-pairs of classical type, PhD thesis, UBC 1974, §2.3.
-- Ref: [sagan2001] B. Sagan, The Symmetric Group, 2nd ed., Proposition 3.7.1.
noncomputable def skewSYTCount (mu lam : List ℕ) : ℕ :=
  if lam = mu then 1
  else ((oneCellRemovals lam).attach.map (fun x => skewSYTCount mu x.val)).sum
termination_by lam.sum
decreasing_by exact oneCellRemovals_sum_lt lam x.val x.property

/-- SYT count of an empty skew shape is 1: `f^{μ/μ} = 1`. -/
theorem skewSYTCount_self (mu : List ℕ) : skewSYTCount mu mu = 1 := by
  rw [skewSYTCount, if_pos rfl]

/-- Pieri rule for skew SYT counts: adding one cell decomposes.
    f^{λ⁺/μ} = Σ_{λ: λ⁺ covers λ in Young's lattice} f^{λ/μ}

    The non-trivial content is that the paths μ → λ⁺ in Young's lattice
    decompose over the intermediate λ (paths μ → λ followed by one step
    λ → λ⁺) — the saturated-chain recursion of a graded poset. The
    hypothesis `lambda_plus ≠ mu` excludes the base case `f^{μ/μ} = 1`,
    where the right-hand sum is empty. Here it is the defining recursion of
    `skewSYTCount` (the else-branch), specialised away from the base case. -/
-- Ref: [hoefsmit1974] §2.3 (branching recursion for skew standard tableaux)
theorem pieri_skew_syt (mu lambda_plus : List ℕ) (hne : lambda_plus ≠ mu) :
    skewSYTCount mu lambda_plus =
      ((oneCellRemovals lambda_plus).map (skewSYTCount mu)).sum := by
  rw [skewSYTCount, if_neg hne, List.map_attach_eq_pmap, List.pmap_eq_map]

/-- If the outer shape is strictly smaller than the inner, there is no skew
    SYT: `f^{λ/μ} = 0` when `λ.sum < μ.sum`. Proof by strong induction on
    `lam.sum` via the Pieri recursion (every removal stays below `mu.sum`). -/
theorem skewSYTCount_eq_zero_of_sum_lt (mu lam : List ℕ) (h : lam.sum < mu.sum) :
    skewSYTCount mu lam = 0 := by
  generalize hn : lam.sum = n
  induction n using Nat.strong_induction_on generalizing lam with
  | _ n ih =>
    have hne : lam ≠ mu := by rintro rfl; omega
    rw [pieri_skew_syt mu lam hne, List.sum_eq_zero]
    intro z hz
    rw [List.mem_map] at hz
    obtain ⟨x, hxmem, rfl⟩ := hz
    have hxlt : x.sum < lam.sum := oneCellRemovals_sum_lt lam x hxmem
    exact ih x.sum (by omega) x (by omega) rfl

/-- `f^{λ/μ} = 0` whenever `λ ≠ μ` and `λ.sum ≤ μ.sum` (in particular for
    distinct equal-size shapes): one Pieri step drops every removal strictly
    below `mu.sum`, then `skewSYTCount_eq_zero_of_sum_lt` applies. -/
theorem skewSYTCount_eq_zero_of_ne_of_sum_le (mu lam : List ℕ) (hne : lam ≠ mu)
    (h : lam.sum ≤ mu.sum) : skewSYTCount mu lam = 0 := by
  rw [pieri_skew_syt mu lam hne, List.sum_eq_zero]
  intro z hz
  rw [List.mem_map] at hz
  obtain ⟨x, hxmem, rfl⟩ := hz
  have hxlt : x.sum < lam.sum := oneCellRemovals_sum_lt lam x hxmem
  exact skewSYTCount_eq_zero_of_sum_lt mu x (by omega)

/-- One-cell removal preserves the partition invariants: if `lam` is
    weakly decreasing with positive parts, then so is every `x ∈
    oneCellRemovals lam`. Needed to apply the branching induction hypothesis
    to each removal. The corner condition `ri > lam[i+1]` is exactly what
    keeps the decremented row above its successor after removal. -/
theorem oneCellRemovals_pres (lam : List ℕ) (hsort : lam.Sorted (· ≥ ·))
    (hpos : ∀ a ∈ lam, 0 < a) (x : List ℕ) (hx : x ∈ oneCellRemovals lam) :
    x.Sorted (· ≥ ·) ∧ (∀ a ∈ x, 0 < a) := by
  rw [oneCellRemovals, List.mem_filterMap] at hx
  obtain ⟨i, hi, hsome⟩ := hx
  rw [List.mem_range] at hi
  simp only at hsome
  by_cases hcond : lam.getD i 0 > lam.getD (i + 1) 0 ∧ lam.getD i 0 > 0
  · rw [if_pos hcond, Option.some_inj] at hsome
    obtain ⟨hgt, hpos_i⟩ := hcond
    subst hsome
    set ri := lam.getD i 0 with hri
    have hrii : ri = lam[i] := by rw [hri]; exact getD_eq_getElem' _ _ _ hi
    have hmono : ∀ j k (hj : j < lam.length) (hk : k < lam.length), j ≤ k → lam[k] ≤ lam[j] := by
      intro j k hj hk hjk
      rcases eq_or_lt_of_le hjk with rfl | hlt
      · exact le_refl _
      · exact List.pairwise_iff_getElem.mp hsort j k hj hk hlt
    have dec_take : ∀ a ∈ lam.take i, ∃ j, j < i ∧ ∃ (hj : j < lam.length), lam[j] = a := by
      intro a ha
      obtain ⟨j, hj, hgetj⟩ := List.mem_iff_getElem.mp ha
      rw [List.length_take] at hj
      have hji : j < i := lt_of_lt_of_le hj (min_le_left _ _)
      have hjl : j < lam.length := lt_of_lt_of_le hj (min_le_right _ _)
      refine ⟨j, hji, hjl, ?_⟩
      rw [List.getElem_take] at hgetj; exact hgetj
    have dec_drop : ∀ a ∈ lam.drop (i+1), ∃ k, ∃ (hk : (i+1)+k < lam.length), lam[(i+1)+k] = a := by
      intro a ha
      obtain ⟨k, hk, hgetk⟩ := List.mem_iff_getElem.mp ha
      rw [List.length_drop] at hk
      have hik : (i+1)+k < lam.length := by omega
      refine ⟨k, hik, ?_⟩
      rw [List.getElem_drop] at hgetk; exact hgetk
    have hpos_take : ∀ a ∈ lam.take i, 0 < a := fun a ha => hpos a (List.take_subset _ _ ha)
    have hpos_drop : ∀ a ∈ lam.drop (i+1), 0 < a := fun a ha => hpos a (List.drop_subset _ _ ha)
    have hmid_pos : ∀ a ∈ (if ri = 1 then ([]:List ℕ) else [ri-1]), 0 < a := by
      split_ifs with h1
      · simp
      · intro a ha; simp only [List.mem_singleton] at ha; subst ha; omega
    have hsort_take : (lam.take i).Sorted (·≥·) := hsort.sublist (List.take_sublist _ _)
    have hsort_drop : (lam.drop (i+1)).Sorted (·≥·) := hsort.sublist (List.drop_sublist _ _)
    have hsort_mid : (if ri = 1 then ([]:List ℕ) else [ri-1]).Sorted (·≥·) := by
      split_ifs <;> simp [List.Sorted]
    have cross_tm : ∀ a ∈ lam.take i, ∀ b ∈ (if ri = 1 then ([]:List ℕ) else [ri-1]), a ≥ b := by
      intro a ha b hb
      obtain ⟨j, hji, hjl, rfl⟩ := dec_take a ha
      split_ifs at hb with h1
      · simp at hb
      · simp only [List.mem_singleton] at hb; subst hb
        have : lam[i] ≤ lam[j] := hmono j i hjl hi (le_of_lt hji)
        omega
    have cross_td : ∀ a ∈ lam.take i, ∀ b ∈ lam.drop (i+1), a ≥ b := by
      intro a ha b hb
      obtain ⟨j, hji, hjl, rfl⟩ := dec_take a ha
      obtain ⟨k, hik, rfl⟩ := dec_drop b hb
      exact hmono j ((i+1)+k) hjl hik (by omega)
    have cross_md : ∀ a ∈ (if ri = 1 then ([]:List ℕ) else [ri-1]), ∀ b ∈ lam.drop (i+1), a ≥ b := by
      intro a ha b hb
      obtain ⟨k, hik, rfl⟩ := dec_drop b hb
      have hi1 : i+1 < lam.length := by omega
      have hgtb : ri > lam[i+1] := by
        have he : lam.getD (i+1) 0 = lam[i+1] := getD_eq_getElem' _ _ _ hi1
        rw [he] at hgt; exact hgt
      have hchain : lam[(i+1)+k] ≤ lam[i+1] := hmono (i+1) ((i+1)+k) hi1 hik (by omega)
      split_ifs at ha with h1
      · simp at ha
      · simp only [List.mem_singleton] at ha; subst ha; omega
    refine ⟨?_, ?_⟩
    · show List.Pairwise (·≥·) _
      rw [List.pairwise_append, List.pairwise_append]
      refine ⟨⟨hsort_take, hsort_mid, cross_tm⟩, hsort_drop, ?_⟩
      intro a ha b hb
      rw [List.mem_append] at ha
      rcases ha with ha | ha
      · exact cross_td a ha b hb
      · exact cross_md a ha b hb
    · intro a ha
      rw [List.mem_append, List.mem_append] at ha
      rcases ha with (ha | ha) | ha
      · exact hpos_take a ha
      · exact hmid_pos a ha
      · exact hpos_drop a ha
  · rw [if_neg hcond] at hsome
    exact absurd hsome (by simp)

/-- The only weakly-decreasing lists of positive parts summing to `3` are the
    three partitions of `3`. This is the base-case enumeration for the
    branching from `H₃`. -/
theorem base_enum (lam : List ℕ) (hsort : lam.Sorted (· ≥ ·)) (hpos : ∀ a ∈ lam, 0 < a)
    (hsum : lam.sum = 3) : lam = [3] ∨ lam = [2, 1] ∨ lam = [1, 1, 1] := by
  match lam, hsort, hpos, hsum with
  | [a], hsort, hpos, hsum =>
      left; simp only [List.sum_cons, List.sum_nil, add_zero] at hsum
      have : a = 3 := by omega
      subst this; rfl
  | [a, b], hsort, hpos, hsum =>
      right; left
      simp only [List.sum_cons, List.sum_nil, add_zero] at hsum
      have hab : a ≥ b := (List.sorted_cons.mp hsort).1 b (by simp)
      have hb : 0 < b := hpos b (by simp)
      have ha : 0 < a := hpos a (by simp)
      have h2 : a = 2 ∧ b = 1 := by omega
      simp [h2.1, h2.2]
  | [a, b, c], hsort, hpos, hsum =>
      right; right
      simp only [List.sum_cons, List.sum_nil, add_zero] at hsum
      have ha := hpos a (by simp); have hb := hpos b (by simp); have hc := hpos c (by simp)
      have hs := List.sorted_cons.mp hsort
      have hab : a ≥ b := hs.1 b (by simp)
      have hbc : b ≥ c := (List.sorted_cons.mp hs.2).1 c (by simp)
      have h3 : a = 1 ∧ b = 1 ∧ c = 1 := by omega
      simp [h3.1, h3.2.1, h3.2.2]
  | [], _, _, hsum => simp at hsum
  | a :: b :: c :: d :: t, hsort, hpos, hsum =>
      exfalso
      have ha := hpos a (by simp); have hb := hpos b (by simp)
      have hc := hpos c (by simp); have hd := hpos d (by simp)
      simp only [List.sum_cons] at hsum
      have : (t.sum) ≥ 0 := Nat.zero_le _
      omega

/-- Linearity of the list sum over the three-term branching combination. -/
theorem sum_lin {R : Type*} [CommSemiring R]
    (l : List (List ℕ)) (A B C : List ℕ → R) (p q r : R) :
    (l.map (fun x => A x * p + B x * q + C x * r)).sum
      = (l.map A).sum * p + (l.map B).sum * q + (l.map C).sum * r := by
  induction l with
  | nil => simp
  | cons hd tl ih => simp only [List.map_cons, List.sum_cons, ih]; ring

/-- Real-valued Pieri rule: `(f^{λ/μ} : ℝ)` is the sum of the real casts of
    the removal counts. Cast of `pieri_skew_syt`. -/
theorem cast_pieri (mu lam : List ℕ) (hne : lam ≠ mu) :
    (skewSYTCount mu lam : ℝ)
      = ((oneCellRemovals lam).map (fun x => (skewSYTCount mu x : ℝ))).sum := by
  rw [pieri_skew_syt mu lam hne, Nat.cast_list_sum, List.map_map]; rfl

/-- The universal branching formula.

    For any braid K on 3 strands, the character in irrep λ of H_k(q) is
    determined by the three base characters and the skew SYT counts.

    Proof by induction on k:
    Base (k=3): ρ_μ↓H₃ = ρ_μ, so skewSYTCount μ μ = 1 (empty skew shape).
    Step (k→k+1): by Pieri rule + linearity of the trace. -/
theorem universal_braid_branching
    (chi : List ℕ → ℝ) (chi_sym chi_std chi_alt : ℝ)
    -- Restriction/linearity step: above the base level the character
    -- decomposes over the one-cell removals (branching of ρ_λ↓H_{k-1}).
    (h_rec : ∀ lam : List ℕ, lam.sum > 3 →
      chi lam = ((oneCellRemovals lam).map chi).sum)
    -- Base case k = 3: the three H₃ characters.
    (h_base : chi [3] = chi_sym ∧ chi [2, 1] = chi_std ∧ chi [1, 1, 1] = chi_alt)
    (lam : List ℕ) (hsort : lam.Sorted (· ≥ ·)) (hpos : ∀ a ∈ lam, 0 < a)
    (hsum : lam.sum ≥ 3) :
    chi lam =
      (skewSYTCount [3] lam : ℝ) * chi_sym +
      (skewSYTCount [2, 1] lam : ℝ) * chi_std +
      (skewSYTCount [1, 1, 1] lam : ℝ) * chi_alt := by
  -- Strong induction on lam.sum: the step interchanges the removal sum
  -- with the three-term decomposition and closes with pieri_skew_syt;
  -- the base case is h_base after enumerating the partitions of 3.
  -- Ref: [hoefsmit1974] §2.3; [wenzl1988]; [leitner2026] §5.12 prop:universal-braid-branching
  obtain ⟨hb3, hb21, hb111⟩ := h_base
  generalize hn : lam.sum = n
  induction n using Nat.strong_induction_on generalizing lam with
  | _ n ih =>
    rcases Nat.lt_or_ge n 4 with hlt | hge
    · -- base case: n = 3
      have hn3 : lam.sum = 3 := by omega
      rcases base_enum lam hsort hpos hn3 with rfl | rfl | rfl
      · rw [show skewSYTCount [3] [3] = 1 from skewSYTCount_self _,
            show skewSYTCount [2, 1] [3] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide),
            show skewSYTCount [1, 1, 1] [3] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide), hb3]
        push_cast; ring
      · rw [show skewSYTCount [3] [2, 1] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide),
            show skewSYTCount [2, 1] [2, 1] = 1 from skewSYTCount_self _,
            show skewSYTCount [1, 1, 1] [2, 1] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide), hb21]
        push_cast; ring
      · rw [show skewSYTCount [3] [1, 1, 1] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide),
            show skewSYTCount [2, 1] [1, 1, 1] = 0 from
              skewSYTCount_eq_zero_of_ne_of_sum_le _ _ (by decide) (by decide),
            show skewSYTCount [1, 1, 1] [1, 1, 1] = 1 from skewSYTCount_self _, hb111]
        push_cast; ring
    · -- inductive step: n ≥ 4
      have hstep : lam.sum > 3 := by omega
      have hne3 : lam ≠ [3] := by rintro rfl; simp at hstep
      have hne21 : lam ≠ [2, 1] := by rintro rfl; simp at hstep
      have hne111 : lam ≠ [1, 1, 1] := by rintro rfl; simp at hstep
      rw [h_rec lam hstep]
      have key : ∀ x ∈ oneCellRemovals lam,
          chi x = (skewSYTCount [3] x : ℝ) * chi_sym +
            (skewSYTCount [2, 1] x : ℝ) * chi_std +
            (skewSYTCount [1, 1, 1] x : ℝ) * chi_alt := by
        intro x hx
        obtain ⟨hxs, hxp⟩ := oneCellRemovals_pres lam hsort hpos x hx
        have hxsucc := oneCellRemovals_sum_succ lam x hx
        exact ih x.sum (by omega) x hxs hxp (by omega) rfl
      rw [List.map_congr_left key, sum_lin]
      rw [cast_pieri [3] lam hne3, cast_pieri [2, 1] lam hne21,
        cast_pieri [1, 1, 1] lam hne111]

/-- The Chebyshev identity for traces of SL(2) powers:
    tr(M³) = t³ - 3t where t = tr(M).
    Used to derive the Borromean character from the figure-eight.

    The hypothesis `hCH` is the 2×2 Cayley–Hamilton relation
    `M² = t·M - det(M)·I` specialised to `det M = 1` (M ∈ SL(2)).
    From it: M³ = t·M² - M = (t²)·M - t·I - M, and taking traces
    (tr M = t, tr I = 2) gives tr(M³) = t³ - 3t. -/
theorem chebyshev_sl2_cube {R : Type*} [CommRing R]
    (M : Matrix (Fin 2) (Fin 2) R)
    (hCH : M ^ 2 = M.trace • M - 1) :
    (M ^ 3).trace = M.trace ^ 3 - 3 * M.trace := by
  have h3 : M ^ 3 =
      (M.trace ^ 2) • M - M.trace • (1 : Matrix (Fin 2) (Fin 2) R) - M := by
    calc M ^ 3 = M ^ 2 * M := by rw [pow_succ]
      _ = (M.trace • M - 1) * M := by rw [hCH]
      _ = M.trace • (M * M) - M := by rw [sub_mul, smul_mul_assoc, one_mul]
      _ = M.trace • (M.trace • M - 1) - M := by rw [← pow_two, hCH]
      _ = (M.trace ^ 2) • M - M.trace • 1 - M := by
            rw [smul_sub, smul_smul, ← pow_two]
  rw [h3, Matrix.trace_sub, Matrix.trace_sub, Matrix.trace_smul,
    Matrix.trace_smul, Matrix.trace_one]
  simp only [smul_eq_mul, Fintype.card_fin, Nat.cast_ofNat]
  ring

/-- The BW convergence-bound **envelope** `C₀ · [2]_q^{-2(k-3)}` is
    non-negative for `q > 1`, `C₀ > 0`.

    **This is not the convergence bound.** It says nothing about MAE(k)
    — no error quantity appears in the statement. It establishes only
    that the expression proposed as an upper bound is itself
    non-negative, which follows from `positivity`.

    The claim the manuscript makes, `MAE(k) ≤ C₀ · [2]_q^{-2(k-3)}` with
    `C₀ ≈ 0.035%` the k=3 mass MAE, is **not formalised here and does not
    follow from this**: MAE(k) is a numerical quantity of the mass table
    with no definition in scope, so there is nothing for the inequality
    to constrain. Stating it would need MAE defined first.

    Renamed 2026-08-23 (bean `qou-lo1t`). It was `convergence_bound`,
    under a docstring asserting the MAE inequality and three inline
    comments elaborating a bound the statement never makes. The name and
    the docstring were the whole of the claim.

    For a convergence bound that *is* stated over the quantities it
    bounds, see `QOU.Archimedean.SkewSYT.ConvergenceBound` — the
    Kerov–Vershik `|f_k - f_inf| ≤ C_q / (k-3)`, carried as a class with
    a proved reflexivity instance. It is a different bound (`1/(k-3)`,
    not exponential in `k`), so it is not this one restated. -/
-- Ref: [leitner2026] §5.13
theorem convergence_bound_envelope_nonneg
    (q : ℝ) (hq : q > 1) (C₀ : ℝ) (hC : C₀ > 0)
    (_k : ℕ) :
    C₀ * (q + 1/q) ^ ((-2 : ℤ) * ((_k : ℤ) - 3)) ≥ 0 := by
  -- `C₀ > 0` and `q + 1/q > 0` for `q > 1`; an integer power of a
  -- positive real is positive, so the product is positive.
  have hq_pos : q > 0 := lt_trans zero_lt_one hq
  have h_sum_pos : q + 1/q > 0 := by
    have hinv : (1 : ℝ) / q > 0 := by positivity
    linarith
  positivity

end QOU.BraidKnot
