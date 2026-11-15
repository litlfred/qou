---
# qou-mbar
title: 'GAP: Inv R_q -- braiding eigenvalue + q-ext-deriv written over a field, ground ring is now Z[q,q^-1]'
status: completed
type: task
priority: normal
created_at: 2026-08-17T22:44:34Z
updated_at: 2026-08-18T20:58:40Z
---

Found by the ch1+ch2 elaboration sweep (qou-n4jv), 2026-08-17.
Audit: docs/audits/2026-08-17-ch1-ch2-lean-sibling-elaboration-sweep.md (F1).

R_q = LaurentPolynomial Z has NO Inv instance. Two files write x⁻¹ over it
and therefore do not elaborate:
  * quantum-observable-universes/braiding-eigenvalue-extraction.lean
      BraidingEigenvalueData.anti_eq_neg_inv : lamAnti = -(lamSym)⁻¹   (line ~159)
      hecke_polynomial_roots  (uses bed.q⁻¹)
  * quantum-observable-universes/categorical-q-ext-deriv.lean  (line ~78)

Root cause, not a typo: braiding-eigenvalue-extraction's own docstring says
'the rest is pure algebra over R (proved here without sorry)'. It was written
over a field; the ground ring later became Z[q,q⁻¹]. In R_q the element q IS
invertible but a general element is not, and there is no ⁻¹ operation to write.

Why not patched inline: re-expressing the claims CHANGES WHAT IS STATED, so it
is a content decision, not a repair. Candidate routes:
  (a) state multiplicatively -- det_constraint (lamSym * lamAnti = -1) is
      already a field of the structure and carries the same information;
      drop anti_eq_neg_inv or restate it as lamSym * (-lamAnti) = 1;
  (b) carry IsUnit lamSym + its inverse as explicit data;
  (c) work over a localisation / Laurent field of fractions -- but that
      reintroduces exactly the field assumption the corpus is trying to shed.
Prefer (a): it needs no new hypotheses and matches the 'invertible, not
nonzero' discipline the corpus already uses over rings.

NOTE the lamSym/lamAnti names: these were λ_sym/λ_anti and collided with the
left-unitor notation λ_ (MonoidalCategory is opened). Renamed in 39f5f944.
Do not rename them back.
