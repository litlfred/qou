---
# qou-181p
title: 'q-value-transition: .md defines a MASS difference, .lean + title define an ACTION difference — statement-integrity defect'
status: completed
type: task
priority: high
created_at: 2026-09-04T02:14:49Z
updated_at: 2026-09-04T02:53:42Z
---

Owner pick 2026-09-04 (option 3 of the qou-zmuu close-out). predicted-spectra/q-value-transition.md opens 'We define the Q-value ... directly from the categorical action' and then states 'Definition (mass difference, primary): Q = M(Z,N) - M(Z+1,N-1)' with M = Z m_p + N m_n + Z m_e - B(Z,N). The .lean (QOU.Archimedean.QValueTransition) defines QqValue.value := S_parent - S_daughter - S_electron - S_antineutrino, an ACTION difference, with a header saying 'NOT by classical energy conservation'. The .ts title is 'Q_q-Value as Categorical Action Difference'. Three faces, two definitions. Decide which is primary, make the other a derived remark or proposition, and re-run proof-statement-integrity + wall-side-statement on the block.



DONE 2026-09-04 on claude/lean-ref-resolution-qvalue-2026-09-04 (PR #6554). Root cause was deeper than .md-vs-.lean: TWO Lean carriers — sibling q-value-transition.lean (QqValue.value, ACTION difference, matches title) and library lean/QOU/Archimedean/QValueTransition.lean (structure QValueTransition, MASS difference, header claiming to be 'the manuscript definition') — and lean.ref named the library one while the sibling shadows it per s0a. Fix: .md primary = action difference, mass-difference kept as the archimedean realised form (conditional on conj:q-integer-mass-formula for B); lean.ref -> qou:QOU.Archimedean.QqValue.value; uses += def:categorical-action; defines q-value; library header rewritten to say it carries the FORM and nothing relates Q to QqValue.value. lean-direct exit 0 both files; validate clean; render battery clean (one list-hijack reflowed); qa-sweep 0 automated findings, 29 needs-agent NOT self-certified. generate-index.ts cannot run in a multi-paper folio (requirePaper() takes no arg) — index row hand-patched.
