/-
# The level-map valuation constraint (bean qou-lm4u) — B1.5 step 2

`LevelMixingBridge.lean` states the surviving bridge form; the B1.5
design note warns that a *search* over its coefficients would fit by
construction. This file supplies the first **derived** constraint on
those coefficients, so the eventual check is over a narrowed family
rather than a free one. Nothing is fitted and nothing is searched: the
content is a divisibility theorem.

## The observation

The two sides sit on opposite sides of the `(q;q)` divide:

* the Masbaum level term `T^Mas_n = C_n(a)·(q;q)_n²` carries the
  Pochhammer in the **numerator** — it is an integer Laurent
  polynomial (merged compute: exact integer-Laurent dicts);
* the GGM block level term `T^H_m(0,λ) = (±)^m·q^{e(m,λ)}/(q;q)_m³`
  carries it in the **denominator** — a pole of order `3m` at `q = 1`,
  with a unit (monomial) numerator on the `j = 0` row.

A bridge must therefore *cancel poles*, and that is a constraint the
coefficients cannot dodge. At a single level it is sharp:

  `mas · (q;q)_m³ = c · num` with `num` a unit  ⟹  `(1 − q)^{3m} ∣ c`.

The coefficient at level `m` is forced to carry `3m` factors of
`(1 − q)`. Contrapositive (`no_single_level_of_not_dvd`): exhibiting
one coefficient that misses the divisibility rules the level out —
a **pruning test**, cheap and exact, that needs no scan.

Over `ℤ[X]` this becomes a degree bound (`natDegree_ge_of_bridge`):
a nonzero level-`m` coefficient has degree at least `3m`, so a family
of coefficients of bounded degree reaches only finitely many levels.
That is the honest form of "the module map cannot be arbitrary".

## Base ring — why NOT a field (§7c, and a vacuity trap)

Divisibility is **vacuous over a field**: every nonzero element divides
every element, so stating this over `Field R` would produce a
true-but-contentless theorem — exactly the `def : True` failure mode
the vacuity audit exists to catch. The natural home of the
coefficients is `ℤ[q^{±1}]`, so everything here is over a generic
`CommRing S`, and `qPochC` is `HabiroTailStar.qPoch`'s formula at that
weaker typeclass (`qPochC_eq_qPoch`, definitional). No archimedean
construct appears; pre-wall throughout.

## Scope

This constrains; it does not construct. No bridge is claimed to exist,
no coefficients are proposed, nothing is wired. Comparison to observed
only; no ontological claims.
-/
import QOU.QBeta.HabiroTailStar

namespace QOU.QBeta.LevelMixing

open Finset

section CommRingCase

variable {S : Type*} [CommRing S]

/-- `(q;q)_m = ∏_{j=1..m} (1 − q^j)` over a generic commutative ring —
the same formula as `HabiroTailStar.qPoch`, at the weaker typeclass the
divisibility statements need (see the header: over a field they would
be vacuous). -/
def qPochC (q : S) (m : ℕ) : S := ∏ j ∈ range m, (1 - q ^ (j + 1))

/-- `(1 − q)^m ∣ (q;q)_m`: each factor `1 − q^{j+1}` is divisible by
`1 − q`. -/
lemma sub_one_pow_dvd_qPochC (q : S) (m : ℕ) :
    (1 - q) ^ m ∣ qPochC q m := by
  have h : ∀ j ∈ range m, (1 - q) ∣ (1 - q ^ (j + 1)) := by
    intro j _
    have := sub_dvd_pow_sub_pow (1 : S) q (j + 1)
    simpa using this
  calc (1 - q) ^ m = ∏ _j ∈ range m, (1 - q) := by
        rw [Finset.prod_const, card_range]
    _ ∣ ∏ j ∈ range m, (1 - q ^ (j + 1)) :=
        Finset.prod_dvd_prod_of_dvd _ _ h
    _ = qPochC q m := rfl

/-- `(1 − q)^{3m} ∣ (q;q)_m³`. -/
lemma sub_one_pow_dvd_qPochC_cube (q : S) (m : ℕ) :
    (1 - q) ^ (3 * m) ∣ qPochC q m ^ 3 := by
  rw [mul_comm 3 m, pow_mul]
  exact pow_dvd_pow_of_dvd (sub_one_pow_dvd_qPochC q m) 3

/-- **The derived constraint.** If a single GGM block level `m` carries
the whole bridge — `mas · (q;q)_m³ = c · num` with the block numerator
`num` a unit (as it is on the `j = 0` row, a monomial) — then the
coefficient is forced to carry `3m` factors of `(1 − q)`.

This is what pole cancellation costs: the block's order-`3m` pole at
`q = 1` must be paid for by the coefficient, since the Masbaum side is
regular there. -/
theorem sub_one_pow_dvd_coeff_single_level (q : S) {mas c num : S}
    (hu : IsUnit num) (m : ℕ) (h : mas * qPochC q m ^ 3 = c * num) :
    (1 - q) ^ (3 * m) ∣ c := by
  have h2 : (1 - q) ^ (3 * m) ∣ c * num :=
    h ▸ (sub_one_pow_dvd_qPochC_cube q m).mul_left mas
  obtain ⟨v, hv⟩ := hu
  obtain ⟨w, hw⟩ := h2
  exact ⟨w * (v⁻¹ : Sˣ), by
    rw [← mul_assoc, ← hw, ← hv, mul_assoc, Units.mul_inv, mul_one]⟩

/-- **The pruning form (contrapositive).** A coefficient that misses the
divisibility rules its level out — no scan required. -/
theorem no_single_level_of_not_dvd (q : S) {mas c num : S}
    (hu : IsUnit num) (m : ℕ) (hnd : ¬ (1 - q) ^ (3 * m) ∣ c) :
    mas * qPochC q m ^ 3 ≠ c * num :=
  fun h => hnd (sub_one_pow_dvd_coeff_single_level q hu m h)

/-- The Masbaum level term `C_n·(q;q)_n²` is itself divisible by
`(1 − q)^{2n}` — its Pochhammer sits in the numerator, so it
*contributes* vanishing at `q = 1` rather than consuming it. -/
lemma sub_one_pow_dvd_masLevel (q Cn : S) (n : ℕ) :
    (1 - q) ^ (2 * n) ∣ Cn * qPochC q n ^ 2 := by
  have h : (1 - q) ^ (2 * n) ∣ qPochC q n ^ 2 := by
    rw [mul_comm 2 n, pow_mul]
    exact pow_dvd_pow_of_dvd (sub_one_pow_dvd_qPochC q n) 2
  exact h.mul_left Cn

/-- **The sharpened constraint.** Both sides contribute: the block's
order-`3m` pole must be paid for, *and* the Masbaum level term already
vanishes to order `2n`. So the forced coefficient carries
`(1 − q)^{2n + 3m}`, not merely `(1 − q)^{3m}`.

This is strictly stronger than `sub_one_pow_dvd_coeff_single_level`
(which is the `n = 0` case) and it is the bound that matters: the
Masbaum index `n` is the one that runs when more orders are demanded. -/
theorem sub_one_pow_dvd_coeff_combined (q : S) {Cn c num : S}
    (hu : IsUnit num) (n m : ℕ)
    (h : Cn * qPochC q n ^ 2 * qPochC q m ^ 3 = c * num) :
    (1 - q) ^ (2 * n + 3 * m) ∣ c := by
  have h2 : (1 - q) ^ (2 * n + 3 * m) ∣ c * num := by
    rw [← h, pow_add]
    exact mul_dvd_mul (sub_one_pow_dvd_masLevel q Cn n)
      (sub_one_pow_dvd_qPochC_cube q m)
  obtain ⟨v, hv⟩ := hu
  obtain ⟨w, hw⟩ := h2
  exact ⟨w * (v⁻¹ : Sˣ), by
    rw [← mul_assoc, ← hw, ← hv, mul_assoc, Units.mul_inv, mul_one]⟩

/-- **The full-product constraint — strictly stronger than the
`(1 − q)`-adic one.** The `(1 − q)^{2n+3m}` bound above only reads off
the vanishing at `q = 1`; but the *entire* Pochhammer product divides
the coefficient. Since
`(q;q)_k = ∏_d Φ_d^{⌊k/d⌋}` ranges over every cyclotomic factor, this
captures the constraint at **every** root of unity at once, not just at
`q = 1`.

Its degree consequence is quadratic rather than linear
(`natDegree_ge_quadratic`), which shrinks the reachable region from
`O(D²)` pairs to `O(D)`. -/
theorem qPoch_prod_dvd_coeff (q : S) {Cn c num : S} (hu : IsUnit num)
    (n m : ℕ) (h : Cn * qPochC q n ^ 2 * qPochC q m ^ 3 = c * num) :
    qPochC q n ^ 2 * qPochC q m ^ 3 ∣ c := by
  have h2 : qPochC q n ^ 2 * qPochC q m ^ 3 ∣ c * num :=
    ⟨Cn, by rw [← h]; ring⟩
  obtain ⟨v, hv⟩ := hu
  obtain ⟨w, hw⟩ := h2
  exact ⟨w * (v⁻¹ : Sˣ), by
    rw [← mul_assoc, ← hw, ← hv, mul_assoc, Units.mul_inv, mul_one]⟩

end CommRingCase

section FieldCompat

variable {R : Type*} [Field R]

/-- `qPochC` is `HabiroTailStar.qPoch`'s formula — the two agree
definitionally wherever both typecheck. -/
lemma qPochC_eq_qPoch (q : R) (m : ℕ) :
    qPochC q m = QOU.QBeta.HabiroTailStar.qPoch q m := rfl

end FieldCompat

section DegreeBound

open Polynomial

/-- `(1 − X)^k` has degree `k` in `ℤ[X]`. -/
lemma natDegree_one_sub_X_pow (k : ℕ) :
    ((1 - X : ℤ[X]) ^ k).natDegree = k := by
  have h1 : (1 - X : ℤ[X]).natDegree = 1 := by
    compute_degree!
  rw [Polynomial.natDegree_pow, h1, mul_one]

/-- **Degree bound.** A nonzero level-`m` bridge coefficient in `ℤ[X]`
has degree at least `3m`. Consequence: coefficients drawn from any
bounded-degree family reach only finitely many levels — the module map
cannot be arbitrary, which is precisely the narrowing the B1.5 design
note asked for before any check is run. -/
theorem natDegree_ge_of_bridge {mas c num : ℤ[X]} (hu : IsUnit num)
    (m : ℕ) (hc : c ≠ 0) (h : mas * qPochC X m ^ 3 = c * num) :
    3 * m ≤ c.natDegree := by
  have hdvd := sub_one_pow_dvd_coeff_single_level X hu m h
  have := Polynomial.natDegree_le_of_dvd hdvd hc
  rwa [natDegree_one_sub_X_pow] at this

/-- **The sharpened degree bound.** A nonzero coefficient joining
Masbaum level `n` to block level `m` has degree at least `2n + 3m`.

Both indices cost. Demanding more orders of the tail pushes `n` up,
and each unit of `n` costs two more degrees of coefficient — so a
level map whose coefficients are drawn from any fixed bounded-degree
family covers only a finite triangle of `(n, m)` pairs. -/
theorem natDegree_ge_of_bridge_combined {Cn c num : ℤ[X]} (hu : IsUnit num)
    (n m : ℕ) (hc : c ≠ 0)
    (h : Cn * qPochC X n ^ 2 * qPochC X m ^ 3 = c * num) :
    2 * n + 3 * m ≤ c.natDegree := by
  have hdvd := sub_one_pow_dvd_coeff_combined X hu n m h
  have := Polynomial.natDegree_le_of_dvd hdvd hc
  rwa [natDegree_one_sub_X_pow] at this

/-- **A degree budget caps the reachable Masbaum level.** If the
coefficient joining level `n` has degree at most `D`, then `2n ≤ D`:
only levels `n ≤ D/2` are reachable, whatever `m` is. -/
theorem level_le_of_natDegree_le {Cn c num : ℤ[X]} (hu : IsUnit num)
    (n m D : ℕ) (hc : c ≠ 0)
    (h : Cn * qPochC X n ^ 2 * qPochC X m ^ 3 = c * num)
    (hD : c.natDegree ≤ D) : 2 * n ≤ D := by
  have := natDegree_ge_of_bridge_combined hu n m hc h
  omega

/-- **No bounded-degree level map bridges the tail.** If a level map
intertwines at *every* Masbaum level with nonzero coefficients, then its
coefficient degrees are unbounded: for any budget `D` some level needs
a coefficient of degree exceeding `D`.

So there is no "small" universal bridge. Any level-mixing map valid at
all orders has coefficients whose complexity grows without bound —
which is a structural fact about the surviving family, obtained without
searching it. -/
theorem natDegree_unbounded_of_all_levels
    {C c num : ℕ → ℤ[X]} {mm : ℕ → ℕ}
    (hu : ∀ n, IsUnit (num n)) (hc : ∀ n, c n ≠ 0)
    (h : ∀ n, C n * qPochC X n ^ 2 * qPochC X (mm n) ^ 3 = c n * num n)
    (D : ℕ) : ∃ n, D < (c n).natDegree := by
  refine ⟨D + 1, ?_⟩
  have := natDegree_ge_of_bridge_combined (hu (D + 1)) (D + 1) (mm (D + 1))
    (hc (D + 1)) (h (D + 1))
  omega

/-- `1 − X^{k+1}` has degree `k+1`. -/
lemma natDegree_one_sub_X_pow_succ (k : ℕ) :
    ((1 : ℤ[X]) - X ^ (k + 1)).natDegree = k + 1 := by
  compute_degree!

lemma one_sub_X_pow_succ_ne_zero (k : ℕ) : ((1 : ℤ[X]) - X ^ (k + 1)) ≠ 0 := by
  intro h
  have hd := natDegree_one_sub_X_pow_succ k
  rw [h] at hd
  simp at hd

lemma qPochC_succ_eq (n : ℕ) :
    qPochC (X : ℤ[X]) (n + 1) = qPochC X n * (1 - X ^ (n + 1)) := by
  simp only [qPochC, Finset.prod_range_succ]

lemma qPochC_ne_zero (n : ℕ) : qPochC (X : ℤ[X]) n ≠ 0 := by
  induction n with
  | zero => simp [qPochC]
  | succ n ih =>
    rw [qPochC_succ_eq]
    exact mul_ne_zero ih (one_sub_X_pow_succ_ne_zero n)

/-- `deg (q;q)_n = n(n+1)/2`, stated doubled to stay in `ℕ`. -/
lemma natDegree_qPochC (n : ℕ) :
    2 * (qPochC (X : ℤ[X]) n).natDegree = n * (n + 1) := by
  induction n with
  | zero => simp [qPochC]
  | succ n ih =>
    rw [qPochC_succ_eq,
        Polynomial.natDegree_mul (qPochC_ne_zero n)
          (one_sub_X_pow_succ_ne_zero n),
        natDegree_one_sub_X_pow_succ]
    have hexp : (n + 1) * (n + 1 + 1) = n * (n + 1) + 2 * (n + 1) := by ring
    rw [hexp, ← ih]
    ring

/-- **The quadratic degree bound.** A nonzero coefficient joining
Masbaum level `n` to block level `m` satisfies

`2·deg c ≥ 2n(n+1) + 3m(m+1)`,

i.e. `deg c ≥ n(n+1) + 3m(m+1)/2` — **quadratic in both indices**, not
linear. This supersedes `natDegree_ge_of_bridge_combined` (whose
`2n+3m` reads only the `q = 1` vanishing); the full Pochhammer product
carries every cyclotomic factor.

Consequence: the reachable region under a degree budget `D` shrinks
from `O(D²)` pairs to `O(D)` — `n ≲ √D` and `m ≲ √(2D/3)`. -/
theorem natDegree_ge_quadratic {Cn c num : ℤ[X]} (hu : IsUnit num)
    (n m : ℕ) (hc : c ≠ 0)
    (h : Cn * qPochC X n ^ 2 * qPochC X m ^ 3 = c * num) :
    2 * (n * (n + 1)) + 3 * (m * (m + 1)) ≤ 2 * c.natDegree := by
  have hdvd := qPoch_prod_dvd_coeff X hu n m h
  have hne : (qPochC (X : ℤ[X]) n ^ 2 * qPochC (X : ℤ[X]) m ^ 3) ≠ 0 :=
    mul_ne_zero (pow_ne_zero _ (qPochC_ne_zero n))
      (pow_ne_zero _ (qPochC_ne_zero m))
  have hle := Polynomial.natDegree_le_of_dvd hdvd hc
  rw [Polynomial.natDegree_mul (pow_ne_zero _ (qPochC_ne_zero n))
        (pow_ne_zero _ (qPochC_ne_zero m)),
      Polynomial.natDegree_pow, Polynomial.natDegree_pow] at hle
  have hn := natDegree_qPochC n
  have hm := natDegree_qPochC m
  omega

end DegreeBound

end QOU.QBeta.LevelMixing
