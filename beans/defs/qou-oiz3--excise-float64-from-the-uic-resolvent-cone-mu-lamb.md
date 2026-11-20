---
# qou-oiz3
title: excise float64 from the UIC resolvent cone (mu_lambda, s_*) -- owner directive 2026-09-12
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T20:47:33Z
updated_at: 2026-11-20T14:30:00Z
parent: qou-9nnz
---

## Measured surface and the residual (2026-09-12)

Owner directive, verbatim: **excise float64**. Follows PR #7237 / bean `qou-t6be`.

**The surface was NINE sites, not the two #7237 cited** — plus a tenth that is
not a line at all. `origin/main` line numbers:

| site | main | was |
|---|---|---|
| `q_laplacian_eigenvalue` | :292 | `casimir_sum = 0.0` over the float64 `q_int` |
| `S_REEB_PLANCK` | :520 | `(q0 - 1.0) / q0` |
| `q_resolvent_weight` | :325 | `1.0 / (mu + s)`, float64 default s |
| `_partition_table` | :544 | `_resolvent = 1.0 / (_mu + S_REEB_PLANCK)` |
| `_partition_table` | :539 | `math.log` on an mpf |
| `partition_spectral_log_rate` | :508 | `math.log(ratio)` |
| `partition_character_sigma1` | :491 | exact SYT counts x float64 q0/qi/h |
| `conjugate_pair_cross_term` / `_jet` | :2517,:2527,:2641 | `float(h)`, `math.sqrt` on an mpf MeV scale |
| `atom_markov_trace` / `atom_frobenius_norm_sq` | :2781,:2830 | `math.exp` on an mpf log-norm (the `binding_from_frobenius_pairing` leg) |

**Tenth:** `_partition_table` is a CACHE built at whatever ambient `mp.dps` its
first toucher was at — 70 under `unified_iterative_correction`'s own `workdps`,
**15** under any other consumer, no signal either way. Now wrapped.

**Numbers** (mp.dps 70, proton pin, k_exact 4, baseline from
`git show origin/main:...` loaded by path, totals read as mpf out of
`per_step[-1]` rather than through the public `float()` return):

- worst per-atom gated move **8.44176e-16** at Z=4 N=4; worst absolute
  **2.54345e-17 MeV** (at Z=2 N=1).
- worst ungated move **6.65778e-15**, also Z=4 N=4.
- float64 eps is 2.22045e-16, so **the totals DO exceed the floor** — 3.8x
  gated, 30x ungated. Mechanism is **cancellation**, not error growth: ⁸Be's
  ungated total is 1.3e-3 MeV out of O(1) contributions and its absolute shift
  is 1.04e-17 MeV like everything else. So #7237's per-block bound is right
  per block and does not transfer to a total.
- at k_exact 6 nothing exceeds 3e-16.

**OPEN, and it is larger than what was fixed.** `q_hook_product`,
`q_factorial` and `wedderburn_weight` return `mpf` and accumulate
`mp.mpf(1) * q_int(k)` over the **float64** `q_int` — mpf-typed,
float64-VALUED. Measured over the 31 weighted blocks: this excision removes at
most **2.4946976e-16** and leaves **1.0212424e-15** at lambda = (2,2), i.e. 4x
more than it removed. Root fix is `q_int` itself: **124 python files, 243
witnesses**. That is a corpus-wide sweep AGENTS.md excludes from the precision
exemption, so it is put to the owner rather than run.

**Second, smaller residual:** `_Q_MP` is built from `Q_50_DIGIT_STR` and sits
9.9102461e-52 from `q_at(90)` — ~50 digits, BELOW `OUTPUT_DPS = 60`.

PR #7245; audit `docs/audits/2026-09-12-uic-float64-excision.md`.

## The A-series witness staleness is NOT this change's (measured, both arms)

`uic-binding-a-series-kernel-live.witness.json` carries
`B_pred_MeV = -7.271102124876717` for 2H. Post-fix this container gives
`-7.271102124876745` (1233.9 s). The obvious inference — that the excision
moved it — is **wrong**, and the baseline run says so: `origin/main`'s
`binding_energy(1, 1)` also gives **`-7.271102124876745`** (1278.5 s). So the
committed value is 3.9e-15 from BOTH arms and the staleness is upstream drift on
`main`, not this PR. Left untouched; re-running the whole probe needs five atoms
at A = 3..5 against a 20-minute-per-atom floor at A = 2.

**And the two arms agreeing is not evidence the numbers agree.**
`binding_energy` returns `float(B)`, so both were compared after a cast to 53
bits; the UIC leg's own move at A = 2 is 1.66e-17 MeV, about a fiftieth of a
float64 ulp at 7.27. The public `float()` return ABSORBS this entire excision at
this atom. That boundary is deliberate and documented (bean `qou-sv7h`, #6427:
an mpf raises TypeError at `hadron_knot_table`'s `round(B, 4)`), so it is
recorded here, not changed.

## Two housekeeping notes

**`qou-t6be` could not be appended to.** Its bean FILE exists only on the
unmerged branch `claude/uic-functional-resolution-2026-09-12` (PR #7237); it is
not on `origin/main`, so writing to it here would have created a conflicting
copy. The cross-reference — including the correction that its 2.54432e-16
per-block bound does not transfer to a per-atom total — was posted as a comment
on #7237 instead. Intent was also posted on #7229 (`qou-sv7h`, same file).

**This container's clone is SHALLOW and a sibling process moved the graft
boundary mid-session.** `git log --oneline` locally shows 5 of this branch's 7
commits and `git merge-base origin/main HEAD` returns EMPTY, while both missing
commits exist as objects (`git cat-file -t` = commit) and GitHub reports the PR
at **7 commits / 11 files / +1238 -107**. Nothing was lost; a local
`merge-base` / `log` result is simply not evidence about the branch here.
Verify against the API, not the walk.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-20 — W2: main still carries the float64 q_int; #7443 brought up to date
Checked on main at `917b69399`: `qou_substrate/constants.py:190` and `substrate/q_parameter.py:169` are both still float64, and `_DPS_DEFAULT = 50`. #7443 now has main merged in (the one witness conflict was resolved by re-running its producer: gated_sum moves 1.8e-16 relative) and is ready for /prepare-merge. #7440's stage-1 content is already on main. (session_01VQDpPfkCTEiKEWdANj7rYB)

## 2026-11-20 -- #7443 MERGED; the fix is on main, and the W2 note above is stale by hours

The entry immediately above ("main still carries the float64 q_int ... #7443 is
ready for /prepare-merge", session_01VQDpPfkCTEiKEWdANj7rYB, same day) was
correct when written and is now **wrong in both halves**. #7443 merged at
09:02Z. Verified on `origin/main` rather than taken from the PR state:

- `tools/qou-substrate/python/qou_substrate/constants.py` -- the float64 `q_int`
  is gone, replaced by the exact mpmath version carrying the `qou-oiz3` comment
  block (including the correction that PR #7245 mis-attributed the leak to
  `pyhecke/wedderburn.py`, and the n-growth table).
- `computations/substrate/q_parameter.py` -- the second definition is gone too;
  the old body survives only as a comment explaining why fixing one site alone
  would have left the whole muon layer on float64.
- `_DPS_DEFAULT = 70` (was 50).

Landed commits: `83ede53aad7`, `14a9e822427`, `0218c9ba9ad`, `8d3d1af6a9a`,
`cacbddcffb1`, `cbe26df665c`.

## And the audit's section-3 residual -- the one bigger than the fix -- is CLOSED. Measured.

`docs/audits/2026-09-12-uic-float64-excision.md` S3 records that
`q_hook_product` / `q_factorial` / `wedderburn_weight` were left `mpf`-typed and
float64-**valued**, worst relative **1.0212424e-15** at lambda = (2,2) against
**2.4946976e-16** removed -- "the residual is 4x what was removed" -- and defers
the root fix to the owner on the strength of a 124-file / 243-witness blast
radius. **That paragraph is superseded.** The root `q_int` fix landed, and the
same arc gave each primitive an explicit precision context with a floor
(`_DPS_FLOOR = 50`, `mp.workdps(d + 10)`, return rounded to `d`), which is the
other half: mpmath rounds to the CONTEXT's precision, so an exact `q_int` into
an `mp.mpf("1.0")` accumulator under a bare-import ambient `mp.dps` of 15 would
still have thrown the exactness away one multiplication at a time.

Measured on main at `cacbddcffb1`, python3.13 / mpmath 1.4.1, over **125
quantities** (every partition of n = 3, 6, 9, 12, plus the four `q_factorial`),
as self-consistency across ambient precision -- which needs no reference `q` and
so cannot be contaminated by the input question:

    worst | f(ambient 15) - f(ambient 120) | / f(ambient 120)
        = 1.1575853e-51   at lambda = (5,3,2,2), n = 12

Had the ambient trap been live this would sit near 1e-16. So the arithmetic is
ambient-independent to ~1e-51, and the cone is no longer float64-limited in
three of its four factors.

**A measurement of mine that was wrong, and how.** A first pass compared the
module's output against a 120-dps product built from `Q_50_DIGIT_STR` and got
**3.9873e-49**, ambient-independent across dps 15/50/70/100. That is not an
arithmetic error: `q_int` resolves its `q` from `q_parameter` module globals at
call time with its own cache, which is not `Q_50_DIGIT_STR`, so the figure
measures a difference between two `q` values. Do not quote it. The
ambient-sweep flatness is what exposed it -- a genuine floor artifact would have
shrunk once ambient passed 50.

**What the self-consistency test does NOT establish.** It bounds the arithmetic,
not the absolute accuracy against the true `q`. The input ceiling is a separate
and still-open fact, and it is this bean's line-60 item: `_Q_MP` is built from
`Q_50_DIGIT_STR` and carries ~50 significant digits while `OUTPUT_DPS = 60`.
`pyhecke.wedderburn._DPS_FLOOR = 50` is a second expression of the same ceiling
in the same cone. So a value serialized at 60 digits out of these primitives
still has ~10 digits nothing supplies.

**`qou-5eg1` is NOT re-created as a separate bean, deliberately.** Its file is
absent from the authoritative store (`cat/cat-harness/beans`) -- it existed only
on the #7439 branch -- and its one surviving open item is exactly the line-60
channel above. Minting a second bean for it would duplicate this one. The
`_DPS_DEFAULT` half of `qou-5eg1` is landed and closed; the
`mpf(Q_50_DIGIT_STR)` half lives here.

## 2026-11-20 -- owner selected ALL FOUR options; option 1 (identification) is DONE

Put to the owner as four options; the answer was all four. Sequencing finding
recorded first because two of them interact: **option 3 (close the input
ceiling) must land before option 4 (refresh)**, since closing the ceiling moves
the values a refresh would write, so refreshing first means refreshing twice.
Option 2 (binding shape) touches none of the same files and runs in parallel.

### Option 1 result (READ-ONLY; no producer run, no witness written)

[`computations/audits/exposed_witness_identification.py`](../computations/audits/exposed_witness_identification.py),
write-up `docs/audits/2026-11-20-exposed-witness-identification.md`.

| surface | producers | witnesses >50 digits | coarse (no-op) |
|---|---:|---:|---:|
| A  wedderburn trio / q_dimension | 77 | -- | -- |
| B  q_int( | 142 | -- | -- |
| **A u B -- the LANDED fixes (option 4)** | **182** | **88** | 33 |
| C  mpf(Q_50_DIGIT_STR) -- the ceiling (option 3) | 811 | **461** | 134 |

A u B and C are disjoint by construction; without the exclusion C is 498, so
they overlap on 37. 3625 tracked witnesses, 4773 scanned .py.

**Option 4 is 88 witnesses, not 243.** The 243 was a whole-repo count by a
different predicate two months ago, before either fix landed. 33 further
exposed witnesses are too coarse for the fix to show, so refreshing those is a
no-op diff.

**434 witnesses (12 %) record no producer at all**, plus 8 recording an
untracked one. No triage of this shape reaches them; `scriptFile` would have to
be backfilled at the producer first. Neither cleared nor implicated.

### I quoted option 3's cost to the owner WRONGLY, and it is corrected here

Option 3 was put to the owner as "`constants.py` + `wedderburn.py` plus the
consumers that serialize at 60". Measured: **809 producers call
`mpf(Q_50_DIGIT_STR)`**, and **486** of them back a witness fine enough for the
cap to show. That is ~6x option 4 and is not a two-file change. Re-put to the
owner with the real figure rather than started.

### Two things I had wrong about the ceiling itself

- **The `*_MP` family is NOT truncated at 50.** `Q_MP = q_at(_DPS_DEFAULT)` with
  `_DPS_DEFAULT = 70` since `14a9e822427`, and the other ten derive from it
  inside `workdps(70)`. Referencing an `_MP` constant is the full-precision
  path. This bean's own line-60 item should be read as naming the
  `mpf(Q_50_DIGIT_STR)` channel specifically, not the `_MP` family.
- **`pyhecke.wedderburn._DPS_FLOOR = 50` is a FLOOR, not a cap.** `_wdps()`
  returns `max(mp.mp.dps, 50)`, so it raises precision when ambient is low and
  never lowers it -- which is exactly why the ambient sweep is flat at
  1.158e-51 across dps 15/50/70/100. No change to it is needed and it is not
  part of the ceiling.

So the ceiling is ONE channel: `mpf(Q_50_DIGIT_STR)`. `Q_50_DIGIT_STR` itself
must NOT be changed -- its name is its specification and 1216 files import it;
the fix is to move value-consumers onto `Q_MP`, which is already 70 digits.

### Two blind spots in my own audit, found by running it

Both in the detector, both fixed before commit, both recorded because the
audit's numbers would otherwise read as corpus facts.

1. **Family C measured the wrong thing** -- it keyed on `\b[A-Z][A-Z0-9_]*_MP\b`
   (not a ceiling, see above) and that regex cannot match `Q_50_DIGIT_STR`,
   which does not end in `_MP`. The one real channel was invisible to it:
   401 -> 811 producers, 264 -> 461 witnesses on the fix.
2. **The auditor counted itself** -- it names every family-A function in its own
   `A_FUNCS` tuple, so the derived calibration read 96 against 95 and the run
   refused to print. Excluded by path now.

A first version over-matched **6x** (1519 candidates) because its one-hop rule
flagged any producer importing `q_parameter`, which DEFINES `q_int` -- exposure
to the module rather than to the fix, 2463 of 4773 producers. Direct calls only.

The calibration is a **derived identity**, not a band: the audit's "124 files"
is whole-repo (132 = 23 fsh-guts/deprecated + 10 docs/audits prose + 99 live
code), this scan excludes the qou-mass mirror (3) and tools/sage-examples (1),
so it must read exactly 95 -- asserted, exit 2 on a miss. Per taxonomy row 45,
an audit that self-certifies its calibration cannot find its own blind spot;
both of the above were caught by that assertion or by use.

Bounded scope gap, stated because it is checkable: a second computations tree
exists at `folio/quantum-observable-universe/computations/`, measured at **2**
.py files and **2** witnesses. A gap, not a tree.
