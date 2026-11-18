---
# cj4df
title: 'Conjecture carrier: QouInfraDischargesGoncharovZeta5 (QouInfraDischargesGoncharovZeta5.lean) — §3b, famous-open (aspirational §3b encoding)'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-18T09:14:00Z
parent: qou-cv7z
---

§3b conjecture-class Lean carrier `instance : QouInfraDischargesGoncharovZeta5 := sorry` at folio/quantum-observable-universe/lean/QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean:45. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: famous-open (aspirational §3b encoding). Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

## Progress Update (2026-11-18 — Round 66, PR #8415)

- Added conditional non-triviality of the spanned subspace (`span_ne_bot`), non-triviality of the relation kernel (`ker_ne_bot`), and non-zero generator witness (`exists_nonzero_generator`) in `QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean` (PR litlfred/qou#8415).
