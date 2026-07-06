# Orphan / broken-import `.lean` triage (2026-06-01)

**Trigger:** cleanup of the orphan `mass-theory/geom-yekutieli-alignment.lean`
surfaced 33 *additional* sibling `.lean` files (outside the Lake package tree
`content/quantum-observable-universe/lean/`, whose `lakefile.toml` sets
`srcDir = "."` so only `QOU.*` modules under `lean/QOU/` are compiled) that
`import` a `QOU.*` module absent from the build tree.

**Headline:** **only 1 of 34 was a safe delete.** A naive "broken import →
orphan → delete" sweep would have destroyed ~32 real formalizations. The 33
remaining are NOT cruft — they are real, mostly-referenced content whose
broken imports went undetected *because they sit outside the build srcDir
and `lake build QOU` never compiles them*.

## Method (authoritative)

Classification uses `computations/audits/lean-ref-resolution-audit.witness.json`,
which greps each block's `lean.ref` decl and records `sibling_declares`
(the `.md`/`.ts` sibling `.lean` declares it) vs `lake_root_declares`
(a copy under `lean/QOU/` declares it). The fuzzy last-component matcher
used in the initial scan is **not** authoritative for deletion and was not
relied on.

## Three buckets

### A. Referenced-only-via-sibling — **DO NOT DELETE** (fix import instead)
`sibling_declares=True, lake_root_declares=False, resolved_via=sibling`:
the block's `lean.ref` resolves **to this very file**; there is **no** copy
in the build tree. Deleting loses the only formalization. The broken
`import QOU.X` is a real defect, but the fix is to correct the import (and,
structurally, to get these files into the build srcDir so they are actually
compiled). ~23 files, including:

- `climax-volume-mass/vertex-algebra-{relations,jet-relations}.lean`
- `information-theory/{q-game-of-life,toffoli-lp-stability}.lean`
- `mass-theory/{crystal-basis-resolves-mass-tower-open-problems,em-spectral-completeness,gram-determinant-plancherel-ratio,he4-two-row-dominance,knot-factor-amphicheiral,knot-factor-borromean-composite,knot-factor-shell-closed,mass-tower-coefficient-stratification,nuclear-knot-classification,wigner-coefficient-derivation}.lean`
- `predicted-spectra/{alpha-em-shift-multiplicative-chain,bloch-group-quotient-construction,bring-hyperbolic-knot-bloch-decomposition,cl2-pentagon-and-faddeev-partial,em-coupling-chern-simons,force-carrier-bring-uniqueness,gauge-coupling-uniqueness,upstream-mathlib-additions}.lean`
- `quantum-observable-universes/substrate-parameter-unique.lean` — its
  import `QOU.SubstrateParameter` likely should be
  `QOU.QuantumObservableUniverse.SubstrateParameter` (a real in-build module).

### B. Unreferenced infrastructure `.lean` — owner decision (NOT a clean delete)
`remark`-kind blocks with **no `lean:` field** (the only "lean" token is the
tag `"lean-infrastructure"`), but the sibling `.lean` carries substantial
real decls (e.g. `braid-group-n-strand.lean`: `BraidCrossing`, `writhe`,
`HeckeQuotient`, `MarkovTraceN`). These are dangling — not referenced by any
`lean.ref`, not in the build — but they are real content, not duplicates.
~9 files:

- `braids-and-knots/{braid-group-n-strand,markov-trace-inductive-limit}.lean`
- `mass-endomorphism/{multi-link-jones-q1-extension,u-coordinate-discharges}.lean`
- `mass-theory/{ck-extraction-from-algebraic-rules,mass-tower-deeper-fillers,typed-b3-sub-braid-extraction}.lean`
- `predicted-spectra/{bloch-wigner-mathlib-filler,three-substantive-mathlib-fillers}.lean`
- `stochastic-mechanics/markov-closure-map-axiomatic.lean`

Owner decision: wire these into the build (add to `lean/QOU/`, fix imports)
or archive them. They should not be silently deleted.

### C. True stale-duplicate — **deleted** (the only safe one)
`lake_root_declares=True`: a canonical copy exists under `lean/QOU/`.
- `mass-theory/geom-yekutieli-alignment.lean` — removed; canonical copy is
  `lean/QOU/BraidKnot/geom_yekutieli_alignment.lean` (block kind
  `conjecture`, so the sibling is optional per §3; `lean.ref` still resolves
  via the lake root).

## Root cause (structural, not cruft)

The `qou` Lake package is rooted at `content/quantum-observable-universe/lean/`
(`lakefile.toml` sets `srcDir = "."`), so it compiles only the `QOU.*` modules
under that root's `lean/QOU/` subtree. The ~32 bucket-A/B files
live beside their `.md`/`.ts` blocks under the chapter directories, **outside
that srcDir**, so `lake build QOU` never compiles them — which is exactly why
their broken `QOU.*` imports were never caught. This is a build-coverage gap,
not a pile of orphans to delete.

## Recommended actions (owner-gated, NOT auto-applied)

1. **Bucket A — fix imports** (compile-pending; needs a local `lake build`
   to verify): correct each broken `import QOU.X` to the real module name.
   Several look like simple renames (e.g. `QOU.SubstrateParameter` →
   `QOU.QuantumObservableUniverse.SubstrateParameter`); others import
   modules that may need to be authored or are siblings not yet in the
   build tree.
2. **Build coverage** — decide whether chapter-dir sibling `.lean` files
   should be compiled at all. If yes, they need to be reachable from the
   Lake `srcDir`; if no (they are narrative-adjacent formalizations
   resolved via `lean.ref` grep only), document that they are intentionally
   out-of-build and add them to a lint exclusion so the broken-import scan
   doesn't keep flagging them.
3. **Bucket B** — owner decides per file: wire in or archive.

**No bucket-A/B file was deleted.** Only the one verified stale duplicate
(bucket C) was removed.
