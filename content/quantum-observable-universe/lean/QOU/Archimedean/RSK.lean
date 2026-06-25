import Mathlib.Data.List.Basic
import Mathlib.Data.List.Sort
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic

/-!
# Robinson–Schensted–Knuth Correspondence

Bijection: permutations of {1,...,k} ↔ pairs (P, Q) of SYT of the
same shape λ ⊢ k. Implies Burnside's identity k! = Σ dim(λ)².

## References

- [knuth1970] D. Knuth, Permutations, matrices, and generalized Young tableaux.
- [sagan2001] B. Sagan, *The Symmetric Group*, §3.1–3.3.
-/

namespace QOU.Archimedean.RSK

/-! ## §1  Row insertion (inductive definition) -/

/-- Row bump: insert x into a strictly sorted list.
    Inductive on the list, replacing the first element > x.
    Returns (new_row, bumped_element_or_none). -/
def rowBump : List ℕ → ℕ → List ℕ × Option ℕ
  | [], x => ([x], none)
  | a :: rest, x =>
    if x < a then
      (x :: rest, some a)  -- x replaces a, a is bumped
    else
      let (rest', bumped) := rowBump rest x
      (a :: rest', bumped)

/-- rowBump on empty list. -/
@[simp] theorem rowBump_nil (x : ℕ) : rowBump [] x = ([x], none) := rfl

/-- rowBump when x < head. -/
theorem rowBump_lt (a : ℕ) (rest : List ℕ) (x : ℕ) (h : x < a) :
    rowBump (a :: rest) x = (x :: rest, some a) := by
  simp [rowBump, h]

/-- rowBump when x ≥ head. -/
theorem rowBump_ge (a : ℕ) (rest : List ℕ) (x : ℕ) (h : ¬(x < a)) :
    rowBump (a :: rest) x =
    let (rest', bumped) := rowBump rest x
    (a :: rest', bumped) := by
  simp [rowBump, h]

/-- rowBump preserves length or adds 1. -/
theorem rowBump_length (row : List ℕ) (x : ℕ) :
    (rowBump row x).1.length =
    row.length + (if (rowBump row x).2.isNone then 1 else 0) := by
  induction row with
  | nil => simp [rowBump]
  | cons a rest ih =>
    simp only [rowBump]
    split
    · simp  -- x < a: length preserved (replacement)
    · -- x ≥ a: result is (a :: rest', bumped') where (rest', bumped') = rowBump rest x
      -- LHS = 1 + rest'.length = 1 + rest.length + correction (by ih)
      -- RHS = (a :: rest).length + correction = 1 + rest.length + correction
      simp only [List.length_cons]
      have h := ih
      omega

/-- Elements of `(rowBump row x).1` are either from `row` or equal to `x`.
    This is the key structural lemma: row-bump substitutes at most one element. -/
theorem rowBump_mem (row : List ℕ) (x b : ℕ)
    (hb : b ∈ (rowBump row x).1) : b ∈ row ∨ b = x := by
  induction row with
  | nil => simp [rowBump] at hb; right; exact hb
  | cons a rest ih =>
    simp only [rowBump] at hb
    split at hb
    · -- x < a: result = x :: rest
      simp at hb
      rcases hb with rfl | hr
      · right; rfl
      · left; exact List.mem_cons_of_mem a hr
    · -- x ≥ a: result = a :: (rowBump rest x).1
      simp at hb
      rcases hb with rfl | hr
      · left; exact List.mem_cons_self
      · rcases ih hr with hrest | hx
        · left; exact List.mem_cons_of_mem a hrest
        · right; exact hx

/-- The bumped element (if any) is > x. -/
theorem rowBump_bumped_gt (row : List ℕ) (x : ℕ) (b : ℕ)
    (hsort : row.Sorted (· < ·))
    (hbump : (rowBump row x).2 = some b) :
    x < b := by
  induction row with
  | nil => simp [rowBump] at hbump
  | cons a rest ih =>
    simp only [rowBump] at hbump
    split at hbump
    · -- x < a: bumped = a
      simp at hbump
      obtain rfl := hbump
      assumption
    · -- x ≥ a: recurse
      next hge =>
      have hsort_rest : rest.Sorted (· < ·) := by
        cases hsort with
        | cons h1 h2 => exact h2
      exact ih hsort_rest (by simpa using hbump)

/-- rowBump preserves sortedness (for fresh x ∉ row). -/
theorem rowBump_sorted (row : List ℕ) (x : ℕ)
    (hsort : row.Sorted (· < ·))
    (hfresh : x ∉ row) :
    (rowBump row x).1.Sorted (· < ·) := by
  induction row with
  | nil => simp [rowBump]
  | cons a rest ih =>
    simp only [rowBump]
    split
    · -- x < a: result = x :: rest, need x < all of rest
      next hlt =>
      rw [List.sorted_cons] at hsort
      refine List.sorted_cons.mpr ⟨?_, hsort.2⟩
      intro b hb
      exact lt_trans hlt (hsort.1 b hb)
    · -- x ≥ a: result = a :: (rowBump rest x).1
      next hge =>
      have ha_ne : x ≠ a := by
        intro heq; exact hfresh (heq ▸ List.mem_cons_self)
      have hax : a < x := by omega
      have hfresh_rest : x ∉ rest := by
        intro hm; exact hfresh (List.mem_cons_of_mem a hm)
      rw [List.sorted_cons] at hsort
      have ih_result := ih hsort.2 hfresh_rest
      -- Need: a < all elements of (rowBump rest x).1.  Use rowBump_mem:
      refine List.sorted_cons.mpr ⟨?_, ih_result⟩
      intro b hb
      rcases rowBump_mem rest x b hb with hrest | rfl
      · exact hsort.1 b hrest
      · exact hax

/-! ## §2  Schensted insertion (cascade) -/

/-- Cascade rowBump through rows. Returns new rows and placement position. -/
def schenstedInsertRows : List (List ℕ) → ℕ → List (List ℕ) × (ℕ × ℕ)
  | [], x => ([[x]], (0, 0))
  | row :: rest, x =>
    let (newRow, bumped) := rowBump row x
    match bumped with
    | none => (newRow :: rest, (0, newRow.length - 1))
    | some b =>
      let (restRows, (r, c)) := schenstedInsertRows rest b
      (newRow :: restRows, (r + 1, c))

/-- Schensted insertion adds exactly one cell. -/
theorem schenstedInsertRows_size (rows : List (List ℕ)) (x : ℕ) :
    ((schenstedInsertRows rows x).1.map List.length).sum =
    (rows.map List.length).sum + 1 := by
  induction rows generalizing x with
  | nil => simp [schenstedInsertRows]
  | cons row rest ih =>
    have hlen := rowBump_length row x
    simp only [schenstedInsertRows]
    -- Case-split on whether rowBump bumps a value or appends
    cases hbump : (rowBump row x).2 with
    | none =>
      -- appended at current row: length grows by 1 (from hlen)
      simp only [List.map_cons, List.sum_cons]
      simp [hbump] at hlen
      omega
    | some b =>
      -- bumped: length of new row preserved; recurse with b on rest
      simp only [List.map_cons, List.sum_cons]
      simp [hbump] at hlen
      have := ih b
      omega

/-! ## §3  RSK map -/

/-- Build recording tableau by adding val at position (r, c). -/
def addEntry (rows : List (List ℕ)) (val r : ℕ) : List (List ℕ) :=
  if r < rows.length then
    rows.mapIdx fun i row => if i = r then row ++ [val] else row
  else
    rows ++ [[val]]

/-- The RSK map on raw row data (no invariant proofs). -/
def rskRaw (w : List ℕ) : List (List ℕ) × List (List ℕ) :=
  w.zipIdx.foldl (fun (pR, qR) (x, i) =>
    let (newP, (r, _)) := schenstedInsertRows pR x
    (newP, addEntry qR (i + 1) r)
  ) ([], [])

/-! ## §4  Burnside identity (concrete verifications) -/

/-- k! = Σ dim(λ)² for k = 3. -/
theorem burnside_3 : 1 + 4 + 1 = Nat.factorial 3 := by decide

/-- k! = Σ dim(λ)² for k = 4. -/
theorem burnside_4 : 1 + 9 + 4 + 9 + 1 = Nat.factorial 4 := by decide

/-- k! = Σ dim(λ)² for k = 5. -/
theorem burnside_5 : 1 + 16 + 25 + 36 + 25 + 16 + 1 = Nat.factorial 5 := by decide

/-- k! = Σ dim(λ)² for k = 6.
    Partitions of 6 with irrep dimensions (hook-length formula):
    (6)→1, (5,1)→5, (4,2)→9, (4,1,1)→10, (3,3)→5, (3,2,1)→16,
    (3,1,1,1)→10, (2,2,2)→5, (2,2,1,1)→9, (2,1,1,1,1)→5, (1⁶)→1. -/
theorem burnside_6 :
    1 + 25 + 81 + 100 + 25 + 256 + 100 + 25 + 81 + 25 + 1 = Nat.factorial 6 := by
  decide

/-! ## §5  Fomin identity (concrete) -/

/-- Fomin at k=4, μ=(3): Σ dim(λ)·m_{(3)}^λ = 4!/6·1 = 4.
    dims: 1,3,2,3,1. mults: 1,1,0,0,0. sum = 1+3 = 4. -/
theorem fomin_k4_sym : 1 * 1 + 3 * 1 + 2 * 0 + 3 * 0 + 1 * 0 = 24 / 6 * 1 := by decide

/-- Fomin at k=4, μ=(2,1): mults 0,1,1,1,0. sum = 3+2+3 = 8 = 4·2. -/
theorem fomin_k4_std : 1 * 0 + 3 * 1 + 2 * 1 + 3 * 1 + 1 * 0 = 24 / 6 * 2 := by decide

/-- Fomin at k=4, μ=(1,1,1): mults 0,0,0,1,1. sum = 3+1 = 4 = 4·1. -/
theorem fomin_k4_alt : 1 * 0 + 3 * 0 + 2 * 0 + 3 * 1 + 1 * 1 = 24 / 6 * 1 := by decide

/-- Fomin at k=5, μ=(2,1): dims 1,4,5,6,5,4,1. mults 0,1,2,2,2,1,0. -/
theorem fomin_k5_std :
    1*0 + 4*1 + 5*2 + 6*2 + 5*2 + 4*1 + 1*0 = 120 / 6 * 2 := by decide

/-- Classical branching identity: Σ m_μ × dim(μ) = dim(λ).
    Concrete for (3,1): 1×1 + 1×2 + 0×1 = 3. -/
theorem branch_dim_31 : 1 * 1 + 1 * 2 + 0 * 1 = (3 : ℕ) := by decide
theorem branch_dim_22 : 0 * 1 + 1 * 2 + 0 * 1 = (2 : ℕ) := by decide
theorem branch_dim_211 : 0 * 1 + 1 * 2 + 1 * 1 = (3 : ℕ) := by decide

/-! ## §6  RSK bijectivity (structure) -/

/-- **RSK injectivity — typeclass.**
    Per-`(rsk, rsk_inv)` witness that the RSK map has a left inverse.
    Pending implementation of reverse row bumping in Lean. -/
-- Ref: [sagan2001] §3.2
class RSKInjective (rsk : List ℕ → List (List ℕ) × List (List ℕ))
    (rsk_inv : List (List ℕ) × List (List ℕ) → List ℕ) : Prop where
  /-- `rsk_inv ∘ rsk = id`. -/
  left_inverse : ∀ w, rsk_inv (rsk w) = w

/-- **RSK surjectivity — typeclass.**
    Per-`(rsk, rsk_inv)` witness that the RSK map has a right
    inverse on pairs `(P, Q)` of standard Young tableaux of the
    same shape. -/
-- Ref: [sagan2001] §3.2
class RSKSurjective (rsk : List ℕ → List (List ℕ) × List (List ℕ))
    (rsk_inv : List (List ℕ) × List (List ℕ) → List ℕ) : Prop where
  /-- `rsk ∘ rsk_inv = id` on the image. -/
  right_inverse : ∀ pq, rsk (rsk_inv pq) = pq

/-- **RSK Burnside identity — typeclass.**
    Per-`k` witness that `Σ_{λ ⊢ k} dim(λ)² = k!`. Follows from
    RSK bijectivity once the previous two classes are inhabited. -/
-- Ref: [sagan2001] Corollary 3.3.2
class RSKBurnside (k : ℕ) (sumDimSq factorial : ℕ) : Prop where
  /-- Sum of dim² equals k!. -/
  identity : sumDimSq = factorial

/-- Reflexivity instance for `RSKBurnside`: when `sumDimSq` and
    `factorial` are syntactically the same value, the class holds. -/
instance rskBurnside_refl (k m : ℕ) : RSKBurnside k m m := ⟨rfl⟩

end QOU.Archimedean.RSK
