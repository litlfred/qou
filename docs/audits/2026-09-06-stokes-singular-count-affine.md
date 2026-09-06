# The Stokes singular count: Euler bounds the 1-skeleton below by `9A + 1`, and the reading that made it a count was the 1-dimensional case imported into 2-dim

**Date:** 2026-09-06 · **Beans:** `qou-yc1m` (this), `qou-h7w4` (the correction to the 2026-08-30
audit and to my own #6929 header), `qou-d5hn` (the `μ = A + 1` conditional-proved trap),
`qou-j8hp` (#6929), `qou-20bk`, `qou-prjo`, `qou-brng` · **Arc:** binding law / extensive term ·
**Scope:** formalize-first Lean (sorry-free, 5 declarations), a probe that re-derives every premise
from the production braid word, a **correction to a merged reading including my own**, and a
conclusion that is honest about being conditional. **Nothing is wired, nothing is fitted.**

## 1. The question, and what was open

#6929 bridged Yekutieli's non-abelian Stokes estimate to the bulk criterion and left one open
computation: how the singular count of the "bad" term scales with `A` for the spanning surface of
the nuclear braid closure. **Corpus-grep, six paths (path 0 unavailable — grep-open):** no
Euler/cut-locus/polygon-presentation bound on the Seifert surface exists anywhere on the binding
axis; Euler appears in the corpus only for Bring's `χ = −6`, the deltahedron saturation law, and a
spectral-sequence Euler–Poincaré. Genuinely open — **but the claim shape failed at the held text
before any search was needed**, and that is the main finding.

## 2. The correction — Yekutieli's 1-dimensional statement had been imported into 2-dim

`docs/audits/2026-08-30-nonabelian-stokes-and-the-surface-term.md` §2 reads the bad set as
*"counted by the singularities of the map defining the surface"*, quoting `|bad(k)| ≤ m` with `m`
the number of singular points of `σ`. **That is the 1-dimensional string case** — held text
`library/arxiv-1007.1250v4/sections/sec-000-0-introduction.md:2280`. I repeated it in #6929's
`HyperbolicSurfaceLaw` header. In the **2-dimensional** case:

| held text | what it says |
|---|---|
| Def 4.1.1, `:3278` | the kite map `τ : I² → X` **is a linear map** — it has no singular points |
| Def 4.4.12, `:3964` | an index is **good iff the forms `α|Zᵢ` and `β|Zᵢ` are smooth**; otherwise bad |
| Lemma 4.4.13 proof, `:3969-3976` | cover *"the singular locus of α and the singular locus of β"* by `m` segments `Zⱼ`; **`a₀ := 2m`, `a₁ := 2·Σ len(Zⱼ)`** |

Three consequences, each of which changes what the arc can claim:

1. **The bad set is the singular locus of the connection, not of the surface parametrization.**
   Any Euler argument about cell decompositions reaches it only through a hypothesis about where
   the forms are singular.
2. **`a₁` is a length, not a count.** "`a_S ∝` a count of singularities" can refer only to `a₀`.
3. **Smooth forms give no bad set at all** — `a₀ = a₁ = 0` on every surface at every `A`. A Stokes
   surface term *requires a singular connection*. And the corpus has no `(α, β)` as forms
   (`qou-20bk`: *"Step 2's curvature is stipulated, not a form"*).

Opened as `qou-h7w4`; the #6929 header is corrected on this branch.

## 3. The Lean — `QOU/Mass/StokesSingularCountAffine.lean` (5 decls, sorry-free, axiom-clean)

| declaration | statement | tier |
|---|---|---|
| `edges_ge_two_sub_chi` | any cell decomposition with `V ≥ 1`, `F ≥ 1` has `E = V + F − χ ≥ 2 − χ` | proved, Euler |
| `edges_ge_of_chi_canonical` | at `χ = −9A + 1`: `E ≥ 9A + 1` | proved |
| `chi_of_genus_boundary` | `2 − 2g − μ = −9A + 1` from `2g = 8A`, `μ = A + 1` — the three invariants are mutually consistent | proved |
| `not_stokesSurfaceTerm_of_bounds` | a boundary count eventually `≥` an affine function with positive slope, over a bulk count eventually positive and `≤` an affine function, is not a `StokesSurfaceTerm` | proved |
| `stokes_canonical_not_surfaceTerm` | **under `hsing` = (H1)**: over the Seifert cells `15A − 1`, not a surface term | proved, conditional |

`lean -DautoImplicit=false -s 65536` exit 0; all five `{propext, Classical.choice, Quot.sound}`;
zero `sorry`. The Euler bound is sharp (the one-vertex polygon attains it) and **generalises two
exact counts the corpus already holds** — `AffineCountIsNotASurfaceTerm.crossingCount = 12A − 1`
and `TransverseSurfaceCurvature.seifertBettiOne_extensive` (`1 − χ` affine for all `A`) — from one
decomposition to all of them. It is not a new number.

## 4. The probe — `stokes_singular_count_affine_probe.py`, 11/11, exact arithmetic

Every premise is re-derived from **the production word**, not from a table: `atom_braid_word_3A`
has exactly `12A − 1` letters at `A ∈ {2, 4, 6, 8, 12, 16}`; with `3A` strands the disk-band
Seifert surface has `χ = n − c = −9A + 1`, `15A − 1` cells, and with `μ = A + 1` components
`2g = 8A`. `χ` is therefore **computed**, not measured — and `12A − 1` is derived for all `A`
(`qou-hu1f`: *"the fit was right and is now derived"*). The Euler bound `9A + 1` is exactly linear
(slope 9, second difference 0); the ratio `(9A+1)/(15A−1)` is `≥ 3/5` at every `A` and tends to
`3/5`. The canonical closure's genus `4A` is exactly linear, so no sublinear-`χ` surface is on
offer.

## 5. What this establishes, in three tiers

- **Unconditional (scope-(b)):** the 1-skeleton of *any* cell decomposition of the canonical
  closure's spanning surface grows at least linearly in `A`. No parametrization escapes Euler.
- **Conditional on (H1) (scope-(a) on the premise):** *if* the connection forms' singular locus
  runs along such a 1-skeleton, the Stokes bad-set constant inherits the bound and the Stokes route
  renormalises the volume coefficient — the same conclusion as the hyperbolic ball, for the same
  structural reason: a boundary that is a fixed fraction of the bulk.
- **Not dischargeable now:** (H1) itself. The corpus has no `(α, β)` as forms. Two named ways out:
  smooth forms, which give *no* Stokes surface term at all; or a singular locus that is a **proper
  sub-complex** of sublinear total edge count — Euler forbids that for the whole skeleton but not
  for a subset, so **(H1) is exactly where the remaining content is.**

**Two traps found and recorded.** `μ = A + 1` is a *hypothesis* `(hmu : mu = A + 1)` in
`SLq2LabelParity.lean:77` and `TorusKnotPages.lean:82`, yet `total_curvature_is_the_computable_half_probe.py:43`
and its witness cite it as *"(exact, Lean-proved)"* — conditional-proved ≠ premise-established;
the only derivation is probe-level (`qou-d5hn`). And `YekutieliTrefoilDiscretization.lean` cites
bean `qou-jqof`, which does not exist.

## 6. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The bound, the correction and the conditional are all on the
  record; `qou-h7w4` carries the audit fix. Cost 0.
- **Fix the 2026-08-30 audit in place (`qou-h7w4`).** Its §2 states the 1-dim case as the 2-dim
  one and its §3 draws "`a_S ∝` a count" from it. Cost: a few lines. Risk: none; it is a citation
  correction against held text. Recommended regardless of what else is chosen.
- **Stop opening surface-term tranches on this arc until the framework has `(α, β)` as forms.**
  Five tranches (#6761 → this) have now established: the hyperbolic ball's surface fraction is
  bounded below unconditionally; every affine edge set is `p = 1`; the sub-affine shape is
  excluded on light nuclei; and the Stokes route yields a surface term only from a singular
  connection the corpus does not have. What survives is the empirical `(ln A)/A` **shape** (#6929)
  with a free coefficient. The next derivable step is upstream — a connection form — not another
  surface geometry. Cost 0 now; this is a stop, not a task.
- **Do not** attempt to discharge (H1) by choosing a singular locus. That is selecting the premise
  against the conclusion, the fit signature.

**Recommendation (judgement):** the second, then the third. The arc has reached the point where
its open input is a *connection*, and that is `qou-brng`'s territory, not a surface-term
question.

## 7. Verification

- `lean -DautoImplicit=false -s 65536` exit 0 on `StokesSingularCountAffine.lean` (5 axiom-clean,
  0 `sorry`) and on the corrected `HyperbolicSurfaceLaw.lean` (rebuilt as its dependency).
- Probe 11/11; exact `int`/`Fraction` throughout, mpmath only for the limit; no float64.
- The corpus-grepper's memory files updated by the two sweeps are committed with this PR.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
