---
# qou-xpwx
title: 'The sub-affine (true max-contact) shape: does it carry a surface term, and is the corpus''s max-contact edge set really uncovered by the affine exclusion?'
status: completed
type: task
priority: normal
created_at: 2026-09-05T19:50:28Z
updated_at: 2026-09-05T19:51:08Z
---

## Resolved 2026-09-05 — a NEGATIVE, plus a correction to my own #6801

Lean `QOU/Mass/MaxContactHasBulk.lean` (sorry-free, 6 decls axiom-clean) + probe
`computations/probes/max_contact_bulk_exponent_probe.py` (17/17). Audit:
`docs/audits/2026-09-05-max-contact-sub-affine-negative.md`.

**THE CORRECTION, and it is the main deliverable.** #6801 reserved max-contact sphere packing as an
uncovered candidate whose contact numbers "are not known to be affine". WRONG: the corpus's
max_contacts(A) = 3A - 6 (gap1_max_contact_a5plus.py:77-79), verified by loading it out of the
corpus with ast. The reserved candidate does not exist as implemented, so #6801's conclusion is
STRONGER than it claimed — every derived edge set on main is affine. Also: its "not the same family
in general" should read "not the same family above A = 9" (within 4 <= A <= 7 they agree), and
3A - 6 is derived from Euler on a 2-SPHERE with the packing reading asserted on top, which is why
it has no interior.

**The new object.** A true max-contact packing has a SUB-AFFINE count M(A) = kappa*A - c*A^theta.
Its per-nucleon exponent is p = 1 - theta (the complement), it escapes #6801's Part 1, and it passes
HasBulk — the only shape in this corpus that does. d = 1 returns p = 1, so the production chain is
the family's degenerate surface-free member rather than an outsider.

**THE LIVE COUNTEREXAMPLE.** qou-zy94's zero-fit three-point determinant filter excludes
Phi = c*x + a*x^(2/3) for EVERY (c, a) — and that IS this shape with theta fixed at 2/3.
Reconstructed independently: det3 = 0.013144 against zy94's 0.01406, within 7 %; control psi = x
returns exactly 0. qou-pohg does NOT rescue it — that bean refutes excluding the whole CLASS
(psi free) and explicitly preserves the fixed-psi exclusions. Scope-(a): three light-nucleus points,
SEMF calibrated for A >~ 20.

**The exponent test.** p = 1/d is DISCRETE, so it can be excluded rather than merely "consistent
with". Of #6780's five variants: 3 admit NO d, 1 is too wide to discriminate, 1 picks d = 3
uniquely. The family is excluded by more variants than select it. And the corpus disagrees with
itself: a mirror-split probe puts 1/3 at 4.1 sigma and 1/4 at 0.1 sigma.

**NOT new: p = 1/3 was already derived** in my own CoordinationSurfaceDeficit from
A_surf = c*A^(2/3) — the same import written the other way round. An earlier draft of the Lean
claimed this removed an assumption; corrected.

**Nothing held.** All four library tiers return only homonyms for Harborth/Bezdek/contact number;
references.ts has no packing entry. So no literature constant is cited and theta stays a free
parameter. Four standing objections to the dimensional reading, the sharpest being that the ambient
geometry is HYPERBOLIC (H^3 gives R ~ ln A, not A^(1/3); consistency costs 2.64x).

**Gap with no prepared answer:** no physical-realism objection is recorded anywhere (nuclear matter
is a liquid, not close-packed; nucleons are not hard spheres). That is a statement about the surface
I searched, not evidence nobody holds it. A referee will raise it.

## Next (my judgement, overrule freely)

Take the hyperbolic objection seriously. If the geometry is H^3 the surface law is ln A, a
DIFFERENT functional form never tested against the residual. It is the only option that attacks the
framework's own geometry instead of importing someone else's, it is what qou-rav3 explicitly asks
for, and the honest expectation is a worse fit that is better founded — which is iterable where an
imported better fit is not.
