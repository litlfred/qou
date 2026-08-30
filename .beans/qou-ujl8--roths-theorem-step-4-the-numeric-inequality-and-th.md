---
# qou-ujl8
title: 'Roth''s theorem step 4: the numeric inequality and the shared parameter record'
status: todo
type: task
created_at: 2026-08-30T06:35:01Z
updated_at: 2026-08-30T06:35:01Z
---

Steps 1, 2 and 3 all now end at the same place: an inequality between explicit constants. This
bean is that inequality, plus the parameter record the three should share instead of each
inventing its own normalisation.

THE INEQUALITY, verbatim from le_index_rational_of_taylor's last hypothesis (RothIndexGap):

  (box)^2 * H * (2B)^{sum r_h} * 2^{sum r_h} * exp(-K(mu - nu))  <  1 / prod_h q_h^{r_h}

with box = prod_h (r_h + 1). Taking logs and writing prod_h q_h^{r_h} = exp(sum_h r_h log q_h),
and using the normalisation r_h log q_h ~ L (so sum_h r_h log q_h ~ mL and K = (2+delta) L):

  log(box^2 H (2B)^{sum r} 2^{sum r}) + mL  <  (2+delta) L (mu - nu).

Step 1 supplies mu ~ m(1/2 - eps) and H via auxHeightBound; step 3 (Roth's Lemma, via
index_le_rothBound) supplies nu ~ eps. So the right side is ~ (2+delta) L m (1/2 - 2eps), which
beats mL for delta > 0 once eps is small -- that IS Roth's inequality, and the m in
card_lt_card_idxBox_of_eps is what makes it available.

WHAT TO BUILD.
1. A parameter record carrying m, eps, delta, r, q, L, K, mu, nu with the relations between them
   (r_h log q_h ~ L, K = (2+delta) L, mu = m(1/2 - eps), the growth clause). RothGammaProducer
   already builds half of this for Gamma_m's clauses and should be retargeted onto it rather than
   kept separate -- two normalisations for one ladder is how correction 26 got in.
2. The inequality itself, discharged from the record.
3. The contradiction: step 2 gives nu <= index at the rational point, step 3 gives
   index <= rothBound < nu. Both are already proved; only the arithmetic of composing them at
   the record's parameters is missing.

Child of qou-br3w. Blocked on nothing.

