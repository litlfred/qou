---
# qou-tzfm
title: 'SM-lit: gerbe / non-neutral Tannakian literature is ABSENT from library/ (400 docs, 1 Tannakian hit, 0 gerbe)'
status: completed
type: task
priority: normal
created_at: 2026-08-25T06:12:42Z
updated_at: 2026-08-25T10:35:59Z
---

**Answered 2026-08-25** (PR #5744) — and the answer made the question moot.

Intake triage: `docs/audits/2026-08-25-gerbe-tannakian-intake-triage.md`.
Re-posing: `docs/audits/2026-08-25-4a-question-imports-symmetric-theory.md`.

The library gap is real (measured: 1 Tannakian hit, 0 gerbe across the corpus).
But acquiring gerbe literature would have been the wrong purchase, because the
$4$-A question as posed **imports symmetric-category machinery that QOU does not
have**. The band / $H^1(\text{base}, \underline{\mathrm{Aut}}^\otimes)$
formulation is a statement about $\mathbf{Rep}\,G$ — [DM82 2.8/3.2] are theorems
about a *symmetric* tensor category. QOU's braiding is not symmetric, and that
is now proved rather than asserted:

- `QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff` —
  $\sigma^2 = 1 \iff q^2 = 1$, from the Hecke relation alone.
- `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric.q_gt_one_double_braiding_ne_one`
  — so at the substrate $q_0 \approx 1.10998$ the braiding is not symmetric.

So $4$-A is re-posed in the cheat sheet against non-symmetric reconstruction
(Hopf algebra in $\mathbf{C}$) rather than against a gerbe band. Gerbe
literature is not needed for the re-posed question. If a later route genuinely
needs it, re-open with that route named — do not re-open on the library gap
alone.
