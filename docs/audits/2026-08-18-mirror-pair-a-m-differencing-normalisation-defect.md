# Differencing Habiro coefficients measures the denominators, not the pair

**Date:** 2026-08-18
**Branch:** `claude/agent-4903-polynomial-serialization-smp61e`
**Bean:** `qou-0ndb`
**Status:** defect identified, Lean-proved, drained across five producers; two audit docs re-scoped.

## TL;DR

Nine scripts in `computations/` formed a pair difference by subtracting two
witnesses' Habiro coefficients:

```
Σ_m (a_m^X − a_m^Y) · (u;u)_m
```

Each witness's `a_m` expand **its own denominator-cleared numerator**
`p = d·t`, not the trace `t`. Verified directly against the witness fields on
every entry of the atomic witness:

```
Σ a_m (u;u)_m  ==  p_in_u  ==  denom_in_u · tr_M(u²) · u^shift     (True, ×3)
```

so the coefficient difference reconstructs `d_X·t_X − d_Y·t_Y`, which is
proportional to the pair difference `t_X − t_Y` only where the two denominators
agree at the evaluation point.

They do not agree — and the way they fail is the whole story. **The denominators
are built out of Φ₄ and Φ₈, the very cyclotomic factors being measured**, to
different powers on each member of a pair:

| atom | denominator | its own Φ₄, Φ₈ content |
|---|---|---|
| proton | `4u¹⁸(u⁴+1)²` | Φ₈**²** |
| neutron | `4u¹⁸` | **none** |
| deuteron | `192u⁴⁶(u⁴+1)³` | Φ₈**³** |
| ⁶He | | Φ₄⁵ Φ₈**⁴** |
| ⁶Be | | Φ₄⁵ Φ₈**⁸** |
| ¹⁴O | | Φ₄¹³ Φ₈**¹⁶** |
| ¹⁴C | | Φ₄¹³ Φ₈**¹²** |

So a Φ₈ multiplicity read off `Σ Δa_m (u;u)_m` is in substantial part a property
of the normalisation chosen when clearing denominators, not of the pair. This is
not a rounding-level error; it is measuring the wrong object.

## The Lean

`QOU/Habiro/MirrorPairNormalisation.lean` (sorry-free, generic `CommRing R` /
`CommMonoid R` per §7c — no archimedean structure is used):

```
coeffDiff_of_common_denom     : d * tX - d * tY = d * (tX - tY)
coeffDiff_at_coincidence      : dX * t - dY * t = (dX - dY) * t
coeffDiff_eq_zero_iff         : dX * t - dY * t = 0 ↔ dX = dY ∨ t = 0
coeffDiff_ne_zero_at_coincidence
mirror_trace_eq_of_tau_eq     : τp^Z τn^N c^n = τp^N τn^Z c^n  when τp = τn
mirror_traceDiff_eq_zero_of_tau_eq
```

`coeffDiff_at_coincidence` is the one that names the defect: where the two
traces coincide, the coefficient difference collapses not to zero but to the
**denominator gap** times the common value. `#print axioms` shows four on
`[propext, Quot.sound]` and two on none.

## What the corrected measurement says

`mirror_trace_diff_numerator` / `trace_diff_numerator`
(`computations/habiro/habiro_coefficients_atomic.py`) difference the traces over
a common denominator, which is correct in either trace convention. All ten
mirror pairs, convention D:

| pair | A | deg | Φ₁ | Φ₂ | Φ₄ | Φ₈ | 2⌊(A−1)/2⌋ |
|---|---|---|---|---|---|---|---|
| n−p | 1 | 54 | 1 | 1 | 1 | 0 | 0 ✓ |
| ³He−³H | 3 | 194 | 1 | 1 | 3 | 2 | 2 ✓ |
| ⁵Li−⁵He | 5 | 329 | 1 | 1 | 5 | 4 | 4 ✓ |
| ⁶He−⁶Be | 6 | 398 | 1 | 1 | 6 | 4 | 4 ✓ |
| ⁷Be−⁷Li | 7 | 464 | 1 | 1 | 7 | 6 | 6 ✓ |
| ⁸B−⁸Li | 8 | 533 | 1 | 1 | 8 | 6 | 6 ✓ |
| ⁹B−⁹Be | 9 | 599 | 1 | 1 | 9 | 8 | 8 ✓ |
| ¹⁰C−¹⁰Be | 10 | 668 | 1 | 1 | 10 | 8 | 8 ✓ |
| ¹²N−¹²B | 12 | 803 | 1 | 1 | 12 | 10 | 10 ✓ |
| ¹⁴O−¹⁴C | 14 | 938 | 1 | 1 | 14 | 12 | 12 ✓ |

**10/10 on `mult(Φ₈) = 2⌊(A−1)/2⌋`**, with `Φ₁ = Φ₂ = 1` throughout and
`Φ₄ = A` exactly.

`Φ₄ = A` is an **observation on ten points, not a theorem.** It has no proof, is
not wired to anything, and is recorded here so a later agent can try to derive
or kill it. Do not cite it as established.

## Scoping the two superseded audit docs

Per the convention-D ruling's treatment of the `c_k` ladder — recorded C-frame
numbers need **scoping, not correction** — the superseded tables are left in
place with a banner rather than rewritten.

**`2026-06-01-qbeta-habiro-a6-refutes-refined-scaling-law.md`** — headline
*"BOTH scaling laws REFUTED"*. Under the corrected differencing both refutations
are gone: A=6 measures Φ₈ = 4 (predicted 4) and A=14 measures 12 (predicted 12).
Three further claims in that doc do not survive:

- *"`Φ_4 = u²+1` never appears: multiplicity 0 in all 8 pairs"* — Φ₄ = A on all
  ten. The denominators of ⁶He and ⁶Be carry Φ₄⁵ each and ¹⁴O/¹⁴C carry Φ₄¹³
  each, i.e. the factor being declared absent was sitting in the normalisation.
- *"Φ_2 ⟺ even A OR A=1"* — Φ₂ = 1 universally. The doc's visible pattern-hunt
  around this (an in-text *"Wait: A=1 is odd but Φ_2 = 1…"*, then a discarded
  mod-4 attempt, ending at *"the cleanest description is just the table"*) was
  chasing a normalisation artifact.
- *"the multiplicity is genuinely non-monotonic in A … No closed form in A can
  capture this — the right framework is the per-block Wenzl-annihilator
  linear-relation count"* — the non-monotonicity was the A=14 drop to 4. Φ₈ is
  monotone non-decreasing in A across all ten points and **is** a closed form in
  A. This is the load-bearing one: it directed later work away from a closed
  form that holds.

**`2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`** — the refined
law it proposes is the one that now holds 10/10. Its five-point table and its
`Φ₁/Φ₂/Φ₄` secondary findings are C-frame and computed on the a_m-difference.

**`2026-06-01-mirror-pair-phi8-universal-boundaries.md`** — **its claims
SURVIVE, and are now better supported than when they were made.** `M_first_Φ₈`
and `M_first_Φ₈²` were computed on partial sums of the same a_m-difference, so
they had to be re-measured; on the corrected difference,

```
M_first_Φ₈  = 7   for 9/9 pairs with mult(Φ₈) > 0
M_first_Φ₈² = 15  for 9/9
```

including ⁶He−⁶Be and ¹⁴O−¹⁴C, which under the old differencing were the two
anomalies. So the boundary structure is genuinely universal while the
multiplicity read off the same object was not — a useful separation: the
boundary is a property of where Φ₈ enters the partial sums, which the
denominator gap shifts far less than it shifts the total multiplicity.

This is the one place where correcting the defect **strengthened** an existing
conclusion rather than replacing it.

## Producers drained

| script | pairs | published a witness? |
|---|---|---|
| `_habiro_coefficient_extract.py` (mass-table summary) | 7 | yes — was publishing `phi_8_mult: 0` for all seven |
| `extend_even_a_mirror_pair_test.py` | 3 open even-A | yes |
| `topic2_mirror_pair_phi8_boundary_scan.py` | 10 | yes |
| `shell_closure_phi8_correlation_test.py` | 4 | no — its witnesses are absent, so nothing was published |
| `probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py` | 3 atomic-step | yes |

## The Q_β cluster — measured, and my first reading of it was wrong

Four more scripts subtract coefficients, on `Δa_m := a_m(n) − a_m(p)` ("the
Q_β-relevant Habiro element") and on the atomic-step pairs:

```
qbeta/qbeta_habiro_delta_am_factorization.py     publishes
qbeta/qbeta_habiro_cross_pair_factorization.py   publishes
qbeta/qbeta_habiro_delta_a_m_pattern_probe.py    reads only
qbeta/qbeta_habiro_phase5q_dn_refactorize.py     reads only
probes/qbeta_habiro_element_probe.py             publishes
```

**RETRACTED.** An earlier revision of this doc said these witnesses "published
refutations computed on the wrong object", on the strength of a measurement
showing the two objects have disjoint cyclotomic factor sets for n−p. That
measurement used the **current, convention-D** atomic witness. The three
witnesses were computed **2026-06-02 and 2026-07-07**, in the convention-C era,
and the C-era denominators are not the D-era ones. The right test was to recover
them from git history, which I had not done.

Recovered from `cf5318a97b` (2026-08-09, the last commit before p/n moved to D
at `deg_p_u` 40/40 → 44/36):

| pair | convention-C denominators | a_m-differencing |
|---|---|---|
| **n − p** | `4u¹⁹(u²+1)` vs `4u¹⁹(u²+1)` — **identical** | **VALID** |
| D − n | `32u⁴⁰(u²+1)³` vs `4u¹⁹(u²+1)` | invalid |
| ³He − D | `64u⁵⁵(u²+1)⁵` vs `32u⁴⁰(u²+1)³` | invalid |
| ⁴He − ³He | `256u⁷⁶(u²+1)⁷` vs `64u⁵⁵(u²+1)⁵` | invalid |

So the split is sharp, and it is not the one I first reported:

- **The n−p element was computed on the right object.** Under C the two
  denominators are *identical*, so `Σ Δa_m (u;u)_m = d·(t_n − t_p)` — the pair
  difference up to a fixed common normalisation. `delta_am_factorization`,
  `element_probe`, and the n−p reference leg of `cross_pair_factorization` are
  **correct as computed**. They need convention-scoping, not a defect label.
- **The atomic-step pairs were never valid**, under C or D. `D − n`, `³He − D`,
  `⁴He − ³He` have differing denominators in both conventions.
- **Under D, n−p needs the fix too** — p/n diverged at the 2026-08-15 migration
  (`4u¹⁸(u⁴+1)²` vs `4u¹⁸`). The same script is right under C and wrong under D
  with no edit in between, which is why the guard below is a runtime check
  rather than a rule anyone can apply by reading the code.

### Does any published conclusion move? No — and two are now better supported

`cross_pair_factorization`'s verdict is **SPECIFIC**: the `Φ₁·Φ₂` prefactor is
specific to the isospin doublet rather than universal across atomic-number
jumps. That conclusion rested entirely on the two broken legs, so it was the one
genuinely at risk. Re-measured on the correct trace difference:

| pair | cyclotomic content | Φ₁·Φ₂ |
|---|---|---|
| n − p | {Φ₁, Φ₂, Φ₄, Φ₁₆} | **present** |
| D − n | {} | absent |
| ³He − D | {Φ₈³} | absent |
| ⁴He − ³He | {Φ₄², Φ₈⁴} | absent |

**SPECIFIC is confirmed**, and it now has a structural reason instead of an
empirical one: `mirror_traceDiff_eq_zero_of_tau_eq` says `Φ₁ = (u−1)` divides a
difference exactly where the two traces coincide at `q = 1`. That holds for the
mirror pair n/p (`τ_p(1) = τ_n(1) = 1/2`, measured) and for none of the
atomic-number jumps, which have different mass numbers. The presence of Φ₁ for
n−p and its absence from every jump is *forced*.

`delta_am_factorization`'s C6 falsification (*"no single polynomial factor
unites all m"*) also survives: the gcd across the corrected Δa_m is the constant
4, not a polynomial.

So **no published claim in this cluster is overturned.**

### What was changed instead: a guard

Since the conclusions stand, rewriting five scripts to work under D would be
churn for no result. What was missing is the thing that would have caught this
on day one, so that is what was added —
`habiro_coefficients_atomic.require_am_differenceable(tr_x, tr_y)`, which
compares the two denominators and raises `AmDifferenceInvalid` rather than let a
plausible-but-wrong polynomial through. All five scripts call it as a preflight
and **fail loudly under D**, verified by running them.

A producer that refuses to emit a wrong number is better than one that emits it.
Porting them to D means expanding `trace_diff_numerator` instead of differencing
two expansions — a restructure these files have not had, tracked in `qou-lnog`.

## Why it survived

Nothing raises. `Σ Δa_m (u;u)_m` is a perfectly good polynomial; it factors, it
has cyclotomic content, it prints plausibly. The only signal that it is the
wrong polynomial is structural — a mirror difference must vanish at q = 1, so it
must carry Φ₁ — and no producer checked that. The corrected helper now raises
rather than proceed when half-integer powers survive denesting, but the Φ₁ check
is the one that would have caught this on day one and is worth adding to any
future pair-difference producer.
