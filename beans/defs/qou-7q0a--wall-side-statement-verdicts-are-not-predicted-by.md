---
# qou-7q0a
title: wall-side-statement verdicts are not predicted by banner presence — 5 live fails need re-adjudication, oldest 2026-07-07
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:42:32Z
updated_at: 2026-09-03T10:47:50Z
---

MEASURED 2026-09-03 on main d502ed06ce9 (+ this branch).

I added a rendered wall banner to nuclear-interactions/skein-binding-lagrangian.md
on the premise that wall-side-statement fails a block whose archimedean constructs
lack a rendered §7c banner (the block's banner was in authorNotes, which §4d says
does not render). THAT PREMISE IS NOT SUPPORTED. Measured over every block with
archimedean tokens in its .md AND a wall-side-statement verdict (n=17):

    verdict x md_banner:  pass/no-banner 11 | fail/no-banner 4
                          pass/banner     1 | fail/banner    1

ELEVEN blocks pass with no rendered banner, so a rendered banner is not what the
criterion keys on. And the single fail-with-banner is skein-binding-lagrangian
itself, AFTER my edit -- my block is now the only one failing while having the
thing I added to fix it.

Nor is it chapter-determined: mass-theory contains both passes and fails.

WHAT IS ACTUALLY TRUE. wall-side-statement is automated:false -- a per-block agent
judgement. qa-sweep marks agent criteria needs-agent but does NOT re-adjudicate an
existing entry, so a verdict persists until an agent replaces it. The five live
fails and their ages:

    knots-particles-confinement/magic-shell-coupling-kappa
    mass-theory/terminal-resolution
    mass-theory/neutron-proton-splitting
    nuclear-interactions/skein-binding-lagrangian      (2026-07-07, gemini-3.1-pro)
    nuclear-interactions/tritium-qvalue-symbolic

Each carries its own field_hash, and skein-binding's (4e4a3af31905) matches neither
the live .md nor the pre-edit one -- so it is provably stale, adjudicated against a
version of the text older than either.

WHAT IS OPEN. These five need an agent re-adjudication against their current text.
NOT by me for skein-binding: I edited that block, so clearing its fail is the one
verdict I should not be the one to write.

WHAT IS NOT WRONG. The banner addition itself stands on its own merits -- the block
now declares its wall side in the rendered narrative, matching the verbatim house
wording in mobius-energy.md / surreal-squeeze.md / mi-sw-abelianisation.md. It is
just not a fix for this criterion, and the PR must not claim it is.

2026-09-03 05:0x: owner asked for re-adjudication by dispatched agents. Dispatching 5 background agents, one per block, each adjudicating wall-side-statement ON THE MERITS against the CURRENT text. Agents READ + JUDGE only and return a verdict JSON to scratchpad; the parent applies all five to the sidecars on ONE stacked branch (claude/wall-side-readjudicate-2026-09-03, stacked on #6450 so skein-binding is judged against the post-banner text). The parent is the scribe, not the judge, for skein-binding. Prior worth stating and NOT assuming: all five verdicts come from the 2026-07-07 qa-agent-drain batch that qou-zkia measured at ~88% false positive.

2026-09-03 05:2x RESULT. All five dispatched agents returned `pass`, all five
`prior_verdict_was_correct: false`, all five regime = archimedean. The five entries
are APPENDED (never replaced) to criteria["wall-side-statement"] on branch
claude/wall-side-readjudicate-2026-09-03; qa-sweep --only wall-side-statement is
clean on all five (needs-agent 0).

Per-block ground (each agent's own words, compressed):
  kappa     -- chapter absent from the regime registry but split from
               particle-interactions (ARCHIMEDEAN_CHAPTERS); prior fail was judged
               against md 60ad7858c937, the pre-2026-08-10 conjecture version.
  terminal  -- predicted-spectra consolidation, .lean declares ground ring R with
               CODATA literals; exactly the §7c "CODATA -> R" row.
  npsplit   -- sec:mass-physical-face; 6 of 8 MeV-bearing mass-theory siblings pass.
  skein     -- banner NOT needed for the verdict; the pre-edit text d1e8e0dee29 would
               pass on the chapter-regime ground alone. Parent was scribe only.
  tritium   -- numeric q_0/MeV evaluation is in a separately headed section outside
               the Statement; same shape as the passing peer neutron-qvalue-symbolic.

THREE THINGS THE AGENTS SURFACED THAT ARE NOT CLOSED HERE:
  1. skein + tritium agents: three MORE templated fails in nuclear-interactions
     share the identical 2026-07-07T14:26:57 batch stamp and evidence string --
     frobenius-positivity-filter, gram-weighted-qvalue, parity-regime-selection.
     My "5 live fails" count was the wall-side-statement fails I had listed, and
     tritium measured 5 of 35 nuclear-interactions peers failing; the three above
     were not in my five. Same re-adjudication is owed. (See follow-up bean.)
  2. kappa agent: knots-particles-confinement and nuclear-interactions have NO row
     in _folio-chapter-profiles.qou.ts (both split from particle-interactions).
     Every agent had to infer the regime from lineage. Adding rows would make the
     next adjudication mechanical. That file is in folio-assistant, not qou.
  3. terminal agent: terminal-resolution.lean:8-21 still says "All four rows match
     CODATA to sub-keV precision", which the .ts caveat of 2026-08-11 retracts.
     Lean-docstring currency, not wall-side; not touched.

2026-09-03 10:5x: MERGED. #6450 -> main 0d79e178f82 (rebase), #6475 -> main c10071d7f73 (rebase). All five wall-side-statement entries now pass on main. Follow-ups live in qou-zmuu.
