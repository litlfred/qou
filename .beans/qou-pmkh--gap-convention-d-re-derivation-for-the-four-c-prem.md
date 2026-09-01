---
# qou-pmkh
title: 'GAP: convention-D re-derivation for the four C-premised computations sites'
status: todo
type: task
priority: normal
created_at: 2026-08-29T08:04:34Z
updated_at: 2026-08-30T07:56:33Z
---

Four convention-C sites in computations/ that must NOT stay on C but CANNOT be
migrated by substituting z_D, because the substitution changes what the site
ASSERTS. Same class as the seven already in `blocked_on_rederivation` in
docs/coordination/trace-convention-registry.json. Found while draining the
2026-08-29 excision (PR #5972); all four are invisible to
scripts/convention-c-producer-audit.py.

1-2. THE GRAM PAIR — under convention D the determinant is IDENTICALLY ZERO.
   computations/gram_h3_det_factorization.py:55   (e[(0,1)] = e[(0,2)] = u/(u^2+1))
   computations/gram_h3_symbolic_regression.py:72 (same entries, mpmath)

   MEASURED with sympy on the det factorisation recorded in
   content/.../nuclear-interactions/gram-matrix-h3-symbolic.md item 2:

       det G(q,z) = -(z-q)^5 (qz+1)^5 ((q^2+1)z - q^3) (q^3 z + qz + 1) / q^8

   The third factor is `(q^2+1)z - q^3`, which at z_D = q^3/(q^2+1) is exactly 0
   for every q. So det G == 0 under D; under C it is nonzero (-0.1892 at q0).
   That is not a numerical accident to be worked around: it IS the D Gram
   singularity that bean qou-cds2 tracks, and the whole purpose of
   gram_h3_det_factorization.py is to emit the symbolic factorisation for the
   Lean `gramMatrix_det_ne_zero` discharge. Substituting z_D turns that
   discharge into a proof of a false statement.

   The honest disposition is a registry row (blocked_on_rederivation, blocked on
   qou-cds2) plus an in-source note saying the C is deliberate and why. What
   replaces `gramMatrix_det_ne_zero` under D -- rank 5, radical spanned by the
   three-strand q-antisymmetriser -- is the re-derivation, and it is real work.

3. THE BAR-PARITY PROBE — z_C is bar-even, z_D is bar-NEITHER.
   computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py:131,137

   MEASURED symbolically:
       bar(z_C) - z_C = 0                      -> z_C IS bar-even
       bar(z_D)       = 1/(q^3 + q)
       bar(z_D) - z_D = 1/q - q = -h           -> neither even nor odd

   (The relation `bar(z_D) = z_D - h` is worth keeping; it is what a D-frame
   re-derivation of the bar decomposition has to be built on.)

   The probe asserts `z_naive_bar_even` and its subject is the bar-even B4
   magnitude. Substituting z_D flips that assertion False and the probe then
   reports a fact about a premise it no longer has. I applied the substitution,
   saw this, and REVERTED it -- the file is unchanged on the branch.

4. THE TWO qbeta c_3 PROBES — the C-frame ladder, blocked on qou-cds1.
   computations/qbeta/qbeta_c3_barodd_hs_matrix_resolvent_probe.py:86
   computations/qbeta/qbeta_c3_cross_anchor_exactness_probe.py:55

   Both build `TR_M = [1,z,z,z^2,z^2,z^3]` / the ladder phase `alpha=(z-1)h/2`
   from z_C. AGENTS.md already scopes the whole Q_beta c_k ladder as
   convention-C-frame pending qou-cds1, and
   QOU.QBeta.decayLadder_zC_threeRow_ne_zero makes the C-frame ladder and the
   mass channel three-row forcing mutually exclusive -- so a z-swap here is not
   a valid move, by a sorry-free Lean result. Same disposition as the six
   qbeta rows already registered: blocked on qou-cds1, accounted not excused.

NEXT HONEST STEP: add four rows to `blocked_on_rederivation` (2 on qou-cds2,
1 new, 2 on qou-cds1) with this evidence, so the standing audit accounts for
them instead of being blind to them. Then the re-derivations are four separate
pieces of research, not a sweep.

## 2026-08-30 (PR #6110)

- **Registration COMPLETE.** The sixth line-site (`deltalambda_bareven_b4_magnitude_probe.py` `z_bar`, :137) was never registered — and was double-counted, listed among qou-t9r1's *migratable* sites while described there as "the partner of the blocked site above". Now a `blocked_on_rederivation` row.
- **All four dispositions re-verified symbolically**, not cited: `((q²+1)z−q³)|_{z_D} = 0`; `det G|_{z_C,q₀} = −0.1892052191`; `bar(z_C)−z_C = 0`; `bar(z_D)−z_D = −h`.
- **Gram item: the replacement theorem is DERIVED** — see qou-cds2 above. That was the largest of the four.
- Two c₃ items remain blocked on qou-cds1; the bar-decomposition item (the only one pmkh owns outright) is still open, and must be built on `bar(z_D) = z_D − h`.
