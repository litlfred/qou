# Yekutieli → Quantum rename — scope decision (owner ruling, 2026-07-12)

**Status: CLOSED — do not reopen.** The "rename Yekutieli across content" work
(beans `qou-neei`, `qou-30on`) is **complete at the prose layer and
deliberately stops there.** A structural-identifier rename is **decided
against** by the owner (2026-07-12). This note exists so the corpus-grep
checklist surfaces the decision and no future agent re-proposes the
structural rename.

## What was done (prose only)

- **`qou-neei`** (PR #3656, merged): the lifting-condition **term** renamed
  "Yekutieli lifting condition" → **"Quantum lifting condition"** in prose,
  matching the already-changed `def:yekutieli-lifting-condition` title. The
  convention note in
  [`brane-tower-terminology.md`](../../content/quantum-observable-universe/lifting-and-descent/brane-tower-terminology.md)
  was updated to name the condition "quantum lifting condition" while
  reserving the qualifier *Yekutieli* for the multiplicative integration.
- **`qou-30on`** (PR #3664, merged): descriptive de-attribution — bare
  "Yekutieli" qualifier dropped from the framework's **own** objects
  ("Yekutieli tower" → "brane tower", "Yekutieli lifting obstruction" →
  "lifting obstruction", "Yekutieli class(es)" → "obstruction class(es)")
  across 24 files.

## What is deliberately NOT done (owner decision — do NOT reopen)

- **Structural identifiers keep the `yekutieli` name.** Content-block
  **labels** (`def:yekutieli-lifting-condition`, `prop:yekutieli-lifting`,
  `prop:blowup-yekutieli`, `lem:yekutieli-leading-coefficient`,
  `def:yekutieli-triple`, `conj:geom-yekutieli-alignment`, …), **Lean
  declarations** (`QOU.YekutieliLiftingCondition`, `QOU.Torsion.YekutieliTriple`,
  `QOU.YekutieliLifting`, `QOU.Archimedean.yekutieli_leading_coefficient`, …),
  and **file names** (`yekutieli-lifting*.{ts,md,lean}`, `archimedean-yekutieli.md`,
  `geom-yekutieli-alignment.md`, `p3-blowup-yekutieli.md`, …) are **unchanged
  and are to remain unchanged.** Owner: "ids and filenames can stay" (2026-07-12).

## Genuine attributions retained (never in scope for the rename)

References to Yekutieli's **published theorems/constructions** stay verbatim
and must not be renamed: the **Yekutieli non-abelian Stokes theorem**, the
**Yekutieli nonabelian multiplicative integral / MI** (`\cite{yekutieli2015}`),
the **Yekutieli rigid dualizing complex**, **Yekutieli triples**, the
**Yekutieli leading coefficient**, Čech–Yekutieli descent, and every
`\cite{yekutieli2008/2010/2015}`.
