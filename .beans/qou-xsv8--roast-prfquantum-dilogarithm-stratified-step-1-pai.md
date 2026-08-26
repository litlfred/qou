---
# qou-xsv8
title: 'ROAST: prf:quantum-dilogarithm-stratified Step 1 pairing is diagonal, not anti-diagonal'
status: todo
type: task
priority: normal
created_at: 2026-08-26T05:27:06Z
updated_at: 2026-08-26T05:28:20Z
---

Found by the F5 agent (`qou-09e0`) as an unplanned second result while
excluding GS-definable filtrations. Not what it was sent to look for.

## The finding

`prf:quantum-dilogarithm-stratified` Step 1 transports an **anti-diagonal
annihilator duality** from the whole algebra to the centre's **idempotent
strata**. But distinct central primitive idempotents annihilate each other:
`e_lambda * e_mu = 0` for `lambda != mu`. So the pairing restricted to the
idempotent basis is `diag(phi(e_lambda))` -- **diagonal**.

There is no "Poincare duality of curvature-rank strata" on the centre.

## THE ROAST

**1. It is a different defect class from the other five, and that is the
point.** The five `wpdb` consumer sites are broken because they cite a bridge
that does not exist. This one uses **no word filtration at all**. So supplying
the bridge -- the thing three sessions have now been spent on -- **would not
repair it**. Anyone draining the `wpdb` backlog would have marked this site
fixed and moved on.

**2. The error is a structure-transport with no check that the structure
survives.** Anti-diagonality is a property of a pairing on a basis where
elements pair ACROSS. Idempotents are the opposite: they are mutually
annihilating, so the only surviving pairings are self-pairings. Transporting
"anti-diagonal" onto that basis is not a subtle slip; it is asserting a
property of exactly the structure that the basis destroys.

**3. Nobody caught it because it reads well.** "Poincare duality of
curvature-rank strata" is an appealing sentence. It appears in
`spectral-sequence-collapse-proof.md` too, in the same register. The corpus's
own §"da-arity-conflation" criterion exists for precisely this -- a claim whose
SHAPE is not checked against the object it is made about -- and it was not
applied here.

**4. It is adjacent to a defect I corrected earlier tonight.** The
spectral-sequence collapse block carries a Frobenius-duality paragraph in the
same style. I renamed the vacuous theorem in that file and did NOT check
whether its duality prose has the same problem. **That is an open thread I
created and did not close.**

## What this does NOT mean

Not that the quantum-dilogarithm result is false. The refutation is of Step 1's
STATED justification, not of its conclusion. Whether the conclusion survives on
another route is untested. Do not let this be read as a broader refutation than
it is -- AGENTS.md's (a)/(b) rule applies: this is scope-(a) on the STEP.

## Fix

1. Re-scope Step 1 to what the diagonal pairing actually gives.
2. **Check whether `spectral-sequence-collapse-proof.md`'s Frobenius-duality
   paragraph has the same defect** -- I flagged it and did not check.
3. Add "anti-diagonal duality transported to an idempotent basis" to the
   `da-arity-conflation` worked examples; it is a clean instance.
