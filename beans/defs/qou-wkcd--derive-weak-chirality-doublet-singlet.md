---
# qou-wkcd
title: 'Derive weak chirality (doublet L vs singlet R): |q|>1, quaternion sides, literature'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
blocking:
    - qou-hlx7
created_at: 2026-11-15T13:00:00Z
updated_at: 2026-11-15T13:00:00Z
---

Owner question (relayed by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn, tracker #7735):
"L vs R on singlet vs doublets should be derivable somehow / related? anything in the lit?"
and "does it depend on |q| > 1 vs |q| < 1, or is it derivable from that? Is that the same as
the convention of which crossing carries q in the skein weighting?"

Session: https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7
Branch: claude/weak-chirality-doublet-singlet-2026-11-15

Three routes, each to a derivation or a scoped negative:
1. |q|>1: does the observable regime |q0|>1 select the L line? Is q0>1 forced?
2. Quaternions: left vs right multiplication (Sp(1)_L x Sp(1)_R) as the one-sided source.
3. Literature: Connes-Chamseddine, LR-symmetric / Pati-Salam, SO(10), Furey,
   Bilson-Thompson / Gresnigt, Finkelstein, the Ozma problem.

Starts from #7844 (OneSidedWeakVertex.lean), #7836 (HelicityCommonSource.lean),
#7825 (PolarizationActionHecke / ChiralityPolarizationHopf / PolarizationRealStructure).

## 2026-11-15 result (PR #7855, draft; Lean verified at 6e1e536a9, lean-direct exit 0, sorry-free)

- Route 1: a letter fixes only h; the root relabel q ↦ −q⁻¹ swaps lines and W_L ↔ W_R
  (WeakChiralityRootLabel.lean). "Which crossing carries q" = "which root is q" = L/R.
  Per-letter modulus labelling flips under flavour (scope b, conditional on #7836).
  q0 > 1 is declared, not derived (q-zero-complex-extension.md:11; solvers seed it).
- Owner ruling 2026-11-15: leftLine := eigenline where the positive generator σ has
  |eigenvalue| > 1 (LeftLineDefinition.lean). Derived: label-independent, flavour-blind,
  universal; weakVertex flips flavour on the left line only; = P+ iff |q| > 1; mirror
  swaps; −σ⁻¹ is no braid image (given an index character, cited).
- Route 2: right complex structure ⇒ Sp(1)_left × U(1)_right; conjugation swaps sides;
  left Sp(1) moves Γ_u (QuaternionSidedSymmetry.lean). Weak-isospin identification: scope (a).
- Route 3: no held source derives which side; one-sidedness derived (Connes, Furey,
  SO(10)), label conventional; LR models take v_R > v_L as input.
Open: D-W2 (long-braid limit as mechanism), D-W3 (second singlet space). Audit §4.
