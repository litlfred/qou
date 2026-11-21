---
# qou-lx8f
title: 'Bring lifting obstruction: coefficient group (Z vs Z/2 vs O^x) and the Bring-specific vanishing claim'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:14:41Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-vo9t
---

## Question
The brane-tower lifting obstruction kappa_n on Bring's surface Sigma_4 is written with three different coefficient groups in the corpus:
- **Z**: the Euler class e(xi) = -6 in H^2(Sigma_4, Z) (fluid-dynamics/ns-obstruction-*.md). Also the `persistence` field and `perpetual_obstruction` in lifting-and-descent/yekutieli-lifting.lean.
- **Z/2 = centre(SU_q(2))**: QOU/BringsSurface.lean `yekutieli_lifting`. Its docstring falsely said H^2(Sigma_4, Z/2) = 0; corrected in PR #7747.
- **O_M^x**: yekutieli-lifting.md and the archimedean band.

## The tension
-6 is nonzero in H^2(Sigma_4, Z) = Z, but -6 = 0 mod 2. So "the obstruction persists" (Z) and "the obstruction vanishes" (Z/2) can both be true of the same Euler class under different coefficient groups. The two readings imply opposite answers to "does the tower lift on Bring?".

## Facts already true
- H^2(Sigma_g, Z/2) = Z/2 and H^2(Sigma_g, Z) = Z for a closed orientable surface.
- w_2(T Sigma_g) = chi mod 2 = 0, so every closed orientable surface is spin; for Bring, chi = -6.

## To do
1. Identify which bundle or gerbe the tower lifts, and its band (corpus-grep is running).
2. Formalize (sorry-free) the reduction-mod-2 statement: the mod-2 image of an even Euler class vanishes.
3. Report which reading the corpus actually supports; do not choose one by fit.

## 2026-10-12: six-path corpus check (corpus-grepper) plus own verification

**Six coefficient groups, not three:** ℤ (Euler class), ℤ/2 (BringsSurface), 𝒪_M^× (yekutieli-lifting.md and others), 𝔾_m (Kummer blocks), Z(Aut A_n) (brings-is-qou-proof.md), and HH²(U_q, Ad) ≅ ℤ (qou_obstruction_reduction.lean). **The band 𝓑 is defined nowhere.** No file identifies which bundle or gerbe the tower lifts.

**The 𝒪^× band kills the obstruction on any surface (scope b; proved invariant: the exponential sequence).**
- 0 → ℤ → 𝒪 → 𝒪^× → 0 gives H²(Σ, 𝒪) → H²(Σ, 𝒪^×) → H³(Σ, ℤ). Both ends are 0 on a compact Riemann surface; for smooth 𝒪, the sheaf is fine and H²(𝒪) = 0 as well.
- So H²(Σ₄, 𝒪^×) = 0, and every κ_n vanishes under that band. This contradicts the "perpetual obstruction" (`persistence` field).
- The ℤ-valued κ₀ = e = −6 cannot live in H²(𝒪^×). It is naturally an element of H²(Σ, ℤ) ≅ ℤ, which receives Pic = H¹(Σ, 𝒪^×) via c₁ — one degree lower than H²(𝒪^×). The corpus mixes the degree.
- Also: `yekutieli-lifting-su2.md` writes H²(ℂP¹, 𝒪^×) ≅ H²(ℂP¹, ℤ) ≅ ℤ. Wrong: it is 0; the ℤ is Pic = H¹(𝒪^×).
- Also: `ns-obstruction-computation.md:30` says Bring "possesses real dimension 4"; it is 2.
These are corpus-content corrections and wait on the owner (AGENTS.md §ASK THE OWNER). Tracked in bean qou-v1np.

**ℤ vs ℤ/2.**
- For an oriented surface bundle, w₂ = e mod 2. For Bring's tangent bundle, e = χ = −6, so w₂ = 0 and Bring is spin.
- The bridge in the held source is Yekutieli 2010 `exa:27`: a central extension of sheaves of groups gives a central extension of torsor gerbes. With ℤ/2 → Spin → SO, that is exactly the w₂ lifting problem. No corpus file cites it.
- Mathlib has no Stiefel–Whitney or Euler classes, so "w₂ = χ mod 2" cannot yet be stated meaningfully in Lean. A bare `(-6) % 2 = 0` lemma would be integer arithmetic dressed as cohomology and is deliberately NOT added; `PNeqNpEquivalence.chi_mod_vanishes_iff` already covers the arithmetic.

**κ₀ = Euler class** is asserted (thm:qu-to-qou item 2; "via the Gysin sequence") and is a structure field in every Lean file. It is never derived.

**Theorem hypothesis dropped.** Yekutieli Thm 4.17 assumes the obstruction class "is defined". The corpus drops that everywhere.

**Status:** the coefficient question is answered *negatively*. The corpus has no consistent band, and the 𝒪^× reading makes the obstruction identically zero on Bring. The live Bring-specific question is therefore "which band", not "does it vanish". That is an owner decision about the framework's definition of 𝓑. Bean stays open.

## 2026-10-12: band-construction audit (option 1, owner)
`docs/audits/2026-10-12-jet-tower-band-construction.md`.

**The definitions do not fix B.** The gerbes G_n, the downward functor F and the site are never constructed. If F is descent, the globally built J^1(A_n) is itself a lift, so kappa_n = 0 in every band (Yekutieli "Obstruction to lifting objects").

**Per band on Sigma_4.**
- O^x, G_m, jet kernels: kappa identically 0 (scope b).
- mu_n and Z/2: kappa_0 = -6 mod n, so 0 for n dividing 6, which includes w_2. Item 3 is vacuous.
- Z: kappa_0 = c_1 = -6 holds via Z -> R -> U(1). That is a real Yekutieli instance, but not a jet step. Item 3 is ill-posed.

**Item 3's complementary-subgroups step fails on Sigma_4**, independently of R:
- H^2(Sigma, O) = 0, so the corrections vanish;
- H^2(Sigma, Z) = Z has no nontrivial complement;
- once kappa_0 != 0, kappa_1 has no object to be defined on.
A fourth reason, Hom(divisible, Z) = 0, holds only for divisible R. I scoped it in the doc.

**Open and promising:** the Atiyah class a(T Sigma_4) in H^1(Sigma, K) = C, proportional to the degree. -6 genuinely enters the jet tower there, but in degree 1 and holomorphically only.

**The same claim recurs** in kummer-tower.md:25-29, ns-obstruction-tower.md:40-47, ns-singularity-descartes-proof.md:16 and vertex-algebra-relations.md:475.

## 2026-10-12: Atiyah route (owner option 1, second round)
`docs/audits/2026-10-12-atiyah-jet-classes-bring.md`. The holomorphic n-jet extension class of a degree-d line bundle on a genus-g curve lives in Ext^1 = H^1(K) = C for every n, and equals c·n·(d + (n−1)(g−1)). This is a hand derivation with an exact symbolic check for n = 1..5. It matches three classical results: the Atiyah class at n = 1, projective structures at n = 2, and Bol operators on the vanishing locus.

**On Σ₄:**
- T Σ₄ (d = −6): e_n ∝ 3n(n−3), which is **zero at n = 3**, so not perpetual.
- K (d = 6): e_n ∝ 3n(n+1), never zero. But every level is a multiple of one scalar, the classes are degree 1, and K is not the bundle the theorem names.
- Smooth category: every class is 0.

**Verdict:** no reading built on T Σ₄ yields a perpetual obstruction. The surviving L = K reading would restate item 3 as a condition on d, which is an owner decision. Not Lean-checked; the closed-form arithmetic is a one-line `ring`.

## 2026-11-15 — owner decision: item 3 is the degree condition

Owner chose "restate item 3 of thm:qu-to-qou as a degree condition" in the project thread "Settle open-problem leftovers". On this branch item 3 already reads (since 2026-10-12): ξ has an n-th root iff n | χ(S), obstruction χ mod n ∈ H²(S, μ_n); for Bring n ∈ {1,2,3,6}. So the statement needs no further edit.

**Open, owner call:** 66 files under `folio/` still say "perpetual obstruction", including `thm:motivic-perpetual-obstruction` and `axiom yekutieli_perpetual` (`climax-volume-mass/vertex-algebra-jet-relations.lean:146`, an `axiom`). Not swept: AGENTS.md §ASK THE OWNER.

## 2026-11-15 — "perpetual obstruction" re-scope applied (owner option 1, PR #7747)

Audit: /mnt/project-files/qou-leftovers/perpetual-obstruction-audit.md (66 files; 24 flagged, 42 left).
Lean (commit 0e71fb90d): axiom yekutieli_perpetual removed; qu-to-qou field perpetual -> kummer_persistence
(+ qu_to_qou_obstruction_persists_iff, qu_to_qou_chi_neg_six); BringsObstruction now carries the degree
condition and derives the obstructed levels; docstring notes on 5 files. All lean-direct exit 0.

Prose (11 edits in 10 blocks + millennium-bounds authorNote). On review, q-gl-intro and
q-gl-obstruction-classical-compatibility were reclassified to A (they already say density-1 Kummer levels),
and substrate-gm-torsion already carries a Scope paragraph; left as is.
Old text of blocks whose schema drops authorNotes (prose/table) is recorded here:
- climax-volume-mass/vertex-algebra-relations-table3-data: "\neq 0$ | Perpetual obstruction |"
- introduction/chapter-overview: "revealing a perpetual obstruction $\kappa_0$ that blocks infinite jet refinement."

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
State on main: PR #7747 merged 2026-11-15 (perpetual obstruction scoped, axiom yekutieli_perpetual removed). The cohomological side of route R3 has advanced since the last note: PR #7969 (merged 2026-11-15 22:09) proves Čech H² of S² over ALL open covers equals the coefficient group (CechSphereGood.hemiComputesCech, kummerSurfaceData_sphere', sorry-free). So KummerSurfaceData is now inhabited unconditionally for g = 0. Bring (g = 4) still needs a cover of Σ₄ and Ȟ²(Σ₄, G) ≅ G; no Σ_g model exists in Mathlib or the repo. The 'which band' question remains the owner's; nothing in this bean is closable today.
