---
# qou-533l
title: Formalize Yekutieli central-extension-of-gerbes theorem for the brane tower (tiered)
status: todo
type: feature
priority: high
created_at: 2026-10-12T19:14:51Z
updated_at: 2026-11-27T21:55:00Z
parent: qou-vo9t
---

## Goal
Replace the self-assuming carriers with a derived theorem. Today QOU.YekutieliLifting and QOU.YekutieliLiftingCondition carry "lift exists iff kappa = 0" as structure fields: assumed, not proved. The target is Yekutieli 2010, *Central Extensions of Gerbes* (arXiv 0801.0083), Thm 4.17, proved for the brane tower's actual gerbes.

## Why it is large
Mathlib has no gerbes and no nonabelian H^2. Planned tiers, each sorry-free before the next:
- **T1.** Central extensions of groups 1 -> A -> E -> G -> 1; a lift's obstruction as a 2-cocycle class in H^2(G, A).
- **T2.** Cech level: torsors and lifts over a cover, with a Cech 2-cocycle obstruction.
- **T3.** Gerbes (groupoid-valued) banded by an abelian A, and their central extensions.
- **T4.** Thm 4.17: a lift exists iff the obstruction class vanishes.
- **T5.** Instantiate for the jet-prolongation tower.

## Discipline
- No trivial trues.
- No iff carried as a field.
- Generic R, not Real (AGENTS.md section 7c).
- Each gap gets its own bean.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch B):** in-progress → todo. Stale claim (session ended); work not finished — see docs/coordination/2026-11-20-dangling-claims-proposal.md.

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Tier status on main: T1 (CentralExtensionObstruction), T2/T2b (PresheafCentralExtensionObstruction, CechCentralExtensionObstruction), T3 partial (StackGerbe M1–M3, CechGerbe cocycle form, Čech colimit, S² comparison). T4 holds at cocycle level only, with gerbe ≃ cocycle assumed. T5 (jet tower) is moot as stated: the jet-tower perpetual obstruction was retracted for the degree condition (qou-lx8f, 2026-11-15). Open conjecture-level feature; stays todo.

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Tier status unchanged since 2026-11-21 (no commits to CentralExtension*/Cech*/StackGerbe* since 2026-11-20). The self-assuming carriers YekutieliLifting / YekutieliLiftingCondition are still the reason for the bean.

## 2026-11-27 (thread "Build the brane-tower gerbes", PR #9730)

T1 lifted from cochains to a class. `MathlibExt/CentralExtensionH2.lean` builds `H2 H A` (trivial-action cocycles mod coboundaries, a CommGroup), `obstructionClass`, `obstructionClass_section_indep` and `obstructionClass_eq_one_iff` (lift iff class = 1). `QOU.YekutieliLiftingCondition.ofCentralExtensions` (block def:yekutieli-lifting-condition) discharges both fields of the definition from that theorem for any tower of central group extensions. Sorry-free, standard axioms.
Next: retire the self-assuming `QOU.YekutieliLifting` carrier (prop:yekutieli-lifting); its `persistence` field is the retracted jet-tower claim (qou-lx8f).

## 2026-11-27 owner ruling

Carl chose "Both: conditional now, build 4.17" (card in thread "Build the brane-tower gerbes"): merge the conditional restatement of prop:yekutieli-lifting (PR #9755; group-level lift_iff derived, persistence a hypothesis) AND keep building stack-level Yekutieli Thm 4.17 (next: gerbe vs 2-cocycle, qou-0xk8; central extension of gerbes, Def 3.21).
