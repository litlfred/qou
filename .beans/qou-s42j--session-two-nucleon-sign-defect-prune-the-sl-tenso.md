---
# qou-s42j
title: 'Session: two-nucleon sign defect — prune the (S,L) tensor-coupling route (qou-vbyi route 1)'
status: completed
type: milestone
priority: normal
created_at: 2026-09-03T08:39:48Z
updated_at: 2026-09-03T12:38:41Z
---

Branch: claude/two-nucleon-sign-defect-2026-09-03. Target: qou-vbyi route 1 (non-separable (S,L) tensor coupling) as a fix for the pp/nn SIGN defect. Formalize-first prune, two invariants: (A) the tensor operator S12(n) acts as the scalar 3(1-|n|^2) on the spin singlet — the singlet is an EIGENVECTOR of both sigma1.sigma2 (=-3) and (sigma1.n)(sigma2.n) (=-|n|^2), so no spin-space coupling of this form has an off-diagonal element out of S=0; pp/nn (pure S=0 by Pauli) are untouched. (B) 2x2 interlacing: any off-diagonal coupling t!=0 makes the lower eigenvalue STRICTLY below the uncoupled 3S1 level, so tensor mixing can only bind the (already 27.3% over-bound) deuteron harder. Corpus-grep clean (no prior statement of either). No sibling active on the sector.

Lean file written: QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean (8 theorems: 4 singlet-eigen over C, 4 interlacing over R). Exact probe landed + passing 13/13. Audit doc written. lean-direct verification in flight (lean-verifier); commit/PR gated on exit 0 + axiom-clean.

DONE (2026-09-03): PR #6488 open, non-draft. lean-direct exit 0; #print axioms on all 8 declarations = {propext, Classical.choice, Quot.sound}; probe 13/13; precision-gates: probe in no dirty list, NEW dirty witnesses 0; check-sidecars: no §7c flags. Route 1 of qou-vbyi pruned (scope-b). Awaiting owner merge. Memory: merge-coordinator TRAP corrected (all-REST close→reopen→merge route around the dead GraphQL draft toggle, 3/3).

## CLOSED 2026-09-03 — merged as PR #6488 (e47c388164)

Delivered: QOU.QBeta.TensorCouplingSinglet (8 sorry-free theorems, axiom-clean), exact companion probe (13/13), audit docs/audits/2026-09-03-tensor-coupling-cannot-unbind-singlet.md, qou-vbyi route 1 recorded closed as a sign-defect fix. The sign defect is now boxed from every interface-side direction (scalar, separable factor, non-separable spin-space coupling); survivors are all outside the interface value: the sigma^{-2k} stacked class (right sign, 6-9x magnitude), the binding law (qou-y0mc), or the pp/nn bond/carrier assignment. Recommendation (judgement): the carrier assignment is the least-worked survivor and the one this prune points at.
