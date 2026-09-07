---
# qou-durg
title: 3 he_nu_sdp probes raise NameError on their success path yet publish witnesses
status: completed
type: task
priority: normal
created_at: 2026-09-06T03:37:41Z
updated_at: 2026-09-06T10:45:08Z
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

---

## Update 2026-09-06 — answered, and the names restored from the corpus's own record

**The open question is settled: the witnesses are records of WORKING code.**

Each witness records a `scriptCommitSha`. Retrieving the producer at that
commit and AST-checking the name there:

| producer | name | scriptCommitSha | ancestors | bound there? |
|---|---|---|---|---|
| `he_nu_sdp_barfold_h9_test` | `RAIL` | `138ab4aa9afd` | 8706 | **yes** |
| `he_nu_sdp_psd_count_test` | `H` | `df5a7ee4e5af` | 7582 | **yes** |
| `he_nu_sdp_saturation_obstruction` | `RAIL` | `fcc65c13805d` | 10202 | **yes** |

All three are real commits (thousands of ancestors, so not graft boundaries —
checked, after this bean's earlier attribution turned out to be one). All three
`scriptHash` values differ from the current files, so the producers changed
after the witnesses were written. So: **not failure-branch output, and not
fabricated — the code worked, and a later edit broke it.**

### What broke them

The q0-anchor migration. Each file had a two-line block:

```
Q0 = 1.1099785955573347
RAIL = 1e5   # |x| above this is a degenerate bound-rail, not a genuine support
```

(`H = Q0 - 1.0 / Q0` in `psd_count`). The migration rewrote that block into the
resolved pin plus its explanatory comment and **took the second line with it**.
The call sites survived, so each module still imports cleanly and raises
`NameError` only when the LP succeeds — which nothing in either test tree
exercises. Exactly the failure mode as `_is_sparse_sigma` in the qou-uiut
merge: a block rewrite drops a definition while its consumer lives on.

### Restored — recovered, not invented

`RAIL = 1e5` (with its original comment) and `H = Q0 - 1.0 / Q0`, taken
verbatim from the commit each witness names. Kept as **float** deliberately:
`RAIL` is compared against `res.x[i]`, scipy LP output, and these modules
already carry a documented deliberate `Q0 = float(Q_50_DIGIT_STR)` pin. Making
them mpf would fight the module's own stated choice, not serve NO-FLOAT64.

Verified: 0 dangling names in all three.

### Remaining — regeneration, and a verdict re-read

`H` depends on `Q0`, and the pin moved from the retired pin A to the resolved
proton pin, so H goes 0.20906032199559366 → 0.20906029879563937 (−1.1e-7
relative). That is the migration working as intended, not a defect — but it
means these three witnesses **cannot** reproduce as committed, and their
`verdict` / `bounded_support` fields have not been recomputed since the code
was repaired. Whether the published verdicts still hold is open until they run.

Not run here: the `hadron_knot_table` regeneration (bean qou-uiut) holds the
checkout. Queued.

---

## 2026-09-07 — RE-RUN. All three verdicts hold. Closing.

With `RAIL` and `H` restored, all three producers run (1–2 s each, exit 0) and
emit fresh witnesses. Compared field-by-field against the committed ones:

| witness | verdict | conclusion | data |
|---|---|---|---|
| `he-nu-sdp-barfold-h9-test` | **unchanged** | unchanged | provenance only (4 lines) |
| `he-nu-sdp-psd-count-test` | **unchanged** | — | provenance only (4 lines) |
| `he-nu-sdp-saturation-obstruction` | **unchanged** | unchanged | `q1_saturation_sizes` MOVED |

**The published findings survive.** `#2552` stands and sharpens; the
self-conjugate count match remains a coincidence with the weaker fact intact;
ρ_F=2 for ⁴He remains an underived input.

### The one real data change, and why it is not this bean's defect

`q1_saturation_sizes` went `{D:1, T:0, ³He:0}` → `{D:0, T:0, ³He:1}` — the
saturating atom moved from D to ³He, with D's `support` going from one entry to
empty.

That is **not** the NameError. The committed witness was computed 2026-08-30 at
a `scriptCommitSha` where `RAIL` WAS bound, so it took the success path too —
both runs did. What changed in between is `atom_canonical_crossings`, which
this probe consumes and which bean qou-hu1f rewrote to the interleaved
Borromean word. A probe in that cone moving is the ruling working, not a bug.

### Summary of Changes

- Established the witnesses were records of WORKING code, by AST-checking each
  producer at the `scriptCommitSha` its own witness records (8706 / 7582 /
  10202 ancestors — real commits, checked for graft boundaries).
- Traced the breakage to the q0-anchor migration rewriting the
  `Q0 = …` / `RAIL = …` block and taking the second line with it.
- Restored `RAIL = 1e5` and `H = Q0 - 1.0 / Q0` **verbatim from those commits**,
  not invented, and kept them float to match each module's documented
  deliberate `float(Q_50_DIGIT_STR)` pin.
- Re-ran all three: verdicts unchanged, one data field moved for an unrelated
  and understood reason.

Nothing outstanding.
