---
# qou-yidh
title: 'Q1: where the photon lives — augmentation jet, photon filtration, Frobenius Gram on W'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T10:30:31Z
updated_at: 2026-11-25T15:32:57Z
parent: qou-y2o9
---

2026-11-25: I/I^2 = 0 over Q(q) (proved: PhotonJet.hecke_sub_mul_self/sub_eq_smul_sq); photon not in 1+ker eps (augmentation_photon); lives in affine 1+W, W=span{s0,s1,V}; photon filtration H3 1,4,6 / H4 1,6,15,22,24; gr noncommutative; W->sl2 in reflection block, trace form signature (2,1). PR #9415, docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md. OPEN: categorical reason for gg (braided tensor algebra candidate, untested).

2026-11-25 round 2: PhotonTangent.lean (infinitesimal photons add; Borromean weights forced on R.V); V^3 = gamma(phi)gamma(psi) has exactly the corpus pair over ALL photons at q=3/2,7/5 (not generic proof); gr H3 = T(W)/(R), dim R=7; braided carrier PhotonBraidedConjecture.lean (no instance; gl3/sl2 standard braidings excluded by dimension). Content blocks prop:photon-augmentation-jet, prop:photon-response-determines-q added. OPEN: generic-q uniqueness proof; braiding search.

2026-11-25 round 3: PhotonAssertions.lean (all sorry-free): markov_trace_photon, flipReverse_photon, reflection block + Gram det, independent_of_rep, borromean_weights_forced_of_rep. §9: theta.rho stabilises W and is trace-invisible; theta maps W to its mirror W' (chirality invisible to traces); (l,G) symmetry SO(1,1) at q0 (q^4<2), broken by cubic trace; F1 normaliser = centre. §10 status table. NEXT: a concrete Lean model of H3(q) would turn every 'measured' row into a theorem.

2026-11-25 round 4 (owner: 'Fix - no lean model of H3(q)'): HeckeH3Model.lean, regular representation over any comm ring; model_rel, F1_independent, one_V_V2_independent (any ring), borromean_weights_forced_model, commutator_not_mem_F1, mirror_not_mem_W, electron_eq, normaliser_F1_central — all sorry-free. Remaining measured-only: general 6-weight factorisation uniqueness (symbolic Groebner over Q(h) running), dim R=7, continuous symmetry, Gassmann counts.

2026-11-25 round 5: CORRECTED my claim that the two-photon factorisation of V^3 is unique over all photons; Singular shows 8 points, 2 real extra at q0. #9415 head 4635901077.

2026-11-25 round 6: L(n)=floor(n^2/4) for n=3..6 (conj); bounds proved on paper, Lean core; external discussion part 2 not incorporated. PR #9427 stacked on #9415.
