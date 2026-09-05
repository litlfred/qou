# The surface exponent is not free, and the production chain's value is excluded by the data — but the inverse-dimension reading is **not** thereby established

**Date:** 2026-09-05 · **Beans:** `qou-glji` (this), `qou-kqdn` (#6761, the ratio this replaces),
`qou-rav3` (the genericity guard), `qou-7e67` (the recorded dimension negative, distinguished),
`qou-brng`, `qou-3wvl` · **Arc:** binding law / extensive term · **Scope:** formalize-first Lean
(sorry-free) plus a probe that **rejects the framework's own production graph** and **fails a
pre-registered expectation**, both recorded. **Nothing is wired, nothing is fitted.**

## 1. Why, and what #6761 left

#6761 (`qou-kqdn`) proved the boundary deficit of a bounded-degree bond count gives the SEMF
volume-minus-surface **shape** exactly, and then disqualified its own magnitude result: the
surface-to-volume ratio `a_S/a_V = c(k−k')/k` reaches **67.9 %** of its plausible window as the
facet and shell treatment are varied, the same failure mode `qou-rav3` measured at 73.7 % for `k`.
Its §6 recommendation was to attack the remaining free number from the braid side.

This tranche takes the other half of the split instead. In `B/A = ε·k/2 − (ε(k−k')/2)·(A_surf/A)`
the ratio sets the *amplitude*; the surface fraction sets the *`A`-dependence*. Under the compact-
cluster hypothesis `A_surf ∼ c·A^((d−1)/d)` that fraction is `c·A^(−1/d)`, so the **exponent** is
the candidate dimension probe — and unlike the amplitude it is not free to be chosen.

## 2. Corpus-grep, six paths — and the verdict split three ways

**Path 0 unavailable** (the `paper-assistant` MCP server failed to connect, `ENOENT`), so these
are grep-open, not graph-open.

| question | verdict |
|---|---|
| has the exponent `p` in `B/A = a − b·A^(−p)` ever been **measured**? | **open** |
| has it been read as an **inverse dimension**? | **open**, with an adjacent recorded negative |
| is the chain's `A^(−1)` correction known? | **CLOSED, and it predates this work** |

**The third row is the one that changes what may be claimed.**
`QOU.MassTheory.ChainBindingNoSaturationPeak.chainPerNucleon_eq_hyperbola` already proves, by
`ring`, that an isobaric chain's per-nucleon binding is **exactly** `c₁ + c₂/A` — which is
`a − b·A^(−1)`. So the chain's `A^(−1)` scaling is a corpus fact. **This work re-derives it from
the boundary DEGREE** (two endpoints of degree 1 against interior degree 2), where the corpus
carries the same deficit only as a bond count ("an open `A`-chain has one fewer bond than
nucleons", `2026-06-15-delta-lambda-offset-open-chain-boundary.md`). The degree reading is what
makes it an instance of `CoordinationSurfaceDeficit` rather than an isolated arithmetic fact —
but the scaling is not a discovery and is not reported as one.

Three further prior results are cited in the Lean rather than left to be found by a reviewer:

- `QOU.Mass.AffineCountIsNotASurfaceTerm` — independent scope-(b) route to "affine is not a
  surface term" via monotonicity of `(12A−1)/A^(2/3)`. `A − 1` is affine, so it covers this graph.
- The Faddeev–Niemi verdict's scope-(b) exclusion: no pure power law reproduces a non-monotone
  `B/A`. `a − b·A^(−p)` is monotone too, so the exponent measured here is the **deficit's**, with
  Coulomb carried separately — as `QOU.Mass.SaturationPeakStructure` sets the problem up.
- Bean `qou-7e67`, *"Is the exponent a DIMENSION question? NO: no single exponent fits"*. That
  tests `R ∼ A^x` for the **radius** over `A ≤ 4`, varying `d` over ambient manifolds. Different
  object, different observable; it does not transfer, and is cited so it is not thought missed.

**The sharpest objection, met rather than avoided.** The corpus's only *derived* three-dimensional
coordination object is the deltahedron contact graph, and by Euler it has `E = 3A − 6` — still
affine, so it also gives `A^(−1)`. A convex deltahedron puts every nucleon on the boundary: `d = 3`
geometrically, with no bulk. `A_surf ∼ c·A^((d−1)/d)` needs a bulk, so this is precisely the case
where the inverse-dimension reading fails.

## 3. Lean — `QOU/Mass/SurfaceExponentIsDimension.lean` (sorry-free, 7 declarations axiom-clean)

| declaration | statement |
|---|---|
| `chain_bondCount` | the path graph's bond count is `A − 1` at `k = 2, k' = 1, A_surf = 2` |
| `chain_perNucleon` | `B/A = ε − ε/A` — the chain, exactly |
| `chain_is_dimension_one` | the chain is the `p = 1` member of `a − b·A^(−p)` |
| `perNucleonExp` / `chain_eq_perNucleonExp` | the family, and the chain's place in it |
| **`perNucleonExp_exponent_inj`** | **distinct exponents are distinct functions of `A`** — no amplitude can disguise a wrong exponent |
| `chain_ne_semf` | the chain's law differs from any `p ≠ 1` law at some `A > 0` |
| `perNucleon_surfaceExponent` | feeding `A_surf/A = c·A^(−1/d)` into `perNucleon_split` gives `perNucleonExp` with `p = 1/d` |

`lean`-direct exit 0 (2.9 s); `#print axioms` on all seven `= {propext, Classical.choice,
Quot.sound}`; zero `sorry`. Ground ring `ℝ` (§7c: real powers).

`perNucleonExp_exponent_inj` is the load-bearing one: it is what makes the exponent a *test*
rather than a *parameter*, and it is what distinguishes this from #6761's disqualified ratio.

## 4. Probe — `computations/probes/surface_exponent_is_dimension_probe.py`, **19/19**

50 dps, 2548 measured AME nuclides, #6611's selection. `p` is **profiled**, not searched: at fixed
`p` the model is linear in its coefficients, so each `p` is one exact least-squares solve and the
minimisation is a grid plus golden section — no starting guess, no gradient, no nonlinear solver.

Basis: `B/A = a_V − b·A^(−p) − a_C Z²/A^(4/3) − a_A (N−Z)²/A² + a_P δ/A^(3/2)`.

**Controls reproduce #6761 on its own basis** (which had no pairing column): `a_S/a_V = 0.960671`
and `R² = 0.96406` at `p` fixed to `1/3`, matching its 0.9607 / 0.964.

**Result.**

| quantity | value |
|---|---|
| profiled `p*` (all nuclides) | **0.363999**  →  `d = 1/p* = 2.7473` |
| 1 %-RSS interval | `p ∈ [0.3315, 0.3969]`  →  `d ∈ [2.519, 3.017]` |
| `RSS(p*)` / `RSS(1/3)` / `RSS(1)` | 38.19 / 38.53 / **147.05** |
| `R²` at `p*` | 0.96947 |

**The production chain is rejected.** `p = 1` costs 3.85× the minimum RSS, lies outside the
1 %-RSS interval, and is excluded under **every** analysis variant tried (no variant's `p*` exceeds
0.583). This is the tranche's positive result and it is robust.

## 5. The finding against my own reading — a pre-registered expectation that FAILED

I expected the analysis variants to agree, so that any spread would be loss of constraint rather
than disagreement, and pre-committed to a threshold (a variant is "constraining" if its 1 %-RSS
interval is narrower than 0.30 — the same threshold already used for the main result). **Every
variant constrains `p`, and they disagree anyway:**

| variant | n | `p*` | `d = 1/p*` | 1 %-RSS width | constrains? |
|---|---:|---:|---:|---:|---|
| full basis, all nuclides | 2548 | 0.3640 | 2.747 | 0.065 | yes |
| A ≥ 16 | 2484 | 0.5700 | 1.754 | 0.062 | yes |
| A ≥ 40 | 2301 | 0.5823 | 1.717 | 0.082 | yes |
| no pairing column | 2548 | 0.4027 | 2.483 | 0.067 | yes |
| N = Z ± 1 only, no asymmetry column | 128 | 0.2292 | 4.364 | 0.134 | yes |

The all-nuclide interval `[0.331, 0.397]` and the A ≥ 40 interval `[0.542, 0.624]` are
**disjoint**. So **no single power-law exponent describes the whole chart**, and the fitted
"dimension" drifts from 2.75 to 1.72 with the mass cut. The expectation was wrong; the probe is
not. This is recorded in the probe source and asserted as a check, not dropped.

**Genericity, by `qou-rav3`'s method applied to my own quantity** (the discipline #6761 established
by disqualifying itself): the exponent reaches **17.66 %** of its plausible window `[0, 2]` across
the five variants, against **67.9 %** for #6761's ratio and **73.7 %** for `qou-rav3`'s `k`. So the
exponent is far less generic than either — which is why `p = 1` can be rejected — but 17.66 % with
disjoint intervals is not a clean one-number measurement either.

## 6. Verdict and scope

- **Scope-(a) negative against the framework's own production graph, and it is the main result.**
  The braid word's path graph is `d = 1` and predicts `p = 1`; the data reject `p = 1` at every
  analysis choice. Combined with `AffineCountIsNotASurfaceTerm`'s scope-(b) exclusion of affine
  counts, the production word cannot supply the surface term, and the obstruction is the graph's
  dimension rather than any tuning of `ε`, `k` or `k'`.
- **Scope-(a) positive, weak:** the full-sample exponent `0.364` is close to `1/3`, and `p = 1/3`
  costs only 0.9 % more RSS than the optimum.
- **The inverse-dimension reading is NOT established.** Two independent reasons: the mass-cut
  drift above, and the `E = 3A − 6` objection — the corpus's only derived 3-D coordination object
  is surface-only, so it has `d = 3` with no bulk and the hypothesis does not apply to it.
- **Does not close Avenue 2**, and now sharpens it differently from #6761: Avenue 2 wants an edge
  set from the braid geometry. #6761 asked "what fixes `1 − k'/k`?"; this asks the prior question
  **"what edge set has a bulk at all?"**, since the two derived candidates on `main` (the chain's
  `A − 1` and the deltahedron's `3A − 6`) are both affine and both give `A^(−1)`.

## 7. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The chain rejection and the failed expectation are both on the
  record. `qou-brng` and `qou-3wvl` are unaffected. Cost 0.
- **Take the sharpened question: find a derived edge set with a bulk.** Both derived candidates
  are affine, and an affine count can never be a surface term (`AffineCountIsNotASurfaceTerm`,
  scope-(b)). So the open item is whether the substrate emits any coordination object that is not
  affine in `A`. Cost: a formalize-first tranche. Risk: the answer may be that it does not, which
  would be a scope-(b) closure of Avenue 2 rather than a route into it — a negative worth having,
  and cheaper to reach than the amplitude.
- **Investigate the mass-cut drift as physics rather than as noise.** `p` moving 0.36 → 0.58 with
  disjoint intervals is a statement about the data, not about the framework: it says the SEMF
  surface term is itself a poor description away from the light end. Cost: a probe. Risk: this is
  nuclear-structure phenomenology, some distance from the substrate, and may not repay the tranche.
- **Do not** quote `d = 2.75` as a measured dimension. It is one analysis choice among five that
  disagree.

**Recommendation (judgement):** the second. It is the question both derived candidates now point
at, it is decidable by a proved invariant rather than by a fit, and a negative on it would close
Avenue 2 outright instead of leaving the amplitude open indefinitely.

## 8. Verification

- `lean`-direct exit 0 on `SurfaceExponentIsDimension.lean` (2.9 s); 7 declarations axiom-clean;
  0 `sorry`; imported `CoordinationSurfaceDeficit.olean` built lean-direct from `main`.
- Probe 19/19, including the two controls reproducing #6761 on its own basis, a cross-check that
  the chain law is the hyperbola `ChainBindingNoSaturationPeak` proves, and the monotonicity
  caveat (the surface term alone is monotone; the fitted model turns over at A = 58 against AME's
  measured peak at A = 62, and only because Coulomb is carried separately).
- No float64: every reported quantity asserted to be an `mpmath.mpf`.
- `scripts/precision-gates.sh --changed` — result recorded in the PR body.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
