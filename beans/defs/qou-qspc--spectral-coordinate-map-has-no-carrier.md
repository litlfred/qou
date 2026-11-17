---
# qou-qspc
title: 'q-RH: the spectral coordinate map alpha_i = q^rho_i has no carrier'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-10-04T15:15:01Z
parent: qou-4fqg
---

The cheapest real gap in the q-Riemann-hypothesis arc. Review:
[`docs/audits/2026-08-29-q-riemann-hypothesis-arc-gap-review.md`](../docs/audits/2026-08-29-q-riemann-hypothesis-arc-gap-review.md).

`cor:spectral-half-line` (`spectral-half-line.lean`) is genuinely proved and
`#print axioms`-clean — the best-formalised declaration in the chapter. But its
statement takes

```lean
(spectral_coord : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i))
```

as a **hypothesis**, and nothing in the corpus constructs that map or ties the
`ρ i` to the Reeb spectrum of `ξ_q`. As it stands the corollary says: *for any
complex exponents whose `q`-powers are the Frobenius eigenvalues, the real parts
are ½.* That is true and proved. It is not yet a statement about the Reeb
spectrum, which is what the arc needs it to be.

## The real content is the branch choice

`α = q^ρ` determines `ρ` only modulo `2πi / log q`. So:

- `Re(ρ)` **is** well-defined on the coset — which is exactly why the corollary
  is not vacuous, and worth recording as a lemma in its own right.
- but the *map* `α ↦ ρ` is not, without a branch.

Either disposition is honest; pick one and say which:

1. **Construct it.** `ρ i := Complex.log (α i) / Real.log q` with the principal
   branch, then `spectral_coord` becomes a lemma rather than a hypothesis (needs
   `α i ≠ 0`, which `LocalQZetaFunction.eigenvalues_ne_zero` already gives).
   Prove `Re(ρ)` is branch-independent separately.
2. **Name it as an assumption**, in the `IsWeilZeta` style introduced by
   `qou-hwax`: a hypothesis class `HasReebSpectralCoords Z` carrying the map and
   its compatibility with the Reeb derivation, with an inhabited witness so the
   class is not vacuous. This is the right shape if the tie to `ξ_q` is the part
   that is genuinely open — and it probably is.

Option 1 is provable today and is worth doing regardless; it does **not** close
the gap, because the identification of those `ρ` with Reeb eigenvalues is the
actual claim. Do not report option 1 as having closed this bean.

---

## PARTIAL 2026-08-29 — option 1 done; the bean stays OPEN

Option 1 above is landed in `spectral-half-line.lean`, three lemmas, all
`#print axioms`-clean (`[propext, Classical.choice, Quot.sound]`), file exit 0
`lean`-direct:

- `exists_spectral_coord` — a spectral coordinate map always exists:
  `ρ := Complex.log α / Real.log q` on the principal branch gives `α = q^ρ`.
  Uses only `q > 1` and `α ≠ 0`, the latter already a field of
  `LocalQZetaFunction`.
- `spectral_coord_re_unique` — **the useful one.** Any two exponents with the
  same `q`-power share a real part. So `Re(ρᵢ) = 1/2` is a well-posed
  conclusion even though `α ↦ ρ` is not well-defined, being pinned only modulo
  `2πi / log q`. This is what makes `spectral_half_line`'s conclusion mean
  something independent of a branch convention, and it was not recorded
  anywhere before.
- `spectral_coord_re_eq` — the closed form `Re(ρ) = log‖α‖ / log q`, which with
  the previous lemma is *the* real part of any spectral coordinate for `α`.

**This does NOT close the bean, and must not be reported as closing it.** The
gap was never that no map exists — it is that nothing identifies these `ρᵢ`
with the spectrum of the Reeb derivation `ξ_q`. `spectral_coord` in
`spectral_half_line` is doing double duty: a coordinate relation (now supplied)
*and* a Reeb-eigenvalue identification (still supplied nowhere). What the three
lemmas buy is that the gap is now **isolated and named** rather than bundled
into one opaque hypothesis — the remaining work is exactly option 2, a
`HasReebSpectralCoords`-style class tying the exponents to `ξ_q`, with an
inhabited witness.

Sharpened statement of what is open: *the Frobenius eigenvalues of Bring's
curve and the Reeb spectrum are two sets of numbers that the arc requires to be
the same set, and no result in the corpus relates them.*

---

## BLOCKED 2026-08-29 — option 2 cannot be written faithfully today

Attempted the `HasReebSpectralCoords` class. **The object it must quantify over
does not exist in the corpus**, and that is a more precise statement of the gap
than "nothing relates them".

Corpus-grep, all `.lean` under `content/`: the identifier `ReebEigenvalue`
occurs in **exactly one file** — `q-geometric-langlands/explicit-formula.lean` —
which is a content-block sibling, i.e. outside the package globs and therefore
**not importable by any module**. The library's Reeb infrastructure
(`ReebEpsilon` over a monoidal category, `QReebFlow`, `ReebDecomposition`,
`ReebVectorField`) carries no spectrum with complex eigenvalues.

So a `HasReebSpectralCoords Z` class would have to take the Reeb side as an
opaque parameter — which is precisely the `holds : Prop` shape filed as
`qou-hprp` in the same session. Writing it would look like progress and assert
nothing. Not written.

**Blocker, stated for whoever unblocks it:** a ℂ-valued Reeb spectrum as a
library module — something of the shape `QOU.AlgebraicSubstrate.ReebSpectrum`
with eigenvalues in `ℂ`, importable, that `spectral-half-line.lean` and
`explicit-formula.lean` can both reference. Until that exists the arc has two
unconnected notions of "the Reeb spectrum" and no way to say they are the same.

## And the two notions are not merely unconnected — they disagree on the field

`ReebEigenvalue` is `structure ReebEigenvalue where val : ℝ`, docstring *"The
eigenvalue ρ ∈ ℂ (represented here as ℝ for the real part)"*. `spectralSide`
then uses it as the exponent directly:

```lean
(spectrum.map fun ρ => X ^ ρ.val / qInteger q hq ρ.val).sum
```

Meanwhile `spectral_half_line` quantifies over `ρ : Fin 8 → ℂ` and concludes
`(ρ i).re = 1/2`.

Two consequences, both worth fixing independently of this bean:

1. **`Re(ρ) = 1/2` is nearly contentless against a real spectrum.** If Reeb
   eigenvalues were real, the spectral half-line would assert every eigenvalue
   *equals* ½ — a different and far stronger claim than the one the arc makes.
   The two blocks cannot both be about the same object as typed.

2. **The formalised spectral side cannot oscillate — `da-lean-narrative-divergence`.**
   `explicit-formula.md` says *"each eigenvalue `ρ` contributes a wave of
   amplitude `X^ρ/[ρ]_q`"*. A wave is what the imaginary part produces: in the
   classical explicit formula `X^ρ` with `ρ = ½ + iγ` is `X^{1/2}·e^{iγ log X}`.
   Substituting the *real part* for `ρ`, as `spectralSide` does, leaves
   `X^{1/2}` — monotone, no oscillation. The docstring calls the truncation a
   representation "for the real part"; the arithmetic then uses that real part
   where the full complex exponent belongs. The narrative promises an
   oscillatory sum the Lean cannot express.

Item 2 is the cheaper of the two and does not need the missing module: widen
`ReebEigenvalue.val` to `ℂ` and let `spectralSide` use `Complex.cpow`. It will
change the type of `spectralSide` and of `QExplicitFormula`, both of which this
session already touched, so it is a natural follow-on rather than a new tranche.

---

## Item 2 CLOSED 2026-08-29 — `ReebEigenvalue` widened to ℂ

`explicit-formula.lean`. `structure ReebEigenvalue where val : ℂ` (was `ℝ`), and
`spectralSide` now returns `ℂ`, so the identity in `QExplicitFormula` reads
`(ψ_q(X) : ℂ) = spectralSide …` — the geometric side coerced, the spectral side
genuinely complex. The oscillatory term `X^ρ` is `Complex.cpow` and can now
oscillate; previously it was `X^{Re ρ}`, monotone for every eigenvalue.

Nothing about the real-index case was lost, and that is checked rather than
asserted:

- `qIntegerReal` keeps the real-index bracket, and `qIntegerReal_pos` — the
  genuine positivity fact the complex bracket cannot state — is preserved
  verbatim, renamed only.
- `qInteger_ofReal` proves the two agree: `qInteger q hq (ρ : ℂ) = ↑(qIntegerReal q hq ρ)`.
  So the widening is conservative on the old domain.
- `exists_offAxis_reebEigenvalue` records what it bought: the type now admits
  `ρ = ½ + i`, which the old `val : ℝ` could not express at all.

`not_qExplicitFormula_empty` survives the change — its hypothesis is now a ℂ
equation whose terms are all real coercions, so it returns to ℝ by taking real
parts, and the counterexample stands.

**Verification.** `lean`-direct exit 0; `#print axioms`
`[propext, Classical.choice, Quot.sound]` on `qIntegerReal_pos`,
`qInteger_ofReal`, `not_qExplicitFormula_empty`, `explicit_formula` and
`not_qLog_tendsto_log`. `run-validate` exit 0.

**Item 1 of that pair is NOT closed.** The two Reeb notions no longer disagree on
the *field*, but nothing still ties these eigenvalues to `spectral_half_line`'s
`ρ : Fin 8 → ℂ`, and the blocker above stands: there is no importable ℂ-valued
Reeb spectrum module. The widening removes a type-level obstruction to writing
one; it does not write it. This bean stays open on that.

---

## Item 1 CARRIED 2026-08-30 — the blocker is lifted; the identification is still unproved

The blocker stated above — *"a ℂ-valued Reeb spectrum as a library module …
importable, that `spectral-half-line.lean` and `explicit-formula.lean` can both
reference"* — is now satisfied by
`QOU/AlgebraicSubstrate/ReebSpectrum.lean`. **Read the rest of this entry before
recording the bean as closed: it is not.**

### What was written

`ReebSpectrum H` is a structure, not an opaque carrier: an operator
`op : H →ₗ[ℂ] H`, eight modes, eight complex eigenvalues, and the two facts that
make it content-bearing — `mode_ne_zero` and `is_eigen : ∀ i, op (mode i) =
spec i • mode i`. The earlier attempt was abandoned because it would have taken
the Reeb side as an opaque parameter, "the `holds : Prop` shape filed as
`qou-hprp`". This one does not: an instance has to produce an operator and
vectors satisfying a real equation, which `⟨True⟩` cannot discharge.

`HasReebSpectralCoords Z R` carries the identification — `∀ i, Z.eigenvalues i =
(Z.q : ℂ) ^ (R.spec i)` — as a `Prop` class **with no instance**. That is the
honest open state (§3b-tax), not an omission.

Two payoff theorems in `spectral-half-line.lean`, both taking the class as an
explicit `[…]` hypothesis so the dependency is visible in the type
(§3b-cond): `reeb_spectrum_on_critical_line` — the Reeb spectrum lies on the
critical line — and `reeb_spectrum_fixed_by_involution`, the same as a symmetry
statement.

### The check that mattered, and what it changed

A conditional theorem is worthless if its hypothesis cannot be met. That is
exactly the defect the `False`-proving axioms in `hasse-weil-bound.lean` had, so
it was worth proving rather than assuming — and the inhabitedness witness
already in the file does **not** settle it: `reebSpectrumExample` has every
`spec i = 1`, which forces `αᵢ = q` for all `i`, false for any `Z` with distinct
eigenvalues. It witnesses that `ReebSpectrum` is inhabited and nothing about the
class.

`hasReebSpectralCoords_satisfiable` proves the real statement: for every `Z` with
`q > 1` there **is** a `ReebSpectrum` satisfying `HasReebSpectralCoords Z`. The
proof is a construction — take the exponents from `exists_spectral_coord` and
diagonalise them on `Fin 8 → ℂ` with `diagOp`, modes `Pi.single i 1`.

**This sharpens the gap rather than closing it, and the sharpening is the
result.** Satisfiability says *some* operator has the Frobenius exponents as its
spectrum — here one built from them, which is bookkeeping. The arc claims the
framework's Reeb derivation `ξ_q` is such an operator, a statement about a
*particular* operator, untouched by this. So: everything now rests on the choice
of operator and nothing on the shape of the hypothesis, and one way the arc could
have been empty is eliminated.

### Verification

`lean`-direct exit 0 on `ReebSpectrum.lean`, `spectral-half-line.lean`,
`hasse-weil-bound.lean`, `explicit-formula.lean`. `#print axioms`
`[propext, Classical.choice, Quot.sound]` — no `sorryAx` — on
`hasReebSpectralCoords_satisfiable`, `diagOp`, `reeb_spectrum_on_critical_line`,
`reeb_spectrum_fixed_by_involution`, `reebSpectrumExample`, `spectral_half_line`,
`spectral_half_line_is_fixed_locus`, `critical_line_iff_fixed`,
`partner_re_eq_one_sub`. `run-validate` ✓ Valid (13 warnings, all pre-existing,
none in these files).

### What stays open

The identification itself: *no result relates the framework's `ξ_q` to
`HasReebSpectralCoords`.* An instance would assert it, so none is provided. The
bean stays open on precisely that, and it is now a single named class rather than
a missing module plus an unstated hypothesis.

---

## The magnitude is now DERIVED, not assumed 2026-08-30

A duplication found while writing the entry above, and worth recording as its
own finding because it is a *structural* consequence of §0a rather than an
oversight anyone made.

`reeb_spectrum_on_critical_line` carried

```lean
(hw : ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ))
```

as a hypothesis. That is exactly `hasse_weil_bound`, which is **proved** in
`hasse-weil-bound.lean` from `[IsWeilZeta Z]` — the file next door. The same
fact was assumed in one sibling and derived in the other, and neither could see
the other, because content-block siblings sit outside the package globs and
cannot import one another (§0a). Nothing was wrong with either file on its own;
the gap was in the gap between them, and it would have stayed invisible to any
per-file check.

**Fix.** `IsWeilZeta`, the chain `eigenvalue_functional_equation` →
`castelnuovo_severi_bound` → `eigenvalue_norm_sq` → `hasse_weil_bound`, and the
`weilZetaExample` instance moved verbatim to a new library module
`QOU/AlgebraicSubstrate/WeilZeta.lean`, importable by both siblings.
`hasse-weil-bound.lean` imports it and keeps everything downstream of the
magnitude — conjugation-closure, the characteristic-polynomial facts, Vieta —
which is the block's own content. `spectral-half-line.lean` imports it and
replaces `hw` with `[IsWeilZeta Z]`.

**What this buys.** The critical-line theorem is now conditional on exactly two
hypotheses, of quite different standing:

- `[IsWeilZeta Z]` — the two classical Weil inputs, cited, and jointly
  satisfiable (`weilZetaExample`).
- `[HasReebSpectralCoords Z R]` — the identification. **The open one.**

Before, a reader had to notice that a third hypothesis was redundant to see
this. Now the statement says it. The arc's whole remaining conditionality is one
named class, which is the shape a gap should have.

**Verification.** `lean`-direct exit 0 on all six files — the three library
modules (`LocalQZetaFunction`, `WeilZeta`, `ReebSpectrum`) and the three content
blocks (`hasse-weil-bound`, `explicit-formula`, `spectral-half-line`).
`#print axioms` `[propext, Classical.choice, Quot.sound]` on
`reeb_spectrum_on_critical_line`, `reeb_spectrum_fixed_by_involution`,
`hasReebSpectralCoords_satisfiable`, `hasse_weil_bound`, `eigenvalue_norm_sq`,
`eigenvalues_conj_closed`, `charPoly_coeff_isReal`, `prod_eigenvalues_eq_pm`,
`norm_charPoly_coeff_seven_le`, `weilZetaExample`.

**Generalisable, and probably not unique.** Two content-block siblings in one
chapter, one assuming what the other proves, is a defect class §0a makes
structurally likely and no existing checker looks for: the per-block sidecars
audit blocks in isolation, and neither file is wrong by itself. Worth a detector
— hypotheses of a content-block theorem that match, up to renaming, the
*conclusion* of a theorem in a sibling block of the same chapter. Filed as
`qou-sibdup`.


--------

## 2026-08-31 — what the FUNCTIONAL EQUATION alone forces. Bean stays OPEN.

Four new declarations in `spectral-half-line.lean`, all `lean`-direct exit 0
and all `#print axioms`-clean (`[propext, Classical.choice, Quot.sound]`).

**This does not close the bean, and is not offered as closing it.** The
identification `HasReebSpectralCoords` still has no instance. What changed is
that the open item now has a *cheap falsification test* attached to it.

### The observation

`reeb_spectrum_on_critical_line` consumes BOTH Weil inputs — the functional
equation and Castelnuovo–Severi, the latter through `hasse_weil_bound`.
Castelnuovo–Severi is the deep one. Nobody had asked what the shallow half
forces on its own.

It forces a reflection. The pairing `α_{σi} = q/αᵢ` transports through
`αᵢ = q^{ρᵢ}` to `Re ρ_{σi} = 1 − Re ρᵢ`: the eight real parts are a multiset
**symmetric about 1/2** without yet lying on it. Summing that over the
bijection gives `S = 8 − S`, hence

    ∑ᵢ Re ρᵢ = 4 = g,   the genus of Bring's curve

with `8 = 2g` eigenvalues pairing into `g` reflected pairs of total 1 each.

### Why the weaker statement is the useful one

It is genuinely weaker — real parts `{0.3, 0.7}` satisfy it and violate the
critical line, so passing is evidence and not proof (scope-(a)). But it is
weaker in a useful direction:

- it is **one real number**, the trace of `ξ_q` on the eight fundamental modes;
- it needs **no Castelnuovo–Severi**, so it can be checked before any of the
  hard machinery is in place;
- it is **necessary**: a `ξ_q` whose eight modes have `∑ Re ρᵢ ≠ 4` cannot
  satisfy `HasReebSpectralCoords` for ANY `IsWeilZeta` datum. The
  identification would be refuted outright.

The hypothesis-honesty is in the types, not just the prose: the two primitive
theorems take the permutation `σ` as an **explicit argument** rather than
reaching for `[IsWeilZeta Z]`, so which half of the Weil input is doing the
work is visible in the signature. The `[IsWeilZeta]` form is a convenience
wrapper over them.

### The declarations

- `reeb_spectrum_reflected_by_functional_equation` — the reflection.
- `reeb_spectrum_sum_re` — the trace identity, explicit `σ`.
- `reeb_spectrum_sum_re_of_isWeilZeta` — convenience wrapper.
- `reeb_spectrum_sum_re_witness` — **joint** satisfiability on
  `weilZetaExample` (`q = 4`, all `αᵢ = 2`; supersingular, so every
  `ρᵢ = log 2/log 4 = 1/2` and the eight sum to 4). Each of the three
  hypotheses was separately known inhabited, which is NOT the same as their
  being jointly inhabited — a theorem conditional on an unsatisfiable
  conjunction proves nothing, and that is the exact defect the `False`-proving
  axioms removed from `hasse-weil-bound.lean` had.

### What is still open — unchanged

Nothing here says what `ξ_q` is. The gap remains exactly where the bean put
it: the identification of the framework's Reeb derivation with an operator
whose spectrum is the Frobenius exponents. This adds a test that a candidate
must pass, not a candidate.


## 2026-08-31 (cont.) — the fixed locus, from the functional equation alone

Three more declarations, `lean`-direct exit 0, all `#print axioms`-clean.
**Still does not close this bean** — no instance of `HasReebSpectralCoords`.

The reflection theorem had a sharper consequence I did not take at the time.

**`eigenvalue_functional_equation_involutive`** — applying the Weil pairing
twice returns the eigenvalue: `α_{σ²i} = αᵢ`.

Stated on the **eigenvalues**, not on the permutation, and the distinction is
the honest part: `σ² = id` as a permutation needs the `αᵢ` to be *distinct* — a
repeated eigenvalue lets `σ` permute its indices without moving any value —
whereas `α_{σ²i} = αᵢ` holds unconditionally. The weaker form is what is true
and is all the rest uses.

**`reeb_spectrum_fixed_point_on_critical_line`** — if `σ i = i` then
`Re ρᵢ = 1/2` exactly, **with no Castelnuovo–Severi**.

`reeb_spectrum_on_critical_line` reaches the same conclusion for *every* index,
but pays the deep Weil bound. This gets it for the fixed indices free.

**Why it is not a restatement of `critical_line_iff_fixed`.** That lemma says
`Re ρ = 1/2 ↔ Re ρ = 1 − Re ρ`, which is an identity about real numbers — true
of any `ρ` whatsoever, and it says nothing about this spectrum. Here the
fixed-ness is supplied *by the Weil pairing itself*. So the critical line stops
being a value the spectrum is observed to have and becomes **the fixed locus of
a symmetry the functional equation forces on it**. That is the difference
between a coincidence and a mechanism.

**`eigenvalue_sq_eq_q_of_fixed`** — the eigenvalue-level form: a fixed index has
`αᵢ² = q`, the supersingular shape `αᵢ = ±√q`. Needs no Reeb spectrum and no
identification; it is a statement about `Z` alone. `weilZetaExample` is exactly
this case at every index, which is why its permutation is `Equiv.refl`.

### The structure is now complete, and it adds nothing to the trace test

Fixed points sit on the line; non-fixed indices pair `(i, σi)` with
`Re ρᵢ + Re ρ_{σi} = 1`. So with `f` fixed points the sum is
`f·(1/2) + ((8−f)/2)·1 = 4` for **every** `f`. The trace identity is recovered
independently of the fixed-point count — consistent, and worth recording as a
negative: **counting fixed points yields no new constraint**, so it is not a
sharper test than `∑ Re ρᵢ = 4` and should not be pursued as one.

### Still open, unchanged

Nothing here says what `ξ_q` is. The arc now has a described structure the
identification would have to satisfy — reflection symmetry, fixed points on the
line, trace 4 — and still no candidate operator.


## 2026-08-31 (cont.) — PERIODICITY pins the spectrum to two points

I said the next move was to stop deriving necessary conditions from Weil and go
after the operator. This is that step, and it uses the framework's **own** axiom
rather than another Weil consequence.

`QOU.AlgebraicSubstrate.CategoricalReebDerivation` carries

    reeb_periodic : (reeb : End obj) ^ period = 1

The Reeb derivation is **periodic**. That has never been set against the
critical line, and the combination is severe.

Four declarations, `lean`-direct exit 0, all `#print axioms`-clean:

- `reeb_spectrum_pow_apply` — `op^n (modeᵢ) = specᵢ^n • modeᵢ`.
- `reeb_spectrum_periodic_eigenvalue` — `op^Ω = id ⟹ specᵢ^Ω = 1`. This is
  where `mode_ne_zero` earns its place in the structure: without it the zero
  vector satisfies the eigenvalue equation for every scalar and nothing follows.
- `reeb_spectrum_norm_one_of_periodic` — hence `‖specᵢ‖ = 1` for `Ω ≠ 0`.
- **`reeb_spectrum_pinned_by_periodicity`** — with the identification and a Weil
  datum: `Re ρᵢ = 1/2` **and** `(Im ρᵢ)² = 3/4`.

### Why this is the sharpest thing in the arc

The two constraints have **independent origins**: the real part comes from the
Weil bound, the modulus from the framework's own `reeb_periodic`. Together they
leave the eight eigenvalues only **two possible values**, `1/2 ± i√3/2` — the
primitive sixth roots of unity.

So the conjunction is **falsifiable by a computation nobody has run**: a genus-4
curve whose Frobenius eigenvalues are not all `q^{1/2 ± i√3/2}` refutes it.
Either `ξ_q` is not the operator whose spectrum these are, or it is not periodic.

And a corollary in words: since `1/2 ± i√3/2` are primitive **sixth** roots,
`specᵢ^Ω = 1` forces **`6 ∣ Ω`**. The framework's Reeb period cannot be an
arbitrary natural number.

**No contradiction with Hasse–Weil** — it entails it: `‖q^{ρᵢ}‖ = q^{Re ρᵢ}
= √q` for either value.

### Scope, stated precisely

The periodicity is carried as an **explicit hypothesis on `R.op`**, not imported
from `CategoricalReebDerivation`. That structure's `reeb` is an endomorphism of a
monoidal-category object; identifying it with a `ℂ`-linear operator on an
8-dimensional space is exactly this bean's open problem. What is proved is the
*consequence* of periodicity, available to any candidate operator having it.

**So this still does not close the bean** — but it changes its character. The
open item is no longer "find any operator"; it is now "does the framework's `ξ_q`
have a spectrum of primitive sixth roots of unity, and is `6 ∣ Ω_q`?" That is a
question with a computable answer.

### Next

Determine `Ω_q` (`CategoricalReebDerivation.period`) as the corpus actually uses
it. If a value is pinned anywhere, `6 ∣ Ω` is an immediate live test.


## RETRACTION 2026-08-31 — the `6 ∣ Ω` test is NOT runnable, and I said it was

Last entry closed with *"the open item is now a question with a computable
answer"*, and named determining `Ω_q` as the next step. **I tried it. It cannot
be computed, and the reason is not a difficulty — the quantity has no value.**

Measured: `CategoricalReebDerivation` has **zero instances** in the tree, and
there is **no `period :=` assignment anywhere**. Its five `.lean` occurrences are
three in its own defining file and two in a docstring I wrote this session. So
the natural number the corollary constrains is not pinned by anything, and there
is nothing for `6` to divide.

The theorems are unaffected — `reeb_spectrum_pinned_by_periodicity` is proved and
its hypothesis is explicit. What was wrong was my characterisation of what
remained: *"a question with a computable answer"* is false while
`CategoricalReebDerivation` is uninhabited. **Inhabiting it is the prerequisite,
and that is separate work.**

### And the attempt turned up something worse — bean `qou-9iwt`

`Ω_q` denotes **at least three genuinely distinct objects** in the corpus:

1. the smallest positive **integer** with `ξ_q^{Ω_q} = id_A` (the Lean
   `period : ℕ`);
2. a **topological space**, in `q-plancherel-asymptotic-skeleton.md` — *"We
   define a topological space `Ω_q`"*, target of `ι_n : {λ ⊢ n} → Ω_q`;
3. an **infinite surreal** `Ω_q ≍ ε⁻¹` (`ε = 1/ω`), across five
   `appendix-surreals` blocks.

A space is not a natural number and neither is an infinite surreal, so **`6 ∣ Ω`
says nothing whatever about (2) or (3)**. My own corollary is the thing most at
risk of being carried across that boundary, so its docstring now scopes itself
explicitly to (1) and names the other two.

That is the exact failure AGENTS.md flags — *"attributes do not transfer across
overloaded symbols … distinct objects sharing a glyph is a recurring root
cause"*.
