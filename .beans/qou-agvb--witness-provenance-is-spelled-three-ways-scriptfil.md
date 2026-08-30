---
# qou-agvb
title: Witness provenance is spelled THREE ways (scriptFile / computation / producer) — 139 live witnesses carry none; every orphan count so far keyed on one field
status: todo
type: task
priority: normal
created_at: 2026-08-30T13:03:01Z
updated_at: 2026-08-30T13:03:27Z
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
