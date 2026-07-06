import QOU.BraidKnot.AJTrefoil

/-!
# QOU.BraidKnot.AJTrefoilRootEval

**Root-of-unity evaluation of the trefoil Rosso–Jones cyclotomic sum** —
the two lemmas that discharge the cited evaluation cores
`trefoil_eval_at_root_prev` / `trefoil_eval_at_root_next` in
`QOU.BraidKnot.AJTrefoilAnnihilation`:

* `trP_sum_at_root_self` — under `(w⁴)^M = 1`,
  `∑_{j≤M} (−1)^j w^{6j(j+1)} [2j+1]_{w²} = (−1)^M w^{6M(M+2)} [M+1]_{w²}`;
* `trP_sum_at_root_offset` — under `(w⁴)^{n+2} = 1`, the same closed form
  holds for the sum truncated at `n`.

## Proof architecture

Multiplying by `w²(w² − w⁻²)` turns the quantum-integer sum into a
difference of two signed pure-power sums `S₁ − S₂` (`sum_bridge`), and the
closed form into a two-term power difference (`rhs_expand`) — both exact.
Then three lemmas close the evaluation:

1. **Shift** (`s1_eq_shift`, exact): re-indexing `j ↦ j+1` maps the `S₁`
   summand onto the negated summand of the Gauss-type sum
   `G(m) = ∑_{j≤m} (−1)^j w^{6j²−2j}`, so `S₁(m) = 1 − G(m+1)`.
2. **Reflection** (`s2_eq_reflect`, uses the root): `j ↦ m−j` maps the
   `S₂` summand onto the `G` summand times `w^{12mj}`, and
   `w^{12mj} = ((w⁴)^m)^{3j} = 1`, so `S₂(m) = (−1)^m w^{6m²+2m} G(m)`.
3. **Dichotomy** (`gauss_dichotomy`, uses the root):
   `(G(m) − 1)(1 + β) = 0` with `β = (−1)^m w^{6m²+2m}`.  Since `β² = 1`,
   either `β = −1` (automatic for `m` odd) and the bracket vanishes, or
   `β = 1`, which forces `m` even and `(w²)^m = 1`, and then the residual
   Gauss-type sum collapses to its last term (`gauss_sum_eq_one`): with
   `d = orderOf (w²)`, the summand is antiperiodic (`d` odd) or pairwise
   cancelling over each period (`d` even, where `(w²)^{d/2} = −1` is
   forced), so the first `m` terms cancel in blocks and `G(m) = 1`.

The offset variant reflects the *extended* sum `S₂(n+2)` (whose range
matches the root `(w⁴)^{n+2} = 1`), peels the top two terms of each sum,
and the same dichotomy at `m = n+2` closes it — the peeled top term of
`S₂` cancels `β` exactly, and the two survivors match the target under
two multiplications by `(w⁴)^{n+2} = 1`.

All identities were pre-verified exactly (sympy, symbolic `w`) and at
roots of unity (mpmath, 40 dps) before formalisation; see the session
scratch checks accompanying PR #3434.

## Base ring (§7c)

Generic `{K : Type*} [Field K]`; no `ℝ`, no ordering, no `CharZero` —
the char-2 degeneracy is absorbed by the dichotomy (`1 + β = 0` holds
identically there).
-/

namespace QOU.BraidKnot.AJTrefoil

open Finset

variable {K : Type*} [Field K]

/-! ## The three signed power sums -/

/-- `S₁` summand: `(−1)^j w^{6j²+10j+4}` (exponent written `ℕ`-safely). -/
private def rf1 (w : K) (j : ℕ) : K :=
  (-1 : K) ^ j * w ^ (6 * (j * (j + 1)) + 4 * j + 4)

/-- `S₂` summand: `(−1)^j w^{6j²+2j}` (via `j(j−1)`, exact at `j = 0`). -/
private def rf2 (w : K) (j : ℕ) : K :=
  (-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 8 * j)

/-- Gauss-type summand: `(−1)^j w^{6j²−2j}` (via `j(j−1)`). -/
private def rg (w : K) (j : ℕ) : K :=
  (-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 4 * j)

private def rS1 (w : K) (m : ℕ) : K := ∑ j ∈ range (m + 1), rf1 w j
private def rS2 (w : K) (m : ℕ) : K := ∑ j ∈ range (m + 1), rf2 w j
/-- `G(m) = ∑_{j≤m} (−1)^j w^{6j²−2j}` — the Gauss-type sum of the module
    docstring. -/
private def rgS (w : K) (m : ℕ) : K := ∑ j ∈ range (m + 1), rg w j

/-! ## `ℕ`-exponent bookkeeping (truncated subtraction resolved by cases) -/

/-- `2 + 6j(j+1) = e₂(j) + (4j+2)` where `e₂(j) = 6j(j−1)+8j = 6j²+2j`. -/
private theorem exp_bridge (j : ℕ) :
    2 + 6 * (j * (j + 1)) = 6 * (j * (j - 1)) + 8 * j + (4 * j + 2) := by
  cases j with
  | zero => rfl
  | succ j => simp only [Nat.add_sub_cancel]; ring

/-- Canonical form of `e₂`: `6m(m−1) + 8m = 6m² + 2m`. -/
private theorem exp_e2_canon (m : ℕ) :
    6 * (m * (m - 1)) + 8 * m = 6 * (m * m) + 2 * m := by
  cases m with
  | zero => rfl
  | succ m => simp only [Nat.add_sub_cancel]; ring

/-- Reflection exponent law: `e₂(k) + 12(j+k)j = e₂(j+k) + eg(j)` where
    `eg(j) = 6j(j−1)+4j = 6j²−2j`. -/
private theorem exp_reflect (j k : ℕ) :
    6 * (k * (k - 1)) + 8 * k + 12 * ((j + k) * j)
      = 6 * ((j + k) * ((j + k) - 1)) + 8 * (j + k)
        + (6 * (j * (j - 1)) + 4 * j) := by
  rcases j with _ | j <;> rcases k with _ | k
  · rfl
  · simp only [Nat.zero_add, Nat.add_sub_cancel, Nat.zero_mul, Nat.mul_zero]
  · simp only [Nat.add_zero, Nat.add_sub_cancel, Nat.zero_mul, Nat.mul_zero]
    ring
  · rw [show j + 1 + (k + 1) - 1 = j + k + 1 by omega,
      show k + 1 - 1 = k by omega, show j + 1 - 1 = j by omega]
    ring

/-- Step exponent law for the Gauss summand:
    `eG(c+h) = h(6c+3h−1) + eG(c)` where `eG(x) = 3x(x−1)+2x = 3x²−x`. -/
private theorem exp_step (c h : ℕ) :
    3 * ((c + h) * ((c + h) - 1)) + 2 * (c + h)
      = h * (6 * c + 3 * h - 1) + (3 * (c * (c - 1)) + 2 * c) := by
  rcases h with _ | h
  · simp
  · rw [show 6 * c + 3 * (h + 1) - 1 = 6 * c + 3 * h + 2 by omega]
    rcases c with _ | c
    · simp only [Nat.zero_add, Nat.add_sub_cancel, Nat.zero_mul, Nat.mul_zero]
      ring
    · rw [show c + 1 + (h + 1) - 1 = c + h + 1 by omega,
        show c + 1 - 1 = c by omega]
      ring

/-- Last-term exponent: `eG(N) = N(3N−1)`. -/
private theorem exp_last (N : ℕ) :
    3 * (N * (N - 1)) + 2 * N = N * (3 * N - 1) := by
  cases N with
  | zero => rfl
  | succ N =>
      simp only [Nat.add_sub_cancel]
      rw [show 3 * (N + 1) - 1 = 3 * N + 2 by omega]
      ring

/-! ## Block-cancellation machinery for the residual Gauss sum -/

/-- A sum over `range (p * t)` of a function whose every length-`p`
    block-sum vanishes is zero. -/
private theorem sum_range_mul_eq_zero {f : ℕ → K} {p : ℕ} (t : ℕ)
    (hp : ∀ c, ∑ j ∈ range p, f (c + j) = 0) :
    ∑ j ∈ range (p * t), f j = 0 := by
  induction t with
  | zero => simp
  | succ t ih =>
      rw [show p * (t + 1) = p * t + p by ring, Finset.sum_range_add, ih,
        zero_add]
      exact hp (p * t)

/-- **The residual Gauss-sum collapse**: for `v² ≠ 1`, `N` even and
    `v^N = 1`, the sum `∑_{j≤N} (−1)^j v^{3j²−j}` collapses to its last
    term, which is `1`.  (Blocks of length `orderOf v` — antiperiodic for
    odd order, pairwise-cancelling for even order — annihilate the first
    `N` terms.) -/
private theorem gauss_sum_eq_one {v : K} (hv2 : v ^ 2 ≠ 1) {N : ℕ}
    (hNe : Even N) (hroot : v ^ N = 1) :
    ∑ j ∈ range (N + 1), (-1 : K) ^ j * v ^ (3 * (j * (j - 1)) + 2 * j)
      = 1 := by
  rcases Nat.eq_zero_or_pos N with hN0 | hNpos
  · subst hN0; simp
  set f : ℕ → K := fun j => (-1 : K) ^ j * v ^ (3 * (j * (j - 1)) + 2 * j)
    with hfdef
  -- the one-step transport of the summand
  have hstep : ∀ c h : ℕ,
      f (c + h) = (-1 : K) ^ h * (v ^ h) ^ (6 * c + 3 * h - 1) * f c := by
    intro c h
    show (-1 : K) ^ (c + h) * v ^ (3 * ((c + h) * ((c + h) - 1)) + 2 * (c + h))
        = (-1 : K) ^ h * (v ^ h) ^ (6 * c + 3 * h - 1)
          * ((-1 : K) ^ c * v ^ (3 * (c * (c - 1)) + 2 * c))
    rw [exp_step c h, pow_add, pow_add, ← pow_mul]
    ring
  -- order-theoretic facts
  have hfin : IsOfFinOrder v := isOfFinOrder_iff_pow_eq_one.mpr
    ⟨N, hNpos, hroot⟩
  have hdpos : 0 < orderOf v := hfin.orderOf_pos
  have hddvd : orderOf v ∣ N := orderOf_dvd_of_pow_eq_one hroot
  have hvd : v ^ orderOf v = 1 := pow_orderOf_eq_one v
  have hd2 : orderOf v ≠ 2 := fun h => hv2 (h ▸ hvd)
  -- the first N terms cancel in blocks
  have hzero : ∑ j ∈ range N, f j = 0 := by
    rcases Nat.even_or_odd (orderOf v) with hde | hdo
    · -- even order: in-block pairing at half-period, block-sum zero
      obtain ⟨h, hdh⟩ := hde
      have hh0 : 0 < h := by omega
      have hδ : v ^ h = -1 := by
        have hsq : v ^ h * v ^ h = 1 := by
          rw [← pow_add, ← hdh]; exact hvd
        rcases mul_self_eq_one_iff.mp hsq with h1 | hm1
        · exfalso
          have hdvd := orderOf_dvd_of_pow_eq_one h1
          have := Nat.le_of_dvd hh0 hdvd
          omega
        · exact hm1
      have hpair : ∀ x, f (x + h) = -f x := by
        intro x
        rw [hstep x h, hδ, ← pow_add]
        have hodd : Odd (h + (6 * x + 3 * h - 1)) := by
          refine Nat.odd_iff.mpr ?_
          omega
        rw [hodd.neg_one_pow]
        ring
      have hblock : ∀ c, ∑ j ∈ range (orderOf v), f (c + j) = 0 := by
        intro c
        rw [hdh, Finset.sum_range_add]
        have h2 : ∑ j ∈ range h, f (c + (h + j))
            = ∑ j ∈ range h, -f (c + j) := by
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [show c + (h + j) = c + j + h by ring, hpair]
        rw [h2, Finset.sum_neg_distrib]
        ring
      obtain ⟨t, hNt⟩ := hddvd
      rw [hNt]
      exact sum_range_mul_eq_zero t hblock
    · -- odd order: antiperiod, blocks of twice the period
      have hanti : ∀ x, f (x + orderOf v) = -f x := by
        intro x
        rw [hstep x (orderOf v), hvd, one_pow, hdo.neg_one_pow]
        ring
      have hblock2 : ∀ c,
          ∑ j ∈ range (orderOf v + orderOf v), f (c + j) = 0 := by
        intro c
        rw [Finset.sum_range_add]
        have h2 : ∑ j ∈ range (orderOf v), f (c + (orderOf v + j))
            = ∑ j ∈ range (orderOf v), -f (c + j) := by
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [show c + (orderOf v + j) = c + j + orderOf v by ring, hanti]
        rw [h2, Finset.sum_neg_distrib]
        ring
      obtain ⟨m, hNm⟩ := hddvd
      have hme : Even m := by
        rcases Nat.even_mul.mp (hNm ▸ hNe) with h | h
        · exact absurd h (Nat.not_even_iff_odd.mpr hdo)
        · exact h
      obtain ⟨t, hmt⟩ := hme
      rw [hNm, hmt,
        show orderOf v * (t + t) = (orderOf v + orderOf v) * t by ring]
      exact sum_range_mul_eq_zero t hblock2
  -- last term survives and equals 1
  rw [Finset.sum_range_succ, hzero, zero_add]
  show (-1 : K) ^ N * v ^ (3 * (N * (N - 1)) + 2 * N) = 1
  rw [exp_last, pow_mul, hroot, one_pow, hNe.neg_one_pow, one_mul]

/-! ## The three structural lemmas -/

/-- **Shift (exact)**: `S₁(m) = 1 − G(m+1)` — re-indexing `j ↦ j+1` maps
    the `S₁` summand onto the negated `G` summand. -/
private theorem s1_eq_shift (w : K) (m : ℕ) :
    rS1 w m = 1 - rgS w (m + 1) := by
  have hterm : ∀ i : ℕ, rg w (i + 1) = -rf1 w i := by
    intro i
    show (-1 : K) ^ (i + 1) * w ^ (6 * ((i + 1) * ((i + 1) - 1)) + 4 * (i + 1))
        = -((-1 : K) ^ i * w ^ (6 * (i * (i + 1)) + 4 * i + 4))
    rw [Nat.add_sub_cancel, pow_succ,
      show 6 * ((i + 1) * i) + 4 * (i + 1) = 6 * (i * (i + 1)) + 4 * i + 4
        by ring]
    ring
  have h0 : rg w 0 = 1 := by
    show (-1 : K) ^ 0 * w ^ (6 * (0 * (0 - 1)) + 4 * 0) = 1
    norm_num
  unfold rS1 rgS
  rw [Finset.sum_range_succ' (fun i => rg w i) (m + 1), h0]
  rw [show ∑ i ∈ range (m + 1), rg w (i + 1)
      = ∑ i ∈ range (m + 1), -rf1 w i from
    Finset.sum_congr rfl fun i _ => hterm i, Finset.sum_neg_distrib]
  ring

/-- **Reflection (at the root)**: under `(w⁴)^m = 1`,
    `S₂(m) = (−1)^m w^{6m²+2m} G(m)`. -/
private theorem s2_eq_reflect (w : K) {m : ℕ} (hroot : (w ^ 4) ^ m = 1) :
    rS2 w m = (-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m) * rgS w m := by
  unfold rS2 rgS
  rw [← Finset.sum_range_reflect (fun j => rf2 w j) (m + 1), Finset.mul_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  have hjm : j ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
  rw [show m + 1 - 1 - j = m - j by omega]
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hjm
  rw [Nat.add_sub_cancel_left]
  show (-1 : K) ^ k * w ^ (6 * (k * (k - 1)) + 8 * k)
      = (-1 : K) ^ (j + k) * w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k))
        * ((-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 4 * j))
  have hsign : (-1 : K) ^ (j + k) * (-1 : K) ^ j = (-1 : K) ^ k := by
    rw [← pow_add, show j + k + j = 2 * j + k by ring, pow_add, pow_mul]
    norm_num
  have hpow : (w : K) ^ (6 * (k * (k - 1)) + 8 * k)
      = w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k))
        * w ^ (6 * (j * (j - 1)) + 4 * j) := by
    have hone : ((w : K) ^ 4) ^ (j + k) = 1 := hroot
    calc (w : K) ^ (6 * (k * (k - 1)) + 8 * k)
        = w ^ (6 * (k * (k - 1)) + 8 * k) * (((w ^ 4) ^ (j + k)) ^ (3 * j))
          := by rw [hone, one_pow, mul_one]
      _ = w ^ (6 * (k * (k - 1)) + 8 * k) * w ^ (12 * ((j + k) * j)) := by
          congr 1
          rw [← pow_mul, ← pow_mul]
          congr 1
          ring
      _ = w ^ (6 * (k * (k - 1)) + 8 * k + 12 * ((j + k) * j)) := by
          rw [← pow_add]
      _ = w ^ (6 * ((j + k) * ((j + k) - 1)) + 8 * (j + k)
            + (6 * (j * (j - 1)) + 4 * j)) := by rw [exp_reflect]
      _ = w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k)
            + (6 * (j * (j - 1)) + 4 * j)) := by rw [exp_e2_canon]
      _ = w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k))
            * w ^ (6 * (j * (j - 1)) + 4 * j) := pow_add w _ _
  calc (-1 : K) ^ k * w ^ (6 * (k * (k - 1)) + 8 * k)
      = ((-1 : K) ^ (j + k) * (-1 : K) ^ j)
          * (w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k))
            * w ^ (6 * (j * (j - 1)) + 4 * j)) := by
        rw [hsign, ← hpow]
    _ = (-1 : K) ^ (j + k) * w ^ (6 * ((j + k) * (j + k)) + 2 * (j + k))
          * ((-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 4 * j)) := by ring

/-- **Dichotomy (at the root)**: under `(w⁴)^m = 1` and `w⁴ ≠ 1`,
    `(G(m) − 1)(1 + β) = 0` with `β = (−1)^m w^{6m²+2m}`. -/
private theorem gauss_dichotomy {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0)
    {m : ℕ} (hroot : (w ^ 4) ^ m = 1) :
    (rgS w m - 1) * (1 + (-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m)) = 0 := by
  have hw : w ≠ 0 := by rintro rfl; apply hv; norm_num
  by_cases hb : (1 : K) + (-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m) = 0
  · exact mul_eq_zero_of_right _ hb
  -- β² = 1
  have hβsq : ((-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m))
      * ((-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m)) = 1 := by
    have hs : (-1 : K) ^ m * (-1 : K) ^ m = 1 := by
      rw [← mul_pow]; norm_num
    have hp : (w : K) ^ (6 * (m * m) + 2 * m) * w ^ (6 * (m * m) + 2 * m)
        = 1 := by
      rw [← pow_add,
        show 6 * (m * m) + 2 * m + (6 * (m * m) + 2 * m)
          = 4 * m * (3 * m + 1) by ring,
        pow_mul, pow_mul, hroot, one_pow]
    calc ((-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m))
        * ((-1 : K) ^ m * w ^ (6 * (m * m) + 2 * m))
        = ((-1 : K) ^ m * (-1 : K) ^ m)
          * (w ^ (6 * (m * m) + 2 * m) * w ^ (6 * (m * m) + 2 * m)) := by
          ring
      _ = 1 := by rw [hs, hp, one_mul]
  rcases mul_self_eq_one_iff.mp hβsq with h1 | hm1
  · -- β = 1 forces m even and (w²)^m = 1; then the residual collapse
    rcases Nat.even_or_odd m with hme | hmo
    · -- m even
      obtain ⟨s, hms⟩ := hme
      have hE1 : (w : K) ^ (6 * (m * m) + 2 * m) = 1 := by
        have := h1
        rwa [Even.neg_one_pow ⟨s, hms⟩, one_mul] at this
      have hvm : ((w : K) ^ 2) ^ m = 1 := by
        have hsplit : (w : K) ^ (6 * (m * m) + 2 * m)
            = w ^ (2 * m) * (((w ^ 4) ^ m) ^ (3 * s)) := by
          rw [← pow_mul, ← pow_mul, ← pow_add]
          congr 1
          subst hms; ring
        rw [hsplit, hroot, one_pow, mul_one] at hE1
        rw [← pow_mul]
        exact hE1
      -- residual collapse with v := w²
      have hv2' : ((w : K) ^ 2) ^ 2 ≠ 1 := by
        intro h
        apply hv
        have hmul : (w : K) ^ 2 * (w : K) ^ 2 = 1 := by
          rw [← sq]; exact h
        rw [inv_eq_of_mul_eq_one_right hmul]
        exact sub_self _
      have hgauss := gauss_sum_eq_one hv2' ⟨s, hms⟩ hvm
      have hG : rgS w m = 1 := by
        unfold rgS
        rw [show ∑ j ∈ range (m + 1), rg w j
            = ∑ j ∈ range (m + 1),
                (-1 : K) ^ j * ((w : K) ^ 2) ^ (3 * (j * (j - 1)) + 2 * j)
          from Finset.sum_congr rfl fun j _ => by
            show (-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 4 * j) = _
            rw [← pow_mul,
              show 2 * (3 * (j * (j - 1)) + 2 * j)
                = 6 * (j * (j - 1)) + 4 * j by ring]]
        exact hgauss
      rw [hG, sub_self, zero_mul]
    · -- m odd: β = −1 unconditionally, so the bracket vanishes — contra hb
      exfalso
      obtain ⟨s, hms⟩ := hmo
      have hE1 : (w : K) ^ (6 * (m * m) + 2 * m) = 1 := by
        have hsplit : (w : K) ^ (6 * (m * m) + 2 * m)
            = ((w ^ 4) ^ m) ^ (3 * s + 2) := by
          rw [← pow_mul, ← pow_mul]
          congr 1
          subst hms; ring
        rw [hsplit, hroot, one_pow]
      apply hb
      rw [hE1, mul_one, Odd.neg_one_pow ⟨s, hms⟩]
      ring
  · -- β = −1: bracket vanishes, contradicting hb
    exact absurd (by rw [hm1]; ring) hb

/-! ## Bridge and closed-form expansion (both exact) -/

/-- Multiplying the Rosso–Jones cyclotomic sum by `w²(w² − w⁻²)` yields
    `S₁ − S₂` (termwise, exact — needs only `w ≠ 0` and `w⁴ ≠ 1`). -/
private theorem sum_bridge {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) (m : ℕ) :
    w ^ 2 * (w ^ 2 - (w ^ 2)⁻¹)
      * ∑ j ∈ range (m + 1),
          (-1 : K) ^ j * w ^ (6 * (j * (j + 1))) * qInt (w ^ 2) (2 * j + 1)
      = rS1 w m - rS2 w m := by
  unfold rS1 rS2
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  show w ^ 2 * (w ^ 2 - (w ^ 2)⁻¹)
      * ((-1 : K) ^ j * w ^ (6 * (j * (j + 1))) * qInt (w ^ 2) (2 * j + 1))
    = rf1 w j - rf2 w j
  unfold qInt
  have hY : ((w : K) ^ 2) ^ (2 * j + 1) = w ^ (4 * j + 2) := by
    rw [← pow_mul]; congr 1; ring
  have hYne : (w : K) ^ (4 * j + 2) ≠ 0 := pow_ne_zero _ hw
  calc w ^ 2 * (w ^ 2 - (w ^ 2)⁻¹)
      * ((-1 : K) ^ j * w ^ (6 * (j * (j + 1)))
        * ((((w : K) ^ 2) ^ (2 * j + 1) - (((w : K) ^ 2) ^ (2 * j + 1))⁻¹)
          / (w ^ 2 - (w ^ 2)⁻¹)))
      = (-1 : K) ^ j * (w ^ 2 * w ^ (6 * (j * (j + 1))))
        * (((((w : K) ^ 2) ^ (2 * j + 1) - (((w : K) ^ 2) ^ (2 * j + 1))⁻¹)
            / (w ^ 2 - (w ^ 2)⁻¹)) * (w ^ 2 - (w ^ 2)⁻¹)) := by ring
    _ = (-1 : K) ^ j * w ^ (2 + 6 * (j * (j + 1)))
        * (w ^ (4 * j + 2) - (w ^ (4 * j + 2))⁻¹) := by
        rw [div_mul_cancel₀ _ hv, ← pow_add, hY]
    _ = (-1 : K) ^ j * (w ^ (2 + 6 * (j * (j + 1))) * w ^ (4 * j + 2))
        - (-1 : K) ^ j
          * (w ^ (2 + 6 * (j * (j + 1))) * (w ^ (4 * j + 2))⁻¹) := by ring
    _ = rf1 w j - rf2 w j := by
        congr 1
        · show _ = (-1 : K) ^ j * w ^ (6 * (j * (j + 1)) + 4 * j + 4)
          rw [← pow_add]
          congr 2
          ring
        · show _ = (-1 : K) ^ j * w ^ (6 * (j * (j - 1)) + 8 * j)
          rw [exp_bridge, pow_add, mul_assoc, mul_inv_cancel₀ hYne, mul_one]

/-- The closed form times `w²(w² − w⁻²)` is a two-term power difference
    (exact). -/
private theorem rhs_expand {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) (m : ℕ) :
    w ^ 2 * (w ^ 2 - (w ^ 2)⁻¹)
      * ((-1 : K) ^ m * w ^ (6 * (m * (m + 2))) * qInt (w ^ 2) (m + 1))
      = (-1 : K) ^ m
        * (w ^ (6 * (m * m) + 14 * m + 4) - w ^ (6 * (m * m) + 10 * m)) := by
  unfold qInt
  have hY : ((w : K) ^ 2) ^ (m + 1) = w ^ (2 * m + 2) := by
    rw [← pow_mul]
    congr 1
  have hYne : (w : K) ^ (2 * m + 2) ≠ 0 := pow_ne_zero _ hw
  calc w ^ 2 * (w ^ 2 - (w ^ 2)⁻¹)
      * ((-1 : K) ^ m * w ^ (6 * (m * (m + 2)))
        * ((((w : K) ^ 2) ^ (m + 1) - (((w : K) ^ 2) ^ (m + 1))⁻¹)
          / (w ^ 2 - (w ^ 2)⁻¹)))
      = (-1 : K) ^ m * (w ^ 2 * w ^ (6 * (m * (m + 2))))
        * (((((w : K) ^ 2) ^ (m + 1) - (((w : K) ^ 2) ^ (m + 1))⁻¹)
            / (w ^ 2 - (w ^ 2)⁻¹)) * (w ^ 2 - (w ^ 2)⁻¹)) := by ring
    _ = (-1 : K) ^ m * w ^ (2 + 6 * (m * (m + 2)))
        * (w ^ (2 * m + 2) - (w ^ (2 * m + 2))⁻¹) := by
        rw [div_mul_cancel₀ _ hv, ← pow_add, hY]
    _ = (-1 : K) ^ m
        * ((w ^ (2 + 6 * (m * (m + 2))) * w ^ (2 * m + 2))
          - w ^ (2 + 6 * (m * (m + 2))) * (w ^ (2 * m + 2))⁻¹) := by ring
    _ = (-1 : K) ^ m
        * (w ^ (6 * (m * m) + 14 * m + 4) - w ^ (6 * (m * m) + 10 * m)) := by
        congr 2
        · rw [← pow_add]; congr 1; ring
        · rw [show 2 + 6 * (m * (m + 2))
              = 6 * (m * m) + 10 * m + (2 * m + 2) by ring,
            pow_add, mul_assoc, mul_inv_cancel₀ hYne, mul_one]

/-! ## The two main evaluation lemmas -/

/-- `S₁ − S₂` at the self-matched root. -/
private theorem s1_sub_s2_self {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0)
    {M : ℕ} (hroot : (w ^ 4) ^ M = 1) :
    rS1 w M - rS2 w M
      = (-1 : K) ^ M
        * (w ^ (6 * (M * M) + 14 * M + 4) - w ^ (6 * (M * M) + 10 * M)) := by
  have hrefl := s2_eq_reflect w hroot
  have hdich := gauss_dichotomy hv hroot
  have hshift := s1_eq_shift w M
  have hpeel : rgS w (M + 1)
      = rgS w M + (-1 : K) ^ (M + 1) * w ^ (6 * (M * M) + 10 * M + 4) := by
    unfold rgS
    rw [Finset.sum_range_succ]
    congr 2
    show (-1 : K) ^ (M + 1) * w ^ (6 * ((M + 1) * ((M + 1) - 1)) + 4 * (M + 1))
        = _
    rw [Nat.add_sub_cancel]
    congr 2
    ring
  have hr1 : (w : K) ^ (6 * (M * M) + 14 * M + 4)
      = w ^ (6 * (M * M) + 10 * M + 4) * (w ^ 4) ^ M := by
    rw [← pow_mul, ← pow_add]; congr 1; ring
  have hr2 : (w : K) ^ (6 * (M * M) + 10 * M)
      = w ^ (6 * (M * M) + 2 * M) * ((w ^ 4) ^ M) ^ 2 := by
    rw [← pow_mul, ← pow_mul, ← pow_add]; congr 1; ring
  rw [hshift, hrefl, hpeel, hr1, hr2]
  linear_combination (-1 : K) * hdich
    + ((-1 : K) ^ M * (w ^ (6 * (M * M) + 2 * M) * ((w ^ 4) ^ M + 1)
        - w ^ (6 * (M * M) + 10 * M + 4))) * hroot

/-- `S₁ − S₂` at the offset root `(w⁴)^{n+2} = 1` (sum truncated at `n`). -/
private theorem s1_sub_s2_offset {w : K} (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0)
    {n : ℕ} (hroot : (w ^ 4) ^ (n + 2) = 1) :
    rS1 w n - rS2 w n
      = (-1 : K) ^ n
        * (w ^ (6 * (n * n) + 14 * n + 4) - w ^ (6 * (n * n) + 10 * n)) := by
  have hrefl := s2_eq_reflect w hroot
  have hdich := gauss_dichotomy hv hroot
  have hshift := s1_eq_shift w n
  -- peel the top terms of the extended sums
  have hpeel_g2 : rgS w (n + 2)
      = rgS w (n + 1) + (-1 : K) ^ (n + 2) * w ^ (6 * (n * n) + 22 * n + 20)
      := by
    unfold rgS
    rw [Finset.sum_range_succ]
    congr 2
    show (-1 : K) ^ (n + 2) * w ^ (6 * ((n + 2) * ((n + 2) - 1)) + 4 * (n + 2))
        = _
    rw [show n + 2 - 1 = n + 1 by omega]
    congr 2
    ring
  have hpeel_g1 : rgS w (n + 1)
      = rgS w n + (-1 : K) ^ (n + 1) * w ^ (6 * (n * n) + 10 * n + 4) := by
    unfold rgS
    rw [Finset.sum_range_succ]
    congr 2
    show (-1 : K) ^ (n + 1) * w ^ (6 * ((n + 1) * ((n + 1) - 1)) + 4 * (n + 1))
        = _
    rw [Nat.add_sub_cancel]
    congr 2
    ring
  have hpeel_s2b : rS2 w (n + 2)
      = rS2 w (n + 1) + (-1 : K) ^ (n + 2) * w ^ (6 * (n * n) + 26 * n + 28)
      := by
    unfold rS2
    rw [Finset.sum_range_succ]
    congr 2
    show (-1 : K) ^ (n + 2) * w ^ (6 * ((n + 2) * ((n + 2) - 1)) + 8 * (n + 2))
        = _
    rw [show n + 2 - 1 = n + 1 by omega]
    congr 2
    ring
  have hpeel_s2a : rS2 w (n + 1)
      = rS2 w n + (-1 : K) ^ (n + 1) * w ^ (6 * (n * n) + 14 * n + 8) := by
    unfold rS2
    rw [Finset.sum_range_succ]
    congr 2
    show (-1 : K) ^ (n + 1) * w ^ (6 * ((n + 1) * ((n + 1) - 1)) + 8 * (n + 1))
        = _
    rw [Nat.add_sub_cancel]
    congr 2
    ring
  -- one linear combination over the peel/reflection/dichotomy equations;
  -- `ring` normalises the polynomial exponents, so the reflection's
  -- `6(n+2)² + 2(n+2)` unifies with the peeled `6n² + 26n + 28` atoms
  linear_combination hshift - hrefl + hpeel_s2a + hpeel_s2b + hpeel_g2
    - hdich
    + ((-1 : K) ^ n * (w ^ (6 * (n * n) + 14 * n + 4) * ((w ^ 4) ^ (n + 2) + 1)
        - w ^ (6 * (n * n) + 10 * n))) * hroot

/-- **Self-matched root evaluation** — under `(w⁴)^M = 1` and `w⁴ ≠ 1`,
    the trefoil Rosso–Jones cyclotomic sum has the closed form
    `(−1)^M w^{6M(M+2)} [M+1]_{w²}`.  (Stated with the explicit sum so
    that `trP` in `AJTrefoilAnnihilation` unfolds to it definitionally.) -/
theorem trP_sum_at_root_self {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) {M : ℕ} (hroot : (w ^ 4) ^ M = 1) :
    ∑ j ∈ range (M + 1),
        (-1 : K) ^ j * w ^ (6 * (j * (j + 1))) * qInt (w ^ 2) (2 * j + 1)
      = (-1 : K) ^ M * w ^ (6 * (M * (M + 2))) * qInt (w ^ 2) (M + 1) := by
  have hA : (w : K) ^ 2 * (w ^ 2 - (w ^ 2)⁻¹) ≠ 0 :=
    mul_ne_zero (pow_ne_zero _ hw) hv
  apply mul_left_cancel₀ hA
  rw [sum_bridge hw hv M, rhs_expand hw hv M]
  exact s1_sub_s2_self hv hroot

/-- **Offset root evaluation** — under `(w⁴)^{n+2} = 1` and `w⁴ ≠ 1`, the
    trefoil Rosso–Jones cyclotomic sum truncated at `n` has the same
    closed form `(−1)^n w^{6n(n+2)} [n+1]_{w²}`. -/
theorem trP_sum_at_root_offset {w : K} (hw : w ≠ 0)
    (hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0) {n : ℕ} (hroot : (w ^ 4) ^ (n + 2) = 1) :
    ∑ j ∈ range (n + 1),
        (-1 : K) ^ j * w ^ (6 * (j * (j + 1))) * qInt (w ^ 2) (2 * j + 1)
      = (-1 : K) ^ n * w ^ (6 * (n * (n + 2))) * qInt (w ^ 2) (n + 1) := by
  have hA : (w : K) ^ 2 * (w ^ 2 - (w ^ 2)⁻¹) ≠ 0 :=
    mul_ne_zero (pow_ne_zero _ hw) hv
  apply mul_left_cancel₀ hA
  rw [sum_bridge hw hv n, rhs_expand hw hv n]
  exact s1_sub_s2_offset hv hroot

end QOU.BraidKnot.AJTrefoil
