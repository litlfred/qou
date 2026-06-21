/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q-Casoratian (Abel) law for the q-Bessel q-difference equation

The algebraic backbone of two results in the qbk2 q-Bessel "quadratic action"
exploration:

* the coincidence-limit propagator `G_q = g₁ g₂ / D` is well-defined because the
  Casoratian `D` of two solutions is a clean monomial `D(w) = C · w^{-ν}` rather
  than the divergent power series (compute:
  `computations/qbeta/qbessel_second_kind_quadratic_action_gate.py`,
  `qbessel_offshell_resolvent_quadratic_correction.py`;
  audits `2026-06-20-qbessel-second-kind-quadratic-action-gate.md`,
  `…-offshell-resolvent-quadratic-correction.md`);
* the **reduction-of-order** construction of the genuine integer-order second
  solution recovers `g₂` from `g₁` and `D` alone, side-stepping the Neumann
  resonance and the `ν = 0` confluence (compute:
  `qbessel_rigorous_log_neumann_reduction.py`).

Both rest on one purely algebraic fact: for a second-order linear `q`-difference
equation, the **Casoratian** of any two solutions obeys a first-order
`q`-recurrence (the `q`-analogue of Abel's identity). This file proves it.

The Hahn–Exton q-Bessel generating function `g(w)` satisfies (compute
`qbessel_second_order_qdifference_equation.py`)

    (☆)   q^ν · g(q²w) − (1 + q^ν − w) · g(qw) + g(w) = 0,

a three-point (`w, qw, q²w`) equation `a · g(q²w) + b · g(qw) + c · g(w) = 0`
with `a = q^ν`, `c = 1`.  For two solutions `f, g` the Casoratian
`C(w) = f(w) g(qw) − f(qw) g(w)` then satisfies `a · C(qw) = c · C(w)`, i.e.
`q^ν · C(qw) = C(w)`.  Iterating gives `C(w) = const · w^{-ν}` — the monomial
form the propagator and the reduction-of-order construction depend on.

**Scope (honesty).** This is a `q`-special-function *machinery* lemma. It is NOT
a mass/binding claim: per `docs/audits/2026-06-20-qbessel-quadratic-binding-wiring-gate.md`
the binding use of the propagator is unforced (a 7th `Δ_λ` ansatz) and is not
wired. This lemma certifies the algebra the exploration runs on, nothing more.

Generic base ring `[CommRing R]` — `q`, `a`, `c`, and the solution values are
formal fibre parameters with no archimedean structure (CLAUDE.md §7c).
Sorry-free.

`-- Ref:` [koelink1994] https://doi.org/10.1215/S0012-7094-94-07617-0
(Hahn–Exton q-Bessel / `E_q(2)` matrix coefficients); the Casoratian/Abel
identity for linear difference equations is classical (Gasper–Rahman,
*Basic Hypergeometric Series*, 2nd ed., CUP 2004).
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-- **q-Casoratian (Abel) law — pointwise form.**

For a second-order linear `q`-difference equation `a·h₂ + b·h₁ + c·h₀ = 0`
(values of `h` at `q²w, qw, w`), two solutions `f, g` have Casoratian values
`C₀ = f₀ g₁ − f₁ g₀` at `w` and `C₁ = f₁ g₂ − f₂ g₁` at `qw` satisfying

    a · C₁ = c · C₀.

The middle coefficient `b` drops out — only the outer coefficients `a` (at `q²w`)
and `c` (at `w`) survive, which is what makes the Casoratian a *first-order*
`q`-recurrence. Proof is the elimination of the `q²w` values via the two
equations, then `ring`. -/
theorem casoratian_abel
    (a b c f₀ f₁ f₂ g₀ g₁ g₂ : R)
    (hf : a * f₂ + b * f₁ + c * f₀ = 0)
    (hg : a * g₂ + b * g₁ + c * g₀ = 0) :
    a * (f₁ * g₂ - f₂ * g₁) = c * (f₀ * g₁ - f₁ * g₀) := by
  -- a·(f₁ g₂ − f₂ g₁) = f₁·(a g₂) − g₁·(a f₂); substitute a g₂, a f₂ from hf, hg.
  linear_combination f₁ * hg - g₁ * hf

/-- **Specialisation to the Hahn–Exton q-Bessel equation `(☆)`.**

With `a = q^ν` (here the abstract parameter `qpow := q^ν`), `b = −(1 + q^ν − w)`,
`c = 1`, the Casoratian satisfies `qpow · C₁ = C₀`, i.e. `C(qw) = qpow⁻¹ · C(w)`.
Iterating this first-order `q`-recurrence yields the monomial form
`C(w) = const · w^{-ν}` that the coincidence propagator `G_q = g₁ g₂ / D` and the
reduction-of-order second solution rely on. -/
theorem qbessel_casoratian_qabel
    (w qpow f₀ f₁ f₂ g₀ g₁ g₂ : R)
    (hf : qpow * f₂ - (1 + qpow - w) * f₁ + f₀ = 0)
    (hg : qpow * g₂ - (1 + qpow - w) * g₁ + g₀ = 0) :
    qpow * (f₁ * g₂ - f₂ * g₁) = f₀ * g₁ - f₁ * g₀ := by
  have h := casoratian_abel qpow (-(1 + qpow - w)) 1 f₀ f₁ f₂ g₀ g₁ g₂
    (by linear_combination hf) (by linear_combination hg)
  simpa using h

end QOU.QBeta
