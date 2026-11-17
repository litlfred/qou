---
# qou-oyty
title: 'Two Hecke normalisations coexist and give different Ext^1: Z vs Z[i]'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T20:25:30Z
updated_at: 2026-11-17T13:00:03Z
parent: qou-k4oq
---

Found while computing Ext^1 for bean qou-zut2 (2026-08-24). Not a defect in either block on its own — a discrepancy BETWEEN blocks that changes a stated answer, and it is invisible unless the two are read together.

## The two relations

* `QOU/BraidKnot/HeckeAnyonicSubstrate.lean` field `heckeQuadratic`:
  "(T_{s_i} - q)(T_{s_i} + 1) = 0"  -->  eigenvalues q and -1.
* `content/.../knots-particles-confinement/categorical-meson.md`, and the
  Groebner-Shirshov normal-form work generally:
  "sigma_i^2 = h sigma_i + 1" with h = q - q^-1  -->  roots q and -q^-1.

Both are standard Iwahori-Hecke normalisations. They are related by rescaling
the generator, so neither is wrong. But the Ext computation is not invariant
under that rescaling, because it depends on the DIFFERENCE of the eigenvalues.

## Why it changes the answer

QOU/Mathlib/HeckeExtOne.lean proves Ext^1(V_beta, V_alpha) = R / (alpha - beta),
for the rank-one-by-rank-one extension, over any CommRing.

* Convention A (alpha = q, beta = -1): ideal (q + 1), and
  R_q/(q+1) = Z[q,q^-1]/(q+1) = Z  via q |-> -1.
* Convention B (alpha = q, beta = -q^-1): ideal (q + q^-1). In R_q the factor
  q^-1 is a unit, so the ideal is (q^2 + 1), and the quotient is
  Z[q]/(q^2+1) = Z[i] — the GAUSSIAN INTEGERS, not Z.

So `phase-transition-boundary.md`s "Ext^1_{H_n(q)}(V_asym, V_sym) = Z" is
correct under A and false under B. The block does not say which relation it
assumes, and the corpus uses B in the chapter where the normal forms are
actually computed.

The degeneracy loci differ too, which is the physical reading: A degenerates at
q = -1, B at q^2 = -1. Those are different points, so "the non-semisimple locus"
is not a convention-free notion here either.

## What to do

Not mechanical — pick one and say so, or state both. Three options:

1. Declare a normalisation in the substrate (one block, cited by both chapters)
   and mark every Hecke relation elsewhere as a rescaling of it, with the
   rescaling written down. Most work, most durable.
2. Leave both but annotate `phase-transition-boundary.md` with the relation its
   "= Z" assumes. Cheapest honest fix.
3. Check whether the mixed-channel argument actually needs B, in which case the
   answer is Z[i] and the pi_3(S^2) generator claim needs re-examining, since
   Z[i] is not the Hopf invariant group.

Option 3 is the one that could change a physics claim, so it should be checked
before 2 is written.

## Where the evidence is

QOU/Mathlib/HeckeExtOne.lean module docstring states the caveat in full and
proves the general R/(alpha - beta) form deliberately, so neither convention is
baked in. Zero sorries, axiom-clean. This bean exists so the caveat is not lost
in a file docstring.


---

## Option 3 answered 2026-08-24 — the mixed-channel argument needs B, so the answer is Z[i]

Checked, as this bean asked, before writing option 2.

**The block is under B.** `rem:hecke-algebra-from-braiding` is the block that
*defines* H_n(R,q) for this corpus and it writes `(sigma - q)(sigma + q^-1) = 0`.
`rem:phase-transition-interpretation`, the remark interpreting
`prop:phase-transition-boundary` itself, names the channels "Gas (symmetric
channel, eigenvalue q)" and "Solid (antisymmetric channel, eigenvalue -q^-1)".
Convention A appears in a Lean file (`HeckeAnyonicSubstrate`), not in any
content block attached to this claim.

**So the value is Z[i], and the physics claim does change.** Z[i] is Z^2 as an
abelian group with no distinguished generator, so "the Hopf invariant of
pi_3(S^2) = Z generates it" cannot be repaired by naming a convention — it is
false under B and the block is under B.

**And the degeneracy locus is not reachable.** Newly proved sorry-free in
`QOU/Mathlib/ExtensionClass.lean`: `twoQ_eq_zero_iff` (under B the eigenvalue
gap q + q^-1 vanishes exactly on q^2 + 1 = 0) and `twoQ_ne_zero_of_ordered`
plus `heckeSES_isSplit_of_ordered` (over an ordered field it never vanishes, so
the sequence splits at every nonzero q). A degenerates at q = -1; B at q = ±i.
Neither is admissible under `def:substrate-parameter`, and ±i is not real, so
the archimedean side never reaches it.

**Consequence for this bean.** Option 3 is discharged: the claim it was
protecting is withdrawn on `prop:phase-transition-boundary` (status authorNote,
2026-08-24, bean qou-zut2), so option 2 no longer has a live "= Z" to annotate.
Options 1 and 2 remain open as a *general* hygiene item — the two normalisations
still coexist undeclared, and the next block to compute something
eigenvalue-difference-dependent will hit the same fork. Option 1 (declare one
normalisation in the substrate and write the rescaling down) is the durable fix
and is unaffected by the withdrawal.

`HeckeExtOne.lean` keeps every theorem; its module docstring now states which
normalisation each result belongs to, and the two normalisation-A theorems are
labelled as such rather than as "the corpus's".


---

## Reduced to one live item 2026-08-24 — this is now a standing to-do

Owner's call, recorded: keep this open as a to-do to resolve. Options 2 and 3
are closed, so the bean is exactly option 1 and nothing else.

- [x] **Option 3** — check whether the mixed-channel argument needs B.
      Answered above: it does, the value is `Z[i]`, and the claim it protected
      is withdrawn on `prop:phase-transition-boundary`.
- [x] **Option 2** — annotate `phase-transition-boundary` with the relation its
      "= Z" assumes. Moot: there is no live "= Z" left to annotate.
- [ ] **Option 1** — declare ONE normalisation in the substrate, in a single
      block cited by both chapters, and mark every Hecke relation elsewhere as
      a rescaling of it with the rescaling written down.

**Why option 1 survives its own motivating claim.** The withdrawal removed the
*symptom*, not the fork. Convention A lives in
`QOU/BraidKnot/HeckeAnyonicSubstrate.lean` (`(T - q)(T + 1) = 0`) and
convention B in `rem:hecke-algebra-from-braiding` (`(sigma - q)(sigma + q^-1) = 0`);
neither declares itself, and any future computation depending on the eigenvalue
*difference* hits the same divergence with no signpost. `HeckeExtOne.lean`
proves the general `R/(alpha - beta)` form precisely so neither convention is
baked in — that is a mitigation, not a fix.

**Scope when picked up.** One substrate block declaring the relation; a
rescaling note on `HeckeAnyonicSubstrate`'s `heckeQuadratic` field; and a sweep
for other statements of the quadratic. Not urgent, not large, and it stops the
next occurrence rather than annotating it.

### Progress Update (Round 68 — PR litlfred/qou#8356)
- **PR:** https://github.com/litlfred/qou/pull/8356 (`2c058b5e380e076d0aec9233aad57fa6af43d018`)
- **Lean 4 Module:** `QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py` & `computations/probes/bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json` (`COMMIT1 = 8ee314938e6a9bac9ee46faedf9aebdee8b895fb`, `scriptHash = 326bd13833f0`, `allPassed = True`, `dps = 80`)
