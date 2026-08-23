---
# qou-q0inv
title: 'q0_consistency_audit labels the LIVE canonical q0 as "stale" — and contradicts itself'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:25:00Z
updated_at: 2026-08-23T17:25:00Z
---

`computations/audits/q0_consistency_audit.py` scans `computations/**/*.py` and
flags scripts that hardcode what it calls the "stale" q₀. Its committed witness
carries three fields that cannot all be true at once:

```
canonical_q0_source : "q_parameter.q_at() / Q_50_DIGIT_STR (proton pin, habiro-refined)"
stale_pre_habiro_q0 : "1.10997858275138080759…"
canonical_proton_q0 : "1.10997859555733471989…"
```

Measured live:

```
q_parameter.Q          = 1.1099785827513808
q_parameter.Q_50_DIGIT = 1.1099785827513808075916690956107688798744991218736
```

**`Q_50_DIGIT_STR` IS the value the witness labels `stale_pre_habiro_q0`.** The
audit names that constant as its canonical source and, in the same payload,
calls its value stale. The value it calls `canonical_proton_q0` is the one
AGENTS.md calls the **muon / ideal-CAL-2** pin.

The docstring says the same thing (lines 6–11): *"Canonical q₀ is the
proton-anchored, habiro-refined value C = 1.10997859555733471… (`q_parameter.Q`)"*
— `q_parameter.Q` is not that value.

## Why this matters more than a comment typo

This is a **live tree-scanning audit**. If its labels are inverted, it is
telling every agent who runs it to migrate *away* from the pin AGENTS.md makes
canonical for all new compute (owner directive 2026-08-07).

## What I did NOT do, and why

I did not flip the labels. Doing so changes what the audit flags across the
whole tree — a convention migration, which AGENTS.md scopes as a tracked sweep
needing sign-off, not a drive-by inside a drain PR. Same reason `qou-akdup` was
beaned rather than fixed.

## A possible innocent reading, to check before flipping

Within `computations/`, the **muon** pin was historically called "canonical"
(the q0-value-drift audit still buckets 607 muon-pinned fields as `canonical`).
This audit may be using that older sense while *also* saying "proton pin" — in
which case the fix is to disambiguate the words, not swap the numbers. Either
way the current payload is self-contradictory.

## Also: the same root/subdir duplication as `qou-akdup`

Two witnesses, two paths, different payloads:

- `computations/audits/q0-consistency-audit.witness.json` — has all three fields
- `computations/q0-consistency-audit.witness.json` — has `canonical_q0_source`
  (without "habiro-refined") and **neither** of the two value fields

## Suggested disposition

1. Decide whether the numbers or the words are wrong.
2. Re-run and re-emit; deprecate the superseded root copy.
3. Re-check what the audit has been flagging in the meantime — anything it
   "migrated" may have been moved off the canonical pin.

Found while draining tier C (bean `dgpc`), PR #5289.
