import QOU.BraidKnot.SYTEncodingBridge
import Mathlib.Order.Interval.Finset.Nat

/-!
# The SYT-encoding bridge, half two: the 0-indexed count embeds into the 1-indexed one

`SYTEncodingBridge` embedded `QOU.Mathlib.StandardYoungTableau` (1-indexed, `BijOn`-packaged) into
`QOU.BraidKnot.StandardYoungTableau` (0-indexed, raw predicates), giving
`numStandardYoungTableaux μ ≤ numSYT μ`. This file supplies the reverse embedding, and hence the
equality of the two counts.

The reverse direction needs two things the 0-indexed encoding does not carry directly:

* **general monotonicity from adjacent strictness** — the raw structure states `row_strict` /
  `col_strict` only for adjacent cells, while `SemistandardYoungTableau` demands the general
  `j1 < j2` / `i1 < i2` forms (`entry_lt_row`, `entry_lt_col` below, by induction on the gap);
* **the pigeonhole** — the 1-indexed side demands `Set.BijOn` onto `Set.Icc 1 n`, i.e.
  *surjectivity*, which the raw structure never states. It follows from `inj_on` plus `lt_card`:
  an injection from the `n`-cell set into an `n`-element target is onto
  (`Finset.surj_on_of_inj_on_of_card_le`).

-- Ref: [sagan2001] Sagan, The Symmetric Group §3 (standard tableaux; both entry conventions)
-/

namespace QOU.BraidKnot.SYTEncodingBridge

open QOU.BraidKnot

variable {μ : YoungDiagram}

/-! ## General monotonicity from adjacent strictness -/

/-- Rows increase strictly over an arbitrary gap (induction on the gap; the intermediate cells lie
in `μ` by the lower-set property). -/
theorem entry_lt_row (T : StandardYoungTableau μ) :
    ∀ (d i j : ℕ), (i, j + d + 1) ∈ μ → T.entry i j < T.entry i (j + d + 1) := by
  intro d
  induction d with
  | zero => intro i j h; exact T.row_strict i j h
  | succ d ih =>
      intro i j h
      have hmid : (i, j + d + 1) ∈ μ := μ.up_left_mem (le_refl i) (by omega) h
      have h1 : T.entry i j < T.entry i (j + d + 1) := ih i j hmid
      have h2 : T.entry i (j + d + 1) < T.entry i (j + d + 1 + 1) :=
        T.row_strict i (j + d + 1) (by convert h using 2)
      have heq : j + (d + 1) + 1 = j + d + 1 + 1 := by omega
      rw [heq]
      exact lt_trans h1 h2

/-- Columns increase strictly over an arbitrary gap. -/
theorem entry_lt_col (T : StandardYoungTableau μ) :
    ∀ (d i j : ℕ), (i + d + 1, j) ∈ μ → T.entry i j < T.entry (i + d + 1) j := by
  intro d
  induction d with
  | zero => intro i j h; exact T.col_strict i j h
  | succ d ih =>
      intro i j h
      have hmid : (i + d + 1, j) ∈ μ := μ.up_left_mem (by omega) (le_refl j) h
      have h1 : T.entry i j < T.entry (i + d + 1) j := ih i j hmid
      have h2 : T.entry (i + d + 1) j < T.entry (i + d + 1 + 1) j :=
        T.col_strict (i + d + 1) j (by convert h using 2)
      have heq : i + (d + 1) + 1 = i + d + 1 + 1 := by omega
      rw [heq]
      exact lt_trans h1 h2

/-- Row monotonicity in the `j1 < j2` form the semistandard structure demands. -/
theorem entry_lt_row' (T : StandardYoungTableau μ) {i j1 j2 : ℕ} (hlt : j1 < j2)
    (hc : (i, j2) ∈ μ) : T.entry i j1 < T.entry i j2 := by
  obtain ⟨d, rfl⟩ : ∃ d, j2 = j1 + d + 1 := ⟨j2 - j1 - 1, by omega⟩
  exact entry_lt_row T d i j1 hc

/-- Column monotonicity in the `i1 < i2` form the semistandard structure demands. -/
theorem entry_lt_col' (T : StandardYoungTableau μ) {i1 i2 j : ℕ} (hlt : i1 < i2)
    (hc : (i2, j) ∈ μ) : T.entry i1 j < T.entry i2 j := by
  obtain ⟨d, rfl⟩ : ∃ d, i2 = i1 + d + 1 := ⟨i2 - i1 - 1, by omega⟩
  exact entry_lt_col T d i1 j hc

/-! ## The shifted entry map and the pigeonhole -/

/-- The 1-indexed shift of a 0-indexed tableau: `+1` on cells, `0` off them. -/
def shift (T : StandardYoungTableau μ) (i j : ℕ) : ℕ :=
  if (i, j) ∈ μ then T.entry i j + 1 else 0

theorem shift_of_mem (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    shift T i j = T.entry i j + 1 := by
  rw [shift, if_pos h]

theorem shift_of_not_mem (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∉ μ) :
    shift T i j = 0 := by
  rw [shift, if_neg h]

/-- The shifted map lands in `{1, …, |μ|}` on cells. -/
theorem shift_mem_Icc (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    shift T i j ∈ Finset.Icc 1 μ.cells.card := by
  rw [shift_of_mem T h, Finset.mem_Icc]
  have hlt := T.lt_card i j h
  have hce : μ.card = μ.cells.card := rfl
  omega

/-- The shifted map is injective on the cells. -/
theorem shift_injOn (T : StandardYoungTableau μ) :
    ∀ p ∈ μ.cells, ∀ q ∈ μ.cells, shift T p.1 p.2 = shift T q.1 q.2 → p = q := by
  intro p hp q hq heq
  have hp' : (p.1, p.2) ∈ μ := by rwa [YoungDiagram.mem_cells] at hp
  have hq' : (q.1, q.2) ∈ μ := by rwa [YoungDiagram.mem_cells] at hq
  rw [shift_of_mem T hp', shift_of_mem T hq'] at heq
  have := T.inj_on p.1 p.2 q.1 q.2 hp' hq' (by omega)
  exact Prod.ext this.1 this.2

/-- **The pigeonhole**: an injection of the `n`-cell set into `{1, …, n}` is onto. -/
theorem shift_surjOn (T : StandardYoungTableau μ) :
    ∀ b ∈ Finset.Icc 1 μ.cells.card, ∃ p ∈ μ.cells, shift T p.1 p.2 = b := by
  have hcard : (Finset.Icc 1 μ.cells.card).card ≤ μ.cells.card := by
    rw [Nat.card_Icc]
    omega
  have hmaps : ∀ p ∈ μ.cells, shift T p.1 p.2 ∈ Finset.Icc 1 μ.cells.card := by
    intro p hp
    exact shift_mem_Icc T (by rwa [YoungDiagram.mem_cells] at hp)
  intro b hb
  obtain ⟨p, hp, hpb⟩ :=
    Finset.surj_on_of_inj_on_of_card_le (fun p _ => shift T p.1 p.2)
      (fun p hp => hmaps p hp) (fun p q hp hq h => shift_injOn T p hp q hq h) hcard b hb
  exact ⟨p, hp, hpb.symm⟩

/-- The `Set.BijOn` the 1-indexed structure demands, assembled from maps-to, inj-on and the
pigeonhole. -/
theorem shift_bijOn (T : StandardYoungTableau μ) :
    Set.BijOn (fun c : ℕ × ℕ => shift T c.1 c.2) (μ.cells : Set (ℕ × ℕ))
      (Set.Icc 1 μ.cells.card) := by
  refine ⟨?_, ?_, ?_⟩
  · intro p hp
    have hp' : p ∈ μ.cells := by rwa [Finset.mem_coe] at hp
    have := shift_mem_Icc T (by rwa [YoungDiagram.mem_cells] at hp')
    rw [Finset.mem_Icc] at this
    exact Set.mem_Icc.mpr this
  · intro p hp q hq heq
    exact shift_injOn T p (by rwa [Finset.mem_coe] at hp) q (by rwa [Finset.mem_coe] at hq) heq
  · intro b hb
    have hb' : b ∈ Finset.Icc 1 μ.cells.card := by
      rw [Finset.mem_Icc]
      exact Set.mem_Icc.mp hb
    obtain ⟨p, hp, hpb⟩ := shift_surjOn T b hb'
    exact ⟨p, by rwa [Finset.mem_coe], hpb⟩

/-! ## The reverse embedding and the equality of counts -/

/-- **The 0-indexed encoding embeds into the 1-indexed one**: add one on cells. The semistandard
fields come from the generalized monotonicity lemmas, and the `Set.BijOn` from the pigeonhole. -/
def toMathlibSYT (T : StandardYoungTableau μ) : QOU.Mathlib.StandardYoungTableau μ where
  toSsyt :=
    { entry := shift T
      row_weak' := by
        intro i j1 j2 hlt hc
        have hc1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hlt) hc
        rw [shift_of_mem T hc1, shift_of_mem T hc]
        have := entry_lt_row' T hlt hc
        omega
      col_strict' := by
        intro i1 i2 j hlt hc
        have hc1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt hlt) (le_refl j) hc
        rw [shift_of_mem T hc1, shift_of_mem T hc]
        have := entry_lt_col' T hlt hc
        omega
      zeros' := by
        intro i j h
        exact shift_of_not_mem T h }
  bijOn := shift_bijOn T

/-- The reverse embedding is injective (entries agree on cells after removing the shift, and vanish
off cells). -/
theorem toMathlibSYT_injective :
    Function.Injective (toMathlibSYT : StandardYoungTableau μ → _) := by
  intro T T' hTT'
  have hentry : ∀ i j, T.entry i j = T'.entry i j := by
    intro i j
    by_cases hc : (i, j) ∈ μ
    · have h : shift T i j = shift T' i j := by
        have := congrArg
          (fun S : QOU.Mathlib.StandardYoungTableau μ => S.entry i j) hTT'
        simpa [toMathlibSYT, QOU.Mathlib.StandardYoungTableau.entry] using this
      rw [shift_of_mem T hc, shift_of_mem T' hc] at h
      omega
    · rw [T.zero_off i j hc, T'.zero_off i j hc]
  cases T with
  | mk e lt zo io rs cs =>
    cases T' with
    | mk e' lt' zo' io' rs' cs' =>
      have : e = e' := by
        funext i j
        exact hentry i j
      subst this
      rfl

/-- **The other half of the bridge**. -/
theorem numSYT_le_numStandardYoungTableaux (μ : YoungDiagram) :
    numSYT μ ≤ QOU.Mathlib.numStandardYoungTableaux μ := by
  haveI : Finite (QOU.Mathlib.StandardYoungTableau μ) :=
    Finite.of_injective _ QOU.Mathlib.StandardYoungTableau.encode_injective
  unfold QOU.Mathlib.numStandardYoungTableaux numSYT
  exact Nat.card_le_card_of_injective _ toMathlibSYT_injective

/-- **The bridge**: the two standard-Young-tableau encodings count the same thing. With it, the RSK
identity `OVTopAssembly.sum_numSYT_sq_eq_factorial` (stated with `numSYT`) becomes available to the
hook-length side (`sytDim`/`numSYTenum`/`numStandardYoungTableaux`), which is what
`RSKBurnsideTarget.RSKBurnsideHolds` and the Plancherel normalisation
`Σ_λ (f^λ)² = k!` both need. -/
theorem numSYT_eq_numStandardYoungTableaux (μ : YoungDiagram) :
    numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ :=
  le_antisymm (numSYT_le_numStandardYoungTableaux μ) (numStandardYoungTableaux_le_numSYT μ)

end QOU.BraidKnot.SYTEncodingBridge
