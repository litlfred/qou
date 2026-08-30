---
# qou-e2cf
title: AME drain leaves ONE unrouted deuteron literal, 2.22452, in 6 tables — 2.1e-5 from the registry, a reconciliation decision not a sweep
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:26:28Z
updated_at: 2026-08-30T07:30:50Z
---


The TARGET class of the AME routing roadmap is drained: 109 literal sites in
53 files now read the registry, and `ame_registry_routing_triage.py` reports
TARGET 0/0 where it reported 109/53. Twenty-seven distinct spellings of four
binding energies collapsed onto four constants; the largest value move was
3.06e-6 relative (2.224573 -> 2.2245662).

WHAT THE DRAIN DELIBERATELY DID NOT TOUCH

One literal survives, and it is the same one every time: `2.22452` for the
deuteron. It is 2.08e-5 relative from AME_B_DEUTERON_MEV_VALIDATION
(2.2245662) -- four times the 5e-6 band the drain treats as "a rounding of
the canonical value". At that distance it is not a rounding, it is a
DIFFERENT NUMBER, and routing it would change a value on the strength of a
guess about where it came from.

It sits in six tables, in every case beside three siblings that DID route:

    delta_lambda_multi_atom_crosscheck.py:94       {'D': mpf('2.22452'), 'T': <reg>, '3He': <reg>, ...}
    rho_k_counit_defect_form.py:67                 same shape
    rho_k_counit_isotope_systematics.py:50         same shape
    deltalambda/..._extensivity_gap_synthesis_probe.py:56   {'D': 2.22452 (raw float64), 'T': <reg>, ...}
    deltalambda/..._binding_cross_isotope_probe.py:75       {"d": "2.22452", "t": <reg>, ...}
    probes/frobenius_gram_delta_lambda_probe.py:71          same shape

So the drain has left six tables that are three-quarters canonical and
one-quarter something else -- which is worse to read than six tables that
were uniformly stale, and is the reason this bean exists rather than a
comment in the diff.

Corpus-wide the literal appears in 55 .py files and 36 witnesses, so the
decision is bigger than these six sites.

THE DECISION TO MAKE (not made here -- it changes a value)
  a. `2.22452` is a stale evaluation (an older AME, or a 6-digit truncation)
     -> route all 55 files, re-run, accept the 2.1e-5 move.
  b. `2.22452` is pinned on purpose for a published comparison, the way
     option_e_canonical_reeb_v5.py pins its stale q0 with an ARCHIVAL note
     -> leave it and ADD that note, so the next drain does not re-ask.
Whoever answers this should say which, in the file, next to the literal.


---

## RESOLVED: 2.22452 is a mislabelled transcription error, not a pinned evaluation

Option (a). The evidence is one-sided and comes entirely from the repo's own
data, so no external reference is needed to settle it.

WHAT THE CORPUS CLAIMS

    deuteron_trefoil_qinvariant_closed_form_probe.py:81
        B_D = mp.mpf("2.22452")          # MeV, AME2020 deuteron binding
    option_e_kl_betti_contributive_deuteron.py:20
        AME 2020: B(D) = 2.22452 MeV.

WHAT THE VENDORED AME2020 SAYS (qou-mass/src/qou_mass/data/ame2020.json)

    Z=1 A=2   binding_energy_per_A_keV      1112.2831  +/- 0.0002
              binding_energy_total_keV      2224.5662
    registry  1112.2831 x 2 / 1000       =  2.2245662 MeV

    corpus literal                           2.2245200 MeV
    difference                               0.0462 keV  =  115 sigma
                                             on the AME quoted uncertainty

So the literal names the same source the registry reads, and disagrees with it
by 115 sigma. It is not a pin to a different evaluation -- it is asserted to be
this one.

NO DERIVATION ROUTE PRODUCES IT

    m_p + m_n - m_d      (CODATA nuclear)   2.2245661
    M(1H) + m_n - M(2H)  (atomic)           2.2245663
    AME2020 total_keV / 1000                2.2245662
    corpus literal                          2.2245200

THE ROUNDING PATTERN IN ITS OWN TABLE

    {"d": "2.22452", "t": "8.48180", "3he": "7.71804", "4he": "28.29567"}

    t     8.4817962  -> 8.48180   correct 5-dp rounding
    3He   7.7180413  -> 7.71804   correct
    4He  28.2956624  -> 28.29566 expected, written 28.29567  (off by 1 ulp)
    D     2.2245662  -> 2.22457  expected, written 2.22452   (off by 5)

Two of four round correctly, one slips by one in the last place, and the
deuteron is off by five. That is a typo that then propagated by copy-paste, not
a considered choice.

## What was routed, and what was not

Of the 35 files where 2.22452 appears as CODE (not prose):

    21  TARGET  -> ROUTED. Permitted by the roadmap's own role gate.
    14  REVIEW  -> left alone. Their role is unknown; the value question is
                   settled but the routing question is not, and REVIEW is
                   exactly the class that needs reading first.
     0  INPUT   -> nothing forbidden was touched.

The drainer's 5e-6 band exists to stop exactly this kind of routing while
provenance is unestablished, so it was not widened globally: QOU_DRAIN_BAND
raises it for this one settled literal and defaults back to 5e-6.

The six "'D' is NOT routed" notes added when the answer was unknown are removed
where D is now routed. The prose guard flagged all six removals, which is the
guard working -- they are deliberate, and they are the only prose the drain
touched.

## The move is 7x anything in round 1, and that matters for verification

    round-1 ledger max   3.06e-6   (2.224573 -> 2.2245662, a rounding)
    deuteron             2.08e-5   (2.22452  -> 2.2245662, a typo)

Confirmed on deltalambda_binding_cross_isotope, whose deuteron ratio moved

    0.3314003377150088  ->  0.3313934551616367     = 2.077e-5 relative

against a predicted 2.077e-5. The witness carries it; the printed table reports
4 decimals and is unchanged.

Through a near-cancellation this amplifies: a residual reported at 0.1% can move
by ~2% OF ITSELF. Three probes report residuals that tight and all three were
routed — deuteron_binding_plancherel_channel,
deltalambda/deuteron_binding_frame_independent_probe, and
deltalambda_binding_cross_isotope. Their numbers change, correctly, and the
verification bar was widened from 3.06e-4 to 2.08e-3 to match rather than
flagging every deuteron leaf as unexplained.
