import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# The algebraic pole half of `conj:algebraic-geometric-dilog-equivalence`

`conj:algebraic-geometric-dilog-equivalence` (mass-theory) is **downstream of
the Kashaev–Murakami–Murakami volume conjecture** and is therefore, per
AGENTS.md §3b and the anti-laundering rule, a genuine **conjecture** — not
provable by axiomatisation. Its *asymptotic/geometric* content (partial product
→ Bloch–Wigner volume; poles ↔ ideal-tetrahedron cusps) is the volume
conjecture and stays open in general (the **figure-eight** case is the known
theorem of Andersen–Hansen 2006 / Ohtsuki).

Its **algebraic half is unconditionally a theorem**, and this file proves it
sorry-free: the q-Pochhammer partial denominator `(x;q)_n = ∏_{k<n}(1 − x qᵏ)`
vanishes **exactly** at the poles `x = q^{-k}`, `k < n`. This is the rigorous
"pole" side of the pole-to-cusp bijection — the seed data that
`thurston-relaxation.md` feeds to the Newton solve. It does **not** establish
the cusp correspondence (geometric, conjectural).

Base ring: a generic `[Field K]` (the negative powers `q^{-k}` need inverses;
`q ≠ 0`). No `ℝ` — the pole structure is algebraic, not archimedean (§7c).
-/

namespace QOU.QBeta

/-- q-Pochhammer partial denominator `(x; q)_n = ∏_{k=0}^{n-1}(1 − x qᵏ)`. -/
def qPochDenom {K : Type*} [Field K] (q x : K) : ℕ → K
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * qPochDenom q x n

@[simp] theorem qPochDenom_zero {K : Type*} [Field K] (q x : K) :
    qPochDenom q x 0 = 1 := Eq.refl _

theorem qPochDenom_succ {K : Type*} [Field K] (q x : K) (n : ℕ) :
    qPochDenom q x (n + 1) = (1 - x * q ^ n) * qPochDenom q x n := Eq.refl _

/-- **The pole vanishing.** `(x; q)_n` vanishes at each pole `x = q^{-j}`,
    `j < n` — the algebraic, unconditional half of the pole-to-cusp bijection
    (`conj:algebraic-geometric-dilog-equivalence §1`). -/
theorem qPochDenom_eq_zero_at_pole {K : Type*} [Field K] (q : K) (hq : q ≠ 0)
    (n j : ℕ) (hj : j < n) : qPochDenom q (q ^ (-(j : ℤ))) n = 0 := by
  induction n with
  | zero => exact absurd hj (Nat.not_lt_zero j)
  | succ m ih =>
    rw [qPochDenom_succ]
    rcases (Nat.lt_succ_iff.mp hj).lt_or_eq with h | h
    · rw [ih h, mul_zero]
    · have key : q ^ (-(j : ℤ)) * q ^ (m : ℕ) = 1 := by
        rw [h, ← zpow_natCast q m, ← zpow_add₀ hq, neg_add_cancel, zpow_zero]
      rw [key, sub_self, zero_mul]

/-- The pole set `{q^{-k} : k < n}` is contained in the zero set of `(x;q)_n`;
    stated as the roots exist as the explicit function `k ↦ q^{-k}` **and**
    each is a genuine root (the content the bare `∃ z, z k = q^{-k}` field of
    the conjecture class omits). -/
theorem qPochDenom_poles {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ) :
    ∃ z : Fin n → K, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, qPochDenom q (z k) n = 0) :=
  ⟨fun k => q ^ (-(k : ℤ)), fun _ => rfl,
    fun k => qPochDenom_eq_zero_at_pole q hq n k k.isLt⟩

/-- **Exact zero locus of the `q`-Pochhammer partial denominator (`qou-mfdq`).**
    Over any field `K` with `q ≠ 0`, `qPochDenom q x n = 0` holds if and only
    if `x = q^{-j}` for some `j : Fin n`. -/
theorem qPochDenom_eq_zero_iff {K : Type*} [Field K] (q x : K) (hq : q ≠ 0) (n : ℕ) :
    qPochDenom q x n = 0 ↔ ∃ j : Fin n, x = q ^ (-(j : ℤ)) := by
  constructor
  · induction n with
    | zero =>
      intro h
      exact absurd h one_ne_zero
    | succ m ih =>
      rw [qPochDenom_succ, mul_eq_zero]
      rintro (hfactor | htail)
      · refine ⟨⟨m, Nat.lt_succ_self m⟩, ?_⟩
        have hmul : x * q ^ m = 1 := (sub_eq_zero.mp hfactor).symm
        have hqm : q ^ m ≠ 0 := pow_ne_zero m hq
        have hx : x = (q ^ m)⁻¹ := by
          calc x = x * q ^ m * (q ^ m)⁻¹ := by rw [mul_inv_cancel_right₀ hqm]
            _ = 1 * (q ^ m)⁻¹ := by rw [hmul]
            _ = (q ^ m)⁻¹ := one_mul _
        rw [hx, zpow_neg, zpow_natCast]
      · rcases ih htail with ⟨j, hj⟩
        exact ⟨⟨j.val, Nat.lt_succ_of_lt j.isLt⟩, hj⟩
  · rintro ⟨j, rfl⟩
    exact qPochDenom_eq_zero_at_pole q hq n j.val j.isLt

/-- **Cardinality obstruction to an `n`-pole ↔ 4-vertex bijection (`qou-mfdq`, Finding 1).**
    The `n`-element pole index set `Fin n` admits a bijection with a 4-element
    ideal-tetrahedron vertex set `Fin 4` if and only if `n = 4`. -/
theorem pole_fin_equiv_fin_four_iff (n : ℕ) :
    Nonempty (Fin n ≃ Fin 4) ↔ n = 4 := by
  constructor
  · rintro ⟨e⟩
    simpa using Fintype.card_congr e
  · rintro rfl
    exact ⟨Equiv.refl (Fin 4)⟩

/-- **For any `n ≠ 4`, no bijection `Fin n ≃ Fin 4` exists (`qou-mfdq`).** -/
theorem not_pole_fin_equiv_fin_four_of_ne {n : ℕ} (hn : n ≠ 4) :
    ¬ Nonempty (Fin n ≃ Fin 4) :=
  fun h => hn ((pole_fin_equiv_fin_four_iff n).mp h)

end QOU.QBeta
