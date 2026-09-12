# Excising float64 from the UIC resolvent cone

**Date** 2026-09-12 · **Bean** `qou-oiz3` · **PR** #7245 ·
**Branch** `claude/uic-float64-excision-2026-09-12`

## 0. The directive

Owner, 2026-09-12, verbatim:

> **excise float64**

It follows the report of PR #7237 (bean `qou-t6be`), which found the defect and
deliberately did not fix it:

> `μ_λ` and `s_*` are float64 (`hecke_core_legacy.py:292`, `:520`). Worst gap vs
> `mpf`: **2.54432e-16** — *the floor of float64*, so it bounds the damage at
> ~1e-16 and **cannot** distinguish correctly-rounded from slightly-wrong.
> Fixing it moves every binding number.

This audit records what the surface actually was, what the numbers did, and —
the part that matters most — **what is still float64 after this PR**, which is
larger than what it removed.

## 1. The surface: nine sites, not two

The two cited lines are where #7237 looked. Measured over
`unified_iterative_correction`'s call cone and `binding_energy`'s, on
`origin/main` (line numbers are `origin/main`'s):

| # | site | `origin/main` | what it was |
|---|---|---|---|
| 1 | `q_laplacian_eigenvalue` | `hecke_core_legacy.py:292` | `casimir_sum = 0.0`, accumulating `q_int(c) * q_int(c+1)` over the **float64** `q_int` |
| 2 | `S_REEB_PLANCK` | `:520` | `(q0 - 1.0) / q0` over the float64 `q0` |
| 3 | `q_resolvent_weight` | `:325` | `1.0 / (mu + s)`, with a float64 default `s` |
| 4 | `_partition_table` | `:544` | `_resolvent = 1.0 / (_mu + S_REEB_PLANCK)` |
| 5 | `_partition_table` | `:539` | `_log_rho = math.log(_rho)` on an `mpf` ratio |
| 6 | `partition_spectral_log_rate` | `:508` | `math.log(ratio)` — the same defect in the function the table restates |
| 7 | `partition_character_sigma1` | `:491` | exact `Fraction`-guarded SYT counts multiplied by the float64 `q0`/`qi`/`h` in the last line |
| 8 | `conjugate_pair_cross_term` / `unified_iterative_correction_jet` | `:2517`, `:2527`, `:2641` | `hbar_like = float(h)`, then `_math.sqrt` on an `mpf` MeV scale |
| 9 | `atom_markov_trace` / `atom_frobenius_norm_sq` | `:2781`, `:2830` | `_math.exp(ln - max_ln)` on an `mpf` log-norm |

Sites 1–7 are on the `unified_iterative_correction` leg; site 9 is on the
`binding_from_frobenius_pairing` leg of `binding_energy`, which #7237's framing
did not reach.

Sites 7 and 8 are the pattern AGENTS.md names verbatim — *"`hf = float(G.h)`
followed by arithmetic against it is a computation, not a display"*. In site 8
the cast is even a no-op (`h` is already a Python float); the arithmetic is the
defect, not the cast, which is exactly why a `float(` grep is a weak detector
here.

### 1a. A tenth defect that is not a line at all

`_partition_table` is a **cache**, materialised once per process and reused.
mpmath rounds every operation to the **ambient** `mp.dps`, which is **15** in a
bare import of this module. So the precision of every `mpf` in that table was a
function of *who touched it first*:

- 70 digits when `unified_iterative_correction` got there first — it carries its
  own `workdps(COMPUTE_DPS)`;
- **15** when any other consumer did — and `_ensure_ysn_attached`, eight probes
  and two audits reach `_PARTITION_TABLE` outside any precision context;

with no signal either way. Measured on `main`: `q_factorial(4)` is
`25.15363700485133338303819153288353870856` at `workdps(70)` and
`25.15363700485133335860155057162046432495` at the ambient 15 — they part
company at the 17th digit. The body is now wrapped in `workdps(COMPUTE_DPS)`.

### 1b. One deliberate float64 boundary, added

`sdp_cross_channel.py` gains `_f64_for_solver`. cvxpy/SCS is a float64
numerical solver and cannot take an `mpf` coefficient, so every `μ_λ` reaching
a cvxpy expression is narrowed **at the solver call** and nowhere else. The
scalar-LP fallback (`_scalar_lp_fallback`, which is what runs when cvxpy is
absent — as it is in this container) does **not** cast and keeps the `mpf`.

## 2. What the numbers did

`mp.dps = 70` (`_precision.COMPUTE_DPS`), proton pin
(`q0 = 1.1099785827513808075916…`), convention D. Baseline taken from
`git show origin/main:computations/hecke_core_legacy.py` loaded by path under a
distinct module name — **not** from a working tree the measurement itself
writes to. Totals read as `mpf` out of `per_step[-1]`, not through the public
`float()` return, which would have quantised the answer to the thing being
measured.

### 2a. Per-atom binding totals, `k_exact = 4`

| atom | before (gated, MeV) | after (gated, MeV) | rel | abs (MeV) |
|---|---|---|---|---|
| ¹H  | −0.098109599307044661 | −0.098109599307044642 | 1.85233e-16 | 1.81731e-17 |
| ¹n  | −0.093806476972514165 | −0.093806476972514148 | 1.85233e-16 | 1.73761e-17 |
| ²H  | −0.089559683058950681 | −0.089559683058950664 | 1.85233e-16 | 1.65894e-17 |
| ³He | −0.10951151287181357  | −0.10951151287181354  | 2.32254e-16 | 2.54345e-17 |
| ³H  | −0.10235605915957370  | −0.10235605915957367  | 2.35419e-16 | 2.40966e-17 |
| ⁴He | −0.080586748477691433 | −0.080586748477691416 | 2.13680e-16 | 1.72198e-17 |
| ⁶Li | −0.075419054841717470 | −0.075419054841717456 | 1.82738e-16 | 1.37819e-17 |
| ⁸Be | +0.012299065065498735 | +0.012299065065498724 | **8.44176e-16** | 1.03826e-17 |

Ungated (the running total the per-step rows carry), same run:

| atom | before | after | rel |
|---|---|---|---|
| ¹H  | −14.697711478738904 | −14.697711478738900 | 2.52283e-16 |
| ²H  | −0.41221219224502691 | −0.41221219224502681 | 2.36066e-16 |
| ⁴He | −0.27423977161740013 | −0.27423977161740007 | 1.91484e-16 |
| ⁸Be | +0.0013137055911927322 | +0.0013137055911927235 | **6.65778e-15** |

### 2b. `k_exact = 6`, all eight atoms

Worst gated **2.76139e-16** (²H), worst ungated **2.48916e-16** (²H). Nothing
exceeds 3e-16 at this cutoff.

### 2c. Does anything exceed the float64 floor? YES — say it plainly

float64 machine epsilon is **2.22045e-16**. At `k_exact = 4` the ⁸Be gated
total moves **8.44176e-16**, which is **3.8×** that floor, and its ungated total
moves **6.65778e-15**, **30×**. So #7237's bound — *"the floor of float64 …
bounds the damage at ~1e-16"* — is correct **per block** and does **not**
transfer to the totals.

**The mechanism is cancellation, not error growth, and that distinction is the
honest part of this finding.** ⁸Be's ungated total is 1.3e-3 MeV assembled from
contributions of order 1; the *absolute* shifts are ~1e-17 MeV everywhere,
including there. So the correct statement is:

> The absolute damage was ~1e-17 MeV, uniformly. The *relative* damage on a
> total that arises by cancellation is unbounded by any per-block figure, and
> at ⁸Be it was 30× the float64 floor.

And the thing the old figure could not do, it still cannot do in the direction
people want: **2.54432e-16 was never evidence that the float64 path was
correctly rounded.** What settles that is the recomputation, and the
recomputation says the old values were wrong in the last 1–3 digits of their
float64 representation — which is what "at the floor" means and is *not* the
same as "correct".

## 3. What is STILL float64, and it is bigger than what was removed

`q_hook_product`, `q_factorial` and `wedderburn_weight`
(`tools/pyhecke/python/pyhecke/wedderburn.py`) **return `mpf` and accumulate
`mp.mpf(1) * q_int(k)` over the float64 `q_int`.** They are `mpf`-typed and
float64-**valued** — the "float64 in string clothing" class. So

  `C_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*)`

is still float64-limited through **three of its four factors**; only `m_e` and
(now) `ρ_λ` are genuinely exact.

Measured against an all-`mpf` recomputation over the 31 weighted blocks
(`dim ≥ 2`, `k ≤ 7`):

| | worst relative |
|---|---|
| what this PR **removes** | **2.4946976e-16** |
| what this PR **leaves** | **1.0212424e-15** at λ = (2,2) |

**The residual is 4× what was removed.** The probe asserts both — that the
residual is bounded (a regression guard) and that it is *larger* than what was
removed — so no later reader can quote this PR as having cleaned the cone.

**Why it was not fixed here.** The root fix is `q_int` itself. Measured blast
radius: **124 Python files** reference `q_hook_product` / `wedderburn_weight` /
`q_factorial` / `q_dimension`, and **243 committed witnesses** carry a field
those produce. That is a corpus-wide sweep whose witnesses cannot be refreshed
in this container, and AGENTS.md §"ASK THE OWNER" excludes exactly it —
*"mass-refreshing witnesses or sidecars"* and *"applying a rule from this
document across files you were not sent to"* are **not** exempt. Put to the
owner on bean `qou-oiz3`; the decision is theirs, and the no-op is that the
cone stays ~1e-15 rather than ~1e-52.

### 3a. A second, much smaller residual: the q input itself

`_q_int_mp` is built on `_Q_MP`, the module's single `mpf` q — deliberately the
same constant the seminormal builder uses, because a character and the YSN
matrices it is the character *of* must be evaluated at one q. `_Q_MP` comes
from `Q_50_DIGIT_STR` and sits **9.9102461e-52** from a full-precision
`q_at(90)` solve, i.e. it carries ~50 significant digits — **below**
`OUTPUT_DPS = 60`. A value serialized at 60 digits from it has ~8 digits
nothing supplies.

Recorded, not fixed. It is 36 orders of magnitude tighter than the float64 path
it replaces, and closing it means moving the seminormal builder onto a
different q, which is a separate change with its own blast radius.

**Do not confuse this with the `70 → 90` stability check.** Those are different
facts and the probe checks them separately: `ρ_λ` recomputed at `mp.dps` 70 and
90 agrees to **1.9583756e-71**, but both runs read the same `_Q_MP`, so that
number is the arithmetic reproducing itself and is *silent* about the input.
An earlier draft of the probe's own docstring asserted the stability check
would land near 1e-50 "and not further"; it lands at 1e-71, because it never
touched the input at all. Corrected in the committed version.

## 4. Verification

- **Probe** — [`computations/probes/uic_float64_excision_probe.py`](../../computations/probes/uic_float64_excision_probe.py),
  **12/12**, `mp.dps = 70`, proton pin, convention D recorded. Five checks on
  type (5 scalars) + one on the five derived `_PARTITION_TABLE` columns across
  31 weighted blocks; one AST check over **nine function bodies** for
  `math.log` / `math.exp` / `math.sqrt` / `float(` / `q_int` — by AST over each
  function's own body, not by grep over the file, so a `math.log` in a
  neighbouring function can neither pass nor fail it; one value check that
  `s_*` is a *different number* from its float64 twin; two precision-ceiling
  checks; two residual checks.
- **Precision gates** — see §6.
- **Sidecars** — `scripts/check-sidecars.sh`; see §6.
- **Lean** — none touched.

## 5. Witnesses

Every committed witness downstream of these quantities was identified by
grepping the witness tree for the producing stems and for
`C_lambda_resolvent_MeV` / `q_laplacian_eigenvalue` /
`resolvent_weight_planck`, then re-run. Payload movement was classified with
the volatile keys masked (`timestamp`, `computedAt`, `elapsed_seconds`,
`durationMs`, `environment`, `scriptHash`, `scriptCommitSha`, …), and the
fields that moved recorded, so a mask gap is re-classifiable without another
sweep.

| witness | verdict |
|---|---|
| `probes/uic-sign-forced-by-gate.witness.json` | **MOVED**, 6 fields — every atom's `gated_sum`, ~3.2e-16 relative. Refreshed. |
| `probes/uic-gate-justification-disproved.witness.json` | **MOVED**, 9 fields — `as_is` and `with_proved_y0` on every atom. Refreshed. |
| `probes/uic-word-level-locality.witness.json` | **MOVED**. Refreshed. |
| `probes/uic-a1-vanishing-trace.witness.json` | payload **IDENTICAL** — not committed. Its numbers do not depend on the resolvent scale. |
| `probes/uic_per_block_log_valley_scan_probe.witness.json` | payload **IDENTICAL** (only `durationMs`, 12 → 15 ms) — **reverted, not committed.** Committing a witness whose only diff is a timing field is noise. |
| `probes/uic-float64-excision.witness.json` | new, committed with its probe. |
| `probes/uic-binding-a-series-kernel-live.witness.json` | **NOT refreshed — too slow here, deliberately left.** See below. |

**The one that could not be re-run, and exactly why.**
`uic_binding_a_series_kernel_live_probe.py` calls `binding_energy(Z, N)` — the
production entry point, not the accumulator — for five atoms at A = 3…5.
Measured in this container, **`binding_energy(1, 1)` alone takes 1233.9 s**
(20.6 min) for the *smallest* bound atom, and A = 3…5 are strictly larger. The
probe did not produce its first row within the session's window. Its witness is
left **untouched**: hand-patching the five `B_pred_MeV` strings would be exactly
the move AGENTS.md forbids, and a partial re-run is worse than none. Tracked on
`qou-oiz3`.

That witness is stale in a quantifiable way: post-fix,
`binding_energy(1, 1) = -7.271102124876745` against the committed
`-7.271102124876717`, a relative move of **3.9e-15**. **That figure is NOT
attributed to this change** — no baseline `binding_energy` run completed in this
container either, and the committed value was produced on a different `main`
with a different import cone. What can be said is that the witness is stale and
by roughly how much; what produced the staleness is undetermined.

**An independent defect in that same witness, not caused here and not fixed
here.** `binding_energy` returns `float(B)` at the public boundary — a
deliberate, documented contract (bean `qou-sv7h`; an `mpf` raises
`TypeError: Object of type mpf is not JSON serializable` at
`hadron_knot_table`'s `round(B, 4)`, verified in #6427). The probe then `fmt()`s
that float to 60 digits, so `B_pred_MeV` reads
`-7.27110212487671700000000000000000000000000000000000000000000` — 17
significant digits and **43 zeros that assert a precision nothing supplies**.
This is the READ-value half of the `fmt()` trap: `fmt` is right for a value
computed at full working precision and wrong for one that reached `mpf` from a
narrower source. Recorded; fixing it means either changing the public contract
or having the probe emit the float at its true width, and both belong to
`qou-sv7h`'s arc rather than this one.

## 6. Gates

`PYTHONPATH=tools/qou-substrate/python:tools/pyhecke/python:computations:schemas/witness-schema/python bash scripts/precision-gates.sh --changed`

- **raw-float64 ratchet: `NEW dirty witnesses 0`, `REGRESSED 0`** on all three
  scan roots (`computations/`, `docs/audits/`, `qou-mass/src/`).
- **Zero hits naming any file this PR touches.** The only occurrence of the
  branch name anywhere in the 491-line log is the ratchet's own "On branch …"
  status line.
- Measured directly with the audit's own scanner
  (`witness_raw_float64_audit.scan()`), **0 raw-float64 fields** in each of the
  seven UIC witnesses — the three refreshed, the two identical, the new one, and
  the one left stale.
- The family exits 1 with **11 blocking reds**, all pre-existing on `main`:
  `q0-anchor flip`, `q0-anchor refill ratchet`, `import-time dps ratchet`,
  `never-raises-dps ratchet`, `float64-padding ratchet`, `raw-float64 ratchet`,
  `reference-literal ratchet`, `witness-value copy ratchet`, `q0-value drift
  ratchet`, `mixed mpf/f64 → serializer`. Their NEW entries name `alpha-em-*`,
  `hadron-knot-table`, `_deprecated/alpha-high-precision`,
  `binding-closed-form-c-vs-d` and two `probes/two_blocks_*` — none of them this
  PR's.
- The 11 contended tree-measuring audit witnesses the run regenerates were
  reverted **by name**, not with the bare `git checkout -- computations/` the
  gate prints: that command is path-scoped and essentially every probe in this
  repo lives under `computations/`, so running it verbatim discards uncommitted
  source edits (bean `qou-v0t8`).

`bash scripts/check-sidecars.sh` — its one ⚠ is on `docs/precision-goals.md:82`
and is pre-existing (the canonical-mass status guard, unrelated).

`python3 computations/lp_dual_witness_validator.py` — 6 missing-dual witnesses
corpus-wide, **none** of them this PR's.

## 7. What this does NOT settle

- **Whether the old binding numbers were wrong.** They were float64-limited; the
  mpf recomputation moves them by ~1e-17 MeV. Nothing here says the *physics*
  changed, and nothing here touches the sign, the gate, or the extensive-term
  frontier. `qou-brng` and `qou-sv7h` stay **open**.
- **Whether the cone is clean.** It is not — §3. The probe asserts that the
  residual exceeds what was removed, precisely so a later reader cannot quote
  this PR for the opposite.
- **The `binding_energy` public `float()` return.** Still a float64 boundary,
  left deliberately (§5).
