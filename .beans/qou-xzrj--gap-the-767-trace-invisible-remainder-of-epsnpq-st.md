---
# qou-xzrj
title: 'GAP: the 7.67% trace-invisible remainder of epsNPq (step 8)'
status: todo
type: task
priority: normal
created_at: 2026-08-26T21:07:16Z
updated_at: 2026-08-26T21:08:07Z
---

Opened from `qou-cds1` / step 8 of the 2026-05-24 Q_β fitting-finding audit,
on owner instruction to bean-and-queue anything arising while `qou-cds1` is the
priority.

## What is open

`epsNPq` — the functional the Q_β ansatz calls `ε(Δ)` — is the **coordinate sum**
of the neutron−proton normal-form difference, not the Frobenius counit
(`qou-99qc`). It is not a trace: 8 of 36 ordered basis pairs fail cyclicity in
the regular representation of `H_3(q)`
(`computations/qbeta/qbeta_net_trace_invariance_probe.py`, 25/25).

`H_3(q)` is split semisimple, so `H = Z(H) ⊕ [H,H]` with dim 3 + 3, and **every**
trace annihilates `[H,H]`. At q₀:

    epsNPq   = −0.187207194529378
      central   −0.172847658641848   92.33 %
      commutator −0.014359535887530   7.67 %

The central 92.33 % is **derived**: it is exhibited as the unique trace agreeing
with `net` on the centre,

    a_(3) = (q+1)/((q²+1)(q²−q+1))
    a_(2,1) = q(q²−1)/(q⁴+q²+1)
    a_(1³) = q³(q−1)/((q²+1)(q²+q+1))

verified to reproduce `net` on the whole centre, annihilate `[H,H]`, and give
exactly the central part on Δ.

**The remaining 7.67 % is what is open.** No Markov trace, no augmentation, no
`χ^λ` and no combination of them can see it, so it is not an eigenvalue of
anything in the framework's current observable vocabulary. Q_β's +0.168 % match
to CODATA requires all of it: the trace-visible part alone gives 0.723537 MeV,
−7.52 %.

## What is already known about it

- It is **bar-even**, exactly: `net(dC) = −(q²−1)²/(q⁴+q²+1)`
  (`qbeta_alpha_commutator_floor_probe.py`, 22/22). So it supplies no bar-odd
  material — which *extends* the sibling prune `fcffeee29` rather than breaking it.
- It is **z-independent**, hence convention-independent: identical in C and D,
  and it is the whole z-free part of the ladder phase (13.72 % of 2α in C,
  17.73 % in D).
- Related: conjugating both nucleon words by one basis element — a Markov-I
  move — swings Q_β over 0.692169…0.783646 MeV, ≈ 70× the residual. `net` takes
  exactly two values across the six, because conjugation by `w₀` is the diagram
  automorphism `s₀↔s₁` and permutes the standard basis.

## The question

What object in the framework carries a non-cyclic functional's value on `[H,H]`,
and is the preferred presentation (the "single-wrap convention", audit step 4)
derivable rather than chosen? Step 8's postulate is now narrowed from the whole
of `net` to this remainder; answering it would close the postulate or replace it.
