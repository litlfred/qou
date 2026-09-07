---
# qou-ndt5
title: 'Substrate branch: r(q) depends on s=sqrt(q); q=phi^2 is a second degeneration missing from the regime table'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T12:24:17Z
updated_at: 2026-09-07T12:58:01Z
---

ALGEBRA SETTLED (2026-09-07, PR #7077, issue #7076). s^2+s-1 has root set {1/phi, -phi}; q=s^2 gives {(3-sqrt5)/2, (3+sqrt5)/2} = {phi^-2, phi^2}, exactly reciprocal. Quartic 4s^4-s^3-4s^2+s+4 has NO real roots (all four complex), so that is the whole real locus. s -> -1/s is the UNIQUE lift of q -> 1/q preserving it (s -> 1/s maps the quadratic to s^2-s-1, a different polynomial). Source formula in descartes-elliptic-curve.md carries q^(3/2) and sqrt(q), so r depends on s not q; its 'expressible directly in q' claim is false. NOT closing this bean: whether s = -sqrt(q) is PHYSICALLY admissible is an open question about the framework, not settled by the algebra (AGENTS.md 13a).

REFRAMED + FORMALISED 2026-09-07. My earlier framing was wrong twice. (1) 'r depends on s not q' misses the point: the modulus is z = s - 1/s (the corpus's own spacetime ratio) and r is a clean POLYNOMIAL in z, r = (5/27)(z+1)(4z^2-z+4) = (5/27)(4z^3+3z^2+3z+4) — which is EXACTLY the q_W(z) already in t-duality-elliptic.md. Two blocks agree; one sentence of presentation in a third is wrong. (2) 'the corpus lists half the locus' is wrong: there is ONE degeneration, at z = -1 (since z+1=0 <=> s^2+s-1=0), whose two q-preimages are phi^-2 and phi^2. The table lists one preimage of one point. Now Lean: QOU/BringsSurface/ColourCurveModulus.lean, 6 theorems, lean-direct exit 0 with -DautoImplicit=false, 0 sorry, axioms = {propext, Classical.choice, Quot.sound} only.

OWNER RULING 2026-09-07, verbatim: 'not sure. don't exclude but maybe not observable.' So the negative branch s = -sqrt(q) stays OPEN, not excluded, with the live possibility that the two sheets are physically identified and the branch carries no observable. Bean stays open per AGENTS.md 13a. GATES: the bounded window (phi^-2, phi^2) depends on this — if the negative branch is unreachable, q = phi^2 is not a reachable degeneration and the window is NOT bounded above. The Lean and the bar-defect results are unaffected: they are statements about z, and z = -1 is one point regardless of how many q-preimages are physical.
