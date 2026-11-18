---
# qou-ogj5
title: 'Assess: is the quantum-gravity claim GR or analogue/acoustic gravity'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T18:08:47Z
updated_at: 2026-10-04T15:11:54Z
parent: qou-ddmn
---

MEASURED (subagent + own verification). THE FINDING: 'G' IS A GLYPH COLLISION. Two propositions assert the IDENTICAL formula alpha = m_e * 8G with two different G. prop:binding-scale-catalan (mass-theory/binding-scale-catalan.md:20-26) says G = CATALAN'S CONSTANT 0.9159655941772190 and Vol(B_3) = 8G is the Borromean hyperbolic volume — which is a correct, sorry-free theorem of hyperbolic geometry. prop:gravity-spectral-prefactor (observations/gravity-spectral-prefactor.md:7) says 'G is NEWTON's gravitational constant in Planck units (G_Planck = 1)'. VERIFIED NUMERICALLY MYSELF: m_e*8*Catalan = 3.744459659941610 MeV vs corpus's quoted 3.7445 (err 4.0e-5); m_e*8*1 = 4.08799160552 MeV (err 0.343). The number is CATALAN. Newton's G is ABSENT from the repo: no witness, no producer, no CODATA comparison, no 6.674 anywhere; gravity-spectral-prefactor.lean:29 DEFINES newtonG U := U.alpha/(8*U.m_e) and then 'proves' alpha = m_e*8*newtonG U by field_simp — i.e. x = y*(x/y). The corpus's OWN adversarial watcher already caught it: gravity-spectral-prefactor.qa.json carries THREE criteria at result=fail severity=critical (da-hidden-dof, da-empirical-fragility, da-physical-implausibility), reviewed 2026-07-07 sha 3d013432, note 'Severe numerology / post-hoc rationalization suspected... The factor of 8 appears fitted.' Still live. NO EINSTEIN EQUATIONS: GaugeTheory.lean:159 makes the Einstein equation a CLASS FIELD and :198 projects it; einsteinTensor/stressTensor are typed (1_C) -> (1_C), i.e. SCALARS, not rank-2 tensors. categorical-action.lean:88 proves it with the proof term 'id'. NO GRAVITON (2 mentions: one about Penrose's own CCC, one inside a conjecture). NO BACKREACTION (no equation lets stress-energy determine a metric). ZERO gravitational observables: post-Newtonian 0, light deflection 0, redshift 0, perihelion 0, PPN 0, Shapiro 0. The 'gravity' present is UNCITED analogue/acoustic gravity (Unruh's metric verbatim; no Unruh/Visser/Barcelo/Liberati entry in references.ts). Corpus's own honest line: swampland-connections-intro.md:3 'This paper does not model quantum gravity.' VERDICT: not quantum gravity, not gravity; analogue-gravity vocabulary over a glyph collision.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
