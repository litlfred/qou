---
# qou-ujl8
title: 'Roth''s theorem step 4: the numeric inequality and the shared parameter record'
status: completed
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

WHAT COMPOSING THEM FOUND -- and a correction to my own first report of it.

I first wrote, in the module header, the bean and the commit message, that composing the two steps
"surfaced three mismatches": algebraMap Z Q against Int.castRingHom Q, kappa against p_h/q_h, and
Gamma_m's ratio parameters p,q against the numerators and denominators of the approximations.
That was an over-claim and it is now corrected in place.

I tested it rather than leaving it asserted: deleting the rewrite that bridged algebraMap and
Int.castRingHom and rebuilding shows the file STILL COMPILES. The two unify definitionally; there
was no mismatch and the rewrite was not load-bearing. It has been removed and algebraMap_int_rat
kept as a recorded check with the correction in its docstring. The kappa "mismatch" was likewise
not one -- I wrote roth_contradiction's hypothesis as InRothFracSet Hh (fun h => p_h/q_h), forcing
the two to agree by construction rather than discovering anything. The p,q overloading is a real
trap for a reader and was navigated by naming step 2's data pn, qd, but nothing about it failed.

THE HONEST REPORT is that the two halves fit as they stood. That is the good outcome, and it is
worth stating as an outcome rather than dressed up as a discovery. The reason the expectation was
the opposite is correction 26, which WAS a pair of halves each correct that did not compose;
composing early remains the cheapest defence, and this time it found nothing to fix.

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

## 2026-08-30 -- the record is not needed: rothDegrees was already two-sided

QOU/Mathlib/RothNormalisation.lean, six declarations, all axiom-clean, .olean deleted first,
registered in QOU.lean.

THE FINDING. Last entry concluded that a one-sided normalisation cannot discharge step 4's
inequality and that the record must carry L <= r_h log q_h <= L'. I expected that to be a NEW
obligation on whatever supplies the degrees. It is not. rothDegrees H N h is log_{H_h} N (plus one
off the first coordinate), and rothDegrees_log_bounds proves

    log N - log H_h  <=  r_h log H_h  <=  log N + log H_h

for every h -- the two-sided normalisation, with L = log N - max_h log H_h and
L' = log N + max_h log H_h. Gamma_m's growth clause consumes the lower half; step 4's inequality
needs both; they are the SAME construction. So the worry that opened this bean -- two
normalisations for one ladder, the shape correction 26 had -- was unfounded. The fix is to record
that they coincide, not to introduce a record reconciling them.

ITEM 1 (the record) IS THEREFORE SCRAPPED, with two reasons rather than one:
  * there is nothing to reconcile, per the above;
  * a structure : Prop carrier is exactly taxonomy row 19, which I opened myself: such carriers
    are invisible to every detector in the 17-detector suite, so a false or over-strong clause
    inside one goes unflagged. With a single consumer the packaging buys nothing and re-creates
    the blind spot I documented.
The normalisation stays as explicit hypotheses.

ITEM 2 (the inequality) IS DONE, reduced to checkable conditions.
  * log_taylorConst_le -- the polynomial's total size is at most theta * sum_h r_h log q_h from
    ONE per-coordinate condition, 2 + c_H + log(4B) <= theta log q_h. That is Roth's "choose the
    q_h large" in exactly the form the estimate consumes.
  * log_condition_of_cost -- closes the additive inequality against (1+theta) m L' < K(mu-nu).
  * roth_contradiction_of_normalisation -- step 4 with its additive hypothesis replaced by data a
    parameter choice can be checked against.

WHAT DOES NOT TRANSFER, and this is the one asymmetry worth carrying forward. Step 4 wants bounds
on r_h log q_h; rothDegrees is built from the HEIGHTS H_h = max(|p_h|, q_h). The UPPER half
transfers free because q_h <= H_h (rothDegrees_log_bounds_den). The LOWER half does not: H_h <= q_h
fails whenever the numerator dominates. height_le_den identifies exactly what recovers it --
|p_h| <= q_h -- and proves it, including the wrinkle that it is the REDUCED fraction's height
(2/4 has height 2, not 4), so it is an inequality and not the equality H_h = q_h one expects.
In Roth's setting |p_h| <= q_h is the harmless consequence of approximating a number of absolute
value at most 1, but it is a hypothesis on the approximations and not a consequence of the degrees.

STILL NOT SHOWN, unchanged and now argued rather than asserted: the collision does not fire at
any small witness. I checked why. With alpha = 0 and beta_h = 1/q_h the approximation exponent is
1, so K <= L and hlog needs (1+theta) m L' < L(mu - nu) -- impossible for mu <= m and theta,nu >= 0.
More generally ANY rational alpha = a/b has |p/q - a/b| >= 1/(qb), capping the exponent at
1 + log b / log q, so K stays at or below L up to a bounded factor. Roth needs exponent 2 + delta,
which forces alpha irrational, and certifying an index at an irrational alpha is step 1's
non-constructive Siegel argument. A firing witness is not reachable by construction, not merely
expensive.

## 2026-08-30 -- item 2 finished: "take m large", and what it costs

slack_pos / exists_m_of_slack / hfin_of_large finish the discharge. Substituting the standard
relations K = (2+delta)L, L' = (1+eta)L, mu = m(1/2 - eps) turns the last inequality into

    (2+delta) nu  <  m * [ (2+delta)(1/2 - eps) - (1+theta)(1+eta) ],

so everything hinges on the bracket, and slack_pos says exactly when it is positive:

    (2+delta) eps + theta + eta + theta*eta  <  delta/2.

THE APPROXIMATION EXCESS delta/2 PAYS FOR ALL THREE SLACKS, and they are of different origin:
eps is how far step 1's index falls short of m/2; eta is how far the normalisation is from exact;
theta is the auxiliary polynomial's share of the denominators' size. Only after the bracket is
positive is m free, and exists_m_of_slack is then pure Archimedes -- the ONE place in the whole
theorem where "sufficiently large" is used for its Archimedean content rather than as shorthand
for a counting bound.

Writing it out is what made the four constants comparable. Before it eta had no budget at all: it
entered only when rothDegrees turned out to be two-sided, and nothing said how tight the two sides
had to be relative to delta. Now delta/2 pays for it, explicitly.

exists_m_of_slack was written with 0 <= nu; the linter reported it unused and it is -- exists_nat_gt
does not care. Stronger statement kept.

## Summary of Changes

QOU/Mathlib/RothContradiction.lean (9 declarations) and QOU/Mathlib/RothNormalisation.lean
(9 declarations), all axiom-clean [propext, Classical.choice, Quot.sound], each built with the
.olean deleted first, both registered in QOU.lean.

  * ITEM 3 (the contradiction) -- false_of_le_index_of_rothBound and roth_contradiction. Steps 2
    and 3 bound the same index from below and above; the collision is where Roth's theorem is.
    Composing them surfaced no interface mismatches; my first report said it had, and that was
    tested and corrected in place.
  * ITEM 2 (the inequality) -- mul_exp_neg_lt_one_div gives the additive form, log_taylorConst
    names the four costs, log_taylorConst_le reduces them to one per-coordinate condition,
    log_condition_of_cost closes the inequality, and slack_pos / exists_m_of_slack / hfin_of_large
    discharge the remainder with the slack budget delta/2 > (2+delta)eps + theta + eta + theta*eta.
  * ITEM 1 (the record) -- SCRAPPED, see below.

## Reasons for Scrapping (item 1 only, not the bean)

Two, and the first is the substantive one.

1. There was nothing to reconcile. The bean was opened on the worry that RothGammaProducer and
   step 4 would need different normalisations -- the shape correction 26 had. rothDegrees_log_bounds
   shows rothDegrees H N h = log_{H_h} N already puts r_h log H_h within log H_h of log N on BOTH
   sides. Gamma_m's growth clause consumes the lower half, step 4 needs both, same construction.
2. A structure : Prop carrier is taxonomy row 19, which this arc opened: invisible to every
   detector in the 17-detector suite. With one consumer the packaging buys nothing and re-creates
   a blind spot we documented.

## Deferred, with a home

roth_contradiction_of_normalisation still takes hgap (the ratio Gamma_m supplies is below
(nu/c_m)^{2^{m-1}}) and the step-1/step-3 suppliers of mu and nu as hypotheses. Assembling those
into the final statement of Roth's theorem, and then step 5 (not LiouvilleWith), is qou-br3w.
The O_K coefficient ring is qou-86j4. No small witness can make the collision fire, and the reason
is now argued rather than asserted: any rational alpha caps the approximation exponent near 1, so
K stays at or below L; exponent 2 + delta forces alpha irrational, and certifying an index at an
irrational alpha is step 1's non-constructive Siegel argument.

