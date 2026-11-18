---
# cj2d5
title: 'Conjecture carrier: BorelZagierQouVolumes (BorelZagierQouVolumes.lean) — §3b, framework/substrate §3b carrier'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-18T09:14:00Z
parent: qou-cv7z
---

§3b conjecture-class Lean carrier `instance : BorelZagierQouVolumes := sorry` at folio/quantum-observable-universe/lean/QOU/Archimedean/BorelZagierQouVolumes.lean:45. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

## Progress Update (2026-11-18 — Round 66, PR #8415)

- Added conditional non-vanishing theorems (`vol41_ne_zero`, `vol52_ne_zero`, `volBorromean_ne_zero`), pairwise rational-ratio exclusions (`vol41_ne_rat_smul_vol52`, `vol52_ne_rat_smul_volBorromean`), and rational linear combination injectivity `rat_comb_inj` in `QOU/Archimedean/BorelZagierQouVolumes.lean` (PR litlfred/qou#8415).
