---
# qou-xsv8
title: 'ROAST: prf:quantum-dilogarithm-stratified Step 1 pairing is diagonal, not anti-diagonal'
status: in-progress
pr: 8217
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-26T05:27:06Z
updated_at: 2026-10-04T15:13:50Z
parent: qou-r9ih
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


---

## RESOLVED — all three fix steps. And the open thread is closed: YES, same defect.

**Step 2 first, since it was the thread I left open.**
`spectral-sequence-collapse-proof.md`'s *"Frobenius duality of strata"* paragraph
**has the same defect**. It asserts `(J^ℓ)^⊥ = J^{N−ℓ}` and calls it "Poincaré
duality of curvature-rank strata", then the next paragraph reads those strata off
the central idempotents. Refuted in place, scope (b).

**Step 1.** `prf:quantum-dilogarithm-stratified` Step 1's displayed condition read
`⟨Z^(k), Z^(ℓ)⟩ = 0 whenever k + ℓ ≠ N`. Corrected to **`whenever k ≠ ℓ`**.

**The correction REPAIRS Step 4 rather than breaking it — the finding I did not
expect.** Step 4 argues that `φ_q^(k) ∈ Z^(k)` pairs to zero with any `T_w` whose
`Z^(k)`-projection vanishes. That is exactly the *diagonal* statement. Under the
old anti-diagonal condition the pairing was licensed to be **non**-zero at
`ℓ = N − k`, so Step 4's truncation did not follow from Step 1 as written whenever
`N − k ≤ k_⋆(T_w)`. So this defect class does not automatically cost anything
downstream.

**Step 3.** Added as **question 5** of `da-arity-conflation` in
`local/devils-advocate-watcher`: *"Transported to a basis that destroys the
property?"* — a structural property of a pairing is relative to a basis, so check
the new basis's own multiplication before restating it there.

**Measured, not just argued.** `computations/probes/centre_frobenius_pairing_is_diagonal_probe.py`
computes the Gram on `Z(H_3(q))` in the idempotent basis, exact in ℚ(q), **without
multiplying in the algebra** — via `τ(T_u T_v) = δ_{u,v⁻¹}`, so `τ(xy) = Σ_u a_u b_{u⁻¹}`
needs only the inversion permutation on `S_3`. That makes it independent of the
source probe's own orthogonality assertion A2 rather than a re-reading of it.
All 6 off-diagonal entries identically `0`; diagonal
`1/(q⁶+2q⁴+2q²+1)`, `2q²/(q⁴+q²+1)`, `q⁶/(q⁶+2q⁴+2q²+1)`, all nonzero;
completeness self-test `Σ_λ τ(e_λ) = 1` exact — which validates both the τ-rule
and the committed coefficients at once.

**A second refutation I built and then discarded — recorded because it is the same
error this bean is about.** `gbDepth_pos` (sorry-free) proves the partition grading
never occupies degree 0, and at `n = 4` the occupied degrees are `{3,4}`, so the
partners `{1,0}` required by `ℓ ↔ N−ℓ` are both empty. Decisive-looking, and
**wrong**: it assumes `N` is the top *occupied* degree. `N` is not pinned by the
block, and `{3,4}` is symmetric about `3.5`, so `N = 7` pairs `3 ↔ 4`. I nearly
committed a shape-vs-object error inside the correction of a shape-vs-object error.

**Incidental, riding along** (same rule, same files): two P4:date-ref voice
failures and one pre-existing crash-class `…` at
`quantum-dilogarithm-stratified-proof.md:206`. Dates moved to `authorNotes` per
AGENTS.md §4d, including the pre-existing `**Gap (2026-08-16)**` note.

Audit: `docs/audits/2026-08-26-frobenius-duality-of-strata-is-diagonal.md`.

**Not claimed:** that either block's conclusion is false (scope (a) on the step —
the truncation identity and the *Practical consequence* both survive); nor that
`(J^ℓ)^⊥ = J^{N−ℓ}` fails on the whole algebra `A`, which is a different claim.
**Still open:** Step 4 pairs a central `φ_q^(k)` against a general `T_w ∈ A`, so
"zero projection on `Z^(k)`" has to be read block-wise. Plausible, unstated, not
repaired here.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (2026-11-16T22:04:01Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/SteepestDescentEulerMaclaurinAndFrobeniusDiagonal.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/steepest-descent-euler-maclaurin-and-frobenius-diagonal.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8217 (`f4d145a08828886b4eba631166b3e61717adc12d`); keeping `status: in-progress` until PR merges.
