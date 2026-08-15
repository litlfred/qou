---
# qou-aze5
title: 'GAP: test_empty_active_set_fails contradicts verify_dual_present''s own documented policy'
status: todo
type: task
created_at: 2026-08-15T01:00:10Z
updated_at: 2026-08-15T01:00:10Z
---


## State: PRE-EXISTING on main, not introduced by the convention-D work

Reproduced in a clean `origin/main` worktree, so this is not fallout from
PR #5055. Found while draining the pyhecke suite for the C → D migration;
beaned rather than folded into that diff because it is unrelated to the
trace convention.

    tools/pyhecke/tests/test_lp_dual_null_hardening.py::test_empty_active_set_fails
    E   assert True is False

## The contradiction

`verify_dual_present` (`tools/pyhecke/python/pyhecke/lp_dual_solver.py`
~L525) deliberately accepts an empty `active_set`, with a documented
mathematical rationale:

> An EMPTY active_set is a legitimate dual result — it means no Frobenius
> constraint is tight (all shadow prices y_star are sub-tolerance, i.e. an
> interior SDP/LP optimum). Treat any list (incl. []) as present; the
> hollowness check stays strict for y_star/y0_star/objectives, which a
> genuinely un-computed dual leaves null/empty.

The test asserts the opposite — that `active_set: []` is hollow and must
fail. Both cannot be right.

## Why this needs a judgement call, not a quick fix

The two readings are both defensible and they trade off against each other:

- **Implementation is right.** An interior optimum genuinely has no tight
  constraints. Failing it would reject correct witnesses, and the AGENTS.md
  LP-dual contract does not say the active set must be non-empty.
- **Test is right.** In practice an empty `active_set` is far more often a
  solver that never populated it than a true interior optimum — which is
  exactly the witness-hollowness pattern the null-hardening file exists to
  catch. Accepting `[]` reopens the hole the file was written to close.

The distinguishing evidence nobody has gathered: **do any real
`*.witness.json` in the corpus carry `active_set: []` together with a
nonzero `y_star`?** If yes, the implementation's interior-optimum case is
real and the test is stale. If every empty `active_set` in the corpus sits
next to an all-zero or absent `y_star`, the test is right and the
implementation's carve-out is laundering hollow duals.

## Next honest step

1. Grep the corpus for witnesses with an empty `active_set` / 
   `active_constraints` / `active_channels`, and cross-tabulate against
   `y_star` and `duality_gap`.
2. Decide from that evidence, not from the prose in either file.
3. Whichever side loses, delete the losing claim rather than weakening
   both — and record the decision in the file that survives, since the
   next reader will hit the same contradiction.

Do NOT resolve this by loosening the test's tolerance or by deleting the
test: that would drop the hollowness guard without establishing that the
interior-optimum case is real.
