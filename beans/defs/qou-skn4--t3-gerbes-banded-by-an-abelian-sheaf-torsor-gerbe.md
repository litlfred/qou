---
# qou-skn4
title: 'T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:48:14Z
updated_at: 2026-10-12T19:48:14Z
parent: qou-533l
---

Tier T3 of qou-533l.

**Carried from T2.**
- (a) Port `cechObstruction_lift_change` to the presheaf setting (independence of the local lift ξ).
- (b) Refinement of covers, then the colimit over covering families for a Grothendieck topology. Mathlib's H1 file lists the same colimit as a TODO.

**Main.** Gerbes banded by an abelian sheaf A: groupoid-valued stacks, locally nonempty and locally connected, with automorphism sheaves identified with A. Then a central extension of gerbes in the sense of Yekutieli Def 3.21 (`library/arxiv-0801.0083v4`, sec-002 :671).

**First milestone.** The torsor gerbe Tors(G) (exa:27), recovering T2b. Mathlib has no stacks. Scope the minimal 2-categorical structure first, and ask the owner before committing to a large design.

## 2026-10-12: residual (a) done
`PresheafCentralExtension.obstruction_lift_change`: two local lifts ξ, ξ' give obstructions differing by the coboundary of a 1-cochain of 𝒜, so the class is independent of ξ. Sorry-free; lean-direct exit 0, no warnings; axioms [propext, Classical.choice, Quot.sound].

**Next:** residual (b), refinement of covers and the colimit over covers, then gerbes. Gerbes need a design decision, since Mathlib has no stacks. That decision goes to the owner before any large build; per this bean, scope it first.

## 2026-10-12: residual (b), part 1, done: refinement
`pullOneCochain`, `pullOneCocycle`, `pullTwoCochain`, and `obstruction_pull`: pulling γ and ξ back along a refinement f : V j ⟶ U (r j) pulls the obstruction back. Lean-direct exits 0 with no warnings; axioms are standard.

**Remaining for (b):** the colimit over covering families of a Grothendieck topology, i.e. a well-defined class independent of the cover. Then gerbes.

## 2026-10-12: class-level vanishing done
- `IsCoboundary`: a 2-cochain is a coboundary.
- `isCoboundary_obstruction_iff`: whether the obstruction vanishes does not depend on the local lift ξ.
- `isCoboundary_pull`: vanishing survives refinement.
Lean-direct exits 0; standard axioms.

**Not done.** The CONVERSE, that vanishing on a refinement implies vanishing on the coarser cover, needs 𝓔 (or 𝒜) to be a SHEAF so that lifts glue. That is the real content of the colimit over covers, and the presheaf framework cannot supply it. Next: add the sheaf condition (Mathlib `Presheaf.IsSheaf` over a Grothendieck topology), then gerbes. The design goes to the owner first.
