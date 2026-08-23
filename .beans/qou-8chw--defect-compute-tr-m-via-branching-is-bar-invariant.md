---
# qou-8chw
title: 'DEFECT: compute_tr_m_via_branching is BAR-INVARIANT -- returns identical values at q and 1/q, disagreeing with the transfer by 387x at 1/q0'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:42:01Z
updated_at: 2026-08-23T18:35:39Z
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


RETRACTED 2026-08-23 -- THE BAR-INVARIANCE DOES NOT REPRODUCE.

Re-measured on current main after rebasing this branch:

    q0     0.5751722439177720556      (bean recorded 0.5750908722902754)
    1/q0   0.03320366093055433826     (bean recorded the SAME as q0)
    |gap across the bar| = 0.541969

So the claim in this bean's headline is FALSE as of now. The measurement was
taken on a branch that predated main's qou-zck8 / qou-cds4, which ported the
H_6 pn A-operator extract off float64, regenerated it, and fixed its consumers
to parse the extract's decimal strings. Do not plan around the invariance.

AND THE RETRACTION IS GOOD NEWS. The value moved ONTO the transfer value:

    branching (now)  0.5751722439177720556
    transfer         0.5751722439177718708
    relative         3.2e-16

A sibling working the mass table, from the other side and knowing nothing about
this branch, landed on the same number the transfer path and the Hoefsmit /
markov-peel arbiter give. That is a FOURTH agreement on tr_M^atom(D) and it
strengthens the qou-r9dv refresh. Stated at the right precision: the branching
path's rho factor is NumPy complex, so this is agreement AT THE FLOAT64 FLOOR of
the arithmetic it uses -- not a 16-digit corroboration, and two consecutive runs
differ in the last few digits. Do not quote it as exact.

WHAT SURVIVES, and it is the part that mattered for qou-r9dv: THE COMBINER STILL
CANNOT ARBITRATE AWAY FROM q0. Three inputs carry q into the A=2 path; only two
receive q_val:

    y_lambda_at(6, q_val)                      <- q_val, and BAR-EVEN (0.0
                                                  departure at 50 dps, 11 parts)
    evaluate_word_matrix_np(mu, intra, q_val)  <- q_val
    A^lambda_{xi nu}(I)                        <- JSON LOADED FROM DISK, frozen
                                                  at the q it was generated at

For q_val != q0 the return is a HYBRID: a frozen operator at q0 contracted
against weights and blocks at q_val. Neither tr_M at q_val nor at q0. Same class
as the AGENTS.md layer-straddle rule, with q-values in place of anchors. At 1/q0
it returns +0.0332 against the transfer's -0.00148 -- it does not agree in SIGN.

The trap this bean named is therefore intact: at q_val = q0 the hybrid
degenerates to the correct value, so the function is right exactly where it is
usually tested, and it fails toward AGREEMENT with an independent path at the
anchor.

SECOND FINDING, unrelated to the bar. Of the two extracts on disk, the H_9 nn
one carries NO q0Value stamp at all -- a frozen operator that does not record
which q it was frozen at is invisible to every q0-drift check. Ten of the twelve
(n, interface) extracts are absent entirely, so the A=2 pn deuteron is the only
path this defect can currently reach; A >= 3 goes through the transfer.

THE FIX IS NOT A DOCSTRING. This bean's FIRST STEP allowed for "bar-even by
design, so document the symmetry". It is not by design and, post-qou-zck8, not
even bar-even: the operator is frozen. Honest minimum is to REJECT q_val != q0
with a clear error rather than return a number; regenerating A^lambda at
arbitrary q is the real fix and is separate, larger work. NOT done here -- I am
not touching a producer a sibling is actively regenerating without coordinating
first.

Probe: computations/branching_q_threading_probe.py -- ASSERTIONS PASS, exit 0.
Conclusions rest only on exact quantities (JSON fields, source facts) and
mpmath at 60 dps; the one float64 number is labelled as such.

STATUS: the original claim is retracted; the underlying defect is confirmed and
stays open, re-scoped to "q_val is not threaded into the A^lambda extract".
