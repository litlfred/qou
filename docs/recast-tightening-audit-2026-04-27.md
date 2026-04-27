# Recast / tightening audit (Apr 2026)

This document is the deliverable for the inventory sweep that
accompanies the pre/post-Archimedean recast plan applied in
`copilot/explore-analogues-sqrtq` (mirrors the recast pattern from
`claude/mass-units-bridge-followups` commit `7588970f`).

## Part B — dual-leg / asymptotic-bridge candidates

Grep across `content/quantum-observable-universe/**/*.md` for
"geometric leg / algebraic leg / two legs / both legs / the two agree"
returned **one** file, `partition-sum-proton-residual.md`, where
"the two" referred to two numerical values (q-deformed vs classical
limit), **not** the dual-leg structure. Result: no other true
dual-leg blocks exist on `main`; the one canonical case
(`atom-knot-mass-derivation`) is recast on the followups branch.

Grep for `mostow1968 / gromov1982 / kashaev1995 / murakami2001 /
thurston1978` cites returned 4 files. All 4 are already conjectures,
remarks, or genuinely post-Archimedean propositions
(`thurston-volume-additivity` literally states Thurston's theorem).
**Result: no core proposition borrows volume conjecture / Mostow /
Gromov / Kashaev for derivations.**

The only block on `main` that needed a recast in this pass was
`algebraic-quantum-volume-specialization.md` (route 1 and route 2
explicitly flagged as **post-Archimedean borrowed naming**;
route 3 is the only QOU-internal step). Done in this PR.

## Part C — paper-wide tightening

| Item | Status | Notes |
|------|--------|-------|
| C1: drop "why this is absent from core" passages | partial | Ribbon block done; $\tau$-suppression and categorical-instanton are already concise (no such passages). |
| C2: Markov-trace decomposition single canonical statement | OK | Only 5 files mention $\sum_\lambda y_\lambda \chi_\lambda$; canonical statement is `thm:jones-markov-trace` + `prop:alpha-k-derivation-procedure`. No rampant duplication. |
| C3: move illustrative $y_\lambda$ computations to witness JSON | deferred | Editorial pass; needs per-block judgment. The followups branch has already moved several to `folio-assistant/computations/*.witness.json`. |
| C4: unify Markov-trace symbol | done | Paper is 92% consistent on `\mathrm{tr}_M`; 7 brace-variants `\mathrm{tr}_{M}` normalized. |
| C5: cap proof length at ~40 lines | audit only | 25 proof blocks exceed 40 lines (list below). Refactoring requires per-block judgment (split proposition vs. extract sub-proof). Recommend doing as a separate batch with peer review. |
| C6: transitive prune | done | `pipeline/prune-transitive-deps.ts --apply` removed **1797** transitive edges across **643** files; validation issue count 204 → 197 (7 unresolved-uses errors fixed as bonus). |

## Proof-length audit (Part C5 deferred list)

Proof blocks exceeding 40 lines, ordered by length:

| Lines | Block |
|------:|-------|
| 169 | `lifting-and-descent/topological-mass-proof.md` |
| 111 | `quantum-observable-universes/quantum-observable-universe-exists-proof.md` |
| 103 | `quantum-observable-universes/su2-emergence-proof.md` |
| 100 | `observations/terminal-resolution-proof.md` |
|  95 | `braids-and-knots/topological-mass-categorical-proof.md` |
|  93 | `braids-and-knots/feynman-categorical-trace-proof.md` |
|  82 | `descartes-universe/genus-filtration-ideal-proof.md` |
|  69 | `lifting-and-descent/descent-condition-proof.md` |
|  61 | `lifting-and-descent/cosimplicial-crossed-groupoid-proof.md` |
|  59 | `lifting-and-descent/jet-prolongation-proof.md` |
|  57 | `quantum-observable-universes/fiber-adjoint-involution-proof.md` |
|  57 | `descartes-universe/brings-is-qou-proof.md` |
|  55 | `descartes-universe/mi-sw-abelianisation-proof.md` |
|  53 | `braids-and-knots/transfer-matrix-level-independence-proof.md` |
|  53 | `braids-and-knots/non-self-intersection-proof.md` |
|  53 | `braids-and-knots/mobius-energy-proof.md` |
|  51 | `braids-and-knots/skein-generation-proof.md` |
|  50 | `lifting-and-descent/euler-char-stability-proof.md` |
|  48 | `quantum-universes/frobenius-relation-proof.md` |
|  46 | `observations/skein-mass-relation-proof.md` |
|  46 | `lifting-and-descent/vacuum-state-proof.md` |
|  45 | `quantum-observable-universes/substrate-parameter-unique-proof.md` |
|  44 | `lifting-and-descent/qu-to-qou-proof.md` |
|  43 | `quantum-observable-universes/categorical-dq-squared-proof.md` |
|  43 | `lifting-and-descent/descent-lemma-proof.md` |

Top targets for splitting (over 80 lines):
`topological-mass-proof`, `quantum-observable-universe-exists-proof`,
`su2-emergence-proof`, `terminal-resolution-proof`,
`topological-mass-categorical-proof`, `feynman-categorical-trace-proof`,
`genus-filtration-ideal-proof`. Each is a candidate for either
(a) splitting the parent statement into two propositions, or
(b) extracting a key lemma into its own block referenced by `proves`.

## Items that depend on the followups branch landing first

- **Part B step 4: collapse Lean `PipelineStage` enumerations.** The
  recast on the followups branch went from 11 stages to 8 by the
  $E_2$-collapse argument. Other multi-stage Lean stubs in the repo
  may collapse similarly, but the analysis depends on the recast
  Lean infrastructure (`YekutieliFiniteSliceMultiplicativeTrace`,
  `GbSpectralSequenceCollapseAtE2`,
  `CategoricalMassInvariantFinite`) which exists only on the
  followups branch. Defer to a follow-on PR after `7588970f` lands.

- **Part B step 3 (boxed $\mathbb{Q}(q)$-element form)** is a
  template-establishment pass. The template lives in the recast
  `atom-knot-mass-derivation-proof.md` on the followups branch
  ($M(\mathfrak{H}) := \rho \cdot \mathrm{tr}_M(T_w) \in \mathbb{Q}(q)$,
  $B(\mathfrak{H}) = m_e \cdot M(\mathfrak{H})|_{q=q_0}$). Once that
  lands, applying the same template to charge / magnetic moment /
  binding energy is a per-block edit that should reference rather
  than re-prove. Defer.
