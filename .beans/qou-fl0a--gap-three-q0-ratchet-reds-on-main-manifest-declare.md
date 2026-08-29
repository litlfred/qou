---
# qou-fl0a
title: 'GAP: three q0-ratchet REDs on main — manifest declared, WitnessBuilder has no script path, declaration inert'
status: todo
type: task
priority: normal
created_at: 2026-08-29T18:04:28Z
updated_at: 2026-08-29T18:05:01Z
---

Found while running `/prepare-merge` on PR #6026. **Inherited from `main`, not
introduced by that branch** — established rigorously, see Evidence.

## The RED

`computations/audits/q0_anchor_ratchet.py --strict` exits 1 with `NEW (not in
baseline): 3`:

  + computations/audits/mpmath-version-staleness.witness.json
  + computations/qbeta/qbeta-nl84-provenance.witness.json
  + computations/qbeta/qbeta-primitive-basis-overcomplete.witness.json

## The cause — the SAME trap for the third time today

All three stems ARE declared in `computations/q0_anchor_manifest.json`
(grep count 1 each, identical on `main` and on the branch). The declaration is
**inert**, because all three construct their builder with a name and no script
path:

    w = WitnessBuilder("mpmath-version-staleness", engine="mpmath")
    w = WitnessBuilder("qbeta-primitive-basis-overcomplete", engine="sympy")

`q_parameter` resolves the anchor by MANIFEST STEM, and the stem comes from the
script path. No script path, no lookup, no stamp — whatever the manifest says.

This is the third instance in one session:
  1. `habiro_interpolation_wlambda` — found by re-running it and watching it
     ignore both the manifest AND `resolve_q0_anchor`, which agreed with each
     other and with nothing that reached the file. Fixed at the producer.
  2. `aK_via_lp_dual_hecke_basis` — a hardcoded `{"q0Anchor": "muon"}` literal
     over a proton value; fixed by #6017 as a LABEL change (re-running it at
     the muon pin, which is what a naive flip-drain does, would have moved real
     numbers to satisfy an error).
  3. these three.

The ratchet's own output already warns about it — *"only takes effect if the
producer uses WitnessBuilder — a declaration on a hand-rolled json.dump producer
is INERT"* — but that wording names the WRONG condition. All three of these DO
use `WitnessBuilder`. The discriminator is not builder-vs-json.dump, it is
**whether the builder was given a script path**. Worth correcting in the
ratchet's message, because as written it clears exactly the files that fail.

## Proposed patch (not applied — would widen #6026)

Per producer, either:
  * pass the script path to `WitnessBuilder` so the manifest stem resolves; or
  * declare at the producer, `w.save({'q0Anchor': ..., 'q0AnchorReason': ...})`,
    which is what the corpus does for `independent` / `comparison`.

For these three the second is likely right — `mpmath-version-staleness` is an
environment audit and `qbeta-nl84-provenance` is provenance bookkeeping;
neither plausibly evaluates at a substrate pin. `qbeta-primitive-basis-overcomplete`
needs checking: PR #5958 declared it `ambiguous` in the manifest, which is a
different claim from `independent` and would not be satisfied by a producer-side
`independent`.

## Evidence that it is not #6026's

  witness blobs   all three byte-identical to origin/main (git rev-parse equal)
  manifest        identical to origin/main
  ratchet baseline  q0-anchor-missing-baseline.json identical to origin/main
  PR diff         5 files, all under computations/deltalambda/ — none of the three

Every input to the gate is identical to main's, so the gate result is main's.
A worktree check against a pristine `origin/main` was attempted and aborted:
the container hit `No space left on device` (719M free). The blob-identity
argument above is stronger anyway — it does not depend on reproducing a run.
