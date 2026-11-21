---
# cj317
title: 'Conjecture carrier: QCollatz (QCollatz.lean) — §3b, famous-open (aspirational §3b encoding)'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-18T10:36:00Z
parent: qcz14
---

§3b conjecture-class Lean carrier `instance : QCollatz := sorry` at folio/quantum-observable-universe/lean/QOU/AppendixSurreals/QCollatz.lean:39. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: famous-open (aspirational §3b encoding). Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.


## 2026-11-18 — Round 67 PR #8429 (`claude/round67-devacuify-6qbv-b9cj`)

- PR: https://github.com/litlfred/qou/pull/8429 (`309fbd8f12dcf4d789f3437e4bedf0425965e331`, C1 `202ce0a6f5124bc5df548850fb8706709c33eae1`)
- Probe: `computations/probes/round67_devacuify_6qbv_b9cj_probe.py` (`scriptHash = scriptSha256 = 33016f917e977bd9e4a22e14e192b44ea617b7cd335221741598e8aee1a1a640`, `dps = 80`, `allPassed = true`)
- Directory-mode static audits: `0 CRITICAL, 0 major, 0 advisory` across all 6 scripts; `0` `sorry` and `0` `axiom`.


## 2026-11-21T12:09:57Z — location corrected; supersession check (bean drain, pnp-collatz sibling, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): rests on none of the superseded premises; pure algebra over ℤ[q^{±1}].

The body's carrier description is stale. On main `2ae54ab40` there is **no** `instance : QCollatz := sorry`. `AppendixSurreals/QCollatz.lean:84` declares `class QCollatz (Skein : Type u) [CommRing Skein]`, and no instance exists. **Read its docstring's vacuity banner (bean `qou-dx7g`, 2026-11-20):** `pos` is a free field, so `pos := fun _ => False` satisfies the class; as written the class does not state the conjecture. Pinning it needs `Skein := LaurentPolynomial ℤ` and `pos` defined as the actual cone. That refactor touches ~15 consumers and is owner-gated.

Related progress this session: a sorry-free classification of **all** periodic orbits of the Skein–Collatz map on ℤ[q^{±1}] is in progress (`AppendixSurreals/collatz_cycle_classification.lean`, bean `qcz8`). It addresses the cycle half of the conjecture, not `reaches_cycle`.
