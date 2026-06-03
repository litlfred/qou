# `proof-objects.json` extractor broken since content-object migration

> Surfaced 2026-06-03 in PR [#1771](https://github.com/litlfred/qou/pull/1771) during a
> Lean-audit-stats query. Captures the root cause; the fix is
> tracked as a follow-up infra item.

## Headline

[`proof-objects.json`](../../proof-objects.json) is **45 days stale** — `generated_at`
field is `2026-04-19T01:39:52`, but the file is committed to `main` and
serves as the Lean formalization status manifest consumed by three CI
workflows ([`lean_ci.yml`](../../.github/workflows/lean_ci.yml),
[`lean-build.yml`](../../.github/workflows/lean-build.yml),
[`blueprint.yml`](../../.github/workflows/blueprint.yml)) and the
gh-pages deploy.

All 106 objects in the manifest carry `kind: '?'` and `status: '?'` —
the data is effectively empty. The live state would be 77 axiom
declarations + 653 raw `sorry` matches across 255 `.lean` files.

## Root cause (not "CI billing failures")

Initial guess: the GitHub Actions billing pattern that's been hitting
every CI check this session has been blocking the auto-regen for 45
days. **Wrong.** The actual cause is more structural:

The regen script
[`.github/scripts/extract_proof_objects.py`](../../.github/scripts/extract_proof_objects.py)
reads `chapters/<chapter>.tex` files as its source of truth. Running it
in the current repo state:

```
⚠️  Skipping missing chapter: /home/user/qou/chapters/lifting-of-quantum-torsion.tex
⚠️  Skipping missing chapter: /home/user/qou/chapters/path-integrals-and-braiding.tex
⚠️  Skipping missing chapter: /home/user/qou/chapters/descartes-universe.tex
⚠️  Skipping missing chapter: /home/user/qou/chapters/experimental-evidence.tex
⚠️  Skipping missing chapter: /home/user/qou/chapters/interpretations.tex
⚠️  Skipping missing chapter: /home/user/qou/chapters/glossary.tex

Total objects extracted: 0
```

The `chapters/*.tex` files are **generated** by the content pipeline
(`bun run pipeline/build.ts`), not authored. They're not even in the
repo tree right now — they're build artifacts. The extractor was
written when LaTeX was the authoritative source; the content-objects
migration moved authorship to `.ts` + `.md` triples but the extractor
was never updated.

**Consequence:** even when CI runs successfully (i.e. when billing
clears), the extractor produces 0 objects → fails the downstream
`update_proof_status.py` step → `proof-objects.json` stays whatever
was last manually committed. The committed file has been frozen at the
April-19 state with placeholder `kind: '?'` / `status: '?'` ever since.

The "45-day staleness" attribution to CI billing was misleading. The
script is broken regardless of CI state.

## Why this matters

Three CI workflows + the gh-pages dashboard consume `proof-objects.json`:

- `lean_ci.yml`: uploads it as an artifact (retention 30 days)
- `lean-build.yml`: feeds it into the build pipeline
- `blueprint.yml`: passes it to `generate_dependency_graph.py` for the
  visual dependency-graph SVG on gh-pages
- gh-pages: serves it as the human-readable manifest at
  `litlfred.github.io/qou/proof-objects.json`

All four consumers receive **empty placeholder data**. The dependency
graph, the public manifest, and the build-time triage all silently
operate on stale-empty data.

## Fix paths

**Option 1 — Rewrite the extractor (recommended).** Port
`extract_proof_objects.py` to read the canonical content-object
sources:

- Walk `content/**/*.ts` for block manifests (kind, label, uses, lean.ref)
- Parse `content/**/*.lean` for declaration shape, sorry count, axiom
  count
- Compose into the existing `proof-objects.json` schema (v1.0)

Effort: 1-2 days. Produces a manifest that is actually live + populated.

**Option 2 — Drop the manifest.** Remove `proof-objects.json` + the
three CI consumers. Replace with a simpler script that emits per-block
sorry/axiom counts to stderr during validation. Effort: ~1 day. Loses
the dependency-graph SVG.

**Option 3 — Minimal stub-extractor.** Have `extract_proof_objects.py`
fall back to scanning `content/**/*.ts` if `chapters/*.tex` is absent,
emitting a minimal manifest with `label` + `lean.ref` only. Doesn't
populate `kind` or `status` but at least gives a non-empty manifest.
Effort: ~2 hours. Partial fix.

## What this PR does NOT do

- Does **not** attempt the rewrite — out of scope for a canonical-axis
  PR.
- Does **not** modify `proof-objects.json` directly (any local regen
  would emit 0 objects, which is worse than the stale-placeholder
  current state).
- Does **not** add a queue item — the underlying issue is a 1-2-day
  rewrite, tracked here for now.

## See also

- [`docs/audits/2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md) — companion: which axioms are tractable to discharge
- [`.github/scripts/extract_proof_objects.py`](../../.github/scripts/extract_proof_objects.py) — the broken extractor
- [`.github/scripts/update_proof_status.py`](../../.github/scripts/update_proof_status.py) — the consumer that errors out on empty input
- [`.github/workflows/lean_ci.yml`](../../.github/workflows/lean_ci.yml) — CI regen step (currently no-op for the reason above)
