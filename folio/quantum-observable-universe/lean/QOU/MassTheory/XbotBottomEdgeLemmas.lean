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
3. **Tail lemma, structural half and per-row bracket bound** (the probe's M7; bean `qou-xbl8`).
   `pairObjective_move_gain` derives, for an arbitrary two-body objective, that the gain of a
   `+χ_H` move is `Σ_{j∈H}` (one-body change of `j` + the change of every pair with exactly one
   end, `j`, in `H`); pairs inside `H` cancel because their difference is unchanged.
   `tail_never_helps` then gives, for disjoint `L, H`:
   `gain(L ∪ H) ≤ gain(L) + |H|·β`, hence `< 0` when `H ≠ ∅`, `β < 0`, `gain(L) ≤ 0`.
   For the per-row bracket bound `hrow` itself (`qou-xbl8`):
   - **(i) Gap-2 lattice cancellation**: `latticeKernel_antisymm`, `latticeKernel_sum_self_eq_zero`,
     `latticeKernel_sum_sdiff_eq`, and `symmetric_gap2_lattice_sum_eq_zero` prove that on the
     signed lattice kernel `sgn(j − x) P(|j − x|)`, the `H × H` part vanishes by antisymmetry and
     symmetric lower/upper gap-2 steps `±P(2(m+1))` around row `j` cancel identically.
   - **(ii) Frame comparison below `N`**: `crossChange_framePsi_of_lt`, `crossChange_framePsi_of_gt`,
     `activeCross_le_cbarAt`, and `rowGain_le_rowBracket` decompose row `j`'s gain at a zero-padded
     base point (`j ≥ N ≥ pe`) into the one-body piece `ε(b_j + 1) − c`, the wall/displaced rows
     `x < N` (`≤ c̄_N(j) = Σ_{x<N : x<pe ∨ w_x>0} p⁻(b_j − b_x − w_x)`), and the undisplaced
     gap-2 lattice rows plus upper tail (`≤ 0` after lattice cancellation), yielding
     `rowGain j ≤ rowBracket eps pe w c N j`.
   - **(iii) Monotonicity in `j ≥ N`**: `rowBase_strictMono_of_ge`, `cbarAt_antitone`, and
     `rowBracket_antitone` prove that `rowBracket eps pe w c N j ≤ rowBracket eps pe w c N N` for
     every `j ≥ N ≥ pe`, making row `N` the worst case and discharging `hrow` in
     `frame_tail_never_helps` and `frame_tail_move_lt_zero`.

## What is NOT proved here (honest scope)

* The numeric sign `rowBracket eps pe w c N N < 0` at `c = (ln q₀)/2` is the probe's numerical
  check M7 and enters as the hypothesis `hβ : rowBracket eps pe w c N N < 0`.
* The L♮-concave optimality criterion itself (Murota 2003, Ch. 7) is proved in
  `QOU/BraidKnot/LNaturalOptimality.lean` (`global_of_local_boxDiffDomain`, bean `qou-r9a6`).

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

/-! ## The per-row bracket bound of the tail lemma (bean `qou-xbl8`)

Derives the hypothesis `hrow` of `tail_never_helps` / `tail_move_lt_zero` for the bottom-edge
frame objective in three steps matching `rev_e_infinity_xbot_lnatural_probe.py` (check M7):

1. **Gap-2 lattice cancellation**: on the signed lattice kernel `sgn(j − x) P(|j − x|)`, the
   `H × H` sum vanishes (`latticeKernel_sum_self_eq_zero`), so summing over `x ∈ U \ H` equals
   summing over all `x ∈ U` (`latticeKernel_sum_sdiff_eq`), and on a symmetric gap-2 window around
   `j` the lower `+P(2(m+1))` and upper `−P(2(m+1))` steps cancel (`symmetric_gap2_lattice_sum_eq_zero`).
2. **Frame comparison below `N`**: decomposing a high row `j ∈ H` (`N ≤ j < n`, `pe ≤ N`) into
   its one-body piece `ε(b_j + 1) − c`, the wall/displaced rows `x < N` (`x < pe ∨ 0 < w_x`), and
   the undisplaced gap-2 lattice rows plus upper tail bounds `rowGain j` by
   `rowBracket eps pe w c N j = ε(b_j + 1) + c̄_N(j) − c` (`rowGain_le_rowBracket`).
3. **Monotonicity in `j ≥ N`**: `b_j = 2j − pe` is strictly increasing for `j ≥ pe`, so with `ε`
   and `p⁻` antitone, both `ε(b_j + 1)` and `c̄_N(j)` decrease with `j` (`cbarAt_antitone`,
   `rowBracket_antitone`), making row `N` the worst case (`rowGain_le_rowBracket_N`) and discharging
   `hrow` in `frame_tail_never_helps` and `frame_tail_move_lt_zero`. -/

/-- Above the wall (`pe ≤ j`), `b_j = 2j − pe`. -/
theorem rowBase_of_ge (pe j : ℕ) (h : pe ≤ j) : rowBase pe j = 2 * j - pe := by
  unfold rowBase
  rw [if_neg (not_lt.mpr h)]

/-- Above the wall (`pe ≤ j`), the wall weight `w_j = pe − j` vanishes. -/
theorem wallWeight_eq_zero_of_ge (pe j : ℕ) (h : pe ≤ j) : wallWeight pe j = 0 := by
  unfold wallWeight
  omega

/-- `b_j` is monotone in the row index `j`. -/
theorem rowBase_mono (pe : ℕ) {i j : ℕ} (hij : i ≤ j) : rowBase pe i ≤ rowBase pe j := by
  unfold rowBase
  split_ifs <;> omega

/-- Above the wall (`pe ≤ i`), `b_j` is strictly increasing with gap `2(j − i)`. -/
theorem rowBase_strictMono_of_ge (pe : ℕ) {i j : ℕ} (hpe : pe ≤ i) (hij : i < j) :
    rowBase pe i < rowBase pe j := by
  rw [rowBase_of_ge pe i hpe, rowBase_of_ge pe j (le_trans hpe (le_of_lt hij))]
  omega

/-- On the gap-2 lattice (`pe ≤ i ≤ j`), the gap `b_j − b_i` is `2(j − i)`. -/
theorem rowBase_gap_two_of_ge (pe i j : ℕ) (hpe : pe ≤ i) (hij : i ≤ j) :
    (rowBase pe j : ℤ) - rowBase pe i = 2 * ((j : ℤ) - i) := by
  rw [rowBase_of_ge pe i hpe, rowBase_of_ge pe j (le_trans hpe hij)]
  omega

/-- Signed pair-step kernel `sgn(j − x) · P(|j − x|)` on the 1D lattice `ℕ`:
rows `x < j` below `j` contribute `+P(j − x)`, rows `x > j` above `j` contribute
`−P(x − j)`, and the diagonal `x = j` contributes `0`. -/
def latticeKernel (P : ℕ → R) (j x : ℕ) : R :=
  if x < j then P (j - x) else if j < x then - P (x - j) else 0

/-- The signed lattice kernel is antisymmetric: `K(j, x) = −K(x, j)`. -/
theorem latticeKernel_antisymm (P : ℕ → R) (j x : ℕ) :
    latticeKernel P j x = - latticeKernel P x j := by
  unfold latticeKernel
  rcases lt_trichotomy x j with h | rfl | h
  · have hnot : ¬ j < x := not_lt_of_gt h
    simp [h, hnot]
  · simp
  · have hnot : ¬ x < j := not_lt_of_gt h
    simp [h, hnot]

/-- On any finite move set `H`, the internal `H × H` sum of the signed lattice kernel vanishes. -/
theorem latticeKernel_sum_self_eq_zero [LinearOrder R] [IsStrictOrderedRing R]
    (P : ℕ → R) (H : Finset ℕ) :
    ∑ j ∈ H, ∑ x ∈ H, latticeKernel P j x = 0 :=
  antisymm_double_sum_eq_zero H (latticeKernel P) (latticeKernel_antisymm P)

/-- **Ambient lattice reduction (piece i)**: for `H ⊆ U`, the cross-sum of the signed lattice
kernel over `j ∈ H, x ∈ U \ H` equals the full sum over `j ∈ H, x ∈ U`, because the internal
`H × H` part is antisymmetric and vanishes. -/
theorem latticeKernel_sum_sdiff_eq [LinearOrder R] [IsStrictOrderedRing R]
    (P : ℕ → R) (U H : Finset ℕ) (hH : H ⊆ U) :
    ∑ j ∈ H, ∑ x ∈ U \ H, latticeKernel P j x
      = ∑ j ∈ H, ∑ x ∈ U, latticeKernel P j x := by
  have hsplit : ∀ j ∈ H, ∑ x ∈ U, latticeKernel P j x
      = ∑ x ∈ U \ H, latticeKernel P j x + ∑ x ∈ H, latticeKernel P j x := by
    intro j _
    exact (sum_sdiff hH).symm
  rw [sum_congr rfl hsplit, sum_add_distrib, latticeKernel_sum_self_eq_zero P H, add_zero]

/-- **Symmetric gap-2 lattice cancellation around row `j` (piece i)**: when `K` lower gap-2 steps
`+P(2(m+1))` are paired against `K` upper gap-2 steps `−P(2(m+1))`, the net lattice contribution
vanishes identically. -/
theorem symmetric_gap2_lattice_sum_eq_zero (P : ℕ → R) (K : ℕ) :
    (∑ m ∈ range K, P (2 * (m + 1))) + (∑ m ∈ range K, - P (2 * (m + 1))) = 0 := by
  rw [sum_neg_distrib, add_neg_cancel]

/-- `p⁻(g) = ε(g − 1) − ε(g)`: what a pair at gap `g` loses when it closes by `1`
(`pminus` in `rev_e_infinity_xbot_lnatural_probe.py`). -/
def pminus (eps : ℤ → R) (g : ℤ) : R := eps (g - 1) - eps g

/-- `p⁺(g) = ε(g) − ε(g + 1)`: what a pair at gap `g` gains when it opens by `1`. -/
def pplus (eps : ℤ → R) (g : ℤ) : R := eps g - eps (g + 1)

/-- `p⁺(g − 1) = p⁻(g)`: shifting the gap down by `1` turns `p⁺` into `p⁻`. -/
@[simp] theorem pplus_sub_one_eq_pminus (eps : ℤ → R) (g : ℤ) :
    pplus eps (g - 1) = pminus eps g := by
  unfold pplus pminus
  have h : g - 1 + 1 = g := by ring
  rw [h]

/-- `p⁻(g) ≥ 0` when `ε` is antitone on the positive integers and `1 < g`. -/
theorem pminus_nonneg [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (heps : AntitoneOn eps (Set.Ioi 0)) {g : ℤ} (hg : 1 < g) :
    0 ≤ pminus eps g := by
  unfold pminus
  have hle : eps g ≤ eps (g - 1) := by
    apply heps
    · show (0 : ℤ) < g - 1; omega
    · show (0 : ℤ) < g; omega
    · omega
  linarith

/-- For `x < j` and `v j = 0`, the cross-pair change of `{x, j}` when `j` moves up by `1` is
`p⁺(b_j − b_x − v_x)`. -/
theorem crossChange_framePsi_of_lt (eps : ℤ → R) (pe : ℕ) (v : ℕ → ℕ)
    {j x : ℕ} (hxj : x < j) (hvj : v j = 0) :
    crossChange (framePsi eps pe) v j x
      = pplus eps ((rowBase pe j : ℤ) - rowBase pe x - v x) := by
  unfold crossChange framePsi pplus
  rw [if_pos hxj, hvj]
  push_cast
  have h1 : (rowBase pe j : ℤ) - rowBase pe x + (1 - (v x : ℤ))
      = (rowBase pe j : ℤ) - rowBase pe x - v x + 1 := by ring
  have h2 : (rowBase pe j : ℤ) - rowBase pe x + (0 - (v x : ℤ))
      = (rowBase pe j : ℤ) - rowBase pe x - v x := by ring
  rw [h1, h2]
  ring

/-- For `j < x` and `v j = 0`, `v x = 0`, the cross-pair change of `{j, x}` when `j` moves up
by `1` is `−p⁻(b_x − b_j)` (the upper pair closes by `1`). -/
theorem crossChange_framePsi_of_gt (eps : ℤ → R) (pe : ℕ) (v : ℕ → ℕ)
    {j x : ℕ} (hjx : j < x) (hvj : v j = 0) (hvx : v x = 0) :
    crossChange (framePsi eps pe) v j x
      = - pminus eps ((rowBase pe x : ℤ) - rowBase pe j) := by
  have hnot : ¬ x < j := not_lt_of_gt hjx
  unfold crossChange framePsi pminus
  rw [if_neg hnot, if_pos hjx, hvj, hvx]
  push_cast
  have h1 : (rowBase pe x : ℤ) - rowBase pe j + -1
      = (rowBase pe x : ℤ) - rowBase pe j - 1 := by ring
  have h2 : (rowBase pe x : ℤ) - rowBase pe j + 0
      = (rowBase pe x : ℤ) - rowBase pe j := by ring
  rw [h1, h2]
  ring

/-- For any lower row `x < j` at `v = moveBy w L` (with `v j = 0`), the cross-pair change of
`{x, j}` is at most `p⁻(b_j − b_x − w_x)` whenever `p⁺(g) ≤ p⁻(g)` at `g = b_j − b_x − w_x`
(discrete convexity of `ε`): if `x ∉ L` it is `p⁺(g) ≤ p⁻(g)`, and if `x ∈ L` it is
`p⁺(g − 1) = p⁻(g)` exactly. -/
theorem crossChange_moveBy_le_pminus [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (L : Finset ℕ)
    {j x : ℕ} (hxj : x < j) (hvj : moveBy w L j = 0)
    (hconv : pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
      ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)) :
    crossChange (framePsi eps pe) (moveBy w L) j x
      ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x) := by
  rw [crossChange_framePsi_of_lt eps pe (moveBy w L) hxj hvj]
  unfold moveBy
  by_cases hxL : x ∈ L
  · simp only [if_pos hxL, Nat.cast_add, Nat.cast_one]
    have hsub : (rowBase pe j : ℤ) - rowBase pe x - ((w x : ℤ) + 1)
        = (rowBase pe j : ℤ) - rowBase pe x - w x - 1 := by ring
    rw [hsub, pplus_sub_one_eq_pminus]
  · simp only [if_neg hxL]
    exact hconv

/-- The active lower rows below `N`: wall rows (`x < pe`) or rows displaced by the certified
optimum `w` (`0 < w x`), matching the filter in `tail_bound` of
`rev_e_infinity_xbot_lnatural_probe.py`. -/
def activeLowerRows (pe : ℕ) (w : ℕ → ℕ) (N : ℕ) : Finset ℕ :=
  (range N).filter (fun x => x < pe ∨ 0 < w x)

/-- The wall-and-displaced-row correction `c̄_N(j)` at row `j ≥ N`:
`∑_{x ∈ activeLowerRows pe w N} p⁻(b_j − b_x − w_x)`. -/
def cbarAt (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (N j : ℕ) : R :=
  ∑ x ∈ activeLowerRows pe w N, pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)

/-- The per-row bracket `ε(b_j + 1) + c̄_N(j) − c` at row `j ≥ N`; at `j = N` and `c = (ln q₀)/2`
this is the probe's M7 bracket `eps(b_N + 1) + cbar_N - (ln q0)/2`. -/
def rowBracket (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (c : R) (N j : ℕ) : R :=
  eps ((rowBase pe j : ℤ) + 1) + cbarAt eps pe w N j - c

/-- **Active lower-row bound (piece ii)**: for `N ≤ j` and `moveBy w L j = 0`, the sum of
`crossChange` over `activeLowerRows pe w N` is at most `cbarAt eps pe w N j`. -/
theorem activeCross_le_cbarAt [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (L : Finset ℕ) {N j : ℕ}
    (hNj : N ≤ j) (hvj : moveBy w L j = 0)
    (hconv : ∀ x ∈ activeLowerRows pe w N,
      pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
        ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)) :
    ∑ x ∈ activeLowerRows pe w N, crossChange (framePsi eps pe) (moveBy w L) j x
      ≤ cbarAt eps pe w N j := by
  unfold cbarAt
  refine sum_le_sum fun x hx => ?_
  have hxj : x < j := lt_of_lt_of_le (mem_range.mp (mem_filter.mp hx).1) hNj
  exact crossChange_moveBy_le_pminus eps pe w L hxj hvj (hconv x hx)

/-- **Matched lower/upper gap-2 lattice domination (piece i → ii)**: when each undisplaced lower
lattice row `x ∈ U_low` is matched injectively to an upper lattice row `σ x ∈ U_high` with
`lowTerm x + highTerm (σ x) ≤ 0` (`p⁺(2m) − p⁻(2m) ≤ 0`), every unmatched upper step satisfies
`highTerm y ≤ 0` (`−p⁻(2m) ≤ 0`), and the above-block tail step satisfies `tailDiff ≤ 0`, the
combined undisplaced-lattice + tail sum is non-positive. -/
theorem matched_lower_upper_sum_nonpos [LinearOrder R] [IsStrictOrderedRing R]
    (U_low U_high : Finset ℕ) (σ : ℕ → ℕ) (lowTerm highTerm : ℕ → R) (tailDiff : R)
    (hinj : Set.InjOn σ U_low)
    (hmaps : ∀ x ∈ U_low, σ x ∈ U_high)
    (hmatch : ∀ x ∈ U_low, lowTerm x + highTerm (σ x) ≤ 0)
    (hhigh : ∀ y ∈ U_high, highTerm y ≤ 0)
    (htail : tailDiff ≤ 0) :
    tailDiff + (∑ x ∈ U_low, lowTerm x + ∑ y ∈ U_high, highTerm y) ≤ 0 := by
  have hsub : U_low.image σ ⊆ U_high := image_subset_iff.mpr hmaps
  have himg : ∑ y ∈ U_low.image σ, highTerm y = ∑ x ∈ U_low, highTerm (σ x) :=
    sum_image hinj
  have hsdiff := (sum_sdiff hsub (f := highTerm)).symm
  have hrem : ∑ y ∈ U_high \ U_low.image σ, highTerm y ≤ 0 :=
    sum_nonpos fun y hy => hhigh y (mem_sdiff.mp hy).1
  have hpaired : ∑ x ∈ U_low, lowTerm x + ∑ x ∈ U_low, highTerm (σ x) ≤ 0 := by
    rw [← sum_add_distrib]
    exact sum_nonpos hmatch
  rw [hsdiff, himg]
  linarith

/-- **Per-row bracket bound at row `j` (piece ii)**: for a tail row `j ∈ H` (`pe ≤ N ≤ j < n`)
where `moveBy w L j = 0` and all rows of `H` lie at or above `N`, if the undisplaced gap-2
lattice rows `(range n \ H) \ activeLowerRows pe w N` plus the above-block tail change
`W(h_j) − W(h_j − 1)` have net contribution `≤ 0` (by gap-2 lattice cancellation against the
upper lattice steps), then `rowGain j ≤ rowBracket eps pe w c N j`. -/
theorem rowGain_le_rowBracket [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe N n : ℕ) (w : ℕ → ℕ) (L H : Finset ℕ)
    {j : ℕ} (hpeN : pe ≤ N) (hNj : N ≤ j) (hjn : j < n)
    (hvj : moveBy w L j = 0)
    (hH_ge : ∀ y ∈ H, N ≤ y)
    (hconv : ∀ x ∈ activeLowerRows pe w N,
      pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
        ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x))
    (hlattice :
      (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
        - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - 1))
      + ∑ x ∈ (range n \ H) \ activeLowerRows pe w N,
          crossChange (framePsi eps pe) (moveBy w L) j x ≤ 0) :
    rowGain (framePhi eps W a c pe n) (framePsi eps pe) n (moveBy w L) H j
      ≤ rowBracket eps pe w c N j := by
  have hpej : pe ≤ j := le_trans hpeN hNj
  -- one-body difference at v j = 0 above the wall (wallWeight pe j = 0)
  have hphi : framePhi eps W a c pe n j (moveBy w L j + 1)
      - framePhi eps W a c pe n j (moveBy w L j)
      = eps ((rowBase pe j : ℤ) + 1)
        + (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
            - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - 1)) - c := by
    rw [hvj]
    simp only [framePhi, zero_add, range_one, sum_singleton, range_zero, sum_empty,
      wallWeight_eq_zero_of_ge pe j hpej, Nat.cast_zero, Nat.cast_one, add_zero, sub_zero,
      one_pow, mul_zero, mul_one, zero_pow (by decide : 2 ≠ 0)]
    ring
  -- activeLowerRows pe w N sits inside range n \ H
  have hsub : activeLowerRows pe w N ⊆ range n \ H := by
    intro x hx
    have hxN : x < N := mem_range.mp (mem_filter.mp hx).1
    refine mem_sdiff.mpr ⟨mem_range.mpr (lt_trans (lt_of_lt_of_le hxN hNj) hjn), ?_⟩
    intro hxH
    exact not_le_of_gt hxN (hH_ge x hxH)
  have hsplit := (sum_sdiff hsub (f := fun x => crossChange (framePsi eps pe) (moveBy w L) j x)).symm
  have hact := activeCross_le_cbarAt eps pe w L hNj hvj hconv
  unfold rowGain rowBracket
  rw [hphi, hsplit]
  linarith

/-- **Monotonicity of `c̄_N(j)` in `j` (piece iii)**: when `p⁻` is antitone on `(1, ∞)` (discrete
convexity of `ε`) and every active lower row has gap `> 1` at row `N`, `c̄_N(j)` is antitone for
`N ≤ j₁ ≤ j₂`. -/
theorem cbarAt_antitone [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (N : ℕ)
    (hpminus : AntitoneOn (pminus eps) (Set.Ioi 1))
    (hdom : ∀ x ∈ activeLowerRows pe w N,
      1 < (rowBase pe N : ℤ) - rowBase pe x - w x)
    {j₁ j₂ : ℕ} (hNj₁ : N ≤ j₁) (hj : j₁ ≤ j₂) :
    cbarAt eps pe w N j₂ ≤ cbarAt eps pe w N j₁ := by
  unfold cbarAt
  refine sum_le_sum fun x hx => ?_
  have hdomN := hdom x hx
  have hb1 : (rowBase pe N : ℤ) ≤ rowBase pe j₁ := by exact_mod_cast rowBase_mono pe hNj₁
  have hb2 : (rowBase pe j₁ : ℤ) ≤ rowBase pe j₂ := by exact_mod_cast rowBase_mono pe hj
  apply hpminus
  · show (1 : ℤ) < (rowBase pe j₁ : ℤ) - rowBase pe x - w x; linarith
  · show (1 : ℤ) < (rowBase pe j₂ : ℤ) - rowBase pe x - w x; linarith
  · linarith

/-- **Monotonicity of the per-row bracket in `j` (piece iii)**: for `N ≤ j₁ ≤ j₂`, when `ε` is
antitone on `(0, ∞)` and `p⁻` is antitone on `(1, ∞)`, `rowBracket` decreases with `j`; in
particular, row `N` is the worst case for all `j ≥ N`. -/
theorem rowBracket_antitone [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (pe : ℕ) (w : ℕ → ℕ) (c : R) (N : ℕ)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hpminus : AntitoneOn (pminus eps) (Set.Ioi 1))
    (hdom : ∀ x ∈ activeLowerRows pe w N,
      1 < (rowBase pe N : ℤ) - rowBase pe x - w x)
    {j₁ j₂ : ℕ} (hNj₁ : N ≤ j₁) (hj : j₁ ≤ j₂) :
    rowBracket eps pe w c N j₂ ≤ rowBracket eps pe w c N j₁ := by
  unfold rowBracket
  have hcbar := cbarAt_antitone eps pe w N hpminus hdom hNj₁ hj
  have hb : (rowBase pe j₁ : ℤ) ≤ rowBase pe j₂ := by exact_mod_cast rowBase_mono pe hj
  have he : eps ((rowBase pe j₂ : ℤ) + 1) ≤ eps ((rowBase pe j₁ : ℤ) + 1) := by
    apply heps
    · show (0 : ℤ) < (rowBase pe j₁ : ℤ) + 1; positivity
    · show (0 : ℤ) < (rowBase pe j₂ : ℤ) + 1; positivity
    · linarith
  linarith

/-- **Worst-case bracket bound at row `N` (pieces i–iii combined)**: every tail row `j ∈ H`
(`pe ≤ N ≤ j < n`) satisfies `rowGain j ≤ rowBracket eps pe w c N N`, discharging the hypothesis
`hrow` of `tail_never_helps`. -/
theorem rowGain_le_rowBracket_N [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe N n : ℕ) (w : ℕ → ℕ) (L H : Finset ℕ)
    (hpeN : pe ≤ N) (hH : H ⊆ range n) (hH_ge : ∀ y ∈ H, N ≤ y)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hpminus : AntitoneOn (pminus eps) (Set.Ioi 1))
    (hdom : ∀ x ∈ activeLowerRows pe w N,
      1 < (rowBase pe N : ℤ) - rowBase pe x - w x)
    (hvH : ∀ j ∈ H, moveBy w L j = 0)
    (hconv : ∀ j ∈ H, ∀ x ∈ activeLowerRows pe w N,
      pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
        ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x))
    (hlattice : ∀ j ∈ H,
      (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
        - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - 1))
      + ∑ x ∈ (range n \ H) \ activeLowerRows pe w N,
          crossChange (framePsi eps pe) (moveBy w L) j x ≤ 0) :
    ∀ j ∈ H,
      rowGain (framePhi eps W a c pe n) (framePsi eps pe) n (moveBy w L) H j
        ≤ rowBracket eps pe w c N N := by
  intro j hj
  have hNj : N ≤ j := hH_ge j hj
  have hjn : j < n := mem_range.mp (hH hj)
  have h1 := rowGain_le_rowBracket eps W a c pe N n w L H hpeN hNj hjn
    (hvH j hj) hH_ge (hconv j hj) (hlattice j hj)
  have h2 := rowBracket_antitone eps pe w c N heps hpminus hdom (le_refl N) hNj
  exact le_trans h1 h2

/-- **Frame tail lemma (`hrow` discharged)**: for any move `S = L ∪ H` with `H` at or above row
`N ≥ pe`, the objective change satisfies
`G(moveBy w (L ∪ H)) − G(w) ≤ (G(moveBy w L) − G(w)) + |H| · rowBracket eps pe w c N N`. -/
theorem frame_tail_never_helps [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe N n : ℕ) (w : ℕ → ℕ) (L H : Finset ℕ)
    (hd : Disjoint L H) (hpeN : pe ≤ N) (hH : H ⊆ range n) (hH_ge : ∀ y ∈ H, N ≤ y)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hpminus : AntitoneOn (pminus eps) (Set.Ioi 1))
    (hdom : ∀ x ∈ activeLowerRows pe w N,
      1 < (rowBase pe N : ℤ) - rowBase pe x - w x)
    (hvH : ∀ j ∈ H, moveBy w L j = 0)
    (hconv : ∀ j ∈ H, ∀ x ∈ activeLowerRows pe w N,
      pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
        ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x))
    (hlattice : ∀ j ∈ H,
      (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
        - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - 1))
      + ∑ x ∈ (range n \ H) \ activeLowerRows pe w N,
          crossChange (framePsi eps pe) (moveBy w L) j x ≤ 0) :
    frameObjective eps W a c pe n (moveBy w (L ∪ H)) - frameObjective eps W a c pe n w
      ≤ (frameObjective eps W a c pe n (moveBy w L) - frameObjective eps W a c pe n w)
        + (H.card : R) * rowBracket eps pe w c N N := by
  unfold frameObjective
  exact tail_never_helps n (framePhi eps W a c pe n) (framePsi eps pe) w L H hd hH
    (rowBracket eps pe w c N N)
    (rowGain_le_rowBracket_N eps W a c pe N n w L H hpeN hH hH_ge heps hpminus hdom hvH hconv
      hlattice)

/-- **Strict frame tail lemma (`hrow` discharged)**: when the worst-case bracket at row `N` is
negative (`rowBracket eps pe w c N N < 0`, the probe's check M7) and the lower move `L` does not
improve `w` (`G(moveBy w L) − G(w) ≤ 0`, the probe's check M5), any move with `H ≠ ∅` at or above
`N` strictly lowers the frame objective. -/
theorem frame_tail_move_lt_zero [LinearOrder R] [IsStrictOrderedRing R]
    (eps : ℤ → R) (W : ℕ → ℤ → R) (a c : R) (pe N n : ℕ) (w : ℕ → ℕ) (L H : Finset ℕ)
    (hd : Disjoint L H) (hpeN : pe ≤ N) (hH : H ⊆ range n) (hH_ge : ∀ y ∈ H, N ≤ y)
    (hne : H.Nonempty)
    (heps : AntitoneOn eps (Set.Ioi 0))
    (hpminus : AntitoneOn (pminus eps) (Set.Ioi 1))
    (hdom : ∀ x ∈ activeLowerRows pe w N,
      1 < (rowBase pe N : ℤ) - rowBase pe x - w x)
    (hvH : ∀ j ∈ H, moveBy w L j = 0)
    (hconv : ∀ j ∈ H, ∀ x ∈ activeLowerRows pe w N,
      pplus eps ((rowBase pe j : ℤ) - rowBase pe x - w x)
        ≤ pminus eps ((rowBase pe j : ℤ) - rowBase pe x - w x))
    (hlattice : ∀ j ∈ H,
      (W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j)
        - W (pe - n) ((rowBase pe n : ℤ) - rowBase pe j - 1))
      + ∑ x ∈ (range n \ H) \ activeLowerRows pe w N,
          crossChange (framePsi eps pe) (moveBy w L) j x ≤ 0)
    (hβ : rowBracket eps pe w c N N < 0)
    (hL : frameObjective eps W a c pe n (moveBy w L) - frameObjective eps W a c pe n w ≤ 0) :
    frameObjective eps W a c pe n (moveBy w (L ∪ H)) - frameObjective eps W a c pe n w < 0 := by
  unfold frameObjective at hL ⊢
  exact tail_move_lt_zero n (framePhi eps W a c pe n) (framePsi eps pe) w L H hd hH hne
    (rowBracket eps pe w c N N) hβ hL
    (rowGain_le_rowBracket_N eps W a c pe N n w L H hpeN hH hH_ge heps hpminus hdom hvH hconv
      hlattice)

end Tail

end XbotBottomEdge
end QOU.MassTheory
