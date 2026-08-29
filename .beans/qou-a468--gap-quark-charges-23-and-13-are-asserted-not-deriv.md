---
# qou-a468
title: 'GAP: quark charges +2/3 and -1/3 are asserted, not derived — the stated mirror mechanism forces Q_d = -Q_u and cannot make the neutron neutral'
status: completed
type: task
priority: normal
created_at: 2026-08-29T04:09:43Z
updated_at: 2026-08-29T07:49:03Z
---

## The finding, derived rather than asserted

`rem:up-quark-properties` and `def:down-quark` state ONE mechanism and TWO
numbers, and the two are incompatible.

**The mechanism.** The down quark "differs from the up quark only by crossing
orientation": at every crossing where the up strand passes over, the down
strand passes under. `down-quark.lean` formalises exactly this and proves it
sorry-free — `QOU.Archimedean.quark_crossing_asymmetry :
DownQuark.crossing_orientation = -(UpQuark.crossing_orientation)`.

**The numbers.** The same two blocks assign "+2/3" and "-1/3".

**The obstruction.** `def:coulomb-charge` is Q = (n+ - n-)/2, which is ODD
under the mirror (n+, n-) -> (n-, n+). So the mechanism forces
Q(d) = -Q(u): equal magnitude, opposite sign, ratio -1. The asserted pair has
ratio -2. No crossing count repairs this: it is a statement about the
symmetry, not about the counts.

Two further failures, each independently sufficient:

- **Representability.** Q lies in (1/2)Z, so +/-2/3 and +/-1/3 are outside its
  range for EVERY braid word.
- **Neutron neutrality — the sharp one, and mechanism-independent.** Using
  ONLY oddness under the mirror (not the particular formula), the proton `uud`
  gets Q = a and the neutron `udd` gets Q = -a. So the mechanism predicts
  Q(neutron) = -Q(proton): a neutron of charge -1 beside a proton of +1.
  Demanding a neutral neutron forces a = 0, hence a neutral proton too. The
  Standard Model escapes this only because |Q_u| = 2|Q_d| — an asymmetry
  between the two orientations that a pure mirror cannot supply.

## Scope, per the (a)/(b) discipline

Scope-(b) STRUCTURAL EXCLUSION of the stated mechanism. The invariant cited is
oddness of the charge under crossing-orientation reversal, which the Lean
sibling proves relates the two quarks. It is NOT an exclusion of the framework
deriving fractional charge by some other route.

## The corpus was already right elsewhere

`rem:flavor-charge-assignments` is honest: it records the twist multiset as a
FREE LABEL, and reports the parameter-free ribbon content-sum repair as tested
and REFUTED — "no n <= 8 yields both quark charges {+2/3, -1/3}"
(`ribbon_twist_charge_quantum_probe.py`), correctly marked scope-(a). The two
quark blocks are the outliers, exactly as with the coulomb-charge channel swap
(`qou-toul`).

## Why the sweeps missed it

Both blocks are swept on the full `da-*` adversarial battery INCLUDING
`da-false-claim`, `da-overclaim`, `da-non-sequitur`, `canonical-no-numerology`
and `da-lean-narrative-divergence`, and none fired. `da-lean-narrative-divergence`
could not fire because the Lean says nothing about charge at all — it proves
the mirror and stops. The divergence is between what the Lean PROVES and what
the prose INFERS from it, which a text-level comparison cannot see.

## Correction to my own earlier measurement (qou-toul / PR #5956)

I reported "of the 12 .ts files carrying a `def:coulomb-charge` edge, two
genuinely inherit the swap". That count is correct for what it measured and
had a blind spot: it was measured over DECLARED manifest edges, and NEITHER
quark block declares one — `down-quark.ts` has `uses: ["def:up-quark"]` only,
`up-quark-properties.ts` has no `uses` at all. Both invoke the Coulomb charge
in prose regardless. A propagation scan keyed on `uses[]` cannot see a block
that uses a quantity without declaring it.

I did NOT add the edges: `coulomb-charge` sits at position ~189 in the chapter
manifest against `up-quark`/`down-quark` at ~46-48, so a `uses` edge would be
an in-chapter FORWARD reference and would trip the detangler. The forward
dependency is real and pre-existing; adding the edge would record it in the
one place that flags it as a defect. Left for the author.

## Disposition

Fixed in place on branch `claude/coulomb-charge-channel-swap-2026-08-29`
(PR #5956):

- `up-quark-properties.md`, `down-quark.md` — the mechanism is kept and its
  actual consequence stated; the SM values are marked ADOPTED, not derived,
  with the two reasons they are unreachable and a pointer to the honest
  eightfold-way treatment.
- `coulomb-charge.lean` — five new sorry-free declarations: `mirror`,
  `value_mirror`, `abs_value_mirror`, `asserted_quark_charges_not_mirror_odd`,
  `neutron_charge_eq_neg_proton_charge`, `mirror_odd_neutral_neutron_forces_zero`.
  `#print axioms` on all: [propext, Classical.choice, Quot.sound].
- `computations/probes/quark_charge_mirror_obstruction_probe.py` — exact,
  fractions.Fraction throughout, no floating point and no numerical q anchor.

## Not done — for the author

`def:categorical-neutron` asserts 1*(+2/3) + 2*(-1/3) = 0 from the same
assigned charges. The arithmetic is right; what it is NOT is a consequence of
the crossing mechanism. Whether to re-derive neutron neutrality, or to state
plainly that the charges are an input, is a physics call.
