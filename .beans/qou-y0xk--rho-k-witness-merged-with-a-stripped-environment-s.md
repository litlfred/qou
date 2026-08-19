---
# qou-y0xk
title: rho-k witness merged with a STRIPPED environment — scipy/clarabel dropped, mpmath downgraded
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:53:31Z
updated_at: 2026-08-16T13:53:59Z
---

Self-inflicted, and merged: PR #5199, merge SHA cc2687b3d9. I regenerated computations/rho-k-co-casimir-extended.witness.json on convention D in a container missing two libraries, and the environment block went backwards:

  field            before (on main)   what I merged
  scipy            1.17.1             ABSENT
  clarabel         0.11.1             ABSENT
  mpmath           1.4.1              1.3.0
  sympy            1.12               1.14.0   (upgrade, fine)

This is the exact provenance-stripping hazard I had documented in
.claude/skills/local/compute-author.md section 0.1 EARLIER IN THE SAME SESSION,
after hitting it once on a different witness. Documenting a trap does not
stop you walking into it; the missing check is a preflight that compares the
environment you are about to write against the one already recorded.

Surfaced by the merge subagent, which caught the same class on
derivation-chain-audit and correctly declined to commit it.

The physics is very likely unaffected -- rho_k's chi path is pure mpmath
(chi_numeric), and scipy/clarabel are not in its call graph -- but 'likely'
is not 'verified', so the fix is a re-run with the environment restored
(scipy 1.17.1, clarabel 0.11.1, mpmath 1.4.1 reinstalled to match) and a
value-by-value diff against the merged witness.

FOLLOW-UP WORTH DOING: a preflight in WitnessBuilder.save() that warns when
the environment block LOSES a key or DOWNGRADES a version relative to the
witness already on disk. That is a mechanical check and it would have caught
both this and the derivation-chain case at write time.
