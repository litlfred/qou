---
# qou-8chw
title: 'DEFECT: compute_tr_m_via_branching is BAR-INVARIANT -- returns identical values at q and 1/q, disagreeing with the transfer by 387x at 1/q0'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:42:01Z
updated_at: 2026-08-23T17:42:36Z
---

MEASURED 2026-08-19. computations/canonical_tr_m_via_branching.compute_tr_m_via_branching(Z, N, q_val) returns IDENTICAL values at q and 1/q:

    q_val=None   -> 0.5750908722902753612501
    q_val=q0     -> 0.575090872290275362348
    q_val=1/q0   -> 0.575090872290275362348    <- IDENTICAL to q0
    q_val=1.5    -> 0.6872499967008388608549
    q_val=2.0    -> 0.879272760520779915328
    q_val=0.5    -> 0.879272760520779915328    <- IDENTICAL to 2.0

So q_val IS honoured in magnitude (1.5 and 2.0 differ) but the function is BAR-INVARIANT. The transfer path gives tr_M_atom(D) at 1/q0 = -0.001480853171161937, so the two disagree by 387x at the bar image while agreeing to 1.4e-4 at q0.

WHY THIS MATTERS BEYOND ITS OWN CORRECTNESS: I reached for this function as an INDEPENDENT ARBITER for the transfer value at 1/q0 (qou-r9dv) and it cannot serve -- a bar-invariant function corroborates nothing about bar. Worse, it agrees with the transfer AT q0, so a check run only at the anchor would look like confirmation.

WHICH IS RIGHT IS NOT DECIDED HERE. Evidence that the TRANSFER is right away from q0: the word demonstrably re-lifts at 1/q0 (12 of 23 deuteron letters change; flavor_split_leading is exactly bar-odd, f(1/q) = -q^2 f(q)), and the bond-product formula tr_free/tr_atom = PROD 1/(z + d_b) holds at 4.45e-31 over 16 nuclei A=2..10 using the bar image throughout. Evidence for BRANCHING at 1/q0: none found. But that is not a proof, and the branching path may be computing a deliberately bar-even object (its docstring says it returns |tr_M|, though abs alone does not explain it).

FIRST STEP: read what the function actually varies with q_val. If it is bar-even BY DESIGN, the q_val parameter should REJECT q < 1 or document the symmetry -- silently returning the q image value is the trap. If it is not by design, it is a bug in the q-threading.

Found while arbitrating qou-r9dv.
