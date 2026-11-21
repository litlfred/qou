---
# qou-cvru
title: 'C-5a: does the R-matrix obstruction share the Kummer zero set? (open)'
status: todo
type: task
priority: normal
created_at: 2026-11-15T17:35:00Z
updated_at: 2026-11-21T13:20:00Z
parent: qou-lx8f
---

Open conjecture-level question (keep open per AGENTS §13a). The owner chose
"keep open, scope it" on 2026-11-15. Issue litlfred/qou#7935, PR #7936.

**Question.** C-5 defines κ_n = tr_M(Ř_(n+1) − L₋₁Ř_(n)). Does it vanish
exactly for n | 6, the zero set of the Kummer obstruction χ mod n with χ = −6?

**Proved (PR #7936, `QOU/MathlibExt/KummerObstruction.lean`, sorry-free):**
- `bring_kummerObstruction_eq_zero_iff`: χ mod n = 0 iff n ∣ 6.
- `addMonoidHom_zmod_eq_zero`: every additive map ℤ/n → torsion-free group is 0.
  So the trace (in ℚ(q)) can share the zero set at most. It cannot be the
  class. This is a scope-(b) exclusion for "image under a homomorphism";
  the invariant is torsion-freeness.
- `kappa_eq_sub`: by J-3, κ_n = tr⁽ⁿ⁺¹⁾(Ř') − tr⁽ⁿ⁾(Ř).
- `kappa_eq_zero_of_descended`: κ_n = 0 if Ř' = ℓ_n Ř (e.g. Ř = σᵢ).
- `transient_eq_zero_of_surjective`: the JC-4 (1 − τ̂) form is 0 for every Ř'
  when ℓ_n is onto. Under J-1, ℓ_n is onto at fixed strand count.
- `kummerObstruction_eq_trace_id_mod` (route R1): the Kummer class equals
  tr_M(id) mod n, with C-4b as a hypothesis.

**Blocker.** Ř⁽ⁿ⁾ is defined nowhere, and the brane tower is a jet tower, not a
strand tower. With the relations as written, κ_n ≡ 0.

**Routes** (doc: /mnt/project-files/qou-leftovers/c5a-gap-routes.md):
- R1: done on #7936.
- R2: define a non-jet-image Ř⁽ⁿ⁾, fixed BEFORE computing (anti-fit).
- R3: the gerbe layer, qou-skn4 G1–G2, plus Ȟ²(S, μ_n) ≅ ℤ/n.

## 2026-11-15 (session 01Qmmkt7): G1 started, R3 scoped
- PR #7945 (issue #7944): `QOU/MathlibExt/CechColimit.lean`, sorry-free. Refinement map on Čech H², a colimit `CechH2` over admissible covers, and the T2b lifting obstruction as a cover-independent class (`cechObstruction`, `_indep_lift`, `_pull`, `_eq_one_of_lift`).
- Still open: the converse (trivial in colimit ⇒ lift on a refinement) needs filtered covers (G1b). The scope note's degree-2 injectivity claim was not claimed.
- R3 plan: /mnt/project-files/qou-leftovers/r3-cohomology-route.md. The Kummer class is δ(T_S) for 1→μ_n→𝒪*→𝒪*→1, and δ(L) = deg L mod n. Missing pieces: H²(S,μ_n)≅ℤ/n (no Čech–singular comparison in Mathlib) and the Kummer sequence on a Riemann surface.

## 2026-11-15 R3 conditional theorem (PR #7945)

The Kummer class of C-5a is now a defined colimit class. `cechKummer_eq_map_chern` (sorry-free) proves it is the Chern class reduced mod n. Conditional on `KummerSurfaceData` and deg c₁(T_S) = χ, it is trivial iff n ∣ χ, which for Bring's curve is n ∣ 6. The link to an R-matrix trace is NOT made; that is still R2. This bean stays open.

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
No change: R2 (a non-jet Ř⁽ⁿ⁾ fixed before computing) has no derivation in the corpus. R3 side advanced for g = 0 only (PR #7969). Stays open (rule 13a).

## 2026-11-21 R2 candidates A and B excluded in Lean (PR #8865)

`QOU/SchurWeyl/R2TwistTower.lean` (sorry-free). Candidate A (strand tower, full twist, convention D): κ₁ = (q²−1)(q⁸+q⁶+q⁴+1)/(q²+1)² ≠ 0 for real q ≠ 0, q² ≠ 1, so its zero set is not {n ∣ 6}. Scope (a): this tower with this element only. Candidate B (jet in q): a level-independent κ cannot vanish exactly at n ∣ 6. Scope (b), invariant = level-independence. Candidate C (roots of unity) has the target built in and was not adopted. No candidate realises C-5a, so this bean stays open.
