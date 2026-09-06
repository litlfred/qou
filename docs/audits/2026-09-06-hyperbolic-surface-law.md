# The hyperbolic surface law: in `H³` the surface fraction never vanishes — and the framework's own `(ln A)/A` fits the residual **better** than the Euclidean import it replaces

**Date:** 2026-09-06 · **Beans:** `qou-j8hp` (this), `qou-yc1m` (the Stokes singular-count scaling,
opened as the open item), `qou-xpwx` (#6886), `qou-99rx` (#6801), `qou-glji` (#6780), `qou-kqdn`
(#6761), `qou-rav3`, `qou-20bk`, `qou-brng` · **Arc:** binding law / extensive term ·
**Scope:** formalize-first Lean (sorry-free, 14 declarations), a probe whose **pre-registered
expectation failed in the unexpected direction**, the non-abelian-Stokes / kite connection the owner
asked for, and a literature-holdings assessment. **Nothing is wired, nothing is fitted to
production; the surface *coefficient* stays free throughout.**

## 1. Why this, and what was on the record before it ran

Every surface-term tranche on this arc (#6761, #6780, #6801, #6886) imported the compact
**Euclidean** law `A_surf ∝ A^(2/3)`, and each time the corpus objected that the ambient geometry
is hyperbolic. `sm-26-parameter-chip-away.md:193-201` had measured that using `H³` consistently on
the *Coulomb radius* costs **2.64×** in scatter, and `qou-rav3` asked for "a packing argument
inside the framework" rather than a citation. This tranche is that argument for the surface
fraction. **Pre-registered, in the Lean header and the probe docstring before either ran: the
hyperbolic form was expected to fit worse.**

**Corpus-grep, six paths (path 0 unavailable — grep-open):** the `ln A` form exists in the corpus
**only** as the Coulomb-pairing *separation/radius* law (`em_linking_alpha_scaling_provenance_probe.py`,
scored by scatter of `κ(A)`, scope-(a)); it had never been written as a *surface* law or fitted
against the binding residual. `S/V → 2`, `4π sinh² R`, "surface fraction", `(ln A)/A`: **zero
hits**. No Lean formalisation of hyperbolic ball volume or area existed on the tree
(`QOU/Archimedean/HyperbolicMetric.lean` has the density `dx dy dz / z³`, no ball). Genuinely open.

## 2. The fact, and the Lean — `QOU/Mass/HyperbolicSurfaceLaw.lean` (14 decls, sorry-free, axiom-clean)

A ball of radius `R` in `H³` has `V = π(sinh 2R − 2R)` and `S = 4π sinh² R = 2π(cosh 2R − 1)`.
**The volume is Bolyai's formula and it is held** — `library/arxiv-1010.5321v3/` (Horváth,
*Formulas on hyperbolic volume*, §3.1, key `horvath2010`): `πk³ sinh(2x/k) − 2πk²x`, which at
`k = 1` is `hypVol`. The area is its derivative, and `hasDerivAt_hypVol` proves `V' = S`, so the
area rests on the held source too. **Nothing had to be ingested.**

In Euclidean space `S/V = 3/R → 0`, and that vanishing is the whole origin of the `A^(−1/3)` term.
In hyperbolic space it does not vanish:

    S − 2V = 2π (e^(−2R) + 2R − 1)  ≥  0        since  e^(−x) ≥ 1 − x

| declaration | statement |
|---|---|
| `two_mul_hypVol_le_hypArea`, `surfaceFraction_ge_two` | **`S/V ≥ 2` for every `R > 0`** — the boundary of a large hyperbolic ball is a *fixed* fraction of its volume |
| `eucFraction_eq`, `eucFraction_tendsto_zero` | the Euclidean contrast, `3/R → 0` |
| `not_hasBulk_of_fraction_ge` | generic: a surface fraction bounded below by a positive constant never satisfies `HasBulk` |
| **`hyperbolic_not_hasBulk`** | a hyperbolic-ball cluster fails `HasBulk` under **any** positive radius assignment `R(A)` |
| `hyperbolic_perNucleon_le` | its "surface term" is a **constant shift** of the volume coefficient: `B/A ≤ εk/2 − ε(k−k')` at every `A` |
| `surfaceFraction_sub_two_le` | residual `A`-dependence `f − 2 ≤ 4R/(sinh 2R − 2R)`, i.e. with `R ∼ ½ ln A`, of order **`(ln A)/A`** |
| `hasDerivAt_hypVol` | `V' = S` — the area from the held volume |
| `StokesSurfaceTerm`, `affine_over_affine_not_surfaceTerm` | the non-abelian-Stokes bridge, §4 |

`lean -DautoImplicit=false -s 65536` exit 0; `#print axioms` on all fourteen `= {propext,
Classical.choice, Quot.sound}`; zero `sorry`. **Not proved:** the limit `S/V → 2` itself (the
decay bound is proved; that its right side → 0 is checked numerically) and the `(ln A)/A`
asymptotic, which needs the inverse `R(A)`.

## 3. The probe — `computations/probes/hyperbolic_surface_law_probe.py`, **21/21**, and the expectation that failed

50 dps, 2548 measured AME nuclides, #6780's exact least squares; `B/A` on
`[1, φ(A), Z²/A^(4/3), (N−Z)²/A², δ/A^(3/2)]`.

| surface shape `φ(A)` | RSS | `R²` | `a_V` (MeV) | coef/`a_V` |
|---|---:|---:|---:|---:|
| Euclidean `A^(−1/3)` | 38.5325 | 0.96920 | 13.99 | −0.947 |
| **hyperbolic `(ln A)/A`** | **31.4432** | **0.97487** | 11.53 | −1.574 |
| chain `1/A` | 147.048 | 0.88247 | 10.06 | −2.395 |
| exact ball `S/V(R(A))`, `V = v₀A`, best `v₀ = 0.0826` | 35.1764 | — | — | — |
| best pure power `A^(−p)`, `p* = 0.364` (#6780) | 38.1934 | — | — | — |

**The pre-registered expectation failed: the framework's own geometry fits better than the
Euclidean import** — ratio 0.816 — and better than the best pure power at *any* exponent. The
exact ball also beats the import. Both are recorded in the probe as failed pre-registrations
converted to what was measured, with the record in-line; the probe was not changed to make them
pass.

**Genericity, by the `qou-rav3` / `qou-kqdn` discipline applied to my own win.** Two tests:

- A zoo of nine "reasonable" shapes — `A^(−1/4)`, `A^(−1/2)`, `A^(−2/3)`, `1/ln A`,
  `ln A/A^(1/3)`, `ln A/A^(1/2)`, `ln A/A^(2/3)`, `(ln A)²/A`, `1/A²`: **none beats the Euclidean
  import, and the hyperbolic `(ln A)/A` beats all nine** (their RSS run 43 → 580).
- The family `(ln A)^m/A^p` with `p` profiled at each `m`: `m = 0` reproduces #6780 exactly
  (`p* = 0.364`, 38.19); **`m = 1` optimises at `p* = 0.912`, within 0.09 of the hyperbolic
  `p = 1`**, RSS 28.46 — so `(ln A)/A` is near the optimum of its own family, not a lucky point on
  its flank.

**Two cautions the same probe surfaces, both stated rather than smoothed over:**

1. **The data prefer the shape, not a literal ball.** The exact ball's best `v₀ = 0.083` puts
   every nucleus at `R ∈ [0.34, 1.50]` — the *near-Euclidean* small-radius regime where
   `S/V ≈ 3/R` (at iron, `R = 1.3`, `S/V = 2.9` against `3/R = 2.3`) — and there its asymptotic
   `(ln A)/A` shape fits *better* than the ball itself (31.44 vs 35.18). A first version of the
   probe asserted the opposite order "because the exact form has one more free number"; that was
   logically wrong — the asymptotic with a free amplitude is not a member of the exact family —
   and is corrected in place.
2. **Log factors absorb structure.** Letting `m` float to 2 keeps improving (`p* = 0.34`, RSS
   21.90). So the hyperbolic point is the best **predicted** shape (no free exponent), not the
   global optimum of a two-parameter `(m, p)` search — the latter would be a fit, and is not
   claimed.

Two further check defects fixed in place: the `S − 2V` identity was tested at absolute `1e-40` and
failed at `R = 20` on cancellation alone (`S ∼ 7e17`); the derivative was tested by a central
difference with `h = 1e-20`, which divides 50-dps rounding by `2h`. Both now relative; both the
Lean's identities, not defects in them.

## 4. The non-abelian Stokes connection, and what "the surface of kites" is

Yekutieli's estimate (**held**, `library/arxiv-1007.1250v4/`; Def 4.4.12 / Lemma 4.4.13) bounds
the multiplicative-integral error by a **good** term counted by the `4^k` square **kites** of the
`k`-th binary tessellation of `I²` — an *area* count — plus a **bad** term `≤ a₀ + a₁·2^k`, one
dimension down, counted by the **singular points** of the surface map (`|bad| ≤ m`; `bad = ∅` if
the map is linear; confirmed in the held text at `sec-000-0-introduction.md:2280-2281`). So:

- **The surface of kites is the BULK of the Stokes estimate, not its surface term.** Kites are the
  area count. The 2026-08-30 audit reads the *surface* coefficient `a_S` as proportional to the
  singular count of the spanning surface of the nuclear braid closure.
- That is a bulk/boundary split, so `HasBulk`'s question applies to it verbatim
  (`StokesSurfaceTerm`): the singular count is a genuine surface term iff it grows without bound
  while vanishing as a fraction of the kite count.
- **Nobody has computed how the singular count scales with `A`** — the audit never states it, and
  no probe evaluates it for any nucleus. What the corpus does know is that every Seifert invariant
  of the canonical closure measured so far is **affine** (`every_seifert_invariant_is_affine_probe`:
  `χ = −9A+1`, `2g = 8A`, `σ = 6A−1`, six nuclei), so any fixed-mesh 2-cell count of the spanning
  surface is affine; and `affine_over_affine_not_surfaceTerm` proves an affine singular count over an
  affine cell count tends to a **nonzero constant** ratio — verified numerically on the four
  measured invariants against the affine kite-tail `3A − 1` (ratios → 4, −3, 8/3, 2). **So if the
  singular count is affine, the Stokes route does exactly what the hyperbolic ball does:
  renormalise the volume term and supply no `A^(−1/3)`.** Whether it is affine is the open
  computation, opened as bean **`qou-yc1m`** rather than guessed.

Two homonyms kept apart: the "kite-tail" `(1 + r²)^(3A−1)` is a Hecke cyclotomic factor of `tr_M`,
not a 2-cell, and its exponent is affine — #6801 already excludes it as a surface term; and bean
`qou-20bk` with `QOU/LiftingDescent/CrossedModuleSurfaceHolonomy.lean` (sorry-free) has settled that
no 2-dim Yekutieli object carries a non-abelian 3-body term. Kites are not where a many-body term
lives; the only 3-body-shaped object in the book is the balloon `∫γ`, abelian and extensive.

## 5. Literature holdings — the assessment the owner asked for

| work | status | needed here? |
|---|---|---|
| Yekutieli, *Nonabelian multiplicative integration on surfaces* (+ 12 other Yekutieli, Broda, Schreiber–Waldorf, Martins–Picken) | **HELD** (`arxiv-1007.1250v4`; all Yekutieli keys held since `qou-3pck`, 2026-09-05) | cited |
| **Bolyai's ball volume in `H³`** — Horváth, *Formulas on hyperbolic volume* §3.1 | **HELD** (`arxiv-1010.5321v3`, key `horvath2010`) — nobody had cited it for this | **cited; area derived from it in Lean** |
| Thurston notes | held, Ch 1–2 only (33 pp); hyperbolic trig, no ball | — |
| Ratcliffe GTM 149; Benedetti–Petronio | **registered-only** (`references.ts:4417`, `:4438`); textbook-without-PDF is the accepted norm | not needed |
| Martelli, *An Introduction to Geometric Topology* (arXiv:1610.02592, free) | **absent** | optional — a held area/isoperimetry statement |
| Bethe–Weizsäcker 1935 / Bethe–Bacher 1936 | **registered-only** confirmed (`:15434`, `:15412`) | not for this |
| Harborth 1974 / Bezdek–Reid contact numbers (arXiv:1210.5756) | **absent** on 639 dirs, confirmed | not for this; would close #6886's "cited without a held source" and `MaxContactSimplex.lean:184`'s uncited Schütte–van der Waerden |
| hyperbolic isoperimetry / Cheeger of `H^n` (Schmidt 1940; Chavel 2001; Ni's arXiv note) | **absent** — all 33 "isoperimetric" hits are probability | optional |

**Judgement (mine):** nothing needs ingesting for this tranche — the one external fact it uses is
held. If the owner wants the area and the `S/V → 2` limit to rest on a held *statement* rather than
a held *derivation*, ingest **Martelli** (free). If the previous tranche's contact-number citations
are to be made held rather than deliberately omitted, ingest **Bezdek–Reid arXiv:1210.5756**.

## 6. Verdict and scope

- **Scope-(b), unconditional:** a hyperbolic-ball cluster has no bulk under any radius assignment;
  its surface term is a constant renormalisation of the volume coefficient. Proved, not fitted.
- **Scope-(a), the finding:** the framework's own `(ln A)/A` shape describes the AME residual
  **better** than the imported Euclidean `A^(−1/3)`, by RSS 31.44 vs 38.53, robustly against nine
  alternative shapes and near the optimum of its own family — against a pre-registered expectation
  of the opposite. **This is a statement about the *shape*, not the coefficient**: `a_V`, the
  surface coefficient, and the volume-per-nucleon all stay free. **Nothing here derives `a_S`.**
- **Not claimed:** that the nucleus *is* a hyperbolic ball (the best-fit ball sits in the
  near-Euclidean regime; the data prefer the asymptotic shape); that the substrate emits such a
  cluster (`qou-brng`, unchanged); or that the `(ln A)/A` form is the *right* form as opposed to
  the best *predicted* one — a free `(m, p)` search does better and is a fit.
- **The Euclidean placement of the coordination graph is an unexamined import** — named as such:
  `EquilateralBound`, `EquidistantCoordinationCap`, `MaxContactSimplex` and `coulomb_energy.py`'s
  `R₀·A^(1/3)` all assume `ℝ³` and none derives it; the equidistant cap and kissing number in `H³`
  at fixed edge length differ and would need re-proving there. No theorem places the graph in either.

## 7. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The Lean, the finding and its cautions are on the record;
  `qou-yc1m` holds the Stokes computation. Cost 0.
- **Compute the Stokes singular count's `A`-scaling (`qou-yc1m`).** The one route that could give a
  *derived* surface term with its coefficient. Cost: formalize-first on the spanning surface of the
  canonical closure — the trefoil discretisation (`YekutieliTrefoilDiscretization.lean`) is the
  starting point. Risk: if it is affine, as every other Seifert invariant is, it joins the
  volume-renormalisation column and the answer is a negative worth having.
- **Re-prove the equidistant cap and coordination bound in `H³`.** If the graph's placement is to
  stop being an import, the four-point cap (`EquilateralBound`) and the kissing-number bound must be
  re-established at fixed edge length in `H³`, where both differ. Cost: a Lean tranche. Risk: the
  hyperbolic kissing configuration at the framework's edge length may not be the fcc 12, which would
  move `k` — that is information, not a fit.
- **Do not** promote `(ln A)/A` to a production surface term. It has a free coefficient and this is
  not the tranche that derives it.

**Recommendation (judgement):** the second. It is the only route on the board whose *coefficient*
could be derived rather than fitted, the held text supports it, and both outcomes are useful.

## 8. Verification

- `lean -DautoImplicit=false -s 65536` exit 0; 14 declarations axiom-clean; 0 `sorry`; the
  four imported oleans (`CoordinationSaturation` → `CoordinationBulkCriterion`) rebuilt lean-direct
  from the current `main`.
- Probe 21/21, mpmath 50 dps, no float64; two check-precision defects and one logically wrong check
  corrected in place and recorded in §3; two failed pre-registrations recorded, not removed.
- `scripts/precision-gates.sh --changed`: recorded in the PR body.
- The corpus-grepper's memory files (`.claude/agent-memory/corpus-grepper/`) were updated by the
  survey and are committed with this PR, per the memory-maintenance rule.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
