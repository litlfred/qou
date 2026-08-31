# bounded_degree_coordination_genericity_probe — full output (2026-08-31)

Verbatim run of `computations/bounded_degree_coordination_genericity_probe.py`. Regenerate with:

    python3 -u computations/bounded_degree_coordination_genericity_probe.py

```
bounded_degree_coordination_genericity_probe
==============================================================================
q0 (50-digit proton pin) = 1.1099785827513808076
E_0 = m_e/(q0(q0-1))     = 4.18598136329 MeV
Derived per-bond energies eps = E_0*log(1/f_bond)  [MeV], NOT fitted:
    f_pp =   0.612688037146    eps_pp = 2.05070969238
    f_pn =   0.508229789377    eps_pn = 2.833162572
    f_nn =   0.403627738351    eps_nn = 3.79778293514

Bond-count-weighted eps at A=20, N=Z:
    complete graph (45 pp, 100 pn, 45 nn) -> 2.876307502 MeV
    chain          (9 pp, 1 pn, 9 nn) -> 2.919452433 MeV

THE INVERSION.  bounded_degree_saturates:  B/A = eps*k/2  =>  k = 2*(B/A)/eps
  This inverts an EMPIRICAL anchor for a parameter, i.e. it is a FIT.
  It is reported only as a plausibility check: is the implied k inside the
  physically possible window [2, 12] for a 3D packing?

                            eps choice                                 target   implied k  in window?
                         eps_pp (pure)                        B/A peak (62Ni)     8.57703         yes
                         eps_pp (pure)                        B/A peak (56Fe)     8.57284         yes
                         eps_pp (pure)    a_V (Bethe-Weizsacker volume coeff)     15.3605          NO
                         eps_pp (pure)                        a_V low bracket     15.1167          NO
                         eps_pp (pure)                       a_V high bracket     15.4093          NO
                         eps_pn (pure)                        B/A peak (62Ni)     6.20826         yes
                         eps_pn (pure)                        B/A peak (56Fe)     6.20522         yes
                         eps_pn (pure)    a_V (Bethe-Weizsacker volume coeff)     11.1183         yes
                         eps_pn (pure)                        a_V low bracket     10.9418         yes
                         eps_pn (pure)                       a_V high bracket     11.1536         yes
                         eps_nn (pure)                        B/A peak (62Ni)     4.63139         yes
                         eps_nn (pure)                        B/A peak (56Fe)     4.62912         yes
                         eps_nn (pure)    a_V (Bethe-Weizsacker volume coeff)     8.29431         yes
                         eps_nn (pure)                        a_V low bracket     8.16266         yes
                         eps_nn (pure)                       a_V high bracket     8.32064         yes
       complete-graph mean (A=20, N=Z)                        B/A peak (62Ni)     6.11513         yes
       complete-graph mean (A=20, N=Z)                        B/A peak (56Fe)     6.11214         yes
       complete-graph mean (A=20, N=Z)    a_V (Bethe-Weizsacker volume coeff)     10.9515         yes
       complete-graph mean (A=20, N=Z)                        a_V low bracket     10.7777         yes
       complete-graph mean (A=20, N=Z)                       a_V high bracket     10.9863         yes
                chain mean (A=20, N=Z)                        B/A peak (62Ni)     6.02476         yes
                chain mean (A=20, N=Z)                        B/A peak (56Fe)     6.02181         yes
                chain mean (A=20, N=Z)    a_V (Bethe-Weizsacker volume coeff)     10.7897         yes
                chain mean (A=20, N=Z)                        a_V low bracket     10.6184         yes
                chain mean (A=20, N=Z)                       a_V high bracket     10.8239         yes
          unweighted mean of the three                        B/A peak (62Ni)     6.07799         yes
          unweighted mean of the three                        B/A peak (56Fe)     6.07502         yes
          unweighted mean of the three    a_V (Bethe-Weizsacker volume coeff)      10.885         yes
          unweighted mean of the three                        a_V low bracket     10.7122         yes
          unweighted mean of the three                       a_V high bracket     10.9196         yes

GENERICITY — the actual measurement
------------------------------------------------------------------------------
  combinations tried                    : 30  (6 eps x 5 targets)
  implied k, full range                 : 4.62912 .. 15.4093
  landing inside the plausible window   : 27/30
  fraction of window [2,12] reachable : 73.709 %

  The two matches someone will notice, and what they are worth:
    eps_pn (pure) vs a_V (Bethe-Weizsacker volume coeff)
      k = 11.118317   vs fcc/hcp close packing k = 12   (7.347 % away)
    eps_pn (pure) vs B/A peak (62Ni)
      k = 6.2082565   vs simple-cubic / in-plane k = 6   (3.471 % away)

VERDICT
------------------------------------------------------------------------------
  The reachable k range covers 73.71 % of the plausible
  window, so landing near ANY particular lattice coordination number --
  12 for fcc/hcp, 6 for simple cubic, 8 for bcc -- is a property of
  WHICH eps and WHICH empirical target were chosen, not of the
  framework.  The inversion does not constrain k, and a 'k = 12,
  therefore close packing' reading is NUMEROLOGY.  Guard, not a result.

  What this does NOT say: bounded_degree_saturates is correct as stated,
  and nothing here argues against bounded coordination.  What is measured
  is only that INVERTING it for k is uninformative at the current inputs.

  What WOULD be informative: a k derived from the substrate -- from the
  braid word's own geometry or from a packing argument inside the
  framework -- and then COMPARED to the plateau.  That is derive-then-
  check; the above is check-then-derive, which is the forbidden direction.
```
