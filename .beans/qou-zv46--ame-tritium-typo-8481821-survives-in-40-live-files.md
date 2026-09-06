---
# qou-zv46
title: AME tritium typo 8.481821 survives in 40 live files; 3He companion 7.718058 in 25
status: todo
type: task
created_at: 2026-09-06T03:41:22Z
updated_at: 2026-09-06T03:41:22Z
---

Not an inference — **already established prior art**. `computations/binding_canonical.py:610-623`
records that PR #1105 (2026-08-19) routed that file's targets through the
`AME_B_*_MEV_VALIDATION` accessors *"after finding the inline tritium value was
a typo (8.481821 for 8.481798)"*, and measured the residue it left behind:

```
6Li  31.994526  vs  31.9939872   (-538.8 eV)
7Li  39.244531  vs  39.2450807   (+549.7 eV)
7Be  37.600350  vs  37.6008409   (+490.9 eV)
```

That fix was applied to **one file**. The typo is still live everywhere else.

## Measured spread (vendored AME2020 via `codata_constants.ame_binding_mev`)

| literal | nuclide | AME2020 | offset | live files |
|---|---|---|---|---|
| `8.481821`  | ³H  | `8.4817962`  | **+24.8 eV** | 40 |
| `7.718058`  | ³He | `7.71804132` | **+16.7 eV** | 25 |

20 files carry both. Forms vary — bare float, `mp.mpf("…")`, `Decimal("…")`,
and a plain string in a table — so a single textual sweep will not catch them;
`8.481821` also appears inside prose/comments where it must stay (e.g. the
`binding_canonical.py` note above, and `w3_closeability_audit.py:311`'s printf).

Full site lists: `git grep -n '8\.481821' -- '*.py' | grep -v _deprecated` and
the same for `7\.718058`.

## Why this is not cosmetic

Both values are **denominators or numerators of published residuals**. The
T/³He pair is the standard mirror discriminator across this corpus, so a
per-atom offset does not cancel — it lands directly on the mirror mismatch these
probes exist to report. `deltalambda/*` alone carries the pair in 7 magnitude
probes as `B3H`/`B3He`.

## Scope notes

- **Do not touch `computations/_deprecated/`** (15 more files). Deprecated,
  and its own dominant lineage is `2.22456612` for D, off by 0.1 eV — noise.
- Most other near-misses found by the same scan are honest 6-dp roundings
  (±20 eV or less) of the right value, not stale numbers. Only the two above
  show the copy-paste signature of a single wrong source.
- Main's `drain(qou-psjm)` (372 AME/CODATA literals across 178 files,
  2026-09-05) did **not** reach these.

## Already done (this session, branch claude/anchor-followups-2026-08-08)

3 sites, both files verified by AST:
- `computations/phase5/phase3_triton_binding_convention_b.py` — `3He`
  `mp.mpf("7.71810")` (+58.7 eV) → `AME_B_HE3_MEV_VALIDATION`
- `computations/probes/rho_binding_constancy_probe.py` — `T` and `3He` bare
  float64 literals → `AME_B_TRITIUM_MEV_VALIDATION` / `AME_B_HE3_MEV_VALIDATION`

Both witnesses are queued to regenerate.

**The remaining ~62 live sites are UNCLAIMED — nobody is working them.**
