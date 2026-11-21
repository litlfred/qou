import QOU.BraidKnot.HabiroNewtonLadder

/-!
# Bar-parity invariant — the formalize-first filter on any μ-anchor correction

**The surviving μ–p route, gated by its invariant.** The μ–p tension attack
(bean `qou-ph2a`, `docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`)
found the naive mechanism refuted: the q-deformed projector-weight shift on the
`H_5` Markov trace (#2584) is not only 6–7 orders too large but **bar-mixed** —
its correction has a nonzero **bar-odd** part, and so fails the parity a genuine
figure-8 (`4₁`) correction must have. The one un-refuted route (the colored
Σ(2,3,5) WRT / Habiro q-series, s5-so3 keystone) must respect the same parity.

This module **states that parity invariant and proves its algebra**, so the
route is gated *before* any wide numerics (formalize-first, AGENTS.md
§"Formalize-first probe discipline"). The invariant is the bar-involution
`q ↦ q⁻¹`:

* **`BarEven f`** — `f(q⁻¹) = f(q)`: the parity the amphichiral figure-8 anchor
  has. Proved for the actual colored-Jones tower here (packaging the sorry-free
  `coloredJones41_bar_symmetric`), and for `[2]_q = q + q⁻¹`.
* **`BarOdd f`** — `f(q⁻¹) = −f(q)`: the parity `ℏ = q − q⁻¹` has.
* **Exclusion (the filter):** a function that is *both* bar-even and has a
  bar-odd part must have that part vanish (`barEven_barOdd_forces_zero`; over
  `CharZero`, forced to `0`). So a candidate μ-correction with a nonzero bar-odd
  component (the refuted projector shift) **cannot** be a bar-even figure-8
  correction. This is a **structural exclusion (scope-(b))** justified by the
  proved parity invariant — not a numerical near-miss.

Nothing here fits or uses `q₀` / the 210 ppb target; it is the parity algebra +
the anchor's proved bar-symmetry. Wiring a *derived* bar-even correction to
production remains gated on the open Σ(2,3,5) WRT evaluation (bean `s5bb`).

## Base ring (§7c)

Generic `{K : Type*} [Field K]` throughout (the bar-involution needs `q⁻¹`); no
`ℝ`, no ordering, no archimedean constructs. `CharZero` is assumed *only* for the
two lemmas that must divide by `2` (the odd-part-forced-zero corollary and the
even/odd reconstruction).

-- Ref: [leitner2026] docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md; docs/coordination/s5-so3-keystone.md; bean s5bb
-/

namespace QOU.BraidKnot.BarParityInvariant

open QOU.BraidKnot.HabiroNewtonLadder

variable {K : Type*} [Field K]

/-- The bar-conjugate of `f`: precompose with the bar-involution `q ↦ q⁻¹`. -/
def barConj (f : K → K) : K → K := fun q => f q⁻¹

/-- `f` is **bar-even** if invariant under `q ↦ q⁻¹` (on the punctured line). -/
def BarEven (f : K → K) : Prop := ∀ q : K, q ≠ 0 → f q⁻¹ = f q

/-- `f` is **bar-odd** if it negates under `q ↦ q⁻¹`. -/
def BarOdd (f : K → K) : Prop := ∀ q : K, q ≠ 0 → f q⁻¹ = -f q

/-! ## Closure algebra of the two parities -/

theorem barEven_const (c : K) : BarEven (fun _ => c) := fun _ _ => rfl

theorem barEven_add {f g : K → K} (hf : BarEven f) (hg : BarEven g) :
    BarEven (fun q => f q + g q) := fun q hq => by
  simp only [hf q hq, hg q hq]

theorem barEven_mul {f g : K → K} (hf : BarEven f) (hg : BarEven g) :
    BarEven (fun q => f q * g q) := fun q hq => by
  simp only [hf q hq, hg q hq]

theorem barOdd_add {f g : K → K} (hf : BarOdd f) (hg : BarOdd g) :
    BarOdd (fun q => f q + g q) := fun q hq => by
  simp only [hf q hq, hg q hq]; ring

theorem barOdd_neg {f : K → K} (hf : BarOdd f) : BarOdd (fun q => -f q) :=
  fun q hq => by simp only [hf q hq]

/-- Product of two **bar-odd** functions is **bar-even** (the two sign flips
cancel) — this is why `ℏ²`-order corrections can be bar-even. -/
theorem barOdd_mul_barOdd {f g : K → K} (hf : BarOdd f) (hg : BarOdd g) :
    BarEven (fun q => f q * g q) := fun q hq => by
  show f q⁻¹ * g q⁻¹ = f q * g q
  rw [hf q hq, hg q hq]; ring

/-- **bar-even × bar-odd = bar-odd** (a single uncancelled sign flip). -/
theorem barEven_mul_barOdd {f g : K → K} (hf : BarEven f) (hg : BarOdd g) :
    BarOdd (fun q => f q * g q) := fun q hq => by
  show f q⁻¹ * g q⁻¹ = -(f q * g q)
  rw [hf q hq, hg q hq]; ring

/-! ## The two canonical generators -/

/-- `[2]_q = q + q⁻¹` is **bar-even** (the balanced quantum integer). -/
theorem barEven_bracket2 : BarEven (fun q : K => q + q⁻¹) := fun q hq => by
  show q⁻¹ + q⁻¹⁻¹ = q + q⁻¹
  rw [inv_inv]; ring

/-- `ℏ = q − q⁻¹` is **bar-odd** (the unbalanced difference). -/
theorem barOdd_hbar : BarOdd (fun q : K => q - q⁻¹) := fun q hq => by
  show q⁻¹ - q⁻¹⁻¹ = -(q - q⁻¹)
  rw [inv_inv]; ring

/-! ## Power parity — the Δ_λ chirality sign IS the bar-involution grading

The Δ_λ closure target (bean `s5bb`, Option-E) is **mixed-sign**: the chirality
sign is `deltaSign λ = (-1)^(principal grading λ)`
(`QOU.BraidKnot.PrincipalGradingJetOrder.deltaSign`,
`QOU.BraidsAndKnots.PartitionOf5.deltaSign`). Since each principal-grading-`1`
generator is the bar-odd `ℏ = q − q⁻¹`, a degree-`d` monomial has bar-parity
`(-1)^d` — so the Δ_λ chirality sign and the μ-correction bar-even requirement
(#2584) are the **same `ℤ/2` bar-involution grading** on the shared s5-so3 `W_λ`
object. The two open routes are gated by one invariant.
-/

/-- A **bar-odd** function raised to the `n`-th power picks up `(-1)^n`. -/
theorem barOdd_pow {f : K → K} (hf : BarOdd f) (n : ℕ) (q : K) (hq : q ≠ 0) :
    (f q⁻¹) ^ n = (-1) ^ n * (f q) ^ n := by
  rw [hf q hq, neg_pow]

/-- **Even power of a bar-odd generator is bar-even** (`deltaSign = +1` at even
principal grading). -/
theorem barEven_barOdd_pow_even {f : K → K} (hf : BarOdd f) {n : ℕ} (hn : Even n) :
    BarEven (fun q => (f q) ^ n) := fun q hq => by
  show (f q⁻¹) ^ n = (f q) ^ n
  rw [barOdd_pow hf n q hq, hn.neg_one_pow, one_mul]

/-- **Odd power of a bar-odd generator is bar-odd** (`deltaSign = −1` at odd
principal grading). Together with the previous lemma this is exactly
`deltaSign = (-1)^(principal grading)`: the Δ_λ chirality sign is the
bar-involution parity of the principal-grading degree — the SAME `ℤ/2` grading
that forces the μ-correction bar-even. -/
theorem barOdd_barOdd_pow_odd {f : K → K} (hf : BarOdd f) {n : ℕ} (hn : Odd n) :
    BarOdd (fun q => (f q) ^ n) := fun q hq => by
  show (f q⁻¹) ^ n = -((f q) ^ n)
  rw [barOdd_pow hf n q hq, hn.neg_one_pow, neg_one_mul]

/-! ## The μ-anchor object is bar-even (reusing the proved figure-8 symmetry) -/

/-- **The figure-8 (`4₁`) colored-Jones tower is bar-even**, for every color
`N`.  This *packages* the sorry-free `coloredJones41_bar_symmetric`
(`QOU.BraidKnot.HabiroNewtonLadder`) into the `BarEven` predicate: the muon
anchor `m_μ = m_e·Vol(4₁)/ℏ_q²` sits on the amphichiral figure-8, whose knot
invariant is palindromic.  Any correction *factored through this tower* inherits
bar-evenness by the closure algebra above. -/
theorem barEven_coloredJones41 (N : ℕ) :
    BarEven (fun q : K => coloredJones41 q N) := fun _ hq =>
  coloredJones41_bar_symmetric hq N

/-! ## The exclusion filter — bar-even ∧ bar-odd part ⇒ that part vanishes -/

/-- **Common-parity collapse.**  A function that is *both* bar-even and bar-odd
satisfies `f q + f q = 0` everywhere on the punctured line.  Over any field: the
even law gives `f q⁻¹ = f q`, the odd law gives `f q⁻¹ = −f q`, so `f q = −f q`. -/
theorem barEven_barOdd_forces_two_zero {f : K → K}
    (he : BarEven f) (ho : BarOdd f) (q : K) (hq : q ≠ 0) :
    f q + f q = 0 := by
  have hh : f q = -f q := (he q hq).symm.trans (ho q hq)
  linear_combination hh

/-- **Exclusion (`CharZero`).**  Over a characteristic-zero field, a function that
is both bar-even and bar-odd is identically zero on `q ≠ 0`.  This is the filter:
the bar-odd part of a required-bar-even μ-correction must vanish, so the refuted
bar-mixed projector shift (#2584) is **structurally excluded** — not merely a
numerical near-miss. -/
theorem barEven_barOdd_forces_zero [CharZero K] {f : K → K}
    (he : BarEven f) (ho : BarOdd f) (q : K) (hq : q ≠ 0) : f q = 0 := by
  have h2 : (2 : K) * f q = 0 := by
    have := barEven_barOdd_forces_two_zero he ho q hq; linear_combination this
  rcases mul_eq_zero.mp h2 with h | h
  · exact absurd h two_ne_zero
  · exact h

/-! ## Even/odd decomposition (the bar-parity splitting) -/

/-- Bar-even part `(f q + f q⁻¹)/2`. -/
def barEvenPart (f : K → K) : K → K := fun q => (f q + f q⁻¹) / 2

/-- Bar-odd part `(f q − f q⁻¹)/2`. -/
def barOddPart (f : K → K) : K → K := fun q => (f q - f q⁻¹) / 2

theorem barEven_barEvenPart [CharZero K] (f : K → K) : BarEven (barEvenPart f) :=
  fun q hq => by simp only [barEvenPart, inv_inv]; ring

theorem barOdd_barOddPart [CharZero K] (f : K → K) : BarOdd (barOddPart f) :=
  fun q hq => by simp only [barOddPart, inv_inv]; ring

/-- **Reconstruction.**  `f = barEvenPart f + barOddPart f` on the punctured line.
So `BarEven f` is exactly `barOddPart f = 0`: the parity filter is the vanishing
of a well-defined odd component, not a soft numerical criterion. -/
theorem barEvenPart_add_barOddPart [CharZero K] (f : K → K) (q : K) :
    barEvenPart f q + barOddPart f q = f q := by
  simp only [barEvenPart, barOddPart]; ring

end QOU.BraidKnot.BarParityInvariant
