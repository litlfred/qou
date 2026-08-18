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

**`2026-06-01-mirror-pair-phi8-universal-boundaries.md`** — `M_first_Φ₈ = 7` and
`M_first_Φ₈² = 15` are computed on partial sums of the same a_m-difference. The
boundary claim is **not re-measured here**; `topic2_mirror_pair_phi8_boundary_scan.py`
is corrected and its witness regenerated, so the numbers in that doc should be
read against the regenerated witness rather than trusted as-is.

## Producers drained

| script | pairs | published a witness? |
|---|---|---|
| `_habiro_coefficient_extract.py` (mass-table summary) | 7 | yes — was publishing `phi_8_mult: 0` for all seven |
| `extend_even_a_mirror_pair_test.py` | 3 open even-A | yes |
| `topic2_mirror_pair_phi8_boundary_scan.py` | 10 | yes |
| `shell_closure_phi8_correlation_test.py` | 4 | no — its witnesses are absent, so nothing was published |
| `probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py` | 3 atomic-step | yes |

## The Q_β cluster — same defect, different consequence, NOT yet drained

Four more scripts subtract coefficients, all on `Δa_m := a_m(n) − a_m(p)`, "the
Q_β-relevant Habiro element":

```
qbeta/qbeta_habiro_delta_am_factorization.py     publishes
qbeta/qbeta_habiro_cross_pair_factorization.py   publishes
qbeta/qbeta_habiro_delta_a_m_pattern_probe.py    reads only
qbeta/qbeta_habiro_phase5q_dn_refactorize.py     reads only
probes/qbeta_habiro_element_probe.py             publishes
```

For n−p the two objects are not close:

| | `Σ Δa_m (u;u)_m` (what was computed) | numerator of `t_n − t_p` |
|---|---|---|
| degree | 44 | 54 |
| cyclotomic factors | **{Φ₃, Φ₆, Φ₁₂}** | **{Φ₁, Φ₂, Φ₄, Φ₁₆}** |
| integer content | 1 | 4 |

Disjoint factor sets, and not proportional. Note the correct object is divisible
by Φ₁ — it must be, since a mirror pair's two traces coincide at q = 1 — and the
computed one is not.

**These three witnesses record NEGATIVE / PARTIAL verdicts, so the defect did
not publish a false positive here; it published refutations computed on the
wrong object.** That is the over-narrowing failure mode of
AGENTS.md §"Before declaring refuted / ruled out / dead end", and it is the
reason this section exists rather than a bare "also broken" line.

Re-measured on the correct object, the headline negative of
`qbeta-habiro-delta-am-factorization` — *"no single polynomial factor unites all
m; the conjecture in C6 of the prior audit is FALSIFIED"* — **survives**: the
gcd across the corrected Δa_m is the constant 4, not a polynomial. Its published
`integer_content_gcd: 1` is **4** on the correct object, and the support moves
from m = 0..8 to m = 1..9. So the conclusion stands and the evidence needs
re-basing. Draining this cluster is a separate tranche; it is not done here, and
the C6 falsification should not be re-opened on the strength of this defect
alone.

## Why it survived

Nothing raises. `Σ Δa_m (u;u)_m` is a perfectly good polynomial; it factors, it
has cyclotomic content, it prints plausibly. The only signal that it is the
wrong polynomial is structural — a mirror difference must vanish at q = 1, so it
must carry Φ₁ — and no producer checked that. The corrected helper now raises
rather than proceed when half-integer powers survive denesting, but the Φ₁ check
is the one that would have caught this on day one and is worth adding to any
future pair-difference producer.
