---
# qou-kebu
title: 'T2b: derive per-strand twist multisets from framed braid words'
status: todo
type: task
priority: high
created_at: 2026-08-04T10:16:22Z
updated_at: 2026-08-04T17:40:00Z
parent: qou-8lxd
---

BATTERY RESULT (strand-twist-y-battery.witness.json):
- 10,000 candidate helon-style twist assignments tested
- Only 4 survive the spectrum + nucleon-GMN battery
- u-quark multiset {0,1,1} is UNIQUELY determined
- electron multiset {-1,-1,-1} is UNIQUELY determined
- All 4 survivors are sign-flip variants of the SAME assignment

DERIVATION GAP:
The battery proves CONSISTENCY (the twist assignments are compatible
with known physics) but does NOT DERIVE them from QOU axioms.

To close T2b, need to show: given the framed braid word for each
torus knot T(2,p), the per-strand twists follow from the ribbon
structure of the Hecke category. Specifically:
1. The twist θ_V = q^{c_V} acts on each strand by the Casimir
2. For T(2,p) = σ₁^p, the total twist is p·θ_V
3. The per-strand multiset is determined by the braid monodromy
4. The battery result shows the answer is {0,1,1} for u, etc.

DEPENDS ON: T2 (hypercharge from ribbon twist = the derivation
of what Y means categorically, which is still the gap).
