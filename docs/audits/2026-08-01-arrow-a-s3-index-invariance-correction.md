# W1 arrow (A) — CORRECTION to #4498: the 3D-index is S₃-invariant

**Date:** 2026-08-01
**Tier:** audit-only; scope-(a); no fit; nothing wired; L2 unchanged.
**Corrects:** [`2026-08-01-arrow-a-s3-equivariance-and-build-plan.md`](2026-08-01-arrow-a-s3-equivariance-and-build-plan.md)
(PR #4498), Part 1 + build-plan step 1.

## The error in #4498

#4498 computed the S₃-isotypic decomposition of the 729-dimensional
representation **space** `ℂ[classes] = 165·triv ⊕ 84·sign ⊕ 240·std`, then
claimed `I_tot_meridian` "discards the 240 standard copies" and that a derived
arrow (A) should "build from the graded **standard** component." That conflated
the representation-**space** decomposition with the index **function**'s content.

## The fact

The 3D-index function `b ↦ I_𝓑₃(b)` is **S₃-invariant**: `I(σ·b) = I(b)` for every
cusp permutation `σ` (the S₃ symmetry of `𝓑₃` is realised by isometries).
Corpus-verified — the graded-index witness stores **one q-series per S₃-orbit**
(165 entries for 729 classes; orbit-size distribution `{1:9, 3:72, 6:84}`), and
[`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md)
§2 records "729 classes × 6 permutations, direct equality."

An S₃-invariant vector lives **entirely in the trivial isotypic** (dim 165 =
#orbits). So the index carries **zero sign and zero standard content** — the
`84·sign + 240·std` live in the representation *space*, **not** in the index
vector.

## Corrected finding (supersedes #4498)

1. `I_tot_meridian` and the graded index carry the **same** (trivial) S₃-content;
   `I_tot` discards **nothing** — #4498's "discards 240 standard copies" is
   **false**.
2. The S₃-equivariance invariant is **vacuous** for arrow (A): a trivial-rep index
   mapping to the S₃-invariant scalar `tr_M(β_Bor)` is automatically consistent
   and **unconstrained**. S₃ does not constrain (A) at any level.
3. **The real (corrected) structural point — a rep-theoretic gap.** `tr_M(β_Bor)`'s
   underlying operator `ρ(β_Bor)` lives in the Hecke `H₃(q)` block `[2,1]` = the
   **standard** S₃-irrep (borromean-h3-2-1-irrep-derivation), while the 3D-index
   is **trivial-only**. So the standard structure of the binding operator is
   **not** sourced by the 3D-index; it is **categorical** (Hecke/Wedderburn).
   Arrow (A) can fix only the S₃-invariant **scalar** `tr_M`; the `[2,1]` operator
   structure enters through arrow (B) and the Wedderburn structure, not (A).

## Corrected build guidance (supersedes #4498 step 1)

Do **not** try to source `tr_M`'s standard structure from the index (impossible —
the index is trivial-only). Arrow (A) is a map of **S₃-scalars** (index total →
`tr_M` scalar); the operator/`[2,1]` content of the binding is Hecke-categorical.
The rest of the #4498 build plan (steps 2–5: the state integral validated on 4₁,
the state-integral↔index and state-integral↔`tr_M` continuations, the anti-fit
gate) stands — but with step 1 corrected: the index supplies the S₃-invariant
scalar only, and the value-map is a scalar-to-scalar continuation.

## Why the self-correction

This is an honest correction of a merged claim (#4498), per the anti-laundering /
"before declaring" disciplines. The corrected finding is stronger and more
accurate than the original: it identifies a genuine rep-theoretic gap (index
trivial vs `tr_M` `[2,1]`-standard) that sharpens *where* the binding's operator
structure comes from (the categorical side, not the index).

## Discipline

scope-(a); the S₃ decomposition is exact integer enumeration; the index's
S₃-invariance is read from the committed graded-index witness (165 orbit-keyed
q-series) and the 2026-07-24 verification; nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
