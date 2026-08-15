---
# qou-q9ih
title: 'D1: Route C M1 — construct the (Q,W) reproducing {3,4} + bar split (7,1); fitted quiver = candidate only (parent qou-rtec)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-15T10:56:28Z
---


## 2026-08-15 first rung — implementation class pruned (Lean-proved)

`QOU/QBeta/QuiverMirrorAutomorphismExcluded.lean` (sorry-free, axioms
[propext, Quot.sound]): any COUNT-INVARIANT mirror implementation — a
quiver automorphism, the op-duality Q ↦ Q^op, or any DT-preserving
equivalence — forces every readable pair amphichiral, so the (4,3)
datum is unreachable (`count_invariant_excludes_five_two`), and
conversely reading (4,3) forces Ω(σd) ≠ Ω(d)
(`five_two_forces_count_breaking`).

CONSEQUENCE for the search: the M1 object is (quiver, potential, TWO
stability rays) with the mirror acting on the RAY, never (quiver +
automorphism). Consistent with M2's distinct-Borel-rays finding
(RouteCM3CategoryIdentification). Extends Driver14's no-scalar theorem
one level up (no count-preserving symmetry implementation either).

REMAINING (the big rung, still open): actually construct a (Q,W) + ray
pair whose DT counts are (4,3) with bar split (7,1), FROM Hecke/Bring
data. A fitted quiver stays a labeled CANDIDATE only (anti-laundering).
