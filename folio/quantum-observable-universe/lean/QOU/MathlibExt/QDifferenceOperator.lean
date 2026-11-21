/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q-difference operator: q-Leibniz, monomial q-chain rule, and the composition obstruction

Foundational Mathlib-style infrastructure for the q-difference D-module program the
c₃↔SW leg needs (bean `qou-d8de` W1; the "missing infra (i)" recorded there). Mathlib
has no q-difference operator calculus; this file supplies the algebraic core over a
generic `CommRing`, in the **numerator form** `Δ_q f(x) = f(q·x) − f(x)` (= `(q−1)x`
times the Jackson derivative `D_q f`), which is division-free and hence total.

The point of the file — and the answer to "what breaks without a q-chain rule":

- **q-Leibniz (product) rule is clean** (`qDiff_mul`): `Δ_q(fg) = Δ_q(f)·g + (σ_q f)·Δ_q(g)`,
  where `σ_q f = f(q·)`. This is why q-difference *modules* (built from products and
  sums of the defining polynomial's coefficients) are well-behaved.
- **The chain rule survives ONLY for a monomial inner function** (`qDiff_comp_monomial`):
  `Δ_q(f ∘ (·^m))(x) = Δ_{q^m}(f)(x^m)` — with `q` rescaled to `q^m`, because
  `(q·x)^m = q^m·x^m`.
- **For a non-monomial inner function it fails** (`qDiff_comp_no_naive_chain`): a concrete
  counterexample over `ℚ`. So the SW jet tower — whose inner function is a *branch*
  `X(z)` of the color cubic, not a monomial in `z` — cannot be built by implicit
  q-differentiation; it must be a q-difference module on `C_z(X)` directly.

**Scope.** General-purpose q-difference calculus (linearity, q-Leibniz, monomial action,
monomial q-chain rule, composition counterexample). Sorry-free, §7c-clean (generic
`CommRing`; the counterexample is over `ℚ` because it is a decidable numeric fact). No
QOU-specific content, no fit, nothing wired — pure reusable infra.

-- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1 infra (i))
-/
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.MathlibExt.QDifferenceOperator

/-- **The q-shift** `σ_q f = x ↦ f(q·x)`. -/
def qShift {R : Type*} [CommRing R] (q : R) (f : R → R) : R → R := fun x => f (q * x)

/-- **The q-difference operator** (numerator form) `Δ_q f = x ↦ f(q·x) − f(x)`.
Equals `(q−1)·x · D_q f(x)` for the Jackson derivative `D_q`; division-free, so total
over any `CommRing`. -/
def qDiff {R : Type*} [CommRing R] (q : R) (f : R → R) : R → R := fun x => f (q * x) - f x

variable {R : Type*} [CommRing R]

@[simp] theorem qDiff_apply (q : R) (f : R → R) (x : R) :
    qDiff q f x = f (q * x) - f x := rfl

/-- **Additivity.** `Δ_q(f + g) = Δ_q f + Δ_q g`. -/
theorem qDiff_add (q : R) (f g : R → R) (x : R) :
    qDiff q (f + g) x = qDiff q f x + qDiff q g x := by
  simp only [qDiff, Pi.add_apply]; ring

/-- **Constant scaling.** `Δ_q(c • f) = c • Δ_q f` (as `c * f` pointwise). -/
theorem qDiff_const_mul (q c : R) (f : R → R) (x : R) :
    qDiff q (fun y => c * f y) x = c * qDiff q f x := by
  simp only [qDiff]; ring

/-- **q-Leibniz (product) rule** — the clean one:
`Δ_q(f·g)(x) = Δ_q(f)(x)·g(x) + f(q·x)·Δ_q(g)(x)`. This is the structural reason
q-difference *modules* are well-behaved. -/
theorem qDiff_mul (q : R) (f g : R → R) (x : R) :
    qDiff q (fun y => f y * g y) x
      = qDiff q f x * g x + f (q * x) * qDiff q g x := by
  simp only [qDiff]; ring

/-- **Monomial action.** `Δ_q(·^n)(x) = (q^n − 1)·x^n`. (Divide by `(q−1)x` to recover
`D_q(x^n) = [n]_q·x^{n−1}`.) -/
@[simp] theorem qDiff_pow (q x : R) (n : ℕ) :
    qDiff q (fun y => y ^ n) x = (q ^ n - 1) * x ^ n := by
  simp only [qDiff, mul_pow]; ring

/-- **The monomial q-chain rule** — the *only* surviving composition rule, with `q`
rescaled to `q^m`: `Δ_q(f ∘ (·^m))(x) = Δ_{q^m}(f)(x^m)`, because `(q·x)^m = q^m·x^m`. -/
theorem qDiff_comp_monomial (q x : R) (m : ℕ) (f : R → R) :
    qDiff q (fun y => f (y ^ m)) x = qDiff (q ^ m) f (x ^ m) := by
  simp only [qDiff, mul_pow]

/-- **No naive q-chain rule for a non-monomial inner function.** Concrete counterexample
over `ℚ`: with `f = g = (·²)` (so `f ∘ g = (·⁴)`), `Δ₂((·²)∘(·²))(1) = 15`, but the naive
"product of q-derivatives" `Δ₂(·²)(1²)·Δ₂(·²)(1) = 3·3 = 9`. `15 ≠ 9` — implicit
q-differentiation through a non-monomial branch does not close. -/
theorem qDiff_comp_no_naive_chain :
    qDiff (2 : ℚ) (fun y => (y ^ 2) ^ 2) 1
      ≠ qDiff (2 : ℚ) (fun y => y ^ 2) (1 ^ 2) * qDiff (2 : ℚ) (fun y => y ^ 2) 1 := by
  norm_num [qDiff]

end QOU.MathlibExt.QDifferenceOperator
