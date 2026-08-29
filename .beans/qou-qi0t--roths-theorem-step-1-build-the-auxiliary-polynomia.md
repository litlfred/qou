---
# qou-qi0t
title: 'Roth''s theorem step 1: build the auxiliary polynomial, and thereby audit Gamma_m'
status: todo
type: task
created_at: 2026-08-29T19:34:44Z
updated_at: 2026-08-29T19:34:44Z
---

Roth's Lemma is proved (qou-4lbh) but Gamma_m has never been PRODUCED -- only transported (rename_equiv), descended (rothGammaFull_descend), or hand-built at m=2. Its seven clauses have never been discharged from a Diophantine setup at m >= 3. Mathlib has the engine: NumberTheory/SiegelsLemma.lean (exists_ne_zero_int_vec_norm_le) and NumberField/House.lean. The work is the wiring: encode 'P vanishes to index >= mu at (alpha,...,alpha)' as a linear system over Z in P's coefficients, count equations against unknowns, apply Siegel, and read off the height bound. Treat it as an AUDIT of RothGammaFull, not as construction: if Gamma_m is misstated, index_le_rothBound is a true theorem about the wrong hypothesis -- which is exactly what correction 18 was. Child of qou-br3w.
