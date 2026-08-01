---
# qou-q64u
title: Lean-formalize the Milnor = leading-Vassiliev bridge (Habegger–Masbaum 2000; Bar-Natan 1995; Meilhan–Yasuhara)
status: todo
type: task
priority: normal
tags:
    - formalization
    - knot-theory
created_at: 2026-08-01T19:01:04Z
updated_at: 2026-08-01T19:01:04Z
parent: qou-pddf
---

The general proof of the exact-order Milnor law (order(D_A) = 2(A−1), i.e. leading coeff = μ̄(12…A) ≠ 0) rests on: the first non-vanishing Vassiliev invariant of an A-component Brunnian link at degree 2(A−1) is ±μ̄(12…A) = ±1. Currently CITATION-ONLY (Bar-Natan, 'On the Vassiliev knot invariants', 1995; Habegger–Masbaum, 'The Kontsevich integral and Milnor's invariants', 2000; Meilhan–Yasuhara). The Vassiliev/finite-type infra scaffold (branch claude/vassiliev-finite-type-infra-2026-08-01) states this as an instance-less conjecture class — NOT axiomatized. This task: eventually Lean-prove the bridge on top of that scaffold (chord diagrams → 4T → weight systems → finite-type invariants → Kontsevich universality → the Milnor bridge). Large multi-session effort; caveat: verify the cited theorems' exact hypotheses match our Brunnian iterated-commutator generator (papers are not infallible / may need adaptation).
