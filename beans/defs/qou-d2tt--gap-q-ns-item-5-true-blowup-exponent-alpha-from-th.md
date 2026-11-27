---
# qou-d2tt
title: 'GAP: q-NS item 5, true blowup exponent alpha from the q-NS spectrum'
status: todo
type: task
created_at: 2026-11-27T17:26:53Z
updated_at: 2026-11-27T17:26:53Z
parent: qou-a3n3
---

Item (5) of qou-innq (sibling of that bean, same parent). Open conjecture; do not close until alpha is derived.

State: p2-critical-exponent gives two heuristic values, and the CriticalExponent carrier no longer fixes alpha=4/3 (qou-4670). Part A (PR #9485, q_ns_enstrophy_order_parameter.lean) shows two things: alpha=2 on the physical layer is a unit-conversion artifact, and Part A is FALSE on substrate-layer data. So alpha has no derived value yet. Deriving one depends on two things: the Part A layer ruling, still pending with the owner; and a modal law with triad transfer, which QNsWellposednessContext cannot see (stokesContext satisfies it). The q_turbulence_spectrum file carries 8 sorries.

Next honest step: after the Part A layer ruling, define alpha as a limit of a QOU-defined spectral quantity, then prove or refute that the limit exists. No fitting: alpha may not be chosen to match K41 or any measured exponent. Sources rule 2026-11-27: QOU-formalized work only.
