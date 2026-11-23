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

All sorry-free.  The bridge in the *other* direction —
`not_superPolynomial_of_polyGrowth : PolyGrowth ⟹ ¬ SuperPolynomial` (polynomial
growth genuinely undercuts the super-polynomial grade) — is proved below via the
`(n+1)ᵏ ≤ (2n)ᵏ = 2ᵏnᵏ` domination for `n ≥ 1`.  This is exactly the squeeze the
grade wants: nothing polynomial-growth is super-polynomial.  It works only
because `SuperPolynomial`'s witness is guarded `n ≥ 1` — the earlier unguarded
definition was satisfied by the plain polynomial `(n+1)²` via the `n = 0` escape
(`c·0ᵏ = 0 < f 0`), confirmed in Lean; repairing that (bean `qou-qgyw`) is what
made this direction true.  Base ring not applicable (ℕ-valued).
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
theorem of_polyBounded {f : ℕ → ℕ} (h : PolyBounded f) : PolyGrowth f := by
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
theorem add {f g : ℕ → ℕ} (hf : PolyGrowth f) (hg : PolyGrowth g) :
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
theorem mul {f g : ℕ → ℕ} (hf : PolyGrowth f) (hg : PolyGrowth g) :
    PolyGrowth (fun n => f n * g n) := by
  obtain ⟨c1, k1, h1⟩ := hf
  obtain ⟨c2, k2, h2⟩ := hg
  refine ⟨c1 * c2, k1 + k2, fun n => ?_⟩
  calc f n * g n
      ≤ (c1 * (n + 1) ^ k1) * (c2 * (n + 1) ^ k2) := Nat.mul_le_mul (h1 n) (h2 n)
    _ = (c1 * c2) * (n + 1) ^ (k1 + k2) := by rw [pow_add]; ring

/-! ## The reverse squeeze: polynomial growth is never super-polynomial -/

/-- **`PolyGrowth ⟹ ¬ SuperPolynomial` (sorry-free).**  Polynomial growth
    strictly undercuts the super-polynomial grade — the reverse of the
    `PolyBounded`-side squeeze, on the constant-safe class.  Given `f ≤ c·(n+1)ᵏ`
    and a super-polynomial witness `n ≥ 1` for the scaled budget `(c·2ᵏ, k)`, the
    domination `(n+1)ᵏ ≤ (2n)ᵏ = 2ᵏnᵏ` (valid exactly because `n ≥ 1`) forces
    `f n ≤ c·2ᵏ·nᵏ`, contradicting `c·2ᵏ·nᵏ < f n`.  The `n ≥ 1` guard on
    `SuperPolynomial` is what closes the `n = 0` escape that made this false
    before (bean `qou-qgyw`). -/
theorem not_superPolynomial_of_polyGrowth {f : ℕ → ℕ} (h : PolyGrowth f) :
    ¬ SuperPolynomial f := by
  obtain ⟨c, k, hb⟩ := h
  intro hs
  obtain ⟨n, hn1, hn2⟩ := hs (c * 2 ^ k) k
  have hdom : (n + 1) ^ k ≤ 2 ^ k * n ^ k := by
    calc (n + 1) ^ k ≤ (2 * n) ^ k := Nat.pow_le_pow_left (by omega) k
      _ = 2 ^ k * n ^ k := by rw [mul_pow]
  have hchain : f n ≤ c * 2 ^ k * n ^ k := by
    calc f n ≤ c * (n + 1) ^ k := hb n
      _ ≤ c * (2 ^ k * n ^ k) := by gcongr
      _ = c * 2 ^ k * n ^ k := by ring
  exact absurd hn2 (not_lt.mpr hchain)

/-- **Dually (sorry-free): a super-polynomial function has no polynomial
    growth.** -/
theorem not_polyGrowth_of_superPolynomial {f : ℕ → ℕ} (h : SuperPolynomial f) :
    ¬ PolyGrowth f := fun hg => not_superPolynomial_of_polyGrowth hg h

/-- **Every monomial `n ↦ n^d` has polynomial growth (`bean qou-151z`).** -/
theorem polyGrowth_pow (d : ℕ) : PolyGrowth (fun n => n ^ d) := by
  refine ⟨1, d, fun n => ?_⟩
  rw [one_mul]
  exact Nat.pow_le_pow_left (Nat.le_succ n) d

/-- **Every polynomially-bounded function is not super-polynomial (`bean qou-151z`).** -/
theorem not_superPolynomial_of_polyBounded {f : ℕ → ℕ} (h : PolyBounded f) :
    ¬ SuperPolynomial f :=
  not_superPolynomial_of_polyGrowth (of_polyBounded h)

/-! ## Composition, and the exact duality (bean `qou-034l`)

The bean asks for the grade algebra under `+`, `·` **and `∘`**. `+` and `·` are
`add` / `mul` above. Composition closes the budget side: a polynomial-growth
cost evaluated at a polynomial-growth size is polynomial-growth. The
super-polynomial side is *not* closed under precomposition in general, and
`superPolynomial_not_stable_under_precomp` records the obstruction, so the
"stable under `∘`" reading of the bean title holds for the budget grade only. -/

/-- **Closed under composition (sorry-free).**  `f (g n) ≤ c·(g n + 1)ᵏ
    ≤ c·((c'+1)(n+1)^{k'})ᵏ`. -/
theorem PolyGrowth.comp {f g : ℕ → ℕ} (hf : PolyGrowth f) (hg : PolyGrowth g) :
    PolyGrowth (fun n => f (g n)) := by
  obtain ⟨c, k, hfb⟩ := hf
  obtain ⟨c', k', hgb⟩ := hg
  refine ⟨c * (c' + 1) ^ k, k' * k, fun n => ?_⟩
  have h1 : g n + 1 ≤ (c' + 1) * (n + 1) ^ k' := by
    have hp : 1 ≤ (n + 1) ^ k' := Nat.one_le_pow _ _ (by omega)
    nlinarith [hgb n]
  calc f (g n) ≤ c * (g n + 1) ^ k := hfb (g n)
    _ ≤ c * ((c' + 1) * (n + 1) ^ k') ^ k := by gcongr
    _ = c * (c' + 1) ^ k * (n + 1) ^ (k' * k) := by rw [mul_pow, ← pow_mul]; ring

/-- **Super-polynomial growth is not stable under precomposition (sorry-free).**
    `2ⁿ` is super-polynomial, the constant size map `n ↦ 0` has polynomial
    growth, and the composite is the constant `1`. -/
theorem superPolynomial_not_stable_under_precomp :
    ∃ f g : ℕ → ℕ, SuperPolynomial f ∧ PolyGrowth g ∧
      ¬ SuperPolynomial (fun n => f (g n)) :=
  ⟨fun n => 2 ^ n, fun _ => 0, superPoly_two_pow, polyGrowth_const 0,
    not_superPolynomial_of_polyGrowth (by simpa using polyGrowth_const 1)⟩

/-- **Exact De Morgan duality (sorry-free).**  `PolyGrowth` is precisely the
    negation of `SuperPolynomial`. (`PolyBounded` is not: `n ↦ n + 1` is neither
    `PolyBounded` nor super-polynomial, the `n = 0` artifact noted in the header.) -/
theorem polyGrowth_iff_not_superPolynomial {f : ℕ → ℕ} :
    PolyGrowth f ↔ ¬ SuperPolynomial f := by
  refine ⟨not_superPolynomial_of_polyGrowth, fun h => ?_⟩
  simp only [SuperPolynomial, not_forall, not_exists, not_and, not_lt] at h
  obtain ⟨c, k, hb⟩ := h
  refine ⟨c + f 0, k, fun n => ?_⟩
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · calc f n ≤ c * n ^ k := hb n hn
      _ ≤ (c + f 0) * (n + 1) ^ k := by gcongr <;> omega

end QOU.Information
