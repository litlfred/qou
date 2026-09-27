# Chapter 3 — Lifting and Descent — QA Report

**Review Date:** 2026-04-25
**Chapter Directory:** `folio/quantum-observable-universe/lifting-and-descent/`
**Coverage:** 99 .md, 33 .lean, ~99 .ts (sample-based audit)

## Inventory

99 blocks across 11 sections (manifest lists 10; sub-grouping increases effective count to 11).

## Section-to-content alignment

All sections align with their stated topic. Brane-tower iteration ordered $A_0 \to A_1 \to A_n$ logically; obstruction-theory material kept clean.

## Section-to-chapter alignment

Chapter intent (brane tower, lifting obstruction $\kappa(x)$, mass identity, $\chi(A) = -6$) is delivered. Arc intact across sections.

## One-voice violations

Grep across `.md` files for the editorializing blacklist found **no matches**. No "surprisingly", "remarkably", "notably", "interestingly", "it turns out", "elegant", "beautiful". No "the author", "this work", "this book". Clean voice.

## Notational alignment

- `\mathcal{C}` — none in misuse (categories use `\mathbf{C}`)
- `\omega` for fibre functor — none (uses `\tau`)
- `E_p` for state fibre — none (uses `\mathcal{S}_p`)
- Plain `$m$` for categorical mass — none (uses `\mathfrak{m}`)
- Numerical `$q$` values — none in this chapter
- `\gamma` for vortex — N/A (no vortices in Ch 3)

## Mass identity & Descartes condition

`def:mass-identity` defined in `mass-identity.md` — single authoritative statement. `def:descartes-condition` is **referenced** in this chapter but **defined upstream** (likely Ch 2 QOU axioms or via χ = −6 derivation). This is a minor cross-chapter issue: a forward-pointing breadcrumb in the lifting chapter would help readers locate the canonical definition.

## Expository simplification opportunities

1. **SU(2) running-example consolidation** — multiple SU(2) blocks scattered through brane-tower iteration; could share a single set-up paragraph.
2. **Mass-identity exposition** — currently a long derivation; tighten by referencing the categorical-action setup once and computing.
3. **Descent variants** — several near-duplicate descent-data discussions; reduce to one canonical statement plus references.
4. **Cosimplicial intro** — could be expanded to give cleaner motivation for the Yekutieli engine.
5. **χ = −6 derivation** — multiple paragraphs converge on this; could be a single proof block with side remarks.

## Issue tally

| Severity | Count |
|---|---|
| Blocker | 0 |
| Major (Descartes-condition forward reference unresolved in chapter) | 1 |
| Minor | 2 |
| Simplification | 5 |
| **Total** | **8** |
