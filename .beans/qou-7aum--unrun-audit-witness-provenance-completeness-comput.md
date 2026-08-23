---
# qou-7aum
title: 'Unrun audit: witness provenance COMPLETENESS (computations/audits/) is red at 55 and is in no gate array'
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T15:46:27Z
updated_at: 2026-08-21T15:46:38Z
---

## Which audit (the trap — read first)

Two audits share the filename `witness_provenance_audit.py` and are **not**
forks. Be certain which you are running.

| path | lines | asks | wired |
|---|---|---|---|
| `computations/witness_provenance_audit.py` | 529 | does `scriptFile` actually **WRITE** the witness? (CORRECTNESS) | BLOCKING (bean qou-w9s3) |
| `computations/audits/witness_provenance_audit.py` | 292 | does the witness **DECLARE** engine/scriptFile/commitSha? (COMPLETENESS) | **this bean** — was unwired |

## Measured 2026-08-21 (PR #5373)

```
total scanned 2682 | PROV_OK 2325 | AUDIT_EXEMPT 74 | EXEMPT_NO_READER 227
EXEMPT_ACKNOWLEDGED 3 | PROV_MISSING 55 -> 52 | PROV_PARSE_ERROR 1 | ratio 0.980
```

**The committed witness was stale at 2296 / 10 (2026-08-01).** So the class grew
**10 -> 55** and 386 witnesses landed with nothing observing either — the audit
was in no gate array and no workflow. Third instance of the qou-j6gb pattern.

## Triage of the 55 — a count is not a work plan

| class | n | what it is | disposition |
|---|---|---|---|
| **C1 near-miss** | 9 | 2 of 3 fields present. Six are `chi-*` caches, the most-read witnesses in the set (13–46 py mentions), missing **only** `scriptFile` while carrying `engine`+`commitSha`+`producer`+`scriptHash` | highest value / lowest risk, BUT re-running them is the H_9…H_18 markov_peel compute (AGENTS.md names ⁶Li at H_18 as 18 min). Needs the long-compute logging discipline, not an idle pass |
| **C2 alt-convention** | 18 | carry `producer` + `scriptHash`/`scriptCommitSha` instead of the required triple — provenance EXISTS under other key names | **the real question**: is this a corpus convention the audit should recognise, or one that should be migrated? Answering it is worth more than draining C4. Do not silently widen the checker to accept `producer` without deciding |
| **C3 audit-only-as-field** | 11 | declare `audit_only`/`auditOnly` as a **field**; the exemption is a **filename glob** (`*-audit`/`*-scan`/`*-compliance`), so these are structurally invisible to it | **NOT exempted, deliberately.** qou-w9s3 hit this exact question on the sibling audit: *"I did NOT make the audit skip auditOnly witnesses — that would suppress a true finding by widening the checker."* Same call |
| **C4 bare** | 17 | no provenance of any kind | mechanical WitnessBuilder migration at the producer. **3 drained in #5373** |

Plus **1 PROV_PARSE_ERROR** (in none of the above): bean `qou-2ht2`.

## Done in #5373

- `completeness_ratio` carried as `mpf` + `_precision.fmt` — the audit was
  tripping the raw-float64 ratchet **on its own output**. Corpus
  dirty_witnesses 1539 -> 1538.
- 3 C4 producers wired through `WitnessBuilder.wrap_legacy` and re-run
  (55 -> 52). Verified zero lost keys, full `environment` (not the
  stripped-env defect of qou-y0xk), `start_time` at import so `durationMs`
  is real.
- Wired **ADVISORY** into `scripts/precision-gates.sh`. Not blocking: it is
  red on arrival, and that file's own header says a red-on-arrival gate gets
  skipped. Flip to blocking at PROV_MISSING 0.
- Corrected the stale all-clear in watcher-queue entry `63a90056cb57` + bean
  `e4cz` ("32 files, PROV_MISSING=0" — no longer true).
- Found + beaned `qou-j9yk`: `wrap_legacy` destroys a payload `computation`
  method-description.

## Next, in the order I would take it

1. **C2 (18)** — decide the convention question. Highest leverage: it is a
   third of the backlog and the answer is a ruling, not a sweep.
2. **C1 (9)** — the six chi-* caches want only `scriptFile`. Check whether the
   producer can stamp it without recomputing the payload; if it must re-run,
   budget it as long-compute with a teed log.
3. **C4 (14 remaining)** — mechanical, same wrap_legacy recipe as #5373, but
   watch the `computation`-clobber (qou-j9yk) on each.
4. **C3 (11)** — leave until 1–3 land; the disposition is a judgement about
   what `audit_only` means, not a fix.
