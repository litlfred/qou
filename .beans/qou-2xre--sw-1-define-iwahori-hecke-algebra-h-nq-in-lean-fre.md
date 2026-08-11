---
# qou-2xre
title: 'SW-1: define Iwahori-Hecke algebra H_n(q) in Lean (FreeAlgebra quotient; σ_i, quadratic (σ_i-q)(σ_i+q⁻¹)=0 + braid relations)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:30:46Z
updated_at: 2026-08-02T19:33:06Z
parent: qou-59vq
---

Foundational, no deps. Define H_n(q) as a K-algebra: FreeAlgebra K (Fin (n-1)) quotient by the two-sided ideal of quadratic + braid + far-commutation relations, OR as MonoidAlgebra of the braid group quotient. Provide the AlgHom universal property (extend a map on generators satisfying the relations). Ref: [kassel1995]. Sorry-free target; honest sorry+Ref only if a Mathlib quotient lemma is missing.

## ✅ LANDED (2026-08-02, background agent) — sorry-free, verified

[`QOU/SchurWeyl/HeckeAlgebra.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeAlgebra.lean)
(EXIT=0, 18 decls, sorry-free, independently re-verified). `H_n(q)` =
`RingQuot` of an inductive relation (quadratic + braid + far-commutation) on
`FreeAlgebra K (Fin n)`, generic `[CommRing K]` (§7c), QOU §7a normalization
via `qi` (intended `q⁻¹`), inverse-free until the guarded units section.

**Ships the full universal property (this is the SW-4 interface):**
`lift` (AlgHom from any relation-satisfying `g : Fin n → A`), `lift_σ`
(`lift g (σ i) = g i`), `hom_ext` (uniqueness), plus `σ_quadratic/_braid/
_commute/_factored` and the units (`σInv`, `isUnit_σ`, guarded by `q*qi=1`).

**SW-4 handoff:** a Hoefsmit rep = a matrix family `g` + the three relation
proofs → `Hecke.lift g`. SW-4 crosses the §7c wall to `K:=ℝ` only at the
seminormal-matrix step (Real.sqrt/q⁻¹); check relations generically first.

**Duplication note:** repo already has `QOU.Hecke.IwahoriHecke` (units, (σ−q)(σ+1)
normalization) and `QOU.IwahoriHecke.Quotient` (quadratic-only, Coxeter-general);
neither ships lift+uniqueness. Consolidation is a possible follow-up (back-port
`lift`/`hom_ext`), not done now. Wired into QOU.lean.
