---
# qou-j0nv
title: reaches_q0() is structurally blind to hardcoded q0 literals — 38 producers stamped q0_anchor=False hold one
status: todo
type: bug
priority: normal
created_at: 2026-08-30T12:32:18Z
updated_at: 2026-08-30T12:32:18Z
---

Found while closing `qou-0hnz`; measured before filing.

## The defect

`scripts/migrate_bare_producer_provenance.py:114`

```python
Q_MARKERS = ("q_parameter", "Q_50_DIGIT", "qou_substrate.constants", "q_at", "Q_MP")
```

Every marker is a **resolution name**. A producer that hardcodes
`1.1099785955573347…` matches none of them, so `reaches_q0()` (`:164`) returns
False and the script stamps `q0_anchor=False` — "no q0 in this producer's cone" —
over a file with a q0 literal in it.

The function's own docstring says it is *"Deliberately conservative: anything
this cannot rule out is treated as q0-dependent, so the anchor is stamped."*
That is precisely backwards for literals: it cannot SEE them, so it silently
rules them out. The conservatism is real for the import-hop case and absent for
the literal case.

## Measured population

Of **389** producers stamping `q0_anchor=False`, **44** hold a q0 decimal literal
on a non-comment line with no resolution marker anywhere. Splitting those:

| | count |
|---|---|
| audits/detectors holding the literal as a fixture — legitimate | 6 |
| **real producers — the defect** | **38** |

Examples: `a3_magnitude_berezinian_crossterm_probe`,
`alpha_em_perloop_integer_forcedness_probe`,
`deltalambda/mu4_rhoF_cluster_derivation_probe`,
`probes/binding_additive_linked_cluster_probe`.

Consequence: those 38 carry no `q0Anchor`, land in `Q0_ANCHOR_MISSING`, and are
invisible to any check keyed on the stamp — while actually being q0-dependent.
This is how `tau_binding_hitchin_wzw_wall_probe` came to stamp
`q0_anchor=False` under a comment reading "no q0 in this producer's cone" with
the literal 30 lines above it.

## Todo

- [ ] Add a q0-literal pattern to the detector so `reaches_q0` sees pinned files.
- [ ] Do NOT mass-restamp on the strength of it: re-running the migration script
      would rewrite 38 producers' provenance in one sweep. Report first.
- [ ] Exempt audits/detectors that hold the literal deliberately as a fixture.
