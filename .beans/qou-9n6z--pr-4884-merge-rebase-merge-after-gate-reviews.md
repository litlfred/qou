---
# qou-9n6z
title: 'PR #4884: merge (rebase-merge) after gate + reviews'
status: completed
type: task
priority: normal
created_at: 2026-08-10T07:07:54Z
updated_at: 2026-08-10T12:53:11Z
parent: qou-aemy
---

Merged **2026-08-10T08:19:08Z** by `litlfred` — **rebase-merge**, 25 commits
onto `main`, landing as `5cc389cfe5`. Head branch
`claude/algebraic-independence-obstruction-e8hiex` **preserved**, per the
never-delete-feature-branches directive.

Method was the AGENTS.md default (rule 8): rebase, not squash. It matters here
— the 25 commits include four that are worth bisecting to on their own (the
aggregator wiring `a8677cb28`, the producer-level float64 drain `0516ca508`,
and the two regeneration commits), and squashing would have collapsed them into
the authoring session's 21.

**What the merge rested on.** Explicit owner authorisation, plus the
verification gate in `qou-rok2` — *not* CI, and *not* a review:

- 0 check runs (`build.yml` is `workflow_dispatch`-only)
- Copilot timed out past the 15-minute cap (`qou-f0dj`); Gemini sunset
- so the Phase-4 gate was the agent's own Lean + precision-gate verification

**Carried onto main, deliberately visible, not absorbed:**

- `qou-5wuz` — neither new witness records `q0Anchor`; `Q0_ANCHOR_MISSING`
  1892 → 1894. The branch's own defect, left open as a bean.
- `check-sidecars` P30 — both new producers bypass `WitnessBuilder`, so they
  emit `PROV_MISSING`. Advisory, tracked.
- `qou-oflu` — the inherited `kappa-shell8-excess-convention` float64 offender
  (25 fields). Predates the branch; still the only thing holding the §4b gate
  red repo-wide, and it kept its owner at merge time rather than acquiring one
  by proximity.

**Scope discipline as merged**, since it is easy to over-read a merged negative:
the PR's §1 is scope-(b) (proved invariant) for the narrow claim that grade
separation alone cannot decide a polynomial relation among standard reals — it
does **not** exclude surreal methods from the problem. §2's findings 1–2, §3,
and §5 are scope-(a): they are about the *stated arguments* and about what
*that extraction procedure* can determine, not about the volume conjecture or
the c_k themselves.
