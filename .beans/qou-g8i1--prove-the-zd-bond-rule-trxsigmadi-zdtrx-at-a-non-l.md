---
# qou-g8i1
title: 'Prove the (z+d) bond rule: tr(x*(sigma+d*I)) = (z+d)*tr(x) at a non-last-strand generator'
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:42:04Z
updated_at: 2026-08-23T13:42:34Z
---

The one thing left from qou-kgsx, and much smaller than what that bean started with.

MEASURED RULE (16 nuclei numerically A=2..10 to 4.45e-31; 6 nuclei symbolically at n=6,9,12):

    tr(x * (sigma_g + d*I)) = (z + d) * tr(x),    z = q^3/(q^2+1)

verified for d = 0 (p-p bond), d = -h (n-n bond, giving exactly zbar), and d = d_iface (the p-n interface).

WHY IT IS NOT ALREADY A THEOREM: Markov theorem gives tr(x*sigma_n) = z*tr(x) for the LAST-STRAND generator, with x in H_n and sigma_n the new generator. The bond generators here are interior (gen 3k+2 for nucleon k, with strands above them), so the rule has the FORM of the Markov property without being an instance of it. Either it follows from the monotone structure of the atom word (each generator used once, never revisited -- the KEY FACT in chi_monotone_transfer docstring), or it is a genuinely wider multiplicativity.

WHY IT MATTERS: it is the sole remaining input to the whole delta result --
    tr_M^free/tr_M^atom = PROD 1/(z + d_b)
    P = 12 q^5 (q^2+1)(z + d_iface)
    exp(delta) = (zbar + dbar)/(z + d)
all follow from it in one line each, including nucleus-independence.

ROUTE TO TRY FIRST: the monotone/fine-Bratteli argument. Because each generator appears in one contiguous block and is never revisited, the transfer factorises per generator, and the added letter changes only that generator alpha,beta pair. The claim should reduce to a statement about a single fine-Bratteli level. If that works it is Lean-able (formalize-first) and closes the chain.

Audit: docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md section 4f.
