---
# s1ik
title: 'Lean-formalize the Phase-5q closed-form exact-Q identity (currently sympy-verified only, 11/11): product identity over generic CommRing'
status: completed
type: task
priority: normal
created_at: 2026-07-03T00:20:51Z
updated_at: 2026-07-03T00:47:10Z
---


## COMPLEMENT NOTE (2026-07-06, PR #3247)

Independently of the subsumption above, PR #3247 landed
`QOU/Hecke/ClosedFormInterfaceFactors.lean` (22 thms, sorry-free): the
EXPLICIT-factor layer — f_pp/f_nn/f_pn in the s-variable with the proven
flavor split δ(q), per-factor bar-involution, δ cubic factorization, the
bring-color identity f_pn = (f_pp+f_nn)/2 + h·δ/4, canonical Z/N assembly,
and the bond-kind trace bridge extending MarkovBondFactor. This COMPLEMENTS
(does not duplicate) the abstract fold in interface-knot-markov-z.lean;
cross-cited in both docstring directions.
