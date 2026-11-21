import QOU.BraidsAndKnots.HookArmLeg

/-!
# Depth-1 (`v = n − 1`) hook classification, confinement, enumeration, and shape data

Completes beans **D1 (`qou-ckyw`)**, **D3 (`qou-x3u6`)**, **D4 (`qou-q621`)**, and **D5 (`qou-amf8`)**
for the second `(TAIL)` instance `ν_{n−1} = Cov_Planch(N_{n−1}, ω₃)`
(`computations/deltalambda/wlambda_covariance_epic_A2_tail_second_instance_probe.py`,
`computations/deltalambda/wlambda_covariance_epic_A2_nu_nm1_closed_form.py`):

1. **D1 (`qou-ckyw`) — Carrier classification at `v = n − 1`**:
   `HookArmLeg.carrier_mem_three` confines any cell `p ∈ cells l` with `hookLen l p + 1 = l.sum`
   to `(0,0)`, `(0,1)` or `(1,0)`. Here we prove that on any sorted positive partition `l`:
   - `p = (0,1)` forces the single row `l = [l.sum]` (`2 ≤ l.sum`)
     (`eq_singleRow_of_carrier_zero_one`);
   - `p = (1,0)` forces the single column `l = List.replicate l.sum 1` (`2 ≤ l.sum`)
     (`eq_singleCol_of_carrier_one_zero`);
   - `p = (0,0)` forces the two-corner shape
     `l = l.headD 0 :: 2 :: List.replicate (l.length − 2) 1` (`2 ≤ l.headD 0`, `2 ≤ l.length`)
     (`eq_twoCorner_of_carrier_zero_zero`);
   bundled as `carrier_classification_depth_one`.

2. **D3 (`qou-x3u6`) — `hookCount` confinement in count form at `v = n − 1`**:
   Each of the three depth-1 carrier shapes has `hookCount l (l.sum − 1) = 1`
   (`hookCount_depthOne_singleRow`, `hookCount_depthOne_singleCol`,
   `hookCount_depthOne_twoCorner`), and every other sorted positive partition has
   `hookCount l (l.sum − 1) = 0` (`hookCount_sub_one_eq_zero_of_not_isDepthOneShape`).

3. **D4 (`qou-q621`) — Depth-1 enumeration inside `partsOf`**:
   Defines `twoCornerShapes k` and `depthOneShapes k = [k] :: 1^k :: twoCornerShapes k`, proves
   membership in `partsOf k` (`depthOneShapes_mem_partsOf`), `Nodup` (`depthOneShapes_nodup`),
   cardinality `k − 1` (`depthOneShapes_length`), the converse completeness
   (`mem_depthOneShapes_of_isDepthOneShape`), and the Plancherel sum restriction
   (`sum_partsOf_eq_sum_depthOneShapes`, `depthOne_mixedMoment_eq_depthOneShapes_sum`).

4. **D5 (`qou-amf8`) — Depth-1 shape data (`contentSq`, `omega3`, `hookProd`, `sytDim`)**:
   Proves `contentSq_twoCorner`, `six_mul_omega3_twoCorner`, `hookProd_twoCorner`,
   `sytDim_twoCorner`, `sytDim_singleRow`, and `sytDim_singleCol`.
-/

namespace QOU.BraidsAndKnots.DepthOneHookClassification

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.HookArmLeg

/-! ## Basic shape helpers for single row, single column, and two-corner partitions -/

/-- Every entry of `List.replicate c 1` is positive, so `countP (0 < ·)` equals `c`. -/
theorem countP_pos_replicate_one :
    ∀ c : ℕ, (List.replicate c 1).countP (fun x => decide (0 < x)) = c := by
  intro c
  induction c with
  | zero => rfl
  | succ c ih =>
      rw [List.replicate_succ, List.countP_cons, ih]
      rfl

/-- The single-row partition `[n]` (`1 ≤ n`) is weakly decreasing. -/
theorem sorted_singleRow (n : ℕ) (hn : 1 ≤ n) : ([n] : List ℕ).Sorted (· ≥ ·) :=
  sorted_hookShape n 0 hn

/-- The single-column partition `List.replicate n 1` is weakly decreasing. -/
theorem sorted_singleCol (n : ℕ) : (List.replicate n 1).Sorted (· ≥ ·) := by
  cases n with
  | zero => exact List.sorted_nil
  | succ m => exact sorted_hookShape 1 m (Nat.le_refl 1)

/-- A two-corner partition `a :: 2 :: List.replicate c 1` with `2 ≤ a` is weakly decreasing. -/
theorem sorted_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    (a :: 2 :: List.replicate c 1).Sorted (· ≥ ·) := by
  rw [List.sorted_cons]
  refine ⟨?_, sorted_hookShape 2 c (by omega)⟩
  intro b hb
  rcases List.mem_cons.mp hb with rfl | hbc
  · exact ha
  · have hb1 : b = 1 := List.eq_of_mem_replicate hbc
    omega

/-- The size of `a :: 2 :: List.replicate c 1` is `a + c + 2`. -/
theorem sum_twoCorner (a c : ℕ) :
    (a :: 2 :: List.replicate c 1).sum = a + c + 2 := by
  rw [List.sum_cons, List.sum_cons, sum_replicate_one c]
  omega

/-- Every part of `a :: 2 :: List.replicate c 1` (`2 ≤ a`) is positive. -/
theorem pos_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    ∀ x ∈ (a :: 2 :: List.replicate c 1), 0 < x := by
  intro x hx
  rcases List.mem_cons.mp hx with rfl | hx1
  · omega
  · rcases List.mem_cons.mp hx1 with rfl | hx2
    · omega
    · rw [List.eq_of_mem_replicate hx2]
      omega

/-- `(0, 1) ∈ cells [n]` for `2 ≤ n`. -/
theorem zero_one_mem_cells_singleRow (n : ℕ) (hn : 2 ≤ n) :
    ((0 : ℕ), (1 : ℕ)) ∈ cells [n] := by
  rw [mem_cells]
  exact hn

/-- `hookLen [n] (0, 1) = n − 1` for `2 ≤ n`. -/
theorem hookLen_singleRow_zero_one (n : ℕ) (hn : 2 ≤ n) :
    hookLen [n] (0, 1) = n - 1 := by
  have hs : ([n] : List ℕ).Sorted (· ≥ ·) := sorted_singleRow n (by omega)
  unfold hookLen
  dsimp only
  rw [conj_getD [n] hs 1]
  have h1 : ([n] : List ℕ).getD 0 0 = n := rfl
  have h1lt : 1 < n := by omega
  have h2 : ([n] : List ℕ).countP (fun x => decide (1 < x)) = 1 := by
    simp [h1lt]
  rw [h1, h2]
  omega

/-- `(1, 0) ∈ cells (List.replicate n 1)` for `2 ≤ n`. -/
theorem one_zero_mem_cells_singleCol (n : ℕ) (hn : 2 ≤ n) :
    ((1 : ℕ), (0 : ℕ)) ∈ cells (List.replicate n 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  rw [mem_cells]
  dsimp only
  simp [List.replicate_succ]

/-- `hookLen (List.replicate n 1) (1, 0) = n − 1` for `2 ≤ n`. -/
theorem hookLen_singleCol_one_zero (n : ℕ) (hn : 2 ≤ n) :
    hookLen (List.replicate n 1) (1, 0) = n - 1 := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  have hs : (List.replicate (m + 2) 1).Sorted (· ≥ ·) := sorted_singleCol (m + 2)
  unfold hookLen
  dsimp only
  rw [conj_getD (List.replicate (m + 2) 1) hs 0]
  have h1 : (List.replicate (m + 2) 1).getD 1 0 = 1 := by
    simp [List.replicate_succ]
  have h2 : (List.replicate (m + 2) 1).countP (fun x => decide (0 < x)) = m + 2 :=
    countP_pos_replicate_one (m + 2)
  rw [h1, h2]
  omega

/-- `(0, 0) ∈ cells (a :: 2 :: List.replicate c 1)` for `2 ≤ a`. -/
theorem zero_zero_mem_cells_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    ((0 : ℕ), (0 : ℕ)) ∈ cells (a :: 2 :: List.replicate c 1) := by
  rw [mem_cells]
  dsimp only
  rw [List.getD_cons_zero]
  omega

/-- `hookLen (a :: 2 :: List.replicate c 1) (0, 0) = a + c + 1` for `2 ≤ a`. -/
theorem hookLen_twoCorner_zero_zero (a c : ℕ) (ha : 2 ≤ a) :
    hookLen (a :: 2 :: List.replicate c 1) (0, 0) = a + c + 1 := by
  have hs : (a :: 2 :: List.replicate c 1).Sorted (· ≥ ·) := sorted_twoCorner a c ha
  unfold hookLen
  dsimp only
  rw [conj_getD (a :: 2 :: List.replicate c 1) hs 0]
  have h1 : (a :: 2 :: List.replicate c 1).getD 0 0 = a := rfl
  have h2 : (a :: 2 :: List.replicate c 1).countP (fun x => decide (0 < x)) = c + 2 := by
    have ha0 : (0 : ℕ) < a := by omega
    simp [ha0, countP_pos_replicate_one c]
  rw [h1, h2]
  omega

/-! ## D1 (`qou-ckyw`): Carrier classification at `v = n − 1` -/

/-- **D1, case `p = (0, 1)`**: if `(0, 1) ∈ cells l` has `hookLen l (0, 1) + 1 = l.sum` on a
sorted positive partition `l`, then `(0, 0)` is the unique missed cell, so `(1, 0) ∉ cells l` and
`l` is the single row `[l.sum]` with `2 ≤ l.sum`. -/
theorem eq_singleRow_of_carrier_zero_one (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((0 : ℕ), (1 : ℕ)) ∈ cells l)
    (heq : hookLen l (0, 1) + 1 = l.sum) :
    2 ≤ l.sum ∧ l = [l.sum] := by
  have hpc : 1 < l.getD 0 0 := by rw [mem_cells] at hp; exact hp
  obtain ⟨c, hc⟩ := exists_unique_missed_cell l hs (0, 1) hp heq
  have hmissed : ∀ q : ℕ × ℕ, q ∈ cells l → q ∉ armF l (0, 1) ∪ legF l (0, 1) → q = c := by
    intro q hq hnot
    have hqs : q ∈ (cells l) \ (armF l (0, 1) ∪ legF l (0, 1)) := Finset.mem_sdiff.mpr ⟨hq, hnot⟩
    rwa [hc, Finset.mem_singleton] at hqs
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by rw [mem_cells]; dsimp only; omega
  have h00_eq_c : ((0 : ℕ), (0 : ℕ)) = c :=
    hmissed (0, 0) h00 (origin_not_mem_hookUnion l (0, 1) (by decide))
  have hno_row1 : l.getD 1 0 = 0 := by
    by_contra hcon
    have h10 : ((1 : ℕ), (0 : ℕ)) ∈ cells l := by
      rw [mem_cells]; dsimp only; omega
    have hnot10 : ((1 : ℕ), (0 : ℕ)) ∉ armF l (0, 1) ∪ legF l (0, 1) := by
      intro hmem
      rcases Finset.mem_union.mp hmem with harm | hleg
      · have := ((mem_armF_iff l (0, 1) (1, 0)).mp harm).1
        omega
      · have := ((mem_legF_iff l (0, 1) (1, 0)).mp hleg).1
        omega
    have h10_eq_c := hmissed (1, 0) h10 hnot10
    have : (0 : ℕ) = 1 := congrArg Prod.fst (h00_eq_c.trans h10_eq_c.symm)
    omega
  cases l with
  | nil =>
      simp [List.getD] at hpc
  | cons a t =>
      cases t with
      | nil =>
          simp only [List.getD_cons_zero] at hpc
          refine ⟨?_, by simp⟩
          simp only [List.sum_cons, List.sum_nil, add_zero]
          omega
      | cons b s =>
          simp only [List.getD_cons_succ, List.getD_cons_zero] at hno_row1
          have hbpos : 0 < b := hpos b (List.mem_cons_of_mem a List.mem_cons_self)
          omega

/-- **D1, case `p = (1, 0)`**: if `(1, 0) ∈ cells l` has `hookLen l (1, 0) + 1 = l.sum` on a
sorted positive partition `l`, then `(0, 0)` is the unique missed cell, so `(0, 1) ∉ cells l` and
`l` is the single column `List.replicate l.sum 1` with `2 ≤ l.sum`. -/
theorem eq_singleCol_of_carrier_one_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((1 : ℕ), (0 : ℕ)) ∈ cells l)
    (heq : hookLen l (1, 0) + 1 = l.sum) :
    2 ≤ l.sum ∧ l = List.replicate l.sum 1 := by
  have hpc : 0 < l.getD 1 0 := by rw [mem_cells] at hp; exact hp
  obtain ⟨c, hc⟩ := exists_unique_missed_cell l hs (1, 0) hp heq
  have hmissed : ∀ q : ℕ × ℕ, q ∈ cells l → q ∉ armF l (1, 0) ∪ legF l (1, 0) → q = c := by
    intro q hq hnot
    have hqs : q ∈ (cells l) \ (armF l (1, 0) ∪ legF l (1, 0)) := Finset.mem_sdiff.mpr ⟨hq, hnot⟩
    rwa [hc, Finset.mem_singleton] at hqs
  have hlen2 : 2 ≤ l.length := by
    by_contra hcon
    rw [List.getD_eq_default _ _ (by omega)] at hpc
    omega
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by
    rw [mem_cells]; dsimp only
    cases l with
    | nil => simp at hlen2
    | cons a t => simpa using hpos a List.mem_cons_self
  have h00_eq_c : ((0 : ℕ), (0 : ℕ)) = c :=
    hmissed (0, 0) h00 (origin_not_mem_hookUnion l (1, 0) (by decide))
  have hhead_le_one : l.getD 0 0 ≤ 1 := by
    by_contra hcon
    have h01 : ((0 : ℕ), (1 : ℕ)) ∈ cells l := by
      rw [mem_cells]; dsimp only; omega
    have hnot01 : ((0 : ℕ), (1 : ℕ)) ∉ armF l (1, 0) ∪ legF l (1, 0) := by
      intro hmem
      rcases Finset.mem_union.mp hmem with harm | hleg
      · have := ((mem_armF_iff l (1, 0) (0, 1)).mp harm).1
        omega
      · have := ((mem_legF_iff l (1, 0) (0, 1)).mp hleg).2.1
        omega
    have h01_eq_c := hmissed (0, 1) h01 hnot01
    have : (0 : ℕ) = 1 := congrArg Prod.snd (h00_eq_c.trans h01_eq_c.symm)
    omega
  have hall_one : ∀ x ∈ l, x = 1 := by
    intro x hx
    have hxpos : 0 < x := hpos x hx
    have hxle : x ≤ l.getD 0 0 := by
      rw [getD_zero_eq_headD]
      exact mem_le_headD l hs x hx
    omega
  have hrep : l = List.replicate l.length 1 :=
    List.eq_replicate_iff.mpr ⟨rfl, hall_one⟩
  have hsum_eq : l.sum = l.length := by
    conv_lhs => rw [hrep]
    exact sum_replicate_one l.length
  refine ⟨by omega, ?_⟩
  rw [hsum_eq]
  exact hrep

/-- Off the first row and first column (`1 ≤ q.1` and `1 ≤ q.2`), a cell `q` never belongs to
the corner hook `armF l (0, 0) ∪ legF l (0, 0)`. -/
theorem not_mem_hookUnion_origin_of_pos (l : List ℕ) (q : ℕ × ℕ)
    (hq1 : 1 ≤ q.1) (hq2 : 1 ≤ q.2) :
    q ∉ armF l (0, 0) ∪ legF l (0, 0) := by
  intro hmem
  rcases Finset.mem_union.mp hmem with harm | hleg
  · have := ((mem_armF_iff l (0, 0) q).mp harm).1
    omega
  · have := ((mem_legF_iff l (0, 0) q).mp hleg).1
    omega

/-- Every cell of `cells l` in row 0 or column 0 belongs to `armF l (0, 0) ∪ legF l (0, 0)`. -/
theorem mem_hookUnion_origin_of_fst_or_snd_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (q : ℕ × ℕ) (hq : q ∈ cells l) (h0 : q.1 = 0 ∨ q.2 = 0) :
    q ∈ armF l (0, 0) ∪ legF l (0, 0) := by
  rw [mem_cells] at hq
  rcases h0 with hq1 | hq2
  · apply Finset.mem_union_left
    rw [mem_armF_iff]
    exact ⟨hq1, Nat.zero_le q.2, hq1 ▸ hq⟩
  · by_cases hq1 : q.1 = 0
    · apply Finset.mem_union_left
      rw [mem_armF_iff]
      exact ⟨hq1, Nat.zero_le q.2, hq1 ▸ hq⟩
    · apply Finset.mem_union_right
      rw [mem_legF_iff]
      refine ⟨hq2, Nat.pos_of_ne_zero hq1, ?_⟩
      rw [conj_getD l hs]
      exact (lt_countP_iff l hs 0 q.1).mpr (hq2 ▸ hq)

/-- **D1, case `p = (0, 0)`**: if `(0, 0) ∈ cells l` has `hookLen l (0, 0) + 1 = l.sum` on a
sorted positive partition `l`, then `(1, 1)` is the unique cell outside the corner hook, forcing
`2 ≤ l.headD 0`, `2 ≤ l.length`, and `l = l.headD 0 :: 2 :: List.replicate (l.length − 2) 1`. -/
theorem eq_twoCorner_of_carrier_zero_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((0 : ℕ), (0 : ℕ)) ∈ cells l)
    (heq : hookLen l (0, 0) + 1 = l.sum) :
    2 ≤ l.headD 0 ∧ 2 ≤ l.length ∧
      l = l.headD 0 :: 2 :: List.replicate (l.length - 2) 1 := by
  obtain ⟨c, hc⟩ := exists_unique_missed_cell l hs (0, 0) hp heq
  have hmissed : ∀ q : ℕ × ℕ, q ∈ cells l → q ∉ armF l (0, 0) ∪ legF l (0, 0) → q = c := by
    intro q hq hnot
    have hqs : q ∈ (cells l) \ (armF l (0, 0) ∪ legF l (0, 0)) := Finset.mem_sdiff.mpr ⟨hq, hnot⟩
    rwa [hc, Finset.mem_singleton] at hqs
  -- Since c ∈ cells l \ (armF ∪ legF), c must have 1 ≤ c.1 and 1 ≤ c.2
  have hc_mem : c ∈ (cells l) \ (armF l (0, 0) ∪ legF l (0, 0)) := by
    rw [hc]; exact Finset.mem_singleton_self c
  obtain ⟨hc_cell, hc_not⟩ := Finset.mem_sdiff.mp hc_mem
  have hc_pos : 1 ≤ c.1 ∧ 1 ≤ c.2 := by
    by_contra hcon
    have h0 : c.1 = 0 ∨ c.2 = 0 := by omega
    exact hc_not (mem_hookUnion_origin_of_fst_or_snd_zero l hs c hc_cell h0)
  -- Since c ∈ cells l and 1 ≤ c.1, 1 ≤ c.2, monotonicity of l gives (1, 1) ∈ cells l
  have hc_lt : c.2 < l.getD c.1 0 := (mem_cells l c).mp hc_cell
  have hc1_len : c.1 < l.length := by
    by_contra hcon
    rw [List.getD_eq_default _ _ (by omega)] at hc_lt
    omega
  have hle1 : l.getD c.1 0 ≤ l.getD 1 0 := by
    have h1_len : 1 < l.length := by omega
    rw [List.getD_eq_getElem _ _ hc1_len, List.getD_eq_getElem _ _ h1_len]
    rcases eq_or_lt_of_le hc_pos.1 with hEq | hLt
    · simp [hEq]
    · exact List.Sorted.rel_get_of_lt hs hLt
  have h11_cell : ((1 : ℕ), (1 : ℕ)) ∈ cells l := by
    rw [mem_cells]; dsimp only; omega
  have h11_eq_c : ((1 : ℕ), (1 : ℕ)) = c :=
    hmissed (1, 1) h11_cell (not_mem_hookUnion_origin_of_pos l (1, 1) (le_refl 1) (le_refl 1))
  -- Row 1 has length ≤ 2 (else (1, 2) would also be missed)
  have hrow1_eq_two : l.getD 1 0 = 2 := by
    have hge2 : 2 ≤ l.getD 1 0 := by rw [mem_cells] at h11_cell; dsimp only at h11_cell; omega
    by_contra hne2
    have hge3 : 3 ≤ l.getD 1 0 := by omega
    have h12_cell : ((1 : ℕ), (2 : ℕ)) ∈ cells l := by
      rw [mem_cells]; dsimp only; omega
    have h12_eq_c :=
      hmissed (1, 2) h12_cell (not_mem_hookUnion_origin_of_pos l (1, 2) (le_refl 1) (by omega))
    have : (1 : ℕ) = 2 := congrArg Prod.snd (h11_eq_c.trans h12_eq_c.symm)
    omega
  -- Every row i ≥ 2 has length ≤ 1 (else (i, 1) would also be missed)
  have hrows_ge2 : ∀ i, 2 ≤ i → l.getD i 0 ≤ 1 := by
    intro i hi
    by_contra hcon
    have hi1_cell : (i, (1 : ℕ)) ∈ cells l := by
      rw [mem_cells]; dsimp only; omega
    have hi1_eq_c :=
      hmissed (i, 1) hi1_cell (not_mem_hookUnion_origin_of_pos l (i, 1) (by omega) (le_refl 1))
    have : (1 : ℕ) = i := congrArg Prod.fst (h11_eq_c.trans hi1_eq_c.symm)
    omega
  -- Deconstruct l as a :: b :: t
  cases l with
  | nil => simp at hc1_len
  | cons a r =>
      cases r with
      | nil => simp at hc1_len; omega
      | cons b t =>
          simp only [List.getD_cons_succ, List.getD_cons_zero] at hrow1_eq_two
          subst hrow1_eq_two
          have ha2 : 2 ≤ a := (List.sorted_cons.mp hs).1 2 List.mem_cons_self
          have ht1 : t = List.replicate t.length 1 := by
            refine List.eq_replicate_iff.mpr ⟨rfl, fun x hx => ?_⟩
            obtain ⟨k, hk, rfl⟩ := List.mem_iff_getElem.mp hx
            have h1 : (a :: 2 :: t).getD (k + 2) 0 ≤ 1 := hrows_ge2 (k + 2) (by omega)
            rw [List.getD_cons_succ, List.getD_cons_succ, List.getD_eq_getElem _ _ hk] at h1
            have h2 : 0 < t[k] :=
              hpos _ (List.mem_cons_of_mem a (List.mem_cons_of_mem 2 hx))
            omega
          simp only [List.headD_cons, List.length_cons]
          exact ⟨ha2, by omega, congrArg (fun s => a :: 2 :: s) ht1⟩

/-- **D1 (`qou-ckyw`): Complete carrier classification at `v = n − 1`.**
On a sorted positive partition `l`, any cell `p ∈ cells l` with `hookLen l p + 1 = l.sum` is one
of the three depth-1 carriers:
- `(0, 0)` on a two-corner shape `a :: 2 :: 1^c` (`2 ≤ a`),
- `(0, 1)` on the single row `[n]` (`2 ≤ n`),
- `(1, 0)` on the single column `1^n` (`2 ≤ n`). -/
theorem carrier_classification_depth_one (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (p : ℕ × ℕ) (hp : p ∈ cells l)
    (heq : hookLen l p + 1 = l.sum) :
    (p = (0, 0) ∧ 2 ≤ l.headD 0 ∧ 2 ≤ l.length ∧
      l = l.headD 0 :: 2 :: List.replicate (l.length - 2) 1) ∨
    (p = (0, 1) ∧ 2 ≤ l.sum ∧ l = [l.sum]) ∨
    (p = (1, 0) ∧ 2 ≤ l.sum ∧ l = List.replicate l.sum 1) := by
  rcases carrier_mem_three l hs p hp heq with rfl | rfl | rfl
  · obtain ⟨h1, h2, h3⟩ := eq_twoCorner_of_carrier_zero_zero l hs hpos hp heq
    exact Or.inl ⟨rfl, h1, h2, h3⟩
  · obtain ⟨h1, h2⟩ := eq_singleRow_of_carrier_zero_one l hs hpos hp heq
    exact Or.inr (Or.inl ⟨rfl, h1, h2⟩)
  · obtain ⟨h1, h2⟩ := eq_singleCol_of_carrier_one_zero l hs hpos hp heq
    exact Or.inr (Or.inr ⟨rfl, h1, h2⟩)

/-! ## D3 (`qou-x3u6`): `hookCount` confinement in count form at `v = n − 1` -/

/-- Structural predicate for the three depth-1 carrier shapes (`v = n − 1`):
single row `[n]` (`2 ≤ n`), single column `1^n` (`2 ≤ n`), or two-corner `(a, 2, 1^c)` (`2 ≤ a`). -/
def isDepthOneShape (l : List ℕ) : Prop :=
  (2 ≤ l.sum ∧ l = [l.sum]) ∨
  (2 ≤ l.sum ∧ l = List.replicate l.sum 1) ∨
  (2 ≤ l.headD 0 ∧ 2 ≤ l.length ∧ l = l.headD 0 :: 2 :: List.replicate (l.length - 2) 1)

/-- **D3 (single row `[n]`)**: `N_{n−1}([n]) = 1` for `2 ≤ n` — `(0, 1)` is the unique cell of
hook length `n − 1`. -/
theorem hookCount_depthOne_singleRow (n : ℕ) (hn : 2 ≤ n) :
    hookCount [n] (n - 1) = 1 := by
  have hs : ([n] : List ℕ).Sorted (· ≥ ·) := sorted_singleRow n (by omega)
  have hpos : ∀ x ∈ ([n] : List ℕ), 0 < x := by
    intro x hx; rw [List.mem_singleton.mp hx]; omega
  unfold hookCount
  rw [Finset.card_eq_one]
  refine ⟨((0 : ℕ), (1 : ℕ)), ?_⟩
  rw [Finset.eq_singleton_iff_unique_mem]
  refine ⟨Finset.mem_filter.mpr ⟨zero_one_mem_cells_singleRow n hn, hookLen_singleRow_zero_one n hn⟩,
    ?_⟩
  intro p hp
  obtain ⟨hpcell, hplen⟩ := Finset.mem_filter.mp hp
  have heq : hookLen [n] p + 1 = ([n] : List ℕ).sum := by
    rw [hplen, List.sum_cons, List.sum_nil]; omega
  rcases carrier_classification_depth_one [n] hs hpos p hpcell heq with
    ⟨_, _, hlen, _⟩ | ⟨hp01, _, _⟩ | ⟨_, _, hcol⟩
  · simp at hlen
  · exact hp01
  · have hlen := congrArg List.length hcol
    simp at hlen
    omega

/-- **D3 (single column `1^n`)**: `N_{n−1}(1^n) = 1` for `2 ≤ n` — `(1, 0)` is the unique cell of
hook length `n − 1`. -/
theorem hookCount_depthOne_singleCol (n : ℕ) (hn : 2 ≤ n) :
    hookCount (List.replicate n 1) (n - 1) = 1 := by
  have hs : (List.replicate n 1).Sorted (· ≥ ·) := sorted_singleCol n
  have hpos : ∀ x ∈ List.replicate n 1, 0 < x := by
    intro x hx; rw [List.eq_of_mem_replicate hx]; omega
  unfold hookCount
  rw [Finset.card_eq_one]
  refine ⟨((1 : ℕ), (0 : ℕ)), ?_⟩
  rw [Finset.eq_singleton_iff_unique_mem]
  refine ⟨Finset.mem_filter.mpr ⟨one_zero_mem_cells_singleCol n hn, hookLen_singleCol_one_zero n hn⟩,
    ?_⟩
  intro p hp
  obtain ⟨hpcell, hplen⟩ := Finset.mem_filter.mp hp
  have heq : hookLen (List.replicate n 1) p + 1 = (List.replicate n 1).sum := by
    rw [hplen, sum_replicate_one]; omega
  rcases carrier_classification_depth_one (List.replicate n 1) hs hpos p hpcell heq with
    ⟨_, hhd, _, _⟩ | ⟨_, _, hrow⟩ | ⟨hp10, _, _⟩
  · obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
    simp [List.replicate_succ] at hhd
  · have hlen := congrArg List.length hrow
    simp at hlen
    omega
  · exact hp10

/-- **D3 (two-corner `(a, 2, 1^c)`)**: `N_{n−1}((a, 2, 1^c)) = 1` for `2 ≤ a` (`n = a + c + 2`) —
`(0, 0)` is the unique cell of hook length `a + c + 1 = n − 1`. -/
theorem hookCount_depthOne_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    hookCount (a :: 2 :: List.replicate c 1) (a + c + 1) = 1 := by
  set l := a :: 2 :: List.replicate c 1
  have hs : l.Sorted (· ≥ ·) := sorted_twoCorner a c ha
  have hpos : ∀ x ∈ l, 0 < x := pos_twoCorner a c ha
  unfold hookCount
  rw [Finset.card_eq_one]
  refine ⟨((0 : ℕ), (0 : ℕ)), ?_⟩
  rw [Finset.eq_singleton_iff_unique_mem]
  refine ⟨Finset.mem_filter.mpr ⟨zero_zero_mem_cells_twoCorner a c ha,
    hookLen_twoCorner_zero_zero a c ha⟩, ?_⟩
  intro p hp
  obtain ⟨hpcell, hplen⟩ := Finset.mem_filter.mp hp
  have heq : hookLen l p + 1 = l.sum := by
    rw [hplen, sum_twoCorner a c]
  rcases carrier_classification_depth_one l hs hpos p hpcell heq with
    ⟨hp00, _, _, _⟩ | ⟨_, _, hrow⟩ | ⟨_, _, hcol⟩
  · exact hp00
  · have hlen := congrArg List.length hrow
    simp [l] at hlen
  · have hhd := congrArg (fun s => s.headD 0) hcol
    rw [sum_twoCorner a c] at hhd
    obtain ⟨m, hm⟩ : ∃ m, a + c + 2 = m + 1 := ⟨a + c + 1, by omega⟩
    rw [hm, List.replicate_succ] at hhd
    simp [l] at hhd
    omega

/-- **D3 (non-carrier shapes)**: off the depth-1 carrier shapes, `N_{n−1}(l) = 0` for every sorted
positive partition `l` with `1 ≤ l.sum`. -/
theorem hookCount_sub_one_eq_zero_of_not_isDepthOneShape (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hsum : 1 ≤ l.sum) (hnot : ¬ isDepthOneShape l) :
    hookCount l (l.sum - 1) = 0 := by
  unfold hookCount
  rw [Finset.card_eq_zero, Finset.eq_empty_iff_forall_notMem]
  intro p hp
  obtain ⟨hpcell, hplen⟩ := Finset.mem_filter.mp hp
  have heq : hookLen l p + 1 = l.sum := by omega
  rcases carrier_classification_depth_one l hs hpos p hpcell heq with
    ⟨_, h1, h2, h3⟩ | ⟨_, h1, h2⟩ | ⟨_, h1, h2⟩
  · exact hnot (Or.inr (Or.inr ⟨h1, h2, h3⟩))
  · exact hnot (Or.inl ⟨h1, h2⟩)
  · exact hnot (Or.inr (Or.inl ⟨h1, h2⟩))

/-! ## D4 (`qou-q621`): Depth-1 enumeration inside `partsOf` (membership, `Nodup`, restriction) -/

/-- The `k − 3` two-corner shapes `(a, 2, 1^c)` of size `k`, indexed by `i ∈ range (k − 3)` with
`a = i + 2` and `c = k − 4 − i`. -/
def twoCornerShapes (k : ℕ) : List (List ℕ) :=
  (List.range (k - 3)).map (fun i => (i + 2) :: 2 :: List.replicate (k - 4 - i) 1)

/-- All `k − 1` depth-1 carrier shapes of size `k` (`k ≥ 3`): the single row `[k]`, the single
column `1^k`, and the `k − 3` two-corner shapes `twoCornerShapes k`. -/
def depthOneShapes (k : ℕ) : List (List ℕ) :=
  [k] :: List.replicate k 1 :: twoCornerShapes k

/-- Each enumerated two-corner shape has size `k`. -/
theorem twoCornerShape_sum (k i : ℕ) (hi : i < k - 3) :
    ((i + 2) :: 2 :: List.replicate (k - 4 - i) 1).sum = k := by
  rw [sum_twoCorner]
  omega

/-- Every enumerated two-corner shape belongs to `partsOf k`. -/
theorem twoCornerShape_mem_partsOf (k i : ℕ) (hi : i < k - 3) :
    ((i + 2) :: 2 :: List.replicate (k - 4 - i) 1) ∈ partsOf k := by
  apply mem_partsFuel _ k k k (twoCornerShape_sum k i hi)
  · exact pos_twoCorner (i + 2) (k - 4 - i) (by omega)
  · intro x hx
    rcases List.mem_cons.mp hx with rfl | hx1
    · omega
    · rcases List.mem_cons.mp hx1 with rfl | hx2
      · omega
      · rw [List.eq_of_mem_replicate hx2]; omega
  · exact sorted_twoCorner (i + 2) (k - 4 - i) (by omega)
  · rw [List.length_cons, List.length_cons, List.length_replicate]; omega

/-- The single column `List.replicate k 1` belongs to `partsOf k` for `1 ≤ k`. -/
theorem singleCol_mem_partsOf (k : ℕ) (hk : 1 ≤ k) :
    List.replicate k 1 ∈ partsOf k := by
  have h := hookShape_mem_partsOf k 0 hk
  obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
  simpa [List.replicate_succ] using h

/-- **D4 (membership)**: every shape in `depthOneShapes k` belongs to `partsOf k` for `1 ≤ k`. -/
theorem depthOneShapes_mem_partsOf (k : ℕ) (hk : 1 ≤ k) :
    ∀ l ∈ depthOneShapes k, l ∈ partsOf k := by
  intro l hl
  rcases List.mem_cons.mp hl with rfl | hl1
  · exact singleRow_mem_partsOf k hk
  · rcases List.mem_cons.mp hl1 with rfl | hl2
    · exact singleCol_mem_partsOf k hk
    · obtain ⟨i, hi, rfl⟩ := List.mem_map.mp hl2
      exact twoCornerShape_mem_partsOf k i (List.mem_range.mp hi)

/-- `twoCornerShapes k` has no duplicates (the first row `i + 2` is injective). -/
theorem twoCornerShapes_nodup (k : ℕ) : (twoCornerShapes k).Nodup := by
  unfold twoCornerShapes
  refine List.Nodup.map ?_ List.nodup_range
  intro a b hab
  simp only [List.cons.injEq] at hab
  omega

/-- **D4 (`Nodup`)**: `depthOneShapes k` has no duplicates for `2 ≤ k` (the single row has length
`1`, the single column has head `1`, and every two-corner shape has length `≥ 2` and head `≥ 2`). -/
theorem depthOneShapes_nodup (k : ℕ) (hk : 2 ≤ k) : (depthOneShapes k).Nodup := by
  unfold depthOneShapes
  rw [List.nodup_cons, List.nodup_cons]
  refine ⟨?_, ?_, twoCornerShapes_nodup k⟩
  · intro hmem
    rcases List.mem_cons.mp hmem with hEq | h2c
    · have hlen := congrArg List.length hEq
      simp at hlen
      omega
    · obtain ⟨i, _, hEq⟩ := List.mem_map.mp h2c
      have hlen := congrArg List.length hEq
      simp at hlen
  · intro hmem
    obtain ⟨i, _, hEq⟩ := List.mem_map.mp hmem
    obtain ⟨m, rfl⟩ : ∃ m, k = m + 2 := ⟨k - 2, by omega⟩
    have hhd := congrArg (fun s => s.headD 0) hEq
    simp [List.replicate_succ] at hhd

/-- `depthOneShapes k` has exactly `k − 1` elements for `3 ≤ k`. -/
theorem depthOneShapes_length (k : ℕ) (hk : 3 ≤ k) :
    (depthOneShapes k).length = k - 1 := by
  unfold depthOneShapes twoCornerShapes
  simp only [List.length_cons, List.length_map, List.length_range]
  omega

/-- **D4 (completeness)**: every member of `partsOf k` satisfying `isDepthOneShape` lies in
`depthOneShapes k`. -/
theorem mem_depthOneShapes_of_isDepthOneShape (k : ℕ) (l : List ℕ)
    (hl : l ∈ partsOf k) (hd : isDepthOneShape l) :
    l ∈ depthOneShapes k := by
  obtain ⟨hsum, _, _⟩ := partsOf_facts k l hl
  unfold depthOneShapes
  rcases hd with ⟨_, hrow⟩ | ⟨_, hcol⟩ | ⟨hhd, hlen, h2c⟩
  · rw [hsum] at hrow
    exact List.mem_cons.mpr (Or.inl hrow)
  · rw [hsum] at hcol
    exact List.mem_cons.mpr (Or.inr (List.mem_cons.mpr (Or.inl hcol)))
  · apply List.mem_cons.mpr; right; apply List.mem_cons.mpr; right
    have hsum2 : l.headD 0 + (l.length - 2) + 2 = k := by
      have := congrArg List.sum h2c
      rw [sum_twoCorner] at this
      omega
    unfold twoCornerShapes
    refine List.mem_map.mpr ⟨l.headD 0 - 2, List.mem_range.mpr (by omega), ?_⟩
    have h1 : l.headD 0 - 2 + 2 = l.headD 0 := by omega
    have h2 : k - 4 - (l.headD 0 - 2) = l.length - 2 := by omega
    rw [h1, h2]
    exact h2c.symm

/-- Off `depthOneShapes k`, `hookCount l (k − 1) = 0` on `partsOf k`. -/
theorem hookCount_depthOne_eq_zero_of_not_mem (k : ℕ) (hk : 1 ≤ k) (l : List ℕ)
    (hl : l ∈ partsOf k) (hnm : l ∉ depthOneShapes k) :
    hookCount l (k - 1) = 0 := by
  obtain ⟨hsum, hpos, hsort⟩ := partsOf_facts k l hl
  have hnot : ¬ isDepthOneShape l := fun hd =>
    hnm (mem_depthOneShapes_of_isDepthOneShape k l hl hd)
  have h0 := hookCount_sub_one_eq_zero_of_not_isDepthOneShape l hsort hpos (hsum ▸ hk) hnot
  rwa [hsum] at h0

/-- On every shape in `depthOneShapes k` (`2 ≤ k`), `hookCount l (k − 1) = 1`. -/
theorem hookCount_depthOne_eq_one_of_mem (k : ℕ) (hk : 2 ≤ k) (l : List ℕ)
    (hl : l ∈ depthOneShapes k) :
    hookCount l (k - 1) = 1 := by
  rcases List.mem_cons.mp hl with rfl | hl1
  · exact hookCount_depthOne_singleRow k hk
  · rcases List.mem_cons.mp hl1 with rfl | hl2
    · exact hookCount_depthOne_singleCol k hk
    · obtain ⟨i, hi, rfl⟩ := List.mem_map.mp hl2
      have hi' : i < k - 3 := List.mem_range.mp hi
      have h1 := hookCount_depthOne_twoCorner (i + 2) (k - 4 - i) (by omega)
      have heq : i + 2 + (k - 4 - i) + 1 = k - 1 := by omega
      rwa [heq] at h1

/-- **D4 (Plancherel sum restriction)**: any weight on `partsOf k` (`2 ≤ k`) that vanishes outside
`depthOneShapes k` sums over `depthOneShapes k` alone. -/
theorem sum_partsOf_eq_sum_depthOneShapes (k : ℕ) (hk : 2 ≤ k) (g : List ℕ → ℝ)
    (hg : ∀ l ∈ partsOf k, l ∉ depthOneShapes k → g l = 0) :
    ((partsOf k).map g).sum = ((depthOneShapes k).map g).sum := by
  have hnd : (partsOf k).Nodup := partsFuel_nodup k k k
  rw [← List.sum_toFinset g hnd, ← List.sum_toFinset g (depthOneShapes_nodup k hk)]
  refine (Finset.sum_subset ?_ ?_).symm
  · intro x hx
    rw [List.mem_toFinset] at hx ⊢
    exact depthOneShapes_mem_partsOf k (by omega) x hx
  · intro x hx hnx
    rw [List.mem_toFinset] at hx hnx
    exact hg x hx hnx

/-- **D4 (depth-1 mixed moment restriction)**: for `2 ≤ k`, the `v = k − 1` numerator of the
`ν`-system restricts to the `k − 1` shapes of `depthOneShapes k`, each with multiplicity `1`. -/
theorem depthOne_mixedMoment_eq_depthOneShapes_sum (k : ℕ) (hk : 2 ≤ k) :
    ((partsOf k).map
        (fun l => tilt 0 (sytDim l) * (hookCount l (k - 1) : ℝ) * (omega3 k l : ℝ))).sum
      = ((depthOneShapes k).map (fun l => tilt 0 (sytDim l) * (omega3 k l : ℝ))).sum := by
  rw [sum_partsOf_eq_sum_depthOneShapes k hk _ (fun l hl hnm => by
    rw [hookCount_depthOne_eq_zero_of_not_mem k (by omega) l hl hnm]
    push_cast
    ring)]
  refine congrArg List.sum (List.map_congr_left fun l hl => ?_)
  rw [hookCount_depthOne_eq_one_of_mem k hk l hl]
  push_cast
  ring

/-! ## D5 (`qou-amf8`): Depth-1 shape data (`contentSq`, `omega3`, `hookProd`, `sytDim`) -/

/-- **D5 (`contentSq` of a two-corner shape `(a, 2, 1^c)`)**:
row 0 contributes `∑_{j < a} j²`, row 1 (`c(1,0) = −1`, `c(1,1) = 0`) contributes `1 + 0 = 1`,
and rows `2 .. c + 1` contribute `∑_{t < c} (t + 2)²`, which combines with row 1 into
`∑_{j < c + 2} j²` (`Q(a − 1) + Q(c + 1)` in the second-instance audit). -/
theorem contentSq_twoCorner (a c : ℕ) :
    contentSq (a :: 2 :: List.replicate c 1)
      = (∑ j ∈ Finset.range a, ((j : ℤ)) ^ 2)
        + ∑ j ∈ Finset.range (c + 2), ((j : ℤ)) ^ 2 := by
  rw [contentSq_eq_finset_sum]
  have hlen : (a :: 2 :: List.replicate c 1).length = c + 2 := by
    simp
  rw [hlen, Finset.sum_range_succ', Finset.sum_range_succ']
  have hrow0 : (a :: 2 :: List.replicate c 1).getD 0 0 = a := rfl
  have hrow1 : (a :: 2 :: List.replicate c 1).getD 1 0 = 2 := rfl
  have htail : ∑ i ∈ Finset.range c,
      ∑ j ∈ Finset.range ((a :: 2 :: List.replicate c 1).getD (i + 1 + 1) 0),
        ((j : ℤ) - ((i + 1 + 1 : ℕ) : ℤ)) ^ 2
      = ∑ i ∈ Finset.range c, ((i : ℤ) + 2) ^ 2 := by
    refine Finset.sum_congr rfl fun i hi => ?_
    have hgd : (a :: 2 :: List.replicate c 1).getD (i + 1 + 1) 0 = 1 := by
      rw [List.getD_cons_succ, List.getD_cons_succ]
      exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
    rw [hgd, Finset.sum_range_one]
    push_cast
    ring
  rw [hrow0, hrow1, htail]
  have h2 : ∑ j ∈ Finset.range 2, ((j : ℤ) - ((1 : ℕ) : ℤ)) ^ 2 = 1 := by decide
  rw [h2]
  simp only [Nat.cast_zero, sub_zero]
  have hshift : (∑ i ∈ Finset.range c, ((i : ℤ) + 2) ^ 2) + 1
      = ∑ j ∈ Finset.range (c + 2), ((j : ℤ)) ^ 2 := by
    rw [Finset.sum_range_succ' _ (c + 1), Finset.sum_range_succ' _ c]
    have hcongr : ∑ k ∈ Finset.range c, (((k + 1 + 1 : ℕ) : ℤ)) ^ 2
        = ∑ i ∈ Finset.range c, ((i : ℤ) + 2) ^ 2 := by
      refine Finset.sum_congr rfl fun i _ => ?_
      push_cast
      ring
    rw [hcongr]
    push_cast
    ring
  linarith

/-- **D5 (`6 · ω₃` on a two-corner shape `(a, 2, 1^c)` of size `k`, with `a = i + 2`,
`c = k − 4 − i`)**: explicit polynomial form of `6 · ω₃(k, (i + 2, 2, 1^{k − 4 − i}))`. -/
theorem six_mul_omega3_twoCorner (k i : ℕ) (hi : i < k - 3) :
    6 * omega3 k ((i + 2) :: 2 :: List.replicate (k - 4 - i) 1)
      = ((i : ℤ) + 1) * ((i : ℤ) + 2) * (2 * (i : ℤ) + 3)
        + ((k : ℤ) - 3 - (i : ℤ)) * ((k : ℤ) - 2 - (i : ℤ)) * (2 * ((k : ℤ) - 3 - (i : ℤ)) + 1)
        - 3 * (k : ℤ) * ((k : ℤ) - 1) := by
  have harm : 6 * ∑ j ∈ Finset.range (i + 2), ((j : ℤ)) ^ 2
      = ((i : ℤ) + 1) * ((i : ℤ) + 2) * (2 * (i : ℤ) + 3) := by
    rw [six_mul_sum_range_sq (i + 2)]
    push_cast
    ring
  have hleg : 6 * ∑ j ∈ Finset.range (k - 4 - i + 2), ((j : ℤ)) ^ 2
      = ((k : ℤ) - 3 - (i : ℤ)) * ((k : ℤ) - 2 - (i : ℤ))
        * (2 * ((k : ℤ) - 3 - (i : ℤ)) + 1) := by
    rw [six_mul_sum_range_sq (k - 4 - i + 2)]
    have hc : ((k - 4 - i : ℕ) : ℤ) = (k : ℤ) - 4 - (i : ℤ) := by
      push_cast [Nat.cast_sub (by omega : i ≤ k - 4), Nat.cast_sub (by omega : 4 ≤ k)]
      ring
    push_cast [hc]
    ring
  have hcentre : ((k * (k - 1) / 2 : ℕ) : ℤ) * 2 = (k : ℤ) * ((k : ℤ) - 1) := by
    have hZ : ((2 * (k * (k - 1) / 2) : ℕ) : ℤ) = ((k * (k - 1) : ℕ) : ℤ) :=
      congrArg (fun n : ℕ => (n : ℤ)) (two_mul_choose_two k)
    rw [Nat.cast_mul, Nat.cast_ofNat, Nat.cast_mul, Nat.cast_sub (by omega : 1 ≤ k),
      Nat.cast_one] at hZ
    linarith
  unfold omega3
  rw [contentSq_twoCorner (i + 2) (k - 4 - i)]
  linarith

/-- **D5 (`hookProd` of a two-corner shape `(a, 2, 1^c)`)**:
for `2 ≤ a`, `∏_□ h(□) = (a + c + 1) · a · (c + 2) · (a − 2)! · c!`. -/
theorem hookProd_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    hookProd (a :: 2 :: List.replicate c 1)
      = (a + c + 1) * a * (c + 2) * (a - 2).factorial * c.factorial := by
  obtain ⟨b, rfl⟩ : ∃ b, a = b + 2 := ⟨a - 2, by omega⟩
  simp only [Nat.add_sub_cancel]
  set l := (b + 2) :: 2 :: List.replicate c 1
  have hsorted : l.Sorted (· ≥ ·) := sorted_twoCorner (b + 2) c (by omega)
  have hcj0 : (conj l).getD 0 0 = c + 2 := by
    rw [conj_getD _ hsorted]
    simp [l, countP_pos_replicate_one c]
  have hcj1 : (conj l).getD 1 0 = 2 := by
    rw [conj_getD _ hsorted, List.countP_cons, List.countP_cons]
    have hz : (List.replicate c 1).countP (fun x => decide (1 < x)) = 0 := by
      rw [List.countP_eq_zero]
      intro x hx
      rw [List.eq_of_mem_replicate hx]
      decide
    rw [hz]
    have hb1 : 1 < b + 2 := by omega
    simp [hb1]
  have hcjj : ∀ j, 2 ≤ j → j < b + 2 → (conj l).getD j 0 = 1 := by
    intro j hj2 hjb
    rw [conj_getD _ hsorted, List.countP_cons, List.countP_cons]
    have hz : (List.replicate c 1).countP (fun x => decide (j < x)) = 0 := by
      rw [List.countP_eq_zero]
      intro x hx
      rw [List.eq_of_mem_replicate hx]
      simp only [decide_eq_true_eq]
      omega
    rw [hz]
    have hnot2 : ¬ j < 2 := by omega
    simp [hjb, hnot2]
  rw [hookProd_eq_finset_prod]
  have hlen : l.length = c + 2 := by simp [l]
  rw [hlen, Finset.prod_range_succ', Finset.prod_range_succ']
  -- Rows 2 .. c + 1 contribute c!
  have hrows : ∀ i ∈ Finset.range c,
      (∏ j ∈ Finset.range (l.getD (i + 1 + 1) 0),
        (l.getD (i + 1 + 1) 0 + (conj l).getD j 0 - j - (i + 1 + 1) - 1))
      = c - i := by
    intro i hi
    have hgd : l.getD (i + 1 + 1) 0 = 1 := by
      simp only [l, List.getD_cons_succ]
      exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
    rw [hgd, Finset.prod_range_one, hcj0]
    omega
  rw [Finset.prod_congr rfl hrows, prod_range_sub_eq_factorial]
  -- Row 1 contributes (c + 2) * 1 = c + 2
  have hrow1 :
      (∏ j ∈ Finset.range (l.getD 1 0),
        (l.getD 1 0 + (conj l).getD j 0 - j - 1 - 1))
      = c + 2 := by
    have hgd1 : l.getD 1 0 = 2 := rfl
    rw [hgd1, Finset.prod_range_succ', Finset.prod_range_one, hcj1, hcj0]
    omega
  -- Row 0 contributes (b + 2 + c + 1) * (b + 2) * b!
  have hrow0 :
      (∏ j ∈ Finset.range (l.getD 0 0),
        (l.getD 0 0 + (conj l).getD j 0 - j - 0 - 1))
      = (b + 2 + c + 1) * (b + 2) * b.factorial := by
    have hgd0 : l.getD 0 0 = b + 2 := rfl
    rw [hgd0, Finset.prod_range_succ', Finset.prod_range_succ']
    have hgj : ∀ j ∈ Finset.range b,
        (b + 2 + (conj l).getD (j + 1 + 1) 0 - (j + 1 + 1) - 0 - 1) = b - j := by
      intro j hj
      rw [hcjj (j + 1 + 1) (by omega) (by have := Finset.mem_range.mp hj; omega)]
      omega
    rw [Finset.prod_congr rfl hgj, prod_range_sub_eq_factorial, hcj1, hcj0]
    have hg0 : b + 2 + (c + 2) - 0 - 0 - 1 = b + 2 + c + 1 := by omega
    have hg1 : b + 2 + 2 - 1 - 0 - 1 = b + 2 := by omega
    rw [hg0, hg1]
    ring
  rw [hrow1, hrow0]
  ring

/-- **D5 (`sytDim` of a two-corner shape `(a, 2, 1^c)`)**:
`f^{(a,2,1^c)} = (a + c + 2)! / ((a + c + 1) · a · (c + 2) · (a − 2)! · c!)` for `2 ≤ a`,
matching line 96 of `wlambda_covariance_epic_A2_tail_second_instance_probe.py`. -/
theorem sytDim_twoCorner (a c : ℕ) (ha : 2 ≤ a) :
    sytDim (a :: 2 :: List.replicate c 1)
      = (a + c + 2).factorial
        / ((a + c + 1) * a * (c + 2) * (a - 2).factorial * c.factorial) := by
  unfold sytDim
  rw [sum_twoCorner a c, hookProd_twoCorner a c ha]

/-- **D5 (`sytDim` of the single row `[n]`)**: `f^{(n)} = 1` for `1 ≤ n`. -/
theorem sytDim_singleRow (n : ℕ) (hn : 1 ≤ n) : sytDim [n] = 1 := by
  have h := sytDim_hookShape n 0 hn
  simp only [List.replicate_zero, Nat.add_zero, Nat.choose_self] at h
  exact h

/-- **D5 (`sytDim` of the single column `1^n`)**: `f^{(1^n)} = 1` for `1 ≤ n`. -/
theorem sytDim_singleCol (n : ℕ) (hn : 1 ≤ n) : sytDim (List.replicate n 1) = 1 := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  have h := sytDim_hookShape 1 m (le_refl 1)
  simpa [List.replicate_succ] using h

end QOU.BraidsAndKnots.DepthOneHookClassification
