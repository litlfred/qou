import Mathlib.Data.Matrix.Basis
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-
# The length-A Milnor/Magnus coefficient is nonzero (faithful nilpotent realization)

Continues #4471 (`QOU.MassTheory.MilnorOrderLawGeneral`, all-A order lower bound
`order(D_A) ≥ 2(A−1)`) and #4480 (`QOU.MassTheory.MilnorExactCoefficient`,
Route-B **proved negative**: a cyclic Markov trace annihilates the Lie
iterated-commutator tower, so the leading coefficient is NOT extractable from
the Lie tower via a trace).

This file records the **positive** counterpart to the Route-B wall, and closes
the honest sub-target *"the length-A Milnor coefficient is nonzero"* at the
level the finite-type theory actually supplies it — the **Magnus coefficient**,
NOT the cyclic trace.

## What is proved here (sorry-free, 0 free parameters)

The #4471 left-normed **Lie** iterated-commutator tower `iterCommTower c n`
(`V₀ = c₀`, `V_{n+1} = [c_{n+1}, V_n] = c_{n+1}·V_n − V_n·c_{n+1}`) is evaluated
on the **Magnus generators** — the elementary matrices `c_i = E_{i,i+1}` in
`Mₙ(R)` (the faithful nilpotent / free-2-step representation underlying Milnor's
Magnus expansion).  The result is computed exactly:

  `iterCommTower magnusGen n = (−1)ⁿ • E_{0, n+1}`   (`iterCommTower_magnusGen`),

hence the tower is **nonzero** (`iterCommTower_magnusGen_ne_zero`) and its
`(0, n+1)` matrix coordinate — the **length-`(n+2)` Milnor/Magnus coefficient
μ̄(12…(n+2))** — equals `(−1)ⁿ = ±1` (`milnorMagnusCoeff_eq`,
`milnorMagnusCoeff_ne_zero`).  This is Milnor's classical
`μ̄(12…A) = ±1 ≠ 0` for the iterated-commutator link, realized concretely and
**derived** (matrix computation), not fitted.

## Why this is the *positive* counterpart to Route B — and does NOT close the conjecture

The surviving coefficient sits in the **off-diagonal** `(0, n+1)` entry, a
**non-cyclic** linear coordinate functional.  Its cyclic **trace** is `0`
(`trace_magnusGen_realization_eq_zero`: `E_{0,n+1}` is off-diagonal), in exact
agreement with #4480's `cyclic_trace_kills_iterCommTower`.  So the Route-B
negative and this positive result are two sides of one fact:

> the Lie tower's leading coefficient **exists and is nonzero as an algebra
> element** (the `(0,A)` Magnus coordinate `= ±1`); it is the *cyclic trace*
> that annihilates it, **not** the coefficient that vanishes.

This does **NOT** discharge `MilnorExactOrderConjecture` (#4471, the QOU
**Markov-trace** deficit `D_A`'s leading coefficient being nonzero).  Identifying
the surviving off-diagonal Magnus coefficient `±1` with the *Markov-trace*
deficit's leading coefficient is the Bar-Natan / Habegger–Masbaum
Milnor = leading-Vassiliev bridge (`BrunnianVassilievBridge`, stated
instance-less in the Vassiliev scaffold), which Mathlib does not have.  The
trace-normalised leading-coefficient sequence `μ̄_A = (3/4)·(−2)^{A−3}` (#4480)
stays **MEASURED**.  `MilnorExactOrderConjecture` is left **instance-less**
(the honest open state) — no instance is fabricated here.

## Epistemic status — VISIBLE IN THE TYPES

| Claim | status |
|-------|--------|
| `iterCommTower magnusGen n = (−1)ⁿ • E_{0,n+1}` | **PROVED** (0 free params) |
| length-A Magnus coeff `μ̄(12…A) = ±1 ≠ 0` (off-diagonal `(0,A)` coordinate) | **PROVED** (`milnorMagnusCoeff_ne_zero`) |
| cyclic **trace** of the realized tower `= 0` (agrees with #4480 Route B) | **PROVED** (`trace_magnusGen_realization_eq_zero`) |
| QOU **Markov-trace** deficit `D_A` leading coeff `≠ 0` (⇒ exact order law) | **OPEN** — `MilnorExactOrderConjecture` (#4471), no instance; needs the Milnor = leading-Vassiliev bridge (cited, Mathlib-inaccessible) |
| trace-normalised `μ̄_A = (3/4)·(−2)^{A−3}` | **MEASURED** (#4480), not derived here |

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/MilnorOrderLawGeneral.lean (#4471; iterCommTower + MilnorExactOrderConjecture)
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/MilnorExactCoefficient.lean (#4480; Route-B cyclic-trace wall)
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/MilnorVassilievGrading.lean (DD-1; grading crux, μ̄ Vassiliev degree A−1)
-- Ref: [barnatan1995] https://doi.org/10.1016/0040-9383(95)93237-2
-- Ref: [leitner2026] Habegger–Masbaum, The Kontsevich integral and Milnor's invariants, Topology 39 (2000) 1253–1289, https://doi.org/10.1016/S0040-9383(99)00041-5
-/

namespace QOU.MassTheory.MilnorMagnusCoefficient

open Matrix

/-! ### 1. The left-normed Lie iterated-commutator tower (restated from #4471) -/

section Tower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **Left-normed iterated commutator tower** (restated from #4471).
`V 0 = c 0`; `V (n+1) = [c (n+1), V n] = c(n+1)·V n − V n·c(n+1)`. -/
def iterCommTower (c : ℕ → A) : ℕ → A
  | 0 => c 0
  | (n + 1) => c (n + 1) * iterCommTower c n - iterCommTower c n * c (n + 1)

theorem iterCommTower_succ (c : ℕ → A) (n : ℕ) :
    iterCommTower c (n + 1)
      = c (n + 1) * iterCommTower c n - iterCommTower c n * c (n + 1) := rfl

end Tower

/-! ### 2. The Magnus generators — elementary matrices `E_{i,i+1}` -/

section Magnus

variable {R : Type*} [CommRing R]

/-- **Magnus generators** in `Mₙ(R)`: `magnusGen N i = E_{i, i+1}` (the
elementary matrix `single ⟨i⟩ ⟨i+1⟩ 1`) when `i+1 < N`, else `0`.  These realise
the free 2-step-nilpotent / faithful strictly-upper-triangular representation
underlying Milnor's Magnus expansion `x_i ↦ 1 + X_i`. -/
noncomputable def magnusGen (N : ℕ) (i : ℕ) : Matrix (Fin N) (Fin N) R :=
  if h : i + 1 < N then single (⟨i, by omega⟩ : Fin N) ⟨i + 1, h⟩ 1 else 0

theorem magnusGen_apply {N i : ℕ} (h : i + 1 < N) :
    magnusGen (R := R) N i = single (⟨i, by omega⟩ : Fin N) ⟨i + 1, h⟩ 1 := by
  rw [magnusGen, dif_pos h]

/-- **★ The tower on Magnus generators is `(−1)ⁿ · E_{0, n+1}`.**  A closed-form
matrix computation: the left-normed Lie iterated commutator of the elementary
matrices `E_{i,i+1}` telescopes to a single off-diagonal elementary matrix, with
sign `(−1)ⁿ`.  This is the concrete Magnus realisation of the length-`(n+2)`
Milnor invariant. -/
theorem iterCommTower_magnusGen (N : ℕ) :
    ∀ n : ℕ, ∀ hn : n + 1 < N,
      iterCommTower (magnusGen (R := R) N) n
        = (-1 : R) ^ n • single (⟨0, by omega⟩ : Fin N) ⟨n + 1, hn⟩ 1 := by
  intro n
  induction n with
  | zero =>
    intro hn
    rw [iterCommTower, magnusGen_apply hn, pow_zero, one_smul]
  | succ m ih =>
    intro hn
    have hm : m + 1 < N := by omega
    rw [iterCommTower_succ, ih hm, magnusGen_apply hn]
    -- c(m+1) = E_{m+1,m+2};  V_m = (-1)^m • E_{0,m+1}
    -- c(m+1)·V_m = (-1)^m • (E_{m+1,m+2}·E_{0,m+1}) = 0   (m+2 ≠ 0)
    -- V_m·c(m+1) = (-1)^m • (E_{0,m+1}·E_{m+1,m+2}) = (-1)^m • E_{0,m+2}
    have hne : (⟨m + 1 + 1, by omega⟩ : Fin N) ≠ ⟨0, by omega⟩ := by
      simp [Fin.ext_iff]
    rw [Matrix.mul_smul, Matrix.smul_mul,
        single_mul_single_of_ne _ _ _ _ hne, smul_zero,
        single_mul_single_same]
    rw [zero_sub, pow_succ]
    -- goal: -( (-1)^m • single ⟨0⟩ ⟨m+1+1⟩ (1*1) ) = (-1)^m * (-1) • single ⟨0⟩ ⟨m+1+1⟩ 1
    rw [mul_one, ← neg_smul]
    congr 1
    ring

/-- The tower on Magnus generators is **nonzero**: the length-`(n+2)` Milnor
commutator does not degenerate (needs `1 ≠ 0`). -/
theorem iterCommTower_magnusGen_ne_zero (N n : ℕ) (hn : n + 1 < N)
    [Nontrivial R] :
    iterCommTower (magnusGen (R := R) N) n ≠ 0 := by
  rw [iterCommTower_magnusGen N n hn]
  intro hcontra
  -- read off the (0, n+1) entry: it is (-1)^n ≠ 0
  have hval := congrArg (fun M : Matrix (Fin N) (Fin N) R => M ⟨0, by omega⟩ ⟨n + 1, hn⟩) hcontra
  simp only [Matrix.smul_apply, single_apply_same, smul_eq_mul, mul_one,
    Matrix.zero_apply] at hval
  exact ((isUnit_one.neg).pow n).ne_zero hval

/-! ### 3. The length-A Milnor/Magnus coefficient `μ̄(12…A) = ±1` -/

/-- The **length-`(n+2)` Milnor/Magnus coefficient**: the `(0, n+1)` matrix
coordinate of the Magnus-realised tower — the coefficient of the top Magnus
monomial in the length-`(n+2)` iterated commutator.  This is Milnor's
μ̄(12…(n+2)); it is a **non-cyclic** linear coordinate functional (contrast the
cyclic Markov trace). -/
noncomputable def milnorMagnusCoeff (N n : ℕ) (hn : n + 1 < N) : R :=
  iterCommTower (magnusGen (R := R) N) n ⟨0, by omega⟩ ⟨n + 1, hn⟩

/-- **★ The length-A Milnor/Magnus coefficient equals `(−1)ⁿ = ±1`.**  Derived
(not fitted) from the closed-form tower computation. -/
theorem milnorMagnusCoeff_eq (N n : ℕ) (hn : n + 1 < N) :
    milnorMagnusCoeff (R := R) N n hn = (-1 : R) ^ n := by
  rw [milnorMagnusCoeff, iterCommTower_magnusGen N n hn]
  simp [Matrix.smul_apply, single_apply_same, smul_eq_mul]

/-- **The length-A Milnor/Magnus coefficient is nonzero for every `A ≥ 2`.**  The
honest sub-target *"leading coefficient ≠ 0"* at the Magnus level — the
topological content `μ̄(12…A) = ±1 ≠ 0`.  (Does **not** discharge
`MilnorExactOrderConjecture`; see the module docstring.) -/
theorem milnorMagnusCoeff_ne_zero (N n : ℕ) (hn : n + 1 < N) [Nontrivial R] :
    milnorMagnusCoeff (R := R) N n hn ≠ 0 := by
  rw [milnorMagnusCoeff_eq]
  exact ((isUnit_one.neg).pow n).ne_zero

/-! ### 4. Trace-invisibility — the exact agreement with #4480's Route-B wall -/

/-- **The cyclic trace of the Magnus-realised tower vanishes** — the exact
positive-side witness of #4480's `cyclic_trace_kills_iterCommTower`.  The
surviving Milnor coefficient is off-diagonal (`E_{0,n+1}` with `n+1 ≠ 0`), so its
diagonal trace is `0`: the coefficient is nonzero *as an algebra element* while
being *trace-invisible*. -/
theorem trace_magnusGen_realization_eq_zero (N n : ℕ) (hn : n + 1 < N) :
    Matrix.trace (iterCommTower (magnusGen (R := R) N) n) = 0 := by
  have htr : Matrix.trace (single (⟨0, by omega⟩ : Fin N) ⟨n + 1, hn⟩ (1 : R)) = 0 := by
    rw [Matrix.trace]
    refine Finset.sum_eq_zero (fun i _ => ?_)
    rw [Matrix.diag_apply]
    show (if (⟨0, by omega⟩ : Fin N) = i ∧ (⟨n + 1, hn⟩ : Fin N) = i then (1 : R) else 0) = 0
    rw [if_neg]
    rintro ⟨h1, h2⟩
    simp only [Fin.ext_iff] at h1 h2
    omega
  rw [iterCommTower_magnusGen N n hn, Matrix.trace_smul, htr, smul_zero]

end Magnus

end QOU.MassTheory.MilnorMagnusCoefficient
