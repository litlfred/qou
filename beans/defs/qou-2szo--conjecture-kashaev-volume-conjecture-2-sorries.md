---
# qou-2szo
title: 'Conjecture: kashaev_volume_conjecture (2 sorries)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:49:55Z
updated_at: 2026-11-22T21:33:00Z
parent: qou-n4nr
---

kashaev-volume-conjecture.lean: 2 conjectural sorries about calibration algebraic mass. Genuine conjectures.

- **Round 91 (`https://github.com/litlfred/qou/pull/8413`, head `1d95d75db1b41a96e3b4987d5771f9fd945187c9`)**: Formalized theorem + 80-dps witness (`status: in-progress`).

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change. `mass-theory/kashaev-volume-conjecture.lean` carries the conjecture as classes (`VolumeConjecture`, `PieceVolumeConjecture`) plus a `sorry` value in `pieceVolume`; genuine conjectures. The latest note above points at batch PR #8413, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: RESCOPE.** RESCOPE. The carrier `mass-theory/kashaev-volume-conjecture.lean` holds the Kashaev volume conjecture as classes (pure mathematics: APPLIES, and it stays open). But the bean's framing "calibration algebraic mass" and the file's line ~212 note (Catalan's constant "entering the proton mass formula") belong to the absolute-mass reading excised 2026-08-11 (qou-exam) and to the Vol(𝓑₃)·ρ form that AGENTS.md calls non-canonical (2026-06-24). Corrected scope: the volume conjecture as a mathematical statement; drop the mass framing (a comment edit that needs the owner, since it is not a precision fix).
