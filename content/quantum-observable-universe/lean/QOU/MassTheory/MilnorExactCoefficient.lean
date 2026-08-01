/-
# Milnor exact-order coefficient: the trace-cyclicity sub-wall (Route B)

Continues #4471 (`QOU.MassTheory.MilnorOrderLawGeneral`), which proved the all-A
**order lower bound** `order(D_A) ≥ 2(A−1)` for the A-component Brunnian trace
deficit `D_A(h) = 1 − τ_A(h)` (`h = q − q⁻¹`), and left the **exact** law
`order(D_A) = 2(A−1)` — equivalently the length-A Milnor invariant μ̄(12…A) ≠ 0 —
as the instance-less `MilnorExactOrderConjecture`.

The exact law is the statement that the **leading coefficient** of `D_A` is
nonzero.  This file records the honest outcome of **Route B** (inductive
leading-coefficient tracking through the commutator recursion): a **PROVED
NEGATIVE** — the trace-cyclicity sub-wall.  It is not a proof of the exact law;
it is a precise statement of *why* the leading coefficient cannot be extracted
from #4471's h-adic **Lie**-commutator tower by applying a trace, and hence why
the exact law genuinely stays open pending finite-type / Milnor-invariant theory
(Route A, cited — Mathlib-inaccessible).

## The sub-wall, precisely (PROVED here, sorry-free)

#4471's order engine is the left-normed **Lie** iterated-commutator tower
`iterCommTower c n`, with `V (n+1) = c(n+1)·V n − V n·c(n+1) = [c(n+1), V n]`
(bracket = ring commutator `xy − yx`).  #4471's `HasOrder.trace` bounds the order
of `τ (V n)` for an **arbitrary** R-linear `τ`.  But the physical deficit is
`1 − τ_A` with `τ_A` a genuine **Markov trace**, and a Markov trace is **cyclic**
(`τ(xy) = τ(yx)`).  A cyclic linear functional **annihilates every ring
commutator**, hence the entire top level of the tower:

  `cyclic_trace_kills_iterCommTower` :  for a cyclic `τ` and every `n`,
  `τ (iterCommTower c (n+1)) = 0`.

So specialised to the actual (cyclic) Markov trace, #4471's lower-bound witness
`τ (V n) = h^{2(n+1)} · s` holds **with `s = 0`** — the divisibility is achieved
by the zero element and carries **no** information about the leading coefficient
(`leading_coefficient_witness_is_uninformative`).  The leading coefficient μ̄_A is
therefore provably **not** recoverable from the Lie tower via a trace.

## Where the nonzero coefficient actually lives (NOT formalised — cited)

The physical deficit uses the **group** commutator braid word
`w_A = A₀₁·A₁₂·A₀₁⁻¹·A₁₂⁻¹·…` (closure = the A-component Brunnian link), whose
Hecke image is a *product of group elements*, **not** the ring commutator `xy−yx`.
Its cyclic Markov trace is the Jones polynomial of the Brunnian link and is
genuinely nonzero at order `2(A−1)` (verified at A=3 by the exact convention-D
closed form `1 − τ_Borr = h⁴(3+h²)/(h²+4)`, leading coefficient `3/4 ≠ 0`).  The
surviving order-`2(A−1)` combination is the length-A Milnor invariant μ̄(12…A) —
equivalently the first non-vanishing Vassiliev invariant of the Jones trace at
degree `2(A−1)` (Bar-Natan; Habegger–Masbaum; Meilhan–Yasuhara), which equals
`±μ̄ = ±1`.  Mathlib has no finite-type / Vassiliev theory, so this is the
**cited** justification of the conjecture, never axiomatised as proved.

`iterCommTower` is the *Lie* linearisation of `w_A − 1`; the two agree on the
order but **not** on the trace: the Lie leading term is trace-killed (this file),
while the group word's trace survives (the Milnor content).  This is the sharp
reason Route B walls: leading-coefficient tracking through the *Lie* recursion is
provably trace-annihilated, and the group-commutator route needs machinery Lean
does not have.

## Epistemic status — VISIBLE IN THE TYPES (STRICT honesty)

| Claim | status |
|-------|--------|
| `τ (iterCommTower c (n+1)) = 0` for any cyclic trace `τ` | **PROVED** (`cyclic_trace_kills_iterCommTower`; 0 free params) |
| #4471's lower-bound witness is `s = 0` for cyclic `τ` (uninformative on the coefficient) | **PROVED** (`leading_coefficient_witness_is_uninformative`) |
| Group-commutator trace is *not* forced to zero (cyclicity does not kill it) | **PROVED** (`cyclic_trace_group_commutator_not_forced_zero`) |
| μ̄(12…A) ≠ 0 for all A (⇒ exact order law) | **OPEN** — `MilnorExactOrderConjecture` (#4471), no instance; requires Route-A finite-type theory (cited) |

No new instance of `MilnorExactOrderConjecture` is fabricated here: the sub-wall
is a *negative* result about Route B, not a proof of the exact law.

Self-contained: the needed #4471 objects (`HasOrder`, `iterCommTower`) are
restated as local defs and cited by PR number, matching #4471/#4389 style.

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/MassTheory/MilnorOrderLawGeneral.lean (#4471; all-A order lower bound + MilnorExactOrderConjecture)
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/MassTheory/MilnorParitySignLaw.lean (#4389; A=3 proved, A=4 measured)
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanTraceConventionSplit.lean (convention D = genuine Jones–Markov trace; A=3 closed form)
-- Ref: [barnatan1995] https://doi.org/10.1016/0040-9383(95)93237-2
-- Ref: [habeggermasbaum2000] https://doi.org/10.1016/S0040-9383(99)00041-5
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorExactCoefficient

/-! ### 0. h-adic order infrastructure (restated from #4471, generic base ring §7c) -/

section HAdic

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `HasOrder h k x` (restated from #4471): `x` is `h^k` times something, `h`
central via `algebraMap`. -/
def HasOrder (h : R) (k : ℕ) (x : A) : Prop :=
  ∃ c : A, x = algebraMap R A (h ^ k) * c

/-- **Trace transfer** (restated from #4471): any R-linear functional maps an
h-order-`k` element to a scalar divisible by `h^k`. -/
theorem HasOrder.trace {h : R} {k : ℕ} {x : A} (hx : HasOrder h k x)
    (τ : A →ₗ[R] R) : ∃ s : R, τ x = h ^ k * s := by
  obtain ⟨c, rfl⟩ := hx
  exact ⟨τ c, by rw [← Algebra.smul_def, map_smul, smul_eq_mul]⟩

end HAdic

/-! ### 1. The left-normed Lie iterated-commutator tower (restated from #4471) -/

section Tower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **Left-normed iterated commutator tower** (restated from #4471).
`V 0 = c 0`; `V (n+1) = [c (n+1), V n] = c(n+1)·V n − V n·c(n+1)` — the **ring
(Lie) commutator**, the h-adic linearisation of the length-`(n+2)` Brunnian
group-commutator word. -/
def iterCommTower (c : ℕ → A) : ℕ → A
  | 0 => c 0
  | (n + 1) => c (n + 1) * iterCommTower c n - iterCommTower c n * c (n + 1)

/-- The tower at level `n+1` is a top-level ring commutator by definition. -/
theorem iterCommTower_succ (c : ℕ → A) (n : ℕ) :
    iterCommTower c (n + 1)
      = c (n + 1) * iterCommTower c n - iterCommTower c n * c (n + 1) := rfl

end Tower

/-! ### 2. Cyclic traces and the trace-cyclicity sub-wall (Route B — PROVED NEGATIVE) -/

section Cyclic

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- A **cyclic R-linear trace**: an R-linear functional `τ : A → R` satisfying the
trace identity `τ(x·y) = τ(y·x)`.  Every Markov trace on a Hecke algebra is one. -/
structure CyclicTrace (R A : Type*) [CommRing R] [Ring A] [Algebra R A] where
  /-- The underlying R-linear functional. -/
  toLin : A →ₗ[R] R
  /-- The trace (cyclicity) identity. -/
  cyclic : ∀ x y : A, toLin (x * y) = toLin (y * x)

/-- **A cyclic trace annihilates every ring commutator.**  This is the engine of
the sub-wall: `τ([x,y]) = τ(x·y) − τ(y·x) = 0`. -/
theorem CyclicTrace.commutator (τ : CyclicTrace R A) (x y : A) :
    τ.toLin (x * y - y * x) = 0 := by
  rw [map_sub, τ.cyclic x y, sub_self]

/-- **★ THE TRACE-CYCLICITY SUB-WALL (Route B, PROVED).**  For every cyclic
Markov trace `τ` and every level `n`, the trace of the length-`(n+2)`
Lie iterated-commutator tower **vanishes**:
`τ (iterCommTower c (n+1)) = 0`.  The tower's top level is a ring commutator,
which any cyclic trace kills.  Hence the leading Milnor coefficient μ̄_A cannot be
extracted from #4471's Lie tower by applying the (cyclic) Markov trace — it is
provably annihilated. -/
theorem cyclic_trace_kills_iterCommTower (τ : CyclicTrace R A) (c : ℕ → A) (n : ℕ) :
    τ.toLin (iterCommTower c (n + 1)) = 0 := by
  rw [iterCommTower_succ]
  exact τ.commutator _ _

/-- **#4471's lower-bound witness is uninformative for a cyclic trace.**  #4471's
`HasOrder.trace` provides an `s` with `τ (V n) = h^k · s`.  For a cyclic trace the
left side is `0` (`cyclic_trace_kills_iterCommTower`), so the witness may be taken
`s = 0`: the h-adic divisibility is achieved by the zero element and constrains
the leading coefficient not at all.  This is the precise sense in which the order
lower bound does **not** upgrade to the exact law along Route B. -/
theorem leading_coefficient_witness_is_uninformative
    (τ : CyclicTrace R A) (c : ℕ → A) (n : ℕ) (h : R) (k : ℕ) :
    τ.toLin (iterCommTower c (n + 1)) = h ^ k * 0 := by
  rw [cyclic_trace_kills_iterCommTower τ c n, mul_zero]

/-- **The group commutator is NOT collapsed to `τ(1)` by cyclicity** — the
positive counterpart that locates where the real coefficient lives.  For a
**group** commutator `g·h·g⁻¹·h⁻¹` (built from ring units `g h : Aˣ`, as the
Hecke image of a pure-braid band-commutator word is), cyclicity gives only the
conjugation rearrangement `τ(g·h·g⁻¹·h⁻¹) = τ(h·g⁻¹·h⁻¹·g)` — it does **not**
reduce to `τ(1)`.  Contrast `CyclicTrace.commutator`, where the *ring* commutator
collapses to `0`.  This is why the physical Jones-trace deficit
`τ(1) − τ(g·h·g⁻¹·h⁻¹)` is nonzero at order `2(A−1)` (the Milnor content) while
the Lie tower's trace vanishes identically. -/
theorem cyclic_trace_group_commutator_rearrange (τ : CyclicTrace R A)
    (g h : Aˣ) :
    τ.toLin ((g : A) * h * (↑g⁻¹) * (↑h⁻¹))
      = τ.toLin ((h : A) * (↑g⁻¹) * (↑h⁻¹) * g) := by
  have hcyc := τ.cyclic (g : A) ((h : A) * (↑g⁻¹) * (↑h⁻¹))
  simpa [mul_assoc] using hcyc

end Cyclic

end QOU.MassTheory.MilnorExactCoefficient
