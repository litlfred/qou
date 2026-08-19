---
# qou-p8zx
title: Resolve PDF build warnings (cross-refs, macros, unicode)
status: completed
type: task
priority: normal
created_at: 2026-07-13T01:42:14Z
updated_at: 2026-08-16T21:05:44Z
---

Warnings to resolve:

1. Undefined cross-references (13 warnings):
   - def:simple-objects-V
   - eq:categorical-volume-constraint
   - eq:su2-emergence-diagram
   - eq:q-exp
   - lem:ccg-cosimplicial-identities
   - eq:z-from-SD
   - eq:topological-mass-decomp
   - conj:phi-q-tower-jsj-bridge
   - prop:archimedean-realization-functor
   - prop:six-term-mass-formula-complete
   - sec:mass-comparison-table
   - rem:hadron-half-life-verification
   - local-q-zeta-function

2. Undefined control sequences:
   - \@addpunct
   - \ignorespaces
   - \popQED
   - \endtrivlist
   - \@endpefalse
   - \colorlet
   - \tiny
   - \footnotesize
   - \coth
   - \lbrack
   - \rbrack
   - \coloneqq
   - \arctan

3. Unmapped unicode (failed PDF generation):
   - "𝔙" (U+1D519)
   - "’" (U+2019)
   - "É" (U+00C9)
   - "⥤" (U+2964)

\n**Note:** requires texlive environment for LaTeX build

## Resolved 2026-08-16 (PR #5246 + folio-assistant#129)

Full build: latexmk exit 0, **0 errors**, **0 undefined citations**,
**0 undefined refs**, 1031 pp, all 9 appendices present.

### Errors (all cleared)
- `aligned` outside math mode x2 — wrapped in `\[ … \]`. Now the
  mechanical criterion `render-math-mode-envelope` (fa#129): 2/2 true
  positives, 0 FP on 3529 blocks.
- U+02E3 `ˣ` unmapped — root cause was that inline code rendered to
  `\texttt{}` WITHOUT transliteration (only fenced verbatim was
  transliterated). Fixed in the renderer (fa#129); char set derived by
  compiling all 210 corpus non-ASCII chars against the real preamble
  (41 crash).

### Warnings
- undefined citations 23 -> **0**. references.bib was stale because
  setup-folio-assistant.sh bridged only one of the two paths the
  platform imports the bibliography by; export-bibtex needs
  `<clone>/schemas/references`. Script now links both. Regeneration
  exposed bare math + crash Unicode in 8 entries; sanitized at source.
- undefined \ref 0; multiply-defined labels 0.

### Not this bean's list (original body was measured on a first-pass log)
The "\undefined control sequence" list (\itshape, \coth, \arctan, …)
is **29 latex-preflight FALSE POSITIVES** — all are standard commands
that compile fine. Preflight simultaneously MISSED both real aborts.
Its known-macro seed needs widening; tracked separately.

### Remaining (deliberate, not fixed)
48 `Hyper reference` warnings / 14 unique (6 `term:*`, 5 `sec:*`,
3 `tm-*`). Cause: compact print mode drops 990 example/remark blocks
"unless referenced", and a \refterm does not count as a reference, so
glossary anchors are never emitted. Fixing needs a compact-mode
reference-detection change — real, but wider blast radius than a build
fix. Cosmetic: 115 overfull / 126 underfull hbox.



## Follow-up 2026-08-16 (continued session) — hyper refs now 0 too

Rebased on main (+97 commits), re-verified, then closed the last
warning class. **Every unresolved-reference class is now zero**:
errors 0 | citations 0 | \ref 0 | hyper refs 48 -> 0 | multiply-defined 0
| 1032 pp.

The 48 hyper refs were NOT cosmetic — each was a dead link in the
published PDF. Three distinct causes:

1. **Labelled `prose` blocks emitted no \label at all** (renderer bug).
   `case "prose"` pushed only the body, so `[…](#sec:foo)` at a prose
   block always dangled. 5 sites. Fixed fa#129.
   - Regression caught: a prose block often IS its section intro and
     shares the section label -> 15 multiply-defined labels on the first
     pass. renderBlock now takes the enclosing section label and skips.
2. **`refterm` was not counted as a reference** by compact mode, whose
   contract is "excluded UNLESS referenced". Glossary shipped with 24 of
   27 blocks missing while live appendix-surreals prose linked into it.
   The `term:` anchor lives in the block BODY, not the label.
3. **Term refs cross chapter boundaries** — chapters render
   independently, so fixing (2) alone only moved 48 -> 32. Needed a
   doc-wide `collectReferencedTerms` pre-pass in build.ts.
   Compact mode stays compact: glossary 24 -> 18 excluded, i.e. exactly
   the 6 cited entries restored.
4. 3 x `tm-*` links simply missing the `sec:` prefix (qou-side, 5 files).

Residual is cosmetic only: 116 overfull / 130 underfull hbox, 14
newunicodechar redefinitions.
