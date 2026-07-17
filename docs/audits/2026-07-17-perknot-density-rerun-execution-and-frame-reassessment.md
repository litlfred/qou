# Per-knot density re-run execution + frame reassessment (bean qou-sqgf)

**Date:** 2026-07-17 · **Base:** current `main` (`074dfccb4a`) · fresh branch
`claude/lambda-a-perknot-salvage-ka-ext-2026-07-17` (the 2026-07-02 branch's PR
#3205 was closed-unmerged; work re-derived on current main, not rebased).

## What this closes

The λ_A refutation-artifact audit
([`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](2026-06-24-lambda-a-refutation-artifact-audit.md))
localised 7 refutations that baseline on the fitted global scalar λ_A
(`vol_density_borromean` ≈ 2.533) and set a re-run protocol — its "Next
(under x5az)" steps 1–3 ("re-run … with `vol_density_per_block` … repeat for
the 6 others … record verdict"). Bean `x5az` completed the **static
inspection** but the audit flags twice that the verdicts "require the actual
re-run." Those runs were never executed on `main`. This backfill executes all 7
against the **canonical per-knot Markov trace** `tr_M(K)`
(`vol_density_per_block`, chi-cache, p≠n-distinct: proton 1.0653062380758782,
neutron 0.9232333051498377 — verified identical on current `main`, so not
affected by the #3783 trace-engine kernel bug).

Scripts + witnesses: `computations/probes/*_perknot_rerun.py` /
`*-perknot-rerun.witness.json` (7 each). All EXPLORATORY, `production_wired:
false`, no new fitted constants, every negative scoped (a). Regenerated fresh on
current `main` (70 dps compute, canonical muon-q₀); all `allPassed: true`.

## Verdict table

| # | Refutation | Per-knot verdict |
|---|---|---|
| 1 | co-Casimir Δ_λ = 1/dim_q (#602) | **ROBUST** — density-independent sum unchanged; failure ≥30× under every base |
| 2 | color-vs-charge T/³He | **ROBUST** — λ_A cancels algebraically (was a normalization, not a density under test); split base-independent to 30 dps |
| 3 | L1 multiplicative λ(K) (#1874) | **ROBUST** — per-knot fails *harder* on every atom |
| 4 | ³He residual λ_A/2 (#1882) | **ROBUST** — λ_A/2 confirmed family numerology; honest lead: bare tr_M(p)²·tr_M(n) within 25 % with no rescaler |
| 5 | **additive S(K) (#1876)** | **PARTIALLY ARTIFACT** — the refutation's sign-flip **disappears** on the per-knot base (S_emp > 0 all six atoms; S/(A·m_e) uniform to ×1.73). Caveat: S is order-of-mass at A ≥ 2 |
| 6 | T2 Vol-convention (#1891) | **ROBUST** — swings 2610–7545 % under all three Vol conventions |
| 7 | T4 Schur–Weyl derive-λ_A | **ROBUST** (retargeted) — 0/140 aggregates MATCH; 1 NEAR is look-elsewhere noise |

**Net:** 1 of 7 (additive S(K)) is the informative verdict-changer; the other 6
extend to the per-knot base, all scope (a).

## Frame reassessment (2026-07-17 — read before building on this)

The GAP-A-4 landscape moved substantially between 2026-07-03 and 2026-07-17.
This backfill closes an honest documented loop, but the **organizing question of
the 2026-07-02 GAP-A-4 scoping note ("derive the per-knot density rule ρ(K)") is
superseded**:

- **Magnitude base CLOSED:** `|Δ_λ| = classical dim(λ)` (#3537) — the substrate
  q-dim / per-knot trace the note chased is not the magnitude carrier.
- **Sign CLOSED:** `sgn = (−1)^{n(λ)}` (g_ρ jet-order grading, 2026-07-11).
- **Only open gap:** the derived **k(A) extensivity / level-selection rule**
  (GAP-A-3; μ_ext = 5.85/4.44/3.29/9.31 non-monotone in A).
- **Δ_λ gate generally reversed** (#3723) — route restriction void; anti-fit
  discipline kept.
- **Provenance:** the note's invariants I-1 (p/n-degeneracy), I-2 (bar-parity),
  I-6 (trace-convention pin) already landed on `main` verbatim as the Lean gate
  trio (`TraceConventionGate.lean` → `no_uniform_scalar_density`,
  `traceConvention_factor_determined`; `BarParityExclusion.lean`). I-3's
  "linear-in-A" guess was corrected to logarithmic on `main`.

The **one** live thread from this work is verdict #5: the per-knot additive S(K)
family, reframed in binding-ratio form (scale cancels — matching `main`'s
"per-knot leverage is binding, not absolute mass"), with its ×1.73 A-scaling
regularity examined for a link to the open k(A) extensivity gap. Pursued under
bean `qou-cqqs`, honoring the `adhb` gate (Term-5 BW-fit forbidden). The other 6
verdicts are recorded here as confirmatory negatives, not a research thread.
