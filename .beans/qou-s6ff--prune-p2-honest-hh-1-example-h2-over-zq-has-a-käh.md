---
# qou-s6ff
title: 'Prune P2: honest HH_1 example — H2 over Z[q^±] has a Kähler degree, inverting [2]_q kills it (Lean)'
status: completed
type: task
priority: normal
created_at: 2026-09-05T19:14:23Z
updated_at: 2026-09-05T19:14:23Z
parent: qou-2akx
---

2026-09-05: QOU/Hecke/H2KaehlerDegrees.lean (8 decls, lean-direct exit 0, -DautoImplicit=false, all on propext/Classical.choice/Quot.sound, 0 sorry). A_h := R[X]/(X²−hX−1) (= InstanceH2.H2 at h=q−q⁻¹). Proved: x_sq; two_x_sub_h_sq: (2x−h)² = h²+4 (= [2]_q² at the Hecke parameter, two_x_sub_h_sq_hecke); kaehlerIdeal_eq_top_of_isUnit: h²+4 unit ⇒ (2x−h)=A_h (fibre: Ω¹=HH_1=0); kaehlerIdeal_ne_top_of_hom: a ring hom to a field with h²+4 ↦ 0 (and 2≠0) ⇒ (2x−h) proper (tower: Ω¹=HH_1≠0), e.g. Z[q^±]→C, q↦i; kaehlerIdeal_eq_top_of_qint_ne_zero / kaehlerIdeal_ne_top_of_fourth_root in the corpus's own H2(q). CITED not proved: HH_1(A)=Ω¹_{A/R} for commutative A (HKR deg 1; Weibel 9.4.3) and Ω¹ of a monogenic algebra = A/(f'). n=2 only. Does not replace the vacuous centralIdempotent_idem; complements it.
