---
# qou-rtm0
title: Route C M0 (bounded, Lean) — formalize the bar-involution action on the certified Stokes matrices S+(0)/S-(0) and prove the {3,4} split IS its bar-eigenspace decomposition
status: completed
type: task
priority: high
tags:
    - alien-habiro
    - g3-aomega
    - route-c
created_at: 2026-08-11T00:45:00Z
updated_at: 2026-09-26T11:03:17Z
parent: qou-rtec
---

First honest brick of Route C (docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md §4 M0). The scalar-exhaustion (Driver14 no_scalar_matches_chirality_split_datum, sorry-free) says the DT count is not a scalar; M0 turns that negative into a positive structural statement.

TASK: define the bar-involution (q↦q⁻¹ / chirality / orientation-reversal) action on the certified integer Stokes matrices S⁺(0), S⁻(0) (already Fin n → Fin n → Int in StokesQZeroDTCount.lean and FiveTwoDTSpectrumSplit.lean) and prove, sorry-free, that the 5₂ DT spectrum split (4∈S⁺, 3∈S⁻) IS the bar-eigenspace decomposition — i.e. the count factors through a ℤ/2 (bar-even ⊕ bar-odd) graded object of which any scalar is the trivial shadow. Connect to the landed bar-parity infra (c1-ggm-bar-parity-faces / DoorVParityNoIdentity / OhtsukiTowerBarParity).

WHY IT MATTERS: converts "no scalar works" into "the count IS the bar-graded object", grounding Route C in the corpus's own bar-parity programme rather than a generic CoHA. Bounded, decidable-integer, Lean-achievable now (both matrices are concrete Fin-indexed integer matrices). NOT a derivation of A_ω (M3 is); M0 is the structural reframing.

Downstream: M1 (closed-sector (Q,W) for 4₁/5₂ from NZ gluing / Bring embedding), M2 (BPS cohomology dim = {3,4}), M3 (Hecke→BPS categorified-AJ bridge = the open research theorem).

## 2026-08-11 DONE
M0 capstone added sorry-free to QOU/QBeta/FiveTwoDTSpectrumSplit.lean (core Int, lean-direct exit 0): barSwap (involution) + barSwap_involutive; eigenspace laws barEvenPair_fixed / barOddPair_negated; barGrading_faithful (2*d+ = even+odd, 2*d- = even-odd, so the Z/2 grading is FAITHFUL); dtPair52_grading = (7,1); dtPair52_chiral; symmetric_scalar_blind_to_chirality (bar-graded restatement of Driver14 no_scalar_matches_chirality_split_datum).

INTEGRATED (the file previously had no content-block home): new proposition prop:dt-spectrum-bar-eigenspace (.ts + .md), lean.ref -> QOU.QBeta.FiveTwoDTSpectrumSplit, wired into the mass-theory chapter manifest after aomega-fourone-dt-count. run-validate exit 0 (only pre-existing unrelated warnings).

Next: M1 (closed-sector quiver-with-potential for 4_1/5_2 from NZ gluing), M2 (BPS cohomology dim = {3,4}), M3 (Hecke->BPS categorified-AJ bridge = the open research theorem).
