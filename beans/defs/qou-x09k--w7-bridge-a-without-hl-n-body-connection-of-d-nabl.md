---
# qou-x09k
title: 'W7: Bridge A without hL (n-body connection of D_nabla, local monodromy, colour singlets)'
status: in-progress
type: task
created_at: 2026-11-22T22:17:23Z
updated_at: 2026-11-22T22:17:23Z
parent: qou-ywyq
---

Workstream W7 of the L2 1-ppQ plan (docs/coordination plan 2026-11-22). New Lean file QOU/Mass/BridgeAStokesNBody.lean: P1-P3 n-body form = KZHolonomy.kzForm (kappa = beta/2, c = -alpha/beta); its generator monodromy = kzBraidRep, conjugate to Jimbo, Hecke quadratic; lagrangian_gauge_to_KZ_of_stokes replaces hL by the named assumption StokesToBraiding; colour singlets: (X+1)(X-q^-2)=0 and singlet_exterior_iff under named ColourTubeBraided. Sorry-free, axioms propext/choice/Quot.sound only.
