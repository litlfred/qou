---
# qou-avv6
title: 'A=3 magnitude ROUTE 5: mu3 target robustness audit — well-posed at ~10pct, NOT an artifact, NOT to 3 sig figs'
status: todo
type: task
tags:
    - a3-cross-channel
created_at: 2026-08-01T23:55:59Z
updated_at: 2026-08-01T23:55:59Z
---

Red-team audit of whether mu3=+0.4708 (numerator of r*=mu3/c3~1.585) is a structural target or a residual-decomposition artifact.

VERDICT (scope-a): well-posed at ~10pct, NOT an artifact, NOT to 3 sig figs. The ROUTE 1-4 cross-channel hunt is JUSTIFIED (sign + O(1.6) magnitude are real), with the caveat: score derived c3 by sign + r* in [1.50,1.71], NOT by matching 1.585 to 3 sig figs.

RECIPE: mu3 = M(3) = B(3H)/B(2H) - [3]_q = 3.8128 - 3.3420 = 0.4708. Exact reproduction. A 12.3pct residual of two O(3.4) numbers -> condition number ~8.1. NOT a statistical moment: 3 isotopes pin 3 coeffs via unit-triangular counts matrix (det=1) -> exact invertible relabel; mu3 = M(3) identically (mu2=0 forced by deuteron self-reference). Axis-(c) 'moment method' freedom does not exist.

ROBUSTNESS:
- Axis (a) isotope/isospin: within isospin-corrected-strong family (3H, 3He+E_C) mu3 in [0.445,0.509], spread 1.14x (+-8pct), r* in [1.50,1.71]. Collapses to 0.127 (0.27x) only under raw 3He (no Coulomb corr) = physically inconsistent, not defensible.
- Axis (b) subtracted ladder convention: PINNED. rho_grad=[A]_q! is the coinvariant graded dimension -> Gaussian/unbalanced forced by Chevalley. The 1.63x balanced-vs-unbalanced swing was checked and RETRACTED as illegitimate (balanced is not a graded dim). q0 pin (muon/proton) not a lever (identical to 8sf).
- Corpus (deltalambda_damping_nonmonotone_wall #4300) already proves sign(mu3)=+ robust for BOTH raw and corrected AME, and non-monotone -> not a damping (so A=3 baseline [3]_q is stable).

DELIVERABLES:
- computations/deltalambda/mu3_target_robustness_audit_probe.py + mu3-target-robustness-audit.witness.json
- content/quantum-observable-universe/lean/QOU/MassTheory/Mu3TargetWellPosedness.lean (sorry-free, lean-direct exit 0; mu2 FORCED [cannot reach 1] vs mu3 FREE [surjective in target])
- docs/audits/2026-08-01-mu3-target-robustness-audit.md

Branch claude/mu3-target-robustness-audit-2026-08-01. Nothing wired.
