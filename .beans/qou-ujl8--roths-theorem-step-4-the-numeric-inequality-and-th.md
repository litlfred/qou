---
# qou-ujl8
title: 'Roth''s theorem step 4: the numeric inequality and the shared parameter record'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T06:35:01Z
updated_at: 2026-08-30T06:44:19Z
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

## 2026-08-30 -- the collision is built; the record is not, and here is why

QOU/Mathlib/RothContradiction.lean, nine declarations, all axiom-clean, .olean deleted first,
registered in QOU.lean.

ITEM 3 (the contradiction) IS DONE.
  * false_of_le_index_of_rothBound -- the collision itself: a lower bound nu and Roth's Lemma's
    upper bound cannot both hold once c_m^{2^{m-1}} (p/q) drops below nu^{2^{m-1}}.
  * roth_contradiction -- steps 2 and 3 in one place, with both hypothesis lists composed.

WHAT COMPOSING THEM ACTUALLY FOUND. Neither step was missing mathematics; what was missing is
that they had never been written down together, so nothing forced their interfaces to agree.
Three mismatches surfaced only on composition:
  * step 3 states its conclusion with algebraMap Z Q, step 2 with Int.castRingHom Q
    (algebraMap_int_rat);
  * step 3's kappa against step 2's p_h/q_h;
  * step 3's p, q are Gamma_m's RATIO parameters and have nothing to do with the numerators and
    denominators of the approximations, despite the shared letters -- the single most likely
    place for a silent wrong-variable bug in the whole arc.
Correction 26 was exactly a pair of halves each correct that did not compose. Composing early is
the cheapest defence there is.

ITEM 2 (the inequality) IS HALF DONE, deliberately.
  * mul_exp_neg_lt_one_div converts step 2's multiplicative hypothesis
    taylorConst * e^{-K(mu-nu)} < prod_h q_h^{-r_h} into the additive form
    log(taylorConst) + sum_h r_h log q_h < K(mu - nu), which is Roth's inequality as it is
    stated in prose. le_index_rational_of_log is step 2 in that form. Both forms are kept: the
    multiplicative one is what the estimate hands over, the additive one is what a parameter
    choice is checked against.
  * log_taylorConst decomposes the left side into its four named costs: 2 log(box) + log H +
    sum_r log(2B) + sum_r log 2.

AND THAT DECOMPOSITION CHANGES THE RECORD'S SPEC. Every term on the left except log H scales with
sum_h r_h. So the normalisation CANNOT BE ONE-SIDED: r_h log q_h >= L bounds the right side from
below but leaves sum_h r_h log q_h on the left unbounded above. A record carrying only the lower
bound -- which is what I described when I opened this bean, and what RothGammaProducer's growth
clause supplies -- cannot discharge the inequality. It needs L <= r_h log q_h <= L'. Found by
writing the decomposition, not by assuming it.

ITEM 1 (the record) NOT BUILT, on purpose. A record with one consumer is speculative structure,
and roth_contradiction's hypothesis list is the specification such a record has to meet -- now
including the two-sided normalisation above. It earns its place when RothGammaProducer is
retargeted onto it, which is the next step here.

SATISFIABILITY CHECKED, and note this is not the usual vacuity check. roth_contradiction concludes
False, so its hypotheses are SUPPOSED to be jointly unsatisfiable; vacuity is not the risk. The
risk is that some STRUCTURAL subset is already inconsistent, making the theorem true for reasons
having nothing to do with Roth. roth_contradiction_at_witness rules that out by supplying every
structural argument at the index_le_rothBound_witness parameters (m = 2, p = q = 1, F = 10, a = 1,
r = (1,1), H = (1024,1024), P = 1, kappa = 1024, alpha = 1024, G = 0), leaving exactly the two
numeric conditions.

WHAT THAT WITNESS DOES NOT SHOW: the collision does not fire there. At mu = nu = 0 both remaining
hypotheses are false -- and they must be false somewhere, or False would follow from satisfiable
hypotheses. Both holding at once needs mu ~ m(1/2 - eps) from step 1 and K ~ (2+delta)L from an
approximation exponent above 2. That is Roth's inequality itself and is what the record has to
deliver; no small witness can exhibit it.

