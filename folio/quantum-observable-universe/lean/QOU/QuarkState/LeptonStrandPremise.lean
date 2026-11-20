/-
# The lepton-strand premise of the β amplitude, and which passage the corpus selects

Bean `qou-99qc` (N1), also `qou-g0jn`. Owner (Carl), 2026-11-20: *derive, don't choose*. Pre-registered in
`computations/probes/lepton_strand_premise/PREREGISTRATION.md`.

`ChargedCurrentW.lean` (#8638) computes `n ⊗ ν → e⁻ ⊗ p` as `(h·q)·T⁺` (leftward positive passage
`σ₁σ₂σ₃`) or `−(h/q)·T⁺` (rightward negative passage `σ₃⁻¹σ₂⁻¹σ₁⁻¹`). It rests on the premise L (the lepton
is a fourth strand carrying the same doublet `V`, `ν = u`, `e⁻ = d`) and leaves open which passage is physical.

## Part A — inside L, the assignment `ν = u, e⁻ = d` is forced (scope (b), invariant: total `T³`)

`2T³` of a strand is `w u = 1`, `w d = −1`; `n = udd` has `−1`, `p = uud` has `+1`.
* `lepton_assignment_forced` : `w(n) + w(ℓ) = w(p) + w(ℓ')` iff `ℓ = u ∧ ℓ' = d`.
* `singlet_lepton_excluded` : a lepton strand with no weight change cannot balance `n → p`.
* `gmn_forces_order` : with `Q = (w + Y)/2` and one `Y` for the lepton doublet, `Q(ℓ) − Q(ℓ') = 1`
  (`= Q(ν) − Q(e⁻) = 0 − (−1)`) iff `ℓ = u ∧ ℓ' = d`; and then `Q(ν) = 0` fixes `Y = −1`.
* The conservation law itself: `Rc_commute_Kt` (`Ř` commutes with `K ⊗ K`) and
  `entry_eq_zero_of_commute_diagonal` + `zpow_ne_of_ne` (for `1 < q`, an operator commuting with the
  weight operator has no matrix element between different total weights).

So, GIVEN L, the label `ν = u, e⁻ = d` is not an extra choice. L itself is not implied by any corpus
definition (`def:electron-knot` = trefoil, `def:neutrino-knot` = unknot, β⁻ = the `L₀⁻` skein smoothing of
`def:antineutrino-knot`): underdetermined; see the PR body for the alternatives.

## Part B — the owner-ruled left line does NOT select the passage

On `V ⊗ V`, `P₊ = q/(q²+1)·(Ř + q⁻¹)` is the left line for `q > 1`.
* `sigma_on_left`, `sigmaInv_on_left` : `Ř` and `Ř⁻¹` are both scalars (`q`, `q⁻¹`) on the same line, so the
  left line does not distinguish a positive from a negative crossing (as `LeftLineDefinition` item 1).
* `WL_eq`, `WR_eq` : the left-line weak vertex is `W_L = q⁻¹(P₊ − P₋)`, the other side `W_R = q(P₊ − P₋)`.
* `WL_beta_both` : strand-tracked, `W_L` changes flavour in BOTH strand orientations, with equal magnitude
  `(q²−1)/(q(q²+1))`. So the weak vertex is blind to the direction in which the lepton passes.
* `WR_beta_ratio` : `W_R`'s β entry is `q²` times `W_L`'s, the same `q²` that separates the two passages
  (`hq` vs `h/q`), with the owner's `W_L` on the `q⁻¹` side. This is a scale coincidence, not a selection.

## Part C — what does select: the corpus orientation of `e⁻` and `ν` (CONDITIONAL on a bridge)

Of the four single-sign passages only two have a β block: `beta_left_pos` (`= (q²−1)·T⁺`),
`beta_right_neg` (`= −((q²−1)/q²)·T⁺`), `beta_left_neg = 0`, `beta_right_pos = 0`. So
`passage_nonzero_iff` : the block is nonzero iff (leftward ↔ positive). The corpus draws `e⁻` as the positive
braid `σ₁³` (`electron_word_writhe`, solid, forward time) and `ν̄` with negative orientation (so the incoming
`ν` is positive). `positive_selects_left` : the only nonzero passage whose crossings are positive is the
leftward positive one, coupling `hq` (C-lep). The step "the knot's chirality is the strand's crossing sign"
is a bridge, not a theorem.

## Part D — three different electrons

* `perm_e_gg`, `e_gg_fixed_strand`, `e_gg_moves` : the γγ coordinate `e⁻ = σ₀σ₁σ₀` has permutation
  `(0 2)` with strand `1` fixed, so its closure has at least two components (a strand closing on itself, plus
  the `(0 2)` cycle).
* `trefoil_perm`, `trefoil_one_component` : `σ₁³` has a fixed-point-free transposition on two strands, so its
  closure `T(2,3)` has exactly one component. So `σ₀σ₁σ₀` is not the trefoil electron.
* The strand electron of L is a weight vector on one strand, not a braid word; a Hecke element cannot change
  `T³` (`Rc_commute_Kt`), so neither knot is that state.

Base ring (§7c): generic `[Field K]`; an ordered field only for `zpow_ne_of_ne`. No `ℝ`, no `sorry`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII (universal R-matrix of U_q(sl₂))
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Field.Power
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm

namespace QOU.QuarkState.LeptonStrandPremise

open Matrix

/-! ## Part A: weights -/

/-- Flavour of one doublet strand. -/
inductive Fl | u | d
  deriving DecidableEq

/-- `2T³` of a strand. -/
def w : Fl → ℤ
  | .u => 1
  | .d => -1

/-- `2T³(udd)`. -/
def wNeutron : ℤ := w .u + w .d + w .d
/-- `2T³(uud)`. -/
def wProton : ℤ := w .u + w .u + w .d

/-- **Inside L the lepton labels are forced:** `n ℓ → p ℓ'` conserves `T³` iff `ℓ = u`, `ℓ' = d`. -/
theorem lepton_assignment_forced (ℓ ℓ' : Fl) :
    wNeutron + w ℓ = wProton + w ℓ' ↔ ℓ = .u ∧ ℓ' = .d := by
  cases ℓ <;> cases ℓ' <;> simp [wNeutron, wProton, w]

/-- A lepton line that carries the same weight in and out (e.g. a singlet) cannot balance `n → p`. -/
theorem singlet_lepton_excluded (a : ℤ) : wNeutron + a ≠ wProton + a := by
  simp [wNeutron, wProton, w]

/-- `Q = T³ + Y/2`, with `2T³ = w`. -/
def charge (ℓ : Fl) (Y : ℚ) : ℚ := ((w ℓ : ℚ) + Y) / 2

/-- **Gell-Mann–Nishijima with one `Y` per doublet forces the same order:** `Q(ℓ) − Q(ℓ') = 1`
(the value `Q(ν) − Q(e⁻) = 0 − (−1)`) iff `ℓ = u ∧ ℓ' = d`. -/
theorem gmn_forces_order (Y : ℚ) (ℓ ℓ' : Fl) :
    charge ℓ Y - charge ℓ' Y = 1 ↔ ℓ = .u ∧ ℓ' = .d := by
  cases ℓ <;> cases ℓ' <;> norm_num [charge, w] <;> (try ring_nf) <;> (try norm_num) <;> (try decide)

/-- With `ν = u` and `Q(ν) = 0` the lepton hypercharge is `−1`, and then `Q(e⁻) = −1`. -/
theorem lepton_hypercharge (Y : ℚ) (h : charge .u Y = 0) : Y = -1 ∧ charge .d Y = -1 := by
  simp [charge, w] at h ⊢
  constructor <;> linarith

variable {K : Type*} [Field K]

/-- **An operator commuting with a diagonal weight operator has no entry between distinct weights.** -/
theorem entry_eq_zero_of_commute_diagonal {n : Type*} [Fintype n] [DecidableEq n]
    {X : Matrix n n K} {D : n → K} (hc : X * diagonal D = diagonal D * X) {i j : n}
    (hij : D i ≠ D j) : X i j = 0 := by
  have h := congrFun (congrFun hc i) j
  simp only [mul_diagonal, diagonal_mul] at h
  have h2 : X i j * (D j - D i) = 0 := by linear_combination h
  rcases mul_eq_zero.mp h2 with h3 | h3
  · exact h3
  · exact absurd (sub_eq_zero.mp h3).symm hij

/-- For `1 < q`, distinct integer weights give distinct eigenvalues `q^a`. -/
theorem zpow_ne_of_ne {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {q : L}
    (hq : 1 < q) {a b : ℤ} (hab : a ≠ b) : q ^ a ≠ q ^ b :=
  fun h => hab ((zpow_right_strictMono₀ hq).injective h)

/-- Jimbo `Ř` on `V ⊗ V`, basis `uu, ud, du, dd` (as in `ChargedCurrentW`, #8638). -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- `K ⊗ K = diag(q², 1, 1, q⁻²)`, the total-weight operator. -/
def Kt (q : K) : Matrix (Fin 4) (Fin 4) K := diagonal ![q ^ 2, 1, 1, q⁻¹ ^ 2]

/-- Entrywise check of a `4 × 4` identity. -/
local macro "mat4" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

/-- **`Ř` conserves total weight.** -/
theorem Rc_commute_Kt (q : K) : Rc q * Kt q = Kt q * Rc q := by
  simp only [Rc, Kt]; mat4

/-! ## Part B: the left line on `V ⊗ V` -/

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- `Ř⁻¹ = Ř − h`. -/
def Rinv (q : K) : Matrix (Fin 4) (Fin 4) K := Rc q - hh q • 1

/-- The `q`-line projector `P₊ = (Ř + q⁻¹)/[2]`, written out (the owner's left line for `q > 1`). -/
def Pp (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![1, 0, 0, 0; 0, 1 / (q ^ 2 + 1), q / (q ^ 2 + 1), 0;
     0, q / (q ^ 2 + 1), q ^ 2 / (q ^ 2 + 1), 0; 0, 0, 0, 1]

/-- The `−q⁻¹`-line projector `P₋ = 1 − P₊`. -/
def Pm (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![0, 0, 0, 0; 0, q ^ 2 / (q ^ 2 + 1), -(q / (q ^ 2 + 1)), 0;
     0, -(q / (q ^ 2 + 1)), 1 / (q ^ 2 + 1), 0; 0, 0, 0, 0]

/-- `P₊` is `(Ř + q⁻¹)/[2]`. -/
theorem Pp_formula (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) :
    Pp q = (q / (q ^ 2 + 1)) • (Rc q + q⁻¹ • 1) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [Pp, Rc, Matrix.one_apply] <;> field_simp <;> (try ring)

theorem Pp_add_Pm (q : K) (hb : q ^ 2 + 1 ≠ 0) : Pp q + Pm q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [Pp, Pm, Matrix.one_apply] <;> field_simp <;> ring

/-- The swap `P` (strand tracking). -/
def swap4 : Matrix (Fin 4) (Fin 4) K := !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

theorem Rinv_mul (q : K) (hq : q ≠ 0) : Rc q * Rinv q = 1 := by
  simp only [Rc, Rinv, hh]; mat4

/-- `σ` acts on the left line by `q`. -/
theorem sigma_on_left (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) : Rc q * Pp q = q • Pp q := by
  simp only [Rc, Pp]; mat4

/-- `σ` acts on the right line by `−q⁻¹`. -/
theorem sigma_on_right (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) : Rc q * Pm q = (-q⁻¹) • Pm q := by
  simp only [Rc, Pm]; mat4

/-- **`σ⁻¹` acts on the SAME line by `q⁻¹`:** the left line does not tell the two crossings apart. -/
theorem sigmaInv_on_left (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) :
    Rinv q * Pp q = q⁻¹ • Pp q := by
  simp only [Rinv, Rc, Pp, hh]; mat4

/-- The left-line weak vertex `W_L = σ⁻¹P₊ + σP₋`. -/
def WL (q : K) : Matrix (Fin 4) (Fin 4) K := Rinv q * Pp q + Rc q * Pm q

/-- The other side, `W_R = σP₊ + σ⁻¹P₋`. -/
def WR (q : K) : Matrix (Fin 4) (Fin 4) K := Rc q * Pp q + Rinv q * Pm q

theorem WL_eq (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) : WL q = q⁻¹ • (Pp q - Pm q) := by
  simp only [WL, Rinv, Rc, Pp, Pm, hh]; mat4

theorem WR_eq (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) : WR q = q • (Pp q - Pm q) := by
  simp only [WR, Rinv, Rc, Pp, Pm, hh]; mat4

/-- **`W_L` is blind to the direction of passage:** strand-tracked it changes flavour with the quark on the
left (`du ↦ ud`, entry `(1,2)`) AND with the quark on the right (`ud ↦ du`, entry `(2,1)`), with equal
magnitude. (Contrast `σ`: only `(1,2)`; `σ⁻¹`: only `(2,1)`, as in #8638.) -/
theorem WL_beta_both (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) :
    ((swap4 : Matrix (Fin 4) (Fin 4) K) * WL q) 1 2 = (q ^ 2 - 1) / (q * (q ^ 2 + 1)) ∧
    ((swap4 : Matrix (Fin 4) (Fin 4) K) * WL q) 2 1 = -((q ^ 2 - 1) / (q * (q ^ 2 + 1))) := by
  rw [WL_eq q hq hb]
  constructor <;>
    (simp [swap4, Pp, Pm, Matrix.mul_apply, Fin.sum_univ_four]; (try field_simp); (try ring))

/-- `W_R`'s β entry is `q²` times `W_L`'s. -/
theorem WR_beta_ratio (q : K) (hq : q ≠ 0) (hb : q ^ 2 + 1 ≠ 0) :
    ((swap4 : Matrix (Fin 4) (Fin 4) K) * WR q) 1 2 = q ^ 2 * ((swap4 : Matrix (Fin 4) (Fin 4) K) * WL q) 1 2 := by
  rw [WR_eq q hq hb, WL_eq q hq hb]
  simp [swap4, Pp, Pm, Rc, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply]
  field_simp

/-! ## Part C: the four single-sign passages (sector of `V^{⊗4}` with two `u`, as in #8638) -/

/-- `σ₁` on the sector `uudd, udud, uddu, duud, dudu, dduu`. -/
def S1 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 0, 1, 0, 0; 0, 0, 0, 0, 1, 0;
     0, 1, 0, q - q⁻¹, 0, 0; 0, 0, 1, 0, q - q⁻¹, 0; 0, 0, 0, 0, 0, q]

/-- `σ₂` on the sector. -/
def S2 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![0, 1, 0, 0, 0, 0; 1, q - q⁻¹, 0, 0, 0, 0; 0, 0, q, 0, 0, 0;
     0, 0, 0, q, 0, 0; 0, 0, 0, 0, 0, 1; 0, 0, 0, 0, 1, q - q⁻¹]

/-- `σ₃` on the sector. -/
def S3 (q : K) : Matrix (Fin 6) (Fin 6) K :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0; 0, 1, q - q⁻¹, 0, 0, 0;
     0, 0, 0, 0, 1, 0; 0, 0, 0, 1, q - q⁻¹, 0; 0, 0, 0, 0, 0, q]

/-- `σᵢ⁻¹ = σᵢ − h`. -/
def inv6 (S : Matrix (Fin 6) (Fin 6) K) (q : K) : Matrix (Fin 6) (Fin 6) K := S - hh q • 1

/-- `T⁺ = Δ²(E)`. -/
def Eu (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q; 1, 0, 1; q⁻¹, 1, 0]

/-- `n ⊗ ν` (lepton at position 4). -/
def inNnu : Fin 3 → Fin 6 := ![2, 4, 5]
/-- `e⁻ ⊗ p` (lepton at position 1). -/
def outEp : Fin 3 → Fin 6 := ![5, 4, 3]
/-- `ν ⊗ n` (lepton at position 1). -/
def inNuN : Fin 3 → Fin 6 := ![0, 1, 2]
/-- `p ⊗ e⁻` (lepton at position 4). -/
def outPe : Fin 3 → Fin 6 := ![3, 1, 0]

/-- The β block of a passage: `leftward = true` is `σ₁σ₂σ₃`-type (lepton 4 → 1), `false` is
`σ₃σ₂σ₁`-type (lepton 1 → 4); `positive` chooses `σᵢ` or `σᵢ⁻¹` at every crossing. -/
def betaBlock (leftward positive : Bool) (q : K) : Matrix (Fin 3) (Fin 3) K :=
  let s : Matrix (Fin 6) (Fin 6) K → Matrix (Fin 6) (Fin 6) K := fun S => if positive then S else inv6 S q
  if leftward then (s (S1 q) * s (S2 q) * s (S3 q)).submatrix outEp inNnu
  else (s (S3 q) * s (S2 q) * s (S1 q)).submatrix outPe inNuN

/-- Entrywise check for the `3 × 3` blocks of `6 × 6` products. -/
local macro "blk" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_succ, Matrix.one_apply, Matrix.submatrix_apply,
      S1, S2, S3, inv6, hh, Eu, inNnu, outEp, inNuN, outPe] <;> (try field_simp) <;> (try ring)))

theorem beta_left_pos (q : K) (hq : q ≠ 0) : betaBlock true true q = (q ^ 2 - 1) • Eu q := by
  simp only [betaBlock, if_true]; blk; all_goals simp

theorem beta_left_neg (q : K) : betaBlock true false q = 0 := by
  simp only [betaBlock, if_true, Bool.false_eq_true, if_false]; blk

theorem beta_right_pos (q : K) : betaBlock false true q = 0 := by
  simp only [betaBlock, if_true, Bool.false_eq_true, if_false]; blk

theorem beta_right_neg (q : K) (hq : q ≠ 0) :
    betaBlock false false q = (-((q ^ 2 - 1) / q ^ 2)) • Eu q := by
  simp only [betaBlock, Bool.false_eq_true, if_false]; blk

/-- `T⁺` has the entry `1` at `(1,0)`. -/
theorem Eu_one_zero (q : K) : Eu q 1 0 = 1 := by simp [Eu]

/-- **Only two passages carry the β block:** nonzero iff (leftward ↔ positive), for `q² ≠ 1`. -/
theorem passage_nonzero_iff (q : K) (hq : q ≠ 0) (h1 : q ^ 2 ≠ 1) (l p : Bool) :
    betaBlock l p q ≠ 0 ↔ l = p := by
  cases l <;> cases p
  · simp only [ne_eq, iff_true]
    rw [beta_right_neg q hq]; intro h
    have := congrFun (congrFun h 1) 0
    simp [Eu] at this
    rcases this with h2 | h2
    · exact h1 (by linear_combination h2)
    · exact hq h2
  · simp [beta_right_pos q]
  · simp [beta_left_neg q]
  · simp only [ne_eq, iff_true]
    rw [beta_left_pos q hq]; intro h
    have := congrFun (congrFun h 1) 0
    simp [Eu] at this
    exact h1 (by linear_combination this)

/-- Crossing signs of the corpus electron word `σ₁³` (`def:electron-knot`, solid trefoil). -/
def electronWord : List ℤ := [1, 1, 1]

/-- Its writhe is `+3`: the corpus electron is drawn with positive crossings. -/
theorem electron_word_writhe : electronWord.sum = 3 := by decide

/-- **The corpus orientation selects the C-lep passage (conditional on the bridge):** among the passages
that carry the β block, the only one whose crossings are positive (the sign of `electronWord`) is the
leftward one, with block `(q² − 1)·T⁺ = (h·q)·T⁺`. -/
theorem positive_selects_left (q : K) (hq : q ≠ 0) (h1 : q ^ 2 ≠ 1) (l : Bool) :
    betaBlock l true q ≠ 0 ↔ l = true := by
  rw [passage_nonzero_iff q hq h1]

/-! ## Part D: the γγ `e⁻ = σ₀σ₁σ₀` and the trefoil are different closures -/

/-- The permutation of `σ₀σ₁σ₀` is the transposition `(0 2)`. -/
theorem perm_e_gg :
    (Equiv.swap (0 : Fin 3) 1) * Equiv.swap 1 2 * Equiv.swap 0 1 = Equiv.swap 0 2 := by decide

/-- Strand `1` closes on itself. -/
theorem e_gg_fixed_strand : (Equiv.swap (0 : Fin 3) 2) 1 = 1 := by decide

/-- Strands `0` and `2` form a second component. -/
theorem e_gg_moves : (Equiv.swap (0 : Fin 3) 2) 0 = 2 := by decide

/-- The permutation of `σ₁³` is the transposition of the two strands. -/
theorem trefoil_perm : (Equiv.swap (0 : Fin 2) 1) ^ 3 = Equiv.swap 0 1 := by decide

/-- It has no fixed strand, and on two strands that is a single cycle: one component. -/
theorem trefoil_one_component : ∀ i : Fin 2, ((Equiv.swap (0 : Fin 2) 1) ^ 3) i ≠ i := by decide

end QOU.QuarkState.LeptonStrandPremise
