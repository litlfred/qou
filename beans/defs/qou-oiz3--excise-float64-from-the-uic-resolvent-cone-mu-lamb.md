---
# qou-oiz3
title: excise float64 from the UIC resolvent cone (mu_lambda, s_*) -- owner directive 2026-09-12
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T20:47:33Z
updated_at: 2026-11-15T13:30:00Z
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
