---
# qou-q6f8
title: 'docstring-sorry-mismatch: 12 audit findings triaged, one tripwire fired'
status: completed
type: task
priority: normal
created_at: 2026-09-03T05:00:19Z
updated_at: 2026-09-03T05:05:12Z
---

MEASURED + FIXED 2026-09-03, branch claude/docstring-sorry-mismatch-drain-2026-09-03.

SOURCE: bun run content/pipeline/lean-vacuity-axiom-audit.ts -> 12 proof-docstring-sorry-mismatch, all severity critical, none exempt. Count after this branch: 5 (see the detector note below -- the drop is 12 -> 3 real, plus 2 the fix itself introduced).

TRIAGE. 9 genuine, 3 detector false positives.

GENUINE (docstring asserts the body is a sorry; body is a projection, #print axioms shows no sorryAx):
  kappa_commutes_bar              -> D.kappa_commutes p
  mobius_frobenius_kernel         -> ctx.classical_limit s t hst
  markovTrace_branching           -> ctx.markovTrace_branching  (docstring said the infra 'cannot be added as a simple class field' -- it WAS, under that exact name)
  nucleon_ordering_factorization  -> ctx.factorization_ident    (docstring was headed 'Honest sorry -- and now actually one')
  four_term_pair_nucleon          -> pair of ctx fields
  descended_trace_is_base_trace   -> ctx.trace_compat
  base_mass_is_norm_of_base_trace -> ctx.base_norm
  ConfinementSDP                  -> hi.strong_duality  (docstring made TWO false claims: 'discharged by sorry here' AND 'no longer merely projects that class field')
  confinement_categorical         -> ctx.confinement_ident

THE HEADLINE -- a tripwire fired and nobody was watching. confinement_categorical's own docstring said: 'no class field posits this conclusion, so the statement cannot be discharged by projection. Verify with #print axioms, which must report sorryAx; if it ever stops doing so without this docstring changing, the projection has come back.' It has. Verified by running exactly that test: [propext, Classical.choice, Quot.sound], no sorryAx. The alarm was correct, well-designed, and unread until this audit.

NOT ALL PROJECTIONS ARE DEFECTS. cat_descended_is_base_mass's two class fields are docstring'd 'Open input 1' / 'Open input 2' -- the class honestly names them as assumptions, so the theorems are accessors (Mathlib's Group.mul_assoc := Group.mul_assoc idiom), not self-assuming projections. Same for ConfinementSDP, which projects a conditional INPUT class a caller supplies, not a data field positing the conclusion. Only the prose was wrong in those.

SCOPE -- prose only, deliberately. Every one of the 9 has external consumers, so restoring the sorry the docstrings promise would propagate sorryAx outward: a change to proof content, not documentation. The projections themselves are proof-no-self-assuming-projection, owned by bean qou-z9ws / PR #6422. Fixing the lie without stepping on that.

DETECTOR LIMIT, MEASURED -- the pattern is 'docstring contains the word sorry AND body has none', which cannot distinguish three different situations:
  1. docstring falsely claims the body is a sorry            <- the real defect
  2. docstring discusses OTHER declarations' sorries         <- 3 false positives:
     identityB_general ('the bricks own honest sorrys'), whitehead_volume_conjecture
     ('whitehead_vc_innerSum_half (sorry-free...)'), shell_filling_rule ('the unproved
     ones carry honest sorrys in their own files')
  3. docstring truthfully says 'this is NOT a sorry'         <- 2 NEW false positives
     caused by THIS FIX: nucleon_ordering_factorization and confinement_categorical
     still fire, because an accurate correction has to use the word.
A refinement would need to check whether the sorry-claim is about THIS declaration. Not attempted here; the audit is 145KB of TS and that is its own tranche.

VERIFICATION: lean-direct exit 0 on all 8 changed files. Comment-only -- no declaration, statement or proof touched.
