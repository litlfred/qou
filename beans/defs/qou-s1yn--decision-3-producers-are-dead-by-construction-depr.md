---
# qou-s1yn
title: 'DECISION: 3 producers are dead by construction — deprecate, delete, or keep as tombstones?'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:56:18Z
updated_at: 2026-10-04T15:18:37Z
parent: qou-5vkl
---

## Three producers cannot run, and none can be repaired mechanically

Found by cost-checking the `qou-tekx` "merely stale" bucket. All three now
**fail with an honest message** instead of a bare crash; the disposition below
is the owner's.

### 1-2. `compound_binding_via_differences.py`, `neutron_error_diagnostic.py`

Both need `atomic-braid-mass-table.witness.json`, **deleted 2026-05-19 by commit
`7f30a57924d` on an explicit owner directive** — *"get rid of/fix what led you
astray. it should be removed."* It was one of 11 legacy mass-compute artifacts
removed together **because they misled**: that witness carried the six-term
formula at **24–54 % error** and an off-main commitSha, and agents were citing
its values as canonical. Its producer was deleted in the same commit.

That commit repointed **two content files** to
`canonical-mass-table-extended.witness.json`. It did not repoint the Python
consumers, and these are two of eight that still reference the removed name.

**Repointing is structurally unavailable.** Both need the six-term decomposition
fields (`term1_atomic_total` and siblings). Measured: `term1_atomic_total`,
`term1` and `six_term` are **all absent** from the canonical witness, whose rows
carry a different schema entirely (`B_AME_MeV`, `err_ppb`, `knot_operators`, …).
That is not an oversight — both scripts **say so themselves**:
*"the resolved formula `M(K) = ρ_K·m_e·|tr_M(K)|` does not have an additive
six-term structure"* and *"All are legacy-only"*.

So they are **dead by construction**: the only possible input was removed on
purpose, and reconstructing it means resurrecting the 24–54 %-error table the
owner ordered removed. **Do not do that.**

### 3. `probes/lambda_scale_homflypt_skein_recursion_probe.py`

Imports `homflypt_borromean_at_az` from
`lambda_scale_alt_g_skein_polynomial_direct`, which was moved to
`_deprecated/strategy-spikes/` and then **deleted from there too**.
`git ls-tree -r origin/main` returns no file of that name and the function is
defined in **no file on main**. The probe has been **unrunnable — not slow, not
env-dependent, unrunnable** — since that deletion, failing at import before a
line of its own body runs.

**Not repointable:** the function is gone, not moved. Reviving it means
re-deriving the Borromean HOMFLYPT closed form, or recovering the deleted file
and judging whether it was deleted for cause.

## The decision

| option | what it means | cost | risk | commits to |
|---|---|---|---|---|
| **A. keep as tombstones** (current state) | they stay, failing with a message naming the commit, the directive, and why no repoint exists | nil, done | a reader still finds three scripts that cannot run | nothing; reversible |
| **B. move to `computations/_deprecated/`** | follows the repo's existing convention for retired compute | ~3 file moves + import checks | `_deprecated` is excluded from several audits, so they stop being counted | that they are retired, not merely broken |
| **C. delete** | removes them | small | irreversible in effect; the diagnostic *intent* of `neutron_error_diagnostic` (localising an 8.3 % error gap) is lost | that the六-term line is closed for good |

**Recommendation (my judgement, not a finding): B for 1–2, A for 3.** The two
mass-table consumers are unambiguously retired by an owner directive, and
`_deprecated/` is where the repo already puts that. The HOMFLYPT probe is
different — its input was deleted with no recorded rationale I could find, so
"retired" is an assumption rather than a fact, and a tombstone keeps the
question visible.

**Default if nothing is decided:** state A holds for all three. They fail
honestly, cost nothing, and mislead no one.
