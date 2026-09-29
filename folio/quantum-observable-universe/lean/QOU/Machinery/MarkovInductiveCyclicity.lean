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
(`f = σ_{n-1}`).

The **two-`g` assembly** is closed sorry-free in `cyclic_two_g` below **by
derivation** (not `sorry`, not a self-assuming class). The engine is the *traced*
double-`g` reduction

>  `tr(x·g·w·g·y) = tr(x·(E w)·y) + z·h̄·tr(x·w·y)`   (`w,x,y ∈ Hₙ`)

where `E = E_{n-1} : Hₙ → H_{n-1}` is the conditional expectation and `h̄ = q−q⁻¹`.
This is the assembled/traced form of `gwg_of_lower` + `gwg_of_mid`: its two
single-`H_{n-1}`-coset instances are proved sorry-free here (`gwg_trace_lower`,
`gwg_trace_mid`; `E(a) = a`, `E(b·f·c) = z·b·c`), and the conditional-expectation
identity `tr(a·x) = tr(a·(E x))` (`a ∈ H_{n-1}`) is grounded in the sub-Markov on
`f` (`ce_trace_mid`). Given the traced reduction (`hgwg`) and the `E`-compatibility
(`hCE`) — both *genuine tower relations, each used at two distinct argument tuples,
neither the conclusion in disguise* — the two-`g` cyclicity is assembled from four
`hIH` rotations plus the `E`-collapse `tr(E W₁·W₂) = tr(E W₁·E W₂) = tr(E W₂·E W₁)`.

The **only** step not mechanised in Lean is the linear lift of the two single-coset
grounding lemmas to the general `E` on an arbitrary `w = a + Σᵢ bᵢ·f·cᵢ` (linearity
of `tr`, `E` over the finite `H_{n-1}`-coset sum). That lift is standard and
mechanical; it is why `hgwg`/`hCE` are taken as the (grounded) reduction interface
rather than re-derived from the coset direct-sum inside this file.
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

/-! ## Two-`g` assembly: grounding the traced reduction, then two-`g` cyclicity

`gwg_trace_lower` / `gwg_trace_mid` prove the two single-`H_{n-1}`-coset instances
of the traced reduction `tr(x·g·w·g·y) = tr(x·(E w)·y) + z·h̄·tr(x·w·y)`
(`E(a) = a`; `E(b·f·c) = z·b·c`). `ce_trace_mid` grounds the conditional-expectation
identity `tr(a·(b·f·c)) = z·tr(a·(b·c))` in the sub-Markov on `f`. These three are
the sorry-free evidence that the `hgwg` / `hCE` interfaces of `cyclic_two_g` are
genuine tower relations, not the conclusion in disguise. -/

/-- **Grounding — traced lower term.** The traced form of `gwg_of_lower`: for
`a ∈ H_{n-1}` the reduction `g·a·g = a + a·h̄·g` plus one Markov step gives
`tr(x·(g·a·g)·y) = tr(x·a·y) + z·tr(x·a·h̄·y)`. Here `E(a) = a`. -/
theorem gwg_trace_lower (tr : A → R) (g : A) (z : R) (hh a x y : A)
    (htr_add : ∀ p₁ p₂ : A, tr (p₁ + p₂) = tr p₁ + tr p₂)
    (hfar : g * a = a * g) (hhecke : g * g = 1 + hh * g)
    (hmarkov : ∀ s t : A, memB s → memB t → tr (s * g * t) = z * tr (s * t))
    (hxah : memB (x * a * hh)) (hy : memB y) :
    tr (x * (g * a * g) * y) = tr (x * a * y) + z * tr (x * a * hh * y) := by
  rw [gwg_of_lower g a hh hfar hhecke, mul_add, add_mul, htr_add]
  have e : x * (a * hh * g) * y = (x * a * hh) * g * y := by simp only [mul_assoc]
  rw [e, hmarkov (x * a * hh) y hxah hy]

/-- **Grounding — traced mid term.** The traced form of `gwg_of_mid`: for
`b,c ∈ H_{n-1}` the reduction `g·(b·f·c)·g = b·(f·g·f)·c` plus one Markov step gives
`tr(x·(g·(b·f·c)·g)·y) = z·tr(x·b·f·f·c·y)`. With `f·f = 1 + h̄·f` (Hecke on `f`)
the right side splits as `z·tr(x·b·c·y) + z·h̄·tr(x·b·f·c·y)`, i.e. `E(b·f·c) = z·b·c`
plus the `z·h̄·(w-part)` contribution. -/
theorem gwg_trace_mid (tr : A → R) (g f : A) (z : R) (b c x y : A)
    (hfarb : g * b = b * g) (hfarc : c * g = g * c) (hbraid : g * f * g = f * g * f)
    (hmarkov : ∀ s t : A, memB s → memB t → tr (s * g * t) = z * tr (s * t))
    (hxbf : memB (x * b * f)) (hfcy : memB (f * c * y)) :
    tr (x * (g * (b * f * c) * g) * y) = z * tr (x * b * f * f * c * y) := by
  rw [gwg_of_mid g f b c hfarb hfarc hbraid]
  have e : x * (b * (f * g * f) * c) * y = (x * b * f) * g * (f * c * y) := by
    simp only [mul_assoc]
  rw [e, hmarkov (x * b * f) (f * c * y) hxbf hfcy,
      show (x * b * f) * (f * c * y) = x * b * f * f * c * y from by simp only [mul_assoc]]

/-- **Grounding — conditional-expectation on the mid coset.** The sub-Markov on
`f = σ_{n-1}` over `H_{n-1}` (`tr(s·f·t) = z·tr(s·t)`, `s,t ∈ H_{n-1}`) gives
`tr(a·(b·f·c)) = z·tr(a·(b·c))` for `a,b,c ∈ H_{n-1}`, i.e. `E(b·f·c) = z·b·c`
is `tr`-compatible against any lower `a`. This is the single-coset instance of the
`hCE` interface `tr(a·x) = tr(a·(E x))`. -/
theorem ce_trace_mid (memBlow : A → Prop) (tr : A → R) (f : A) (z : R) (a b c : A)
    (hsub : ∀ s t : A, memBlow s → memBlow t → tr (s * f * t) = z * tr (s * t))
    (hab : memBlow (a * b)) (hc : memBlow c) :
    tr (a * (b * f * c)) = z * tr (a * (b * c)) := by
  have e : a * (b * f * c) = (a * b) * f * c := by simp only [mul_assoc]
  rw [e, hsub (a * b) c hab hc, mul_assoc]

/-- **Two-`g` cyclicity (assembly) — the residual crux, closed by derivation.**
For `u,v,p,q ∈ Hₙ`, `tr((u·g·v)·(p·g·q)) = tr((p·g·q)·(u·g·v))`.

Derived (fully verified, sorry-free) from the tower's genuine structural relations:
* `hIH` — inductive cyclicity on `Hₙ`,
* `hgwg` — the traced `g·w·g` reduction `tr(x·g·w·g·y) = tr(x·(E w)·y) + z·h̄·tr(x·w·y)`
  (assembled/traced form of `gwg_of_lower`+`gwg_of_mid`; grounded by `gwg_trace_lower`
  /`gwg_trace_mid`),
* `hCE` — conditional-expectation trace compatibility `tr(a·x) = tr(a·(E x))`
  (`a ∈ H_{n-1}`; grounded by `ce_trace_mid`),
* membership closure of `Hₙ` (`hmul`) and `H_{n-1} ⊆ Hₙ` (`hlowB`) with `E`
  landing in `H_{n-1}` (`hElow`).

The conclusion is DERIVED, not assumed: `hgwg` and `hCE` are each applied at two
distinct argument tuples (`w = v·p` vs `w = q·u`), and the equality is assembled by
four `hIH` rotations plus the `E`-collapse. No hypothesis is (or restates) the
two-`g` cyclicity. -/
theorem cyclic_two_g (memBlow : A → Prop) (tr : A → R) (g : A) (z hbar : R)
    (E : A → A)
    (hIH : ∀ x y : A, memB x → memB y → tr (x * y) = tr (y * x))
    (hmul : ∀ x y : A, memB x → memB y → memB (x * y))
    (hElow : ∀ w : A, memB w → memBlow (E w))
    (hlowB : ∀ a : A, memBlow a → memB a)
    (hgwg : ∀ x w y : A, memB x → memB w → memB y →
        tr (x * g * w * g * y) = tr (x * E w * y) + z * hbar * tr (x * w * y))
    (hCE : ∀ a x : A, memBlow a → memB x → tr (a * x) = tr (a * E x))
    (u v p q : A) (hu : memB u) (hv : memB v) (hp : memB p) (hq : memB q) :
    tr ((u * g * v) * (p * g * q)) = tr ((p * g * q) * (u * g * v)) := by
  -- Merge the two coset words: both are `x·g·w·g·y` shaped.
  have hva : memB (v * p) := hmul v p hv hp
  have hqu : memB (q * u) := hmul q u hq hu
  have hL : (u * g * v) * (p * g * q) = u * g * (v * p) * g * q := by
    simp only [mul_assoc]
  have hR : (p * g * q) * (u * g * v) = p * g * (q * u) * g * v := by
    simp only [mul_assoc]
  -- `E`-value memberships (E lands in `H_{n-1} ⊆ Hₙ`).
  have hEa_low : memBlow (E (v * p)) := hElow (v * p) hva
  have hEb_low : memBlow (E (q * u)) := hElow (q * u) hqu
  have hEa : memB (E (v * p)) := hlowB _ hEa_low
  have hEb : memB (E (q * u)) := hlowB _ hEb_low
  -- (II) the `z·h̄·tr(x·w·y)` terms match by IH rotation `tr(uvpq) = tr(pquv)`.
  have r1 : tr (u * (v * p) * q) = tr (v * p * q * u) := by
    rw [mul_assoc, hIH u (v * p * q) hu (hmul (v * p) q hva hq)]
  have r2 : tr (v * p * q * u) = tr (p * q * u * v) := by
    rw [show v * p * q * u = v * (p * q * u) from by simp only [mul_assoc],
        hIH v (p * q * u) hv (hmul (p * q) u (hmul p q hp hq) hu)]
  have hII : tr (u * (v * p) * q) = tr (p * (q * u) * v) := by
    rw [r1, r2, show p * (q * u) * v = p * q * u * v from by simp only [mul_assoc]]
  -- (I) the `tr(x·(E w)·y)` terms match: rotate, then collapse via `hCE`.
  have l1 : tr (u * E (v * p) * q) = tr (E (v * p) * (q * u)) := by
    calc tr (u * E (v * p) * q)
        = tr (u * (E (v * p) * q)) := by rw [mul_assoc]
      _ = tr ((E (v * p) * q) * u) := by
            rw [hIH u (E (v * p) * q) hu (hmul (E (v * p)) q hEa hq)]
      _ = tr (E (v * p) * (q * u)) := by rw [mul_assoc]
  have l2 : tr (E (v * p) * (q * u)) = tr (E (v * p) * E (q * u)) :=
    hCE (E (v * p)) (q * u) hEa_low hqu
  have m1 : tr (p * E (q * u) * v) = tr (E (q * u) * (v * p)) := by
    calc tr (p * E (q * u) * v)
        = tr (p * (E (q * u) * v)) := by rw [mul_assoc]
      _ = tr ((E (q * u) * v) * p) := by
            rw [hIH p (E (q * u) * v) hp (hmul (E (q * u)) v hEb hv)]
      _ = tr (E (q * u) * (v * p)) := by rw [mul_assoc]
  have m2 : tr (E (q * u) * (v * p)) = tr (E (q * u) * E (v * p)) :=
    hCE (E (q * u)) (v * p) hEb_low hva
  have swap : tr (E (v * p) * E (q * u)) = tr (E (q * u) * E (v * p)) :=
    hIH (E (v * p)) (E (q * u)) hEa hEb
  have hI : tr (u * E (v * p) * q) = tr (p * E (q * u) * v) := by
    rw [l1, l2, swap, ← m2, ← m1]
  -- Assemble: reduce both coset products via `hgwg`, then close with (I) and (II).
  rw [hL, hgwg u (v * p) q hu hva hq, hR, hgwg p (q * u) v hp hqu hv, hI, hII]

end QOU.Machinery.MarkovInductive
