---
# qou-7fnr
title: 'W1 local q-dilation: does the SAME rationality theorem exclude t -> mu t at the branch point, or is the local chart genuinely outside it? (tests my own ''not excluded'' claim from #6695)'
status: todo
type: task
created_at: 2026-09-05T06:35:36Z
updated_at: 2026-09-05T06:35:36Z
---

## Question (2026-09-05, follows qou-1z28 / #6695)

#6695 pruned W1 route 1 (a rational q-connection on the base z-line) scope-(b), via: colour cubic irreducible over K(z) => no sheet rational in z; sheets algebraic => D-finite; a rational rank-3 q-difference system => a sheet is q-holonomic; D-finite AND q-holonomic => rational (Bezivin / Ramis / Schaefke-Singer). Contradiction.

In that PR I asserted, in the audit doc AND in the content scope note, that the LOCAL q-dilation t -> mu t at a ramification point is NOT excluded, on the grounds that 'every power series satisfies a first-order q-equation with a power-series coefficient and the theorem does not apply'. That reason is about POWER-SERIES coefficients. The theorem needs RATIONAL coefficients. So the claim as I stated it does not establish what it says, and the local case may in fact be excluded by the very same argument. Test it.

## The setup

At a simple branch point z = z_c + t^2 (z_c a root of the branch sextic 16z^6+24z^5+35z^4+50z^3+35z^2+24z+16, which is IRREDUCIBLE over Q, so K = Q(z_c) is an exact degree-6 field), the sheets are power series in t. Each sheet is algebraic over K(t) — it satisfies the cubic P(X, z_c + t^2) = 0 over K[t] — hence D-finite in t. A q-dilation t -> mu t with coefficients rational in t would make it q-holonomic in t. Same theorem, same shape.

## What decides it

Whether the sheets are RATIONAL in t. So the local analogue of step 1: does P(X, z_c + t^2) have a root in K(t)? Structurally the two ramified sheets are conjugate under t -> -t and the third is analytic in t^2, so over the completion the cubic splits (linear)(quadratic) — but a root in the COMPLETION is not a root in K(t), and only the latter would let a sheet be rational.

- If NO sheet is rational in t: the same contradiction runs, the local dilation is excluded too, and #6695's 'not excluded' must be corrected — the prune is much stronger and W1's surviving space shrinks.
- If a sheet IS rational in t: the local chart is genuinely outside the theorem, my claim stands with a real reason rather than the wrong one I gave, and that rational sheet is itself a structural fact worth having.

## PLAN
1. Exact: factor P(X, z_c + t^2) over K(t), K = Q(z_c) the degree-6 field (sympy with the sextic as the minimal polynomial). Does it have a root in K(t)?
2. Whichever way it falls, formalize the algebraic half in Lean (sorry-free, generic char-0 where possible), mirroring QOU.Mass.ColorCubicIrreducible.
3. Probe: the local-coordinate analogue of the #6695 search — series of each sheet in t, exact; search for a q-difference relation with rational-in-t coefficients; controls.
4. Correct #6695's audit doc and the content scope note if the answer is 'excluded'. That correction is the deliverable if it goes that way, and it must name what it contaminated: docs/audits/2026-09-04-w1-route1-base-qshift-rationality-prune.md, the qdifference-kernel-prolongation-symbol scope note, the #6695 PR body, and beans qou-1z28 / qou-d8de.
