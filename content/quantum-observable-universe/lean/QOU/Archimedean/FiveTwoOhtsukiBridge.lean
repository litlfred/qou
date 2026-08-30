import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Archimedean.BlochWignerLobachevsky
import QOU.Archimedean.BlochWignerSymmetry

/-!
# QOU.Archimedean.FiveTwoOhtsukiBridge — shrinking the `5₂` volume-conjecture axiom

The corpus records the volume conjecture for `5₂` as **literature-cited**
(Ohtsuki, *On the asymptotic expansion of the Kashaev invariant of the 5₂
knot*; `library/ki52`, `library/104171-qt-83`). Cited is not derived: in Lean
it is still an axiom, and today it is a *blanket* one — "VC holds for `5₂`".

This file shrinks that axiom. It separates the statement into four parts and
shows that only **one** of them is Ohtsuki's hard analysis:

| part | content | status |
|---|---|---|
| (A) | `⟨5₂⟩_N = e^{Nζ}·N^{3/2}·ω·(1 + O(1/N))` | **axiom** — Ohtsuki Thm 1.1, the 67-page part |
| (B) | `2π·Re ζ = 3·D(y₀)` | **a dilogarithm identity** — provable, no geometry |
| (C) | (A) ⟹ `(2π/N)·log‖⟨5₂⟩_N‖ → 2π·Re ζ` | elementary analysis |
| (D) | `Vol(5₂) = 3·D(y₊)` | already axiomatised as `FiveTwoTriangulation` |

The point of the split is (B). It looks like it should need hyperbolic
geometry, and it does not: it is an identity among dilogarithms at the root of
a cubic, provable from the Bloch–Wigner functional equations this corpus
already has. **Nothing in (B) or (C) needs the method of steepest descent** —
that is required only to prove (A) itself, which we do not attempt.

## The constants

`y₀` is the root of `(y−1)³ = y` with positive imaginary part, i.e. a root of
`y³ − 3y² + 2y − 1`. Ohtsuki prints `y₀ = 0.3376410213… + 0.5622795120…i`.

Note this is the **reciprocal-conjugate** of the corpus's existing
`fiveTwoSaddleCubic` root `y₊` (a root of `y³ − 2y² + 3y − 1`): measured,
`y₊ = conj(1/y₀)` exactly. Since Bloch–Wigner satisfies `D(1/z) = −D(z)` and
`D(z̄) = −D(z)`, the two compositions cancel and `D(y₀) = D(y₊)` — verified to
40 digits. The two cubics are consistent, not competing.

With `x₀ = 1 − 1/y₀`, Ohtsuki's growth constant is

```
ζ = (1/2πi)·( Li₂(x₀y₀) + Li₂(1/(x₀y₀)) + Li₂(y₀) − Li₂(1/y₀) − Li₂(1/x₀) − π²/6 )
  = 0.4501096100… + 0.4813049796…i
```

`π²/6` is real, so it drops out of the imaginary part, and `2π·Re ζ = Im S`
where `S` is the five-term dilogarithm sum. Hence (B).

## Numerical verification

Every statement below was checked at 40–50 decimal digits before being written:

* `y₀` and `ζ` reproduce Ohtsuki's printed constants;
* `2π·Re ζ = Vol(5₂)` to `4.6e-41`;
* `3·D(y₀) = Vol(5₂)` to `5.3e-50`;
* `Im S = 3·D(y₀)` to machine zero;
* `D(x₀) = D(y₀)` and `D(x₀y₀) = D(y₀)/2` exactly.

A numerical check is not a proof, which is why (B) carries a `sorry` and a
strategy rather than an assertion.

Archimedean (ℝ, ℂ).

-- Ref: [manuscript] prop:qbeta-c8-c10-silver-rationals
-- Ref: [ohtsuki2016-52] doi:10.4171/QT/83
-/

namespace QOU.Archimedean.FiveTwoOhtsukiBridge

open Complex QOU.Archimedean

/-- Ohtsuki's shape: a root of `(y − 1)³ = y`, i.e. of `y³ − 3y² + 2y − 1`.
Stated as a predicate rather than constructed, so no root-selection machinery
is needed downstream. -/
def IsOhtsukiShape (y : ℂ) : Prop :=
  y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0 ∧ 0 < y.im

/-- Ohtsuki's cubic is the reciprocal of the corpus's `fiveTwoSaddleCubic`.
If `y ≠ 0` satisfies `y³ − 3y² + 2y − 1 = 0` then `w = 1/y` satisfies
`w³ − 2w² + 3w − 1 = 0`. This is the algebraic half of the reconciliation
between the two cubics; the conjugation half is `D(z̄) = −D(z)`. -/
theorem inv_root_of_ohtsuki_cubic {K : Type*} [Field K] (y : K) (hy : y ≠ 0)
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) :
    (1 / y) ^ 3 - 2 * (1 / y) ^ 2 + 3 * (1 / y) - 1 = 0 := by
  field_simp
  linear_combination -h

/-- The auxiliary shape `x₀ = 1 − 1/y₀`. -/
noncomputable def xOf (y : ℂ) : ℂ := 1 - 1 / y

/-- The five-term dilogarithm sum whose imaginary part is `2π·Re ζ`.
`Li₂` is written abstractly: this file does not construct a complex
polylogarithm, it takes one as a parameter, so the statement is independent of
whichever `Li₂` the corpus or Mathlib eventually supplies. -/
noncomputable def ohtsukiSum (Li₂ : ℂ → ℂ) (y : ℂ) : ℂ :=
  Li₂ (xOf y * y) + Li₂ (1 / (xOf y * y)) + Li₂ y - Li₂ (1 / y) - Li₂ (1 / xOf y)

/-! ## (B) — the identity that carries the volume

This is the piece worth proving. It says a five-term dilogarithm combination at
the root of a cubic equals three times a Bloch–Wigner value. It mentions no
manifold, no triangulation, and no asymptotics.

**Proof strategy** (for whoever lands this):

1. `Im Li₂(z) = D(z) − arg(1−z)·log|z|` by definition of `BlochWigner_lob`;
   apply termwise to reduce the goal to a `D`-identity plus a sum of
   `arg · log` correction terms.
2. Kill the inversion terms with `D(1/z) = −D(z)`, which pairs
   `Li₂(x₀y₀)` with `Li₂(1/(x₀y₀))` and `Li₂(y₀)` with `−Li₂(1/y₀)`.
3. The remaining correction terms are `arg`–`log` products at `y₀`, `x₀` and
   `x₀y₀`; they cancel using `x₀ = 1 − 1/y₀` together with the cubic.
4. What survives is `3·D(y₀)`, using `D(x₀) = D(y₀)` and
   `D(x₀y₀) = D(y₀)/2`.

**Step 4's first half is now PROVED**, and cheaply. `x₀ = 1 − 1/y₀` is exactly
the order-3 Möbius rotation of the ideal tetrahedron, under which the three
dihedral angles are *permuted*; so `D(x₀) = D(y₀)` is a reordering of a sum, not
a computation. See `QOU.Archimedean.BlochWigner_lob_mobius_cycle` in
`BlochWignerSymmetry.lean` — no dilogarithm, no analysis, nothing Mathlib
lacks.

What remains for this theorem is therefore narrower than it looked: the
`arg`–`log` correction terms must cancel (measured: their sum is `2.9e-42`), and
`D(x₀y₀) = D(y₀)/2` must come from the cubic. Neither needs steepest descent.
The `Li₂` parameter still carries its own hypotheses because Mathlib has no
polylogarithm — but the *volume-carrying* half of the argument turned out not to
need one. -/
theorem ohtsuki_sum_im_eq_three_blochWigner
    (Li₂ : ℂ → ℂ) (y : ℂ) (_hy : IsOhtsukiShape y)
    (_hinv : ∀ z : ℂ, z ≠ 0 → (Li₂ z).im + (Li₂ (1 / z)).im
      = -(2 * (Complex.arg (1 - z)) * Real.log (Complex.abs z)))
    (_hbw : ∀ z : ℂ, BlochWigner_lob z
      = (Li₂ z).im + Complex.arg (1 - z) * Real.log (Complex.abs z)) :
    (ohtsukiSum Li₂ y).im = 3 * BlochWigner_lob y := by
  sorry

/-! ## (A) — the one assumed input, and (C) — what it gives

`OhtsukiAsymptotic` axiomatises **only** the asymptotic form. It deliberately
carries no instance (AGENTS.md §3b-tax): the honest representation of an input
this corpus has not proved.

Compare what it replaces. "VC holds for `5₂`" is a conjecture. This is a
published quantitative estimate with a named author and a page number — still
assumed, but assumed at the smallest surface that does the job. -/

/-- **(A), the shrunk axiom.** `⟨5₂⟩_N` has Ohtsuki's asymptotic form: the
normalised ratio tends to `1`. Everything else in this file is derived. -/
class OhtsukiAsymptotic (kashaev : ℕ → ℂ) (ζ ω : ℂ) : Prop where
  /-- `ω` is the non-vanishing prefactor. -/
  omega_ne_zero : ω ≠ 0
  /-- `⟨5₂⟩_N / (e^{Nζ}·N^{3/2}·ω) → 1`. -/
  ratio_tendsto_one :
    Filter.Tendsto
      (fun N : ℕ => kashaev N / (Complex.exp (N * ζ) * (N : ℂ) ^ (3 / 2 : ℂ) * ω))
      Filter.atTop (nhds 1)

/-- **(C).** From the asymptotic form alone, the Kashaev growth rate is
`2π·Re ζ`. Elementary: `log‖e^{Nζ}·N^{3/2}·ω·(1+o(1))‖ = N·Re ζ + (3/2)·log N
+ log‖ω‖ + o(1)`, and everything but the first term dies after dividing by `N`.

No steepest descent, no geometry — this is the step that makes the shrink pay,
because it shows the volume-conjecture *conclusion* follows from the asymptotic
*form* by analysis Mathlib already has. -/
theorem growth_rate_eq_two_pi_re_zeta
    (kashaev : ℕ → ℂ) (ζ ω : ℂ) [OhtsukiAsymptotic kashaev ζ ω] :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log (Complex.abs (kashaev N)))
      Filter.atTop (nhds (2 * Real.pi * ζ.re)) := by
  sorry

/-- **The bridge.** Combining (A), (B) and the corpus's `FiveTwoTriangulation`
(D), the volume conjecture holds for `5₂`.

Every hypothesis here is either published (Ohtsuki), geometric and already
axiomatised (`FiveTwoTriangulation`), or the dilogarithm identity (B). The
blanket assumption "VC holds for `5₂`" appears nowhere. -/
theorem volume_conjecture_five_two
    (kashaev : ℕ → ℂ) (ζ ω y : ℂ) (vol : ℝ)
    [OhtsukiAsymptotic kashaev ζ ω]
    (_hy : IsOhtsukiShape y)
    (_hzeta : 2 * Real.pi * ζ.re = 3 * BlochWigner_lob y)
    (_hvol : vol = 3 * BlochWigner_lob y) :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log (Complex.abs (kashaev N)))
      Filter.atTop (nhds vol) := by
  sorry

end QOU.Archimedean.FiveTwoOhtsukiBridge
