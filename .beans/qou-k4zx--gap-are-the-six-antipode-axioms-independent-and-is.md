---
# qou-k4zx
title: 'GAP: are the six antipode axioms independent, and is the braiding instance over-applied?'
status: todo
type: task
priority: normal
created_at: 2026-09-15T08:45:13Z
updated_at: 2026-09-15T08:45:44Z
---

## Two loose ends from the 2026-09-15 antipode change (`qou-c64q`), both found by red-teaming it

### 1. Independence of the six antipode axioms -- UNMEASURED

`def:frobenius-hopf-substrate` axiom 2 now asserts six laws on `S`:
anti-algebra, anti-coalgebra, `S(1) = 1`, `eps . S = eps`, `S^2 = id`,
`lambda . S = lambda`.

Classically the first two are THEOREMS derived from the convolution antipode
axiom, not axioms. Here they are asserted, because the convolution axiom is
gone (it has no models -- `qou-aawz`). Nobody has checked whether any of the
six follows from the others plus the Frobenius relation, the unit/counit laws
and the snake identities.

Asserting a redundant axiom is not a defect, but AGENTS.md's derive-then-check
discipline says measure it rather than assume it, and that was not done.

**How to settle it:** for each of the six, try to derive it in Lean from the
other five plus the structure axioms; where that fails, exhibit a model
satisfying five and violating the sixth. The `k[G]` probe harness
(`computations/probes/frobenius_hopf_intermediate_axioms_probe.py`) already has
every check as a separate predicate, so the counterexample search is cheap --
vary `S` over all `|G|^|G|` basis-permutation candidates for small `G` and look
for one satisfying five of six.

### 2. `[BraidedCategory C]` may be over-applied -- 55 added occurrences

The change gave `FrobeniusHopfData` a `[BraidedCategory C]` parameter, which had
to be threaded through its consumers. Six files were patched with a BLANKET
regex that added the instance to EVERY `MonoidalCategory` binder in the file,
including declarations that never touch `FrobeniusHopfData`.

Those declarations are now over-constrained: usable only in a braided category
where any monoidal one would previously do. Practical harm is low -- QOU's
ambient is braided throughout, and `QuantumUniverse` carries the instance -- but
it is a silent narrowing of the library's generality that nobody asked for, and
it is exactly the kind of thing a mechanical diff hides.

**How to settle it:** for each added instance, remove it and recompile the
module; keep the removal where the module is still clean. ~55 compiles, each a
few seconds against the restored olean shadow. Files to check first are the six
blanket-patched ones: `Instanton`, `ChannelSeparation`, `LightningPath`,
`QDifferentialGeometry`, `Torsion/Descent`, `CategoricalDqSquared`.

Both items are recorded in the red-team section of
`docs/audits/2026-09-15-antipode-anti-automorphism-package.md`.
