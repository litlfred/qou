---
# qou-7ue5
title: homflypt_2strand returns the v -> v^-1 MIRROR of this module's own reference — owner convention call
status: completed
type: task
priority: normal
created_at: 2026-08-21T21:14:35Z
updated_at: 2026-08-21T21:28:50Z
---

## The discrepancy (measured 2026-08-21, found while deriving braid index 6_1)

`homflypt_engine.homflypt_2strand([1,1,1])` returns

    -v^-4 + 2v^-2 + v^-2 z^2

`homflypt_reference_qa._torus_homfly`, in the SAME module family, derives
closure(sigma_1^k) from the skein relation by hand and its docstring states

    P(sigma_1^3) = 2v^2 - v^4 + v^2 z^2      (right trefoil 3_1)

These are exactly v -> v^-1 of each other. Its recurrence
P(k) = v^2 P(k-2) + v z P(k-1) is the standard positive-crossing resolution
of Lickorish v^-1 P(L+) - v P(L-) = z P(L0), and an independent exact skein
engine written this session (computations/homfly_skein_braid.py) agrees with
the REFERENCE, reproducing unknot / Hopf / 3_1 / 4_1 / 5_1 textbook values and
passing Conway P(v=1,z)=grad(z) on seven knots.

## Why it survived

homflypt_reference_qa's own docstring says the path under test is
_homflypt_nstrand_numerical (n>=3). It never exercises homflypt_2strand. So
the module's independent reference and its symbolic 2-strand path have never
been compared to each other.

The k=3 branch also carries this, in shipped code:

    # Right-hand trefoil: P = -v^-4 + v^-2 z^2 + 2v^-2
    # Wait, let me use the correct Lickorish convention.

i.e. it was noticed mid-authoring and not finished. Two more unresolved notes
sit further down ('wait, this uses q not (v,z)', 'delegate to the n=3+
Wedderburn path once implemented').

## Two further facts about that function

- It is a hardcoded lookup table over k = sum(signs), NOT the formula
  P = v^-k [omega_2 q^k + omega_11 (-q^-1)^k] its docstring states.
- It raises NotImplementedError for |k| > 3.

## Why I did NOT flip it

- It is a convention call in a shared numerical module with five importers.
- Its self-test enshrines the mirrored values, so any correct flip also
  rewrites the test's asserted constants.
- This repo has a documented, costly history of convention flip-flops
  (the C/D saga). A unilateral sign flip by a passing agent is exactly the
  move that history argues against.
- Blast radius is genuinely ZERO either way: homflypt_2strand and
  homflypt_from_braid have no consumers anywhere in the corpus (measured).
  So there is no urgency, only a correctness question.

## What WAS fixed on branch claude/reeb-flow-tetraplectic-q2460a (PR #5380)

homflypt_from_braid's n>=3 branch, a separate and unambiguous defect: it
evaluated numerically at q_0 and returned LaurentPoly2({(0,0): <float>}), a
degree-zero constant typed as a polynomial, so a v-degree read gave spread 0
with no error. For MFW that is worse than a crash -- 'braid index >= 1' is
consistent with every hypothesis. Now raises, pointing at homfly_skein_braid.
Zero consumers, and the self-test never exercises n>=3, so no risk.

## Decision needed from the owner

Which v-convention is intended for the symbolic path. If it is the reference's
(the textbook one), homflypt_2strand's table and _self_test's expected values
both need the mirror applied, and the module docstring's 'v = a^-1' note should
say which of the two it means.


## 2026-08-21 — LEAN-VALIDATED. It is a mirror, and the z-sign is the point.

QOU/Knot/HomflySkeinReference.lean (sorry-free, axiom-clean, generic Field
per §7c) formalises the reference recurrence and proves:

    engine_k2_is_mirror   v^-3/z - v^-1/z - v^-1 z  =  skein(v^-1, -z) 2
    engine_k3_is_mirror   -v^-4 + 2v^-2 + v^-2 z^2  =  skein(v^-1, -z) 3

So homflypt_2strand is NOT wrong about the polynomial. It computes the LEFT
trefoil and the NEGATIVE Hopf link while LABELLING them 'Right-hand trefoil'
and 'Hopf link (positive)'. The defect is the label + the crossing-sign
convention, not the algebra.

### Correction to this bean's own earlier text

I wrote that the two differ by 'exactly v -> v^-1'. That is WRONG in general.
The HOMFLY mirror is (v, z) -> (v^-1, -z). It looks like plain v-inversion at
k=3 only because z occurs there as z^2; at k=2 the reference's +vz must become
-v^-1 z, and plain inversion gives the wrong sign.

Proved both ways, so the accident is on the record beside the refutation:

    plain_inversion_ne_mirror            skein(1/2, 1) 2 != skein(1/2, -1) 2
    plain_inversion_eq_mirror_at_three   skein(1/2, 1) 3  = skein(1/2, -1) 3

Independently confirmed against the actual Python table at v=2, z=1:
k=2 engine = mirror = -7/8, naive = +7/8 (DIFFER); k=3 all three = 11/16.

### Scope

NOT proved: anything geometric. That a crossing switch on sigma_1^k gives
sigma_1^(k-2) and a smoothing gives sigma_1^(k-1), that closure(sigma_1^0) is
the 2-unlink and closure(sigma_1^1) the unknot, and that HOMFLY exists and is
an isotopy invariant, are all BUILT INTO the definition of skein. What is
proved is the algebra downstream of the skein relation -- exactly the layer
the two computations/ files disagree on.

### Decision still needed (unchanged, but now cheap)

Which crossing-sign convention the symbolic path should use. If the
reference's, then homflypt_2strand's table and _self_test's expected values
both need (v,z) -> (v^-1,-z) applied, and the k=2/k=3 comments relabelled.
The Lean gives the exact substitution to apply, so the edit is mechanical.


## 2026-08-21 — APPLIED (owner: 'go'). Table corrected, and it was worse than reported.

Ground-truthed every entry against computations/homfly_skein_braid.homfly
(exact-integer skein). k = 0, +-1 were always right. The other four were not,
in TWO distinct ways:

    k = +3  held the LEFT trefoil            -> pure mirror swap
    k = -3  held the RIGHT trefoil           -> pure mirror swap
    k = +2  held the NEGATIVE Hopf link      -> pure mirror swap
    k = -2  held MINUS the positive Hopf     -> mirror swap AND a sign error

The k = -2 sign error is the interesting one and it is exactly what the Lean
predicted. That entry, commented 'mirror of positive', had been derived from
the (already mirrored) k = +2 by plain v -> v^-1. The HOMFLY mirror is
(v, z) -> (v^-1, -z). At k = 2, z appears to ODD powers, so dropping the z
sign negates the whole polynomial. At k = 3, z occurs only as z^2, so the same
omission is INVISIBLE -- which is why the bug survived and why my first report
of it ('they differ by exactly v -> v^-1') was itself wrong.

Also corrected: _self_test's three expected constants, and the labels
('Right-hand trefoil' was on the left trefoil). Self-test passes; all seven
k values now match ground truth; precision gates green.

Blast radius remains zero -- homflypt_2strand and homflypt_from_braid have no
consumers anywhere in the corpus, and a v-spread is mirror-invariant, so no
MFW reading was ever affected. This was latent, not live.

Closing: the convention question this bean opened is answered (the reference's
is correct, and it is now what the code returns) and applied.
