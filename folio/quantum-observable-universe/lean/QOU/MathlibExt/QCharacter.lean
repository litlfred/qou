/-
Copyright (c) 2026 litlfred. All rights reserved.

# The q-character algebra `e_{q,c}` — building block of the Birkhoff connection matrix (W2)

Foundational infra for the DRSZ Birkhoff-matrix recipe (bean `qou-xufp`, W2). The canonical
local solutions `X^{(0)} = M^{(0)} e_{q,A(0)}`, `X^{(∞)} = M^{(∞)} e_{q,A(∞)}` are built from
the **q-characters** `e_{q,c}` of the exponents: a q-character is a nonzero `f` with

  `f(q·x) = c · f(x)`   (`IsQChar q c f`).

Concretely `e_{q,c}` is a theta quotient (Sauloy); constructing it requires analysis
(θ-convergence), taken here as the standard input. What this file formalizes is the
**algebra** of q-characters and the one structural fact that makes the Birkhoff matrix
`P = (X^∞)⁻¹X^0` **elliptic (theta-valued)**: the ratio of two q-characters with the *same*
multiplier is `q`-invariant (elliptic). That ellipticity is exactly why `P`'s entries are
theta quotients rather than complex constants.

Results (generic `CommRing`, then `Field` for the ratio):
- `IsQChar.mul` — q-characters multiply: `e_{q,c}·e_{q,d} = e_{q,cd}`.
- `isQChar_one` — the constant `1` is `e_{q,1}`.
- `c1_det_character` — for the C1 exponents (`λ₊·λ₋ = q−1 = det A(0)`), the product of their
  characters is the determinant character `e_{q,q−1}`.
- `IsQChar.ratio_qInvariant` — **the ellipticity source**: `e_{q,c}/e_{q,c}` (two solutions,
  same exponent) is `q`-invariant. This is why the connection matrix is theta-valued.

**Scope.** The q-character algebra + the elliptic-ratio fact. The analytic construction of
`e_{q,c}` (theta) and the ∞ slope-½ Stokes multipliers are NOT here — beaned (`qou-xufp`).
§7c: generic `CommRing`; `Field` only for the ratio. Sorry-free. No fit; nothing wired.

-- Ref: [leitner2026] library/equations-aux-q-differences/Equations_aux_q-differences.pdf (DRSZ, q-characters e_{q,c})
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

namespace QOU.MathlibExt.QCharacter

/-- **q-character**: `f(q·x) = c·f(x)`. The multiplier `c` is the local exponent. -/
def IsQChar {R : Type*} [Mul R] (q c : R) (f : R → R) : Prop := ∀ x, f (q * x) = c * f x

/-- **q-invariant (elliptic)**: `h(q·x) = h(x)`, i.e. a function on `ℂ*/qℤ`. -/
def QInvariant {R : Type*} [Mul R] (q : R) (h : R → R) : Prop := ∀ x, h (q * x) = h x

variable {R : Type*} [CommRing R]

/-- **q-characters multiply**: `e_{q,c}·e_{q,d}` is a q-character with multiplier `c·d`. -/
theorem IsQChar.mul {q c d : R} {f g : R → R} (hf : IsQChar q c f) (hg : IsQChar q d g) :
    IsQChar q (c * d) (fun x => f x * g x) := by
  intro x
  show f (q * x) * g (q * x) = c * d * (f x * g x)
  rw [hf x, hg x]; ring

/-- The constant `1` is the trivial q-character `e_{q,1}`. -/
theorem isQChar_one (q : R) : IsQChar q (1 : R) (fun _ => 1) := by
  intro x; show (1 : R) = 1 * 1; ring

/-- **C1 determinant character.** The product of the two C1 exponent characters (multipliers
`λ₊, λ₋` with `λ₊·λ₋ = q−1 = det A(0)`, per `C1ModuleExponents`) is the determinant character
`e_{q,q−1}` — the q-character carried by `det X^{(0)}`. -/
theorem c1_det_character {q lp lm : R} {ep em : R → R}
    (hp : IsQChar q lp ep) (hm : IsQChar q lm em) (hdet : lp * lm = q - 1) :
    IsQChar q (q - 1) (fun x => ep x * em x) := by
  have h := hp.mul hm
  rwa [hdet] at h

/-- **The ellipticity source (why the Birkhoff matrix is theta-valued).** If `f` and `g` are
two q-characters with the *same* nonzero multiplier `c`, their ratio `f/g` is `q`-invariant
(elliptic). The connection matrix `P = (X^∞)⁻¹X^0` compares two solutions with matching
exponents, so its entries are such ratios — elliptic, hence theta quotients, not constants. -/
theorem IsQChar.ratio_qInvariant {K : Type*} [Field K] {q c : K} {f g : K → K}
    (hf : IsQChar q c f) (hg : IsQChar q c g) (hc : c ≠ 0) :
    QInvariant q (fun x => f x / g x) := by
  intro x
  show f (q * x) / g (q * x) = f x / g x
  rw [hf x, hg x, mul_div_mul_left _ _ hc]

end QOU.MathlibExt.QCharacter
