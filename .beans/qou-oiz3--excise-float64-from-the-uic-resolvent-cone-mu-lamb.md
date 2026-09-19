---
# qou-oiz3
title: excise float64 from the UIC resolvent cone (mu_lambda, s_*) -- owner directive 2026-09-12
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T20:47:33Z
updated_at: 2026-09-19T06:26:14Z
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


## Stage 1 landed (PR #7440, 2026-09-19) — and BOTH recorded figures were wrong

Owner-authorised as its own tranche with a witness-refresh budget. **Stage 1 is
staging only: an audit script and a doc, no source change, zero witnesses moved.**
`qou-oiz3` stays **in-progress** — stages 2–5 are scoped and NOT started.

**The file PR #7245's report named for this defect was wrong.** `q_int` is not in
`tools/pyhecke/python/pyhecke/wedderburn.py`; it is at
`tools/qou-substrate/python/qou_substrate/constants.py:190`, over the binary64
globals `Q` (:150) / `Q_INV` (:177) / `HA` (:178). Verified 2026-09-19.

**There is a SECOND float64 definition**, `computations/substrate/q_parameter.py:169`,
which redefines `q_int` over the MUON globals inside the `ideal`-anchor branch as
default arguments. A grep of `qou_substrate` does not see it. `q_int_at` /
`q_int_classical_at` are already exact and already `raise` in the no-mpmath branch —
they are not part of the fix.

### The blast radius, re-measured against `origin/main` 665c91e403a

The "124 python files, 243 witnesses" above is **two different questions conflated**,
and it is wrong in opposite directions for each:

| question | measured | recorded | verdict |
|---|---|---|---|
| files **mentioning** `q_hook_product`/`q_factorial`/`wedderburn_weight` | **105** | 124 | **HIGH by 18 %** |
| **value cone** (importers of the q_int-derived Hecke layer) | **1290** | 124 | **LOW by 12.3×** |
| committed witnesses with a producer in that cone | **917** | 243 | **LOW by 3.8×** |
| …carrying ≥30 significant digits — the real refresh budget | **673** | — | — |
| shim cone (importers of the constant modules) | 3921 | — | not a measure of this defect |

Reproduced by `computations/audits/q_int_float64_cone_audit.py` — a script, not a
figure, because a hand-kept count here decays (AGENTS.md's own importer table was
wrong by two orders of magnitude). One trap recorded in it: resolving a dotted
import by its LAST component puts `qou_substrate.constants` and `pyhecke.constants`
in one bucket and reports the cone as **3921 — the entire corpus**.

### The error is NOT bounded by float64 eps — it grows with the tower

80 dps, proton pin, swapping only `q_int` in `pyhecke.wedderburn`:

| n | blocks | worst λ | rel move | × eps |
|---:|---:|---|---|---:|
| 3 | 3 | (3) | 3.0495805e-16 | 1.4 |
| 4 | 5 | (2,2) | 8.804973e-16 | 4.0 |
| 6 | 11 | (4,1,1) | 8.7499765e-16 | 3.9 |
| 9 | 30 | (3,3,1,1,1) | 1.6189461e-15 | 7.3 |
| **12** | **77** | **(4,4,2,2)** | **2.4104405e-15** | **10.9** |

`q_factorial(n)` multiplies **n** float64-valued factors. `n = 12` is the A = 4 atom,
and 2.41e-15 is **2.4× the framework's own L1 target of 1 ppQ** — so this is an L1
miss in the Wedderburn-weight layer, invisible because the values are `mpf` and
print 40 digits.

**This corrects the λ=(2,2) residual above.** The `1.0212424e-15` recorded there is
with this branch's `μ_λ` excision applied; the **pure-weight** move is
**8.804973e-16**. Different quantities — do not reconcile them into one number.

**Secondary finding confirmed, and it is a separate defect.** `Q_MP = q_at(50)`
(`_DPS_DEFAULT = 50`, constants.py:247/:331) while `COMPUTE_DPS = 70` and
`OUTPUT_DPS = 60`; measured `|Q_MP − q_at(90)| = 1.1000161e-51` this session (bean
records 9.9102461e-52 — same order, different working precision). A producer that
calls `set_compute_dps()` and `fmt`s a `Q_MP`-derived value at 60 digits publishes
~10 manufactured digits. Its consumer base is the **shim** cone (3921 files), i.e.
far wider than q_int's. Not fixed by this arc.

### Why no source change, and what the stages are

A `wedderburn.py` edit is an **import-cone** change: producers' own bytes do not
move, `witness.scriptHash` never drifts, and **no gate in the tree flags any of the
917**. That is `cosmetic_import_cone_drift`, the only `witness_staleness_triage.py`
bucket that has grown across five measurements (4 → 9). Landing the code without
the refresh leaves 673 witnesses publishing wrong digits with every detector green.

Partition, measured:

- **(d) anchor-defining in cone: 0.** `q_pinning_50_digit` is **NOT** in the cone —
  this arc cannot re-run the 2026-08-19 `Q0_FLIP` 262-witness breakage.
- **(c) refuse by design: 3** — `atomic_tr_m_mpfr_50dps`,
  `he4_stage2_ranking_seminormal_xcheck`, `cross_check_trM_1ppb`; all three of the
  producers AGENTS.md names are in the cone.
- **(b) long-compute:** `phi-per-nucleon-orbit-exhaustion` 2558.5 s,
  `he4-binding-k-stage2` 2086.2 s, `chi-lambda-he4-full-partition-table` 317.1 s
  (their own witnesses); plus `binding_energy(1,1)` **1233.9 s** for ²H and
  `hadron_knot_table` **>50 min / exit 124**, both in the cone, neither recording a
  time.
- **(a) cheap: ≤ 906** — an upper bound only: **888 of 917 record no timing field**,
  so the wall-cost partition is not measurable from the witnesses.
- **8 of the 19 `ideal_muon` producers are in the cone** (3 of them the refusals, a
  4th `hadron_knot_table`), against 350 of 914 `physical_proton`.

**The fix recipe is verified, not proposed.** Route through `q_parameter.q_at` (the
muon branch rebinds it), never `q_int_at`'s proton default — otherwise the swap
silently re-pins those 8. Checked under both anchors: `QOU_Q0_ANCHOR=''` gives
`[4]_q` f64 `4.109682411207942` vs exact `4.1096824112079411617605687891`
(rel 1.4425e-16); `QOU_Q0_ANCHOR=ideal` gives `4.109682435806692` vs
`4.10968243580669280986579456072` (rel 1.12725e-16).

Stage 2 alone is ~250–300 producer runs of largely unknown wall cost, against an
idle-pass budget AGENTS.md caps at 3 witnesses. **It is not one tranche.** Highest-
value next step is empirical: sample ~20 in-cone producers, run twice, and measure
how many witnesses ACTUALLY move rather than how many could. Not run here — this
checkout is shared with a live sibling session and producers write sibling witnesses.

Full plan: `docs/audits/2026-09-19-q-int-float64-root-staging.md`.
Intent posted on #7438 (assembly-chain float casts) and #7318 (raw-float64 drain);
neither touches `constants.py` / `q_parameter.py` / `wedderburn.py` / `hecke_*`.
