import QOU.Information.SurrealBudgetGrade

/-!
# QOU.Information.PolyGrowthAlgebra — the budget grade is a bound-management algebra

The surreal ω-grade is *bound management*, not bookkeeping (owner directive):
the polynomial-budget grade must be **closed under the operations one performs
while bounding** — dominate, add overhead, multiply a dressing factor.  This
file makes that precise.

`SurrealBudgetGrade.PolyBounded` (`∃ c k, ∀ n, f n ≤ c·nᵏ`) is the right
*negation target* for the squeeze, but the bare `nᵏ` shape has an `n = 0`
artifact — `0ᵏ = 0` for `k ≥ 1`, so e.g. `n ↦ n + 5` is not `PolyBounded` — and
hence is **not closed under `+`**.  The constant-safe class

    PolyGrowth f  :=  ∃ c k, ∀ n, f n ≤ c · (n+1)ᵏ

is the genuine polynomial-growth *ideal*: it contains the constants and the
identity, and is closed under `+`, `×`, and monotone domination — the algebra
of bound management.  `PolyBounded ⊆ PolyGrowth` (a `PolyBounded` witness is a
`PolyGrowth` witness), so nothing about the squeeze is lost.

All sorry-free.  The one non-trivial bridge in the *other* direction —
`PolyGrowth ⟹ ¬ SuperPolynomial` (that polynomial growth genuinely undercuts
the super-polynomial grade) — needs the standard `(n+1)ᵏ ≤ 2ᵏ(nᵏ+1)` domination
with its `ℕ` `n=0` bookkeeping; it is left as a follow-up bean, not `sorry`'d
here (§Strict Lean Discipline item 13). Base ring not applicable (ℕ-valued).
-/

namespace QOU.Information

/-- **Polynomial-growth class (constant-safe).**  `f` is `O((n+1)ᵏ)` — the
    Landau polynomial-growth ideal, robust at `n = 0`.  This is the closed
    bound-management grade. -/
def PolyGrowth (f : ℕ → ℕ) : Prop := ∃ c k, ∀ n, f n ≤ c * (n + 1) ^ k

/-- **Constants have polynomial growth (sorry-free).** -/
theorem polyGrowth_const (a : ℕ) : PolyGrowth (fun _ => a) :=
  ⟨a, 0, fun n => by simp⟩

/-- **The identity has polynomial growth (sorry-free).** -/
theorem polyGrowth_id : PolyGrowth (fun n => n) :=
  ⟨1, 1, fun n => by simp⟩

/-- **`PolyBounded ⊆ PolyGrowth` (sorry-free).**  Every polynomially-bounded
    function has polynomial growth — the squeeze's negation target embeds in the
    closed algebra, so no separation content is lost by working here. -/
theorem PolyGrowth.of_polyBounded {f : ℕ → ℕ} (h : PolyBounded f) : PolyGrowth f := by
  obtain ⟨c, k, hb⟩ := h
  exact ⟨c, k, fun n => (hb n).trans (by gcongr; omega)⟩

/-- **Downward closed under domination (sorry-free).**  Bounding a smaller
    quantity by the same polynomial budget. -/
theorem PolyGrowth.mono {f g : ℕ → ℕ} (hf : PolyGrowth f)
    (hle : ∀ n, g n ≤ f n) : PolyGrowth g := by
  obtain ⟨c, k, hb⟩ := hf
  exact ⟨c, k, fun n => (hle n).trans (hb n)⟩

/-- **Closed under addition (sorry-free).**  Adding two polynomial-growth costs
    stays polynomial-growth — sum the constants, take the larger exponent. -/
theorem PolyGrowth.add {f g : ℕ → ℕ} (hf : PolyGrowth f) (hg : PolyGrowth g) :
    PolyGrowth (fun n => f n + g n) := by
  obtain ⟨c1, k1, h1⟩ := hf
  obtain ⟨c2, k2, h2⟩ := hg
  refine ⟨c1 + c2, max k1 k2, fun n => ?_⟩
  calc f n + g n
      ≤ c1 * (n + 1) ^ k1 + c2 * (n + 1) ^ k2 := Nat.add_le_add (h1 n) (h2 n)
    _ ≤ c1 * (n + 1) ^ (max k1 k2) + c2 * (n + 1) ^ (max k1 k2) := by gcongr <;> omega
    _ = (c1 + c2) * (n + 1) ^ (max k1 k2) := by ring

/-- **Closed under multiplication (sorry-free).**  Multiplying two
    polynomial-growth costs stays polynomial-growth — multiply the constants,
    add the exponents. -/
theorem PolyGrowth.mul {f g : ℕ → ℕ} (hf : PolyGrowth f) (hg : PolyGrowth g) :
    PolyGrowth (fun n => f n * g n) := by
  obtain ⟨c1, k1, h1⟩ := hf
  obtain ⟨c2, k2, h2⟩ := hg
  refine ⟨c1 * c2, k1 + k2, fun n => ?_⟩
  calc f n * g n
      ≤ (c1 * (n + 1) ^ k1) * (c2 * (n + 1) ^ k2) := Nat.mul_le_mul (h1 n) (h2 n)
    _ = (c1 * c2) * (n + 1) ^ (k1 + k2) := by rw [pow_add]; ring

end QOU.Information
