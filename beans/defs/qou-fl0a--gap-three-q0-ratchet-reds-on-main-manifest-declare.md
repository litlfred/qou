---
# qou-fl0a
title: 'GAP: three q0-ratchet REDs on main — manifest declared, WitnessBuilder has no script path, declaration inert'
status: in-progress
pr: 8307
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T18:04:28Z
updated_at: 2026-11-17T10:37:00Z
parent: qou-5vkl
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


---

## 🛑 CORRECTION — my own diagnosis above is WRONG, retract it

Everything above the line stating the cause as *"WitnessBuilder with no script
path"* is **retracted**. I read `WitnessBuilder(name, engine=...)`, saw no path
argument, and concluded the manifest lookup never runs. It does:
`WitnessBuilder.__init__` **resolves the caller frame** when no path is passed —
its own comment says *"Resolve caller frame ONLY when script path not explicitly
provided"*. All three producers have a script path and their stems resolve.

Measured, not reasoned: `resolve_q0_anchor()` on all three returns
`'ambiguous'`, so the lookup demonstrably works.

## The ACTUAL cause

All three are declared under **`ambiguous`** in the manifest (PR #5958's
declarations). And `WitnessBuilder.build()` writes the stamp only here:

    if _a in ("muon", "proton"):
        witness["q0Anchor"] = _a

`ambiguous` is not in that tuple. The anchor resolves **correctly** and is then
**discarded**. So a manifest `ambiguous` entry can never produce a stamp, and
the witness stays in `Q0_ANCHOR_MISSING` forever while the manifest reads as
handled.

This is worse than the trap I mis-diagnosed, because the ratchet's own docstring
lists `ambiguous` as one of THREE honest answers — *"reads q0 but the pin is
genuinely undetermined --> 'ambiguous' with a q0AnchorReason"* — so the gate
documents an answer its own writer refuses to record.

## Blast radius, measured 2026-08-29

    producers declared ambiguous : 19
      witnesses stamped          : 10
      witnesses UNSTAMPED        :  9

And the decisive split: of the 10 stamped, the two carrying `ambiguous`
(`mu-p-pin-sensitivity-map`, `q0-consistency-audit`) declare it AT THE PRODUCER.
The rest are `comparison`/`independent` (producer-declared) or `proton`.
**Every `ambiguous` stamp in the corpus came from the producer; none came from
the manifest.**

The other 6 unstamped: mass-from-q-symbolic, tau-dictionary-hauptmodul-validator,
tau-dictionary-fricke-spin-probe, qbeta-ck-basis-constrained-pslq,
qbeta-ck-qholonomic-recurrence-test, qbeta-habiro-integrality-kill-test.

## What was done, and what was deliberately NOT

DONE: corrected the ratchet's own warning, which named the wrong condition
("a declaration on a hand-rolled json.dump producer is INERT" — all three of
these DO use WitnessBuilder). It now names both inert paths and cites the
measurement. That warning is what sent me down the wrong route, so fixing it is
the higher-value half.

NOT DONE, deliberately — this is a DESIGN CALL for the owner, not a drive-by:

  (a) add "ambiguous" to build()'s whitelist. Fixes all 9 at once. But a
      manifest entry carries no `q0AnchorReason`, and the ratchet requires one
      for `ambiguous` — so this writes a stamp weaker than the documented
      contract.
  (b) declare at each of the 9 producers with a reason. Matches the documented
      contract exactly. Costs 9 producer edits and 9 re-runs.
  (c) treat manifest-`ambiguous` as a category error and remove the class — the
      manifest's job is muon/proton routing, and `ambiguous`/`independent`/
      `comparison` are producer-side vocabulary. Sharpest reading; largest
      blast radius.

I lean (b) for these 9 plus (c) as the follow-up, but it touches shared infra
that many producers depend on and the owner should pick.

## Method note

Two wrong diagnoses in one bean, both from reading code instead of running it.
The corpus's own `q0_anchor_missing_cause_partition.py` would have said
`DECLARED_STALE` — which is ALSO wrong for these, since a re-run does not fix
them (tested: re-ran `mpmath_version_staleness_probe`, witness came back with
`q0Anchor` still absent). Three classifications, three wrong. The one that held
was calling `resolve_q0_anchor()` and reading `build()`'s actual branch.


---

## The five are DETERMINED — 4 comparison, 1 proton, and NO straddles

I said each of the five genuinely-two-pin producers needed a per-file ruling:
deliberate cross-anchor probe (`comparison`) or accidental straddle (a DEFECT).
Read them. The answer is settled and there is no defect among them.

**`comparison` (4)** — each evaluates at BOTH pins on purpose, in its own code:

  tau_dictionary_hauptmodul_validator  `res = {"muon-pin": gate(fmap(q0_mu)),
                                        "proton-pin": gate(fmap(q0_p))}` (:242),
                                       and asserts "q0-pin-independent (asserted
                                       across muon/proton pins)" (:277).
  tau_dictionary_fricke_spin_probe     `for pin, q0 in (("muon", q0_mu),
                                        ("proton", q0_p))` (:222); already
                                       records `q0_pins` as data (:507).
  qbeta_ck_qholonomic_recurrence_test  `"muon": extract_empirical_ladder(Q0_MUON)`
                                       (:328) — a real evaluation at the muon pin,
                                       not a stored readout.
  qbeta_habiro_integrality_kill_test   "Anchors (both pins of the ONE substrate
                                       modulus)" (:105); computes
                                       |c_3(proton) - c_3(muon)| (:59).

**`proton` (1) — and this is the one that would have been mislabelled:**

  qbeta_ck_basis_constrained_pslq      has NO Q0_MUON, no q0_mu, no pin loop. What
                                       it has is C3_EMP_MUON_HOPF, a c_3 readout
                                       explicitly marked SUPERSEDED (pre-#1422) and
                                       "retained ... spread only", plus
                                       PIN_REL_MUON = 22e-9, a PRECISION FIGURE.
                                       It computes at proton and compares against
                                       STORED NUMBERS. That is one anchor, not two.

METHOD NOTE. Grepping for "muon" in the file would have put all five in
`comparison`. The discriminator is whether the muon value is EVALUATED AT or
merely MENTIONED — a superseded stored readout and a ppb precision figure both
contain the word and neither is a pin. Same shape as
qbeta_primitive_basis_overcomplete, which computes at one pin and mentions the
other. Check the use, not the token.

## Implementation, not yet done

All five currently emit no q0Anchor, no q0Values, no q0Value. Each runs in well
under a second (hauptmodul measured 0.77s), so cost is trivial. The four
`comparison` ones need `q0_comparison(muon=..., proton=..., reason=...)` passed to
save() — and note its contract: pass the values the producer ACTUALLY COMPUTED
WITH, not the canonical constants, so the audit's per-leg re-check stays a real
test rather than a tautology. The fifth moves manifest ambiguous ->
physical_proton.

That would take `ambiguous` 16 -> 11. Left as its own change rather than widened
into #6062, whose body states these five are excluded.


## Round 55 Update (2026-11-17, PR #8307)

Stamped `q0_comparison` on `computations/probes/tau_dictionary_fricke_spin_probe.py` and `computations/probes/qbeta_habiro_integrality_kill_test.py`, drained raw float64 assertion/print arguments to `mpf`/`mp.nstr`, and regenerated both witnesses with `q0Anchor: "comparison"` and `0` raw float64 numbers (PR #8307, commit `cf8ca11962518083f27bc0a2ce60447359b28381`).
