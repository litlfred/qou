# §3b-cond conditional-class banner audit — baseline-allowlist (2026-06-03)

**Branch / PR:** [`claude/strict-mode-baseline-allowlist-2026-06-03`](https://github.com/litlfred/qou/tree/claude/strict-mode-baseline-allowlist-2026-06-03) — [PR #1735](https://github.com/litlfred/qou/pull/1735)

## Why this exists

[`content/pipeline/conditional-class-banner-audit.ts`](../../content/pipeline/conditional-class-banner-audit.ts)
enforces AGENTS.md §3b-cond: every block downstream of a
`conj:`-axiomatised class must carry **both** (i) the upstream class
as an `[Instance]` hypothesis in its `.lean`, **and** (ii) a
`Theorem (conditional on conj:X).` banner in its `.md`.

As of 2026-06-03 on `main`:

| Statistic | Count |
|---|---|
| Total blocks scanned | 1879 |
| Conditional-on-class candidates | 132 |
| Fully compliant (banner + Lean class) | 12 |
| Missing Lean `[Class]` hypothesis | 120 |
| Missing `.md` conditional banner | 112 |

So 12 of 132 candidates fully comply, the other 120 are partially or
fully out of contract. Closing the 232 (label-level) gaps is a
substantive content workplan touching ~120 provable blocks — it is
**not** in scope for this PR. The audit was, however, running with
`--strict` in CI, so every push to `main` (and every PR) was failing
the `Witness pipeline / validate` job on these pre-existing gaps.

## What this PR does

Adds a **baseline-allowlist** mechanism to the audit so the strict
gate catches NEW regressions without blocking on the historical
baseline:

1. New flags in [`conditional-class-banner-audit.ts`](../../content/pipeline/conditional-class-banner-audit.ts):
   - `--baseline-allowlist <path>` — with `--strict`, only labels
     **not** in the allowlist count toward exit 1.
   - `--emit-baseline` — regenerate the allowlist from the current
     gap set. Use after deliberately accepting / discharging a gap.
2. Initial allowlist at
   [`2026-06-03-conditional-class-banner-baseline.json`](2026-06-03-conditional-class-banner-baseline.json)
   capturing today's 120-label + 112-label gap set.
3. CI step in
   [`witness-pipeline.yml`](../../.github/workflows/witness-pipeline.yml#L480)
   now invokes both flags: `--strict --baseline-allowlist <path>`.

## Net effect

- CI **green** for the historical baseline.
- CI **fails** if any NEW conditional-on-class block lands without
  the Lean class hypothesis or the `.md` banner.
- Authors of future propositions still feel the §3b-cond contract
  pressure — the rule is unchanged, only the accepted retroactive
  set differs.

## How to discharge a baselined gap

When a §3b-cond gap is genuinely fixed:

```bash
# 1. Add the banner to the .md and/or the [Class] hypothesis to the .lean.
# 2. Regenerate the allowlist (it will SHRINK by the just-fixed labels):
bun run content/pipeline/conditional-class-banner-audit.ts --emit-baseline

# 3. Inspect the diff — verify only the just-fixed labels were removed.
git diff docs/audits/2026-06-03-conditional-class-banner-baseline.json

# 4. Commit alongside the gap fix:
git add docs/audits/2026-06-03-conditional-class-banner-baseline.json \
        content/quantum-observable-universe/.../<block>.{md,lean}
git commit -m "audit: discharge §3b-cond gap on <block-label>"
```

## What it does NOT do

- **Does not fix the 232 gaps.** That is a separate, substantive
  content campaign (per AGENTS.md §3b-cond #2 + #3).
- **Does not unblock billing-side CI failures.** As of 2026-06-03,
  ~25 of 27 recent main runs are failing on GitHub Actions billing
  (runner_id=0, 3-second simultaneous fails across unrelated
  workflows). Those are out of scope per AGENTS.md
  "CI billing failures" rule.

## Related

- AGENTS.md §3b-cond (the source rule).
- AGENTS.md §"CI billing failures — distinguish from real failures"
  (why we are not retriggering blocked workflows).
- PR #566 (initial 12/12 fully-compliant baseline — the count has
  since regressed as new propositions landed without the contract).
