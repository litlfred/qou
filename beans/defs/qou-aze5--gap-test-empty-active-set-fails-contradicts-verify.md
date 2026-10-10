---
# qou-aze5
title: 'GAP: test_empty_active_set_fails contradicts verify_dual_present''s own documented policy'
status: completed
type: task
priority: normal
created_at: 2026-08-15T01:00:10Z
updated_at: 2026-09-08T04:48:10Z
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


---

## CLOSED 2026-09-08 — the contradiction is fixed on `main`, and an INDEPENDENT run of the measurement this bean asked for reaches the same verdict

This bean set a clear test for itself:

> *"The distinguishing evidence nobody has gathered: **do any real
> `*.witness.json` in the corpus carry `active_set: []` together with a nonzero
> `y_star`?** If yes, the implementation's interior-optimum case is real and the
> test is stale."*

Both halves are now settled, and the answer to the literal question is **yes on
one axis and no on another** — the dichotomy as posed had a third case.

### The fix on `main`

`57db289fdff` resolved it exactly as the bean's step 3 asks — the losing claim
deleted rather than both weakened. `tools/pyhecke/tests/test_lp_dual_null_hardening.py`:

- `test_empty_active_set_fails` → **renamed** `test_empty_active_set_with_nonzero_y_star_fails`,
  and its docstring says why: *"Emptiness alone is not the defect … The two
  fields contradict each other, because the active set is *defined* as
  `{i : y_star[i] > 0}`."*
- The failure now reports under **`inconsistent`**, not `missing` — *"nothing is
  absent here, the present values disagree"*, which is the right register.
- New `test_empty_active_set_with_zero_y_star_passes` covers the interior optimum.

So: **the implementation was right about emptiness, the test was right about the
contradiction, and each governs a different case.** That is the "each half
right" the fixing commit's subject claims, and it is not a fudge.

### I re-ran the measurement rather than taking the fix on trust

3702 tracked `computations/**/*.witness.json`, every empty `active_set` /
`active_constraints` / `active_channels` classified by `max|y_star|` against a
1e-9 tolerance:

| class | count | reading |
|---|---|---|
| **A** `y_star` present, `max|y*| < 1e-9` | **10** | genuine interior optimum (1.08e-46 … 6.70e-14, in `r5-full-canonical-knot-solver`, `e-0-lp-dual-h3`) |
| **B** `y_star` present, `max|y*| ≥ 1e-9` | **6** | inconsistent — the contradiction case |
| **C** no `y_star` at all | **36** | hollow, caught by the separate `y_star` check |
| | 248 | non-empty (ordinary) |

**Class A settles this bean's question**: real witnesses do carry an empty active
set beside a computed `y_star`, so failing emptiness outright would have rejected
them. The implementation's carve-out is not laundering. And class C does not
reopen the hole the null-hardening file exists to close, because the `y_star`
hollowness check catches those independently — verified by running
`verify_dual_present` rather than reading the prose.

### The measurement also turned up something neither side predicted — filed as `qou-ff4b`

**Class B is live.** All six are in `computations/lp-confinement-nf-forcing.witness.json`,
`max|y*| = 1.1160`, and `verify_dual_present` returns **`ok: False`** on it today
with `missing: []` and six `inconsistent` records. The repaired guard catches a
real defect on `main`.

That matters for a second reason: the new test's own docstring says *"Of 3096
witnesses, 14 carry an empty active set and ALL 14 pair it with an absent or
all-zero `y_star`"*. True when written; **the corpus is now 52 empty sets of
which 6 violate it.** Do not read that docstring figure as a current all-clear.
Tracked in `qou-ff4b`, not here — this bean's subject is the test-vs-implementation
contradiction, which is resolved.
