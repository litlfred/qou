import Mathlib.Algebra.Algebra.Defs

/-!
# Ocneanu/Markov trace cyclicity — the inductive route (abstract bricks)

The classical proof that the Markov trace on the Hecke tower `H₁ ⊂ H₂ ⊂ …` is
cyclic (`tr(ab) = tr(ba)`) is an **induction on `n`**. Unlike the per-level Gram
computation (`MarkovTraceH4`, `Fin 24`, 576 whnf-heavy evaluations) or the
character/Hoefsmit-rep keystone, the inductive step needs only the **Markov
property** `tr(x·σₙ·y) = z·tr(xy)` (`x,y ∈ Hₙ`), the inductive hypothesis
(cyclicity on `Hₙ`), and the coset structure `H_{n+1} = Hₙ ⊕ Hₙ·σₙ·Hₙ` — giving
**all levels at once**, `O(cosets²)` per step rather than `O(basis²)`.

This file proves the abstract bricks of the inductive step that follow from the
Markov property + IH **alone** (no ring/tower structure beyond `Ring A` and a
subalgebra membership predicate `memB`):

* `gen_trace_left/right/comm` — the top generator `g = σₙ` trace-commutes with the
  subalgebra: `tr(g·x) = tr(x·g) = z·tr(x)` for `x ∈ Hₙ`.
* `cyclic_one_g` — **one-`g` mixed-coset cyclicity**: for `x ∈ Hₙ` and a coset
  element `u·g·v` (`u,v ∈ Hₙ`), `tr(x·(u·g·v)) = tr((u·g·v)·x)`. Both sides reduce,
  via one Markov step and the IH cyclicity on `Hₙ`, to `z·tr(v·x·u)`.

Together with the trivial `Hₙ×Hₙ` case (IH directly), these discharge every
coset-pair case of the inductive step **except the two-`g` case**
`tr((u·g·v)(p·g·q))`, whose middle `g·(v·p)·g` requires the Hecke relation
`g² = 1 + hh·g` together with the finer tower structure (`H_{n-1} ⊂ Hₙ` and the
braid interaction of `σₙ` with `σ_{n-1}`) to reduce back into `Hₙ + Hₙ·g·Hₙ`.

The **`g·w·g` reduction sub-bricks** for that two-`g` core are proved here
(`gwg_of_lower`, `gwg_of_mid`), using the far-commutation of `g = σₙ` with
`H_{n-1}`, the Hecke relation, and the braid relation `g·f·g = f·g·f`
(`f = σ_{n-1}`). What remains is the **assembly**: decompose an arbitrary
`w ∈ Hₙ` over its `H_{n-1}` cosets (`w = a + b·f·c`), apply these sub-bricks
term-by-term to land `g·w·g ∈ Hₙ + Hₙ·g·Hₙ`, then trace-reduce both sides of the
two-`g` product via one Markov step + the IH. That assembly is the residual crux;
it is documented, not axiomatised or `sorry`'d.
-/

namespace QOU.Machinery.MarkovInductive

variable {R A : Type*} [CommRing R] [Ring A]

/- Membership predicate `memB x` = "`x ∈ Hₙ`", the subalgebra of `H_{n+1}`. -/
variable (memB : A → Prop)

/-- **Brick — top generator, left.** From the Markov property `tr(x·g·y)=z·tr(xy)`
(`x,y ∈ Hₙ`) with `x = 1`: `tr(g·x) = z·tr(x)` for `x ∈ Hₙ`. -/
theorem gen_trace_left (tr : A → R) (g : A) (z : R)
    (hmarkov : ∀ x y : A, memB x → memB y → tr (x * g * y) = z * tr (x * y))
    (hone : memB 1) (x : A) (hx : memB x) :
    tr (g * x) = z * tr x := by
  have h := hmarkov 1 x hone hx
  simpa using h

/-- **Brick — top generator, right.** Symmetric: `tr(x·g) = z·tr(x)`. -/
theorem gen_trace_right (tr : A → R) (g : A) (z : R)
    (hmarkov : ∀ x y : A, memB x → memB y → tr (x * g * y) = z * tr (x * y))
    (hone : memB 1) (x : A) (hx : memB x) :
    tr (x * g) = z * tr x := by
  have h := hmarkov x 1 hx hone
  simpa using h

/-- **Brick — generator trace-commutes with the subalgebra.** For `x ∈ Hₙ`,
`tr(g·x) = tr(x·g)` (both `= z·tr x`). The base cyclicity fact for coset reps. -/
theorem gen_trace_comm (tr : A → R) (g : A) (z : R)
    (hmarkov : ∀ x y : A, memB x → memB y → tr (x * g * y) = z * tr (x * y))
    (hone : memB 1) (x : A) (hx : memB x) :
    tr (g * x) = tr (x * g) := by
  rw [gen_trace_left memB tr g z hmarkov hone x hx,
      gen_trace_right memB tr g z hmarkov hone x hx]

/-- **Brick — one-`g` mixed-coset cyclicity.** For `x ∈ Hₙ` and a coset element
`u·g·v` (`u,v ∈ Hₙ`): `tr(x·(u·g·v)) = tr((u·g·v)·x)`. Both sides reduce, via one
Markov step + the inductive cyclicity on `Hₙ`, to `z·tr(v·x·u)`. -/
theorem cyclic_one_g (tr : A → R) (g : A) (z : R)
    (hIH : ∀ x y : A, memB x → memB y → tr (x * y) = tr (y * x))
    (hmarkov : ∀ x y : A, memB x → memB y → tr (x * g * y) = z * tr (x * y))
    (hmul : ∀ x y : A, memB x → memB y → memB (x * y))
    (x u v : A) (hx : memB x) (hu : memB u) (hv : memB v) :
    tr (x * (u * g * v)) = tr ((u * g * v) * x) := by
  have e1 : x * (u * g * v) = (x * u) * g * v := by simp only [mul_assoc]
  have e2 : (u * g * v) * x = u * g * (v * x) := by simp only [mul_assoc]
  rw [e1, e2, hmarkov (x * u) v (hmul x u hx hu) hv,
      hmarkov u (v * x) hu (hmul v x hv hx)]
  -- both traces reduce, by cyclicity on Hₙ, to `tr (v · (x · u))`
  have key : tr ((x * u) * v) = tr (u * (v * x)) := by
    rw [hIH (x * u) v (hmul x u hx hu) hv, hIH u (v * x) hu (hmul v x hv hx),
        mul_assoc]
  rw [key]

/-! ## Two-`g` core: the `g·w·g` reduction sub-bricks

These use the Hecke tower's braid structure — far-commutation of `g = σₙ` with
`H_{n-1}`, the Hecke relation `g² = 1 + hh·g` (`hh` the central Hecke parameter,
`= q − q⁻¹` in the algebra), and the braid `g·f·g = f·g·f` (`f = σ_{n-1}`) — to
push a `g·w·g` (`w ∈ Hₙ`) back into `Hₙ + Hₙ·g·Hₙ`, term-by-term over `w`'s
`H_{n-1}` coset decomposition `w = a + b·f·c`. -/

/-- **Sub-brick — `g·a·g` for `a ∈ H_{n-1}`.** Far-commutation (`g·a = a·g`) + the
Hecke relation `g² = 1 + hh·g` give `g·a·g = a + a·hh·g ∈ Hₙ + Hₙ·g`. -/
theorem gwg_of_lower (g a hh : A)
    (hfar : g * a = a * g) (hhecke : g * g = 1 + hh * g) :
    g * a * g = a + a * hh * g := by
  rw [hfar, mul_assoc, hhecke, mul_add, mul_one, ← mul_assoc]

/-- **Sub-brick — `g·(b·f·c)·g` for `b,c ∈ H_{n-1}`.** Far-commutation of `g` with
`b, c` + the braid relation `g·f·g = f·g·f` give `g·(b·f·c)·g = b·(f·g·f)·c`, a
single `Hₙ·g·Hₙ` term. -/
theorem gwg_of_mid (g f b c : A)
    (hfarb : g * b = b * g) (hfarc : c * g = g * c)
    (hbraid : g * f * g = f * g * f) :
    g * (b * f * c) * g = b * (f * g * f) * c := by
  have step : g * (b * f * c) * g = b * (g * f * g) * c := by
    rw [show g * (b * f * c) * g = g * b * f * (c * g) by simp only [mul_assoc],
        hfarb, hfarc]
    simp only [mul_assoc]
  rw [step, hbraid]

end QOU.Machinery.MarkovInductive
