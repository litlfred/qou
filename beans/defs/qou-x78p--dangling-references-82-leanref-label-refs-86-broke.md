---
# qou-x78p
title: 'Dangling references: 82 lean.ref / label refs, 86 broken relative links, 12 missing computation scripts, 4 missing citation keys'
status: todo
type: task
tags:
    - reorg-2026-10-04
    - orphan-census
created_at: 2026-10-04T15:31:23Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-hqo3
---

30 lean.refs resolve to nothing, 17 name a module, 26 namespace mismatches, 9 dangling labels; 23 links are just the wrong ../ depth; missing cite keys bokut1978, faddeev1996, manuscript, milnor1950; 4 prose macros exist only in main.tex (pp, bigbowtie, varTheta, yng).

Found by the orphaned-content census 2026-10-04 (inventory: 3,383 rows). Report only: no math or physics content is to be changed; this item links, builds or places existing content.

PROGRESS 2026-11-15 (branch claude/exposition-refs-render-2026-11-15): re-measured on main e67273779. Broken relative links in folio/quantum-observable-universe/**/*.md: 157. Fixed 133 whose target exists under a unique basename (wrong depth or pre-move dir). 24 remain whose target exists nowhere (missing probes/witnesses, 5 missing .lean siblings, ../braids-and-knots/ew-interface-knot.md). Unregistered cite keys in .ts/.md: milnor1950 (4), faddeev1996 (2), manuscript (2), bokut1978 (1). Anchor links to undefined labels: def:markov-trace, ssec:proton-radius, witness:y-lambda-jones-markov, witness:alpha-k-jones-markov-h3. Lean -- Ref: [manuscript] occurs 2074 times and is not a registered key (self-citation is leitner2026).

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Re-measured 2026-11-21: 22 broken relative links. 13 retargeted (unique-basename targets) on branch claude/paper-structure-drain-2026-11-21. 9 left whose target exists nowhere. milnor1950 now registered; faddeev1996/bokut1978 unused; 'manuscript' still in 7 block files.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check (owner-rulings.md on main 2ae54ab401, 2026-11-21): no superseded premise (photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ = 2 − h⁴, fitted values in proofs) is used by this bean's finding.
