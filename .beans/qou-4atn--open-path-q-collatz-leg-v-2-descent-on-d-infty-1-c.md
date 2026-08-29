---
# qou-4atn
title: 'OPEN PATH (q-Collatz leg): v_[2] descent ON D_infty. #1 (collatz_vtwo_domain_rescope) proved the corpus''s v_[2] counterexample -X-2 escapes D_infty, re-opening whether v_[2] descends on the domain-stable cone (which via reaches_cycle_of_descent_domainStable would close q-Collatz). Next: attempt a D_infty counterexample OR corroborate descent on known D_infty elements (fundamental cycle: 1+q^-1 -> q^-1 has v_[2] 1->0, descends). BLOCKER: qTwoValuation is Polynomial-only; cycle lives in Laurent (q^-1) -- needs Laurent v_[2] extension (Mathlib-gap).'
status: todo
type: task
priority: normal
created_at: 2026-08-01T20:37:26Z
updated_at: 2026-08-29T16:25:56Z
---

BLOCKER CLEARED 2026-08-29. This bean's stated blocker was: 'qTwoValuation is Polynomial-only; cycle lives in Laurent (q^-1) -- needs Laurent v_[2] extension (Mathlib-gap)'. That extension LANDED: QOU/MathlibExt/LaurentTwoValuation.lean defines laurentTwoVal = emultiplicity (T 1 + 1) on LaurentPolynomial Z, sorry-free, with laurentTwoVal_qinv = 0 and laurentTwoVal_one_add_qinv = 1.
The corroboration half also landed: AppendixSurreals/collatz_vtwo_cycle_descent.lean proves laurentTwoVal_descends_on_cycle (v_[2] drops 1 -> 0 on the even branch 1+q^-1 -> q^-1).
So the bean's 'next' is now the ONLY thing left: attempt a D_infty counterexample to v_[2]-descent, or characterise D_infty well enough to prove descent there. Note the honest ceiling: a global descent measure on D_infty closes q-Collatz-on-a-QOU via reaches_cycle_of_descent_domainStable, so this is NOT expected to close cheaply. Corroboration so far is 1 cycle + 0 general elements.
