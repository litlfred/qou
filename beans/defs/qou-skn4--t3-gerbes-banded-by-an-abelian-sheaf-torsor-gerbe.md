---
# qou-skn4
title: 'T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:48:14Z
updated_at: 2026-11-21T12:40:00Z
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

2026-11-15 (session_01Qmmkt7arrvA9y98dYdLsLV): KummerSurfaceData consistency check, branch claude/gerbe-kummer-data-point-2026-11-15, file QOU/MathlibExt/CechDominantCover.lean, sorry-free. In a thin category, a cocycle on a family with a dominant member is a coboundary, so Ȟ² is a point when every admissible cover contains the whole space. On a one-point space with the open-cover predicate, every field of KummerSurfaceData is proved (both degrees are 0). This shows the class is satisfiable. It does NOT give the surface case: hχ forces χ=0. Still open: Ȟ²(S,ℤ)≅ℤ and Ȟ²(S,μn)≅ℤ/n for a closed surface (Čech–singular comparison). Bean stays open.

## 2026-11-15 (later): surface steps S1 and S2, plus R2
- S1 is proved: Čech H² of any finite (Alexandrov-discrete) space equals the H² of its minimal cover. See `cechH2EquivMinimal` in `QOU/MathlibExt/CechCofinalCover.lean`, branch `claude/c5a-r2-surface-2026-11-15`, issue #7958. It is sorry-free.
- S2 is negative. On the 6-point finite S², the Čech H² of the minimal cover is 0, measured exactly mod 2, mod 3 and mod 1000003, with locally constant ℤ coefficients. The sanity check passes: the 4-point S¹ gives H¹ = 1. So no finite model of this type gives a non-trivial KummerSurfaceData. Notes are in /mnt/project-files/qou-leftovers/s2-finite-sphere-negative.md.
- A real surface still needs the Čech = singular comparison, which is Mathlib-scale. This bean stays OPEN.
- R2, reading A, is proved to fail for every z: `StrandTowerObstruction.lean`. Reading B (root of unity) has no derivation in the corpus.

## 2026-11-15 — surface case C1 done at cover level; C2 OPEN (PR #7964)

Landed, sorry-free, on `claude/c5a-r2-surface-2026-11-15`:
- `CechNerveTetrahedron.lean`: for a four-set open cover with nonempty preconnected
  overlaps of at most three members and discrete abelian G, the alternating face
  product is a degree on H²(cover) that detects the trivial class, is natural in G,
  and (when no point lies in all four) is a bijection `H²(U,G) ≃ G`.
- `CechSphereHemispheres.lean`: the four open hemispheres of S² centred at the
  tetrahedron vertices are such a cover; `cechH2SphereHemiEquiv`, and the
  cover-level `kummerSurfaceData_sphereHemi`.

STILL OPEN (do not close this bean): C2, that the hemisphere cover computes the
full open-cover colimit Ȟ²(S², G). Needs either Leray (Čech H¹ = H² = 0 on the
convex-cone slices of S²) or a triangulation argument for fine covers; neither is
in the repo or Mathlib. Estimated 5–10 sessions. C3 (full instance, χ = 2) waits on C2.

## 2026-11-15 — D3 `StackGerbe.lean` Milestones 2 & 3 landed (PR #7985, commit `c9b5c7d59272bea9b0afd42852a09253e27ad54c`)

Per owner ruling `Q-VO9T-1 = 3` (session `session_012EE90758AE4945AC814D43`), proved sorry-free in `QOU/MathlibExt/StackGerbe.lean` (0 warnings, standard axioms `[propext, Classical.choice, Quot.sound]`):
- **Milestone 2 (`Hom = Iso` on `A`-torsors, fibre groupoid, band isomorphism):**
  - `SheafTorsor J A P`, `equivariantHom_injective`, `equivariantHom_surjective`, `isIso_of_equivariantHom_torsor`, `inv_mem_equivariantHom`
  - `trivialSheafTorsor`, `trivialTorsorEndEquiv : (equivariantHom (regularAction A hA) (regularAction A hA)).obj (op X) ≃ A.obj (op X)`
  - `TorsorFibre J A X`, `torsorFibreCategory`, `torsorFibreGroupoid`, `torsorPullback`, `torsorPullback_id`, `torsorPullback_comp`
- **Milestone 3 (genuine `SiteGerbeData` over `(C, J)` and `Tors(A)` instantiation):**
  - `equivariantHom_of_sections`, `localIsoSieve`, `torsor_locallyConnected`
  - `SiteGerbeData J A` and `torsorSiteGerbe J A hA hAsheaf`
- **Still open (keep `status: in-progress`, do NOT close):** C2/C3 surface colimit and effective descent of objects / central extension of gerbes (Yekutieli Def 3.21 / Thm 4.17).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Not recorded above: step C2 is DONE. PR #7969 (merged 2026-11-15 22:09, commit ae9bfdc319) proves the four-hemisphere cover computes Ȟ²(S², G) over all open covers for every discrete commutative G, without Leray: CechNerveValues (P1), CechSplit (P2), CechSameNerve + CechSphereBoxes (P3a/b), CechSphereFine (P3c/d), CechSphereGood (P4, Lebesgue number) and CechGoodRefinement (generic reduction). C3 (kummerSurfaceData_sphere') is therefore unconditional on S². Open: the genus-4 analogue (a cover of Σ₄ with connected overlaps and Ȟ²(Σ₄, G) ≅ G); this needs a model of Σ_g that neither Mathlib nor the repo has. Effective descent of objects and the central extension of gerbes remain open (qou-t1dx, qou-0xk8).
