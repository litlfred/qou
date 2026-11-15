---
# qou-s4xb
title: 'Furey C⊗O minimal left ideals: formalise and test tower flavour/chirality embedding'
status: in-progress
type: task
priority: normal
created_at: 2026-11-15T10:23:47Z
updated_at: 2026-11-15T11:01:41Z
parent: qou-8lxd
---

Stream 15 (coordinator session_01M5GA1LmsEf8tSMxFjMkmnn). Formalise C⊗O (generic char-0 field with sqrt(-1)), Witt nilpotents alpha_i, idempotent omega omega^dagger, minimal left ideal S_u; prove dim 8, ladder, 1+3+3bar+1 under su3 e1. Then test whether tower data (quark letter h^1 part, eigenlines P±, flavour bit) embeds FORCED. Branch claude/furey-cxo-ideals-2026-11-15. Session https://claude.ai/code/session_01Qmmkt6KDV9jaJ1LRwuxmDp


## Result (2026-11-15, PR #7872)
Verdict (c). Lean sorry-free: FureyMinimalLeftIdeal.lean (CAR, omega omega-dagger rank one onto Omega=1+i e1, Fock ladder, L(e1) = -i(-1)^N) and FureyIdealTowerTest.lean (S_u dim 8 + minimal, su3 stdIm invariants = span(nu,e+), levels 1/2 preserved; tests: colourBlind_lands_in_singlets, forced_chirality_embedding (b up to scale + i<->-i, image leptonic), flavour_obstruction (S_u<->S_d is G-odd), no_sqrt_neg_one_of_ordered). Extra choices: (1) tower colour index = stream-6c bridge; (2) the root i; (3) a G-odd flavour identification. Audit: docs/audits/2026-11-15-furey-cxo-ideal-embedding-test.md. Missing sources for stream 13: ingest uploads/1806.00612v1.pdf; Furey PLB journal paper(s) not held.

## Triplet irreducibility (2026-11-15, owner pick "prove triplets irreducible")
Added to FureyIdealTowerTest.lean, sorry-free, axioms propext/Classical.choice/Quot.sound only:
`triplet_core` (abstract weight argument), `octDer7/10/11_mem`, `octDer_fock_action`,
`level1_decomp`/`level2_decomp` (each level = span of its three Fock vectors), and
`level1_irreducible`/`level2_irreducible` (every nonzero su3-stable subspace meeting a level
contains all three Fock vectors). Over any char-0 field with i*i = -1. Verdict unchanged.
