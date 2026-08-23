---
# qou-v4ns
title: 'GAP: SU(3) Sym^2 fundamental irreducibility (Mathlib gap) — Sym2Gate'
status: scrapped
type: task
priority: normal
created_at: 2026-08-22T19:37:22Z
updated_at: 2026-08-22T19:39:23Z
---

content/quantum-observable-universe/lean/QOU/Eightfold/Sym2Gate.lean carries su3_sym2_irreducible as 'axiom : True' — a content-free placeholder — and octonion_3_passes_sym2_gate as '(6:ℕ)=6 ∧ (0:ℕ)=0' (reflexive tautology). Both are advisory in the vacuity ledger.

The REAL claim is standard rep theory: the SU(3) fundamental 𝟑 is complex type (𝟑̄ ≠ 𝟑), so Sym²(𝟑) = 𝟔 is irreducible (no singlet), hence 𝟑 passes the Sym² gate. Mathlib has no SU(3)/complex-type Frobenius-Schur machinery to state this faithfully, so it cannot currently be a real Lean statement over genuine rep objects.

Note the SU(2) side IS formalized next door in Sym2GateParity.lean (parity criterion, zero_mem_sym2Indices_iff, adjoint_fails_gate) — that carries the load-bearing physics. Sym2Gate's two decls are the SU(3) complement that stays a documented gap.

OPEN: either (a) build minimal SU(3)-fundamental / FS-indicator rep infra to state+prove Sym²(𝟑) irreducible, or (b) if never needed downstream, remove the vacuous axiom + restate octonion_3_passes to a real dim claim tied to sym2_dim_3. Ref: [fulton-harris1991] §11; FS indicator (-1)^{2j}.

SCRAPPED as redundant with qou-8fl1 item 3 (the Eightfold coverage bean already tracking Sym2Gate.lean vacuity, referenced from the file). Diagnosis + resolution options folded into qou-8fl1.
