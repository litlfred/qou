---
# qou-o922
title: 'GAP: two lever1 producers flip muon->proton and drop q0Anchor on re-run (qou-po7i, measured)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:13:38Z
updated_at: 2026-08-22T20:14:16Z
---

Measured 2026-08-21 while fixing the wrap_legacy `computation` clobber (PR #5436).
A concrete, end-to-end instance of bean qou-po7i's argv[0] finding.

## The two producers

  computations/substrate/lever1_binding_core_characterization.py
  computations/substrate/lever1_binding_habiro_single_element_test.py

Neither is listed in computations/q0_anchor_manifest.json.

## What re-running them does

Both LOSE `q0Anchor` + `q0Value`. The second also flips its physics input:

    params.q0   1.10997859555733 (muon)  ->  1.10997858275138 (proton)

Mechanism, both halves of it:

1. `q_parameter` resolves the anchor from the argv[0] stem. No manifest entry
   => falls through to the PROTON default. The committed witness was written
   under MUON, so the input silently changes.
2. `WitnessBuilder.build()` stamps `q0Anchor` only when
   `q0_anchor_is_declared(script_path)` is true, which is False for an
   unlisted producer. So the label that would have made the flip visible is
   dropped in the SAME step.

That second half is what makes it dangerous: the pin changes and the audit
trail for the pin change disappears together. The anchor audit then reports
Q0_ANCHOR_MISSING -- "pre-backfill; not a failure" -- for a witness whose pin
just moved 11.5 ppb.

## Not fixed in #5436, deliberately

#5436 regenerates four other producers affected by the clobber; these two were
REVERTED rather than committed, because landing their regenerated witnesses
would commit a silent muon->proton flip inside a PR about a provenance key.

## Next step

Decide the intended pin for each, add a manifest entry under `ideal_muon` or
`physical_proton`, THEN re-run. Do not re-run first -- the run is what destroys
the evidence of which pin was intended.

Worth checking whether the pattern is wider: any producer that (a) is absent
from the manifest and (b) has a committed witness carrying a muon `q0Value` is
a candidate for the same silent flip on its next re-run. That intersection has
not been measured.


---

## MEASURED 2026-08-21 — it is 49, and my first number was wrong by 3.8x

`computations/audits/undeclared_muon_pin_flip_risk_audit.py` (2/2, ratcheted at
49, --strict verified to fire).

**49 witnesses / 49 distinct producers** assert `q0Anchor: muon` with the muon
`q0Value` while their producer is absent from `q0_anchor_manifest.json` — so
each would resolve to the PROTON default on re-run, and drop the label in the
same step. Bounded and drainable, not the sweep the ~2384 undeclared producers
implied.

**Correction to my own first pass.** I blob-searched the whole witness JSON for
the muon 14-char prefix and got 185, of which I reported 130 as carrying no
`q0Anchor` label. Both figures are artifacts: most hits are a muon value in a
DATA field (a cross-anchor comparison, a recorded reference), which is not a
pin claim. Keying on `q0Value` specifically gives 49, and the count of
witnesses carrying the muon `q0Value` with no label is **0**, not 130. Do not
quote 185 or 130.

**Not wired into precision-gates.sh** — red-on-arrival at 49, and a gate red on
arrival gets skipped, which is how a checker goes quiet. Wire it at 0.

**Drain order stays as recorded above:** manifest entry FIRST, then re-run. For
an unlisted producer the committed muon `q0Value` is the only surviving record
of intent, and the re-run is what destroys it.


## Drain feasibility, sampled 2026-08-21 — and a THIRD detector-blindness slip

Asked whether the intended pin is recoverable from source, so the drain can be
scoped. Answer: **about half, cheaply; the rest need per-producer work.**

    of the 49 at-risk producers
      q0 accessor in the file itself   18
      only via a ONE-HOP import         7      => 25 resolvable
      still unresolved at one hop      24

**The slip, recorded because it is the third today.** My first pass grepped
each producer for `q_muon_at|q_at\(|q_parameter.Q|...` and found ZERO signals in
5 of 8 sampled, which I was about to report as "intent is not recoverable".
Checking one concretely — `a_operator/cyclic_intertwiner_verify.py` — it reads

    q = aoa.q0_mp(dps)

i.e. through a module alias, a spelling my regex did not carry. The absence was
in the DETECTOR, not the producers. This is exactly the taxonomy AGENTS.md
already documents for convention-C detection (thirteen distinct blind
spellings, four found by detectors written to catch the previous blind spot),
and it is the same error as the 185-vs-49 over-count and the
`computation`-clobber "PROSE_LOST = 0" earlier in this session. In all three I
measured the container rather than the claim.

The 25/24 split above uses an accessor set discovered from the tree rather than
guessed, so treat it as a floor: further spellings would move producers from
`unresolved` into `resolvable`, never the other way.

**Sub-class worth separating before draining.** `compute_audit_scan` and
`derivation_chain_validator` sit in the unresolved set and are AUDITS — they may
not compute at a pin at all, in which case their `muon` label is wrong and the
right fix is `independent` (with a reason), not a manifest entry. Do not
mass-assign manifest entries; sort audits from computes first.


## The 49 are NOT homogeneous — and for part of them re-running is a FIX

Checked the audit-vs-compute sub-class concretely rather than by heuristic.

**`compute_audit_scan` carries a FALSE muon label.** AST-checked: **zero**
q0-ish identifiers used as code. Its only `q0` mention is inside a STRING
LITERAL — advice text ("numerical evalf at q0. Add `simplify=False`") emitted
by a static source scanner. Non-stdlib imports are `_path_bridge` and
`witness_base`, nothing else. It never computes with q0 in any form. Yet
`compute-audit-scan.witness.json` asserts

    q0Anchor: muon
    q0Value:  1.10997859555733471989...

That is a false claim of the strongest kind the vocabulary makes — it asserts
the producer computed at a specific pin. `derivation_chain_validator` is the
same shape but milder: it does `mpf` arithmetic, over AUTHORED digits read from
chain JSON (`mpf(str(target_value_raw))`), not over a substrate pin.

**Consequence, and it inverts the disposition for this subset.** For these
producers re-running does not damage anything — it DROPS a false `q0Anchor`,
which is a correction. The blanket rule recorded above ("declare the manifest
entry FIRST, then re-run") is right for the producers that genuinely compute at
the muon pin (the lever1 case) and WRONG here: adding a manifest entry would
promote a false claim into a declared one.

So the 49 splits at least three ways:

  (i)   genuinely computes at the muon pin, undeclared  -> real flip risk;
                                                           declare, then re-run
  (ii)  never computes with q0, carries a false muon label -> re-run to clear
                                                           it, or set
                                                           `independent` with a
                                                           reason
  (iii) unresolved -> needs the per-producer look, and per the note above
                      "unresolved" is a statement about my detector, not the
                      producer

**Do not drain this bean as one sweep.** Sort into (i)/(ii)/(iii) first. The
sort is the cheap gate and it changes the ACTION, not just the ordering.

Not yet measured: how many of the 49 fall in (ii). Two confirmed by hand.


## Class (ii) is at least 4 — and the sort turns out NOT to be automatable

AST-based (identifiers used as CODE, so a q0 mention inside a string literal or
docstring does not count — that is what made `compute_audit_scan` look
q0-using to a grep), file plus one hop into local imports:

    at-risk producers                          49
      q0 identifier used as code (self/1hop)   45
      NO q0 identifier as code -> class (ii)    4

    computations/audits/fitted_labelled_canonical_audit.py
    computations/compute_audit_scan.py
    computations/habiro/habiro_interpolate_cross_validator.py
    computations/qbeta/qbeta_fsc_g_pattern_comparison.py

So class (ii) is SMALL. It does not warrant separate corpus-wide treatment; it
is a four-item cleanup. That answers the question of whether the false-label
class needed its own arc: it does not.

**But 4 is a LOWER BOUND, and the reason matters.**
`derivation_chain_validator` has **NO** q0 identifier of its own — AST-checked,
`self: NONE`. It landed in the 45 purely because it IMPORTS a module that
contains a q0 accessor. Importing a module that mentions q0 is not using q0, so
the one-hop rule OVER-ATTRIBUTES. I had hand-read that producer as class (ii)
one turn earlier (it does `mpf` arithmetic over AUTHORED digits from chain
JSON, never over a pin) and the detector disagreed with the hand-read — the
detector is wrong here, not the hand-read.

**Consequence: the (i)/(ii)/(iii) sort cannot be automated.** The two available
rules fail in OPPOSITE directions —

  * file-local grep      UNDER-counts (misses `aoa.q0_mp(dps)`, a module alias)
  * one-hop AST          OVER-counts (an import is not a use)

— so neither can produce the sort, and a hybrid inherits both errors. This is
the fourth detector-calibration slip of the session and the first in the
over-inclusive direction; the earlier three all under-counted. The honest
conclusion is that the 49 need 49 reads, or at minimum 49 confirmations of a
machine proposal, exactly as the `library-find-duplicates` proposals are
adjudicated rather than trusted.

Budget it as hand work, not a sweep. The audit script remains the right
artifact: it holds the register and ratchets it, and makes no claim about which
class an entry is in.


## DRAIN STARTED 2026-08-22 — 49 -> 47 (PR #5457)

Two class-(ii) producers dispositioned `independent`:
`fitted_labelled_canonical_audit`, `compute_audit_scan`.

**The disposition is the OPPOSITE of this bean's blanket rule, and that is the
point.** "Declare the manifest entry FIRST, then re-run" is right for class (i);
for class (ii) a manifest entry would promote a FALSE claim into a declared one.
The honest label is `independent` + reason.

**Proved empirically, superseding the AST method.** Static "zero q0 identifiers
as code" is necessary but not sufficient — a module alias defeats it (that is
how `aoa.q0_mp(dps)` slipped past). The decisive test: run under BOTH anchors
and diff. For both producers the ONLY differing non-ephemeral leaves are
`q0Anchor` and `q0Value` themselves; every substantive field is byte-identical.
Use this test for the remaining 47, not the AST heuristic.

**A library bug was in the way, found by the first step.** `save()` carried the
old muon `q0Value` forward onto the new `independent` label — manufacturing the
exact Q0_FLIP contradiction the declaration exists to avoid. Corpus blast radius
0 today, but it would have fired on EVERY subsequent class-(ii) disposition.
Fixed in the same PR.

**Gap between the two audits, recorded.** Both these witnesses end in a suffix
`q0_anchor_consistency_audit` exempts (`-audit.`, `-scan.`), so its flip check
never ran on them — `Q0_FLIP` read 0 while two live contradictions sat on disk.
The risk register scans them; the anchor audit does not. Not reconciled here.

**Ratchet lowered 49 -> 47.** Baselines drain, never grow — a stale-high
baseline is slack the gate will not notice being taken back up. Re-verified it
still fires at 46.

## The three NOT dispositioned, each a different case

  derivation_chain_validator          EXITS 2 under the proton anchor — it DOES
                                      depend on the pin, indirectly. Not (ii).
  habiro_interpolate_cross_validator  byte-identical INCLUDING q0Anchor, so it
                                      is already declared. Different state.
  qbeta_fsc_g_pattern_comparison      witness not resolvable from its emit site.

## Remaining: 47

Still needs per-producer reads; the sort is not automatable (the two available
rules fail in opposite directions, recorded above). But the both-anchor diff
above is a much better per-producer TEST than anything tried so far — it decides
class (ii) membership definitively in one run, without reading the source.


## 2026-08-22 (cont.) — 47 -> 40, and the method I recorded above is WRONG

**RETRACT the both-anchor diff test recorded in the previous entry.** I called it
"the reusable part" and "definitive in one run". It is confounded and it nearly
landed eight false dispositions.

**Why.** The LABEL always tracks QOU_Q0_ANCHOR, because the builder reads the
env var. The PAYLOAD only tracks it if the producer reaches q0 by a route that
env var actually controls. So a "label-only" diff conflates

    (a) the producer does not depend on the pin       <- class (ii)
    (b) the producer does not respond to the ENV VAR  <- says nothing at all

Run over all 47 it returned 16 members. Eight of them changed SUBSTANTIVELY on a
plain re-run — alpha_q0 / alpha_eff_q0 / Q_N2_q0_MeV, z_q0, the Frobenius Gram
eigenvalues, z_markov. Physics. Those producers DO depend on the pin.

**THE CORRECT TEST:** run with NO env var — the default invocation, which is what
any future re-run does — and diff against the COMMITTED witness. Class (ii) iff
nothing but the label fields move. This compares the real before/after instead of
two artificial states, and it is what caught the confound.

Seven survive and are dispositioned `independent` (PR #5457):
chirality_topology_binding_probe, probe_he4_magic_baryeven_prune,
lambda_scale_substrate_probe, qbeta_c3_rung_structure_analysis,
qbeta_habiro_f_from_shape_collapse, qbeta_rung1_div25_framing_squared_test,
z2bn_tau_derivation_probe.

**Also retract:** lever1_binding_core_characterization is NOT class (ii) — its
bare re-run moves computationDetail and the upstream witness hashes. Its partner
lever1_binding_habiro_single_element_test remains a genuine flip. Still two
different cases, just not the two I assigned them.

Ratchet 47 -> 40, re-verified firing at 39.

## Running tally of method errors on this bean — five now

  1. blob-search over the witness JSON            over-counted 185 vs 49
  2. file-local grep for q0 identifiers            under-counted (module alias)
  3. one-hop AST                                   over-counted (import != use)
  4. AST "zero q0 identifiers as code"             necessary, not sufficient
  5. both-anchor env-var diff                      confounded (label vs payload)

Every one failed in a DIFFERENT direction, and each was caught only by measuring
the thing itself rather than a proxy for it. That is the standing lesson for the
remaining 40: the only trustworthy test touches the real committed state under
the real default invocation. Budget accordingly -- it is one re-run per producer,
not a static scan.


## 2026-08-22 (cont.) — the drain's CHEAP PHASE IS OVER at 40

Ran the corrected test (bare re-run, baseline from `git show HEAD:`) across all
40 remaining. Result:

    class (ii) label-only    1     <- and it is an AUDIT, freshness-confounded
    depends on the pin      19
    slow (>240s)             2
    unresolved              14     <- witness not resolvable from emit site
    error                    4

**Essentially no more cheap wins.** The 19 that depend are genuine: their diffs
land in `/data/proton_anchor/...` and `/data/muon_anchor/...` — producers that
compute at both anchors on purpose and whose payload really does vary.

**A SEVENTH confound, in the test I adopted as correct.** Bare-re-run-vs-committed
cannot separate "depends on the pin" from "depends on anything else that drifted
since the witness was committed". Corpus SCANNERS (compute_audit_scan,
q0_anchor_consistency_audit) enumerate tree state, so 200+ commits of main make
them differ for reasons that have nothing to do with q0. It errs CONSERVATIVE —
over-reporting `depends`, under-claiming class (ii) — which is the safe
direction, but it is not a verdict.

So both tests are confounded, in opposite directions:

    both-anchor env diff        isolates the anchor; blind when the producer
                                gets q0 by a route the env var cannot reach
    bare re-run vs committed    real before/after; blind to WHY it changed

Neither is sound alone, which is the measured backing for "not automatable".

## The 14 `unresolved` are a TOOLING gap, not producer defects

My AST heuristic looks for a `wrap_legacy`/`WitnessBuilder` call with a literal
first arg. These 14 build the name some other way. Resolving them needs the
emit-site mapping, and that is worth building before any further drain — it is
35 % of what remains and currently invisible to every sweep.

## Recommended next step, and it is NOT more sweeping

Stop trying to classify by re-running. Build the producer -> witness emit-site
map first (fixes the 14), then read the 19 `depends` individually to separate
"computes at the pin" (class i, needs a manifest entry) from "reads a muon
witness for its q0" (label is TRUE, remove from the register entirely). The
second category is invisible to both tests and may be a large share of the 19.
