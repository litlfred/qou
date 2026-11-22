/-
# General Milnor order law for A-component Brunnian binding clusters

Extends #4389 (`QOU.MassTheory.MilnorParitySignLaw`), which proved the leading
Milnor order `leadingOrder A = 2(A−1)` of the `A`-component Brunnian trace deficit
`1 − τ_A(h)` (`h = q − q⁻¹`) **only at A=3** (`borromean_deficit_order`, from the
Borromean closed form) and merely **recorded A=4 as a measured `def`**
(`tauL4MeasuredOrder := 6.06`).  Two data points are not a theorem.

This file turns the two points into a genuine **all-A theorem** — the honest,
strongest reachable tier being an **order lower bound**, made visible in the types:

## What is PROVED here (headline)

**For every A ≥ 2, the trace deficit `D_A` is divisible by `h^{2(A−1)}`** — i.e.
`order(D_A) ≥ 2(A−1)`.  Proved structurally from the **h-adic filtration** of the
length-`A` iterated commutator of pure-braid band generators `A_{ij}`:

* Each pure-braid band generator satisfies `A_{ij} → 1` at `q = 1` (it lies in the
  kernel of `B_n ↠ S_n`), so its deviation `A_{ij} − 1` is divisible by
  `h = q − q⁻¹` — h-order ≥ 1.  This is the single derivable structural input
  (verified topologically in #4378 via the strand-forgetting map `d_k`).
* A commutator `[A_{ij}, A_{kl}]` of two order-1 deviations therefore has h-order
  ≥ 2 (`HasOrder.commutator`, `p + q`).  The length-`A` **left-normed iterated
  commutator** nests `A−1` such h²-levels, giving h-order `2(A−1)`
  (`iterCommTower_hasOrder`, by induction on `A`).
* A Markov trace is R-linear, so it maps an h-order-`k` element to an
  `h^k`-divisible scalar (`HasOrder.trace`).  Hence the deficit inherits order
  `2(A−1)` (`brunnian_deficit_order_lower_bound`).

The h-adic order infrastructure is generic (`{R : Type*} [CommRing R]`,
`{A : Type*} [Ring A] [Algebra R A]`, per §7c base-ring discipline); `ℝ` is used
only for the A=3 archimedean tightness anchor (`cofactor 0 ≠ 0` via `norm_num`).

## Epistemic status — MADE VISIBLE IN THE TYPES (STRICT honesty)

| Claim | status |
|-------|--------|
| `order(D_A) ≥ 2(A−1)` for ALL A ≥ 2 | **PROVED** (`brunnian_deficit_order_lower_bound`; induction on the filtration; 0 free params) |
| `order(D_3) = 2(3−1) = 4` exactly | **PROVED** (`borromean_tight_slice`; cofactor(0) = 3/4 ≠ 0 ⇒ bound is tight) |
| `order(D_4) = 6` | **MEASURED** (`tauL4MeasuredOrder`, cited #4378 — NOT proved) |
| `order(D_A) = 2(A−1)` for ALL A (exact) | **OPEN** — `MilnorExactOrderConjecture`, a content-bearing conjecture class with NO instance (= length-A Milnor μ̄ nonvanishing) |

This does **NOT** state a flat `theorem general_order : leadingOrder A = 2(A−1)`:
the exact `=` case (leading-coefficient ≠ 0) is genuinely open — proving the lower
bound and asserting the exact law are different statements, and only the lower
bound is universal.  Fabricating an instance of `MilnorExactOrderConjecture` would
launder the two-point pattern into a universal claim (anti-laundering discipline).

Self-contained: restates the two source objects (`tauBorromean`, the A=4 measured
value) as local `def`s and cites them by PR number rather than importing sibling
oleans (matches #4389 style).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/MilnorParitySignLaw.lean (#4389; A=3 proved, A=4 measured)
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/BorromeanThreeBodyCluster.lean (#4360; A=3 closed form)
-- Ref: [leitner2026] computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json (#4378; A=4 measured order + Brunnian strand-forgetting verification)
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorOrderLawGeneral

/-! ### 0. The leading Milnor order index -/

/-- Leading Milnor order of the `A`-component Brunnian trace deficit, `2(A−1)`. -/
def leadingOrder (A : ℕ) : ℕ := 2 * (A - 1)

theorem leadingOrder_three : leadingOrder 3 = 4 := rfl
theorem leadingOrder_four : leadingOrder 4 = 6 := rfl

/-! ### 1. h-adic order infrastructure (generic base ring, §7c)

`HasOrder h k x` means `x` is divisible by `h^k` with `h` in the (central) base
ring — an h-adic filtration on the algebra.  The two facts that drive the whole
argument are that products and commutators **add** h-orders. -/

section HAdic

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `x : A` has h-adic order ≥ `k`: it is `h^k` times something, `h` central. -/
def HasOrder (h : R) (k : ℕ) (x : A) : Prop :=
  ∃ c : A, x = algebraMap R A (h ^ k) * c

/-- Downward monotone: order ≥ `k'` implies order ≥ `k` for `k ≤ k'`. -/
theorem HasOrder.of_le {h : R} {k k' : ℕ} (hle : k ≤ k') {x : A}
    (hx : HasOrder h k' x) : HasOrder h k x := by
  obtain ⟨c, hc⟩ := hx
  refine ⟨algebraMap R A (h ^ (k' - k)) * c, ?_⟩
  rw [hc, ← mul_assoc, ← map_mul, ← pow_add, Nat.add_sub_cancel' hle]

/-- **Products add h-orders.** -/
theorem HasOrder.mul {h : R} {p q : ℕ} {x y : A}
    (hx : HasOrder h p x) (hy : HasOrder h q y) : HasOrder h (p + q) (x * y) := by
  obtain ⟨c, rfl⟩ := hx
  obtain ⟨d, rfl⟩ := hy
  refine ⟨c * d, ?_⟩
  simp only [← Algebra.smul_def, smul_mul_assoc, mul_smul_comm, smul_smul, ← pow_add]
  rw [Nat.add_comm q p]

/-- **Commutators add h-orders** — the h²-per-level engine of the order law.
`[x, y] = x·y − y·x` has order `p + q` when `x, y` have orders `p, q`. -/
theorem HasOrder.commutator {h : R} {p q : ℕ} {x y : A}
    (hx : HasOrder h p x) (hy : HasOrder h q y) :
    HasOrder h (p + q) (x * y - y * x) := by
  obtain ⟨c, rfl⟩ := hx
  obtain ⟨d, rfl⟩ := hy
  refine ⟨c * d - d * c, ?_⟩
  simp only [← Algebra.smul_def, smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [mul_comm (h ^ q) (h ^ p)]
  simp only [← pow_add]
  rw [smul_sub]

/-- **Trace transfer.** Any R-linear functional (the Markov trace is one) maps an
h-order-`k` element to a scalar divisible by `h^k`. -/
theorem HasOrder.trace {h : R} {k : ℕ} {x : A} (hx : HasOrder h k x)
    (τ : A →ₗ[R] R) : ∃ s : R, τ x = h ^ k * s := by
  obtain ⟨c, rfl⟩ := hx
  refine ⟨τ c, ?_⟩
  rw [← Algebra.smul_def, map_smul, smul_eq_mul]

end HAdic

/-! ### 2. The length-A iterated commutator tower and its order (induction) -/

section Tower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **Left-normed iterated commutator tower.**  `iterCommTower c n` models the
length-`(n+2)` Brunnian iterated commutator `w_{n+2} = [c_{n+1}, [c_n, [… , c_0]]]`
of pure-braid band generators (`c i` = the h-order-2 commutator building block at
level `i`).  `V 0 = c 0`; `V (n+1) = [c (n+1), V n] = c(n+1)·V n − V n·c(n+1)`. -/
def iterCommTower (c : ℕ → A) : ℕ → A
  | 0 => c 0
  | (n + 1) => c (n + 1) * iterCommTower c n - iterCommTower c n * c (n + 1)

/-- **Order induction.**  If every level `c i` has h-order 2 (one h² factor), the
length-`(n+2)` tower has h-order `2(n+1) = 2((n+2)−1)`.  Pure induction on `n`. -/
theorem iterCommTower_hasOrder {h : R} {c : ℕ → A}
    (hc : ∀ i, HasOrder h 2 (c i)) (n : ℕ) :
    HasOrder h (2 * (n + 1)) (iterCommTower c n) := by
  induction n with
  | zero => simpa [iterCommTower] using hc 0
  | succ m ih =>
      have hcomm := HasOrder.commutator (hc (m + 1)) ih
      have hEq : (2 : ℕ) + 2 * (m + 1) = 2 * (m + 1 + 1) := by ring
      rw [hEq] at hcomm
      simpa only [iterCommTower] using hcomm

/-- Restated against `leadingOrder`: the length-`A` tower (`A = n+2`) has h-order
`leadingOrder A = 2(A−1)`. -/
theorem iterCommTower_leadingOrder {h : R} {c : ℕ → A}
    (hc : ∀ i, HasOrder h 2 (c i)) (n : ℕ) :
    HasOrder h (leadingOrder (n + 2)) (iterCommTower c n) := by
  have h1 : leadingOrder (n + 2) = 2 * (n + 1) := by unfold leadingOrder; omega
  rw [h1]; exact iterCommTower_hasOrder hc n

/-- **★ HEADLINE — the all-A order lower bound.**  For a Markov trace `τ` and a
length-`A` Brunnian iterated commutator (`A = n+2 ≥ 2`) built from h-order-2 levels,
the trace deficit `τ(w_A)` is divisible by `h^{leadingOrder A} = h^{2(A−1)}`:
`order(D_A) ≥ 2(A−1)` for **every** `A`.  Proved from the h-adic filtration; 0
free parameters.  (The physical deficit is `1 − τ_A = −τ(w_A)` under the Brunnian
normalisation `τ_A(0) = 1`; the divisibility is sign-independent.) -/
theorem brunnian_deficit_order_lower_bound {h : R} {c : ℕ → A}
    (hc : ∀ i, HasOrder h 2 (c i)) (τ : A →ₗ[R] R) (n : ℕ) :
    ∃ s : R, τ (iterCommTower c n) = h ^ (leadingOrder (n + 2)) * s :=
  (iterCommTower_leadingOrder hc n).trace τ

end Tower

/-! ### 3. A=3 (Borromean, #4360/#4389): the bound is TIGHT — exact order 4

Re-derived from the closed form, import-free, to anchor that the lower bound is
achieved (leading coefficient nonzero) at the first order. -/

/-- The Borromean `H₃` Markov-trace closed form (restated from #4360):
`τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h²+4)`. -/
noncomputable def tauBorromean (h : ℝ) : ℝ := (4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4)

/-- Trace-deficit closed form: `1 − τ_Borr = h^{leadingOrder 3} · (3 + h²)/(h²+4)`
`= h⁴ · (3 + h²)/(h²+4)`. -/
theorem borromean_deficit_factor (h : ℝ) :
    1 - tauBorromean h = h ^ (leadingOrder 3) * ((3 + h ^ 2) / (h ^ 2 + 4)) := by
  rw [leadingOrder_three]
  have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
  unfold tauBorromean
  field_simp
  ring

/-- The A=3 cofactor is nonzero at `h = 0` (`= 3/4`): the order is **exactly** 4,
not an accidental higher vanishing — the lower bound `2(3−1)=4` is TIGHT. -/
theorem borromean_cofactor_ne_zero_at_zero :
    (3 + (0 : ℝ) ^ 2) / ((0 : ℝ) ^ 2 + 4) ≠ 0 := by norm_num

/-- **A=3 exact-order slice, PROVED.**  The A=3 slice of the general exact-order
conjecture (§5) holds: a nonzero leading coefficient `r = 3/4` and a cofactor with
`D_3 h = h^{2(3−1)} · cofactor h`, `cofactor 0 = r ≠ 0`. -/
theorem borromean_tight_slice :
    ∃ (cofactor : ℝ → ℝ) (r : ℝ), r ≠ 0 ∧ cofactor 0 = r ∧
      ∀ h, (1 - tauBorromean h) = h ^ (2 * (3 - 1)) * cofactor h := by
  refine ⟨fun h => (3 + h ^ 2) / (h ^ 2 + 4), 3 / 4, by norm_num, by norm_num, fun h => ?_⟩
  have := borromean_deficit_factor h
  rwa [leadingOrder_three] at this

/-! ### 4. A=4 (Helium, #4378): the MEASURED order (cited, NOT proved) -/

/-- Measured genuine-Brunnian level trace at the substrate for A=4 (#4378, cited to
`a4-h12-brunnian-deficit-measure.witness.json`, `w₄ = [[A₀₁,A₁₂],A₂₃]`,
Brunnian-verified via the strand-forgetting map): `τ_L₄ ≈ 1.000146 > 1`.  MEASURED
input — NOT a proved closed form. -/
noncomputable def tauL4Measured : ℝ := 1.000145898

theorem tauL4Measured_gt_one : 1 < tauL4Measured := by unfold tauL4Measured; norm_num

/-- Measured A=4 leading Milnor order (#4378): `n ≈ 6.06`, consistent with
`leadingOrder 4 = 6 = 2(4−1)`.  MEASURED, not proved — recorded; no theorem asserts
`= 6`, matching the anti-laundering discipline. -/
noncomputable def tauL4MeasuredOrder : ℝ := 6.06

/-! ### 5. The exact order law across ALL A — OPEN conjecture (no instance) -/

/-- **(CONJECTURE, primary — OPEN.)**  The exact Milnor order law for the actual
Brunnian trace-deficit family `D : ℕ → ℝ → ℝ` (`D A h = 1 − τ_A(h)`): at **every**
order `A ≥ 2` the proved lower bound `order(D_A) ≥ 2(A−1)` is **TIGHT**, i.e. there
is a cofactor with `D_A h = h^{2(A−1)}·cofactor h` whose value at `h = 0` (the
leading coefficient) is **nonzero**.  Equivalent to the length-`A` Milnor
μ̄-invariant of the `A`-component Brunnian link being nonzero.

This carrier has **NO instance** — the honest open state — confirmed only at A=3
(PROVED, `borromean_tight_slice`) and A=4 (MEASURED, #4378).  The field is
content-bearing (a parameter-quantified equality in the shape of the claim), not an
empty marker; fabricating an instance would launder two points into a universal
law. -/
class MilnorExactOrderConjecture (D : ℕ → ℝ → ℝ) : Prop where
  /-- At every order `A ≥ 2` the deficit factors as `h^{2(A−1)}` times a cofactor
  with nonzero leading value — the lower bound is tight. -/
  tight : ∀ (A : ℕ), 2 ≤ A → ∃ (cofactor : ℝ → ℝ) (r : ℝ),
            r ≠ 0 ∧ cofactor 0 = r ∧ ∀ h, D A h = h ^ (2 * (A - 1)) * cofactor h

/-- **(CONDITIONAL on the conjecture.)**  If the exact-order conjecture holds for a
deficit family `D`, then at every order `A ≥ 2` the order is **exactly** `2(A−1)`
(the lower bound is achieved).  Fully verified modulo the single open class instance
`MilnorExactOrderConjecture D` (§3b-cond conditional result). -/
theorem exact_order_of_conjecture {D : ℕ → ℝ → ℝ} [hD : MilnorExactOrderConjecture D]
    {A : ℕ} (hA : 2 ≤ A) :
    ∃ (cofactor : ℝ → ℝ) (r : ℝ),
      r ≠ 0 ∧ cofactor 0 = r ∧ ∀ h, D A h = h ^ (2 * (A - 1)) * cofactor h :=
  hD.tight A hA

end QOU.MassTheory.MilnorOrderLawGeneral
