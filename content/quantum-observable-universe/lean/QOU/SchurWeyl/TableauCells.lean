import QOU.SchurWeyl.HoefsmitRep

/-!
# `QOU.SchurWeyl.TableauCells` — inverting the entry map, and the axial distance of
consecutive entries (bean `qou-gjg6`, step (i) infrastructure)

The general-`λ` Hoefsmit construction indexes a basis by `SYT λ` and, for each generator
`σ_i`, reads off the **axial distance between the cells holding the entries `i` and `i+1`**.
That requires going *backwards* along the filling — from an entry to its cell — which the
`StandardYoungTableau` structure supports (its `bijOn` field says the entry map is a
bijection from cells onto `{1,…,|μ|}`) but does not expose.  This file exposes it.

## What is delivered

* `cellOf T k` — the cell of `T` holding entry `k`, with `cellOf_mem`, `entry_cellOf`
  (the round trip on entries) and `cellOf_unique` (the round trip on cells).  Total: off-range `k` is sent to `(0,0)`, so no subtype bookkeeping propagates
  into the construction.
* `axialDist T k = axialDistance (cellOf T k) (cellOf T (k+1))` — the parameter that
  selects the seminormal block of `σ_k`.
* `axialDist_of_sameRow` / `axialDist_of_sameCol` — **the two size-`1` orbit cases**:
  consecutive entries sharing a row have axial distance `+1`, and sharing a column, `-1`.
  Via `seminormalParam_one` / `seminormalParam_neg_one` these are exactly the scalar
  eigenvalues `q` and `-q⁻¹`.

The proofs of the last two are the reason they are worth recording: sharing a row forces
the two cells to be **adjacent**, because a cell strictly between them would carry an entry
strictly between two consecutive integers.  That is where standardness (as opposed to mere
semistandardness) does the work.

* `swapTableau T k` — the **`s_k`-action**: the tableau with the entries `k` and `k+1`
  exchanged, proved again standard under `SwapAdmissible` (the two cells share neither a
  row nor a column, which by the adjacency lemmas is exactly the complement of the two
  size-`1` cases).  `swapAdmissible_swapTableau` and `swapTableau_involutive` make
  `{T, s_k·T}` a genuine two-element orbit with no side hypotheses — this is the size-`2`
  orbit of the construction.
* `swapTableau_comm` — **far commutation**: the `s_k`- and `s_l`-actions commute for
  `|k - l| ≥ 2`, the tableau-level form of `σ_k σ_l = σ_l σ_k`.  With
  `cellOf_swapTableau_of_ne` (a far swap moves no cell outside `{l, l+1}`) and
  `swapAdmissible_of_far`, which derives the admissibility the use site needs.

## Scope

Step (ii) — assembling the block-diagonal generator matrices from the orbits (an
enumeration `Fin (dLambda λ) → SYT λ`, the orbit trichotomy as a decidable case split,
and the assembly itself) — is **not** here and remains open under bean `qou-gjg6`, and
with it the `-- Ref:`-cited `sorry` in `hoefsmit_seminormal_rep`.  What this file
supplies is everything that step needs about individual tableaux: the entry→cell
inverse, the axial distance, the two scalar cases, and the size-`2` orbit partner.

Refs:
- [hoefsmit1974] Hoefsmit, PhD thesis (UBC 1974) — the seminormal form.
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373 — the axial-distance formulas.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

namespace TableauCells

variable {μ : YoungDiagram}

open Classical in
/-- **The cell holding entry `k`.**  The `StandardYoungTableau` field `bijOn` makes the
entry map a bijection from the cells onto `{1,…,|μ|}`; this is its inverse, made total by
sending an out-of-range `k` to `(0,0)`. -/
noncomputable def cellOf (T : StandardYoungTableau μ) (k : ℕ) : ℕ × ℕ :=
  if h : ∃ c : ℕ × ℕ, c ∈ μ.cells ∧ T.entry c.1 c.2 = k then h.choose else (0, 0)

/-- For an in-range `k`, `cellOf` really does produce a cell of `μ` carrying entry `k`. -/
theorem cellOf_spec (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) :
    cellOf T k ∈ μ.cells ∧ T.entry (cellOf T k).1 (cellOf T k).2 = k := by
  classical
  have hsurj := T.bijOn.surjOn hk
  obtain ⟨c, hc, hck⟩ := hsurj
  have hex : ∃ c : ℕ × ℕ, c ∈ μ.cells ∧ T.entry c.1 c.2 = k :=
    ⟨c, by simpa using hc, hck⟩
  rw [cellOf, dif_pos hex]
  exact hex.choose_spec

theorem cellOf_mem (T : StandardYoungTableau μ) {k : ℕ} (hk : k ∈ Set.Icc 1 μ.cells.card) :
    cellOf T k ∈ μ.cells := (cellOf_spec T hk).1

@[simp] theorem entry_cellOf (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) :
    T.entry (cellOf T k).1 (cellOf T k).2 = k := (cellOf_spec T hk).2

/-- **Uniqueness**: any cell carrying entry `k` *is* `cellOf T k`.  This is the inverse
round trip, and it is what lets one compute `cellOf` from an explicit tableau. -/
theorem cellOf_unique (T : StandardYoungTableau μ) {k : ℕ} {c : ℕ × ℕ}
    (hc : c ∈ μ.cells) (hck : T.entry c.1 c.2 = k) : cellOf T k = c := by
  have hk : k ∈ Set.Icc 1 μ.cells.card := by
    rw [← hck]; exact T.mapsTo_cells (by simpa using hc)
  refine T.injOn_cells ?_ ?_ ?_
  · simpa using cellOf_mem T hk
  · simpa using hc
  · show T.entry (cellOf T k).1 (cellOf T k).2 = T.entry c.1 c.2
    rw [entry_cellOf T hk, hck]

/-- **The axial distance of the generator `σ_k`** in the tableau `T`: the content of the
cell holding `k+1` minus the content of the cell holding `k`.  This is the parameter that
selects the seminormal block (`seminormalParam`). -/
noncomputable def axialDist (T : StandardYoungTableau μ) (k : ℕ) : ℤ :=
  axialDistance (cellOf T k) (cellOf T (k + 1))

/-- **Consecutive entries in the same row sit in adjacent cells.**  A cell strictly between
them would have to carry an entry strictly between `k` and `k+1`, and there is no such
natural number.  This is the step where standardness — the filling being a bijection onto
an interval — is used, not merely semistandardness. -/
theorem sameRow_adjacent (T : StandardYoungTableau μ) {k i j₁ j₂ : ℕ}
    (h₁ : (i, j₁) ∈ μ) (h₂ : (i, j₂) ∈ μ)
    (hk₁ : T.entry i j₁ = k) (hk₂ : T.entry i j₂ = k + 1) : j₂ = j₁ + 1 := by
  have hlt : j₁ < j₂ := by
    by_contra hcon
    rcases Nat.lt_or_ge j₂ j₁ with h | h
    · have hrs : T.entry i j₂ < T.entry i j₁ := T.row_strict h h₁
      omega
    · have : j₁ = j₂ := by omega
      subst this
      omega
  by_contra hne
  have hmid : j₁ + 1 < j₂ := by omega
  have hcell : (i, j₁ + 1) ∈ μ := μ.up_left_mem (le_refl i) (by omega) h₂
  have hlo : T.entry i j₁ < T.entry i (j₁ + 1) := T.row_strict (by omega) hcell
  have hhi : T.entry i (j₁ + 1) < T.entry i j₂ := T.row_strict hmid h₂
  omega

/-- **Same-row orbit**: consecutive entries sharing a row have axial distance `+1`.  With
`seminormalParam_one` this is the scalar eigenvalue `q`. -/
theorem axialDist_of_sameRow (T : StandardYoungTableau μ) {k i j₁ j₂ : ℕ}
    (h₁ : (i, j₁) ∈ μ) (h₂ : (i, j₂) ∈ μ)
    (hk₁ : T.entry i j₁ = k) (hk₂ : T.entry i j₂ = k + 1) :
    axialDist T k = 1 := by
  have hadj : j₂ = j₁ + 1 := sameRow_adjacent T h₁ h₂ hk₁ hk₂
  subst hadj
  have e₁ : cellOf T k = (i, j₁) :=
    cellOf_unique T (by simpa using h₁) hk₁
  have e₂ : cellOf T (k + 1) = (i, j₁ + 1) :=
    cellOf_unique T (by simpa using h₂) hk₂
  simp only [axialDist, e₁, e₂, axialDistance, cellContent]
  push_cast
  ring

/-- **Consecutive entries in the same column sit in adjacent cells** — the column-strict
mirror of `sameRow_adjacent`. -/
theorem sameCol_adjacent (T : StandardYoungTableau μ) {k i₁ i₂ j : ℕ}
    (h₁ : (i₁, j) ∈ μ) (h₂ : (i₂, j) ∈ μ)
    (hk₁ : T.entry i₁ j = k) (hk₂ : T.entry i₂ j = k + 1) : i₂ = i₁ + 1 := by
  have hlt : i₁ < i₂ := by
    by_contra hcon
    rcases Nat.lt_or_ge i₂ i₁ with h | h
    · have hcs : T.entry i₂ j < T.entry i₁ j := T.toSsyt.col_strict h h₁
      omega
    · have : i₁ = i₂ := by omega
      subst this
      omega
  by_contra hne
  have hmid : i₁ + 1 < i₂ := by omega
  have hcell : (i₁ + 1, j) ∈ μ := μ.up_left_mem (by omega) (le_refl j) h₂
  have hlo : T.entry i₁ j < T.entry (i₁ + 1) j := T.toSsyt.col_strict (by omega) hcell
  have hhi : T.entry (i₁ + 1) j < T.entry i₂ j := T.toSsyt.col_strict hmid h₂
  omega

/-- **Same-column orbit**: consecutive entries sharing a column have axial distance `-1`.
With `seminormalParam_neg_one` this is the scalar eigenvalue `-q⁻¹`. -/
theorem axialDist_of_sameCol (T : StandardYoungTableau μ) {k i₁ i₂ j : ℕ}
    (h₁ : (i₁, j) ∈ μ) (h₂ : (i₂, j) ∈ μ)
    (hk₁ : T.entry i₁ j = k) (hk₂ : T.entry i₂ j = k + 1) :
    axialDist T k = -1 := by
  have hadj : i₂ = i₁ + 1 := sameCol_adjacent T h₁ h₂ hk₁ hk₂
  subst hadj
  have e₁ : cellOf T k = (i₁, j) :=
    cellOf_unique T (by simpa using h₁) hk₁
  have e₂ : cellOf T (k + 1) = (i₁ + 1, j) :=
    cellOf_unique T (by simpa using h₂) hk₂
  simp only [axialDist, e₁, e₂, axialDistance, cellContent]
  push_cast
  ring


/-! ## The `s_k`-action: swapping the entries `k` and `k+1`

The size-`2` orbits of the general construction are the pairs `{T, s_k·T}`.  This section
builds `s_k·T` and proves it is again standard — which holds exactly when the two cells
share neither a row nor a column (`SwapAdmissible`), the complement of the two size-`1`
cases settled above.
-/

/-- The transposition of the values `k` and `k+1`, as a map `ℕ → ℕ`. -/
def swapVal (k x : ℕ) : ℕ := if x = k then k + 1 else if x = k + 1 then k else x

@[simp] theorem swapVal_involutive (k x : ℕ) : swapVal k (swapVal k x) = x := by
  unfold swapVal; split_ifs <;> omega

/-- The entry function of `s_k · T`. -/
def swapEntry (T : StandardYoungTableau μ) (k i j : ℕ) : ℕ := swapVal k (T.entry i j)

/-- **Admissibility of the `s_k`-swap**: the cells holding `k` and `k+1` share neither a
row nor a column.  By `sameRow_adjacent` / `sameCol_adjacent` this is exactly the
complement of the two size-`1` orbit cases, so it is the size-`2` condition. -/
def SwapAdmissible (T : StandardYoungTableau μ) (k : ℕ) : Prop :=
  (cellOf T k).1 ≠ (cellOf T (k + 1)).1 ∧ (cellOf T k).2 ≠ (cellOf T (k + 1)).2

/-- Under admissibility no row carries both `k` and `k+1`. -/
theorem not_sameRow_of_admissible {T : StandardYoungTableau μ} {k : ℕ}
    (h : SwapAdmissible T k) {i j₁ j₂ : ℕ} (h₁ : (i, j₁) ∈ μ) (h₂ : (i, j₂) ∈ μ) :
    ¬(T.entry i j₁ = k ∧ T.entry i j₂ = k + 1) := by
  rintro ⟨hk₁, hk₂⟩
  exact h.1 (by rw [cellOf_unique T (by simpa using h₁) hk₁,
    cellOf_unique T (by simpa using h₂) hk₂])

/-- Under admissibility no column carries both `k` and `k+1`. -/
theorem not_sameCol_of_admissible {T : StandardYoungTableau μ} {k : ℕ}
    (h : SwapAdmissible T k) {i₁ i₂ j : ℕ} (h₁ : (i₁, j) ∈ μ) (h₂ : (i₂, j) ∈ μ) :
    ¬(T.entry i₁ j = k ∧ T.entry i₂ j = k + 1) := by
  rintro ⟨hk₁, hk₂⟩
  exact h.2 (by rw [cellOf_unique T (by simpa using h₁) hk₁,
    cellOf_unique T (by simpa using h₂) hk₂])

/-- `s_k · T` as a semistandard tableau.  Rows stay weakly increasing and columns strictly
increasing: the swap can only disturb the order at the two swapped values, and admissibility
rules out the one configuration that would — `k` and `k+1` in a common row or column. -/
def swapSsyt (T : StandardYoungTableau μ) (k : ℕ) (hk : 1 ≤ k)
    (hadm : SwapAdmissible T k) : SemistandardYoungTableau μ where
  entry := swapEntry T k
  zeros' := by
    intro i j hmem
    have h0 : T.entry i j = 0 := T.toSsyt.zeros hmem
    show swapVal k (T.entry i j) = 0
    rw [h0]
    unfold swapVal
    have hk0 : (0 : ℕ) ≠ k := by omega
    rw [if_neg hk0, if_neg (by omega : (0 : ℕ) ≠ k + 1)]
  row_weak' := by
    intro i j₁ j₂ hj hmem
    have hmem1 : (i, j₁) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hj) hmem
    have hab : T.entry i j₁ < T.entry i j₂ := T.row_strict hj hmem
    have hno := not_sameRow_of_admissible hadm hmem1 hmem
    simp only [swapEntry, swapVal]
    split_ifs <;> omega
  col_strict' := by
    intro i₁ i₂ j hi hmem
    have hmem1 : (i₁, j) ∈ μ := μ.up_left_mem (le_of_lt hi) (le_refl j) hmem
    have hab : T.entry i₁ j < T.entry i₂ j := T.toSsyt.col_strict hi hmem
    have hno := not_sameCol_of_admissible hadm hmem1 hmem
    simp only [swapEntry, swapVal]
    split_ifs <;> omega

/-- The value-swap is a bijection of `{1,…,n}` onto itself when both `k` and `k+1` lie in
range — it is an involution mapping the interval into itself. -/
theorem bijOn_swapVal {k n : ℕ} (hk : 1 ≤ k) (hkn : k + 1 ≤ n) :
    Set.BijOn (swapVal k) (Set.Icc 1 n) (Set.Icc 1 n) := by
  have hmaps : Set.MapsTo (swapVal k) (Set.Icc 1 n) (Set.Icc 1 n) := by
    intro x hx
    rw [Set.mem_Icc] at hx ⊢
    unfold swapVal
    split_ifs <;> omega
  exact Set.InvOn.bijOn ⟨fun x _ => swapVal_involutive k x, fun y _ => swapVal_involutive k y⟩
    hmaps hmaps

/-- **`s_k · T` — the swapped tableau, again standard.**  This is the size-`2` orbit
partner of `T`.  Standardness needs both that the order survives (`swapSsyt`) and that the
filling is still a bijection onto `{1,…,|μ|}`, which holds because the value-swap is an
involution of that interval. -/
def swapTableau (T : StandardYoungTableau μ) (k : ℕ) (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) : StandardYoungTableau μ where
  toSsyt := swapSsyt T k hk hadm
  bijOn := (bijOn_swapVal hk hkn).comp T.bijOn

@[simp] theorem swapTableau_entry (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) (i j : ℕ) :
    (swapTableau T k hk hkn hadm).entry i j = swapVal k (T.entry i j) := rfl

/-- Extensionality for standard tableaux: equal entries give equal tableaux. -/
private theorem syt_ext {T₁ T₂ : StandardYoungTableau μ}
    (h : ∀ i j, T₁.toSsyt.entry i j = T₂.toSsyt.entry i j) : T₁ = T₂ := by
  have hs : T₁.toSsyt = T₂.toSsyt := SemistandardYoungTableau.ext h
  cases T₁; cases T₂; cases hs; rfl

/-- **The swap exchanges the cells of `k` and `k+1`** — the cell of `k` in `s_k·T` is the
cell of `k+1` in `T`. -/
theorem cellOf_swapTableau_self (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    cellOf (swapTableau T k hk hkn hadm) k = cellOf T (k + 1) := by
  have hk1 : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  refine cellOf_unique _ (cellOf_mem T hk1) ?_
  show swapVal k (T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2) = k
  rw [entry_cellOf T hk1]
  unfold swapVal
  rw [if_neg (by omega : ¬(k + 1 = k)), if_pos rfl]

/-- The mirror: the cell of `k+1` in `s_k·T` is the cell of `k` in `T`. -/
theorem cellOf_swapTableau_succ (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    cellOf (swapTableau T k hk hkn hadm) (k + 1) = cellOf T k := by
  have hk0 : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  refine cellOf_unique _ (cellOf_mem T hk0) ?_
  show swapVal k (T.entry (cellOf T k).1 (cellOf T k).2) = k + 1
  rw [entry_cellOf T hk0]
  unfold swapVal
  rw [if_pos rfl]

/-- **Admissibility is symmetric**: if the swap at `k` is admissible for `T` then it is
admissible for `s_k·T`.  Derived, not assumed — the swap merely exchanges the two cells,
so "different row and different column" is preserved. -/
theorem swapAdmissible_swapTableau (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    SwapAdmissible (swapTableau T k hk hkn hadm) k := by
  refine ⟨?_, ?_⟩
  · rw [cellOf_swapTableau_self, cellOf_swapTableau_succ]
    exact hadm.1.symm
  · rw [cellOf_swapTableau_self, cellOf_swapTableau_succ]
    exact hadm.2.symm

/-- **The swap is an involution**: applying `s_k` twice returns `T`.  Together with
`swapAdmissible_swapTableau` this makes `{T, s_k·T}` a genuine two-element orbit, with no
side hypothesis about the swapped tableau. -/
theorem swapTableau_involutive (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    swapTableau (swapTableau T k hk hkn hadm) k hk hkn
        (swapAdmissible_swapTableau T hk hkn hadm) = T := by
  refine syt_ext (fun i j => ?_)
  show swapVal k (swapVal k (T.entry i j)) = T.entry i j
  exact swapVal_involutive k (T.entry i j)

/-! ## Far commutation of the `s_k`-actions

For `|k - l| ≥ 2` the pairs `{k, k+1}` and `{l, l+1}` are disjoint, so the two swaps
commute — the generator relation `σ_k σ_l = σ_l σ_k` at the level of tableaux.  This is
what the far-commutation relation of the representation will be read off from.
-/

/-- Disjoint value-transpositions commute. -/
theorem swapVal_comm {k l : ℕ} (h : k + 1 < l ∨ l + 1 < k) (x : ℕ) :
    swapVal k (swapVal l x) = swapVal l (swapVal k x) := by
  unfold swapVal; split_ifs <;> omega

/-- Applying `s_l` does not move the cell of an entry outside `{l, l+1}`. -/
theorem cellOf_swapTableau_of_ne (T : StandardYoungTableau μ) {k l : ℕ} (hl : 1 ≤ l)
    (hln : l + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T l)
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hkl : k ≠ l) (hkl' : k ≠ l + 1) :
    cellOf (swapTableau T l hl hln hadm) k = cellOf T k := by
  refine cellOf_unique _ (cellOf_mem T hk) ?_
  show swapVal l (T.entry (cellOf T k).1 (cellOf T k).2) = k
  rw [entry_cellOf T hk]
  unfold swapVal
  rw [if_neg hkl, if_neg hkl']

/-- **Admissibility at `k` survives a far swap at `l`**: `s_l` leaves the cells of `k` and
`k+1` alone, so the "different row and different column" condition is untouched. -/
theorem swapAdmissible_of_far (T : StandardYoungTableau μ) {k l : ℕ} (hl : 1 ≤ l)
    (hln : l + 1 ≤ μ.cells.card) (hadml : SwapAdmissible T l)
    (hkr : k ∈ Set.Icc 1 μ.cells.card) (hkr' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k) (hadmk : SwapAdmissible T k) :
    SwapAdmissible (swapTableau T l hl hln hadml) k := by
  have e₁ : cellOf (swapTableau T l hl hln hadml) k = cellOf T k :=
    cellOf_swapTableau_of_ne T hl hln hadml hkr (by omega) (by omega)
  have e₂ : cellOf (swapTableau T l hl hln hadml) (k + 1) = cellOf T (k + 1) :=
    cellOf_swapTableau_of_ne T hl hln hadml hkr' (by omega) (by omega)
  exact ⟨by rw [e₁, e₂]; exact hadmk.1, by rw [e₁, e₂]; exact hadmk.2⟩

/-- **A far swap leaves the axial distance alone.**  `s_l` moves no cell outside
`{l, l+1}`, so the parameter `σ_k` reads off is unchanged.  Together with
`swapAdmissible_far_iff` this says a far swap leaves *every* input to `σ_k`'s row rule
untouched — which is what a matrix-level far-commutation proof needs. -/
theorem axialDist_swapTableau_of_far (T : StandardYoungTableau μ) {k l : ℕ} (hl : 1 ≤ l)
    (hln : l + 1 ≤ μ.cells.card) (hadml : SwapAdmissible T l)
    (hkr : k ∈ Set.Icc 1 μ.cells.card) (hkr' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k) :
    axialDist (swapTableau T l hl hln hadml) k = axialDist T k := by
  unfold axialDist
  rw [cellOf_swapTableau_of_ne T hl hln hadml hkr (by omega) (by omega),
    cellOf_swapTableau_of_ne T hl hln hadml hkr' (by omega) (by omega)]

/-- **Admissibility at `k` is *unchanged* by a far swap at `l`** — both directions.
`swapAdmissible_of_far` gives the forward implication; the converse matters just as much,
because a matrix-level argument has to know that a far swap cannot *create* a size-`2`
orbit where there was a scalar. -/
theorem swapAdmissible_far_iff (T : StandardYoungTableau μ) {k l : ℕ} (hl : 1 ≤ l)
    (hln : l + 1 ≤ μ.cells.card) (hadml : SwapAdmissible T l)
    (hkr : k ∈ Set.Icc 1 μ.cells.card) (hkr' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k) :
    SwapAdmissible (swapTableau T l hl hln hadml) k ↔ SwapAdmissible T k := by
  have e₁ : cellOf (swapTableau T l hl hln hadml) k = cellOf T k :=
    cellOf_swapTableau_of_ne T hl hln hadml hkr (by omega) (by omega)
  have e₂ : cellOf (swapTableau T l hl hln hadml) (k + 1) = cellOf T (k + 1) :=
    cellOf_swapTableau_of_ne T hl hln hadml hkr' (by omega) (by omega)
  unfold SwapAdmissible
  rw [e₁, e₂]

/-- **The `s_k`-actions commute at far distance** — `s_k s_l · T = s_l s_k · T` for
`|k - l| ≥ 2`.  This is the tableau-level form of `σ_k σ_l = σ_l σ_k`. -/
theorem swapTableau_comm (T : StandardYoungTableau μ) {k l : ℕ} (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hkn : k + 1 ≤ μ.cells.card) (hln : l + 1 ≤ μ.cells.card)
    (hfar : k + 1 < l ∨ l + 1 < k)
    (hadmk : SwapAdmissible T k) (hadml : SwapAdmissible T l) :
    swapTableau (swapTableau T l hl hln hadml) k hk hkn
        (swapAdmissible_of_far T hl hln hadml ⟨hk, by omega⟩ ⟨by omega, hkn⟩ hfar hadmk)
      = swapTableau (swapTableau T k hk hkn hadmk) l hl hln
        (swapAdmissible_of_far T hk hkn hadmk ⟨hl, by omega⟩ ⟨by omega, hln⟩
          (by omega) hadml) := by
  refine syt_ext (fun i j => ?_)
  show swapVal k (swapVal l (T.entry i j)) = swapVal l (swapVal k (T.entry i j))
  exact swapVal_comm hfar (T.entry i j)


/-! ## The orbit trichotomy

For consecutive entries `k, k+1` exactly one of three things happens, and this is the
decidable case split the block assembly of step (ii) runs on: the two cells share a row
(a size-`1` orbit, axial distance `+1`, scalar `q`), share a column (size `1`, distance
`-1`, scalar `-q⁻¹`), or share neither (`SwapAdmissible` — a size-`2` orbit, a
`seminormalBlock`).  There is no fourth case, and no two of them overlap: the cells are
distinct because the entries are, so they cannot agree in both coordinates.
-/

/-- The cells of two distinct entries are distinct. -/
theorem cellOf_ne (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card) :
    cellOf T k ≠ cellOf T (k + 1) := by
  intro h
  have h₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have h₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  rw [h] at h₁
  omega

/-- **The orbit trichotomy.**  Exactly one of: the two cells share a row (axial distance
`+1`), share a column (`-1`), or share neither (`SwapAdmissible`).  This is the case split
the generator assembly runs on — the first two give the scalar entries `q` and `-q⁻¹`, the
third a `seminormalBlock`. -/
theorem axialDist_trichotomy (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card) :
    axialDist T k = 1 ∨ axialDist T k = -1 ∨ SwapAdmissible T k := by
  have hm₁ : cellOf T k ∈ μ.cells := cellOf_mem T hk
  have hm₂ : cellOf T (k + 1) ∈ μ.cells := cellOf_mem T hk'
  have hμ₁ : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₁
  have hμ₂ : ((cellOf T (k + 1)).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₂
  have he₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have he₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  by_cases hrow : (cellOf T k).1 = (cellOf T (k + 1)).1
  · left
    exact axialDist_of_sameRow T hμ₁ (by rw [← hrow] at hμ₂; exact hμ₂) he₁
      (by rw [← hrow] at he₂; exact he₂)
  · by_cases hcol : (cellOf T k).2 = (cellOf T (k + 1)).2
    · right; left
      exact axialDist_of_sameCol T hμ₁ (by rw [← hcol] at hμ₂; exact hμ₂) he₁
        (by rw [← hcol] at he₂; exact he₂)
    · exact Or.inr (Or.inr ⟨hrow, hcol⟩)

/-- **The axial distance of a generator is never zero** — consecutive entries never sit on
the same diagonal.

If they did, the cell completing their rectangle would be forced to carry an entry strictly
between `k` and `k+1`.  Concretely, if `k` sits at `(i₁, j₁)` and `k+1` at `(i₂, j₂)` with
equal contents `j₁ - i₁ = j₂ - i₂`, then the two cells are strictly ordered in *both*
coordinates, and the corner cell (`(i₁, j₂)` in one orientation, `(i₂, j₁)` in the other)
lies in `μ` by up-left closure and is squeezed between them.

This is what keeps `seminormalParam q (axialDist T k)` away from the pole of
`(q - q⁻¹)/(1 - q^{-2d})` at `d = 0`, so the parameter is defined at every generator and
every tableau. -/
theorem axialDist_ne_zero (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card) :
    axialDist T k ≠ 0 := by
  have hm₁ : cellOf T k ∈ μ.cells := cellOf_mem T hk
  have hm₂ : cellOf T (k + 1) ∈ μ.cells := cellOf_mem T hk'
  have hμ₁ : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₁
  have hμ₂ : ((cellOf T (k + 1)).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₂
  have he₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have he₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  intro hzero
  -- equal contents: `j₁ - i₁ = j₂ - i₂` over `ℤ`
  have hcontent : ((cellOf T (k + 1)).2 : ℤ) - ((cellOf T (k + 1)).1 : ℤ)
      = ((cellOf T k).2 : ℤ) - ((cellOf T k).1 : ℤ) := by
    have := hzero
    simp only [axialDist, axialDistance, cellContent] at this
    omega
  -- the cells are distinct, so the rows differ; with equal contents the columns follow
  have hne : cellOf T k ≠ cellOf T (k + 1) := cellOf_ne T hk hk'
  have hrow : (cellOf T k).1 ≠ (cellOf T (k + 1)).1 := by
    intro h
    exact hne (Prod.ext h (by omega))
  rcases Nat.lt_or_ge (cellOf T k).1 (cellOf T (k + 1)).1 with hlt | hge
  · -- `k` is strictly up-left of `k+1`: the corner `(i₁, j₂)` is squeezed
    have hjlt : (cellOf T k).2 < (cellOf T (k + 1)).2 := by omega
    have hcorner : ((cellOf T k).1, (cellOf T (k + 1)).2) ∈ μ :=
      μ.up_left_mem (le_of_lt hlt) (le_refl _) hμ₂
    have hlo : T.entry (cellOf T k).1 (cellOf T k).2
        < T.entry (cellOf T k).1 (cellOf T (k + 1)).2 := T.row_strict hjlt hcorner
    have hhi : T.entry (cellOf T k).1 (cellOf T (k + 1)).2
        < T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 :=
      T.toSsyt.col_strict hlt hμ₂
    omega
  · -- `k+1` is strictly up-left of `k`: the corner `(i₂, j₁)` is squeezed the other way
    have hilt : (cellOf T (k + 1)).1 < (cellOf T k).1 := by omega
    have hjlt : (cellOf T (k + 1)).2 < (cellOf T k).2 := by omega
    have hcorner : ((cellOf T (k + 1)).1, (cellOf T k).2) ∈ μ :=
      μ.up_left_mem (le_of_lt hilt) (le_refl _) hμ₁
    have hlo : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2
        < T.entry (cellOf T (k + 1)).1 (cellOf T k).2 := T.row_strict hjlt hcorner
    have hhi : T.entry (cellOf T (k + 1)).1 (cellOf T k).2
        < T.entry (cellOf T k).1 (cellOf T k).2 := T.toSsyt.col_strict hilt hμ₁
    omega

/-- **The swap negates the axial distance.**  `s_k` exchanges the cells of `k` and `k+1`
(`cellOf_swapTableau_self` / `_succ`) and `axialDistance` is antisymmetric, so the pair
`{T, s_k·T}` carries the two distances `d` and `-d`.

This is what makes the size-`2` block a `seminormalBlock`: its diagonal is
`(a(d), a(-d))`, whose entries sum to `q - q⁻¹` by `seminormalParam_add_neg`.  Without it
the two rows of a pair would be unrelated and the quadratic relation could not close. -/
@[simp] theorem axialDist_swapTableau (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    axialDist (swapTableau T k hk hkn hadm) k = -axialDist T k := by
  unfold axialDist
  rw [cellOf_swapTableau_self T hk hkn hadm, cellOf_swapTableau_succ T hk hkn hadm]
  exact axialDistance_antisymm _ _

end TableauCells

end QOU.SchurWeyl
