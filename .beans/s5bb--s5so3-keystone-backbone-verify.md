---
# s5bb
title: 's5-so3 keystone — combinatorial backbone VERIFIED (14/14); functor IDENTIFIED, q-closure OPEN'
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T03:30:00Z
updated_at: 2026-06-16T03:30:00Z
parent: qz9k
---

User pick ("go" on the keystone all three beans reduced to: `conj:s5-so3-fiber-action`).
PR #2504.

## Result (2026-06-16) — backbone verified + stale framing corrected; pending human close

Compute: [`computations/probes/s5so3_branching_backbone_verify.py`](../computations/probes/s5so3_branching_backbone_verify.py)
(witness `s5so3-branching-backbone-verify.witness.json`, **14/14 self-checking assertions**).
Finding: [`docs/audits/2026-06-16-s5so3-keystone-backbone-verified.md`](../docs/audits/2026-06-16-s5so3-keystone-backbone-verified.md).

- **VERIFIED** (this compute): Res^{S₅}_{S₃} branchings + (1,1,1) difference; S₅↓A₅ generation
  indexing (ℓ=1→T₁ in (3,1,1); ℓ=2→H in (3,2)/(2,2,1)) with char-table orthonormality self-check;
  per-block H₃(q) Borromean chars (triv=1, sign=1, χ^{(2,1)}=2−3h⁴−h⁶) ⇒ h⁴ exclusively in (2,1).
- **CORRECTION** to the merged `#2345` synthesis doc: the functor is **IDENTIFIED** as Res^{S₅}_{S₃}
  (2026-06-13), not "awaiting". Three-tier: VERIFIED combinatorics / IDENTIFIED functor / OPEN
  q-deformed closure (the E_{(3,2)} vs E_{(3,1,1)} shift at q₀ + 210 ppb).
- **Fair critical-distance read**: the functor-resolution doc is appropriately scoped (its §4 lists
  the open obligations); the overclaim risk is only in the operator-branching §5 "closes" language.
- **Link to qkhc**: C3 confirms the q=1 χ^{(1,1,1)}(β_Bor)=1; but the c_k sign-block lead must still
  reproduce the q-holonomic argument recurrence + clear refuted-class C12 — necessary, not sufficient.
- **No q-deformed probe run** (pyhecke_native + owner gated).