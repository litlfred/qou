#!/usr/bin/env bun
/**
 * Run the bibliography / cross-reference validator, injecting the
 * domain-specific reference registry into the folio-assistant platform.
 *
 * WHY THIS FILE EXISTS
 *
 * `folio-assistant/folio-assistant-sci/pipeline/validate-references.ts` is the only checker
 * that cross-checks Lean `-- Ref: [key]` comments and `\cite{}` against
 * `folio/schema/references.ts`. Run directly it does not merely report
 * nothing — it THROWS, on its own first statement:
 *
 *   error: Reference registry not configured. The downstream repo must call
 *          configureReferenceRegistry() before running pipeline functions.
 *     at getReferenceRegistry (references-registry-di.ts:62:15)
 *     at validate-references.ts:55:21
 *
 * It imports `references` from the DI shim at module scope and touches it in
 * the schema loop before anything else, so there is no partial run. Nothing in
 * this repo invokes it either — no workflow, no script, no package.json entry;
 * every other mention of the name is prose describing what it would do.
 *
 * So the Lean-ref citation surface has never been measured. That is the same
 * defect `scripts/run-validate.ts` carries for `cites-resolve` (bean
 * `qou-cite`), one layer up: the platform expects dependency injection the
 * folio side never supplies.
 *
 * The configuration MUST happen before the checker module is imported, hence
 * the dynamic `await import` below rather than a top-level one — the checker
 * runs its work at module scope, so a static import would execute it during
 * hoisting, before the registry exists.
 *
 * A SECOND blocker sits behind the first, so `--paper` is not optional here:
 * past the registry, the checker throws again at validate-references.ts:133 --
 * "5 papers found (bach2013-double-slit, fred2005-formal-groups,
 * quantum-observable-universe, unital-groebner-bases, visualizer) -- name one
 * explicitly." Pass `--paper quantum-observable-universe`.
 *
 * WHAT A FIRST RUN REPORTS, so it is not mistaken for a regression this
 * introduced: 19 errors / 173 warnings / 411 info, over 367 Lean, 189 LaTeX
 * and 345 `.ts` citations. The 19 are bean `qou-e4eu` -- twelve real works
 * missing from the bibliography, and seven keys that are not citations at all
 * (`audit`, `probe`, `probe-w/j/q`, `bean`, `metallichierarchy`), where an
 * author used `-- Ref:` to point at an audit doc, a probe or a bean.
 *
 * `manuscript` is NOT among them, and an earlier version of this comment
 * predicted it would dominate. It does not: validate-references.ts:171-172
 * exempts it deliberately -- "Skip cross-paper refs (paper-dir:label format)
 * and manuscript self-refs" -- so all 4436 `-- Ref: [manuscript]` sites pass
 * by design. It is `cites-resolve` that lacks the carve-out, which is a
 * folio-assistant fix (bean `qou-cite`), not a corpus one.
 */

import { configureReferenceRegistry } from "../folio-assistant/cat-harness-tools/pipeline/references-registry-di";

const bib = await import("../folio/schema/references");

if (!bib.references?.length) {
  console.error("  ✗ folio/schema/references.ts parsed but holds no entries");
  process.exit(1);
}

configureReferenceRegistry({
  references: bib.references,
  referenceMap: bib.referenceMap,
  CSLEntrySchema: bib.CSLEntrySchema,
});

console.log(`Reference registry configured: ${bib.references.length} entries\n`);

// Default the paper (C9 story B1, issue #7528). Without `--paper` the checker
// throws on a 5-paper folio, so the wrapper used to exit 1 before checking
// anything. Measured 2026-10-05: running it with each of the five papers gives
// IDENTICAL findings (11 errors / 177 warnings / 444 info), because the
// citation cross-check walks the whole folio. So a default changes nothing
// about what is checked, and an explicit `--paper` still wins.
if (!process.argv.includes("--paper")) {
  process.argv.push("--paper", "quantum-observable-universe");
}

// Dynamic, and after configuration — see the note above.
await import("../folio-assistant/folio-assistant-sci/pipeline/validate-references");
