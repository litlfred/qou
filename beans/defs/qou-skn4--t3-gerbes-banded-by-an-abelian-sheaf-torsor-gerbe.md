---
# qou-skn4
title: 'T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:48:14Z
updated_at: 2026-11-15T17:55:17Z
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

## 2026-11-15 (session 01Qmmkt7): G1 started, R3 scoped
- PR #7945 (issue #7944): `QOU/MathlibExt/CechColimit.lean`, sorry-free. Refinement map on Čech H², a colimit `CechH2` over admissible covers, and the T2b lifting obstruction as a cover-independent class (`cechObstruction`, `_indep_lift`, `_pull`, `_eq_one_of_lift`).
- Still open: the converse (trivial in colimit ⇒ lift on a refinement) needs filtered covers (G1b). The scope note's degree-2 injectivity claim was not claimed.
- R3 plan: /mnt/project-files/qou-leftovers/r3-cohomology-route.md. The Kummer class is δ(T_S) for 1→μ_n→𝒪*→𝒪*→1, and δ(L) = deg L mod n. Missing pieces: H²(S,μ_n)≅ℤ/n (no Čech–singular comparison in Mathlib) and the Kummer sequence on a Riemann surface.

## 2026-11-15 G1b and R3 landed on PR #7945 (still open, not merged)

- G1b `CechColimitConverse.lean`, sorry-free. It has the prism homotopy, `Cover.meet` from pullbacks, and `isCoverDirected_topology` (the covers of a Grothendieck topology with pullbacks are directed). It proves `cechClass_eq_one_iff` (trivial in the colimit iff a coboundary on a refinement) and `cechObstruction_eq_one_iff` (lifts on a finer cover iff the class is trivial).
- R3 `CechKummerSurface.lean` has `CechH2.map` and `cechKummer_eq_map_chern`, both sorry-free. Conditional on `KummerSurfaceData`: trivial iff n ∣ χ, and χ = −6 gives n ∣ 6.
- Still open: the Čech–singular comparison and orientation (`KummerSurfaceData`), Poincaré–Hopf `deg c₁(T_S) = χ`, and local real lifts of the tangent cocycle. Not planned (Mathlib-scale).
