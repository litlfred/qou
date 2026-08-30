---
# qou-bzy0
title: Three blocks in knots-particles-confinement are unregistered and never render
status: completed
type: task
created_at: 2026-08-24T21:01:32Z
updated_at: 2026-08-24T21:01:32Z
---

Found while closing qou-1ngr, 2026-08-24.

`content/quantum-observable-universe/knots-particles-confinement/knots-particles-confinement.ts` is the gate: a block whose slug is not in some section's `blocks[]` does not render, and its label does not resolve — any other block that links it fails validation with "Unresolved uses".

Sweep of the directory (~200 blocks) found exactly two stragglers, both committed and both complete:

  pion-mass-hyperbolic-threshold   (rem:pion-mass-hyperbolic-threshold)
  antiquark-channel-ledger         (rem:antiquark-channel-ledger, commit c8f1d436098)

Confirmed the hard way: adding `rem:antiquark-channel-ledger` to a new block's uses[] turned validate from "Valid — 26 issues" into "Invalid — 28", one of them an error. The reference was dropped instead, so rem:gluon-stabiliser-ledger states the volume contrast without linking the sibling remark that makes it.

Not just a registration edit — it needs an ordering decision. `antiquark-channel-ledger.ts` has `uses: ["rem:pion-mass-hyperbolic-threshold"]`, and the natural homes are sec:nucleon-derivation (it interprets def:derived-atom, section 2) for the ledger and the meson material (section 12) for the pion remark. Registering them in those spots makes the ledger point forward, which detangler-no-forward-ref will flag. Decide the placement, register both, then restore the cross-link from rem:gluon-stabiliser-ledger.

(The third unregistered slug is gluon-stabiliser-ledger itself, registered as part of qou-1ngr.)


## Resolved 2026-08-24 — the detangler picked the order, and it picked against the obvious answer

The bean framed this as "decide the placement", expecting a taste call between
`sec:nucleon-derivation` (the ledger `interprets: def:derived-atom`) and the
meson material. Measured instead, against the same forward-ref metric
`detangler-no-forward-ref` uses: same-chapter `uses[]` + `interprets` edges
that point at a block appearing later.

Scored every insertion point for both blocks jointly (the ledger `uses` the
pion remark, so they cannot be placed independently):

    chapter as authored, both unregistered ........... 10 forward refs
    best achievable with both registered ............. 10   (6 tied placements)
    the bean's feared placement (ledger §2, pion §12) . 12

So **both blocks register for free**, and the feared split costs exactly the
two edges the bean predicted — `rem:antiquark-channel-ledger ->
def:categorical-meson` and `-> rem:pion-mass-hyperbolic-threshold`.

All six zero-cost placements put **both** blocks in `sec:categorical-hadrons`.
Among the six, exactly one does not split the `meson-scale-independence`
statement / calibration / proof triple, so that is the one taken:

    ... meson-scale-independence-proof
        pion-mass-hyperbolic-threshold
        antiquark-channel-ledger

The bean's instinct that the ledger belongs in §2 was reasonable and wrong.
`interprets` is a dependency, not a location: it says what the block reads
against, and a dependency pointing backward across ten sections is exactly
what it should do.

### The cross-link, restored without laundering

`rem:gluon-stabiliser-ledger` states the volume contrast at line 11 and the
link was dropped when the ledger landed. Restored as a **`.md` link only**, not
a `uses[]` entry. The reason is in `checkForeshadowsPointForward`'s docstring:
moving a genuine prerequisite into `foreshadows[]` to clear a red is
laundering. This is the other case — the gluon ledger is complete without the
antiquark ledger, and points forward at where the contrast gets worked out.
`deriveForeshadows` classifies an `.md` ref to a later block as a derived
foreshadow, and `checkDetanglerNoForwardRef` reads `usesGraph` only, so the
link costs nothing and nothing was moved to make it cost nothing.

### Second finding: the gluon ledger's own placement, moved

Not part of this bean, found by running the same scan on it. In §2 it emitted
two forward refs (`-> rem:ilp-solution-count-unwrap` pos 144,
`-> rem:categorical-proton-properties` pos 158). Scanned: §12 clears both,
chapter total **10 -> 8**.

Three things decided it over leaving a sibling's fresh placement alone:

1. **No §2 block references it.** Its only two referrers,
   `categorical-proton-properties` and `categorical-neutron-properties`, are
   both in §12. It was holding no thread where it sat.
2. Both blocks it `uses` are in §12.
3. Ran **all nine** detangler criteria before and after on the five affected
   blocks. Nothing new appears. `section-band`, `topic-coherence`,
   `no-dependency-cycle` and `archimedean-wall` pass either way, and
   `categorical-proton-properties`'s lone `block-tanglement` warn
   (`-> conj:borromean-quark`, cross-chapter) is identical in both layouts —
   verified by restoring the original manifest and re-measuring rather than
   assuming.

Recorded in the manifest at both the old and the new site, with the reason and
an explicit "revert if the editorial call outweighs the measurement". It
overrides a sibling agent's same-day decision on one signal (`interprets`)
using several, so it should be easy to undo if the owner disagrees.

### Residual, not fixed

Four cross-chapter `block-tanglement` warns survive, all inherent to what the
blocks depend on rather than to where they sit: the gluon ledger to
`nuclear-interactions` and `predicted-spectra` (3), the antiquark ledger to
`mass-theory` (1). No within-chapter ordering can reach them.
