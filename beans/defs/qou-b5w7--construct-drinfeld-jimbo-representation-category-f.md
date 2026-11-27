---
# qou-b5w7
title: Construct Drinfeld-Jimbo representation category for QOU exists_instance
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T18:19:09Z
updated_at: 2026-11-27T22:05:00Z
parent: b9cj
---

## Round 78 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8272 (`be42fef123e1a988fe70707cab448f5763ca2cfc`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoAdjointTorsionAndSniadyGenusCovarianceBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/five_two_adjoint_torsion_and_sniady_genus_covariance_brick_probe.py` (`scriptCommitSha: f9d16753dbb36bbe177e31872e1864ef809ebf0e`) and `computations/probes/five-two-adjoint-torsion-and-sniady-genus-covariance-brick.witness.json` (`allPassed: true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8272, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-27 — constraints and reusable pieces (thread "Prove a non-trivial QOU instance exists")

- Owner ruling 2026-11-27: `QuantumObservableUniverse.exists_instance` stays `sorry` until this
  q-faithful witness exists; the ℤ/2 model (#9759) is not to close it.
- The snake identities in `FrobeniusHopfData` make `A` dualizable, so `A` must be a finite
  object of a rigid category: `A = O_q(SU(2))` (infinite rank, PBW basis #9731) cannot be the
  Frobenius object. Natural candidate: `A = End(V) = V ⊗ V*` with `Ad(A)` the traceless V₂.
- Reusable: `QOU/Core/FreeFinRigid.lean` (rigid category of free finite modules over any
  commutative ring) and the proof pattern of `QOU/Core/Z2Witness.lean` (Action category,
  linear-map reduction tactic `lin_reduce`).
- Open checks: `antipode_involutive` (S² = id) and `frobenius_symmetric` fail on full
  `O_q(SU(2))` at q ≠ ±1 (TN-1/TN-2 notes in CategoricalFoundations); verify they hold for
  `End(V)` with the braided anti-multiplicativity before building.
