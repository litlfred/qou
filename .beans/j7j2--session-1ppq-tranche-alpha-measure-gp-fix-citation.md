---
# j7j2
title: 'Session: 1ppQ tranche — α_EM 1/(πb₁) measure scoping + GP kernel bug fix (qou-b2ie) + van der Veen citation check'
status: completed
type: milestone
created_at: 2026-07-17T14:45:00Z
updated_at: 2026-07-17T14:45:00Z
---

Owner pick "1 2 3" on the 2026-07-17 1ppQ re-evaluation:
1. α_EM per-loop measure 1/(πb₁) — scoping tranche (the single wall per
   2026-07-14-alpha-em-2loop-derivability-map.md; Schwinger tier demoted same day).
2. L1 leg → collapsed to the GP-kernel-bug fix + revalidation (bean qou-b2ie);
   L1 itself complete incl. ⁴He (2026-07-13-l1-4he-certification-complete.md).
3. Verify van der Veen Whitehead-chain volume-conjecture citation — DONE 2026-07-17:
   arXiv:math/0611181 confirmed (Acta Math. Vietnam. 33(3) 2008; family includes
   Borromean rings). Ledger row binding-scale-is-hyperbolic-volume.md was already
   current (web-verified 2026-07-13) — independent confirmation, zero diff.

Branch: claude/h4-exponents-value-screen-96501m

## Landed 2026-07-17
- Item 1 (alpha_EM measure): sibling PR #3834 merged onto main — zeta_{Delta1}(0)=-b1 area-free (the bare-b1 source). Residual wall (pi + reciprocal 1/(pi*b1)) OPEN, active swarm three-front attack. Deferred to avoid duplication.
- Item 2 (GP bug): guard landed PR #3812 — trivial-rep q^writhe cross-check + panic-on-disagreement; 16/16 rust tests green. Full GP cuspidal-move reduction stays open (bean qou-b2ie).
- Item 3 (citation): DONE, van der Veen arXiv:math/0611181 confirmed, zero diff.
