---
# qou-agvb
title: Witness provenance is spelled THREE ways (scriptFile / computation / producer) — 139 live witnesses carry none; every orphan count so far keyed on one field
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T13:03:01Z
updated_at: 2026-10-04T15:14:26Z
parent: qou-5vkl
---

Found while cross-checking PR #6215 against sibling commit 6f39734ea3 (qou-bake), which landed on main minutes earlier and corrects ITS OWN orphan claim: 'The qou-tekx triage put these in a "producer not found" bucket on the strength of scriptFile: None. That read the WRONG FIELD -- the provenance was in `computation` all along.'

THAT CORRECTION IS ITSELF INCOMPLETE. There is a THIRD spelling, `producer`, which neither scriptFile nor computation catches. Measured on main 2026-08-30 over 2939 live witnesses (excluding _deprecated):

  neither computation nor scriptFile          145
  of those, carrying a top-level `producer`     6   <- ALL SIX name a .py that EXISTS
  genuinely carrying none of the three         139

So an orphan count keyed on any ONE field OVER-reports: it calls provenanced witnesses orphans. scriptFile alone was wrong (qou-bake's own finding); scriptFile+computation is still wrong by 6.

The six: neutrino-mass-volume-exclusion, charm-mass-tower, charm-composite-volume,
h4-markov-character-decomposition, mu3-target-robustness-audit,
qbeta-meridian-holonomy-anchor-swing.

CAUTION ON THE NUMBER 6. A first pass reported 10 by substring-matching the key
names anywhere in the JSON; only 6 have a TOP-LEVEL `producer` naming a real
script. Quote 6, and say the method.

MY OWN CLAIM SURVIVES THE CORRECTION, checked explicitly rather than assumed.
a4-interface-magnitude-one-scalar-gate.witness.json (PR #6215) has NO
`computation`, NO `producer`, NO `scriptFile`; there is no
docs/audits/scripts/ script matching it (the pattern qou-bake's five follow);
and its cited audit doc, which exists, names no script. It is a genuine orphan
and is a SIXTH instance of qou-bake's class, distinct from its five keystones.

NEXT: a single detector checking all three spellings, replacing the per-field
greps. This is entry N of the detector-blindness taxonomy
(docs/audits/2026-08-15-detector-blindness-taxonomy.md) -- same shape as the
convention-C sqrt-variable spelling and the sys.path[:0] miss: a detector that
keys on ONE way of writing a thing, in a corpus that writes it several ways.

NOT DONE HERE. #6215 fixes one witness at its producer; this bean is the class.


RESOLVED 2026-08-30. Detector: computations/audits/witness_producer_resolution_audit.py
(--selftest, 7 checks). Audit: docs/audits/2026-08-30-witness-producer-resolution.md.

THE ANSWER IS 19, and every prior count -- INCLUDING THIS BEAN'S OWN -- over-reported:

  scriptFile only (qou-tekx)                298   15.7x
  + computation (qou-bake's correction)     145    7.6x
  + producer (THIS BEAN, last turn)         139    7.3x   <- my published number
  value-based, 'cites a real .py'           233   12.3x
  + convention + producer-call (final)       19      --

TWO CORRECTIONS TO THIS BEAN'S OWN CLAIMS.

1. TITLE IS WRONG: 'THREE ways'. There are NINE candidate keys, FIVE live
   (scriptFile 2642, computation 2679, producer 64, source 51, scriptPath 8).
   witness_provenance_attribution_audit.py already carried a DIFFERENT three
   (scriptFile/script/scriptPath) -- so the union was five before I started and
   I had not grepped for the prior detector.

2. '139 live witnesses carry none' is an OVER-REPORT BY 7x. The real figure is
   19. And the framing 'an orphan count keyed on ONE field OVER-reports' was
   directionally right but useless in magnitude.

THE INTERESTING RESULT: my value-based method (233) was WORSE than the key-based
one it replaced (139) -- the opposite of what I predicted. 'Does the witness
CITE a real .py' is STRICTER than 'does a provenance key exist', so it flags
more. Strictness is not accuracy. The key-based count was accidentally closer
because the `computation` key is present on 91% of witnesses and a witness with one
usually does have a producer, for reasons unrelated to that field's contents
(it holds the witness ID, not a script -- it names a producer on only 46 of
2679, i.e. 1.7%).

TWO BUGS IN MY OWN DETECTOR, opposite directions, both now fixed and recorded:
 - ORPHAN over-reported: missed the '_probe' SUFFIX (gswz_52_symmetrization ->
   gswz_52_symmetrization_probe.py), and the mention index tokenised only
   HYPHENATED ids so every underscore-named witness was invisible. Most of a
   30-item list.
 - FOUND_BY_MENTION over-reported: 4he-binding-full-pipeline, whose own
   scriptFile says '(legacy -- no matching producer found)', was rescued by
   witness_provenance_audit.py -- an audit that READS it and writes its own
   witness. 'Mentions the id and writes something' is not a producer signature.
   Now requires WitnessBuilder("<id>") or writing <id>.witness.json.

ALL 19 VERIFIED INDIVIDUALLY, not sampled. Six had a similarly-named script and
each was checked by hand: canonical_mass_table_extended.py writes
canonical-mass-table-extended and mass-table-ppb, NOT -242ppb;
meson_spectrum_predictions.py writes meson-spectrum-predictions, NOT
meson-spectral-analysis; tau_hat_n_proton_realisation.py writes -realisation,
NOT -level-1-empty; forward_ref_classifier.py, hecke_core_symbolic.py and
whitehead_volume_search.py write no witness at all.

SCOPE: says a producer EXISTS, not that it REPRODUCES the witness -- that is
witness_provenance_audit.py, strictly stronger where it applies but blind to the
213 resolved here by convention or producer-call. Nothing rewritten; no
canonical spelling proposed (owner's call).


NOTE ON THIS BEAN'S OWN TEXT: two words above were eaten by shell backtick
expansion when this body was appended (`computation` and `_probe` ran as
commands). Repaired. The committed audit doc and commit message used a quoted
heredoc and were never affected.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

In-progress in Round 99 PR litlfred/qou#8444.
