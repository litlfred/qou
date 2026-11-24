/-
# The modular double degenerates at the substrate — and it is forced, not chosen

Option **B** of the front-(a) triage (`qou-dvlt`): is the `|q̃| ≈ 1e-165`
suppression of Faddeev's modular dual at the substrate an artifact of the
`arg b = +pi/4` convention, or intrinsic? **Intrinsic**, and the reason is
algebraic rather than analytic — which is why this file needs no `Real.pi`.

The substrate regime of `computations/qbeta/phi_b_evaluator.py` takes
`b = sqrt(ln q0 / 2pi) * exp(i pi/4)`, so `b^2 = i * ln q0/(2pi)` is purely
imaginary and

    q  = exp( 2 pi i b^2)  = exp(-ln q0) = 1/q0    (real, as the substrate needs)
    q~ = exp(-2 pi i/b^2)  = exp(-4 pi^2 / ln q0)

Write `b^2 = i y` with `y > 0`, and put `c = 2pi`. Then `log q = -c y` and
`log q~ = -c / y`, so

    **log q * log q~ = c^2**

for every `y != 0`. The `y` cancels. That is `modular_reciprocity` below, stated
over a generic field in a generic `c` — because the fact has nothing to do with
`pi` or with the reals: it is `(c y)(c / y) = c^2`. Naming it that way makes the
Option-B conclusion unmissable: **the dual is not a free parameter.** Demanding a
real `q` at all forces `b^2` purely imaginary, `y` is then the only freedom, and
the product does not depend on it.

Consequences, proved here:

* `logQDual_eq_div` — `log q~ = c^2 / log q`. Reciprocal, so the suppression is
  not gradual: halving `|log q|` doubles `|log q~|`.
* `self_dual_iff_y_eq_one` — the two sides balance exactly at `y = 1`
  (`q = exp(-2pi) ~ 0.00187` at `c = 2pi`).
* `dual_lt_of_y_lt_one` — for `0 < y < 1` the dual's log is strictly the more
  negative, i.e. `|q~| < |q|`, and the gap widens reciprocally as `y -> 0`.

**Why this closes front (a) as stated.** `BarInvolutionDomainObstruction` proved
a single q-series cannot supply the bar-even projection, and that the object
required is a *pair* — the Garoufalidis-Zagier shape, whose second entry is
exactly this modular dual. `phi_b_evaluator` already realises that pair at the
substrate. But the substrate sits at `q0 ~ 1.10998`, so `|log q| = 0.10434`
against the balanced value `2pi = 6.28319` — **60.2x too close to 1** — and the
reciprocity then forces `|log q~| = 378.3`, i.e. `|q~| ~ 4.8e-165`.

The second entry of the pair is numerically absent precisely where the framework
needs it, and `q0` is an input, so nothing in the construction can be re-chosen
to avoid it. Sitting near `1` *is* sitting at the degenerate point of the
modular double.

## WHAT IS PROVED HERE, AND WHAT IS NOT (read before citing this file)

**Proved in Lean:** the algebra. `logQ` and `logQDual` below are *definitions* —
they are STIPULATED to be `-(c*y)` and `-(c/y)` — and every theorem in this file
is a statement about those stipulations. `modular_reciprocity` is
`(c y)(c / y) = c^2`. That is a real theorem and it is trivial.

**NOT proved in Lean, and this file must not be cited as if it were:**

1. that `log q = -2 pi y` and `log q~ = -2 pi / y` for Faddeev's actual `q` and
   `q~`. That identification is where the physics lives, and here it is a `def`,
   not a derivation from the state integral;
2. that a real `q` *forces* `b^2` purely imaginary. That step is prose in this
   docstring;
3. anything whatsoever about `Phi_b`.

The identification is standard in the Faddeev / modular-double literature and is
**verified numerically at the substrate** by the companion probe (`Re(b^2) = 0`
exactly, `q = 1/q0` exactly, reciprocity to 0.0 relative error) — but at that
point only, and by evaluating `exp`, not by proof.

So the honest reading of the Option-B conclusion is: *given* the standard
identification, the degeneracy is forced by an algebraic identity. The force is
real; the premise is imported. Per AGENTS.md "sorry-free != derived", do not
upgrade this to "Lean proves the modular double degenerates".

**Scope-(b), invariant named**: the reciprocity holds identically in `y`. Under
the imported identification that covers every real-`q` regime, which is the
Option-B claim. It excludes *any* attempt to obtain a usable modular dual at a
substrate near `1`. It says nothing about the state integral at other `q`, and
nothing about (H1) `c_3^even = -Vol(4_1)`.

Companion probe: `computations/qbeta/qbeta_modular_double_reciprocity.py`
(reciprocity to 0.0 relative error at the substrate; `Re(b^2) = 0` exactly).
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.QBeta.ModularDoubleReciprocity

set_option autoImplicit false

/-- `log q` for `q = exp(2 pi i b^2)` with `b^2 = i y`, in units where `c = 2pi`:
equals `-(c * y)`. -/
def logQ {K : Type*} [Field K] (c y : K) : K := -(c * y)

/-- `log q~` for the modular dual `q~ = exp(-2 pi i / b^2)` with `b^2 = i y`:
equals `-(c / y)`. -/
def logQDual {K : Type*} [Field K] (c y : K) : K := -(c / y)

/-- **The modular-double reciprocity.** `log q * log q~ = c^2`, for every
`y ≠ 0` — the `y` cancels.

Generic per §7c: any field, and no `pi`, no ordering, no `ℝ`.

This is a statement about the two `def`s above, which are stipulated. It is
`(c y)(c / y) = c^2` and nothing more. That it is *algebraic* is the Option-B
point — an algebraic identity leaves no convention to re-choose — but the step
from Faddeev's `q`, `q~` to these definitions is imported, not proved. See the
module docstring. -/
theorem modular_reciprocity {K : Type*} [Field K] (c y : K) (hy : y ≠ 0) :
    logQ c y * logQDual c y = c ^ 2 := by
  unfold logQ logQDual
  field_simp

/-- The dual through the reciprocity: `log q~ = c^2 / log q`.

Reciprocal, so the suppression is not gradual — halving `|log q|` doubles
`|log q~|`. -/
theorem logQDual_eq_div {K : Type*} [Field K] (c y : K) (hc : c ≠ 0) (hy : y ≠ 0) :
    logQDual c y = c ^ 2 / logQ c y := by
  have hlq : logQ c y ≠ 0 := by
    unfold logQ
    simpa using mul_ne_zero hc hy
  rw [eq_div_iff hlq, mul_comm]
  exact modular_reciprocity c y hy

/-- **The balanced point.** The two sides agree exactly at `y = 1` — at `c = 2pi`
that is `q = exp(-2pi) ≈ 0.00187`.

Archimedean: the `↔` needs `y > 0` to rule out `y = -1`, so this one takes `ℝ`. -/
theorem self_dual_iff_y_eq_one {c y : ℝ} (hc : 0 < c) (hy : 0 < y) :
    logQ c y = logQDual c y ↔ y = 1 := by
  unfold logQ logQDual
  constructor
  · intro h
    have hcy : c * y = c / y := by linarith
    -- `field_simp` reduces this to `y ^ 2 = 1`; with `0 < y` that forces `y = 1`
    field_simp at hcy
    have hfac : (y - 1) * (y + 1) = 0 := by nlinarith [hcy]
    rcases mul_eq_zero.mp hfac with h1 | h2
    · linarith
    · linarith
  · intro h; rw [h]; field_simp

/-- **Near `1` is the worst place to sit.** For `0 < y < 1` the dual's log is
strictly the more negative, so `|q~| < |q|`; by `logQDual_eq_div` the gap widens
reciprocally as `y → 0`.

The substrate has `y = ln q0 / (2pi) ≈ 0.0166`, which is this case — and the
resulting `|log q~| ≈ 378` is the `4.8e-165`. -/
theorem dual_lt_of_y_lt_one {c y : ℝ} (hc : 0 < c) (hy : 0 < y) (h1 : y < 1) :
    logQDual c y < logQ c y := by
  unfold logQ logQDual
  have hyy : y * y < 1 := by nlinarith
  have : c * y < c / y := by
    rw [lt_div_iff₀ hy]
    nlinarith [hc, hyy]
  linarith

end QOU.QBeta.ModularDoubleReciprocity
