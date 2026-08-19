---
# qou-kebu
title: 'T2b: derive per-strand twist multisets from framed braid words'
status: in-progress
type: task
priority: high
created_at: 2026-08-04T10:16:22Z
updated_at: 2026-08-16T23:00:29Z
parent: qou-8lxd
---

BATTERY RESULT (strand-twist-y-battery.witness.json):
- 10,000 candidate helon-style twist assignments tested
- Only 4 survive the spectrum + nucleon-GMN battery
- u-quark multiset {0,1,1} is UNIQUELY determined
- electron multiset {-1,-1,-1} is UNIQUELY determined
- All 4 survivors are sign-flip variants of the SAME assignment

DERIVATION GAP:
The battery proves CONSISTENCY (the twist assignments are compatible
with known physics) but does NOT DERIVE them from QOU axioms.

To close T2b, need to show: given the framed braid word for each
torus knot T(2,p), the per-strand twists follow from the ribbon
structure of the Hecke category. Specifically:
1. The twist θ_V = q^{c_V} acts on each strand by the Casimir
2. For T(2,p) = σ₁^p, the total twist is p·θ_V
3. The per-strand multiset is determined by the braid monodromy
4. The battery result shows the answer is {0,1,1} for u, etc.

DEPENDS ON: T2 (hypercharge from ribbon twist = the derivation
of what Y means categorically, which is still the gap).

## Step 1 of the proposed route cannot deliver step 3 (2026-08-16)

`QOU/StandardModel/ComponentFraming.lean` — lean-direct exit 0, no warnings, no
sorry/axiom/native_decide. Library file, no sidecar; my verification is the gate.

### Why theta is the wrong tool, from the corpus's own probe

The route above says "theta_V = q^{c_V} acts on each strand by the Casimir" and
then "the per-strand multiset is determined by the braid monodromy".
`ribbon_twist_charge_quantum_probe.py:13-17`:

  > "On a simple object of a ribbon category the twist theta acts by a SCALAR;
  >  for Hecke / quantum-sl_N the exponent is the CONTENT SUM of the partition"

A scalar attached to an object is ONE number. The battery's answers are
NON-CONSTANT multisets -- u = {0,1,1}, d = {-1,-1,1} -- and no scalar produces a
non-constant multiset over identical strands. That probe tested Q = c(lambda)/3
directly and it FAILED; this is the structural reason it had to.

theta is the WEIGHT PER UNIT FRAMING (q^{c_V t_i}), not the framing t_i. Step 1
cannot fix integers; it acts on them.

### What does fix them: the closure map, not the twist

Step 3's instinct is right but the mechanism is the PERMUTATION. In a framed
link the framing is one integer PER COMPONENT, not per strand. Closing beta
joins strand i to strand pi(beta)(i), so a cycle of pi becomes ONE component and
a well-defined framing takes one value on all of it. That is not an extra
assumption about ribbons -- it is what "framing of a framed link" means,
transported to strand indices.

    IsComponentFraming pi t  :=  forall i, t (pi i) = t i

### Derived, falsifiable consequences

  constant_of_transitive   pi transitive (closure is a KNOT) => t constant, so
                           the multiset is {a,...,a}
  eq_one_of_injective      all entries distinct => pi = 1, closure is a totally
                           split n-component link

Applied to the four survivors:

  u  {0,1,1}              pi is NOT transitive -- u's closure is not a knot
  d  {-1,-1,1}/{-1,0,0}   same
  nu {-1,0,1}             pi = 1, totally split
  nu {0,0,0}              unconstrained
  e  {-1,-1,-1}           unconstrained (constant fits any pi)

Two of these are Lean-instantiated at Fin 3, the battery's strand count:
`u_multiset_forces_nontransitive`, `nu_multiset_forces_trivial_perm`.

These are the first constraints in this arc that are DERIVED rather than
enumerated. The battery searched 10 000 assignments and reported which survive;
this says which are POSSIBLE given a braid, before any search.

### Scope

Scope-(b) on the one excluded step -- theta alone determining a non-constant
per-strand multiset is excluded by the scalar/multiset mismatch, a proved
invariant. Scope-(a) on everything else. NOT excluded: theta in its actual role
as the weight q^{c_V t_i}; the hypercharge programme; this bean, whose step 3 is
reformulated rather than closed.

### Blocking input unchanged

The battery's own witness records it: the corpus carries NO per-chiral-fermion
framed braid words (bean htw2). Until those exist the table cannot be evaluated
-- which is exactly why it is worth stating now, as the test those words face.
