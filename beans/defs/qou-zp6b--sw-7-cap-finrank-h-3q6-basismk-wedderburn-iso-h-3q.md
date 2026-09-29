---
# qou-zp6b
title: 'SW-7-cap: finrank H_3(q)=6 (Basis.mk) + Wedderburn iso H_3(q)≅ℝ×ℝ×M₂ (R2-inst n=3)'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:48:12Z
updated_at: 2026-08-11T00:14:26Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

Both dim bounds now PROVEN sorry-free (span_sixWords_eq_top dim≤6; sixWords_indep dim≥6, qou-pymd closed). Capstone: (1) sixFamily : Fin 6 → H_3(q) := ![1,σ0,σ1,σ0σ1,σ1σ0,σ0σ1σ0]; span(range)=⊤ via sixWords⊆range + span_mono + span_sixWords_eq_top; LinearIndependent ℝ sixFamily via Fintype.linearIndependent_iff + Fin.sum_univ_six + sixWords_indep — NOTE the Fin-6 cons-index reduction (![...] k for k=2..5) is the fiddly bit (cons_val_zero/one/head_cons only reach 0,1; use Matrix.cons_val_succ / show / decide for 2..5). (2) Basis.mk hli hsp ⇒ finrank_eq_card_basis ⇒ finrank=6. (3) Package ρ=(triv,sign,seminormalRep21):H_3(q)→ℝ×ℝ×M₂ as AlgHom.prod; injective (ker=0 from indep on basis) + surjective (dim count 6=6) ⇒ AlgEquiv = R2-inst at n=3. Ref: [kassel1995].
