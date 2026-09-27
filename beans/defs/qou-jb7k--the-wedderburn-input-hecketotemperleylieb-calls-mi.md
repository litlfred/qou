---
# qou-jb7k
title: The Wedderburn input HeckeToTemperleyLieb calls missing now EXISTS — but in a different Hecke carrier (qou-img9), so the TL ideal equality is engineering, not mathematics
status: todo
type: task
priority: normal
created_at: 2026-09-27T07:42:40Z
updated_at: 2026-09-27T07:42:40Z
parent: qou-weeq
---

Measured 2026-09-27 while looking for the next step after
finrank_traceQuot_eq_catalan (PR #7470). Nothing here is blocked on an owner
decision; it is a measurement that saves the next agent a wrong turn, and it
reframes what is left from MATHEMATICS to ENGINEERING.

## The mathematical input HeckeToTemperleyLieb says it lacks now EXISTS

`QOU/MathlibExt/HeckeToTemperleyLieb.lean` states the arc's open item and prices
its two halves:

  > **Open.** <U_i U_j U_i - v^2 U_i> = traceRadical tr_M ...
  > `subset` is a computation: the trace kills each relator. `superset` says the
  > trace sees *everything* outside the ideal, which is semisimplicity of
  > TL_n(delta) at the relevant delta -- exactly the Wedderburn input this
  > construction was built to avoid needing. The corpus has the positivity half
  > of that (TemperleyLiebTower.yw_pos, terms_zero_of_weighted_sum_zero) and
  > **does not have the block decomposition it would be applied to**. That is
  > genuine mathematics, and it is the whole of what is left.

**It has the block decomposition now.** PR #7470:

  traceQuotEquiv : H_n(q)/rad(wtrace) ~= prod_{l(lam)<=2} M_{f^lam}(R)   general n
  finrank_traceQuot_eq_catalan : (finrank R (H_n/rad) : Z) = catalan (n+1)  general n

both sorry-free. So the sentence above is STALE in its pricing: the Wedderburn
input it calls "genuine mathematics, and the whole of what is left" is supplied.

## But the two do not meet, and the reason is the CARRIER

  - #7470's results are about `QOU.SchurWeyl.Hecke R q q^-1 n`.
  - HeckeToTemperleyLieb's `tlKernel` is a TwoSidedIdeal of
    `HeckeAlgebra R (v^2) M` = `RingQuot (Rel R q M)`
    (MathlibExt/IwahoriHeckeAlgebra.lean:114).

Different RingQuots of different relations. Bridging them is bean **qou-img9**,
and `QOU/IwahoriHecke/CoxeterCarrierEquiv.lean:73` records that qou-img9
"recommends retiring rather than repairing" one of the presentations. So this is
not a lemma away; it is a presentation-consolidation decision.

`QOU/SchurWeyl/HeckeSemisimpleGeneral.lean:69-77` already warns about exactly this
pair and says do not cross them.

## And the relator has NEVER been written in the SchurWeyl carrier

Measured: `grep -rn "U_i U_j U_i\|tlRelator\|TLRel" QOU/SchurWeyl/ QOU/QBeta/`
returns **two hits, both docstrings written in PR #7470 itself**
(WtraceRadicalSemisimple:49, TraceQuotCatalan:33). There is no `U`, no relator, and
no TL-quotient construction in the carrier where the Wedderburn results live.

## So the two honest routes, neither short

**(A) Express the relator in the SchurWeyl carrier and prove it lands in
ker(twoRowProduct).** This needs no bridge and would give the `subset` half
there, hence

    catalan (n+1) <= dim TL_n(delta)      at general n

-- i.e. the LINEAR-INDEPENDENCE half of the planar diagram basis, for free from
the Hecke side, which inverts the usual difficulty (spanning is normally the easy
half). Cost: define `U i := sigma i + 1` in the SchurWeyl carrier and show
`seminormalRep lam (U_i U_j U_i - v^2 U_i) = 0` for every at-most-two-row `lam`.
That is a computation in the Hoefsmit/seminormal matrices and is NOT obviously
short; the classical reason is that the relator is essentially the 3-strand
antisymmetriser, and no antisymmetriser machinery exists in this carrier either.

**(B) Do the carrier bridge (qou-img9).** Would connect #7470 directly to
HeckeToTemperleyLieb's open item and close the `superset` half with the
decomposition already in hand. But qou-img9's own note recommends retiring a
presentation rather than proving an equivalence, so this is a
consolidation decision and not a proof task.

## What NOT to do

Do not read finrank_traceQuot_eq_catalan as progress on the ideal equality. It is
a DIMENSION. The content block hecke-radical-is-temperley-lieb's "a count of
blocks and a count of dimensions are not an isomorphism of algebras" remains TRUE.
What the dimension result removes is the dimension OBSTRUCTION, not the ideal
question.

And do not "fix" HeckeToTemperleyLieb's stale pricing sentence by deleting it --
its `subset`/`superset` split is correct and useful. What is stale is only "does
not have the block decomposition it would be applied to", and the accurate
replacement has to name the carrier, or it will send the next reader to a result
that does not apply.
