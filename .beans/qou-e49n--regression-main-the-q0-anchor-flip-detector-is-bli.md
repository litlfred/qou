---
# qou-e49n
title: 'REGRESSION (main): the q0-anchor FLIP DETECTOR is blind — _q0_value_for_anchor(''muon'') returns the PROTON value, because the tnjb proton sweep (9a9c6b31c7) regenerated computations/q-pinning-50-digit.witness.json AT THE PROTON PIN and that file is the muon branch''s source. 262 honest muon witnesses now misclassify as Q0_FLIP, and a REAL muon->proton flip would read Q0_OK. Gate is BLOCKING as of 2c5776834a.'
status: todo
type: task
priority: normal
created_at: 2026-08-19T20:10:58Z
updated_at: 2026-08-19T20:11:36Z
---

## Evidence (all read-only, reproducible in one line)

```
$ python3 -c "import qou_substrate.witness as qw; print(qw._q0_value_for_anchor('muon'))"
1.109978582751380807591669095610768879874499121873578736072814240181799   # <- the PROTON value
```

`_q0_value_for_anchor` (tools/qou-substrate/python/qou_substrate/witness.py):

```python
if anchor == "muon":
    p = _repo_root() / "computations" / "q-pinning-50-digit.witness.json"
    val = json.loads(p.read_text())["derived_50_digit"]["q"]
elif anchor == "proton":
    from qou_substrate.constants import Q_50_DIGIT_STR
    val = str(Q_50_DIGIT_STR)
```

The muon branch's source file now reads:

```
derived_50_digit.q = 1.10997858275138080759...   (proton)
q0Anchor           = proton
```

changed by `9a9c6b31c7` (2026-08-15) *"sweep(tnjb): first 25 witnesses
regenerated at the proton pin"*. AGENTS.md still documents this file as holding
the muon value `1.10997859555733471…`.

So `_q0_value_for_anchor("muon") == _q0_value_for_anchor("proton")`.

## Why it matters

`q0_anchor_consistency_audit.py` classifies by comparing a witness's `q0Value`
against `_canonical(anchor)`. With both anchors resolving to the proton pin:

- **262 witnesses that honestly declare `muon` + the muon value are reported
  `Q0_FLIP`** — false positives, and the gate is **BLOCKING** as of
  `2c5776834a` ("flip the gate to BLOCKING").
- **A genuine muon→proton flip would now report `Q0_OK`** — a false negative in
  exactly the direction the detector exists to watch (bean `tnjb`).

Committed audit witness on main says `Q0_FLIP: 0`, `Q0_OK: 653`; a live re-run
on main's tree gives `Q0_FLIP: 262`, `Q0_OK: 392`. The committed copy is 278
commits stale, which is what has been masking this.

## Verified NOT caused by the branch that found it

- the audit producer is byte-identical to main's (`git diff origin/main` = 0 lines)
- 261 of the 262 flagged files are untouched by the branch's diff
- the 1 file the branch does touch (`mass-table-ppb.witness.json`) has
  **byte-identical** `q0Anchor`/`q0Value` to main's copy
- no q₀ constant source is in the branch's diff

## Do NOT "fix" it by deriving the muon pin

The docstring records that exact attempt and its **revert**, same day
(2026-08-15): deriving the muon branch from `q_muon_at()` made the stamp
disagree with what muon producers actually compute with (1.1099785955573347
computed vs 1.1099785955541805 stamped). The field records the value the
producer used; do not re-derive it.

## The real question (owner/corpus call, not a mechanical fix)

The muon pin needs a *source* again. That is a decision about what the canonical
muon reference is now that the canonical q₀ witness has been migrated to proton
— it sits inside the tracked `qou-1c4y` migration and should not be guessed.
Candidates: restore a dedicated muon-pinned reference witness; pin the muon
string as a package constant beside `Q_50_DIGIT_STR`; or scope the detector to
proton-only and record that muon-anchored witnesses are unchecked until migrated.
