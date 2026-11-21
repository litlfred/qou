import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Archimedean.BlochWignerLobachevsky
import QOU.Archimedean.BlochWignerSymmetry
import QOU.MathlibExt.ExponentialGrowthRate
import QOU.Knot.KummerRadial

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
| (B) | `2π·Re ζ = 3·D(y₀)` | **PROVED**, sorry-free — no geometry |
| (C) | (A) ⟹ `(2π/N)·log‖⟨5₂⟩_N‖ → 2π·Re ζ` | **PROVED**, sorry-free |
| (D) | `Vol(5₂) = 3·D(y₊)` | already axiomatised as `FiveTwoTriangulation` |

The point of the split is (B). It looks like it should need hyperbolic
geometry, and it does not: it is an identity among dilogarithms at the root of
a cubic. **Nothing in (B) or (C) needs the method of steepest descent** — that
is required only to prove (A) itself, which we do not attempt.

**This file has no `sorry`.** `volume_conjecture_five_two_wired` derives the
volume conjecture for `5₂` from (A), (D) and the statement that `Li₂` is a
dilogarithm, and nothing else — (B) and the identification of `ζ` are theorems
here, not hypotheses. Its two class arguments are the honest residue:
`OhtsukiAsymptotic` is Ohtsuki's published analysis, `FiveTwoTriangulation` is
Thurston/SnapPea, and neither has an instance. **They are not instance-free for
the same reason** — see the ⚠ on `FiveTwoTriangulation`'s own declaration, which
is satisfiable at a derived `vol`, where `OhtsukiAsymptotic` is not satisfiable
at all. `exists_isOhtsukiShape` below shows the shape hypothesis both of them
carry is at least met.

The dilogarithm hypothesis is stated at the **five points** the proof applies it
to (`IsKummerAtOhtsukiArgs`), not on a half plane. Two are in the upper half
plane, where `QOU.Knot.KummerRadial.kummer` already proves Kummer's identity;
`IsKummerAtOhtsukiArgs.of_upper_half_plane` reaches the other three from those,
given only that `Li₂` commutes with conjugation off the real axis. So the file
no longer depends on continuing `kummer` across the branch cut.

⚠ **(D) is stated at the conjugate-inverse shape, and that is not cosmetic.**
`FiveTwoTriangulation` lives at `y₊`, the upper-half-plane root of the *saddle*
cubic `y³ − 2y² + 3y − 1`; Ohtsuki's `y₀` is a root of the *reciprocal* cubic
`y³ − 3y² + 2y − 1`. They are different numbers —
`y₀ = 0.3376… + 0.5623…i` against `y₊ = 0.7849… + 1.3071…i` — related by
`y₊ = conj (1/y₀)` (checked to 40 digits, difference exactly `0`). Writing the
instance at `y₀` would be wrong. `conj_inv_is_five_two_shape` proves the shape
supplied is admissible, and `BlochWigner_lob_conj_inv` proves the two `D` values
agree, so the reconciliation is derived rather than asserted.

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

A numerical check is not a proof. It was, however, the thing that caught the
error: the `hinv` hypothesis (B) used to carry was refuted by exactly this kind
of check before any Lean was written — see the ⚠ block on
`ohtsuki_sum_im_eq_three_blochWigner`. Numbers are not evidence *for* a
theorem; they are excellent evidence *against* a wrong one.

Both (B) and (C) are now proved.

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

-- Ref: [leitner2026] prop:qbeta-c8-c10-silver-rationals
-- Ref: [ohtsuki2016] doi:10.4171/QT/83
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

/-- **`IsOhtsukiShape` is inhabited.** Bean `qou-6x46`.

Every theorem in this file takes `IsOhtsukiShape y` as a hypothesis, directly or
as the `shape` field of `OhtsukiAsymptotic`, and until this lemma **nothing in
the corpus showed that hypothesis was satisfiable** — `exact?` could not close
`∃ y, IsOhtsukiShape y` on 2026-08-31. A conditional theorem whose condition is
not known to be met is a different and weaker object than one conditional on a
published result, and the corpus's vacuity audits exist to keep the two apart.

**Constructed, not counted.** No root-multiset or discriminant machinery:

1. the intermediate value theorem gives the real root `t ∈ [2.3, 2.4]`, since
   `p(2.3) = −0.103 < 0 < 0.344 = p(2.4)`;
2. dividing out `(y − t)` leaves `y² + (t−3)y + (t²−3t+2)`, whose discriminant is
   `−(3t² − 6t − 1)` — and `3t² − 6t − 1 > 0` for `t ≥ 2.3`, which is exactly why
   the bracket is taken there rather than at the obvious `[2,3]`: at `t = 2`
   the quantity is `−1`, so the coarse bracket does not decide the sign;
3. its two roots are then written down, and the one with `+√d` has `Im > 0`.

The division in step 2 is legitimate only modulo the cubic — the cofactor's
constant term is `1/t`, and `t² − 3t + 2 = 1/t` *is* `p(t) = 0` rearranged, so
the whole identity is one `linear_combination` against `ht`. -/
theorem exists_isOhtsukiShape : ∃ y : ℂ, IsOhtsukiShape y := by
  -- (1) the real root, by IVT on a bracket tight enough for step (2)
  obtain ⟨t, htmem, ht⟩ : ∃ t ∈ Set.Icc (2.3 : ℝ) 2.4,
      t ^ 3 - 3 * t ^ 2 + 2 * t - 1 = 0 := by
    have hcont : ContinuousOn (fun u : ℝ => u ^ 3 - 3 * u ^ 2 + 2 * u - 1)
        (Set.Icc (2.3 : ℝ) 2.4) := by fun_prop
    have hsub := intermediate_value_Icc (by norm_num : (2.3 : ℝ) ≤ 2.4) hcont
    have h0 : (0 : ℝ) ∈ Set.Icc ((2.3 : ℝ) ^ 3 - 3 * (2.3 : ℝ) ^ 2 + 2 * (2.3 : ℝ) - 1)
        ((2.4 : ℝ) ^ 3 - 3 * (2.4 : ℝ) ^ 2 + 2 * (2.4 : ℝ) - 1) := by norm_num
    obtain ⟨t, htmem, hteq⟩ := hsub h0
    exact ⟨t, htmem, hteq⟩
  obtain ⟨ht23, ht24⟩ := htmem
  -- (2) the cofactor's discriminant is strictly negative on this bracket
  have hd : 0 < 3 * t ^ 2 - 6 * t - 1 := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ t) (by linarith : (0 : ℝ) ≤ t - 2.3)]
  set s : ℝ := Real.sqrt (3 * t ^ 2 - 6 * t - 1) with hsdef
  have hspos : 0 < s := Real.sqrt_pos.mpr hd
  have hs2 : s ^ 2 = 3 * t ^ 2 - 6 * t - 1 := Real.sq_sqrt hd.le
  have hs2c : ((s : ℝ) : ℂ) ^ 2 = 3 * ((t : ℝ) : ℂ) ^ 2 - 6 * ((t : ℝ) : ℂ) - 1 := by
    exact_mod_cast congrArg (fun r : ℝ => ((r : ℝ) : ℂ)) hs2
  have htc : ((t : ℝ) : ℂ) ^ 3 - 3 * ((t : ℝ) : ℂ) ^ 2 + 2 * ((t : ℝ) : ℂ) - 1 = 0 := by
    exact_mod_cast congrArg (fun r : ℝ => ((r : ℝ) : ℂ)) ht
  -- (3) the root with positive imaginary part
  set y : ℂ := ((3 - t : ℝ) : ℂ) / 2 + ((s : ℝ) : ℂ) / 2 * Complex.I with hydef
  have hq : y ^ 2 + (((t : ℝ) : ℂ) - 3) * y + (((t : ℝ) : ℂ) ^ 2 - 3 * ((t : ℝ) : ℂ) + 2)
      = 0 := by
    rw [hydef]
    push_cast
    linear_combination (((s : ℝ) : ℂ) ^ 2 / 4) * Complex.I_sq - (1 / 4 : ℂ) * hs2c
  refine ⟨y, ?_, ?_⟩
  · linear_combination (y - ((t : ℝ) : ℂ)) * hq + htc
  · rw [hydef]
    simp only [Complex.add_im, Complex.div_im, Complex.mul_im, Complex.ofReal_re,
      Complex.ofReal_im, Complex.I_re, Complex.I_im, Complex.mul_re, Complex.div_re,
      Complex.normSq_ofNat]
    norm_num
    linarith

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

/-! ### Everything is a power of `w = 1 − y`

Ohtsuki's five arguments `x₀y₀`, `1/(x₀y₀)`, `y₀`, `1/y₀`, `1/x₀` look like five
unrelated points. They are not. Put `w = 1 − y`. The cubic `(y−1)³ = y` says
exactly `w³ = w − 1`, and then

```
x₀y₀ = −w        y₀ = −w³        x₀ = 1/w²        1 − 1/x₀ = 1/w
```

so **every** argument is `±w^k` for `k ∈ {−2, −1, 1, 3}`. That is what makes the
correction terms collapse: each `log‖·‖` is an integer multiple of `log‖w‖` and
each `arg` is an integer multiple of `arg w`, and the integers cancel.

These are all pure field identities modulo the cubic — `linear_combination`
certificates, no analysis. -/

/-- The cubic recentred at `w = 1 − y`: `w³ − w + 1 = 0`, i.e. `w³ = w − 1`.

Note this is the *plastic-number* cubic with a sign: `u³ = u + 1` for `u = y−1`.
The `5₂` shape field is ℚ(`u`), the complex cubic field of discriminant `−23` —
the smallest `|disc|` there is, which is why `Vol(5₂)` is the smallest volume in
the Zagier tables. -/
theorem cubic_one_sub {y : ℂ} (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) :
    (1 - y) ^ 3 - (1 - y) + 1 = 0 := by linear_combination -h

/-- `y = −w³`. The volume-carrying consequence: `‖y‖ = ‖w‖³`, so `log‖y‖` is
*three* times `log‖w‖` — the `3` in `3·D(y₀)` and the `3` in the coefficient
bookkeeping are the same `3`. -/
theorem eq_neg_one_sub_cube {y : ℂ} (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) :
    y = -(1 - y) ^ 3 := by linear_combination -h

/-- `x₀·y₀ = y₀ − 1 = −w`. No cubic needed — this is just `(1 − 1/y)·y`.

Worth stating on its own: Ohtsuki writes `Li₂(x₀y₀)`, and the product is a
*translate* of `y₀`, not a new transcendental. -/
theorem xOf_mul_self (y : ℂ) (hy : y ≠ 0) : xOf y * y = y - 1 := by
  unfold xOf; field_simp

/-- `x₀ = 1/w²`. This is the cubic doing real work: `x₀ = (y−1)/y` and `y =
(y−1)³`, so the `(y−1)` cancels down to `(y−1)^{-2}`.

The `linear_combination` certificate is `+h`, not `−h`: `field_simp` normalises
the cleared equation with the *opposite* orientation to the one this file's
other certificates use, and the typechecker rejects the sign immediately. Worth
recording only because the same wrong guess costs a compile every time. -/
theorem xOf_eq_one_div_sq {y : ℂ} (hy : y ≠ 0) (hy1 : y ≠ 1)
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) : xOf y = 1 / (1 - y) ^ 2 := by
  have hw : (1 : ℂ) - y ≠ 0 := sub_ne_zero.mpr (Ne.symm hy1)
  unfold xOf
  field_simp
  linear_combination h

/-- `1 − 1/x₀ = 1/w`, and — a small surprise — **the cubic is not needed**.

`x₀ = 1 − 1/y` is the order-3 Möbius map, so `1 − 1/x₀` is that map applied
twice, which the 3-cycle already evaluates: it is `one_sub_inv_mobius` in
`BlochWignerSymmetry.lean`, proved there for every `y ∉ {0,1}`. An earlier draft
routed this through `w³ = w − 1` and needed the root; that was strictly more
than the fact costs. -/
theorem one_sub_one_div_xOf {y : ℂ} (hy : y ≠ 0) (hy1 : y ≠ 1) :
    1 - 1 / xOf y = 1 / (1 - y) :=
  one_sub_inv_mobius y hy hy1

/-! ### `Re(1 − y₀) > 0` — the one place a *root* is analysed, not the cubic

Everything above holds at all three roots. The `arg` bookkeeping does not: it
needs to know which quadrant `w = 1 − y` sits in, and that is a fact about the
complex roots specifically.

The elimination is elementary. Writing `w = s + it` and separating `w³ − w + 1 =
0` into real and imaginary parts gives, when `t ≠ 0`,

```
t² = 3s² − 1          (imaginary part, after dividing by t)
8s³ − 2s − 1 = 0      (real part, after substituting)
```

and the second has no root with `s ≤ 0`, because for `r = −s ≥ 0`

```
8r³ − 2r + 1 = 2r(2r−1)² + 8(r − 1/4)² + 1/2 > 0.
```

That decomposition is the whole proof, and it is what `nlinarith` is fed. -/

/-- **`Re(1 − y) > 0` at every non-real root of Ohtsuki's cubic.**

Equivalently `Re y < 1` — measured, `Re y₀ = 0.3376…`. This pins `w = 1 − y` to
the fourth quadrant (together with `Im w = −Im y < 0`), hence
`arg w ∈ (−π/2, 0)`, which is what every `arg` computation below rests on.

The hypothesis is `y.im ≠ 0`, not `0 < y.im`: the statement is about the
conjugate *pair*, and using less than is available keeps the reason visible —
the real root `y = 2.3247…` genuinely has `Re y > 1`, so some hypothesis
excluding it is unavoidable. -/
theorem one_sub_re_pos {y : ℂ} (him : y.im ≠ 0)
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) : 0 < ((1 : ℂ) - y).re := by
  have hw : ((1 : ℂ) - y) ^ 3 - (1 - y) + 1 = 0 := cubic_one_sub h
  set w : ℂ := 1 - y with hwdef
  have hwim : w.im ≠ 0 := by simpa [hwdef] using him
  have hre : (w ^ 3 - w + 1).re = 0 := by rw [hw]; simp
  have him' : (w ^ 3 - w + 1).im = 0 := by rw [hw]; simp
  simp only [Complex.sub_re, Complex.add_re, Complex.one_re, Complex.sub_im, Complex.add_im,
    Complex.one_im, pow_succ, pow_zero, one_mul, Complex.mul_re, Complex.mul_im] at hre him'
  set s := w.re
  set t := w.im
  -- imaginary part, divided by `t ≠ 0`
  have ht2 : t ^ 2 = 3 * s ^ 2 - 1 := by
    have hfac : t * (3 * s ^ 2 - t ^ 2 - 1) = 0 := by linear_combination him'
    rcases mul_eq_zero.mp hfac with h0 | h0
    · exact absurd h0 hwim
    · linarith
  -- real part, with `t²` eliminated
  have hs : 8 * s ^ 3 - 2 * s - 1 = 0 := by linear_combination -hre - 3 * s * ht2
  by_contra hcon
  push_neg at hcon
  nlinarith [mul_nonneg (neg_nonneg.mpr hcon) (sq_nonneg (2 * s + 1)), sq_nonneg (4 * s + 1),
    sq_nonneg s, sq_nonneg (2 * s + 1)]

/-! ### Kummer's identity is used at five points, not on a half plane

Part (B) below applies Kummer's identity exactly five times, at the five
non-unit arguments of `ohtsukiSum`. Stating the hypothesis as
`∀ z, z.im ≠ 0 → …`, as this file did until now, therefore charged the whole
punctured plane to a hypothesis that `QOU.Knot.KummerRadial.kummer` proves only
for `Im z > 0` — and made "extend `kummer` across the real axis" look like the
blocker. Naming the five points instead does three things: it makes the
dependency auditable, it makes it dischargeable one point at a time, and it
reduces the reflection step to a *pointwise* symmetry of `Li₂`.

Measured at Ohtsuki's shape `y₀ = 0.33764102137762698702 + 0.5622795120623012439i`
(`mpmath`, 40 dps; `x₀y₀ = y₀ − 1` exactly, residual `0.0`):

```
z                        Im z       dist to [1,∞)    half plane
y₀                    +0.5622795       0.8688370        upper
x₀y₀ = y₀ − 1         +0.5622795       1.7548777        upper
1/y₀                  −1.3071413       1.3247180        lower
1/x₀                  −0.7448618       1.1509639        lower
1/(x₀y₀)              −0.7448618       2.0198009        lower
```

Three of the five are below the axis — that is the entire gap — and none is
within `0.86` of the branch cut, so nothing here is a delicate branch question.

`IsKummerAtOhtsukiArgs.of_forall` recovers the old `∀`-form, so no caller that
already had a half-plane statement is worse off. `of_upper_half_plane` is the
new content: **conjugation symmetry of `Li₂` off the real axis is enough**, and
no continuation across the cut is required, because `kummer` is then only ever
evaluated where it is already proved.

**Is the conjugation hypothesis satisfiable?** (The check the false `hinv` below
should have been given.) It is stated at `w.im ≠ 0` and *must* be: the
unrestricted `∀ w, Li₂(w̄) = conj (Li₂ w)` is false for the principal branch on
the cut, where it degenerates to `Li₂ w ∈ ℝ` — at `w = 5`, `mpmath` gives
`Li₂(5) = 1.78371916127 − 5.05619832211i`. Off the axis it holds exactly:
residual `0.0` at 40 dps at all five points above, and still `0.0` at `1e−7`
from the cut on both sides of `Re = 5`. -/

/-- **Kummer's identity at one point**: the Λ-built `BlochWigner_lob` and the
`Li₂`-built Bloch–Wigner function agree at `z`.

Split out of the old `∀`-hypothesis so the bridge can name the points it uses.
Not a convenience abbreviation — `IsKummerAtOhtsukiArgs` is the honest statement
of everything the `5₂` bridge assumes about a dilogarithm away from `z = 1`. -/
def IsKummerAt (Li₂ : ℂ → ℂ) (z : ℂ) : Prop :=
  BlochWigner_lob z = (Li₂ z).im + Complex.arg (1 - z) * Real.log ‖z‖

/-- **The five points.** Exactly the Kummer instances
`ohtsuki_sum_im_eq_three_blochWigner` consumes, one per non-unit argument of
`ohtsukiSum`.

`z = 1` is deliberately absent: it is handled by the separate `hone`, because
there the identity holds only through Lean's `arg 0 = 0` convention. -/
structure IsKummerAtOhtsukiArgs (Li₂ : ℂ → ℂ) (y : ℂ) : Prop where
  /-- at `x₀y₀ = y₀ − 1` — upper half plane. -/
  at_xy : IsKummerAt Li₂ (xOf y * y)
  /-- at `1/(x₀y₀)` — lower half plane. -/
  at_inv_xy : IsKummerAt Li₂ (1 / (xOf y * y))
  /-- at `y₀` — upper half plane. -/
  at_y : IsKummerAt Li₂ y
  /-- at `1/y₀` — lower half plane. -/
  at_inv_y : IsKummerAt Li₂ (1 / y)
  /-- at `1/x₀` — lower half plane. -/
  at_inv_x : IsKummerAt Li₂ (1 / xOf y)

/-- `x₀ = 1 − 1/y` is off the real axis whenever `y` is: `Im x₀ = −Im (1/y)`. -/
theorem xOf_im_ne_zero {y : ℂ} (hy : y.im ≠ 0) : (xOf y).im ≠ 0 := by
  have hx : (xOf y).im = -(1 / y).im := by unfold xOf; simp
  rw [hx]
  exact neg_ne_zero.mpr (one_div_im_ne_zero hy)

/-- `x₀y₀ = y₀ − 1` is off the real axis at any Ohtsuki shape — the shift is
real, so it moves nothing. -/
theorem xOf_mul_self_im_ne_zero {y : ℂ} (hy : IsOhtsukiShape y) :
    (xOf y * y).im ≠ 0 := by
  rw [xOf_mul_self y hy.ne_zero]
  simpa using ne_of_gt hy.2

/-- **The old half-plane hypothesis still discharges the new one.** Anything
that could supply `∀ z, z.im ≠ 0 → …` to this bridge is unaffected by the
weakening. -/
theorem IsKummerAtOhtsukiArgs.of_forall {Li₂ : ℂ → ℂ} {y : ℂ} (hy : IsOhtsukiShape y)
    (hbw : ∀ z : ℂ, z.im ≠ 0 → IsKummerAt Li₂ z) :
    IsKummerAtOhtsukiArgs Li₂ y :=
  have hyim : y.im ≠ 0 := ne_of_gt hy.2
  have hxyim : (xOf y * y).im ≠ 0 := xOf_mul_self_im_ne_zero hy
  have hxim : (xOf y).im ≠ 0 := xOf_im_ne_zero hyim
  { at_xy := hbw _ hxyim
    at_inv_xy := hbw _ (one_div_im_ne_zero hxyim)
    at_y := hbw _ hyim
    at_inv_y := hbw _ (one_div_im_ne_zero hyim)
    at_inv_x := hbw _ (one_div_im_ne_zero hxim) }

/-- **Kummer transports across the real axis by conjugation.**

Every ingredient of the identity is odd under `z ↦ z̄` in the same way:
`D(z̄) = −D(z)` (`BlochWigner_lob_conj`), `Im Li₂(z̄) = −Im Li₂(z)` (the
hypothesis), `arg(1 − z̄) = −arg(1 − z)` (`arg_conj_of_im_ne_zero`, and
`1 − z` is off the axis exactly when `z` is), and `‖z̄‖ = ‖z‖`. So the identity
at `z̄` is `(−1)×` the identity at `z`, and `linear_combination -h` is the
whole proof.

The hypothesis is one equation at one point, not a functional equation: this is
Schwarz reflection reduced to what the bridge actually needs. -/
theorem isKummerAt_of_conj {Li₂ : ℂ → ℂ} {z : ℂ} (hz : z.im ≠ 0)
    (hconj : Li₂ ((starRingEnd ℂ) z) = (starRingEnd ℂ) (Li₂ z))
    (h : IsKummerAt Li₂ ((starRingEnd ℂ) z)) :
    IsKummerAt Li₂ z := by
  have h1z : ((1 : ℂ) - z).im ≠ 0 := by simpa using hz
  have hc1 : (1 : ℂ) - (starRingEnd ℂ) z = (starRingEnd ℂ) (1 - z) := by simp
  have hnorm : ‖(starRingEnd ℂ) z‖ = ‖z‖ := by simp
  unfold IsKummerAt at h ⊢
  rw [BlochWigner_lob_conj hz, hconj, hc1, arg_conj_of_im_ne_zero h1z, hnorm,
    Complex.conj_im] at h
  linear_combination -h

/-- **Kummer on the upper half plane, plus conjugation symmetry, gives Kummer
off the real axis.**

This is *not* an analytic continuation: `hupper` is only ever evaluated where it
already holds, and the lower half plane is reached by the algebraic identity
above. `hconj` is restricted to `w.im ≠ 0` because the unrestricted form is
false on the cut (see the section docstring). -/
theorem isKummerAt_of_upper {Li₂ : ℂ → ℂ} {z : ℂ} (hz : z.im ≠ 0)
    (hconj : ∀ w : ℂ, w.im ≠ 0 → Li₂ ((starRingEnd ℂ) w) = (starRingEnd ℂ) (Li₂ w))
    (hupper : ∀ w : ℂ, 0 < w.im → IsKummerAt Li₂ w) :
    IsKummerAt Li₂ z := by
  rcases hz.lt_or_lt with hlt | hgt
  · refine isKummerAt_of_conj hz (hconj z hz) (hupper _ ?_)
    simpa using hlt
  · exact hupper z hgt

/-- **What the `5₂` bridge really needs of a dilogarithm.** Kummer's identity on
the *upper* half plane — which `QOU.Knot.KummerRadial.kummer` proves — together
with conjugation symmetry off the real axis.

This retires "extend `kummer` across the real axis by Schwarz reflection" as the
blocker: it is sufficient to know that `Li₂` commutes with conjugation, which is
a statement about `Li₂`'s own series/integral representation and needs no
continuation. -/
theorem IsKummerAtOhtsukiArgs.of_upper_half_plane {Li₂ : ℂ → ℂ} {y : ℂ}
    (hy : IsOhtsukiShape y)
    (hconj : ∀ w : ℂ, w.im ≠ 0 → Li₂ ((starRingEnd ℂ) w) = (starRingEnd ℂ) (Li₂ w))
    (hupper : ∀ w : ℂ, 0 < w.im → IsKummerAt Li₂ w) :
    IsKummerAtOhtsukiArgs Li₂ y :=
  IsKummerAtOhtsukiArgs.of_forall hy fun _ hz => isKummerAt_of_upper hz hconj hupper

/-- **(B) — PROVED.**

`Im` of Ohtsuki's five-term dilogarithm sum is `3·D(y₀)`, with no geometry and
no asymptotics.

## What the hypotheses are, and why they are not the theorem in disguise

Mathlib has no polylogarithm, so `Li₂` is a parameter. It is constrained by
exactly two facts, both of which the corpus proves for its **own** dilogarithm
`QOU.MathlibExt.cLiTwoExt`:

* `hbw` is **Kummer's identity**, `D(z) = Im Li₂(z) + arg(1−z)·log‖z‖` — the
  statement that the Λ-built `BlochWigner_lob` and the `Li₂`-built Bloch–Wigner
  function are the same function — asserted at the **five points** this proof
  applies it to and nowhere else (`IsKummerAtOhtsukiArgs`, above).
  `QOU.Knot.KummerRadial.kummer` proves it sorry-free for `Im z > 0`, which
  covers two of the five; the other three are `1/y₀`, `1/x₀` and `1/(x₀y₀)`, in
  the *lower* half plane, and `IsKummerAtOhtsukiArgs.of_upper_half_plane`
  reaches them from the upper ones given only that `Li₂` commutes with
  conjugation off the real axis. So no continuation across the cut is needed.
* `hone` is `Im Li₂(1) = 0`, i.e. `Li₂(1) = π²/6` is real. It is stated
  separately because `hbw` is deliberately *not* assumed at `z = 1`, where
  `arg(1 − z) = arg 0` and the identity holds only through Lean's `arg 0 = 0`
  convention.

Neither hypothesis mentions `5₂`, the cubic, or a volume.

## ⚠ The hypothesis this replaces was FALSE

Until this proof was written the statement also carried

```
hinv : ∀ z ≠ 0, Im Li₂(z) + Im Li₂(1/z) = −2·arg(1−z)·log‖z‖
```

advertised as "the inversion formula". **It is not the inversion formula and it
is not true.** Euler's inversion `Li₂(z) + Li₂(1/z) = −π²/6 − ½log(−z)²` has
imaginary part `−log‖z‖·arg(−z)`, and `arg(−z) ≠ 2·arg(1−z)`. Measured against
`mpmath` at 40 digits, the discharged form is off by `−2.97e-1` at `y₀`,
`−9.17e-2` at `x₀` and `−7.25e-3` at `x₀y₀` — not a branch ambiguity, a wrong
identity. Worse, it is inconsistent with `hbw`, which already determines
`Im Li₂` completely; so the old statement was a `sorry` guarding a hypothesis
set no dilogarithm satisfies. It is gone, and nothing replaced it: the correct
inversion is *derivable* here from `hbw` plus `D(1/z) = −D(z)`, so the theorem
now needs one identity where it claimed to need two.

**The check that failure teaches: are the surviving hypotheses satisfiable?**
A theorem whose hypotheses no object satisfies is vacuous, and that is exactly
what the old one was. `hbw` and `hone` are independent — `hbw` is asserted only
at the five non-unit arguments, `hone` only at `z = 1` — and the
principal-branch `Li₂` satisfies both: `Im Li₂(1) = Im(π²/6) = 0`, and `hbw` was
checked at 40 digits at fourteen random points in **both** half planes (worst
deviation `7.8e-41`) as well as at all five arguments this proof actually uses.
Any new hypothesis added here should get the same treatment before it is
trusted — as the conjugation hypothesis of `of_upper_half_plane` was, where the
check caught that the *unrestricted* form is unsatisfiable.

## The proof, in one line per term

Apply `hbw` at each of the five non-unit arguments, then use
`BlochWigner_lob_inv` (`D(1/z) = −D(z)`) and `blochWigner_xOf_eq`
(`D(x₀) = D(y₀)`). The `D` terms give

```
D(−w) − D(−w) + D(y) + D(y) + D(x₀) = 3·D(y)
```

— note `D(x₀y₀)` cancels against itself between the first two terms, so the
`D(x₀y₀) = D(y₀)/2` that an earlier version of this docstring listed as
required is **not needed**. (It is true — measured to 50 digits — but it is not
on the path.)

The correction terms are all of the form `(integer · arg w) · (integer · log‖w‖)`
because of the `w`-power identities above, and the integers cancel:

```
arg:   1 − 1/(x₀y₀) contributes +1 ,  1 − y contributes −3 ,
       1 − 1/y = x₀ contributes +6 ,  1 − 1/x₀     contributes −2      →  0
```

The `arg(2 − y₀)` terms — the only ones that are *not* multiples of `arg w` —
cancel in pairs between `Li₂(x₀y₀)` and `Li₂(1/(x₀y₀))` before any of that.

## Errors the typechecker caught, recorded for the next reader

* `Complex.arg_mul` needs `arg a + arg b ∈ Ioc (−π) π`, and for `(2−y)/(1−y)`
  the sum is `arg(2−y) + (−arg w)`, in `(−π/2, π)` — it is *not* symmetric about
  `0`, so the two bounds have genuinely different proofs.
* `arg((1−y)²) = 2·arg(1−y)` is only true because `2·arg w ∈ (−π, 0)`; the naive
  `arg_pow` is a `Real.Angle` statement and does not give it. -/
theorem ohtsuki_sum_im_eq_three_blochWigner
    (Li₂ : ℂ → ℂ) (y : ℂ) (hy : IsOhtsukiShape y)
    (hbw : IsKummerAtOhtsukiArgs Li₂ y)
    (hone : (Li₂ 1).im = 0) :
    (ohtsukiSum Li₂ y).im = 3 * BlochWigner_lob y := by
  obtain ⟨hcubic, hyim⟩ := hy
  have hyim' : y.im ≠ 0 := ne_of_gt hyim
  have hy0 : y ≠ 0 := cubic_ne_zero hcubic
  have hy1 : y ≠ 1 := cubic_ne_one hcubic
  have hw0 : (1 : ℂ) - y ≠ 0 := sub_ne_zero.mpr (Ne.symm hy1)
  have hwim : ((1 : ℂ) - y).im < 0 := by simpa using hyim
  have hwre : 0 < ((1 : ℂ) - y).re := one_sub_re_pos hyim' hcubic
  have hwim' : ((1 : ℂ) - y).im ≠ 0 := ne_of_lt hwim
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  -- `ψ = arg w` lies in `(−π/2, 0)`: `w` is in the fourth quadrant.
  have hψneg : ((1 : ℂ) - y).arg < 0 := Complex.arg_neg_iff.mpr hwim
  have hψlow : -(Real.pi / 2) < ((1 : ℂ) - y).arg := by
    have habs : |((1 : ℂ) - y).arg| < Real.pi / 2 :=
      Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl hwre)
    linarith [(abs_lt.mp habs).1]
  ---------------------------------------------------------------- algebra
  have hxy : xOf y * y = -(1 - y) := by rw [xOf_mul_self y hy0]; ring
  have hxe : xOf y = 1 / (1 - y) ^ 2 := xOf_eq_one_div_sq hy0 hy1 hcubic
  have hycube : y = -(1 - y) ^ 3 := eq_neg_one_sub_cube hcubic
  have hx0 : xOf y ≠ 0 := by rw [hxe]; exact one_div_ne_zero (pow_ne_zero 2 hw0)
  have hxim : (xOf y).im ≠ 0 := by
    have hx : (xOf y).im = -(1 / y).im := by unfold xOf; simp
    rw [hx]
    exact neg_ne_zero.mpr (one_div_im_ne_zero hyim')
  have hxyim : (xOf y * y).im ≠ 0 := by rw [hxy]; simpa using hwim'
  ---------------------------------------------------------------- norms
  have hloginv : ∀ v : ℂ, Real.log ‖1 / v‖ = -Real.log ‖v‖ := by
    intro v; rw [norm_div, norm_one, one_div, Real.log_inv]
  have hnormy : ‖y‖ = ‖(1 : ℂ) - y‖ ^ 3 := by
    have h : ‖y‖ = ‖-((1 : ℂ) - y) ^ 3‖ := by rw [← hycube]
    rw [h, norm_neg, norm_pow]
  have hnormxy : ‖xOf y * y‖ = ‖(1 : ℂ) - y‖ := by rw [hxy, norm_neg]
  have hnormx : ‖xOf y‖ = 1 / ‖(1 : ℂ) - y‖ ^ 2 := by
    rw [hxe, norm_div, norm_one, norm_pow]
  have hlogy : Real.log ‖y‖ = 3 * Real.log ‖(1 : ℂ) - y‖ := by
    rw [hnormy, Real.log_pow]; push_cast; ring
  have hlogx : Real.log ‖xOf y‖ = -(2 * Real.log ‖(1 : ℂ) - y‖) := by
    rw [hnormx, one_div, Real.log_inv, Real.log_pow]; push_cast; ring
  ---------------------------------------------------------------- args
  -- `arg (w²) = 2ψ` — legitimate only because `2ψ ∈ (−π, 0)`.
  have hargsq : (((1 : ℂ) - y) ^ 2).arg = 2 * ((1 : ℂ) - y).arg := by
    rw [sq, Complex.arg_mul hw0 hw0 (Set.mem_Ioc.mpr ⟨by linarith, by linarith⟩)]
    ring
  have hargsqne : (((1 : ℂ) - y) ^ 2).arg ≠ Real.pi := by
    rw [hargsq]; intro hc; linarith
  -- `1 − 1/y = x₀ = 1/w²`, so `arg x₀ = −2ψ`.
  have hargx : (xOf y).arg = -(2 * ((1 : ℂ) - y).arg) := by
    rw [hxe, one_div, Complex.arg_inv, if_neg hargsqne, hargsq]
  have harg1y : ((1 : ℂ) - 1 / y).arg = -(2 * ((1 : ℂ) - y).arg) := hargx
  -- `1 − 1/x₀ = 1/w`, so `arg (1 − 1/x₀) = −ψ`.
  have hargx' : ((1 : ℂ) - 1 / xOf y).arg = -((1 : ℂ) - y).arg := by
    rw [one_sub_one_div_xOf hy0 hy1, arg_one_div_of_im_ne_zero hwim']
  -- `1 − x₀y₀ = 2 − y = 1 + w`; only `Re (1 + w) > 0` is needed.
  have h2y : (1 : ℂ) - xOf y * y = 1 + (1 - y) := by rw [hxy]; ring
  have h2yre : 0 < ((1 : ℂ) + (1 - y)).re := by
    simp only [Complex.add_re, Complex.one_re]; linarith
  have h2y0 : (1 : ℂ) + (1 - y) ≠ 0 := by
    intro hc; rw [hc] at h2yre; simp at h2yre
  have hqabs : |((1 : ℂ) + (1 - y)).arg| < Real.pi / 2 :=
    Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl h2yre)
  -- `1 − 1/(x₀y₀) = (2 − y)·(1/(1 − y))`, and its arg is `arg (2 − y) − ψ`.
  have hquot : (1 : ℂ) - 1 / (xOf y * y) = (1 + (1 - y)) * (1 / (1 - y)) := by
    rw [hxy]; field_simp; ring
  have hargquot : ((1 : ℂ) - 1 / (xOf y * y)).arg
      = ((1 : ℂ) + (1 - y)).arg - ((1 : ℂ) - y).arg := by
    have hmem : ((1 : ℂ) + (1 - y)).arg + ((1 : ℂ) / (1 - y)).arg ∈
        Set.Ioc (-Real.pi) Real.pi := by
      rw [arg_one_div_of_im_ne_zero hwim']
      exact Set.mem_Ioc.mpr
        ⟨by linarith [(abs_lt.mp hqabs).1], by linarith [(abs_lt.mp hqabs).2]⟩
    rw [hquot, Complex.arg_mul h2y0 (one_div_ne_zero hw0) hmem,
      arg_one_div_of_im_ne_zero hwim']
    ring
  ---------------------------------------------------------------- the five terms
  -- The five Kummer instances, in `ohtsukiSum`'s own argument order. `unfold`
  -- is needed because `IsKummerAt` is a `def`, so `rw … at` cannot see the
  -- equation through it.
  obtain ⟨e1, e2, e3, e4, e5⟩ := hbw
  unfold IsKummerAt at e1 e2 e3 e4 e5
  have hDx : BlochWigner_lob (xOf y) = BlochWigner_lob y := blochWigner_xOf_eq y hy0 hy1
  rw [h2y, hnormxy] at e1
  rw [BlochWigner_lob_inv hxyim, hargquot, hloginv, hnormxy] at e2
  rw [hlogy] at e3
  rw [BlochWigner_lob_inv hyim', harg1y, hloginv, hlogy] at e4
  rw [BlochWigner_lob_inv hxim, hDx, hargx', hloginv, hlogx] at e5
  ---------------------------------------------------------------- assemble
  simp only [ohtsukiSum, Complex.add_im, Complex.sub_im]
  rw [hone]
  linear_combination -e1 - e2 - e3 + e4 + e5

/-! ### From (B) to `2π·Re ζ = 3·D(y₀)`

(B) is about `Im` of the sum. Ohtsuki's `ζ` is that sum divided by `2π√−1`, and
dividing by `i` is exactly what turns an imaginary part into a real one. So the
hypothesis `hzeta` that the bridge used to take for granted is a one-line
consequence of (B) *plus Ohtsuki's own definition of `ζ`* — which is a
transcription, not an assumption. -/

/-- `2π·Re (S/(2π√−1)) = Im S`. Pure arithmetic; isolated because it is the only
place the `√−1` in Ohtsuki's normalisation is used, and getting its sign wrong
would flip `Vol` against the Chern–Simons invariant without any other symptom.

Proof shape: clear the denominator to `ζ·2π√−1 = S` and read off imaginary
parts, rather than expanding `Complex.div_re`. -/
theorem two_pi_mul_re_of_div_two_pi_I {S ζ : ℂ}
    (hζ : ζ = S / (2 * (Real.pi : ℂ) * Complex.I)) :
    2 * Real.pi * ζ.re = S.im := by
  have hne : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
    simp [Complex.I_ne_zero, Real.pi_ne_zero]
  have h : ζ * (2 * (Real.pi : ℂ) * Complex.I) = S := by
    rw [hζ]; field_simp
  have him := congrArg Complex.im h
  simp [Complex.mul_im, Complex.mul_re] at him
  linarith [him]

/-- **(B), in the form the bridge consumes.** `2π·Re ζ = 3·D(y₀)` when `ζ` is
Ohtsuki's `ζ` — i.e. the `hzeta` hypothesis of `volume_conjecture_five_two`,
discharged.

`hζ` is not an extra assumption about the world: it is the *definition* of `ζ`
in Ohtsuki's Theorem 1.1, transcribed. What used to be an unproved identity
between two independently-named quantities is now a substitution. -/
theorem two_pi_re_zeta_eq_three_blochWigner
    (Li₂ : ℂ → ℂ) (y ζ : ℂ) (hy : IsOhtsukiShape y)
    (hbw : IsKummerAtOhtsukiArgs Li₂ y)
    (hone : (Li₂ 1).im = 0)
    (hζ : ζ = ohtsukiSum Li₂ y / (2 * (Real.pi : ℂ) * Complex.I)) :
    2 * Real.pi * ζ.re = 3 * BlochWigner_lob y := by
  rw [two_pi_mul_re_of_div_two_pi_I hζ]
  exact ohtsuki_sum_im_eq_three_blochWigner Li₂ y hy hbw hone

/-! ### (D) — the corpus already has the geometric input, at the *conjugate*
shape

`BlochWignerLobachevsky.FiveTwoTriangulation` states `Vol(5₂) = 3·D(y₊)` where
`y₊` is the upper-half-plane root of the **saddle** cubic `y³ − 2y² + 3y − 1`.
Ohtsuki's `y₀` is a root of the **reciprocal** cubic `y³ − 3y² + 2y − 1`. These
are not the same number and the file must not pretend they are:

```
y₀ = 0.3376410213… + 0.5622795120…i        y₊ = 0.7849201454… + 1.3071412786…i
y₊ = conj (1/y₀)
```

`inv_root_of_ohtsuki_cubic` is the algebraic half of that reconciliation and was
already here; the conjugation half is `BlochWigner_lob_conj` in
`BlochWignerSymmetry.lean`. Composed, `D(y₊) = D(y₀)` — so the corpus's own
geometric axiom discharges `hvol` with no numerical input. -/

/-- `conj (1/y₀)` is a root of the corpus's `5₂` **saddle** cubic. The
conjugation is free because that cubic has real (indeed integer) coefficients;
the inversion is `inv_root_of_ohtsuki_cubic`. -/
theorem saddle_root_conj_inv {y : ℂ} (hy : y ≠ 0)
    (h : y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0) :
    fiveTwoSaddleCubic ((starRingEnd ℂ) (1 / y)) = 0 := by
  have hinv : (1 / y) ^ 3 - 2 * (1 / y) ^ 2 + 3 * (1 / y) - 1 = 0 :=
    inv_root_of_ohtsuki_cubic y hy h
  unfold fiveTwoSaddleCubic
  have hc := congrArg (starRingEnd ℂ) hinv
  simpa [Complex.conj_ofNat] using hc

/-- …and it is in the **upper** half plane, which the bare inversion is not:
`Im (1/y) = −Im y/|y|² < 0`, and conjugating flips it back. This is exactly why
the corpus's `y₊` is the conjugate rather than the reciprocal. -/
theorem conj_inv_im_pos {y : ℂ} (hy : 0 < y.im) : 0 < ((starRingEnd ℂ) (1 / y)).im := by
  have hy0 : y ≠ 0 := by intro h; rw [h] at hy; simp at hy
  have hn : 0 < Complex.normSq y := Complex.normSq_pos.mpr hy0
  rw [Complex.conj_im, one_div, Complex.inv_im]
  have : -y.im / Complex.normSq y < 0 := div_neg_of_neg_of_pos (by linarith) hn
  linarith

/-- **The `5₂` shape the corpus triangulates is admissible for Ohtsuki's root.**
Both `FiveTwoTriangulation` side conditions hold at `conj (1/y₀)`, so asking for
that instance asks only for the *geometric* content (`vol = 3·D`), never for an
unchecked algebraic claim. -/
theorem conj_inv_is_five_two_shape {y : ℂ} (hy : IsOhtsukiShape y) :
    fiveTwoSaddleCubic ((starRingEnd ℂ) (1 / y)) = 0
      ∧ 0 < ((starRingEnd ℂ) (1 / y)).im :=
  ⟨saddle_root_conj_inv hy.ne_zero hy.1, conj_inv_im_pos hy.2⟩

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
  /-- `⟨5₂⟩_N / (e^{Nζ}·N^{3/2}·ω) → 1`. This is the only analytic content.

  `N^{3/2}` is written as a *real* power cast into `ℂ`, not as `Complex.cpow`.
  That is the faithful reading — Ohtsuki's `N^{3/2}` is a positive real, and
  `cpow` would drag in a branch choice he does not make — and it is also what
  lets `Real.log_rpow` reach it in the proof of (C). -/
  ratio_tendsto_one :
    Filter.Tendsto
      (fun N : ℕ =>
        kashaev N / (Complex.exp (N * ζ) * (((N : ℝ) ^ (3 / 2 : ℝ) : ℝ) : ℂ) * ω))
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

/-- **A second field that is not a field.** `⟨5₂⟩_N ≠ 0` eventually — because a
ratio tending to `1` is eventually non-zero, and a quotient is non-zero only if
its numerator is.

Worth isolating: the obvious way to supply this is to assume it, and assuming it
would be assuming something about the Kashaev invariant that Ohtsuki's theorem
already implies. -/
theorem kashaev_eventually_ne_zero (kashaev : ℕ → ℂ) (y ζ ω : ℂ)
    [h : OhtsukiAsymptotic kashaev y ζ ω] :
    ∀ᶠ N : ℕ in Filter.atTop, kashaev N ≠ 0 := by
  filter_upwards [h.ratio_tendsto_one.eventually_ne (by norm_num : (1 : ℂ) ≠ 0)] with N hN
  exact (div_ne_zero_iff.mp hN).1

/-- **(C).** From the asymptotic form alone, the Kashaev growth rate is
`2π·Re ζ`.

`log‖e^{Nζ}·N^{3/2}·ω·(1+o(1))‖ = N·Re ζ + (3/2)·log N + log‖ω‖ + o(1)`, and
everything but the first term dies after dividing by `N`.

No steepest descent, no geometry — this is the step that makes the shrink pay,
because it shows the volume-conjecture *conclusion* follows from the asymptotic
*form* by analysis Mathlib already has. Both side conditions it needs — `ω ≠ 0`
and `⟨5₂⟩_N ≠ 0` — are the two theorems above rather than assumptions.

The content is entirely generic, and lives in
`QOU.MathlibExt.tendsto_log_norm_div_of_tendsto_one`: *a sub-exponential factor
cannot change an exponential growth rate*. Nothing here is about `5₂`, which is
why it is stated once for every knot with such an expansion rather than per
knot. -/
theorem growth_rate_eq_two_pi_re_zeta
    (kashaev : ℕ → ℂ) (y ζ ω : ℂ) [h : OhtsukiAsymptotic kashaev y ζ ω] :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖kashaev N‖)
      Filter.atTop (nhds (2 * Real.pi * ζ.re)) := by
  have hgr := QOU.MathlibExt.tendsto_log_norm_div_of_tendsto_one
    (omega_ne_zero kashaev y ζ ω) (3 / 2 : ℝ)
    (kashaev_eventually_ne_zero kashaev y ζ ω) h.ratio_tendsto_one
  have := hgr.const_mul (2 * Real.pi)
  refine this.congr fun N => ?_
  ring

/-- **The bridge, in its raw form.** Combining (A) with the two identities (B)
and (D) *as hypotheses*, the volume conjecture holds for `5₂`.

This is the lemma; `volume_conjecture_five_two_wired` below is the theorem. Both
are kept: this one is the reusable shape (any knot with an Ohtsuki-type
expansion and a `vol = 3·D` triangulation), the wired one is `5₂` with both
identities discharged. -/
theorem volume_conjecture_five_two
    (kashaev : ℕ → ℂ) (y ζ ω : ℂ) (vol : ℝ)
    [OhtsukiAsymptotic kashaev y ζ ω]
    (hzeta : 2 * Real.pi * ζ.re = 3 * BlochWigner_lob y)
    (hvol : vol = 3 * BlochWigner_lob y) :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖kashaev N‖)
      Filter.atTop (nhds vol) := by
  have h := growth_rate_eq_two_pi_re_zeta kashaev y ζ ω
  rwa [hvol, ← hzeta]

/-- **The bridge, wired.** No free identity hypotheses remain.

What is assumed, and only this:

* `[OhtsukiAsymptotic …]` — (A), Ohtsuki's Theorem 1.1 at `d = 0`;
* `[FiveTwoTriangulation (conj (1/y)) vol]` — (D), the corpus's own geometric
  axiom, at the shape `conj_inv_is_five_two_shape` certifies is admissible;
* `hbw`, `hone` — that `Li₂` is a dilogarithm (Kummer plus `Li₂(1) ∈ ℝ`),
  unavoidable while Mathlib has no polylogarithm. `hbw` is now
  `IsKummerAtOhtsukiArgs`: Kummer at **five named points**, not on a half plane.
  `IsKummerAtOhtsukiArgs.of_upper_half_plane` builds it from `kummer`'s own
  `Im z > 0` range plus conjugation symmetry, so nothing here waits on a
  continuation across the branch cut;
* `hζ` — Ohtsuki's own **definition** of `ζ`, transcribed.

`hzeta` and `hvol`, which the raw bridge took on faith, are now theorems: the
first is (B) via `two_pi_re_zeta_eq_three_blochWigner`, the second is
`BlochWigner_lob_conj_inv` applied to the triangulation's `vol_eq_three_D`.

The residue is exactly the two things this corpus has not proved and does not
claim to — Ohtsuki's asymptotic expansion, and the hyperbolic geometry of the
`5₂` complement's triangulation — plus the statement that a dilogarithm is a
dilogarithm. Everything between them is derived. -/
theorem volume_conjecture_five_two_wired
    (Li₂ : ℂ → ℂ) (kashaev : ℕ → ℂ) (y ζ ω : ℂ) (vol : ℝ)
    [h : OhtsukiAsymptotic kashaev y ζ ω]
    [ht : FiveTwoTriangulation ((starRingEnd ℂ) (1 / y)) vol]
    (hbw : IsKummerAtOhtsukiArgs Li₂ y)
    (hone : (Li₂ 1).im = 0)
    (hζ : ζ = ohtsukiSum Li₂ y / (2 * (Real.pi : ℂ) * Complex.I)) :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖kashaev N‖)
      Filter.atTop (nhds vol) := by
  refine volume_conjecture_five_two kashaev y ζ ω vol
    (two_pi_re_zeta_eq_three_blochWigner Li₂ y ζ h.shape hbw hone hζ) ?_
  rw [ht.vol_eq_three_D, BlochWigner_lob_conj_inv (ne_of_gt h.shape.2)]

/-! ## The dilogarithm parameter, eliminated

Everything above is stated for an abstract `Li₂ : ℂ → ℂ` because Mathlib has no
polylogarithm. The corpus does — `QOU.MathlibExt.cLiTwoExt`, the integral
definition, proved analytic on `ℂ ∖ [1,∞)` and proved *the* continuation of the
series — and it satisfies both hypotheses:

* Kummer at the five points: `QOU.Knot.KummerRadial.kummer` gives them on the
  upper half plane, `QOU.MathlibExt.cLiTwoExt_conj` reflects to the lower three;
* `Im Li₂(1) = 0`: `QOU.MathlibExt.cLiTwoExt_one_im`.

So `volume_conjecture_five_two_cLiTwoExt` below has **no function parameter and
no identity hypothesis at all**. What is left is the two classes — Ohtsuki's
asymptotic expansion and the `5₂` triangulation, neither with an instance,
neither claimed — and `hζ`, which is Ohtsuki's own definition of `ζ`
transcribed.
-/

/-- **Kummer's identity at Ohtsuki's five arguments, for the corpus's own
dilogarithm.** No hypotheses beyond the shape.

`kummer` states its right-hand side as `log‖z‖ · arg(1−z)`; `IsKummerAt` uses
the other factor order, which is what the trailing `ring` is for. -/
theorem isKummerAtOhtsukiArgs_cLiTwoExt {y : ℂ} (hy : IsOhtsukiShape y) :
    IsKummerAtOhtsukiArgs QOU.MathlibExt.cLiTwoExt y :=
  IsKummerAtOhtsukiArgs.of_upper_half_plane hy
    (fun _ hw => QOU.MathlibExt.cLiTwoExt_conj hw)
    (fun w hw => by
      unfold IsKummerAt
      rw [QOU.Knot.KummerRadial.kummer hw]
      ring)

/-- **The bridge at the corpus's own dilogarithm.** The `Li₂` parameter and both
identity hypotheses of `volume_conjecture_five_two_wired` are gone.

Read the residue directly off the statement: `[OhtsukiAsymptotic …]` is (A),
`[FiveTwoTriangulation …]` is (D), and `hζ` is a transcription. Nothing else. -/
theorem volume_conjecture_five_two_cLiTwoExt
    (kashaev : ℕ → ℂ) (y ζ ω : ℂ) (vol : ℝ)
    [h : OhtsukiAsymptotic kashaev y ζ ω]
    [FiveTwoTriangulation ((starRingEnd ℂ) (1 / y)) vol]
    (hζ : ζ = ohtsukiSum QOU.MathlibExt.cLiTwoExt y / (2 * (Real.pi : ℂ) * Complex.I)) :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖kashaev N‖)
      Filter.atTop (nhds vol) :=
  volume_conjecture_five_two_wired QOU.MathlibExt.cLiTwoExt kashaev y ζ ω vol
    (isKummerAtOhtsukiArgs_cLiTwoExt h.shape) QOU.MathlibExt.cLiTwoExt_one_im hζ

end QOU.Archimedean.FiveTwoOhtsukiBridge
