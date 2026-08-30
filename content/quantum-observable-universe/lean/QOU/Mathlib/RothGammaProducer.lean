/-
# `Γ_m`, produced from height data

⚠⚠ **The clause set `RothGammaFull` had never been PRODUCED.**  Before this module it was
constructed in exactly three places, none of them a production: `RothGammaFull.rename_equiv`
(transport), `rothGammaFull_descend` (consumes a `Γ_{n+1}`), and two hand-built structure
literals at `m = 2`.  So its seven clauses had never been discharged from Diophantine data at
any `m ≥ 3`, and `index_le_rothBound` — Roth's Lemma — was a theorem about a hypothesis nothing
had been asked to supply.

That is correction 9's lesson at arc scale: *a hypothesis nobody has had to discharge is
indistinguishable from a false one.*  This module discharges it.

## The construction, and why it needs no logarithms

Mahler normalises `r_h · log H_h ≈ const`.  Every clause of `Γ_m` is **multiplicative**, so the
normalisation can be written with `Nat.log` and never leaves `ℕ`:

    N          the common scale
    d h  :=    Nat.log (H h) N,      at h = 0   (FLOOR)
               Nat.log (H h) N + 1,  otherwise  (CEILING)

The floor/ceiling split is not cosmetic.  It puts `H₀^{d₀} ≤ N < H_k^{d_k}`, which is clause 2
(`the first K^s is the smallest`) **on the nose** rather than up to rounding.  A uniform choice
gives all `H_h^{d_h}` in the same interval `(N, N·H_h]` and orders none of them.

Clause 1 (growth) then reduces to an integer inequality — `two_mul_lt_of_height_growth` — given
that the heights grow rapidly: `H_j^{2q} ≤ H_k^p` for consecutive `j, k`.  The factor `2` is the
margin the rounding costs; with it, growth holds as soon as `p·d_j ≥ p + 2q`, which is Roth's
"choose `r₁` sufficiently large" reduced to a finite arithmetic condition.

⚠ Not Mathlib-only: imports `QOU/Mathlib/RothRealLadder.lean`, so that the produced `Γ_3` can be
fed straight into Roth's Lemma at the bottom of the file.
-/
import QOU.Mathlib.RothRealLadder

namespace MvPolynomial


/-- **The producer's core.**  Rapid height growth turns a pair of `Nat.log` brackets into an
integer inequality between the degrees.  No logarithm appears in the statement, and none in the
proof — `Γ_m`'s clauses are multiplicative, so the whole normalisation is `Nat.pow` monotonicity. -/
theorem two_mul_lt_of_height_growth {Hj Hk N B C p q : ℕ}
    (hHj : 2 ≤ Hj) (hp : 0 < p) (hgrow : Hj ^ (2 * q) ≤ Hk ^ p)
    (hlo : Hk ^ C ≤ N) (hhi : N < Hj ^ B) :
    2 * q * C < p * B := by
  have h1 : Hj ^ (2 * q * C) ≤ Hk ^ (p * C) := by
    rw [pow_mul Hj (2 * q) C, pow_mul Hk p C]
    exact Nat.pow_le_pow_left hgrow C
  have h2 : Hk ^ (p * C) ≤ N ^ p := by
    rw [mul_comm p C, pow_mul Hk C p]
    exact Nat.pow_le_pow_left hlo p
  have h3 : N ^ p < (Hj ^ B) ^ p := Nat.pow_lt_pow_left hhi (by omega)
  refine (Nat.pow_lt_pow_iff_right hHj).mp ?_
  calc Hj ^ (2 * q * C) ≤ Hk ^ (p * C) := h1
    _ ≤ N ^ p := h2
    _ < (Hj ^ B) ^ p := h3
    _ = Hj ^ (p * B) := by rw [← pow_mul, mul_comm B p]

/-- **The degree vector Roth's setup produces from a height vector.**

Every `H h ^ d h` is pinned to the same scale `N` — Mahler's normalisation `r_h·log H_h ≈ const`,
written without logarithms.  The first index takes the **floor** and the rest the **ceiling**,
which is what makes clause 2 (`H₁^{r₁}` smallest) hold on the nose rather than up to rounding. -/
noncomputable def rothDegrees {m : ℕ} (H : Fin m → ℕ) (N : ℕ) : Fin m → ℕ :=
  fun h => if (h : ℕ) = 0 then Nat.log (H h) N else Nat.log (H h) N + 1

theorem rothDegrees_zero_le {m : ℕ} (H : Fin m → ℕ) {N : ℕ} (hN : N ≠ 0)
    {h : Fin m} (he : (h : ℕ) = 0) : H h ^ rothDegrees H N h ≤ N := by
  rw [rothDegrees, if_pos he]; exact Nat.pow_log_le_self _ hN

theorem lt_rothDegrees_succ {m : ℕ} (H : Fin m → ℕ) {N : ℕ} {h : Fin m} (hH : 2 ≤ H h)
    (he : (h : ℕ) = 0) : N < H h ^ (rothDegrees H N h + 1) := by
  rw [rothDegrees, if_pos he]; exact Nat.lt_pow_succ_log_self hH N

theorem lt_rothDegrees {m : ℕ} (H : Fin m → ℕ) {N : ℕ} {h : Fin m} (hH : 2 ≤ H h)
    (hne : (h : ℕ) ≠ 0) : N < H h ^ rothDegrees H N h := by
  rw [rothDegrees, if_neg hne]; exact Nat.lt_pow_succ_log_self hH N

theorem rothDegrees_sub_one_le {m : ℕ} (H : Fin m → ℕ) {N : ℕ} (hN : N ≠ 0)
    {h : Fin m} (hne : (h : ℕ) ≠ 0) : H h ^ (rothDegrees H N h - 1) ≤ N := by
  rw [rothDegrees, if_neg hne, Nat.add_sub_cancel]; exact Nat.pow_log_le_self _ hN

/-- **Clause 2 holds on the nose.**  The floor at index `0` and the ceiling elsewhere put
`H₀^{d₀} ≤ N < H_k^{d_k}`, which is exactly "the first `K^s` is the smallest". -/
theorem rothDegrees_height {m : ℕ} (H : Fin m → ℕ) {N : ℕ} (hN : N ≠ 0) (hH : ∀ h, 2 ≤ H h)
    (j k : Fin m) (hj : (j : ℕ) = 0) :
    H j ^ rothDegrees H N j ≤ H k ^ rothDegrees H N k := by
  rcases eq_or_ne (k : ℕ) 0 with hk | hk
  · have hjk : j = k := Fin.ext (by omega)
    rw [hjk]
  · exact le_of_lt (lt_of_le_of_lt (rothDegrees_zero_le H hN hj) (lt_rothDegrees H (hH k) hk))

/-- **Clause 1 holds once the degrees are large enough**, and `p·d_j ≥ p + 2q` is exactly how
large.  That is Roth's "choose `r₁` sufficiently large", made a finite arithmetic condition. -/
theorem rothDegrees_growth_nat {m : ℕ} (H : Fin m → ℕ) {N : ℕ} {p q : ℕ}
    (hp : 0 < p) (hN : N ≠ 0) (hH : ∀ h, 2 ≤ H h)
    (hgrow : ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p)
    (hlarge : ∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h)
    (j k : Fin m) (hjk : (j : ℕ) + 1 = (k : ℕ)) :
    q * rothDegrees H N k ≤ p * rothDegrees H N j := by
  have hk0 : (k : ℕ) ≠ 0 := by omega
  have hC : H k ^ Nat.log (H k) N ≤ N := Nat.pow_log_le_self _ hN
  have hdk : rothDegrees H N k = Nat.log (H k) N + 1 := by rw [rothDegrees, if_neg hk0]
  have hlj := hlarge j
  set L := Nat.log (H k) N with hL
  set dj := rothDegrees H N j with hdj
  have e1 : 2 * q * L = 2 * (q * L) := by ring
  have e3 : q * (L + 1) = q * L + q := by ring
  rw [hdk]
  rcases eq_or_ne (j : ℕ) 0 with hj | hj
  · have hB : N < H j ^ (dj + 1) := lt_rothDegrees_succ H (hH j) hj
    have h1 := two_mul_lt_of_height_growth (hH j) hp (hgrow j k hjk) hC hB
    have e2 : p * (dj + 1) = p * dj + p := by ring
    omega
  · have hB : N < H j ^ dj := lt_rothDegrees H (hH j) hj
    have h1 := two_mul_lt_of_height_growth (hH j) hp (hgrow j k hjk) hC hB
    omega

theorem rothDegrees_growth {m : ℕ} (H : Fin m → ℕ) {N : ℕ} {p q : ℕ}
    (hp : 0 < p) (hN : N ≠ 0) (hH : ∀ h, 2 ≤ H h)
    (hgrow : ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p)
    (hlarge : ∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h) :
    RothGrowth (Equiv.refl (Fin m)) ((q : ℚ) / (p : ℚ)) (rothDegrees H N) := by
  intro j k hjk
  have hpQ : (0 : ℚ) < (p : ℚ) := by exact_mod_cast hp
  have hnat := rothDegrees_growth_nat H hp hN hH hgrow hlarge j k (by simpa using hjk)
  have hQ : (q : ℚ) * (rothDegrees H N k : ℚ) ≤ (p : ℚ) * (rothDegrees H N j : ℚ) := by
    exact_mod_cast hnat
  simp only [Equiv.refl_symm, Equiv.refl_apply]
  rw [div_mul_eq_mul_div, div_le_iff₀ hpQ]
  linarith

/-- **`Γ_m`, produced.**  Given heights that grow rapidly enough and a common scale `N`, the
normalised degrees satisfy every clause of `RothGammaFull`.

⚠ This is the first construction of `Γ_m` in the arc that is not a transport
(`rename_equiv`), a descent (`rothGammaFull_descend`), or a hand-built literal.  Clauses 1 and 2
come from the normalisation; 3a, 3b and 4 are conditions on `F` and `b` that the caller supplies,
because they constrain data this construction does not choose. -/
theorem rothGammaFull_of_heights {m : ℕ} (H : Fin m → ℕ) {N : ℕ} {p q F : ℕ} {b : ℤ}
    (hp : 0 < p) (hN : N ≠ 0) (hH : ∀ h, 2 ≤ H h)
    (hgrow : ∀ j k : Fin m, (j : ℕ) + 1 = (k : ℕ) → H j ^ (2 * q) ≤ H k ^ p)
    (hlarge : ∀ h : Fin m, p + 2 * q ≤ p * rothDegrees H N h)
    (hfloorExp : q * ((m - 1) * m * (2 * m + 1)) ≤ F * p)
    (hfloor : ∀ j : Fin m, (j : ℕ) = 0 → (2 : ℤ) ^ F ≤ (H j : ℤ))
    (hbound : ∀ j : Fin m, (j : ℕ) = 0 →
      b ^ (m * q) ≤ (H j : ℤ) ^ (rothDegrees H N j * p)) :
    RothGammaFull (Equiv.refl (Fin m)) p q F (rothDegrees H N) (fun j => (H j : ℤ)) b where
  growth := rothDegrees_growth H hp hN hH hgrow hlarge
  height := by
    intro j k hj
    simp only [Equiv.refl_symm, Equiv.refl_apply]
    exact_mod_cast rothDegrees_height H hN hH j k (by simpa using hj)
  floorExp := hfloorExp
  floor := by intro j hj; simpa using hfloor j (by simpa using hj)
  heightBound := by intro j hj; simpa using hbound j (by simpa using hj)
  two_le := fun j => by exact_mod_cast hH j
  degPos := by
    intro k
    have h := hlarge k
    intro hz
    rw [hz, Nat.mul_zero] at h
    omega

/-! ### `Γ_3` at `t = 1/2`, produced

The arc's `Γ` witnesses were all at `m = 2` and all hand-built, and the one attached to
`index_le_rothBound` sat at `t = 1`, where the bound it exhibits is trivial.  This one is at
`m = 3` and `t = 1/2`, and every clause comes out of `rothGammaFull_of_heights` rather than out
of a structure literal.

The numbers are **forced, not chosen**.  Clause 3a reads `q·(m−1)m(2m+1) ≤ F·p`, which at
`m = 3, p = 1, q = 2` is `84 ≤ F`; clause 3b then demands `2^84 ≤ H₁`.  The rapid-growth
hypothesis `H_j^{2q} ≤ H_k^p` is `H_j^4 ≤ H_k`, so the heights are

    H = (2^84, 2^336, 2^1344),   N = 2^6720,   d = (80, 21, 6)

and `N` is a common power of all three heights, which is what makes the three `Nat.log`s exact.
⚠ `d` is **decreasing** and `H^d` is **increasing** — `2^6720 < 2^7056 < 2^8064` — which is
clauses 1 and 2 pulling in opposite directions and both holding. That is the joint satisfiability
that had never been exhibited above `m = 2`.
-/


def Hw : Fin 3 → ℕ := fun h => 2 ^ (84 * 4 ^ (h : ℕ))
def Nw : ℕ := 2 ^ 6720

theorem hw_two_le : ∀ h, 2 ≤ Hw h := by
  intro h; rw [Hw]
  exact Nat.le_self_pow (by positivity) 2

theorem deg0 : rothDegrees Hw Nw 0 = 80 := by
  rw [rothDegrees, if_pos (by rfl), show Hw 0 = 2 ^ 84 by rw [Hw]; norm_num,
    show Nw = (2 ^ 84) ^ 80 by rw [Nw, ← pow_mul]]
  exact Nat.log_pow (by norm_num) 80

theorem deg1 : rothDegrees Hw Nw 1 = 21 := by
  rw [rothDegrees, if_neg (by decide), show Hw 1 = 2 ^ 336 by rw [Hw]; norm_num,
    show Nw = (2 ^ 336) ^ 20 by rw [Nw, ← pow_mul]]
  rw [Nat.log_pow (by norm_num) 20]

theorem deg2 : rothDegrees Hw Nw 2 = 6 := by
  rw [rothDegrees, if_neg (by decide), show Hw 2 = 2 ^ 1344 by rw [Hw]; norm_num,
    show Nw = (2 ^ 1344) ^ 5 by rw [Nw, ← pow_mul]]
  rw [Nat.log_pow (by norm_num) 5]

theorem hw_grow : ∀ j k : Fin 3, (j : ℕ) + 1 = (k : ℕ) → Hw j ^ (2 * 2) ≤ Hw k ^ 1 := by
  intro j k hjk
  rw [Hw, Hw, ← hjk, ← pow_mul, pow_one]
  refine Nat.pow_le_pow_right (by norm_num) ?_
  rw [pow_succ]; ring_nf; omega

theorem hw_large : ∀ h : Fin 3, 1 + 2 * 2 ≤ 1 * rothDegrees Hw Nw h := by
  intro h
  fin_cases h
  · show 1 + 2 * 2 ≤ 1 * rothDegrees Hw Nw 0
    rw [deg0]; norm_num
  · show 1 + 2 * 2 ≤ 1 * rothDegrees Hw Nw 1
    rw [deg1]; norm_num
  · show 1 + 2 * 2 ≤ 1 * rothDegrees Hw Nw 2
    rw [deg2]; norm_num

/-- **`Γ_3` produced from height data, at `t = 1/2 < 1`.** -/
theorem gamma_three :
    RothGammaFull (Equiv.refl (Fin 3)) 1 2 84 (rothDegrees Hw Nw) (fun j => (Hw j : ℤ)) 1 :=
  rothGammaFull_of_heights Hw (N := Nw) (p := 1) (q := 2) (F := 84) (b := 1)
    one_pos (by rw [Nw]; positivity) hw_two_le hw_grow hw_large (by norm_num)
    (by
      intro j hj
      have : j = 0 := Fin.ext (by simpa using hj)
      subst this
      rw [show Hw 0 = 2 ^ 84 by rw [Hw]; norm_num]
      push_cast)
    (by
      intro j hj
      have : j = 0 := Fin.ext (by simpa using hj)
      subst this
      rw [deg0, show Hw 0 = 2 ^ 84 by rw [Hw]; norm_num]
      push_cast)


/-! ### The loop, closed

`index_le_rothBound` is Roth's Lemma; `gamma_three` is a `Γ_3` nothing assumed.  Composing them
is the first statement in the arc where **both** sides are discharged: the hypothesis is produced
from height data, and the conclusion is a bound on an actual index.

At `m = 3` the constant is `rothConstant 3 = 2⁴ − 3 = 13`, so the bound reads
`Θ⁴ ≤ 13⁴ · ½`, i.e. `Θ ≤ 13/2^{1/4} ≈ 10.9`.

⚠ That number is not small, and saying so matters more than the theorem reads.  `Θ_m ≤ m` holds
outright (`IsRothTheta.le_card`), so at `m = 3` **the trivial bound is 3 and this one is 10.9**:
Roth's Lemma is *weaker* than the trivial bound here. It has to be — the strength is asymptotic
in `t`, and `t = ½` is nowhere near the regime the theorem is for. What this witness establishes
is that the machine runs end to end on data it produced itself, not that the number it emits is
useful at these parameters. Both are worth having; only the first was missing. -/
/-- **Roth's Lemma at `m = 3`, `t = 1/2`, on a produced `Γ_3`.** -/
theorem roth_three :
    ∃ Θ : ℚ, 0 ≤ Θ ∧
      Θ ^ (2 ^ (3 - 1)) ≤ (rothConstant 3 : ℚ) ^ (2 ^ (3 - 1)) * ((1 : ℚ) / (2 : ℚ)) ∧
      index (rothDegrees Hw Nw) (fun h => (Hw h : ℚ))
          (map (algebraMap ℤ ℚ) (1 : MvPolynomial (Fin 3) ℤ)) ≤ ((Θ : ℚ) : WithTop ℚ) :=
  index_le_rothBound (m := 3) (by norm_num) (p := 1) (q := 2) (F := 84) one_pos (by norm_num)
    (Equiv.refl (Fin 3)) gamma_three
    (A := 1) (κ := fun h => (Hw h : ℚ))
    ⟨one_ne_zero, fun h => by rw [← C_1, degreeOf_C]; norm_num, fun n => by
      simp only [coeff_one]; split_ifs <;> norm_num⟩
    (by intro h; simp; have := hw_two_le h; omega)


end MvPolynomial
