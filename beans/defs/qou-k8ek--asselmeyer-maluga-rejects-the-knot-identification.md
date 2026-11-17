---
# qou-k8ek
title: Asselmeyer-Maluga rejects the knot-identification programme our CAL-2 proxy depends on
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T21:44:43Z
updated_at: 2026-11-17T11:52:00Z
parent: qou-v2om
---

`library/symmetry-11-01298` (Asselmeyer-Maluga, *Braids, 3-manifolds, elementary
particles*, Symmetry 2019) shares our ontology — fermions as hyperbolic KNOT
COMPLEMENTS, bosons as the torus bundles between them, everything represented as
**3-braids** — and then explicitly rejects the identification programme:

> "which knot is related to a fermion like the electron? **However, this question
> is meaningless in our approach.** ... the branching set, a knot or link, of a
> 3-manifold is **not unique**."

> "we do not fix the braid. In particular, **we do not believe that the difference
> between an electron and myon is given by a different braid.**"

**Why this is load-bearing and not just a rival opinion.** CAL-2's numerical proxy
is `m_mu/m_e = Vol(4_1)/hbar_q^2` — the muon/electron ratio IS a knot distinction
in our framework (the figure-eight), which is exactly the claim he denies. It also
bears on `conj:canonical-knot-id-sdp`, whose production source already admits
"that IS a form of AME-driven fitting"
(`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`).

His stated ground is specific and answerable: **non-uniqueness of the branching
set** — many knots present the same 3-manifold, so a complement does not pick out
a particle. The natural corpus reply is that `tr_M` is an invariant of the
CLOSURE rather than of the presenting braid (see `markov-disambiguation`), so
presentation non-uniqueness is not obviously fatal. **Whether that answers him or
merely relocates the difficulty is NOT settled** — his non-uniqueness is at the
level of the 3-manifold, not of the braid word, and those are different
quotients.

Note also his 3-braid arises from a 3-fold branched covering T^2 -> S^2 with six
branch points (a 6-plat read as a 3-braid), whereas our 3-per-nucleon is COLOUR.
The numerical coincidence does NOT establish they are the same 3, and nothing
here claims it.

**Disposition:** this is an adversarial datapoint from a framework that shares our
ontology, not a refutation. The honest next step is to state the corpus's answer
to branching-set non-uniqueness somewhere citable — if there is one — rather than
leave the identification programme silently contested in its own literature.

Analysis:
`docs/audits/2026-08-25-recent-knot-particle-uploads-vs-our-identifications.md` §1.

## Round 88 Progress (`litlfred/qou#8330`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/SelfConjugateMultiplicityAndProlongationKernelBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/self_conjugate_multiplicity_and_prolongation_kernel_brick_probe.py` & `computations/probes/self-conjugate-multiplicity-and-prolongation-kernel-brick.witness.json` (`scriptCommitSha = b74bffb0d148592f3bcef84a6e80235048fdcaad`, HEAD `10687cdc1c1ca67ba352499264f665447671cbf9`, `allPassed = true`).
