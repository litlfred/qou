---
# qou-g8i1
title: 'Prove the (z+d) bond rule: tr(x*(sigma+d*I)) = (z+d)*tr(x) at a non-last-strand generator'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T13:42:04Z
updated_at: 2026-08-23T13:50:49Z
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

MECHANISM FOUND 2026-08-19 -- the rule is the Markov property applied at a GAP, not at the last strand.

1. THE RULE IS NOT ABOUT JUNCTIONS, IT IS ABOUT UNUSED GENERATORS. Inserting (sigma_g + d*I) into the FREE deuteron word at each generator in turn, tr_M scales by (z+d) at g=2 AND NOWHERE ELSE (at g=0,1,3,4 the ratio is unrelated). g=2 is exactly the generator the free word does not use. Larger A confirms it as an EXACT SET MATCH: hits = {2,5} for (1,2), {2,5,8} for (2,2), equal to the unused set in both cases. So:

    W monotone and not using generator g  =>  tr_M(W*(sigma_g + d*I)) = (z+d)*tr_M(W)

2. d ENTERS TRIVIALLY. Inserting d*I changes nothing, so the d term reproduces tr_M(W) and the whole (z+d) family reduces to its d=0 case, tr_M(W*sigma_g) = z*tr_M(W). Only the sigma_g case needs proving.

3. THE MECHANISM IS MULTIPLICATIVITY ACROSS THE GAP. Measured: split any monotone word at any UNUSED generator g, W_< on gens <g and W_> on gens >g:

    tr_M(W) = tr_M(W_<) * tr_M(W_>)

ratio 1.0 at every unused generator of (1,2), (2,2), (2,3); worst |ratio-1| = 1.1e-30. In particular THE FREE TRACE FACTORISES EXACTLY OVER NUCLEONS, tr_free = PROD_k tr_M(nucleon_k), since the junctions ARE the free word unused generators.

WHY: because g is unused, W_< lies in <sigma_0..sigma_{g-1}> and W_> in <sigma_{g+1}..>, TWO SUBALGEBRAS THAT COMMUTE (|i-j|>=2). The gap makes them independent towers and inserting sigma_g is exactly the Markov step joining them. The rule IS the Markov property; the gap is what licenses it at an interior generator.

STATUS: mechanism, NOT a Lean proof. This reduces the bean from "why does an unexplained multiplicativity hold" to a named standard fact -- gap-multiplicativity of the Markov/Ocneanu trace plus the Markov property -- with the gap condition identified as the licensing hypothesis. Formalising is now bounded, and only the sigma_g case is needed.

LIT, narrowly: worth ONE look at whether Orellana / Geck-Lambropoulou / Birman / Webster-Williamson state the factorisation across an unused generator in this form, before deriving from scratch.

Audit section 4g.
