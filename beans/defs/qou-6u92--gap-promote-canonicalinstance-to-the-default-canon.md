---
# qou-6u92
title: 'GAP: promote canonicalInstance to the default CanonicalMarkovWeightsH3 instance?'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:13:14Z
updated_at: 2026-09-03T08:45:24Z
---

## DONE 2026-09-03 — promoted, and PAIRED with demoting explicitInstance

Owner approved ("2y", 2026-09-03). Done as a PAIR, which is the part worth
recording: promoting alone would have left TWO global instances of one class,
where resolution silently takes the later declaration and nothing in the source
says so. So `canonicalInstance` becomes the `instance` and `explicitInstance`
becomes a `def`. With exactly one instance, what a bare
`delta_tau_M_canonical q` means is STATED rather than inferred.

`explicitInstance` is NOT weakened: it remains a first-class inhabitant, every
use of it is unchanged (they all name it with `@`, and `is_inhabited` names it
too), and it is simply no longer a candidate for IMPLICIT resolution.

MACHINE-GUARDED, not asserted. `delta_tau_M_canonical_resolves_to_canonical`
is rfl-provable only because resolution picks the canonical weights, so a
future second instance -- or promoting explicitInstance back -- would stop it
typechecking rather than silently changing what every bare use means.
VERIFIED TO HAVE TEETH: the same statement written against explicitInstance
produces 2 errors and does not typecheck.

BLAST RADIUS MEASURED, which is what I said in qou-dwf4 I could not do.
The claim there was that a per-file lean-direct check "cannot verify" it. That
was too pessimistic: the class is mentioned in exactly FIVE files, so the check
is bounded, not unbounded. All five were baselined green BEFORE the change and
re-run green after:

    QBetaCanonicalMarkovWeightsInstance.lean
    QBetaPerBlockChiClosedForms.lean
    QOU/QBeta/DecayLadderConventionDPositivity.lean
    mass-endomorphism/qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.lean
    mass-endomorphism/qbeta-per-block-chi-closed-forms.lean

Taking the baseline first is what makes the "after" result mean anything.

Also updated the .md note that said the promotion was "left as an explicit
follow-up" -- stale the moment this landed.



Landed on main as a8307f0775 via #6487 (REST landing of #6467; GraphQL un-draft rate-limited).
