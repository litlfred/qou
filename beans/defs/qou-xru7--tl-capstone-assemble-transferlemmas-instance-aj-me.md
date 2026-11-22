---
# qou-xru7
title: 'TL-capstone: assemble TransferLemmas instance (aj_mem+division[DONE]+minimality) ⇒ instance-discharge strong_aj_figure_eight unconditional; BLOCKED on TL-aj_mem + TL-minimality'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T04:47:59Z
updated_at: 2026-11-22T21:33:04Z
parent: c7vs
---

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

**Scrapped: impossible as stated.** The class it asks to instantiate is proved uninhabitable on `main`: `Machinery/StrongAJFigureEightInstances.lean`, `not_transferLemmas` / `transferLemmas_isEmpty` (sorry-free). Over any nontrivial ring, `L` is a unit of the localized torus, so `L⁻¹·Â ∈ I` has smaller `topDeg`, and the `minimality` field fails. `strong_aj_figure_eight_of_transfer` is therefore vacuous. The live question is whether to restate `minimality` with the L-length (`topDeg − bottomDeg`) or over the non-localized ring `A⟨L⟩`, as Nguyen–Tran do; that restatement is an owner decision and is carried by `qou-y7o7`.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: SUPERSEDED-BY.** SUPERSEDED-BY not_transferLemmas (Machinery/StrongAJFigureEightInstances.lean): the class it would instantiate is uninhabitable. Scrapped earlier this pass; review confirms.
