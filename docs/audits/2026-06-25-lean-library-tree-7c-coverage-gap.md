# Lean library-tree §7c coverage — audit (CORRECTED 2026-06-25)

**Date:** 2026-06-25 · **PRs:** #2789 (original), follow-up (this correction)

> **⚠ CORRECTION (2026-06-25, per the folio-assistant agent who owns the checkers).** The original
> version of this audit claimed a *candidate-2 coverage gap* (that the 839 library-tree Lean files
> escape the per-block `q-usage`/`wall-side` checkers because they have no co-located sidecar). **That
> claim was wrong.** The checkers **do** read each block's *resolved* Lean file (candidate-1 sibling →
> candidate-2 library/Lake tree via `lean.ref`), so a library file **referenced by a block is audited**,
> with the chapter taken from the **block** path (not the lean dir). Verified two ways: the
> folio-assistant test `scripts/tests/lean-ref-coverage.test.ts`, and a qou spot-check (below). The
> real hole was **orphans** — see §3.

## 1. Why the original audit misfired

- **"2280 sidecars, 0 inside any `lean/` tree" is by design, not evidence of a gap.** A `<block>.qa.json`
  **co-locates with the content block's `.ts`** and stores the **resolved Lean hash** in
  `source_hashes.lean`. Zero sidecars in `lean/` ≠ unswept. The original audit inferred "unswept" from
  the sidecar location — a wrong inference.
- **qou spot-check (candidate-2 coverage confirmed).** The block
  `braids-and-knots/figure-eight-reeb-rotation` (`ref: "qou:QOU.BraidsAndKnots.figure_eight_unitary_on_standard"`,
  no chapter-dir sibling) carries a sidecar with `wall-side-correct`, `q-usage-archimedean-in-categorical-chapter`,
  `q-usage-positivity-implicit`, … **plus `source_hashes`** reflecting the resolved library file. So the
  library decl **is** audited. ✓
- **`check-sidecars.sh`'s path heuristic was the wrong model.** Its earlier "ℝ in an algebraic-domain
  path" rule **over-fired** (96 whole-tree flags) because `lean/QOU/BraidKnot/` is a catch-all holding
  legitimately-archimedean files. Do not generalize that stopgap's limits to the real checker. **Fixed
  in this PR** — `check-sidecars.sh` is now **content-based** (see §4).

## 2. The §7c rule (for context)

A Lean declaration holding over a generic commutative ring must be stated over a type variable
(`{R : Type*} [CommRing R]` / `[Field R]`), **not** silently specialised to `ℝ`. `ℝ` is for genuinely
archimedean constructs (`Real.*`, ordering `0 < q`, `linarith`/`positivity`/`nlinarith`, CODATA
literals). Criteria: `q-usage-archimedean-in-categorical-chapter`, `wall-side-correct`.

## 3. The real hole — ORPHANS (closed upstream in folio-assistant)

The block-driven audit only reaches a library file **some block references**. A library file referenced
by **no** block is an **orphan** and was unswept — the most likely reason the `TauQuantumIntegerForm`
gratuitous-ℝ leaked (qou #2782; it is an orphan — registered in `QOU.lean` but referenced by no content
block). **folio-assistant's `q-usage-audit` now sweeps orphans** (`lean/<lib>/**/*.lean` reachable by no
block) with **content-based, chapter-independent** checks (wall-side mixed-file, base-ring-minimal,
`q-usage-positivity-implicit`); results land in the witness as `orphan_findings`, and orphan fails count
toward `--strict`. **No checker detection logic changed → no `script_hash` bump, no sidecar invalidation.**

### qou-side orphan findings (content-verified, NOT path-based)

The folio-assistant orphan pass is unreachable from a qou-scoped session (clone 403 / no symlink), so the
equivalent analysis was run in qou (`scratchpad/orphan_7c.py`, content-based):

| metric | count |
|---|---|
| library Lean files | 802 |
| referenced by ≥1 block | 380 |
| **orphans (no block ref)** | **422** |
| orphan **base-ring-minimal** candidates (ℝ in type, no archimedean construct) | 53 |
| orphan **mixed** candidates (generic + archimedean in one file) | 33 |

Per the over-claim discipline, the 86 candidates are a **review queue**, not 86 violations — many
base-ring-minimal hits are archimedean-domain files (`Mass/`, `AtomicMass/`, `HadronicMass/`,
`Substrate/`) whose ℝ is correct. **Content-verified genuine leaks** (read by hand — algebraic statement
forced over ℝ, no archimedean need): `BraidsAndKnots/YLambdaQSchur.lean` (q-integer / q-Schur weights
`qInt`/`qFactorial` over ℝ), `BraidKnot/H3HeckeIdempotents.lean` (q-integers + eigenvalues `q+q⁻¹`,
`-q⁻¹`), `HeckeAlgebra/MarkovTrace.lean` (`markovTrace_smul (c : ℝ)`), `Shared/WedderburnBlockDecompositionContext`
(`dim_q`/`w`/`w_tilde : … → ℝ` though the class even declares a coefficient ring `R`). These confirm the
orphan hole harboured real §7c leaks beyond the one already fixed. Generalising them is a **focused
follow-up** (each is a structural `ℝ → {R}/[Field R]` refactor; `Wedderburn…Context` has ~15 extenders) —
**beaned**, not done here (NOT a mass-fix, per the folio-assistant guidance).

> **Currency correction (2026-06-26, bean `z1lz`).** Re-checked the four against the live tree:
> `BraidKnot/H3HeckeIdempotents.lean` is **already generic** `{R} [Field R]` (line 42; carries a §7c
> docstring) — this flag is **STALE** (the file was generalised after the audit snapshot; no work). It is
> the only one of the four that is **in-build** (via the `BraidKnot` aggregator), so the highest-value §7c
> member is already compliant. Of the remaining three: `YLambdaQSchur` is a true **orphan** (0 importers,
> 0 block refs ⇒ CI-unenforced) — generalise **+ wire into the `BraidsAndKnots` aggregator** to make it
> count; `HeckeAlgebra/MarkovTrace.lean` is a **cascade** (`markovTrace`'s ℝ codomain is fixed upstream in
> `HeckeAlgebra.Common`, so generalising just `markovTrace_smul`'s `c` is incoherent); `Wedderburn…Context`
> stays deferred (~15 extenders). Full table:
> [`docs/coordination/keystone-infra.md` §"§7c base-ring follow-up"](../coordination/keystone-infra.md).

## 4. `check-sidecars.sh` — now content-based

Aligned with the real checker: the path heuristic is **removed**. For standalone library Lean it now
flags two **content** classes — **MIXED** (generic + archimedean in one file → split per §7c) and
**base-ring-minimal** (ℝ in a type with **no** archimedean construct → likely gratuitous, generalize).
Verified: `Archimedean/BetaDecay` → justified-OK (no false flag); `H3HeckeIdempotents` / `YLambdaQSchur`
→ base-ring-minimal ⚠; `Mass/TauQuantumIntegerForm` (post-#2782 fix) → generic-OK; `Mathlib/HeckeAlgebra`
→ MIXED ⚠ (legit-by-design — review, not auto-fix). Right-sized for per-commit use.

## Cross-references
- folio-assistant agent guidance (relayed 2026-06-25) — the authoritative correction.
- `docs/workplans/2026-06-25-fa-extend-q-usage-library-tree-coverage.md` — superseded by the orphan pass;
  the "extend candidate-2 coverage" step is moot (coverage already existed); the orphan pass is the fix.
- `docs/audits/2026-06-25-z2bn-pf-monodromy-synthesis.md` — the §7c fix (#2782) that triggered this.
- `AGENTS.md §7c`, `.claude/skills/local/q-usage-watcher.md`, `.claude/skills/local/formalizer.md`.
