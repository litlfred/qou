---
# qou-lyni
title: def:ew-interface-knot is a dangling reference cited by the convolution grid
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:16:52Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-hqo3
---

MEASURED 2026-09-04. tbl:knot-indexed-convolution-grid-table1-data row 'EW interface knot bowtie_K' cites 'def:ew-interface-knot' as its defining block, unlinked (plain code, not a markdown link - which is why no link-resolution check caught it). No .ts under content/ declares label 'def:ew-interface-knot': grep -rhoE 'label: *"def:[^"]*"' --include=*.ts . | grep -i interface returns exactly ONE label, def:canonical-braid-interface-composition.

SCOPE MISMATCH TOO, and it may be the real issue. The grid row says the output is 'element of H_6(q)' with 'EW braid in B_6 with interface I'. def:canonical-braid-interface-composition is stated over H_{3A}(q) with A = Z+N. Whether these are two different objects or one object at A=2 is NOT settled here - do not assume either. If they are one, the grid row should cite the existing label and say A=2; if two, the EW instance needs its own definition block.

WHY IT MATTERS RATHER THAN BEING A TYPO: bowtie_K carries the eightfold's isospin mechanism (conj:isospin-from-canonical-bowtie) and appears in 44 files. A reader following the grid to find out what it IS lands nowhere.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Label removed from 2 .ts files (Phase 7) but the grid row still names a non-existent 'EW interface-knot definition'; H₆ vs H_{3A} scope question unanswered.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check (owner-rulings.md on main 2ae54ab401, 2026-11-21): no superseded premise (photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ = 2 − h⁴, fitted values in proofs) is used by this bean's finding.
