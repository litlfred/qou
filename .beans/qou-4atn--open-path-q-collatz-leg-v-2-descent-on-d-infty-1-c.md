---
# qou-4atn
title: 'OPEN PATH (q-Collatz leg): v_[2] descent ON D_infty. #1 (collatz_vtwo_domain_rescope) proved the corpus''s v_[2] counterexample -X-2 escapes D_infty, re-opening whether v_[2] descends on the domain-stable cone (which via reaches_cycle_of_descent_domainStable would close q-Collatz). Next: attempt a D_infty counterexample OR corroborate descent on known D_infty elements (fundamental cycle: 1+q^-1 -> q^-1 has v_[2] 1->0, descends). BLOCKER: qTwoValuation is Polynomial-only; cycle lives in Laurent (q^-1) -- needs Laurent v_[2] extension (Mathlib-gap).'
status: completed
type: task
priority: normal
created_at: 2026-08-01T20:37:26Z
updated_at: 2026-08-29T17:57:53Z
---

BLOCKER CLEARED 2026-08-29. This bean's stated blocker was: 'qTwoValuation is Polynomial-only; cycle lives in Laurent (q^-1) -- needs Laurent v_[2] extension (Mathlib-gap)'. That extension LANDED: QOU/MathlibExt/LaurentTwoValuation.lean defines laurentTwoVal = emultiplicity (T 1 + 1) on LaurentPolynomial Z, sorry-free, with laurentTwoVal_qinv = 0 and laurentTwoVal_one_add_qinv = 1.
The corroboration half also landed: AppendixSurreals/collatz_vtwo_cycle_descent.lean proves laurentTwoVal_descends_on_cycle (v_[2] drops 1 -> 0 on the even branch 1+q^-1 -> q^-1).
So the bean's 'next' is now the ONLY thing left: attempt a D_infty counterexample to v_[2]-descent, or characterise D_infty well enough to prove descent there. Note the honest ceiling: a global descent measure on D_infty closes q-Collatz-on-a-QOU via reaches_cycle_of_descent_domainStable, so this is NOT expected to close cheaply. Corroboration so far is 1 cycle + 0 general elements.

SETTLED NEGATIVE 2026-08-29, PR #6042, commit 105465b558. Answer: v_[2] does NOT descend on D_inf.

The reason is structural, not a lucky witness, which is why this closes the bean rather than adding one more datum. reaches_cycle_of_descent_domainStable wants mu : Skein -> N with mu(C P) < mu P off the attractor. mu lands in N, so that is impossible wherever mu P = 0. And v_[2] vanishes on EVERY q-odd element: q-odd means [2]_q divides P+1, and if [2]_q divided P too it would divide 1 and be a unit, which T1_add_one_not_isUnit forbids. So every q-odd point of D_inf refutes v_[2] at once -- no search needed once you see it.

Carrier: content/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_vtwo_dinf_refutation.lean, sorry-free, axiom-audited (only propext / Classical.choice / Quot.sound; the two general obstruction lemmas need only propext + Quot.sound).

Witness, produced by CONSTRUCTION not search (computations/qcollatz_vtwo_domain_stable_probe.py): backward orbits of the attractor are in D_inf by definition, so the probe generates the backward tree exactly and ALSO verifies each node forward by iterating to the cycle.
  witnessP = q^-1 (q^6+7q^5+20q^4+29q^3+21q^2+6q+1), v_[2] = 0, reaches the cycle in 7 steps
  C(witnessP) = q^-1 (q+1)^7, v_[2] = 7
Every odd-branch node in the tree fails identically (3 of 3: 0->7, 0->13, 0->19).

SCOPE (a): this refutes v_[2], NOT the descent route. Another mu may still work.

WHAT SURVIVES AS FORWARD GUIDANCE, and it is the useful part: descent_measure_pos_off_target says any candidate mu must be STRICTLY POSITIVE at every non-attractor point of D_inf. Since D_inf contains q-odd points, any valuation-like candidate that vanishes on the q-odd part is excluded for exactly the same reason -- so the next candidate must not be one. That rules out the obvious variants (v_[3], any [k]_q-adic valuation, any 'number of times a fixed irreducible divides') in one stroke, since all of them vanish somewhere. A working mu likely has to be a HEIGHT (degree, coefficient norm) rather than a valuation, or a combination whose valuation part is offset.
