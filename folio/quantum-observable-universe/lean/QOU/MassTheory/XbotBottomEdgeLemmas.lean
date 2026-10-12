import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

/-!
# The two lemmas behind the Xbot bottom-edge certificate

Lean companion of `computations/deltalambda/rev_e_infinity_xbot_lnatural_probe.py`
(bean `qou-as81`), module docstring section *"The two lemmas"* and checks M7 / M8 / M9.

The probe's bottom-edge objective on a frame `pe` with a block of `n` rows is the
L♮-concave split form (its check M1)

  `G(u) = Σ_{j<n} φ_j(u_j) + Σ_{i<j<n} ψ_{ij}(u_j − u_i)`,

  `φ_j(x) = R(b_j) − R(b_j + x) + W(h_j) − W(h_j − x) − a·w_j·x − c·x²`,
  `ψ_{ij}(d) = ε(g_{ij}) − ε(g_{ij} + d)`,

with `b_j = j` for `j < pe`, `b_j = 2j − pe` above, `h_j = b_n − b_j`, `g_{ij} = b_j − b_i`,
`w_j = pe − j` (truncated), `R(x) = Σ_{k≥1} ε(x + k)` and `W` the above-block tail, which
depends on `(pe, n)` only through `m = pe − n` (truncated; the probe's `_D_coeffs`).  At integer
`x ≥ 0`, `R(b) − R(b + x) = Σ_{k<x} ε(b + 1 + k)` exactly, and that finite sum is what is used
below, so no series appears.  In the probe `a = ln q₀`, `c = (ln q₀)/2`, `ε(x) = −log(1 − T₂^{−x})`;
here all of `ε`, `W`, `a`, `c` are abstract.

## What is proved (all sorry-free)

1. **Shift identity** (all-pe lemma, algebraic half; the probe's M8).
   `pairObjective_shift` is the reindexing statement for an arbitrary two-body objective over an
   additive commutative group; `frameObjective_shift` instantiates it:
   `G_{pe+1}(0, u) = G_pe(u)` for **every** function `ε : ℤ → R`, every tail family `W`, and all
   coefficients — the identity is purely combinatorial (a telescoping of the bottom row's pair
   terms into the shifted one-body sums).
2. **Wall inequality** (all-pe lemma, analytic half; the probe's M9).
   `frameObjective_bottom_raise_lt`: on frame `P` with `n + 1` rows, if `ε` and `W_m` are
   antitone on the positive integers, `0 ≤ c`, and `ε(1) < a·P`, then raising the bottom row by
   `x ≥ 1` (at any point of the domain) strictly lowers `G`.  `frame_succ_le` combines it with
   the shift identity: every value of frame `pe + 1` is at most a value of frame `pe`, as soon as
   `ε(1) < a·(pe + 1)`; `wall_persists` shows that condition propagates to every larger frame
   when `a > 0`.  The numeric fact that the probe measures (`ε(1)/ln q₀ ≈ 16.0002`, so the
   condition first holds at `pe + 1 = 17`) is **not** asserted here; it enters only as the
   hypothesis `ε(1) < a·(pe + 1)`.
3. **Tail lemma, structural half** (the probe's M7).
   `pairObjective_move_gain` derives, for an arbitrary two-body objective, that the gain of a
   `+χ_H` move is `Σ_{j∈H}` (one-body change of `j` + the change of every pair with exactly one
   end, `j`, in `H`); pairs inside `H` cancel because their difference is unchanged.
   `tail_never_helps` then gives, for disjoint `L, H`:
   `gain(L ∪ H) ≤ gain(L) + |H|·β`, hence `< 0` when `H ≠ ∅`, `β < 0`, `gain(L) ≤ 0`.
   `antisymm_double_sum_eq_zero` is the finite half of the lattice cancellation (the `x ∈ H`
   part of `Σ_{j∈H} Σ_x sgn(j − x) P(|j − x|)` is antisymmetric, hence zero).

## What is NOT proved here (honest scope)

* The **per-row bracket bound** of the tail lemma — that each high row's contribution is at most
  `ε(b_N + 1) + c̄_N − (ln q₀)/2` — is the hypothesis `hrow` of `tail_never_helps`.  Deriving it
  needs the *infinite* gap-2 lattice cancellation (a convergent bi-infinite sum), the comparison
  of this frame's rows below `N` with the lattice's, and the monotonicity in `j` that makes row
  `N` the worst case.  None of that is formalised; only its finite antisymmetric piece is.
  The sign `bracket < 0` is the probe's numerical check M7 and is likewise a hypothesis.
* The L♮-concave optimality criterion itself (Murota 2003, Ch. 7) is not formalised; the tail
  lemma is stated for `+χ_S` moves, which is what that criterion reduces the certificate to.

-- Ref: [murota2003] Discrete Convex Analysis, SIAM, 2003, Ch. 7 (L♮ optimality criterion)
-/

namespace QOU.MassTheory
namespace XbotBottomEdge

open Finset

/-! ## The abstract two-body objective -/

section Abstract

variable {M : Type*} [AddCommGroup M]

/-- `G(u) = Σ_{j<n} φ_j(u_j) + Σ_{i<j<n} ψ_{ij}(u_j − u_i)` over integer displacements `u ≥ 0`. -/
def pairObjective (n : ℕ) (φ : ℕ → ℕ → M) (ψ : ℕ → ℕ → ℤ → M) (u : ℕ → ℕ) : M :=
  ∑ j ∈ range n, φ j (u j) + ∑ j ∈ range n, ∑ i ∈ range j, ψ i j ((u j : ℤ) - u i)

/-- Peel the bottom row off a two-body objective. -/
theorem pairObjective_succ_bottom (n : ℕ) (φ : ℕ → ℕ → M) (ψ : ℕ → ℕ → ℤ → M) (u : ℕ → ℕ) :
    pairObjective (n + 1) φ ψ u =
      φ 0 (u 0) + ∑ j ∈ range n, ψ 0 (j + 1) ((u (j + 1) : ℤ) - u 0)
        + pairObjective n (fun j => φ (j + 1)) (fun i j => ψ (i + 1) (j + 1))
            (fun j => u (j + 1)) := by
  unfold pairObjective
  rw [sum_range_succ' (fun j => φ j (u j)),
    sum_range_succ' (fun j => ∑ i ∈ range j, ψ i j ((u j : ℤ) - u i))]
  simp only [range_zero, sum_empty, add_zero]
  have h : ∀ j : ℕ, ∑ i ∈ range (j + 1), ψ i (j + 1) ((u (j + 1) : ℤ) - u i)
      = ∑ i ∈ range j, ψ (i + 1) (j + 1) ((u (j + 1) : ℤ) - u (i + 1))
        + ψ 0 (j + 1) ((u (j + 1) : ℤ) - u 0) := fun j => sum_range_succ' _ _
  simp only [h, sum_add_distrib]
  abel

/-- The block with an undisplaced bottom row prepended: `(0, u)`. -/
def bottomZero (u : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | j + 1 => u j

/-- **Shift identity, abstract form.**  If the rows `j ≥ 1` of `(φ', ψ')` are the rows `j − 1`
of `(φ, ψ)` — except that row `j + 1`'s one-body piece plus its pair with an undisplaced bottom
row equals `φ j` — and the bottom row's one-body piece vanishes at `0`, then
`G'(0, u) = G(u)`.  Pure reindexing of the two finite sums. -/
theorem pairObjective_shift (n : ℕ) (φ φ' : ℕ → ℕ → M) (ψ ψ' : ℕ → ℕ → ℤ → M) (u : ℕ → ℕ)
    (h0 : φ' 0 0 = 0)
    (hrow : ∀ j x : ℕ, φ' (j + 1) x + ψ' 0 (j + 1) (x : ℤ) = φ j x)
    (hpair : ∀ (i j : ℕ) (d : ℤ), ψ' (i + 1) (j + 1) d = ψ i j d) :
    pairObjective (n + 1) φ' ψ' (bottomZero u) = pairObjective n φ ψ u := by
  rw [pairObjective_succ_bottom]
  have hp : (fun i j => ψ' (i + 1) (j + 1)) = ψ := by
    funext i j d; exact hpair i j d
  simp only [bottomZero, h0, Nat.cast_zero, sub_zero, zero_add, hp]
  unfold pairObjective
  rw [← add_assoc, ← sum_add_distrib]
  congr 1
  refine sum_congr rfl fun j _ => ?_
  rw [add_comm]; exact hrow j (u j)

end Abstract

/-! ## The bottom-edge frame -/

section Frame

variable {R : Type*} [CommRing R]

/-- `b_j` in frame `pe`: `j` on the wall (`j < pe`), `2j − pe` on the gap-2 lattice above. -/
def rowBase (pe j : ℕ) : ℕ := if j < pe then j else 2 * j - pe

/-- The wall's linear weight `w_j = pe − j` (zero above the wall). -/
def wallWeight (pe j : ℕ) : ℕ := pe - j

theorem rowBase_succ (pe j : ℕ) : rowBase (pe + 1) (j + 1) = rowBase pe j + 1 := by
  unfold rowBase; split_ifs <;> omega

@[simp] theorem rowBase_zero (pe : ℕ) : rowBase pe 0 = 0 := by
  unfold rowBase; split_ifs <;> omega

theorem wallWeight_succ (pe j : ℕ) : wallWeight (pe + 1) (j + 1) = wallWeight pe j := by
  unfold wallWeight; omega

@[simp] theorem wallWeight_zero (pe : ℕ) : wallWeight pe 0 = pe := by
  unfold wallWeight; omega

/-- The one-body piece of row `j` at displacement `x`:
`Σ_{k<x} ε(b_j + 1 + k)` (`= R(b_j) − R(b_j + x)`) `+ W_m(h_j) − W_m(h_j − x) − a·w_j·x − c·x²`,
with `m = pe − n` and `h_j = b_n − b_j`. -/
def framePhi (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe n j x : ℕ) : R :=
  (∑ k ∈ range x, eps ((rowBase pe j : ℤ) + 1 + k))
    + (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
        - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - x))
    - a * (wallWeight pe j : R) * x - c * (x : R) ^ 2

/-- The pair piece of rows `i < j`: `ε(g_{ij}) − ε(g_{ij} + d)`, `g_{ij} = b_j − b_i`. -/
def framePsi (eps : ℤ → R) (pe i j : ℕ) (d : ℤ) : R :=
  eps ((rowBase pe j : ℤ) - rowBase pe i) - eps ((rowBase pe j : ℤ) - rowBase pe i + d)

/-- The bottom-edge objective of frame `pe` on an `n`-row block. -/
def frameObjective (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe n : ℕ) (u : ℕ → ℕ) : R :=
  pairObjective n (framePhi eps W a c pe n) (framePsi eps pe) u

/-- The telescoping behind the shift: a pair that closes from `ε(c) − ε(c + x)` plus the
one-body sum starting one step higher is the one-body sum starting at `c`. -/
theorem telescope (f : ℤ → R) (c : ℤ) (x : ℕ) :
    ∑ k ∈ range x, f (c + 1 + k) + (f c - f (c + x)) = ∑ k ∈ range x, f (c + k) := by
  induction x with
  | zero => simp
  | succ x ih =>
    rw [sum_range_succ, sum_range_succ, ← ih]
    have e1 : c + 1 + (x : ℤ) = c + ((x + 1 : ℕ) : ℤ) := by push_cast; ring
    rw [e1]
    abel

/-- **Shift identity (M8):** `G_{pe+1}(0, u) = G_pe(u)`, for every `ε`, `W`, `a`, `c`. -/
theorem frameObjective_shift (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe n : ℕ)
    (u : ℕ → ℕ) :
    frameObjective eps W a c (pe + 1) (n + 1) (bottomZero u) = frameObjective eps W a c pe n u := by
  unfold frameObjective
  apply pairObjective_shift
  · simp [framePhi]
  · intro j x
    simp only [framePhi, framePsi, rowBase_succ, rowBase_zero, wallWeight_succ,
      Nat.add_sub_add_right]
    push_cast
    have ht := telescope eps ((rowBase pe j : ℤ) + 1) x
    have e3 : (rowBase pe n : ℤ) + 1 - ((rowBase pe j : ℤ) + 1) = rowBase pe n - rowBase pe j := by
      ring
    simp only [sub_zero] at ht ⊢
    rw [e3, ← ht]
    ring
  · intro i j d
    simp only [framePsi, rowBase_succ]
    push_cast
    have e : (rowBase pe j : ℤ) + 1 - ((rowBase pe i : ℤ) + 1) = rowBase pe j - rowBase pe i := by
      ring
    rw [e]

/-- `Σ_{k<x} ε(1 + k) ≤ x·ε(1)` for `ε` antitone on the positive integers. -/
theorem sum_eps_le (eps : ℤ → R) [LinearOrder R] [IsStrictOrderedRing R]
    (heps : AntitoneOn eps (Set.Ioi 0)) (x : ℕ) :
    ∑ k ∈ range x, eps (1 + k) ≤ (x : R) * eps 1 := by
  have h : ∀ k ∈ range x, eps (1 + k) ≤ eps 1 := by
    intro k _
    apply heps
    · show (0 : ℤ) < 1; norm_num
    · show (0 : ℤ) < 1 + k; positivity
    · show (1 : ℤ) ≤ 1 + k; omega
  calc ∑ k ∈ range x, eps (1 + k) ≤ ∑ _k ∈ range x, eps 1 := sum_le_sum h
    _ = (x : R) * eps 1 := by simp [sum_const, card_range, nsmul_eq_mul]

/-- **Wall inequality (M9).**  On frame `P` with `n + 1` rows, at any point of the domain (every
`ε` and `W` argument touched by the bottom row positive), raising the bottom row by `x ≥ 1`
strictly lowers `G`, provided `ε` and `W_m` are antitone on the positive integers, `0 ≤ c`, and
`ε(1) < a·P`.  The one-body gain is at most `x·ε(1)`, the wall costs `a·P·x`, the tail and the
quadratic only cost, and the bottom row's pairs only close. -/
theorem frameObjective_bottom_raise_lt [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (P n : ℕ) (u : ℕ → ℕ)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hW : AntitoneOn (W (P - (n + 1))) (Set.Ioi 0))
    (hc : 0 ≤ c)
    (hx : 1 ≤ u 0)
    (hdomW : 0 < (rowBase P (n + 1) : ℤ) - u 0)
    (hdomPair : ∀ j ∈ range n, 0 < (rowBase P (j + 1) : ℤ) + ((u (j + 1) : ℤ) - u 0))
    (hwall : eps 1 < a * P) :
    frameObjective eps W a c P (n + 1) u
      < frameObjective eps W a c P (n + 1) (bottomZero (fun j => u (j + 1))) := by
  unfold frameObjective
  rw [pairObjective_succ_bottom, pairObjective_succ_bottom]
  simp only [bottomZero]
  -- the untouched upper block is literally the same on both sides
  apply add_lt_add_right
  -- one-body piece of the raised bottom row
  have hphi0 : framePhi eps W a c P (n + 1) 0 0 = 0 := by simp [framePhi]
  have hphi : framePhi eps W a c P (n + 1) 0 (u 0) ≤ (u 0 : R) * (eps 1 - a * P) := by
    simp only [framePhi, rowBase_zero, wallWeight_zero, Nat.cast_zero, sub_zero, zero_add]
    have hs := sum_eps_le eps heps (u 0)
    have hWle : W (P - (n + 1)) (rowBase P (n + 1) : ℤ)
        - W (P - (n + 1)) ((rowBase P (n + 1) : ℤ) - u 0) ≤ 0 := by
      have : W (P - (n + 1)) (rowBase P (n + 1) : ℤ)
          ≤ W (P - (n + 1)) ((rowBase P (n + 1) : ℤ) - u 0) := by
        apply hW
        · exact hdomW
        · show (0 : ℤ) < rowBase P (n + 1); omega
        · omega
      linarith
    have hq : 0 ≤ c * (u 0 : R) ^ 2 := by positivity
    have hs' : ∑ k ∈ range (u 0), eps (0 + 1 + (k : ℤ)) ≤ (u 0 : R) * eps 1 := by
      simpa using hs
    nlinarith
  have hneg : (u 0 : R) * (eps 1 - a * P) < 0 := by
    have : (0 : R) < u 0 := by exact_mod_cast hx
    have : eps 1 - a * P < 0 := by linarith
    nlinarith
  -- every pair of the bottom row closes
  have hpairs : ∑ j ∈ range n, framePsi eps P 0 (j + 1) ((u (j + 1) : ℤ) - u 0)
      ≤ ∑ j ∈ range n, framePsi eps P 0 (j + 1) ((u (j + 1) : ℤ) - (0 : ℕ)) := by
    apply sum_le_sum
    intro j hj
    simp only [framePsi, rowBase_zero, Nat.cast_zero, sub_zero]
    have := hdomPair j hj
    have hle : eps ((rowBase P (j + 1) : ℤ) + u (j + 1))
        ≤ eps ((rowBase P (j + 1) : ℤ) + ((u (j + 1) : ℤ) - u 0)) := by
      apply heps
      · exact this
      · show (0 : ℤ) < (rowBase P (j + 1) : ℤ) + u (j + 1); omega
      · omega
    linarith
  rw [hphi0]
  linarith

/-- **Frame `pe + 1` adds nothing (M8 + M9).**  When `ε(1) < a·(pe + 1)`, every value of the
`(pe + 1)`-frame objective at a domain point is at most a value of the `pe`-frame objective. -/
theorem frame_succ_le [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe n : ℕ) (u : ℕ → ℕ)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hW : AntitoneOn (W (pe + 1 - (n + 1))) (Set.Ioi 0))
    (hc : 0 ≤ c)
    (hdomW : 0 < (rowBase (pe + 1) (n + 1) : ℤ) - u 0)
    (hdomPair : ∀ j ∈ range n, 0 < (rowBase (pe + 1) (j + 1) : ℤ) + ((u (j + 1) : ℤ) - u 0))
    (hwall : eps 1 < a * (pe + 1 : ℕ)) :
    frameObjective eps W a c (pe + 1) (n + 1) u
      ≤ frameObjective eps W a c pe n (fun j => u (j + 1)) := by
  rw [← frameObjective_shift eps W a c pe n (fun j => u (j + 1))]
  rcases Nat.eq_zero_or_pos (u 0) with h0 | h0
  · apply le_of_eq
    congr 1
    funext j
    cases j with
    | zero => simp [bottomZero, h0]
    | succ j => simp [bottomZero]
  · exact le_of_lt (frameObjective_bottom_raise_lt eps W a c (pe + 1) n u heps hW hc h0
      hdomW hdomPair hwall)

/-- The wall condition persists: with `a > 0`, `ε(1) < a·P₀` gives `ε(1) < a·P` for all
`P ≥ P₀`, so the frames beyond the first one meeting it all reduce to it. -/
theorem wall_persists [LinearOrder R] [IsStrictOrderedRing R] (e1 a : R) (P₀ P : ℕ)
    (ha : 0 < a) (h : e1 < a * P₀) (hP : P₀ ≤ P) : e1 < a * P := by
  have : (P₀ : R) ≤ P := by exact_mod_cast hP
  nlinarith

end Frame

/-! ## The tail lemma: structural half -/

section Tail

variable {R : Type*} [CommRing R]

/-- The point `v + χ_H`. -/
def moveBy (v : ℕ → ℕ) (H : Finset ℕ) : ℕ → ℕ := fun j => if j ∈ H then v j + 1 else v j

/-- The change of the pair `{j, x}` when `j` alone moves up by one. -/
def crossChange (ψ : ℕ → ℕ → ℤ → R) (v : ℕ → ℕ) (j x : ℕ) : R :=
  if x < j then ψ x j ((v j : ℤ) + 1 - v x) - ψ x j ((v j : ℤ) - v x)
  else if j < x then ψ j x ((v x : ℤ) - (v j + 1)) - ψ j x ((v x : ℤ) - v j)
  else 0

/-- What row `j ∈ H` contributes to a `+χ_H` move: its one-body change plus the change of every
pair whose other end is outside `H`. -/
def rowGain (φ : ℕ → ℕ → R) (ψ : ℕ → ℕ → ℤ → R) (n : ℕ) (v : ℕ → ℕ) (H : Finset ℕ)
    (j : ℕ) : R :=
  (φ j (v j + 1) - φ j (v j)) + ∑ x ∈ range n \ H, crossChange ψ v j x

/-- Pair sum over `i < j < n` written as a full square sum, for swapping. -/
theorem pair_sum_square (n : ℕ) (f : ℕ → ℕ → R) :
    ∑ j ∈ range n, ∑ i ∈ range j, f i j
      = ∑ j ∈ range n, ∑ i ∈ range n, if i < j then f i j else 0 := by
  refine sum_congr rfl fun j hj => ?_
  rw [← sum_filter]
  congr 1
  ext i
  simp only [mem_range, mem_filter] at hj ⊢
  omega

/-- **Move-gain decomposition.**  For any two-body objective and `H ⊆ range n`, the gain of the
move `+χ_H` is `Σ_{j∈H}` (one-body change of `j` + change of each pair with exactly one end, `j`,
in `H`).  Pairs with both ends in `H` keep their difference and contribute nothing. -/
theorem pairObjective_move_gain (n : ℕ) (φ : ℕ → ℕ → R) (ψ : ℕ → ℕ → ℤ → R) (v : ℕ → ℕ)
    (H : Finset ℕ) (hH : H ⊆ range n) :
    pairObjective n φ ψ (moveBy v H) - pairObjective n φ ψ v
      = ∑ j ∈ H, rowGain φ ψ n v H j := by
  unfold pairObjective rowGain
  rw [pair_sum_square, pair_sum_square, sum_add_distrib]
  have hHs : ∀ g : ℕ → R, ∑ j ∈ H, g j = ∑ j ∈ range n, if j ∈ H then g j else 0 := by
    intro g
    rw [← sum_filter]
    congr 1
    ext j; simp only [mem_filter]; constructor
    · exact fun h => ⟨hH h, h⟩
    · exact fun h => h.2
  -- one-body part
  have hone : ∑ j ∈ range n, φ j (moveBy v H j) - ∑ j ∈ range n, φ j (v j)
      = ∑ j ∈ H, (φ j (v j + 1) - φ j (v j)) := by
    rw [← sum_sub_distrib, hHs]
    refine sum_congr rfl fun j _ => ?_
    by_cases hj : j ∈ H <;> simp [moveBy, hj]
  -- pair part
  have hpair : ∑ j ∈ range n, ∑ i ∈ range n,
        (if i < j then ψ i j ((moveBy v H j : ℤ) - moveBy v H i) else 0)
      - ∑ j ∈ range n, ∑ i ∈ range n, (if i < j then ψ i j ((v j : ℤ) - v i) else 0)
      = ∑ j ∈ H, ∑ x ∈ range n \ H, crossChange ψ v j x := by
    rw [← sum_sub_distrib]
    simp_rw [← sum_sub_distrib]
    -- the target as a square sum over (j, x) ∈ range n × range n
    have hT : ∑ j ∈ H, ∑ x ∈ range n \ H, crossChange ψ v j x
        = ∑ j ∈ range n, ∑ x ∈ range n,
            (if j ∈ H ∧ x ∉ H then crossChange ψ v j x else 0) := by
      rw [hHs]
      refine sum_congr rfl fun j _ => ?_
      by_cases hj : j ∈ H
      · simp only [hj, if_true, true_and]
        rw [← sum_filter]
        congr 1
        ext x; simp [mem_sdiff]
      · simp [hj]
    rw [hT]
    -- split crossChange into its two halves and swap the second
    have hsplit : ∀ j x, (if j ∈ H ∧ x ∉ H then crossChange ψ v j x else 0)
        = (if j ∈ H ∧ x ∉ H ∧ x < j then
              ψ x j ((v j : ℤ) + 1 - v x) - ψ x j ((v j : ℤ) - v x) else 0)
          + (if j ∈ H ∧ x ∉ H ∧ j < x then
              ψ j x ((v x : ℤ) - (v j + 1)) - ψ j x ((v x : ℤ) - v j) else 0) := by
      intro j x
      unfold crossChange
      by_cases h1 : j ∈ H <;> by_cases h2 : x ∈ H <;> simp only [h1, h2] <;>
        rcases lt_trichotomy x j with h | h | h <;> simp [h, not_lt_of_gt]
    simp_rw [hsplit, sum_add_distrib]
    rw [sum_comm (s := range n) (t := range n)
      (f := fun j x => if j ∈ H ∧ x ∉ H ∧ j < x then
        ψ j x ((v x : ℤ) - (v j + 1)) - ψ j x ((v x : ℤ) - v j) else 0)]
    rw [← sum_add_distrib]
    refine sum_congr rfl fun j _ => ?_
    rw [← sum_add_distrib]
    refine sum_congr rfl fun i _ => ?_
    by_cases hij : i < j
    · -- both ends moved, or neither: the difference is unchanged; one end: a cross change
      by_cases hj : j ∈ H <;> by_cases hi : i ∈ H <;> simp [moveBy, hij, hj, hi]
    · by_cases hj : j ∈ H <;> by_cases hi : i ∈ H <;> simp [hij, hj, hi]
  rw [show ∀ a b c d : R, a + b - (c + d) = (a - c) + (b - d) from fun _ _ _ _ => by abel,
    hone, hpair]

/-- `v + χ_{L ∪ H} = (v + χ_L) + χ_H` for disjoint `L`, `H`. -/
theorem moveBy_union (v : ℕ → ℕ) (L H : Finset ℕ) (hd : Disjoint L H) :
    moveBy v (L ∪ H) = moveBy (moveBy v L) H := by
  funext j
  by_cases hL : j ∈ L <;> by_cases hH : j ∈ H
  · exact absurd hH (Finset.disjoint_left.mp hd hL)
  · simp [moveBy, hL, hH]
  · simp [moveBy, hL, hH]
  · simp [moveBy, hL, hH]

/-- **Tail lemma (M7), structural form.**  Split a move `S = L ∪ H` (disjoint, inside the block).
If every row of `H` contributes at most `β` (the per-row bracket — the hypothesis that carries
the lattice-cancellation estimate), then `gain(S) ≤ gain(L) + |H|·β`; with `β < 0`,
`gain(L) ≤ 0` and `H ≠ ∅` the move strictly loses, so the rows of `H` never help. -/
theorem tail_never_helps [LinearOrder R] [IsStrictOrderedRing R]
    (n : ℕ) (φ : ℕ → ℕ → R) (ψ : ℕ → ℕ → ℤ → R) (u : ℕ → ℕ) (L H : Finset ℕ)
    (hd : Disjoint L H) (hH : H ⊆ range n) (β : R)
    (hrow : ∀ j ∈ H, rowGain φ ψ n (moveBy u L) H j ≤ β) :
    pairObjective n φ ψ (moveBy u (L ∪ H)) - pairObjective n φ ψ u
      ≤ (pairObjective n φ ψ (moveBy u L) - pairObjective n φ ψ u) + (H.card : R) * β := by
  have hg := pairObjective_move_gain n φ ψ (moveBy u L) H hH
  have hs : ∑ j ∈ H, rowGain φ ψ n (moveBy u L) H j ≤ (H.card : R) * β := by
    calc ∑ j ∈ H, rowGain φ ψ n (moveBy u L) H j ≤ ∑ _j ∈ H, β := sum_le_sum hrow
      _ = (H.card : R) * β := by simp [sum_const, nsmul_eq_mul]
  rw [moveBy_union u L H hd]
  linarith

/-- The strict form: a move touching the tail rows `H ≠ ∅` loses, given a negative bracket and a
non-improving lower part. -/
theorem tail_move_lt_zero [LinearOrder R] [IsStrictOrderedRing R]
    (n : ℕ) (φ : ℕ → ℕ → R) (ψ : ℕ → ℕ → ℤ → R) (u : ℕ → ℕ) (L H : Finset ℕ)
    (hd : Disjoint L H) (hH : H ⊆ range n) (hne : H.Nonempty) (β : R) (hβ : β < 0)
    (hL : pairObjective n φ ψ (moveBy u L) - pairObjective n φ ψ u ≤ 0)
    (hrow : ∀ j ∈ H, rowGain φ ψ n (moveBy u L) H j ≤ β) :
    pairObjective n φ ψ (moveBy u (L ∪ H)) - pairObjective n φ ψ u < 0 := by
  have h := tail_never_helps n φ ψ u L H hd hH β hrow
  have hc : (0 : R) < H.card := by exact_mod_cast hne.card_pos
  have : (H.card : R) * β < 0 := mul_neg_of_pos_of_neg hc hβ
  linarith

/-- The finite half of the lattice cancellation: an antisymmetric kernel summed over `H × H`
vanishes. -/
theorem antisymm_double_sum_eq_zero [LinearOrder R] [IsStrictOrderedRing R]
    (H : Finset ℕ) (f : ℕ → ℕ → R) (hf : ∀ i j, f i j = - f j i) :
    ∑ i ∈ H, ∑ j ∈ H, f i j = 0 := by
  have h : ∑ i ∈ H, ∑ j ∈ H, f i j = - ∑ i ∈ H, ∑ j ∈ H, f i j := by
    conv_lhs => rw [sum_comm]
    simp only [← sum_neg_distrib]
    exact sum_congr rfl fun i _ => sum_congr rfl fun j _ => hf j i
  linarith

end Tail

end XbotBottomEdge
end QOU.MassTheory
