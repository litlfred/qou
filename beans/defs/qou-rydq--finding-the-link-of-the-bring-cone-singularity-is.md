---
# qou-rydq
title: 'FINDING: the link of the Bring cone singularity is the unit tangent circle bundle of Sigma_4 (Euler number chi_eu = -6), NOT a 3-Sasakian S^3/Gamma; BringCone.lean models H = C^2, the cone over S^3'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-decide
created_at: 2026-09-15T21:23:32Z
updated_at: 2026-10-10T08:08:34Z
parent: qou-8lxd
---

Measured 2026-09-15 while answering the owner's 'obstruction to tetraplectic being global, not affine?' question. FACTS (standard, cited): Bring's curve B in P^3 (after sum x_i = 0) is the (2,3) complete intersection of the invariant quadric and cubic, degree 6, genus 4, and this is its CANONICAL embedding: O_B(1) = K_B (deg K = 2g-2 = 6). Hence the affine cone C(B) minus the vertex is the total space of O(-1)|_B = K_B^{-1} = T_B minus the zero section, and the LINK of the singularity is the unit circle bundle of T_B, i.e. the unit tangent bundle UT(Sigma_4), a Seifert-fibred 3-manifold with Euler number e(T_B) = 2 - 2g = -6 = chi_eu(Sigma_4) and INFINITE pi_1 (SL~2(R) geometry). A 3-Sasakian 3-manifold is a spherical space form S^3/Gamma (finite pi_1). So the sentence in lem:bring-cone-reeb-quaternionic-twist.md that the link 'carries a 3-Sasakian (degenerate quaternionic-contact) structure' is not true of the Bring cone; it is true of the LOCAL model H = C^2 (cone over P^1 with O(-1), link S^3 = Hopf, Euler number -1), which is exactly what lean/QOU/BringCone.lean formalises: abbrev BringCone R := Quaternion R. The Lean lemma (reeb_twist_ij/jk/ki) is a correct, sorry-free quaternion identity; only the prose identification of the space is wrong, and the '-6' shows up here as the OBSTRUCTION: the Euler number of the link fibration is -6 for the Bring cone against -1 for H, so no global quaternionic triad / 3-Sasakian structure exists on the Bring cone, and the tetraplectic (= volume-form, m=1 vacuous, bean qou-8p1g) structure is the only global remnant. Consumers (measured): def:bring-cone-tetraplectic-structure <- lem:bring-cone-reeb-quaternionic-twist (+proof) <- rem:tetraplectic-su2-gauge-reading; conj:tetraplectic-askey-localisation; conj:tetraplectic-sw-localisation-bridge; Lean importers of BringCone: QuaternionicElectroweak.lean, BringConeSplit.lean, Brings/CategoricalLagrangianDMCubic.lean (which calls BringCone 'the load-bearing structure'). Nothing in the mass/binding/Q_beta chain consumes the tetraplectic material; CartanContraction.lean (the iota_R omega closed 3-form of the c_3 scope doc) has ZERO content consumers. OPTIONS for the owner (content change, ask-first rule): (1) rescope the lemma prose to the local model ('the link of the model cone C^2 = H'), keep the Lean; (2) restate the global object honestly: link = UT(Sigma_4), Euler number chi_eu(Sigma_4) = -6, contact structure = the canonical one whose Reeb flow is the geodesic flow, S^1-action only (no SU(2) triad); (3) both, and record that the quaternionic triad of QuaternionicElectroweak is a local/frame statement. Recommendation (agent judgement): (2)+(3) — it turns a false identification into the one place the -6 appears as a genuinely GEOMETRIC invariant of the cone, which is what the chi_eu(M_0) separation of 2026-09-15 needs. Not enacted.


2026-09-15 LEAN + REMARK LANDED; the lemma rewording stays OWNER-GATED. lean/QOU/Brings/BringConeLinkEulerNumber.lean: canonical_link_euler_eq_chi (for a canonically embedded curve the link's Seifert Euler number −deg K = 2 − 2g equals χ_eu), bring_link_euler (−6), hopf_link_euler (the quaternionic model is the cone over the Hopf bundle, Euler number −1), bring_over_hopf (factor 6); Orlik–Wagreich cited (orlik-wagreich1971 added to references.ts, not ingested). rem:spatial-realization-base-generality (models-of-qous) records the singular-base consequence: the vertex is what "ordinary smooth manifold" excludes; the link is a circle bundle over the curve with infinite π₁, and the quaternionic (3-Sasakian) picture is a local model of the smooth fibre, not the link. NOT enacted: the rewording of the corpus's lemma lem:bring-cone-reeb-quaternionic-twist / rem:tetraplectic-su2-gauge-reading (options recorded above; recommendation unchanged: restate link = UT(Σ₄), Euler number −6, scope the triad as local). Awaiting the owner's pick.


## Re-filed `8f-lean` -> `8f-decide`, 2026-10-10 — the Lean half is DONE; what is left is the owner's pick

**The Lean landed and is verified on the live tree.**
`folio/quantum-observable-universe/lean/QOU/Brings/BringConeLinkEulerNumber.lean`
(66 lines, sorry-free — its only `sorry` match is the docstring's "no `sorry`"):
`canonical_link_euler_eq_chi`, `bring_link_euler` (−6), `hopf_link_euler` (−1),
`bring_over_hopf`.

**So this bean carries no agent work.** Its own last line is *"Awaiting the
owner's pick"*, and the three options are a **content change** to
`lem:bring-cone-reeb-quaternionic-twist` / `rem:tetraplectic-su2-gauge-reading`,
which the 2026-09-07 ask-first rule reserves to the owner (it neither increases
precision nor is derived from the corpus — it *corrects* the corpus against an
outside geometric fact). Filing it under `8f-lean` made it look like a
scaffolding task. It is not.

Same mis-filing class as `qou-skgn`, and for the same reason: **the front tags
were assigned from TITLES.** This title opens "FINDING:", which reads as
measurement-complete rather than decision-pending.

Options, costs and the recommendation are unchanged and stated in the body above
(recommendation: (2)+(3) — restate the link as `UT(Σ₄)` with Euler number −6 and
scope the quaternionic triad as local/frame). **Default if unanswered: nothing
changes; the lemma keeps a prose identification that is true of the local model
`ℍ = ℂ²` and not of the Bring cone, and `rem:spatial-realization-base-generality`
already records the correct statement elsewhere.**
