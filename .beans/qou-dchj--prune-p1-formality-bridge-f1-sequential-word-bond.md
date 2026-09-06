---
# qou-dchj
title: 'Prune P1: formality bridge F1 — sequential word ⇒ bond sum ⇒ b3=0; interleaving breaks it (Lean composition)'
status: completed
type: task
priority: normal
created_at: 2026-09-05T19:14:23Z
updated_at: 2026-09-06T03:19:31Z
parent: qou-2akx
---

2026-09-05: corpus-grep BEFORE writing found F1 already proved in three files (MonotoneWordFactorizes.tr_stabWord_eq_prod_tr; MarkovBondRuleForcesPairwise.b3_eq_zero_of_bondRule; InterleavedCrossTerm.interleaved_sub_sequential) — the research doc's §7 item 1 was my corpus-grep miss. Landed the COMPOSITION as QOU/Mass/FormalityBridgeF1.lean (5 decls, lean-direct exit 0, -DautoImplicit=false, all on propext/Classical.choice/Quot.sound or none): additive_map_one, additive_map_prod, f_tr_stabWord_eq_sum (any multiplicative-to-additive f turns a monotone word's trace into a bond SUM), interleaved_ne_sequential and f_interleaved_ne_f_sequential (with nonzero cross term z(z²−hz−1) the interleaved n=4 word is NOT the bond sum of its letters). Reading: semisimplicity does no work at this step; the ordering hypothesis does. Import cone (OcneanuTrace, InterleavedCrossTerm, MonotoneWordFactorizes, MarkovBondRuleForcesPairwise) had no oleans in the 2026-08-31 cache and was compiled from source first, all exit 0.

Landed on main via #6865 (rebase-merge 321aa5adcd).
