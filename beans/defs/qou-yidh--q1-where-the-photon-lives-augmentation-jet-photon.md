---
# qou-yidh
title: 'Q1: where the photon lives — augmentation jet, photon filtration, Frobenius Gram on W'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T10:30:31Z
updated_at: 2026-11-25T11:01:42Z
parent: qou-y2o9
---

2026-11-25: I/I^2 = 0 over Q(q) (proved: PhotonJet.hecke_sub_mul_self/sub_eq_smul_sq); photon not in 1+ker eps (augmentation_photon); lives in affine 1+W, W=span{s0,s1,V}; photon filtration H3 1,4,6 / H4 1,6,15,22,24; gr noncommutative; W->sl2 in reflection block, trace form signature (2,1). PR #9415, docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md. OPEN: categorical reason for gg (braided tensor algebra candidate, untested).

2026-11-25 round 2: PhotonTangent.lean (infinitesimal photons add; Borromean weights forced on R.V); V^3 = gamma(phi)gamma(psi) has exactly the corpus pair over ALL photons at q=3/2,7/5 (not generic proof); gr H3 = T(W)/(R), dim R=7; braided carrier PhotonBraidedConjecture.lean (no instance; gl3/sl2 standard braidings excluded by dimension). Content blocks prop:photon-augmentation-jet, prop:photon-response-determines-q added. OPEN: generic-q uniqueness proof; braiding search.
