---
# qou-m0bv
title: 'GAP: 4 particle-existence blocks prove a degenerate witness (zero-mass proton, two-unknot hadron)'
status: todo
type: task
created_at: 2026-08-08T19:26:21Z
updated_at: 2026-08-08T19:26:21Z
---


Full analysis:
[`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`](docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md).

## The four

| block | witness actually proved |
|---|---|
| `predicted-spectra/categorical-proton-exists` | zero-mass degenerate proton |
| `predicted-spectra/categorical-neutron-exists` | zero-mass degenerate neutron |
| `knots-particles-confinement/hadron-exists` | a "hadron" made of two unknots |
| `lifting-and-descent/quantum-characteristic-classes-exists` | zero obstruction class over ℤ |

Every one is honestly commented ("Trivial witness…", "The intended … witness
is sharper but requires the Hecke NF reduction infrastructure"). The defect is
that a degenerate witness sits under a headline theorem name —
`CategoricalProton.exists` reads as "the categorical proton exists".

## Why a better witness is not the fix

`CategoricalProton` has four fields (`skein_uu`, `skein_ud`, `mass`,
`chirality`) and **no properties**. The narrative claims the witness has
"negative crossing energy and Frobenius stability" — the structure has no
field for either, so those claims are **unstatable**, not merely unproved.

So the order is:

1. Give the structures fields carrying their defining properties (crossing
   energy, Frobenius stability, the Borromean B₃ relation).
2. *Then* the existence theorem is a real obligation, and the intended
   Borromean witness discharges it.

Step 1 is the formalisation project. Both steps need the Hecke NF reduction
infrastructure the comments already name, so this is correctly **blocked**,
not merely undone.

## Do not delete the theorems

For what the statements currently say, the proofs are correct. Deleting them
would misrepresent trivial statements as open conjectures — the mirror of the
defect fixed in #4797. Same rule as `qou-g4x1`.

## Detector note

This class is invisible to every existing audit — no `sorry`, no `True`, no
unsound quantifier, and the statements are *true*. Found by scanning for
kernels whose entire content is `Nonempty X`, then asking whether `X` is
substantive. Triage rules that make the signal usable (376 raw hits → 14 real,
4 findings): strip comments first, exclude `.lake` and `have`/`haveI`/`letI`,
and treat `Nonempty` fields *inside content-bearing structures*
(`fibre_nonempty`, `exceptional_nonempty`, …) as legitimate non-degeneracy
side-conditions rather than findings.
