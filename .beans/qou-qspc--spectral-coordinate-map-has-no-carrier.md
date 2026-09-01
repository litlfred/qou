---
# qou-qspc
title: 'q-RH: the spectral coordinate map alpha_i = q^rho_i has no carrier'
status: todo
type: task
priority: high
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-08-30T04:20:00Z
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
