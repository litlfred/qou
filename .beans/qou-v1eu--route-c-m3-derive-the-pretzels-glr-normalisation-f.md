---
# qou-v1eu
title: 'Route C M3: derive the pretzel''s GL(r) normalisation from the q-Wronskian pairing (GGM 92/93)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T17:43:28Z
updated_at: 2026-09-14T17:44:03Z
---


## Claimed 2026-09-14 (issue #7376, branch `claude/binding-gap-categorical-research-cem5tp`)

Follow-on from `qou-x3iv` (#7152, merged) and `qou-lzzi` (#7333, merged). Both routes
closed on ONE gap: the per-knot `GL(r)` normalisation.

**The finding that makes it a derivation.** GGM (92)/(93) — read further than either
merged PR did — are orthogonality relations on the fundamental solution matrix:

    (1/2) W_m(q) J W_l(q^-1)^T  in  SL(3, Z[q^+-]),   J = [[0,0,1],[0,2,0],[1,0,0]]

So the constant matrices flanking `W^-1(x;q)^T` in (94a)-(94d) / (186a)-(186d) are
constrained by a bilinear pairing the q-difference operator ITSELF determines — a
q-Wronskian, computable from the operator's coefficients via its formal adjoint under
the q-shift. Not a free choice.

**And it is the same object Part 17 measured.** `h_1(q,X) h~_1(q^-1,X^-1)` is a
`W(q) (...) W(q^-1)^T` pairing one entry at a time; Part 17's `Z[s(x)]` integrality is a
(93)-type statement. The two routes point at the same EQUATION, not merely the same gap.

**Anti-fit, load-bearing.** `J` is computed FROM the operator, never solved for against
the index. If the computed `J` does not close the gap, that is the result.

**Gates, in order:** (1) `J` from the 5_2 operator reproduces GGM's
`[[0,0,1],[0,2,0],[1,0,0]]`; (2) same at rank 2 for 4_1; (3) only then rank 6.
GGM state (94)/(186) as Conjecture 12 / Conjecture 19, so a derived `J` reproducing
their two cases is strictly stronger than what is held.
