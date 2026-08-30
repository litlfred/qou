---
# qou-zy94
title: 'The convex class survives but the volume-minus-surface member does not: two zero-fit family filters'
status: completed
type: task
priority: normal
created_at: 2026-08-30T09:42:06Z
updated_at: 2026-08-30T09:42:49Z
---

## Where this sits

`qou-82mc` narrowed the many-body binding magnitude to **convex-through-the-origin**
aggregators `Φ` in `B(A) = Φ(m_A·g)`: the measured `b₃ = +1.4262225` excludes
every concave one, for every bond weight and every bond set, and AME's own `Φ` is
convex and strictly superadditive on the light-nucleus grid.

That left a **class**. This bean removes its most obvious member and supplies two
reusable filters so the next candidate is checked before it is believed.

## The Lean

`QOU/MassTheory/AggregatorFamilyExclusions.lean` — 6 declarations, sorry-free,
`lean`-direct exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]`
on all six.

Three data points overdetermine any family with fewer than three parameters, so
each such family leaves a residual identity that the data either satisfies or
does not. Two filters:

**Test 1 — two-parameter linear families.** `Φ(x) = c·x + a·ψ(x)` for a fixed
shape `ψ` and free `(c, a)`. Realizability forces the `3 × 3` determinant of the
columns `(x, ψ, Φ)` to vanish (`det3_eq_zero_of_realizable`; the proof is one
`ring` after substitution — the third column is a combination of the first two).
So `det3 ≠ 0` excludes the family **for every `(c, a)` simultaneously**, with
nothing fitted and no optimisation run (`not_realizable_of_det3_ne_zero`).
`det3_eq_zero_of_construction` and `det3_ne_zero_example` pin both directions so
the filter is neither vacuous nor always-firing.

**Test 2 — pure power laws.** `Φ(x) = c·x^p` has `log Φ(k·x) − log Φ(x) = p·log k`,
*independent of the base point* (`powerLaw_log_ratio`). Two grid intervals give
two extractions of `p`; disagreement excludes the family
(`not_powerLaw_of_log_ratios_differ`).

## The measurement

`computations/probes/aggregator_family_exclusion_probe.py` — 5/5, mpmath end to
end, zero free parameters, consumes no framework quantity (so neither the
convention-C/D question nor the `q₀` pin can move it).

Determinants normalised by the product of the three column norms (raw
determinants carry the data cubed and are not comparable across shapes):

| ψ | bond-count grid | mass-number grid |
|---|---|---|
| `x^{2/3}` (surface) | 0.01228 | 0.01406 |
| `x^{1/2}` | 0.02194 | 0.02238 |
| `x^{1/3}` | 0.03425 | 0.03153 |
| `log(1+x)` | 0.01447 | 0.01810 |
| `x²` | 0.00631 | 0.02239 |
| `x` (**control**, column-degenerate) | **0.0** | **0.0** |

All five non-degenerate shapes excluded on both readings of the argument. The
control returns exactly zero, so the filter detects genuine degeneracy rather
than firing on everything.

**So the volume-minus-surface form `c·x − a·x^{2/3}` is excluded** — every
`(c, a)`, both grids. That is the canonical member of the class `qou-82mc` points
at: a linear term minus a concave deficit is convex, through the origin, and has
`Φ(x)/x → c` bounded, hence compatible with `CoordinationSaturation`.

Local exponents (Test 2):

| grid | interval 1 | interval 2 | spread |
|---|---|---|---|
| bond count | 1.176295241 | 1.804601798 | 0.628 |
| mass number | 3.187185236 | 4.348045180 | 1.161 |

No pure power law, and — the sharper fact — **the exponent increases**. The
convexity *accelerates* through `A = 4` rather than settling toward 1.

## Why this is unsurprising as physics, and why it is still worth having

The semi-empirical formula is calibrated for `A ≳ 20` and is known to fail on the
light nuclei independently of anything in this framework; ⁴He is doubly magic.
The value here is not the surprise. It is that the exclusion is now **exact and
zero-fit** rather than a remembered fact, that it is stated as a *filter* future
candidates run through, and that it removes the obvious next candidate before a
tranche is spent on it.

## What this does NOT establish

* **Test 1 excludes a TWO-parameter family, not "the SEMF".** The full formula
  carries Coulomb, asymmetry and pairing terms too. On `Z = N` light nuclei the
  asymmetry term vanishes, but three points cannot test a three-or-more-parameter
  form at all — it is **underdetermined, hence untestable here, not excluded
  here**. Asserted in the probe's caveats so it cannot be quoted the wrong way.
* **Five shapes is five shapes.** "Every candidate tried is excluded" is not
  "the two-parameter route is empty". See the follow-up below for what would
  make it general.
* **A vanishing `det3` would mean *consistent with*, never derived.** Two
  parameters on three points leaves one residual; passing one residual is weak
  evidence.

## Follow-up worth formalizing (the general version of Test 1)

The determinant tests specific shapes. The *reason* they all fail looks
structural and is a formalizable claim:

For `Φ(x) = c·x − a·x^s` with `0 < s < 1`, `a > 0`, the secant ratio is
`r(x) = Φ(x)/x = c − a·x^{s−1}`, so

    d(log r)/d(log x) = (1−s)·a·x^{s−1} / (c − a·x^{s−1})

whose numerator decreases and denominator increases in `x` — so the local
exponent `p = 1 + d(log r)/d(log x)` is **strictly decreasing**. The measured
exponent **increases** (1.176 → 1.805). If that holds for the whole
linear-minus-concave-deficit class rather than just `x^s`, it excludes the class
generally and subsumes every row of the table above.

**Not proved. Not asserted anywhere durable beyond this bean.** It needs
calculus in Lean and the concave-`ψ` generalisation is not obviously true as
stated — `r → c` forces `p → 1` asymptotically, but monotone decrease on a finite
grid does not follow from concavity alone. Establish the hypothesis before
claiming the class.

## Related

`qou-82mc` (the convexity dichotomy), `qou-brng` (linking-vs-self-energy
amplitude assignment), `qou-e5jf`.
