---
# qou-durg
title: 3 he_nu_sdp probes raise NameError on their success path yet publish witnesses
status: todo
type: task
created_at: 2026-09-06T03:37:41Z
updated_at: 2026-09-06T03:37:41Z
---

Found by the post-merge AST undefined-name scan (merge 5f5ad14195), not by any
suite — nothing in `tests/` or `tools/qou-substrate/tests/` executes these.

Three probes use a name that is bound nowhere in the file:

| file | line | name | enclosing fn |
|---|---|---|---|
| `computations/probes/he_nu_sdp_barfold_h9_test.py` | 183 | `RAIL` | `barfold` |
| `computations/probes/he_nu_sdp_psd_count_test.py` | 153 | `H` | `_rho_word` |
| `computations/probes/he_nu_sdp_saturation_obstruction.py` | 209 | `RAIL` | `saturate` |

In all three the name sits on the **success** path — past the `if not
res.success: return {...}` early exit — so it is not dead code guarded by a
failure branch. `RAIL` appears in `barfold_h9_test`'s docstring ("NON-RAIL
support") but is never assigned; in `saturation_obstruction` it has no mention
at all outside line 209. `H` in `psd_count_test` is used as the Hecke parameter
in `M @ (s if i > 0 else (s - H * eye))` (σ⁻¹ = σ − h), and the comment says
`h` while the code says `H`.

All three publish witnesses:
`he-nu-sdp-barfold-h9-test.witness.json`, `he-nu-sdp-psd-count-test.witness.json`,
`he-nu-sdp-saturation-obstruction.witness.json`. So either the witnesses predate
the breakage and are being served as current, or the LP never succeeds and the
recorded support sets come from the failure branch. **Which one is the actual
question**; do not guess a value for `RAIL`/`H` to make it run — that would
manufacture a result rather than recover one.

Provenance: present identically on BOTH sides of the main merge (compared by
reading the blobs, `git show <rev>:<path>`), so this is neither merge fallout
nor branch-local. Untouched by the merge commit deliberately — an unrelated
pre-existing defect does not belong inside a merge resolution.

**WITHDRAWN — the age and the introducing commit.** An earlier revision of this
bean said "introduced by `e5dcd8f544` (2026-08-01)" and called the defect five
weeks old. That came from `git log -L`, and `e5dcd8f544` is the **graft
boundary** of this shallow clone: `git rev-list --count e5dcd8f544` is 1, it
has no parents, and everything older than the graft is attributed to it. So
the SHA is an artifact of the clone depth and the date is the graft's date,
not the defect's. This repo's own
`computations/audits/producer_importability_audit.py` warns about exactly this
("DO NOT DATE ANYTHING IN THIS REPO WITH `git log`") and I walked into it
anyway. **How old these NameErrors are is not knowable from this clone.**

What survives is what was measured by reading the code and the blobs: the
names are unbound, they are on the success path, and both sides of the merge
carry them identically.

Next: read each witness's own `computedAt` (real recorded data, unlike `git
log` here) against its producer's current state, decide
stale-vs-failure-branch, then fix the names from the probes' own intent — not
from a plausible constant.

Unclaimed — filed from the qou-uiut merge, not being worked.
