import QOU.Mathlib.SYTHookFormulaGeneral

/-!
# QOU.Mathlib.SYTHookGNW — corner-recursion infrastructure for the general HLF (GNW route)

The general dimension hook-length formula `numSYTenum l = dimHLF l` is presently isolated to the single
**Aitken/Frobenius determinant identity** `SYTHookFormulaGeneral.dimAitkenIdentity` (ii).  That gap is
*blocked* by the pinned Mathlib: it has no `Combinatorics.RSK` / Specht / Frobenius-determinant
infrastructure, so the determinant evaluation cannot be carried out at all.

This file develops the **Greene–Nijenhuis–Wilf corner-recursion** route, which needs **none** of that
infrastructure — it is pure `ℕ`/`ℚ` combinatorics — and so converts the *blocked* determinant gap into
two *unblocked* (if still open) self-contained statements:

* **corner recursion of the count** (`CornerRecursion`):
  `numSYTenum λ = Σ_{removable corners c} numSYTenum (λ ∖ c)` — the largest entry sits in a removable
  corner; deleting it is a bijection onto the disjoint union of the smaller shapes;
* **GNW hook-summation identity** (`GNWHookIdentity`, over `ℚ`):
  `Σ_{corners c} ∏h_λ / ∏h_{λ∖c} = n` — the partial-fractions / telescoping identity on hook products.

The reduction itself — strong induction on `n = sz l` combining the two — is proved **sorry-free** here
(`numSYTenum_eq_dimHLF_of_gnw`), as is all the corner-removal infrastructure (`removeCorner` preserves
sortedness and positivity and drops the size by one).  So the *only* residual content is the two
combinatorial identities above; everything connecting them to the HLF is machine-checked.

Pure combinatorics on `ℕ`/`ℚ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (prodHooks dimHLF sz colLen colLen_duality)

/-! ## Corner-removal infrastructure -/

/-- Row index `i` is a **removable corner** of shape `l`: a genuine row whose last cell is an outer
corner, i.e. the next row is strictly shorter (treating "beyond the last row" as length `0`).  For a
weakly-decreasing positive shape this is exactly the set of cells whose deletion leaves a shape. -/
def IsCorner (l : List ℕ) (i : ℕ) : Prop :=
  i < l.length ∧ l.getD (i + 1) 0 < l.getD i 0

instance (l : List ℕ) (i : ℕ) : Decidable (IsCorner l i) := by
  unfold IsCorner; infer_instance

/-- Remove one cell from the end of row `i`: decrement that row's length, then drop the row entirely
if it has shrunk to `0` (which, for a removable corner of a weakly-decreasing positive shape, happens
only when `i` is the final length-`1` row). -/
def removeCorner (l : List ℕ) (i : ℕ) : List ℕ :=
  (l.set i (l.getD i 0 - 1)).filter (· != 0)

/-- Filtering out zeros leaves the sum unchanged. -/
theorem sum_filter_ne_zero : ∀ m : List ℕ, (m.filter (· != 0)).sum = m.sum
  | [] => rfl
  | a :: t => by
    by_cases h : a = 0
    · subst h
      simp [sum_filter_ne_zero t]
    · have hb : (a != 0) = true := by simpa using h
      simp [hb, sum_filter_ne_zero t]

/-- Decrementing the length of a genuine row drops the total cell count by one. -/
theorem sum_set_decr : ∀ (l : List ℕ) (i : ℕ), i < l.length → 1 ≤ l.getD i 0 →
    (l.set i (l.getD i 0 - 1)).sum + 1 = l.sum
  | a :: t, 0, _, h1 => by
    have h1a : 1 ≤ a := by simpa using h1
    simp only [List.set_cons_zero, List.getD_cons_zero, List.sum_cons]
    omega
  | a :: t, n + 1, hi, h1 => by
    have hi' : n < t.length := by simpa using hi
    have h1' : 1 ≤ t.getD n 0 := by simpa using h1
    have ih := sum_set_decr t n hi' h1'
    simp only [List.set_cons_succ, List.getD_cons_succ, List.sum_cons]
    omega

/-- **`removeCorner` drops the cell count by one** at any genuine row with a positive length. -/
theorem sz_removeCorner (l : List ℕ) (i : ℕ) (hi : i < l.length) (hpos : 1 ≤ l.getD i 0) :
    sz (removeCorner l i) + 1 = sz l := by
  unfold sz removeCorner
  rw [sum_filter_ne_zero]
  exact sum_set_decr l i hi hpos

/-- `l.getD i 0 = l[i]` for a genuine index. -/
private theorem getD_eq_getElem' (l : List ℕ) (i : ℕ) (hi : i < l.length) :
    l.getD i 0 = l[i] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi, Option.getD_some]

/-- **Decrementing a removable corner preserves weak decrease.**  The new length `l[i]−1` still sits
between its neighbours: `l[i−1] ≥ l[i] ≥ l[i]−1` and `l[i]−1 ≥ l[i+1]` (the latter because a corner has
`l[i+1] < l[i]`). -/
theorem sorted_set_corner (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l i) :
    List.Sorted (· ≥ ·) (l.set i (l.getD i 0 - 1)) := by
  obtain ⟨hi, hnext⟩ := hc
  have hgi : l.getD i 0 = l[i] := getD_eq_getElem' l i hi
  have hlg := List.pairwise_iff_getElem.mp hl
  refine List.pairwise_iff_getElem.mpr ?_
  intro p q hp hq hpq
  rw [List.length_set] at hp hq
  rw [List.getElem_set, List.getElem_set]
  by_cases hip : i = p
  · subst hip
    rw [if_pos rfl, if_neg (show ¬ i = q by omega)]
    have hi1 : i + 1 < l.length := by omega
    have hnext' : l[i + 1] < l[i] := by
      have he : l.getD (i + 1) 0 = l[i + 1] := getD_eq_getElem' l (i + 1) hi1
      rw [he, hgi] at hnext; exact hnext
    rcases Nat.lt_or_ge (i + 1) q with hq1 | hq1
    · have := hlg (i + 1) q hi1 hq hq1; omega
    · have hqe : q = i + 1 := by omega
      subst hqe; omega
  · by_cases hiq : i = q
    · subst hiq
      rw [if_neg hip, if_pos rfl]
      have := hlg p i hp hi (by omega)
      omega
    · rw [if_neg hip, if_neg hiq]
      exact hlg p q hp hq hpq

/-- **`removeCorner` preserves weak decrease** (filtering a sorted list keeps it sorted). -/
theorem sorted_removeCorner (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l i) :
    List.Sorted (· ≥ ·) (removeCorner l i) :=
  (List.Pairwise.sublist List.filter_sublist (sorted_set_corner l i hl hc))

/-- **`removeCorner` is positive** — every surviving row has length `≥ 1` (zeros were filtered out). -/
theorem removeCorner_pos (l : List ℕ) (i : ℕ) : ∀ a ∈ removeCorner l i, 0 < a := by
  intro a ha
  unfold removeCorner at ha
  rw [List.mem_filter] at ha
  have : a ≠ 0 := by simpa using ha.2
  omega

/-! ## Hook product is positive, and the corner index set -/

/-- A list of positive naturals has positive product. -/
theorem list_prod_pos : ∀ (L : List ℕ), (∀ x ∈ L, 0 < x) → 0 < L.prod
  | [], _ => by simp
  | a :: t, h => by
    rw [List.prod_cons]
    exact Nat.mul_pos (h a (by simp)) (list_prod_pos t (fun x hx => h x (List.mem_cons_of_mem a hx)))

/-- **The hook product is positive** on a weakly-decreasing positive shape: every cell `(i, j)` with
`j < λ_i` has hook `(λ_i − j) + (colLen j − i) − 1 ≥ 1`, since `λ_i − j ≥ 1` and `colLen j > i` (the
column through an existing cell is at least `i + 1` tall, by `colLen_duality`). -/
theorem prodHooks_pos (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
    0 < prodHooks l := by
  unfold prodHooks
  apply list_prod_pos
  intro x hx
  rw [List.mem_map] at hx
  obtain ⟨i, _hi, rfl⟩ := hx
  apply list_prod_pos
  intro y hy
  rw [List.mem_map] at hy
  obtain ⟨j, hj, rfl⟩ := hy
  rw [List.mem_range] at hj
  have hcol : i < colLen l j := (colLen_duality l hl i j).mpr hj
  omega

/-- The removable corners of `l`, as the list of row indices `i` with `IsCorner l i`. -/
def corners (l : List ℕ) : List ℕ :=
  (List.range l.length).filter (fun i => decide (IsCorner l i))

/-- Membership in `corners l` is exactly being a removable corner. -/
theorem mem_corners {l : List ℕ} {c : ℕ} (h : c ∈ corners l) : IsCorner l c := by
  unfold corners at h
  rw [List.mem_filter] at h
  exact of_decide_eq_true h.2

/-- A removable corner of a positive shape has positive row length, so `removeCorner` shrinks `sz`. -/
theorem getD_pos_of_corner {l : List ℕ} (hpos : ∀ a ∈ l, 0 < a) {c : ℕ} (hc : IsCorner l c) :
    1 ≤ l.getD c 0 := by
  rw [getD_eq_getElem' l c hc.1]
  exact hpos _ (List.getElem_mem hc.1)

/-- Pull a constant out of a list sum-of-map: `∑ (A · f c) = A · ∑ f c`. -/
theorem sum_map_const_mul (A : ℚ) (L : List ℕ) (f : ℕ → ℚ) :
    (L.map (fun c => A * f c)).sum = A * (L.map f).sum := by
  induction L with
  | nil => simp
  | cons a t ih => simp [List.sum_cons, ih, mul_add]

/-! ## Bridge: the brute-force enumerator is Mathlib's `List.permutations'`

`allPerms` / `insertEverywhere` are definitionally Mathlib's `List.permutations'` / `permutations'Aux`
(the structural — kernel-reducible — permutation generator).  Identifying them lets the corner-recursion
bijection use Mathlib's permutation API (`mem_permutations'`, `permutations_perm_permutations'`, …)
instead of re-deriving completeness/no-duplication of the generator by hand. -/

/-- `insertEverywhere` is Mathlib's `permutations'Aux`. -/
theorem insertEverywhere_eq (x : ℕ) (l : List ℕ) :
    insertEverywhere x l = l.permutations'Aux x := by
  induction l with
  | nil => rfl
  | cons a t ih => simp [insertEverywhere, List.permutations'Aux, ih]

/-- **The brute-force generator is `List.permutations'`** — `allPerms l = l.permutations'`. -/
theorem allPerms_eq_permutations' (l : List ℕ) : allPerms l = l.permutations' := by
  induction l with
  | nil => rfl
  | cons a t ih =>
    simp only [allPerms, List.permutations', ih]
    congr 1
    funext y
    exact insertEverywhere_eq a y

/-- **`numSYTenum` as a filtered length over `permutations'`** — the form the corner bijection counts
against: `#SYT(λ) = |{ standard fillings among the permutations of [1,…,n] }|`. -/
theorem numSYTenum_eq_length_filter (l : List ℕ) :
    numSYTenum l = (((List.range (sz l)).map (· + 1)).permutations'.filter (isStdFilling l)).length := by
  unfold numSYTenum sz
  rw [allPerms_eq_permutations', List.countP_eq_length_filter]

/-! ## The two residual GNW identities (cited `sorry` — self-contained, unblocked)

Unlike `SYTHookFormulaGeneral.dimAitkenIdentity` (blocked: needs Specht/RSK/Frobenius-determinant
infrastructure absent from the pinned Mathlib), both statements below are pure `ℕ`/`ℚ` combinatorics on
the list shape model and are in principle provable on the current toolchain. -/

/-- **(GNW count) corner recursion of the standard-tableau count.**  In any standard tableau of shape
`λ` the largest entry `n` occupies a removable corner; deleting it is a bijection
`SYT(λ) ≃ ⨆_{corners c} SYT(λ ∖ c)`, whence the count splits as a sum.

**Closure route (validated this session).**  Do *not* prove this as a flat-list `eraseIdx` bijection on
`numSYTenum`'s permutation model — go through the **already-proved structural bridge**
`SYTEnumerationFintype.numSYTenum_eq_numStandardYoungTableaux`
(`numSYTenum l = numStandardYoungTableaux (YoungDiagram.ofRowLens l hl) = Nat.card (StandardYoungTableau …)`,
sorry-free).  The remaining content is then the **structural branching rule**
`numStandardYoungTableaux μ = ∑_{removable corners c of μ} numStandardYoungTableaux (μ ∖ c)`, proved by the
"delete the cell holding `|μ|`" bijection on `StandardYoungTableau`.  Mathlib's `YoungDiagram` exposes
`ofRowLens` / `rowLens` / `mem_cells` but **no** corner / erase / `SDiff` API, so that corner-removal of a
diagram (and `ofRowLens (removeCorner l c) ↔ (ofRowLens l hl) ∖ c`) must be built first — a multi-session
piece, but on the clean `YoungDiagram` structure rather than on flat lists. -/
theorem cornerRecursion (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a)
    (hne : l ≠ []) :
    numSYTenum l = ((corners l).map (fun c => numSYTenum (removeCorner l c))).sum := by
  -- Ref: [sagan2001] https://doi.org/10.1007/978-1-4757-6804-6 (branching rule for SYT; the largest
  -- entry sits in a removable corner, deletion is a bijection — §3.x).  Route: via the structural
  -- bridge numSYTenum_eq_numStandardYoungTableaux to the YoungDiagram branching rule (see docstring).
  sorry

/-- **(GNW hook) hook-summation identity.**  Summing the hook-product ratios over the removable corners
gives the cell count: `∑_{corners c} ∏h_λ / ∏h_{λ∖c} = n`.  This is the partial-fractions / telescoping
core of the Greene–Nijenhuis–Wilf proof — the rational identity that turns the count recursion into the
hook-length formula. -/
theorem gnwHookIdentity (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a)
    (hne : l ≠ []) :
    ((corners l).map (fun c => (prodHooks l : ℚ) / (prodHooks (removeCorner l c) : ℚ))).sum
      = (sz l : ℚ) := by
  -- Ref: [sagan2001] https://doi.org/10.1007/978-1-4757-6804-6 (Greene–Nijenhuis–Wilf hook walk; the
  -- corner hook-ratio sum equals n — §3.x, partial fractions).  Self-contained ℚ identity.
  sorry

/-! ## The sorry-free reduction: corner recursion + GNW hook identity ⟹ HLF

Strong induction on `n = sz l` combining `cornerRecursion` and `gnwHookIdentity`.  Everything below is
machine-checked; the *only* unproved inputs are the two identities above. -/

/-- Strong-induction core: `#SYT(λ) = n! / ∏h_λ` over `ℚ`, conditional on the two GNW identities. -/
private theorem numSYTenum_eq_div_aux :
    ∀ (n : ℕ) (l : List ℕ), sz l = n → List.Sorted (· ≥ ·) l → (∀ a ∈ l, 0 < a) →
      (numSYTenum l : ℚ) = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro l hsz hl hpos
    rcases eq_or_ne l [] with hnil | hne
    · subst hnil
      have h1 : numSYTenum [] = 1 := by decide
      have h2 : prodHooks [] = 1 := by decide
      simp [h1, h2, sz]
    · -- inductive step
      have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
      have hphQ : (prodHooks l : ℚ) ≠ 0 := by exact_mod_cast hph.ne'
      have hn1 : 1 ≤ n := by
        rcases l with _ | ⟨a, t⟩
        · exact absurd rfl hne
        · have := hpos a (List.mem_cons_self ..)
          rw [← hsz]; unfold sz; rw [List.sum_cons]; omega
      have hcr := cornerRecursion l hl hpos hne
      have hgnw := gnwHookIdentity l hl hpos hne
      -- value of the inner ∑ (∏h_{λ∖c})⁻¹
      have hSval : ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum
          = (sz l : ℚ) / prodHooks l := by
        have hg : (prodHooks l : ℚ)
            * ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum = (sz l : ℚ) := by
          rw [← sum_map_const_mul, ← hgnw]
          apply congrArg List.sum
          apply List.map_congr_left
          intro c _
          rw [div_eq_mul_inv]
        rw [eq_div_iff hphQ, mul_comm]
        exact hg
      -- n! = n · (n−1)!
      have hfact : (n.factorial : ℚ) = (n : ℚ) * ((n - 1).factorial : ℚ) := by
        rcases n with _ | m
        · omega
        · simp only [Nat.add_sub_cancel, Nat.factorial_succ]; push_cast; ring
      calc (numSYTenum l : ℚ)
          = ((corners l).map (fun c => (numSYTenum (removeCorner l c) : ℚ))).sum := by
            rw [hcr]; push_cast; rw [List.map_map]; rfl
        _ = ((corners l).map
              (fun c => ((n - 1).factorial : ℚ) * (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum := by
            apply congrArg List.sum
            apply List.map_congr_left
            intro c hc
            have hcorner := mem_corners hc
            have hszc1 : sz (removeCorner l c) + 1 = sz l :=
              sz_removeCorner l c hcorner.1 (getD_pos_of_corner hpos hcorner)
            have hszc : sz (removeCorner l c) = n - 1 := by omega
            have hmlt : sz (removeCorner l c) < n := by omega
            have hihc := ih (sz (removeCorner l c)) hmlt (removeCorner l c) rfl
              (sorted_removeCorner l c hl hcorner) (removeCorner_pos l c)
            rw [hihc, hszc, div_eq_mul_inv]
        _ = ((n - 1).factorial : ℚ)
              * ((corners l).map (fun c => (prodHooks (removeCorner l c) : ℚ)⁻¹)).sum := by
            rw [sum_map_const_mul]
        _ = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) := by
            rw [hSval, hsz, hfact]; field_simp

/-- **#SYT(λ) = n!/∏h_λ over `ℚ`** — conditional on `cornerRecursion` + `gnwHookIdentity`. -/
theorem numSYTenum_eq_factorial_div (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    (numSYTenum l : ℚ) = ((sz l).factorial : ℚ) / (prodHooks l : ℚ) :=
  numSYTenum_eq_div_aux (sz l) l rfl hl hpos

/-- **Divisor-free HLF `#SYT(λ) · ∏h_λ = n!`** (over `ℕ`) — conditional on the two GNW identities.
This is exactly the divisor-free Frame–Robinson–Thrall form; proving the two GNW identities makes it
unconditional. -/
theorem numSYTenum_mul_prodHooks (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * prodHooks l = (sz l).factorial := by
  have hQ := numSYTenum_eq_factorial_div l hl hpos
  have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
  have hphQ : (prodHooks l : ℚ) ≠ 0 := by exact_mod_cast hph.ne'
  have hmul : (numSYTenum l : ℚ) * prodHooks l = ((sz l).factorial : ℚ) := by
    rw [hQ]; field_simp
  exact_mod_cast hmul

/-- **General HLF `#SYT(λ) = dimHLF λ`** via the GNW route — conditional on the two GNW identities.
Same statement as `SYTHookFormulaGeneral.numSYTenum_eq_dimHLF`, but routed through the self-contained
corner recursion rather than the Mathlib-blocked Aitken determinant. -/
theorem numSYTenum_eq_dimHLF_gnw (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l = dimHLF l := by
  have hkey := numSYTenum_mul_prodHooks l hl hpos
  have hph : 0 < prodHooks l := prodHooks_pos l hl hpos
  unfold dimHLF
  rw [← hkey, Nat.mul_div_cancel _ hph]

/-- **The Aitken/Frobenius determinant identity, derived from the GNW route.**  Identical statement to
the *blocked* `SYTHookFormulaGeneral.dimAitkenIdentity` (which needs Specht/RSK infra absent from the
pinned Mathlib), here obtained with no determinant infrastructure: combine the divisor-free HLF
`#SYT·∏h = n!` with the merged hook-product identity (i) `∏h · betaProdGap = betaFactProd`. -/
theorem dimAitkenIdentity_of_gnw (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    numSYTenum l * betaFactProd l = (sz l).factorial * betaProdGap l := by
  have hi := prodHooks_mul_betaProdGap l hl
  have hkey := numSYTenum_mul_prodHooks l hl hpos
  rw [← hi, ← mul_assoc, hkey]

end QOU.Mathlib.SYTEnum
