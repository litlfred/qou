---
# qou-fg1j
title: 'GAP: u1_hypercharge_assignment.py consumes def:coulomb-charge Q as the ELECTRIC charge and cites the removed coulombCorrection term'
status: completed
type: task
priority: normal
created_at: 2026-08-29T07:10:45Z
updated_at: 2026-08-29T08:39:23Z
---

## RESOLVED 2026-08-29 — nomenclature and provenance, ZERO numeric change

The producer's arithmetic is untouched and its conclusion survives intact. What
was wrong was three descriptive claims.

### What the producer actually does

`u1_hypercharge_assignment.py` asks whether the per-crossing coupling `c` in the
framing phase `q^{w.c}` is structurally fixed or free, and answers `c = 1/2`
from `def:coulomb-charge` (`Q(H) = (1/2)(n_+ - n_-) = w/2`). It then tests the
writhe ladder against `(Q, I_3, Y)` scale-free. Its verdict:

    writhe ladder match: Q=False  I3=True  Y=False

So it already concludes the writhe is NOT the hypercharge and NOT the electric
charge -- it tracks `I_3`.

### The three defects, all descriptive

1. It called `Q` "the framework's ELECTRIC / Coulomb charge". PR #5956
   established `Q` is the halved WRITHE and the coefficient of the SYMMETRIC
   (strong) channel; the antisymmetric coefficient is `(1/2)(n_+ + n_-)`.
2. It cited "the coulombCorrection term `Q(H)*(q - q^{-1})`". That term was the
   swapped assignment and #5956 removed it. `Q` multiplies `(q + q^{-1})`.
3. Stale path: it cited `content/.../climax-volume-mass/coulomb-charge.lean`.
   The block lives in `knots-particles-confinement/`.

### Why `c = 1/2` survives

`c` is the HALVING of the writhe. That is independent of which channel `Q`
weights, so the correction cannot move it. `C_COULOMB = Fraction(1, 2)` is
unchanged.

### The correction STRENGTHENS the producer's own finding

A quantity that weights the STRONG channel is expected to track a
strong-interaction quantum number, and Q2 finds exactly that: the writhe ladder
matches `I_3` and is falsified as a hypercharge map by the proton/neutron
same-Y test. Under the old "electric charge" label that match read as a
surprise; under the corrected label it reads as the expected outcome.

### Verification

Producer re-run: 10 assertions, all passed. Witness diffed key-by-key against
the pre-edit copy with volatile fields masked -- **0 numeric changes**; the only
movement is the caveat text I edited plus `computedAt` / `invocation` /
`environment`.

precision-gates: 7 REDs, and the SAME 7 reproduce on pristine main at
`0a45500968` -- all inherited, my file named nowhere in the log. Note the
inherited count moved 5 -> 7 because MAIN changed, not because of this edit; the
"5 REDs" figure recorded earlier in this session is stale as of this main.
