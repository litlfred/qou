---
# qou-oiz3
title: excise float64 from the UIC resolvent cone (mu_lambda, s_*) -- owner directive 2026-09-12
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T20:47:33Z
updated_at: 2026-11-20T17:26:36Z
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

## 2026-11-20 -- option 3 CLASSIFIED, deliberately NOT swept

`docs/audits/2026-11-20-q50-digit-cap-classification.md`,
`computations/audits/q50_digit_cap_classify.py`.

**The fix direction is proved.** At mp.dps 120 against an independent
`q_at(110)` solve: `mpf(Q_50_DIGIT_STR)` sits 1.91571e-50 away, `Q_MP` sits
6.97057e-72 away -- strictly more correct by 2.75e21, so ASK-OWNER exemption 1.
`Q_50_DIGIT_STR` must NOT change (its name is its spec; 1216 importers); the fix
is at the consumer.

**Why the sweep did not run.** 809 files contain the text; 6 are prose-only;
**803** are real call sites; and **206 of those want 50 digits DELIBERATELY** --
**159 emit an artifact whose own NAME says `50dps`**, so re-pinning their q to
70 digits makes the name a lie while the run still exits 0. A sed would have
corrupted them silently. 589 fixable, 8 with no import to extend; of the 589,
**322** back a witness fine enough for the change to show.

**A figure of mine is WITHDRAWN: the "6 of 6 MOVED".** It compared
patched-vs-committed, so it charged environment churn to the patch -- installing
`pyhecke_native` strengthens the recorded `environment` block and the producer
announces it on stdout. The tell: one of the six, `chi_at_q0_via_matrix_m_mpfr`,
is **prose-only** and never calls the pattern, so it could not have moved from
the substitution. With a control arm in the SAME environment (unpatched -> A,
patched -> B, compare A vs B) the sample completing both arms is **1 MOVED /
1 IDENTICAL**. n = 2. No rate is claimed, and the earlier one should not be
quoted.

**Environment, because it gates every measurement here.** A bare container runs
none of these producers: `sympy`/`numpy`/`scipy` absent (the first sample's five
"IDENTICAL" were rc=1 `ModuleNotFoundError` in 0 s, reported as agreement by a
verdict that never required a successful run -- a verdict must be unreachable
when the run failed); `mpmath` 1.3.0 under `python3` against a corpus needing
1.4.x; `pyhecke_native` not on PyPI, but `maturin build --release` in
`tools/pyhecke-native/` works and gives a cp311 wheel. **171** capped producers
reference it.

**Next, in order:** (1) fix the patcher for parenthesised multi-line imports --
it is why 7 of 10 A/B candidates read UNPATCHABLE, a harness limit not a corpus
fact; (2) A/B a real sample of the 322 with the control arm; (3) sweep the
fixable set EXCLUDING the 206, in reviewable batches, each with its witnesses
refreshed in the same commit. The 206 keep their pin; any one of them being an
accident is a per-file judgement, never a sweep.

## 2026-11-20 -- option 3 SWEPT (588 files) and PARTIALLY refreshed (97 of ~588)

Owner: "Fix any identified issues" / "Go". PR #8560, commits `e925b93b8fb`
(source), `9381528d263` (witnesses).

**Applied.** `mpf(Q_50_DIGIT_STR)` -> `Q_MP` in **588** consumers; the **207
deliberate** pins left alone (159 emit an artifact whose own name says
`50dps`); 1 refused (`borromean_convention_by_evaluation.py`, no ImportFrom to
extend). Three gates, all green on 588/588, any failure reverting the batch:
all parse; zero carry `<alias>.Q_MP`; zero retain a residual call -- checked
through `code_only()`.

**Mover rate 10/20 = 50 %** (A/B, control arm in the SAME environment).
Refresh so far: **97 witnesses rewritten, 61 payload-changed (63 %)**, 36
provenance-only.

### THE REFRESH IS PARTIAL AND THIS IS THE DEBT

~440 producers now carry `Q_MP` in source while their committed witness still
holds the 50-digit value -- genuine `scriptHash` staleness, created
deliberately by this sweep. The run's last checkpoint is 100/589
(ok=82 fail=7 timeout=11) and it was stopped partway into the next 50. The tail
is long-compute: producers past ~100 hit the 45 s budget steadily, which
AGENTS.md says to claim as a bean rather than force. **Next agent: resume the
refresh from ~producer 150 of
`q50_digit_cap_classify.py --emit <dir>`'s fixable.txt ordering.**

### A PATCHER BUG THAT ACTIVELY CORRUPTED FILES, caught by the control arm

The call prefix is a MODULE ALIAS and must be CONSUMED. A pattern allowing only
`mpmath.` or bare matches the `mpf(...)` SUFFIX of `mp.mpf(...)` and rewrites it
to `mp.Q_MP` -- `AttributeError: module 'mpmath' has no attribute 'Q_MP'` at
import. Measured distribution of the 871 sites: **`mp.` 661, bare 197,
`mpmath.` 10, `_mp.` 3** -- so it broke **76 %**. It surfaced as 14 of 20 A/B
candidates failing their PATCHED arm while their CONTROL arm passed. Without
the control arm this would have been read as the corpus being fragile.

### Four measurement figures of mine, all withdrawn

1. option 3 costs "two files plus consumers" -> **486 producers**;
2. "6 of 6 MOVED" -> environment contamination (the tell: one of the six is
   **prose-only** and never calls the pattern);
3. "the patcher fails on parenthesised multi-line imports" -> **invented, not
   observed**; 588 of 589 imports are SINGLE-line and the real cause is a
   trailing `# noqa: E402` defeating a `$` anchor, hitting 535 of 589 (91 %);
4. exposure family C keyed on `*_MP` -> that is the FULL-precision path
   (`Q_MP = q_at(70)`) and the regex cannot match `Q_50_DIGIT_STR` anyway.

### Environment, checked rather than waved past

The refresh records mpmath 1.4.1 / python 3.11.18. That is a CONVERGENCE, not a
deviation: `tools/qou-substrate/pyproject.toml` declares `mpmath>=1.3,<1.5` and
the committed corpus already records **1.4.1 on 1505 witnesses against 976 at
1.3.0**. Payload figures mask the environment block, and the 50 % rate is
attributable to the q change because both A/B arms ran under 1.4.1.

A bare container runs none of these producers: `sympy`/`numpy`/`scipy` absent,
mpmath 1.3.0 too old, `pyhecke_native` not on PyPI (`maturin build --release`
in `tools/pyhecke-native/` works; **171** capped producers need it).

## 2026-11-20 — the two ratchet regressions were NOT the sweep; both producers fixed

Both raw-float64 REGRESSED entries after the 70-digit q sweep are closed. Both gates green (ratchet exit 0, 0 NEW / 0 REGRESSED, drained 78 files / +7,548 fields; padding exit 0). Commits `568693ba12c` (producers) and `da44c4efb5a` (221 witnesses).

**The ratchet counts only NONZERO raw floats.** In both files the float64 was always present and merely masked by the fields being exactly 0.0, so neither 'regression' was introduced by the sweep. A 3 -> 6 on this gate can mean 'three zeros became nonzero', not 'three new float64 paths'.

### probe_d_dressing_is_proton_net
Five serializations used `float()` beside neighbours using `mp.nstr`; now `_precision.fmt`, and the assertions pass strings per `add_assertion`'s own docstring contract (qou-t0rf). Raw floats 7 -> 0.

TRAP, and I got this wrong first: the `binding_candidate_subpercent` failure is **not** the q fix. Control arm (pre-patch source, same container) fails identically. The cause is import-cone drift over 4.5 months — `Delta_tr` moved **4.047x** (0.59517 -> 0.14705) through `tr_m_atom_via_transfer` (the module AGENTS.md already names as THE drift culprit), carrying `B_cand` with the identical ratio while `h`, `net_p`, `net_n`, `abs_delta_net` are unchanged to the last digit. Comparing every recorded quantity by ratio is what isolated it: the two that moved share one factor, and the six that did not bound the cause.

### habiro_q_difference_fourier — a provably-wrong pole classification
`sp.simplify(den.subs(u, zeta)) == 0` is a heuristic zero-test that leans on mpmath, so its verdict flipped with 1.3.0 -> 1.4.1. It had the pole structure **backwards**: pole at d=4, none at d=8. `den_p = 4u^18(u^4+1)^2` gives `u^4 = +1` at zeta_4 (value 4, no pole) and `u^4 = -1` at zeta_8 (value 0, genuine pole). Replaced with **exact cyclotomic divisibility over Q** — zeta_d is a root of a rational polynomial iff the d-th cyclotomic polynomial divides it, by polynomial remainder. Deterministic, no floats, agrees with the hand factorisation. The refreshed witness is CORRECT; the committed one was WRONG.

Also `complex(sp.N(expr, 30))` computed at 30 digits then cast to float64, discarding everything past ~16: d=5 now carries 61 significant digits. Raw floats 24 -> 0. Two hardcoded narrative facts had gone stale — the quoted `|tr_M(p)|=0.6614`/`|dtr_M|=1.5612` (live 0.25 / 0.4330) and a pole asserted at zeta_4 from 'D(u)=4u^19(u^2+1)', which is **not** the live denominator; both now derived from the computation.

### 8 near-match assertions do not reproduce — and the sweep is NOT the cause
Across the 221: 72 moved only below 1e-9 (the intended gain), 12 only in near-zero residuals, 38 material, **8 flipped pass -> fail**. All eight are tightness claims (`sub_ppm`, `residual_under_10ppm`, `S_near_1_plus_hsq`, `ratio_near_qfact5`, `gap_is_sub_ppm`, `deuteron_dressed_subpercent`), six under `habiro/` — the shape of a near-match holding only at 50 digits. Control armed all eight: **7/7 testable fail identically without the patch** (nastokes will not run pre-patch here; inconclusive). **No anti-fit conclusion drawn.** What stands: eight committed sub-ppm claims do not reproduce, for reasons predating this branch — container move (mpmath 1.4.1, python 3.11.18) and/or cone drift, not separated per-witness.

METHOD NOTE (cost me two false claims this session): 'payload-changed' is a useless metric for a precision sweep — 93% of 221 changed, almost all at digit 51. And a relative diff on a residual whose baseline is ~1e-50 reads as 1e+8. Mask timing fields, exclude near-zero baselines, and count **assertion flips**; that is the signal.

**Open decision handed to the owner:** the content block `mass-theory/deuteron-binding-dressing-proton-net.md` asserts +0.12% of AME2020 twice and declares this producer's witness as its source; that witness now reads -75.25%. Not touched — a claim change is not a precision fix.

## 2026-11-20 (C) — the 4.047x Delta_tr move is an OWNER-RULED CORRECTION, not drift

Answered, and it corrects two of my own claims from earlier today.

**Retracted:** I attributed the move to `806d5146227` (2026-11-15, weak chirality) on the strength of `--stat` showing '289 insertions, 0 deletions'. **That commit is a SHALLOW BOUNDARY commit** (it is in `.git/shallow`), so the whole-file-added diff is a fetch artifact. The file was not created then. TRAP: in this clone, `git show --stat <boundary-sha>` reports every file it touches as newly added. Check `.git/shallow` before reading an add as an add.

**The real cause, from the module's own docstring and then the ruling commit:** `atom_braid_word_3A` switched to the interleaved Borromean intra word on **2026-09-05** (`7db032fb48`, owner ruling, bean `qou-hu1f`). `nucleon_gen_chains` commented its B_3 confinement letters as `(sigma_0 . sigma_1^-1)^3` and returned them **bucketed by generator**, so consumers emitted `sigma_0^3 sigma_1^-3`. sigma_0 and sigma_1 do not commute, so that is a **different element of H_3(q)** — 82 % away at q0, where the interleaved word matches the Lean closed form to **5e-60**.

So the pre-2026-09-05 Delta_tr was computed on the **wrong object**, not merely an old one. The `grouped` intra_order path survives, so every published number stays reachable.

**The live value is corpus-consistent, checked three ways rather than assumed:**
- `tr_m_atom_via_transfer` cross-checks `tr_M^atom(D)` against the INDEPENDENT Hoefsmit witness (`atomic-tr-m-mpfr-50dps-proton`, `0.15196833920423160759266569775106`) and passes — and *refuses* a cross-pin reference (q0Value is the proton pin).
- 16 witnesses carry the live Delta_tr against 1 straggler (refreshed in `e8eeb61cfe5`).
- The module's own two assertions are green.

**Stale figure to not repeat:** the module docstring still claims 'tr_M^atom(D) ~ 0.388 (matches the #2080 canonical_tr_m_via_branching value)'. Live is **0.15196834**. AGENTS.md records this quantity as having moved 0.388 -> 0.575; it has now moved again. The module's *assertion* is fine — it compares against a witness, not against the docstring — so the docstring is unguarded prose. 404 files reference `atom_braid_word_3A`.

## 2026-11-20 (B) — magnitude comparison withdrawn, no replacement asserted

`e8d6c9d6374`. `mass-theory/deuteron-binding-dressing-proton-net`: the two `+0.12 %` sites and the `+11.99 %` beside them are withdrawn with the (C) evidence cited inline; a 2026-11-20 `authorNotes` status entry supersedes the 2026-07-04 one (kept as a dated record). The live chain reads **-72.33 % undressed -> -75.22 % dressed** — the dressing now makes the deuteron *worse* — recorded as a measurement, NOT adopted as the block's claim, because that is a re-derivation rather than a renumbering.

`computation.status` **verified -> failed**; the schema is explicit ('script ran, witness does NOT match expected values') and `check-computation-status.py` went 1 disagreement -> 0. Unaffected: the proposition (stated for ANY Delta_tr) and its Lean.

Render-QA preflight battery GREEN (11 checks). The pipeline render is **unavailable** here — the platform is a mounted copy, not a checkout — so the .md is NOT machine-render-validated; stated rather than implied. qa-sweep loads at pin `82b3899` (contra `qou-4jhp`, which reports it failing at `b61e856`) but cannot write sidecars in this container; the committed sidecar is now legitimately stale against the edit, and the attestations file it extracted carries only the OLD field hashes, so nothing attests the new prose.

**next** (D) refreshing the 62 sweep producers still stale by scriptHash — background, ~3.8 h ETA. Scope correction: I told the owner '~100'; the measured figure is **62**. Corpus-wide staleness is far larger (511 distinct stale producers, 472 of them outside the sweep) and is NOT in scope here.

## 2026-11-20 (D) — ENVIRONMENT PROVENANCE: a refreshed witness can move 8 orders unattributably

`759b857c454` reverts `computations/fusion-process-joint-h15-lp.witness.json`, committed in `5428c9c053e`. This changes how the rest of D must be committed, so it is the entry to read.

**What happened.** Three assertions flipped and my commit message said only 'gates green':

    initial_split_multiplicativity   4.24682e-10 (tol 1e-8)  ->  0.127464
    final_split_multiplicativity     2.51527e-9  (tol 1e-8)  ->  0.509668
    active_support_invariant         7, expected 7           ->  6, expected 8

Eight orders on a multiplicativity residual is not a precision effect.

**The sweep is NOT the cause** — control arm byte-identical (0.127464 / 0.509668, both failing). That is **8 of 8** control arms this session exonerating the q patch. The pattern is strong enough to state as a rule: *on this branch, assume a moved witness is NOT the patch until a control arm says otherwise.*

**RETRACTED diagnosis (mine).** The producer tries clarabel (pyhecke_native) and falls back to scipy when absent, and clarabel was not importable — a textbook 'producer branches on what is installed'. I took that for the cause. Installed clarabel 0.11.1 and re-ran with the backend genuinely recorded `clarabel`/`clarabel-mpfr`: **results UNCHANGED**. Not the solver.

**TRAP worth keeping:** in this container `pip` is **python3.13**'s while `python3` is **3.11.18**. `pip install X` reports success and `python3 -c 'import X'` still fails; it also resolves cp313 wheels. Use `python3 -m pip`. This cost me a wrong 'not installable' conclusion on SnapPy too.

**The residual cause is environment provenance.** This container is python 3.11.18 / mpmath 1.4.1 against the witness's 3.11.15 / 1.3.0, and `pyhecke_native_build` moved `110b330d42788fa0` -> `930c010e26215e56` because I rebuilt the extension this session. mpmath cannot be downgraded to test while the refresh is mid-run and using it.

**Consequence for how D finishes — the commit gate.** A refreshed value I cannot attribute, that moves a result materially, does not belong in the corpus. The remaining ~50 are to be committed only when the move is EITHER (a) below 1e-9 — the intended precision gain — OR (b) attributable, as probe_d's 4.047x was to the 2026-09-05 word ruling and cross-validated against the independent Hoefsmit witness. Anything else is flagged for a canonical-environment re-run, not committed. Bulk-committing D's output is no longer appropriate.

**Scope, measured not assumed:** exactly **1** of the 221 in `da44c4efb5a` carries LP/SDP dual fields — `probes/collision-gradient-lagrangian-probe` — and it is **sound**: every assertion passes both ways and its `primal_obj`/`dual_obj`/`y0_star` moved only at the ~50th digit (`…089723648607` -> `…088136197499`). No other committed witness is implicated.

Known D skips: `atomic_chirality_residue` (timeout 420s), `fitted_ideal_low_isotope_calibration` (rc=1, 'cannot create mpf from None' — real producer defect, pre-existing), `m_tau_complex_volume_search` (SnapPy absent).
