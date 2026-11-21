---
# qou-xzda
title: 'B_sym: the chain closed form is NOT the trace — L_pn is overridden by a Reeb bound, worth a constant 1.6561 MeV'
status: todo
pr: 8265
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T21:46:07Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

MEASURED. `mass_binding_dashboard` documents the chain closed form as reproducing the exact p(3A) trace to |chain - exact| ~ 1e-13. It does not. The gap is 1.6561 MeV, CONSTANT across every isotope:

    iso    B_sym chain   B_sym exact    |diff|
    2H        2.233635      3.889692    1.6561
    3H        7.411603      9.067659    1.6561
    3He       5.140831      6.796887    1.6561
    4He      10.318798     11.974855    1.6561

ROOT CAUSE, in `_bond_type_L`: the pp and nn bonds are measured from the 2-nucleon trace, `log(tf/ta)`, but pn is REPLACED by a Reeb-flow bound `5*g_true/alpha`. Three bond constants, two different derivations.

    L_pn measured from the (1,1) trace = 0.929219
    L_pn used (Reeb-flow override)     = 0.533599
    difference 0.395620  x alpha       = 1.6561 MeV

Every chain contains exactly one L_pn term, which is why the offset is constant and A-independent.

THIS IS LOAD-BEARING, NOT COSMETIC. The deuteron is the framework's flagship exact result (err sym = 1.00), and the override is what produces it:

    B_AME(2H)                       2.2246 MeV
    B_sym with the Reeb override    2.2336 MeV   err 0.996
    B_sym with the MEASURED trace   3.8897 MeV   err 0.572

The trace over-binds the deuteron by 1.75x. So 'B_sym is exact at the deuteron' is a statement about the Reeb bound, not about the Frobenius pairing.

WHAT TO DECIDE (not mine to pick):
  1. If the Reeb bound is right, the docstring's 1e-13 claim must go and B_sym must be documented as trace-for-pp/nn + Reeb-for-pn, a hybrid.
  2. If the trace is right, the deuteron result is not what it appears and the 1.75x over-binding is the real starting point.
Either way the current state -- claiming agreement to 1e-13 while carrying a 1.6561 MeV substitution -- is a label contradicting its numbers.

The dashboard's `chain_resid` column already SHOWS 1.7e+00 for every isotope. It was computed, printed, and read past.

Acceptance: `chain_resid` either goes to ~1e-13, or the docstring states the hybrid and explains the substitution.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). **Superseded premise found:** the L_pn / Reeb-bound comparison is a statement about the old p–n interface letter (same γγ rescope). The docstring-vs-number contradiction is real, but the acceptance test (`chain_resid` -> 1e-13) is defined on the old letter. Not reworked; owner decision listed in the drain report.
