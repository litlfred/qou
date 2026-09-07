---
# qou-ndt5
title: 'Substrate branch: r(q) depends on s=sqrt(q); q=phi^2 is a second degeneration missing from the regime table'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T12:24:17Z
updated_at: 2026-09-07T12:29:49Z
---

ALGEBRA SETTLED (2026-09-07, PR #7077, issue #7076). s^2+s-1 has root set {1/phi, -phi}; q=s^2 gives {(3-sqrt5)/2, (3+sqrt5)/2} = {phi^-2, phi^2}, exactly reciprocal. Quartic 4s^4-s^3-4s^2+s+4 has NO real roots (all four complex), so that is the whole real locus. s -> -1/s is the UNIQUE lift of q -> 1/q preserving it (s -> 1/s maps the quadratic to s^2-s-1, a different polynomial). Source formula in descartes-elliptic-curve.md carries q^(3/2) and sqrt(q), so r depends on s not q; its 'expressible directly in q' claim is false. NOT closing this bean: whether s = -sqrt(q) is PHYSICALLY admissible is an open question about the framework, not settled by the algebra (AGENTS.md 13a).
