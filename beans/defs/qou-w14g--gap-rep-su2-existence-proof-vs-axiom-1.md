---
# qou-w14g
title: 'GAP: prf:quantum-universe-exists says Rep(SU(2)) establishes existence; ex:quantum-universe-su2 says it satisfies only axioms 2-4'
status: todo
type: bug
priority: normal
tags:
    - part-1-foundations
    - quantum-universe-axioms
created_at: 2026-11-20T17:30:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-d4kh
---

Found by W14b while draining Ch 1 (PR #8577), not changed.

- `quantum-universes/quantum-universe-exists-proof.md`: "A richer witness is C = Rep(SU(2)) with A the regular representation. Both establish existence."
- `quantum-universes/quantum-universe-su2.md` (v): the braiding of Rep(SU(2)) is the flip, which is symmetric, and "a symmetric braiding induces none" of the well-ordering axiom 1 asks for; "the example verifies axioms 2–4 and is the symmetric point of a one-parameter family that verifies all four".

At most one is right. If (v) is right, the existence proof's second witness is not a witness and should be replaced by the deformed family (which needs Ch 2's parameter) or dropped; the trivial witness A = R (Omega^1 = 0) still stands, but whether its braiding satisfies axiom 1 should be checked by the same criterion. Content decision for the owner: which reading of axiom 1 is intended (does a symmetric braiding vacuously induce a well-founded ordering, or none at all).

Created by W14b (https://claude.ai/code/session_01VQDpPc68uEsyxoN3soj6Ws).

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Still live on main; owner decision (which reading of axiom 1).

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check (owner-rulings.md on main 2ae54ab401, 2026-11-21): no superseded premise (photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ = 2 − h⁴, fitted values in proofs) is used by this bean's finding.
