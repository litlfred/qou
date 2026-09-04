---
# qou-h7mh
title: 'binding: the gap is coordination geometry, not a missing force term — derive the bond count from the SU(4) partition shape'
status: todo
type: task
created_at: 2026-08-08T20:51:00Z
updated_at: 2026-08-08T20:51:00Z
---

MEASUREMENT (read-only, this session). B_AME / B_sym_chain on the most-bound isotope at each A:

    A       4     6     9    12    16    24    40    56    90   140   208   238
    ratio 2.742 1.738 1.837 2.160 2.169 2.175 2.144 2.187 2.122 1.997 1.849 1.771

A plateau at ~2.15 across 12 <= A <= 90, a deficit below A~12, a decline above A~100, and a 4He spike to 2.742. That is the SEMF decomposition — volume/saturation, surface, Coulomb (~Z^2), closed shell — emerging as a COORDINATION RATIO against the framework's own chain, with nothing fitted.

THE DEFECT IS TOPOLOGICAL, NOT ENERGETIC.
  * bond ENERGIES are right: the deuteron is a single p-n bond and B_AME/B_chain = 1.00 exactly.
  * bond COUNT is wrong: B_sym = alpha[(Z-1)L_pp + L_pn + (N-1)L_nn] walks a 1-D chain of (A-1) bonds through a 3-D object.
  * all-pairs is the other extreme and over-binds with no saturation: B_AME/B_allpairs falls 0.996 (2H) -> 0.100 (56Fe).

Isospin/8-fold-way content is ALREADY present — L_pp=0.6945, L_pn=0.5336, L_nn=1.237 are distinct, so asymmetry is built in. What is missing is geometry, not flavour.

> **CORRECTION 2026-08-08 (bean qou-c6gx) — the block above is STALE and its
> headline claim is now FALSE.** It was measured while the Reeb override was
> still in place, i.e. with `L_pn = 5*g_reeb/alpha = 0.5336` substituted for the
> trace value. That override was removed the same day (bean qou-xzda, commit
> 5e0c874b) because `B = 5g` is dimensionally impossible: `g` depends only on
> q0, a mass RATIO, so `5g = 2.2336` is a pure number declared to be MeV.
>
> With the trace value `L_pn = 0.929219`:
>   * "bond ENERGIES are right / deuteron exact" — **NO.** The deuteron
>     over-binds by +74.85% (3.8897 vs 2.2246). Its exactness was a property of
>     the override, not of the Frobenius pairing.
>   * the ordering is `L_nn (1.2370) > L_pn (0.9292) > L_pp (0.6945)`, so the
>     p-n bond is the MIDDLE one. The puzzle recorded below ("makes the p-n bond
>     the WEAKEST") dissolves; what remains anomalous is that L_nn is LARGEST,
>     i.e. the model binds the dineutron hardest of the three.
>   * "the defect is topological, NOT energetic" — **too strong; it is both.**
>     The single-bond case has no topology left to get wrong and still misses by
>     75%, so an energetic defect exists independently of coordination.
>
> The A-ratio table above still stands as a measurement; only its interpretation
> moves, since the denominator B_sym_chain shifted.
>
> **NEW, and it bears directly on "derive the bond count":** the chain
> bond-multiset is not merely under-derived, it is not well defined.
> `atom_braid_word_3A` hard-codes `ordering = ['p']*Z + ['n']*N`, and B depends
> on that arbitrary order:
>
>       atom   canonical    B_canon     B_min      B_max     spread    B_AME
>       3He    ppn          6.7969      6.7969     7.7794    0.9825    7.7180
>       4He    ppnn        11.9749     10.6866    12.9574    2.2708   28.2957
>       6Li    pppnnn      20.0600     18.4660    21.0425    2.5766   31.9946
>       7Li    pppnnnn     25.2380     23.3382    26.2205    2.8823   39.2445
>
> A nucleus has no ordering, so up to 2.88 MeV is a non-physical degree of
> freedom. The convention is not even the good choice: `3He = pnp` gives 7.7794
> (+0.79% of AME) where canonical `ppn` gives -11.9%. The mirror pair is decided
> by it too — `pnn`/`ppn` splits 2.271 MeV, `npn`/`pnp` splits EXACTLY 0
> (nature: 0.764).
>
> So whatever derives the coordination must also make the answer
> order-independent. A bond COUNT alone will not: these orderings all have the
> same count and differ only in the multiset.

THE LEVER ALREADY EXISTS: atom_braid_word_3A(Z, N, *, m_pp=1, m_pn=1, m_nn=1, ...). The chain is the m=1 special case.

DO NOT JUST FIT m_*. Tuning them to reproduce 2.15 buys a good table and costs the parameter-free claim, which is the point of the framework (cf. the dashboard header: 'lambda_A fit + naive Vol*tr_M both EXCISED').

PROPOSED ROUTE. B_gate and B_sym currently use DISJOINT information about the same nucleus: B_gate takes the SU(4) partition lambda's WEIGHT (scalar, ln 1/W_lambda) and discards its shape; B_sym takes a chain topology and ignores lambda entirely. The Young-diagram shape of lambda IS an occupancy geometry. Deriving the bond count from it would unify the two forms and stay parameter-free. Acceptance: the derived coordination reproduces the ~2.15 plateau and its A-dependence WITHOUT a fitted constant.

TWO DEFECTS FOUND ON THE WAY (independent of the above):
  * B_sym breaks for Z=0 — the (Z-1) coefficient goes negative, so a pure-neutron system gets a spurious -L_pp. It also hard-codes exactly one p-n bond regardless of composition.
  * L_nn (1.237) > L_pp (0.695) > L_pn (0.534) makes the p-n bond the WEAKEST, yet the deuteron binds and the dineutron does not. Nothing breaks today (the deuteron is the single-L_pn case and comes out exact), but the ordering should be understood before coordination multiplies these up.

Also: B_gate and B_vol both report 7.58 MeV for a FREE nucleon, where B_AME = 0 by definition. The 7.58 is a_V, the per-nucleon saturation constant, and deriving it is legitimate — but printing it in a binding column against zero is a category error, and makes err gate read 0.00 as though it were a perfect score. Suppress to em-dash at A=1.

## 2026-09-04 — demoted: coordination geometry is NOT the dominant gap

Measured against the additive law's residual over 2548 AME nuclides
(`qbeta_tower_log_z_and_roast_probe.py`): correlation with the surface shape
`A^(-1/3)` is **-0.178**, against **-0.804** for `(N-Z)^2/A^2`. And three
different edge sets — the canonical chain, the alternating chain, and the
renormalised all-pairs graph — land within 0.6 % of one another, so the bond
GRAPH is not where the error lives.

The bond COUNT is doing all the work that works (layout-free `(A-1)` scores
p5-p95 1.1809, better than any isospin-resolved variant), which is consistent
with `qou-zryq` — the inter-nucleon block encodes a count, not a coordination
graph.

(Corrected same day: I wrote "top lead is now `qou-ubsl`" — that bean is
**completed and closed**, the SU(4) reading structurally forbidden by the
`ℓ(λ) ≤ 2` row cap. The demotion of coordination geometry stands on its own
measurement; the re-promotion it pointed at does not.)
