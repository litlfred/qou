# Content-sibling `.lean` compile sweep — 2026-06-28

**Branch:** `claude/ci-enforcement-lean-orphans-5kalev` (PR #2974)
**Scope:** every content-block `.lean` sibling — `content/**/*.lean`
**outside** the `lean/` library tree (926 files) — `lean`-direct
type-checked against the restored `lake-cache/qou-v4-24-0` oleans.

## Why this sweep exists

Content-block `.lean` siblings live **outside** the CI-built
`lake build QOU` target (the qou lakefile globs `srcDir="."` = the
`lean/` tree only). They are never compile-checked by the library
build and have accumulated latent breakage that no existing gate
catches. This sweep quantifies the rot and the new
`lean-content-siblings.yml` CI job (this PR) stops *new* drift.

## Headline result

| Bucket | Count | Meaning |
|---|---|---|
| **swept** | 926 | content siblings (outside `lean/`) |
| pass | 395 | `lean`-direct exit 0 |
| **fail (raw)** | 531 | non-zero exit |
| → **genuine breakage** | **382** | real parse / elaboration / type errors — the "never compiled standalone" class |
| → cache-subset miss | 136 | imports a Mathlib/QOU module outside the restored olean cone — **infra artifact, not a defect** |
| → flaky / sorry-warn | 13 | no error on re-run |

**~41 % of content siblings (382/926) are genuinely broken on `main`.**
This branch makes no content changes, so every one of the 382 is
pre-existing breakage.

### Critical methodology note — cache-subset misses are NOT breakage

The `lake-cache` branch ships only QOU's *transitive Mathlib
dependency cone* (~2951 oleans), not all of Mathlib. A sibling that
imports a module outside that cone (e.g. `import Mathlib`,
`import Mathlib.Data.Nat.Defs`) fails with
`object file '…/X.olean' of module X does not exist` — a runner
limitation, not a file defect. **136 of the 531 raw failures are this
class.** The committed [`scripts/lean-verify-siblings.sh`](../../scripts/lean-verify-siblings.sh)
distinguishes them (missing-object-file → `::warning` neutral-skip;
any other `error:` → `::error` + fail) so the CI gate never
false-blocks a PR on a cache-subset miss.

## Genuine breakage by error type (top 15)

| Count | First error |
|---|---|
| 92 | `unexpected token …; expected …` (parse) |
| 41 | `failed to synthesize` |
| 39 | `Function expected at` |
| 38 | `unknown tactic` |
| 20 | `unsolved goals` |
| 15 | `No goals to be solved` |
| 12 | `invalid binder annotation, type is not a class instance` |
| 12 | `expected token` |
| 10 | `unexpected token …; expected term` |
| 9 | `Tactic 'rewrite' failed` |
| 8 | `Type mismatch` |
| 7 | `Invalid field notation: Type of …` |
| 6 | `unexpected identifier; expected …` |
| 6 | `Invalid field notation: Type is not of the form 'C …'` |
| 6 | `Application type mismatch` |

The largest class is **parse errors** (≈110 across the
`unexpected token` / `expected token` rows). A recurring signature —
`unexpected token 'section'; expected 'lemma'` — appears across many
files (e.g. `predicted-spectra/antineutrino-knot.lean`,
`quantum-observable-universes/q-reeb-flow.lean`,
`information-theory/quantum-ideal-gas-law.lean`), suggesting a shared
broken authoring/stub template rather than independent bugs. That
makes a chunk of the 382 likely fixable by a single template repair.

## Genuine breakage by chapter (top 20)

| Chapter | Count |
|---|---|
| `quantum-observable-universe/mass-theory` | 72 |
| `quantum-observable-universe/quantum-observable-universes` | 63 |
| `quantum-observable-universe/particle-interactions` | 37 |
| `quantum-observable-universe/predicted-spectra` | 26 |
| `quantum-observable-universe/brings-surface` | 24 |
| `quantum-observable-universe/information-theory` | 23 |
| `quantum-observable-universe/observations` | 22 |
| `quantum-observable-universe/lifting-and-descent` | 18 |
| `quantum-observable-universe/climax-volume-mass` | 17 |
| `quantum-observable-universe/braids-and-knots` | 15 |
| `quantum-observable-universe/mass-endomorphism` | 12 |
| `quantum-observable-universe/quantum-universes` | 10 |
| `quantum-observable-universe/molecular-construction` | 9 |
| `quantum-observable-universe/stochastic-mechanics` | 6 |
| `quantum-observable-universe/models-of-qous` | 6 |
| `quantum-observable-universe/fluid-dynamics` | 6 |
| `unital-groebner-bases/unital-groebner-bases-chapter` | 4 |
| `quantum-observable-universe/q-geometric-langlands` | 4 |
| `quantum-observable-universe/organic-chemistry` | 3 |
| `quantum-observable-universe/measurement-observation` | 2 |

## Actionable lists (committed)

- **Genuine orphans (382)** — `file ||| first-error`:
  [`2026-06-28-content-sibling-compile-sweep.genuine.txt`](2026-06-28-content-sibling-compile-sweep.genuine.txt)
- **Cache-subset misses (136)** — re-verify once their import cone is
  cached; not defects:
  [`2026-06-28-content-sibling-compile-sweep.cachemiss.txt`](2026-06-28-content-sibling-compile-sweep.cachemiss.txt)

## Disposition

1. **CI gate prevents new drift (this PR).** `lean-content-siblings.yml`
   now diff-scopes a `lean`-direct check on changed content siblings via
   `lean-verify-siblings.sh`. A PR that *touches* a broken sibling must
   fix it; the 382 pre-existing files are not retroactively blocked
   (diff-scoped).
2. **The 382 genuine orphans are a drain backlog, not this PR's job.**
   Tracked as a bean. Recommended attack order: (a) the shared
   `unexpected token 'section'; expected 'lemma'` template family first
   (one fix, many files); (b) `mass-theory` + `quantum-observable-universes`
   (135 of 382) as the densest chapters; (c) the elaboration-error tail
   per-file.

## Reproduce

```bash
# restore oleans, then for each content sibling outside lean/:
scripts/lean-cache-restore.sh
git ls-files 'content/**/*.lean' | grep -v '/lean/' \
  | xargs -n1 scripts/lean-verify-siblings.sh
```
