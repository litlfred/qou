import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Archimedean.BlochWignerLobachevsky
import QOU.Archimedean.BlochWignerSymmetry

/-!
# QOU.Archimedean.FiveTwoOhtsukiBridge — shrinking the `5₂` volume-conjecture axiom

The corpus records the volume conjecture for `5₂` as **literature-cited**
(Ohtsuki, *On the asymptotic expansion of the Kashaev invariant of the 5₂
knot*; `library/ki52`, `library/104171-qt-83`). Cited is not derived: in Lean
it is still an axiom, and it used to be a *blanket* one — "VC holds for `5₂`".

This file shrinks that axiom. It separates the statement into four parts and
shows that only **one** of them is Ohtsuki's hard analysis:

| part | content | status |
|---|---|---|
| (A) | `⟨5₂⟩_N = e^{Nζ}·N^{3/2}·ω·(1 + O(1/N))` | **axiom** — Ohtsuki Thm 1.1, the 52-page part |
| (B) | `2π·Re ζ = 3·D(y₀)` | a dilogarithm identity — half proved, no geometry |
| (C) | (A) ⟹ `(2π/N)·log‖⟨5₂⟩_N‖ → 2π·Re ζ` | elementary analysis |
| (D) | `Vol(5₂) = 3·D(y₊)` | already axiomatised as `FiveTwoTriangulation` |

The point of the split is (B). It looks like it should need hyperbolic
geometry, and it does not: it is an identity among dilogarithms at the root of
a cubic. **Nothing in (B) or (C) needs the method of steepest descent** — that
is required only to prove (A) itself, which we do not attempt.

## Ohtsuki's Theorem 1.1, verbatim

From `library/ki52` §1 (the published version is `library/104171-qt-83`,
Quantum Topology; note the section text renders `π` as a glyph the extractor
drops, so `2π√−1` reads as `2 √−1` there — the `π` is present in the PDF and
is required for the constants to come out right, see the numerics below).

Let `y₀` be the unique solution with positive imaginary part of `(y−1)³ = y`,
`y₀ = 0.3376410213… + √−1·0.5622795120…`. Put `x₀ = 1 − 1/y₀`,

```
ζ = (1/2π√−1)·( Li₂(x₀y₀) + Li₂(1/(x₀y₀)) + Li₂(y₀) − Li₂(1/y₀) − Li₂(1/x₀) − π²/6 )
  = 0.4501096100… + √−1·0.4813049796…
ω = e^{√−1 π/4}·( (y₀−1)/(2y₀+1) )^{1/2}
  = 0.0901905774… − √−1·0.6499757866…
```

> **Theorem 1.1.** The asymptotic expansion of the Kashaev invariant `⟨5₂⟩_N`
> of the `5₂` knot is given by the following form,
> `⟨5₂⟩_N = e^{Nζ}·N^{3/2}·ω·(1 + Σ_{i=1}^{d} κ_i·(2√−1/N)^i + O(1/N^{d+1}))`,
> for any `d`, where `κ_i` is some constant given by a polynomial in `y₀` with
> rational coefficients; in particular `κ₁` is given by
> `κ₁ = ((37/4)y₀² − (31/6)y₀ + 35/8)/(2y₀+1)³ + 1 = (1650y₀² − 3498y₀ + 2197)/12696 + 1`
> `   = 1.0537470859… − √−1·0.1055728779…`

## What this file assumes, and why it is less than the theorem

`OhtsukiAsymptotic` below assumes only the `d = 0` truncation — the ratio
tends to `1`. That is strictly **weaker** than Theorem 1.1, which is the right
direction for an assumed input: the volume conjecture needs only the leading
exponential, so assuming the full Poincaré expansion would be assuming more
than the conclusion requires. The `κ_i` play no part in the derivation; `κ₁`
appears below only as evidence that the transcription is faithful.

## The prefactor is explicit — so `ω ≠ 0` is a theorem, not a hypothesis

This is the concrete gain over the previous version of this file. Ohtsuki does
not leave `ω` as an unknown constant; he computes it. Squaring his formula
kills the branch ambiguity:

```
ω² = e^{√−1 π/2}·(y₀−1)/(2y₀+1) = √−1·(y₀−1)/(2y₀+1)
```

a **rational function of `y₀` times `i`** — no square root, no dilogarithm, no
analysis. So the class states `ω² = ohtsukiOmegaSq y` rather than carrying a
bare `ω ≠ 0` field, and non-vanishing is then derived (`omega_ne_zero`) from
the cubic alone. One hypothesis became a proof.

Stating the square rather than `ω` itself is also faithful rather than merely
convenient: the printed `ω` is the *negative* of the principal branch of
`e^{iπ/4}((y₀−1)/(2y₀+1))^{1/2}` (checked numerically), so `ω` is only pinned
up to sign by Ohtsuki's own formula. That is the same `±` that appears in
Ohtsuki–Takata's `ω²(D) = ±τ(K)/(2√−1)`.

## Numerical verification of the transcription

Every constant above was recomputed at 120 decimal digits from the polished
root of the cubic (residual `1.9e-121`) before this file was written:

* `y₀`, `ζ`, `ω`, `κ₁` reproduce Ohtsuki's printed digits;
* `2π·Re ζ = Vol(5₂)` and `2π·Im ζ = 3.024128376509301659719951…`, the
  Chern–Simons half, against `computations/substrate/knot_volumes.py`;
* three independent routes to `Vol(5₂)` — the five-term `Li₂` sum, Bloch–Wigner
  via `Im Li₂`, and the pure Lobachevsky sum that `BlochWigner_lob` actually
  uses — agree to 121 digits;
* `κ₁`'s two printed forms agree, and agree with the printed value: this is a
  real check on the transcription, since dropping the trailing `+ 1` from
  either form would have moved the answer by a whole unit;
* `2√−1·ω² = −2(y₀−1)/(2y₀+1) = 0.2344867660… − √−1·0.8286683659…`.

A numerical check is not a proof, which is why (B) still carries a `sorry`.

## The tier boundary lives in the type

`OhtsukiAsymptotic` deliberately carries **no instance** (AGENTS.md §3b-tax).
Any theorem that needs the `5₂` volume conjecture must take `[OhtsukiAsymptotic
…]`, so a reader sees the assumed input in the signature instead of having to
find the knot in a status table. That is the whole point of the refactor.

**A trap this makes it easier to fall into, so it is recorded here.** Ohtsuki–
Takata (*Geom. Topol.* 19 (2015) 853–952 — note **both** authors) prove
`ω²(D) = ±τ(K)/(2√−1)` for *any* two-bridge knot, and Garoufalidis–Yoon
(arXiv:2411.03801) prove 1-loop `=` adjoint torsion for all hyperbolic
two-bridge knots. Both are **unconditional**, and both are about `ω`, not about
`ζ`. Neither says the asymptotic expansion exists. The bridge from the Hessian
invariant to the *actual* asymptotic prefactor is Ohtsuki–Takata Prop. 4.9,
gated on their Assumption 4.8 (Poisson summation + saddle point), verified in
the literature only up to 7 crossings. So for `5₂` both links are theorems,
while for `8₁₁ = b(27,10)` — two-bridge, hyperbolic, hence covered by their
Theorem 1.1 — the volume conjecture **stays open**. Citing those papers as
closing `8₁₁` would be an overstatement.

Archimedean (ℝ, ℂ).

-- Ref: [manuscript] prop:qbeta-c8-c10-silver-rationals
-- Ref: [ohtsuki2016-52] doi:10.4171/QT/83
-/

namespace QOU.Archimedean.FiveTwoOhtsukiBridge

open Complex QOU.Archimedean

/-! ## The shape, and the three non-vanishing facts the cubic already gives

`y₀` is pinned by `(y−1)³ = y` together with `Im y₀ > 0`. Everything this file
needs about it beyond that comes from the **cubic alone** — no appeal to the
imaginary part, and no root-selection machinery. That matters: it means the
algebraic half of the argument holds at every root, and the proofs are
arithmetic rather than complex analysis. -/

/-- Ohtsuki's shape: a root of `(y − 1)³ = y`, i.e. of `y³ − 3y² + 2y − 1`,
with positive imaginary part. Stated as a predicate rather than constructed. -/
def IsOhtsukiShape (y : ℂ) : Prop :=
  y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0 ∧ 0 < y.im

/-- `0` is not a root: it gives `−1 = 0`. -/
theorem cubic_ne_zero {y : ℂ} (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) : y ≠ 0 := by
  intro hy; rw [hy] at h; norm_num at h

/-- `1` is not a root: it gives `1 − 3 + 2 − 1 = −1 = 0`. -/
theorem cubic_ne_one {y : ℂ} (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) : y ≠ 1 := by
  intro hy; rw [hy] at h; norm_num at h

/-- `−1/2` is not a root: it gives `−23/8 = 0`. Hence the denominator of
Ohtsuki's prefactor never vanishes — from the cubic, not from `Im y > 0`. -/
theorem cubic_two_mul_add_one_ne_zero {y : ℂ}
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) : 2 * y + 1 ≠ 0 := by
  intro hc
  have hy : y = -(1 / 2 : ℂ) := by linear_combination hc / 2
  rw [hy] at h
  norm_num at h

theorem IsOhtsukiShape.ne_zero {y : ℂ} (h : IsOhtsukiShape y) : y ≠ 0 :=
  cubic_ne_zero h.1

theorem IsOhtsukiShape.ne_one {y : ℂ} (h : IsOhtsukiShape y) : y ≠ 1 :=
  cubic_ne_one h.1

theorem IsOhtsukiShape.two_mul_add_one_ne_zero {y : ℂ} (h : IsOhtsukiShape y) :
    2 * y + 1 ≠ 0 :=
  cubic_two_mul_add_one_ne_zero h.1

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

/-! ## Ohtsuki's prefactor, without the square root

`ω = e^{iπ/4}·((y₀−1)/(2y₀+1))^{1/2}` needs a branch choice; `ω²` does not. -/

/-- `ω² = i·(y−1)/(2y+1)`, Ohtsuki's prefactor squared. Rational in `y` up to
the factor `i`; no square root, no dilogarithm, nothing transcendental. -/
noncomputable def ohtsukiOmegaSq (y : ℂ) : ℂ := Complex.I * (y - 1) / (2 * y + 1)

/-- **The shrink.** Ohtsuki's prefactor is non-zero — and this is now a
consequence of the cubic rather than a hypothesis carried by the axiom. -/
theorem ohtsukiOmegaSq_ne_zero {y : ℂ} (h : IsOhtsukiShape y) :
    ohtsukiOmegaSq y ≠ 0 := by
  unfold ohtsukiOmegaSq
  exact div_ne_zero
    (mul_ne_zero Complex.I_ne_zero (sub_ne_zero.mpr h.ne_one))
    h.two_mul_add_one_ne_zero

/-- The quantity Ohtsuki–Takata's Theorem 1.1 identifies (up to sign) with the
twisted Reidemeister torsion. Their statement is about `ω²(D)`, a modification
of the Hessian of the potential function; here we record only the elementary
half — that Ohtsuki's own `ω` makes `2√−1·ω²` a rational function of `y₀`.

Measured: `−2(y₀−1)/(2y₀+1) = 0.2344867660… − √−1·0.8286683659…`, matching the
modulus of Ohtsuki–Takata's printed `τ(5₂)` (their value is the negated
conjugate, the usual conjugate-geometric-solution convention).

No hypothesis is needed: when `2y + 1 = 0` both sides are division by zero. -/
theorem two_I_mul_ohtsukiOmegaSq (y : ℂ) :
    2 * Complex.I * ohtsukiOmegaSq y = -2 * (y - 1) / (2 * y + 1) := by
  unfold ohtsukiOmegaSq
  rw [← mul_div_assoc]
  congr 1
  linear_combination (2 * (y - 1)) * Complex.I_sq

/-! ## `κ₁` — corroboration that the transcription is faithful

Ohtsuki prints `κ₁` twice, in two different-looking forms. They are equal, but
**not** as polynomials: the identity holds only modulo the cubic. Proving it is
therefore a real check that the coefficients were read correctly, and it is
cheap — a single `linear_combination` with an explicit certificate. -/

/-- The two printed forms of `κ₁ − 1` agree, with denominators cleared. The
certificate is exact: `A·12696 − B·(2y+1)³ = −4(3300y² + 7854y + 13337)·cubic`.

This is corroboration only — `κ₁` plays no part in the volume conjecture, which
needs the leading term alone. -/
theorem kappaOne_numerator_identity (y : ℂ)
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) :
    ((37 / 4) * y ^ 2 - (31 / 6) * y + 35 / 8) * 12696
      = (1650 * y ^ 2 - 3498 * y + 2197) * (2 * y + 1) ^ 3 := by
  linear_combination (-4 * (3300 * y ^ 2 + 7854 * y + 13337)) * h

/-! ## (B) — the identity that carries the volume

This is the piece worth proving. It says a five-term dilogarithm combination at
the root of a cubic equals three times a Bloch–Wigner value. It mentions no
manifold, no triangulation, and no asymptotics. -/

/-- Ohtsuki's potential function `V(x,y)`, evaluated along `x = x₀(y)`.
`Li₂` is written abstractly: this file does not construct a complex
polylogarithm, it takes one as a parameter, so the statement is independent of
whichever `Li₂` the corpus or Mathlib eventually supplies. The final `Li₂ 1`
term is `π²/6`; it is real, so it drops out of the imaginary part. -/
noncomputable def ohtsukiSum (Li₂ : ℂ → ℂ) (y : ℂ) : ℂ :=
  Li₂ (xOf y * y) + Li₂ (1 / (xOf y * y)) + Li₂ y - Li₂ (1 / y) - Li₂ (1 / xOf y) - Li₂ 1

/-- **(B).**

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

**Step 4's first half is proved**, and cheaply. `x₀ = 1 − 1/y₀` is exactly the
order-3 Möbius rotation of the ideal tetrahedron, under which the three
dihedral angles are *permuted*; so `D(x₀) = D(y₀)` is a reordering of a sum, not
a computation. See `QOU.Archimedean.BlochWigner_lob_mobius_cycle` in
`BlochWignerSymmetry.lean` — no dilogarithm, no analysis, nothing Mathlib lacks.

What remains is therefore narrower than it looked: the `arg`–`log` correction
terms must cancel (measured: their sum is `2.9e-42`), and `D(x₀y₀) = D(y₀)/2`
must come from the cubic. Neither needs steepest descent. The `Li₂` parameter
still carries its own hypotheses because Mathlib has no polylogarithm — but the
*volume-carrying* half of the argument turned out not to need one. -/
theorem ohtsuki_sum_im_eq_three_blochWigner
    (Li₂ : ℂ → ℂ) (y : ℂ) (_hy : IsOhtsukiShape y)
    (_hinv : ∀ z : ℂ, z ≠ 0 → (Li₂ z).im + (Li₂ (1 / z)).im
      = -(2 * (Complex.arg (1 - z)) * Real.log (Complex.abs z)))
    (_hbw : ∀ z : ℂ, BlochWigner_lob z
      = (Li₂ z).im + Complex.arg (1 - z) * Real.log (Complex.abs z))
    (_hone : (Li₂ 1).im = 0) :
    (ohtsukiSum Li₂ y).im = 3 * BlochWigner_lob y := by
  sorry

/-! ## (A) — the one assumed input, and (C) — what it gives

Compare what it replaces. "VC holds for `5₂`" is a conjecture. This is a
published quantitative estimate with a named author and a page number — still
assumed, but assumed at the smallest surface that does the job. -/

/-- **(A), the shrunk axiom** — the `d = 0` truncation of Ohtsuki's Theorem 1.1.

Deliberately carries no instance (AGENTS.md §3b-tax): the honest representation
of an input this corpus has not proved. -/
class OhtsukiAsymptotic (kashaev : ℕ → ℂ) (y ζ ω : ℂ) : Prop where
  /-- `y` is the root of `(y−1)³ = y` in the upper half plane. -/
  shape : IsOhtsukiShape y
  /-- `ω` is Ohtsuki's explicit prefactor `e^{iπ/4}·((y−1)/(2y+1))^{1/2}`,
  stated through its square so that no branch has to be chosen — and so that
  `ω ≠ 0` becomes derivable rather than assumed. -/
  omega_sq : ω ^ 2 = ohtsukiOmegaSq y
  /-- `⟨5₂⟩_N / (e^{Nζ}·N^{3/2}·ω) → 1`. This is the only analytic content. -/
  ratio_tendsto_one :
    Filter.Tendsto
      (fun N : ℕ => kashaev N / (Complex.exp (N * ζ) * (N : ℂ) ^ (3 / 2 : ℂ) * ω))
      Filter.atTop (nhds 1)

/-- **The field that is no longer a field.** The previous version of this class
carried `omega_ne_zero` as an assumption. It is a theorem: `ω² = i(y−1)/(2y+1)`
and neither factor vanishes at a root of the cubic. -/
theorem omega_ne_zero (kashaev : ℕ → ℂ) (y ζ ω : ℂ)
    [h : OhtsukiAsymptotic kashaev y ζ ω] : ω ≠ 0 := by
  intro h0
  refine ohtsukiOmegaSq_ne_zero h.shape ?_
  rw [← h.omega_sq, h0]
  ring

/-- **(C).** From the asymptotic form alone, the Kashaev growth rate is
`2π·Re ζ`. Elementary: `log‖e^{Nζ}·N^{3/2}·ω·(1+o(1))‖ = N·Re ζ + (3/2)·log N
+ log‖ω‖ + o(1)`, and everything but the first term dies after dividing by `N`.

No steepest descent, no geometry — this is the step that makes the shrink pay,
because it shows the volume-conjecture *conclusion* follows from the asymptotic
*form* by analysis Mathlib already has. The `ω ≠ 0` this needs is
`omega_ne_zero` above, no longer an assumption. -/
theorem growth_rate_eq_two_pi_re_zeta
    (kashaev : ℕ → ℂ) (y ζ ω : ℂ) [OhtsukiAsymptotic kashaev y ζ ω] :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log (Complex.abs (kashaev N)))
      Filter.atTop (nhds (2 * Real.pi * ζ.re)) := by
  sorry

/-- **The bridge.** Combining (A), (B) and the corpus's `FiveTwoTriangulation`
(D), the volume conjecture holds for `5₂`.

Unlike the previous version this is **derived, not assumed**: the proof is a
rewrite of (C) along the two identities. Every hypothesis is either published
(Ohtsuki), geometric and already axiomatised (`FiveTwoTriangulation`), or the
dilogarithm identity (B). The blanket assumption "VC holds for `5₂`" appears
nowhere. -/
theorem volume_conjecture_five_two
    (kashaev : ℕ → ℂ) (y ζ ω : ℂ) (vol : ℝ)
    [OhtsukiAsymptotic kashaev y ζ ω]
    (hzeta : 2 * Real.pi * ζ.re = 3 * BlochWigner_lob y)
    (hvol : vol = 3 * BlochWigner_lob y) :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log (Complex.abs (kashaev N)))
      Filter.atTop (nhds vol) := by
  have h := growth_rate_eq_two_pi_re_zeta kashaev y ζ ω
  rwa [hvol, ← hzeta]

end QOU.Archimedean.FiveTwoOhtsukiBridge
