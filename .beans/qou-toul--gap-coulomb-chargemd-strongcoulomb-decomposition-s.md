---
# qou-toul
title: 'GAP: coulomb-charge.md strong/Coulomb decomposition swaps (p+m)/(p-m) multiplicities — Lean-refuted, 5 blocks propagate'
status: completed
type: task
priority: normal
created_at: 2026-08-08T13:04:42Z
updated_at: 2026-08-29T07:49:03Z
---

## VERIFIED AND FIXED — 2026-08-29

The bean title was correct and I confirmed it independently before acting
(it carried no body, so it was a claim rather than evidence).

### The defect, derived rather than asserted

`def:crossing-energy` weights a positive crossing `q` and a NEGATIVE crossing
`-q^-1`, citing the Skein relation. So `E = n+ q - n- q^-1`. Solving
`E = A(q+q^-1) + B(q-q^-1)` gives

    A (symmetric / strong)      = (n+ - n-)/2     the WRITHE
    B (antisymmetric / Coulomb) = (n+ + n-)/2     the crossing COUNT

`coulomb-charge.md` had these exchanged. Its decomposition expands to
`n+ q + n- q^-1`, exceeding the crossing energy by `2 n- q^-1`, and agreeing
only on positive braids — which is why it survived: the canonical atomic
braids the corpus evaluates are positive.

### The corpus was already right three files away

`prop:crossing-energy-decomposition` states `E_sym = (p-m) cosh`,
`E_asym = (p+m) sinh`, and scopes the tanh ratio to `m = 0` explicitly. So
this was never a corpus-wide error — `coulomb-charge.md` and
`crossing-energy.lean` were the two outliers. `QOU.Braiding.crossing_energy_channels`
in the Lake tree is also correct.

### How it survived — the part worth keeping

`crossing-energy.lean` did not inherit the error passively. Its docstring
said: *"with `-q^-1` the baseline + Coulomb decomposition would not hold, so
the energy is the additive `n+ q + n- q^-1`"* — the DEFINITION was adjusted so
the theorem would be provable, then `decomposition` was closed by `ring`,
sorry-free. A fit located in a definition rather than a parameter; no numeric
audit could catch it.

### What landed

- `coulomb-charge.md`: correct decomposition; the trichotomy replaced by the
  two real consequences (the Coulomb coefficient is non-negative, so no
  attractive channel and no negative charge; `n+ = n-` annihilates the
  SYMMETRIC term, so the ratio diverges there rather than vanishing); the
  tanh ratio scoped to `n- = 0`; the electromagnetic identification marked
  NOT established by this decomposition, with the name retained so the 12
  citing blocks do not cascade.
- `crossing-energy.lean`: Skein sign restored, correct multiplicities, the
  laundering docstring replaced by a record of it, and two new theorems so
  the defect cannot recur silently — `swapped_decomposition_off_by` (the
  discrepancy is exactly `2 n- q^-1`) and `swapped_agrees_iff_positive_braid`.
- `coulomb-charge.lean`: `coulombCorrection` (the swapped channel) replaced by
  `coulombContribution` / `strongContribution`, plus
  `antisymCoefficient_nonneg` and `antisymCoefficient_eq_zero_iff` making the
  falsifiable consequences theorems.

All sorry-free; lean-direct exit 0 on both files; `#print axioms` clean on all
seven.

### Still open — deliberately NOT done here

The bean says "5 blocks propagate". I did not verify that number and did not
rewire downstream: 12 `.ts` files carry a `def:coulomb-charge` edge, and
separating genuine dependence from citation, then deciding whether `Q` should
be renamed, is a physics/naming call for the author. The blast radius of the
Lean fix itself is zero — both corrected definitions were used only in their
own files.


## Propagation MEASURED — the bean's "5 blocks" was not verifiable, here is what is

I did not take the count on trust. Of the 12 .ts files carrying a
`def:coulomb-charge` edge, two blocks genuinely inherit the swap; the rest
cite the label without using the decomposition.

**1. `strangelet-crossing-energy` — the conclusion is inverted, with a number.**
It states Q = 0 for each baryon unit, then concludes "Purely strong crossing
energy … there is no Coulomb correction; the entire crossing energy lies in
the symmetric (strong) channel", writing `N·½(n+ + n-)(q + q^-1)`.

Under the correct assignment Q = 0 means n+ = n-, which annihilates the
SYMMETRIC term; the energy is then entirely ANTISYMMETRIC,
`N·½(n+ + n-)(q - q^-1)`. Verified symbolically: sym = 0, asym = k(q - 1/q),
and sym+asym reconstructs E exactly. The stated energy exceeds the true one by
`2 N n- q^-1` — a factor of **9.62 at q0** (2.0109 vs 0.2091). And the block
CITES prop:crossing-energy-decomposition, which says the opposite.

Fixed the algebra; flagged rather than invented the physics: the strangelet
now has zero symmetric and maximal antisymmetric content, which contradicts
the "electromagnetic neutrality" reading in item 1 and the enhanced-binding
argument in item 3. Those need re-deriving, not relabelling.

**2. `strangelet-crossing-energy` also uses non-representable Q values.**
Item 1 computes Q = +2/3 - 1/3 - 1/3 from assigned quark charges. But
`def:coulomb-charge` is ½(n+ - n-) in ½Z, so ±1/3 and ±2/3 are outside its
range for EVERY braid word. Two distinct quantities share the symbol Q. The
vanishing of the sum is unaffected; it is simply not a statement about the
crossing-count Q that item 2 then uses. Flagged in place.

**3. `coulomb-strong-ratio-q-rational` — scoping only.**
Its identity `tanh(ln q) = (q^2-1)/(q^2+1)` is true for all real q > 0 and is
untouched. What it inherited was the UNCONDITIONAL attribution: it said
"def:coulomb-charge defines the Coulomb-to-strong ratio as tanh(ln q)", which
holds only at n- = 0. Scoped to positive braid closures, with the general
multiplicity factor named.

**Not affected:** electroweak-higgs-torus-link-triplet,
electroweak-triplet-charge-spin-from-involution, sm-hypercharge-invariant,
strand-twist-datum, sm-gauge-truncation, sm-lagrangian-selection-rules,
flavor-charge-assignments — these cite the label without invoking the
decomposition.

**Credit where due:** strangelet-crossing-energy already knew Q is
writhe-derived and NOT a Markov invariant, citing `writhe_stabilize` for the
±1 shift under stabilisation. That was one of my red-team lines and the corpus
had already answered it.
