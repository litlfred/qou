---
# qou-uz7q
title: alpha_5_lp_dual_crystal exceeds a 7-min budget and lacks the required progress logging — but editing it drifts scriptHash for zero payload change
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T08:55:10Z
updated_at: 2026-10-04T15:16:20Z
parent: qou-5vkl
---

Surfaced by the #5519 staleness sweep. `computations/alpha/alpha_5_lp_dual_crystal.py`
is TIMEOUT at a 420 s per-producer budget — twice, at 300 s and at 420 s.

## Genuinely long, not hung
Static read: the dominant structure is `for sub in combinations(eigs, ell)`
(line 133) over the cells of partitions with `height == 6` (line 183) — a
combinatorial enumeration, so a long wall time is expected rather than
suspicious.

## It lacks the progress logging AGENTS.md requires
Only 3 flush/print sites in 426 lines. The long-compute discipline requires any
> 5 min script to emit a progress line every ~10 s or ~5 % of work, with wall
elapsed + ETA. Because it does not, **I cannot say how far it got before the
budget expired, or what its true runtime is** — which is precisely the cost the
discipline exists to prevent.

## Why I did NOT just add the logging
Adding a print statement changes the file, which changes `scriptHash` — a
whole-file hash. AGENTS.md is explicit that a comment- or logging-only edit
drifts `scriptHash` while the recomputed payload is byte-identical, and that for
a LONG-COMPUTE producer the right move is to claim it as a bean rather than
spend the pass recomputing numbers that cannot change. Editing this file would
therefore manufacture staleness in the exact audit this branch exists to measure,
and would then demand an expensive re-run to clear the drift it caused.

## What closing this actually needs
1. Measure its true runtime with a generous budget, on its own, teed to a log
   (`python3 -u ... 2>&1 | tee`), so the number is known rather than bounded.
2. THEN decide: if it is minutes, raise the sweep budget and move on. If it is
   hours, it needs a long-compute plan before it can be regenerated in EITHER
   #5519 or #5500 — and the logging should be added in the same pass as the
   re-run, so the scriptHash drift is paid for exactly once.

Until (1), its staleness is UNMEASURED. That is not the same as UNCHANGED, and
it must not be reported as either.

## CORRECTION to my own count — "3 print sites in 426 lines" is wrong

Measured: **20** print sites, at lines 152, 166, 253–256, 286, 292, 296, 299,
302, 303, 306, 310, 316–318, 341, 353, 421. I wrote 3. The producer is not
silent, and I should not have said so without counting.

**The conclusion survives, on a different and narrower basis.** Two things are
actually true, and they are the ones that matter:

1. **No timing anywhere.** `grep -cE "elapsed|ETA|time\.time|perf_counter"` →
   **0**. AGENTS.md's long-compute rule asks for periodic progress *including
   wall elapsed + ETA*; prints without timing cannot tell you whether a run is
   at 5 % or 95 %. That requirement is unmet regardless of the print count.
2. **The expensive region is the silent one.** Prints at 292–318 sit inside the
   stratum/atom loops, so that section does report. But the q-sweep at
   **321–338** (`for q_v in q_sweep_q` × `for atom in atoms`) emits nothing
   until line **341**, after it finishes. A timeout landing inside that nest —
   which is where a q-sweep's cost lives — produces no output at all.

So: "violates the logging rule" holds; "carries only 3 print sites" does not,
and the difference is not cosmetic. The first is a claim about *where and what*
it logs, which I checked; the second was a number I asserted without measuring
and which anyone opening the file would have caught.

## The decision is unchanged

Do **not** add logging now. `scriptHash` is a whole-file hash, so a
logging-only edit drifts it while the payload stays byte-identical —
manufacturing staleness inside the audit that exists to measure it. Add the
timing in the same pass as the eventual re-run, paying the drift once. That
reasoning never depended on the print count.

## This is a class, not one producer

All four TIMEOUT producers, measured:

| producer | lines | print sites | timing refs |
|---|---|---|---|
| `alpha_5_lp_dual_crystal` | 426 | 20 | **0** |
| `binding_via_interface_knot` | 361 | 7 | 3 |
| `block_swap_binding` | 192 | 17 | 3 |
| `he3_tritium_cosh_asymmetry_diagnosis` | 130 | 14 | **0** |

Two of four carry no timing at all. Four of 33 measured producers (12 %) are
TIMEOUT, i.e. unmeasured — and the sweep cannot say how close any of them came
to finishing, which is the decision it would need to inform a budget raise.


---

## Step 1 EXECUTED — and the premise does not survive it

This bean's step 1 was *"measure its true runtime with a generous budget, on its
own, teed to a log, so the number is known rather than bounded."* Done, and
read-only: the whole `computations/` witness tree is snapshotted and restored
around every run, because producers write **sibling** witnesses.

| producer | sweep verdict | measured |
|---|---|---|
| `alpha/alpha_5_lp_dual_crystal` | TIMEOUT at 300 s **and** 420 s | **9 s**, exit 0 |
| `he3_tritium_cosh_asymmetry_diagnosis` | TIMEOUT | **1 s**, exit 0 |
| `binding_via_interface_knot` | TIMEOUT | **> 1800 s**, exit 124 — genuinely long, still **UNMEASURED** |
| `block_swap_binding` | TIMEOUT | in flight |
| `qbeta/qbeta_c3even_exact_sseries_probe` | TIMEOUT | in flight |
| `qbeta/qbeta_c4even_exact_sseries_probe` | TIMEOUT | in flight |

**So this bean's headline — "Genuinely long, not hung" — is refuted for its own
subject.** `alpha_5_lp_dual_crystal` runs in 9 seconds. The static reasoning
that produced that heading (a `combinations(eigs, ell)` enumeration, therefore
long) was plausible and wrong; the combinatorial structure is there, it is just
not expensive at these sizes. **A static read of the code is not a runtime
measurement**, and this bean asserted one from the other.

Two consequences:

1. **The step-2 decision is moot for these two.** There is no budget to raise —
   they finish inside any budget. The sweep's TIMEOUT verdicts are **not
   producer runtimes** and must not be read as such.
2. **`> 1800 s` is still not a runtime.** `binding_via_interface_knot` hit a
   30-minute wall with no completion; per this bean's own standard that is
   UNMEASURED, not "half an hour". Do not quote 1800 s as its cost.

## I checked the obvious catch, and then killed my own explanation

**The catch:** a 9-second run that quietly fell back to a float64 solver would
be *cheaper work*, not *faster work*, and would prove nothing. It did not — the
run recorded `backend: clarabel-mpfr`, `precision_bits: 167`, the same
full-precision path the committed witness carries. The speed is real.

**The explanation that died:** the sweep's recorded environment lists no
`clarabel`, and the pip package is installed now — an inviting story for a slow
fallback path. It is wrong. `_find_clarabel_lp_bin` resolves a **compiled Rust
binary** (`tools/hecke-engine/target/release/clarabel-operator-selection-lp`),
not the Python package, so that diff explains nothing and is not offered as a
cause. The environments do differ (`mpmath 1.3.0` → `1.4.1`), which is a fact I
can state without attributing the timeout to it.

**So the mechanism behind the six TIMEOUTs is unknown.** Candidates I can name
but have not tested: concurrency inside the sweep harness, or a per-run
environment difference. What is established is only that the verdicts do not
measure producer cost.

## A separate blocker, bigger than the timing question

`alpha_5_lp_dual_crystal`'s own guard printed on the run:

> ⚠ raw-float64: `alpha-5-lp-dual-crystal.witness.json`: **101** raw float64
> field(s) would enter the witness

The committed `raw-float64-baseline.json` records **78** for that file, and
`witness_raw_float64_audit.py`'s docstring is explicit: *"a baselined witness
whose count **increases** fails."*

**NOT yet a confirmed regression, and the reason matters.** The two numbers come
from **different functions on different objects**: the producer-side 101 is
`witness.py::_raw_float_paths` counting paths *before* serialization; the
baseline 78 is `witness_raw_float64_audit.py::count_raw_floats` counting the
*committed JSON*. Comparing them directly is a category error, which is why it
is written here as a question rather than a finding. The decisive test is the
audit itself run against a regenerated witness — pending, because it needs a
tree-touching run and a producer batch was in flight.

If it does confirm, it reorders this bean: the blocker on this producer is
**precision, not budget**, and #5500 cannot regenerate it cleanly either way.

## Process note against myself

I ran `alpha_5` twice while the five-producer batch was running. Both use
whole-tree snapshot/restore, so concurrent runs can restore each other's
intermediate state. Nothing was corrupted (`dirty=0` after each), but that was
careless and should not be repeated — serialise tree-touching runs.


## The qbeta pair: cost located, and the obvious fix is not available

Both remaining TIMEOUTs are the exact-`s`-series probes. The running one names
its own expensive phase before it stalls:

    exact sympy series to O(s^9) (log R and u) ...

so the cost is **symbolic algebra**, not a numeric loop. Upstream of that line
sit `sp.simplify` at 62, 75 and 104 and `sp.cancel` at 76 — the class
`local/compute-audit` exists to route ("where is `sympy.simplify`").

**Stated as a candidate, not a cause.** What is observed is that the run sits in
the series phase and that three `simplify` calls precede it. Nothing here is
profiled, so do not record `simplify` as the hot spot without measuring it —
that inference is the same shape as this bean's original "combinatorial,
therefore long", which was wrong.

**"Just lower the series order" does not work, and it is the first thing anyone
will propose.** The order is not a tuning knob:

| probe | `KC` | `NS = 2·KC + 2` |
|---|---|---|
| `qbeta_c3even_exact_sseries_probe` | 3 — *"extract through c_3 (s^6); c_4 needs s^8"* | 8 |
| `qbeta_c4even_exact_sseries_probe` | 4 — *"extract through c_4 (s^8)"* | 10 |

Both are module-level constants with no argparse, and `KC` **is the quantity
the probe extracts**. Lowering it does not make the probe cheaper — it makes it
answer a smaller question. Any long-compute plan has to attack the symbolic
route (targeted `cancel`/`together`/`radsimp` instead of blanket `simplify`, or
an exact-rational route that avoids the series), not the order.

**Expectation, not a measurement:** `c4even` runs at `NS = 10` against
`c3even`'s `NS = 8`, and exact-series cost grows steeply with order, so if
`c3even` exceeds 30 min then `c4even` should be worse. Recorded so the eventual
number can be checked against it rather than rationalised after the fact.


## The 78 → 101 question: RESOLVED, and it was a category error

Measured with the audit's **own** counter on both files, plus a read of the
comparison it actually performs:

| quantity | value |
|---|---|
| `raw-float64-baseline.json` entry | **78** |
| `count_raw_floats(committed)` | **45** |
| `count_raw_floats(regenerated)` | **47** |

And the gate's comparison, from `witness_raw_float64_audit.py:668`:

```python
grew = {f: (prior[f], n) for f, n in found.items()
        if f in prior and n > prior[f]}      # prior = the BASELINE
```

**So regenerating `alpha_5_lp_dual_crystal` does NOT trip the ratchet.** 47 < 78
puts it in `drained`, not `grew`; the gate passes and records a drain. The
concern I raised is closed as a non-blocker, and #5500 is not obstructed here.

**The 101 and the 78 were never comparable**, which is why this was written up as
a question rather than a finding. `witness.py::_raw_float_paths` counts candidate
paths *before* serialization (101); `witness_raw_float64_audit.py::count_raw_floats`
counts the *serialized JSON* (45/47). Two functions, two objects. Had I reported
"78 → 101 regression, #5500 blocked", it would have been wrong in both the number
and the conclusion.

Two residues, neither a defect:

1. **Regeneration does add 2 fields** (45 → 47). Real drift, far under the
   baseline, no gate consequence. Worth knowing only if someone later tightens
   the entry.
2. **The baseline entry overstates the committed file by 33** (78 vs 45). That is
   safe *by construction* — the mechanism is drains-only, so a loose entry
   under-ratchets rather than mis-passing. **Do not hand-edit it to 45**;
   AGENTS.md forbids hand-editing baseline numbers, and the drain is supposed to
   be recorded by a gate run, not by an agent typing a smaller number.

Method note: the regeneration was done in the main tree with a single-file
copy-out and `git checkout --` restore (9 s, one file touched), deliberately
**not** a `git worktree` — the tree is 9.8 G against 13 G free, so a second
checkout was not worth the disk.


## Step 1 COMPLETE — all six measured

| producer | sweep verdict | measured | reading |
|---|---|---|---|
| `alpha/alpha_5_lp_dual_crystal` | TIMEOUT at 300 s **and** 420 s | **9 s**, exit 0 | **refuted** |
| `he3_tritium_cosh_asymmetry_diagnosis` | TIMEOUT | **1 s**, exit 0 | **refuted** |
| `binding_via_interface_knot` | TIMEOUT | 1800 s, exit 124 | long, **UNMEASURED** |
| `block_swap_binding` | TIMEOUT | 1800 s, exit 124 | long, **UNMEASURED** |
| `qbeta/qbeta_c3even_exact_sseries_probe` | TIMEOUT | 1800 s, exit 124 | long, **UNMEASURED** |
| `qbeta/qbeta_c4even_exact_sseries_probe` | TIMEOUT | 1800 s, exit 124 | long, **UNMEASURED** |

`DIRTY_AFTER=0` on every run; the whole-tree snapshot/restore held.

**2 of 6 refuted, 4 of 6 confirmed long — and none of the four has a runtime.**
A 1800 s censoring bound is not a duration. Do not quote "30 minutes" for any of
them; the honest statement is "> 1800 s, unmeasured", which is this bean's own
standard applied to its own results.

## My own prediction: UNTESTED, not confirmed

I recorded the expectation that `c4even` (higher order) would be worse than
`c3even`. **The run cannot distinguish them — both were censored at the same
1800 s bound.** Recording it as confirmed would be reading a tie as a win. It
stays open, and a run that separates them needs a budget above whichever is
larger.

## The slow step is not my inference — the producer says so

`c4even`'s own last line before the wall:

    exact sympy series to O(s^11) (log R and u) — this is the slow step ...

and `c3even`'s, at O(s^9). So the symbolic-series attribution is the producer's
self-diagnosis, not a guess from a static read. It is still **not a profile**:
`sp.simplify` at 62/75/104 remains a candidate for *where inside* that step the
time goes, and nothing here measures it.

## What step 2 now says, per producer class

- **The two fast ones need no budget at all.** Their TIMEOUT verdicts were
  artifacts; nothing to raise.
- **The four long ones need a long-compute plan, not a bigger number.** For the
  qbeta pair the target is the symbolic route — and per the section above,
  lowering `KC` is not available, because `KC` *is* what each probe extracts.
- **`binding_via_interface_knot` has zero timing references in 362 lines.**
  Unlike `alpha_5`, where the logging complaint was moot once it turned out to
  finish in 9 s, here the AGENTS.md long-compute rule genuinely bites: a
  > 30-minute producer emitting no elapsed/ETA is indistinguishable from a hang.

## Harness flaw, found by using it

The timing harness wrote every run to one shared `/tmp/prod_run.log`, so each
producer overwrote the previous one's output — discarding exactly the "last line
before the timeout" that turned out to be the most useful diagnostic in this
whole exercise. Fixed mid-batch to a per-producer path, which is why only
`c4even` has its own log. The measurement tool had the same defect it was
measuring.

## The qbeta probes validate against the MUON pin, via a live fallback

Read while setting up the profile, and complete on its own:

```python
q0 = mp.mpf(str(params["q"])) if params and "q" in params else None
...
if q0 is None:
    # fall back to the canonical muon q0 string used corpus-wide
    q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
```

**That fallback is live, not dead code.** `free-neutron-decay.witness.json` has
**no `parameters` block at all** (`params is None`), so every run takes the muon
branch. The same witness also carries no `q0Anchor` and no `q0Value` — it is
`Q0_ANCHOR_MISSING`, which AGENTS.md classes as *not a failure* and which covers
~71 % of the corpus, so that part is unremarkable.

**It has no consequence for this probe's result, and I am not proposing an edit.**
Two reasons, both checked rather than assumed:

1. **`q0` is used only for a validation assert at `1e-6`.** The probe's product —
   the exact `s`-series and the `c_3` extraction — is symbolic in `q` and carries
   no pin. Observed this run: `Δ(net) mine = -0.188290620016` vs
   `witness = -0.188290620011`, residual ~5e-12, passing with ~2e5× margin. The
   μ–p gap is 1.15e-8 relative — three orders below the tolerance — so the anchor
   choice cannot flip this assert either way.
2. **Editing it would drift `scriptHash` on a > 1800 s producer** for zero payload
   change, which is exactly what this bean argues against elsewhere. If the
   fallback is ever changed to proton per the 2026-08-07 directive, it should ride
   along with the eventual re-run, paying the drift once.

Recorded because "a hardcoded muon string in a live path" is worth knowing even
when it is inert, and because the inertness is a measurement, not an assumption.

## PROFILED — and this bean's own candidate is REFUTED

This bean said: *"`sp.simplify` at 62, 75 and 104 … Stated as a candidate, not a
cause. Nothing here is profiled, so do not record `simplify` as the hot spot
without measuring it."* Measured now. **It is not `simplify`.**

Method: `cProfile` under a wrapper that runs the producer via `runpy` and dumps
cumulative + self-time stats from a `SIGALRM` handler. **The producer is not
edited**, so no `scriptHash` drift — the objection this bean raises against adding
logging does not apply to profiling it from outside. 1200 s budget on
`qbeta/qbeta_c3even_exact_sseries_probe`; it did not finish, consistent with the
earlier > 1800 s censoring.

**2,588,247,572 function calls in 1200 s.** The chain, by cumulative time:

| frame | ncalls | cumtime | share |
|---|---|---|---|
| `main` | 1 | 1199.5 | — |
| `sympy.series.series` → `log._eval_nseries` | 1 | 1192.4 | 99.4 % |
| `Mul._eval_nseries` / `Power._eval_nseries` | 337 / 366 | 1191.4 | 99.3 % |
| **`trigsimp` → `futrig` → `_eapply`** | 383 | 1188.9 | **99.1 %** |
| **`polys.polytools.factor`** | **3** | **1173.8** | **97.8 %** |

Self time is entirely dense multivariate polynomial arithmetic underneath that
`factor`: `dmp_mul` 205 s, `dmp_zero_p` 170 s, `dmp_degree` 101 s, `dmp_sub`
81 s, with `dmp_rr_div` at 971 s cumulative.

**The mechanism.** `Rq` carries a live `sp.cos(alpha_eff)` node. When `series`
expands `log(Rq(1+s)/R1)`, sympy's nseries machinery calls `trigsimp` *because a
trig node is present*, and `futrig`'s `_eapply` hands the accumulated rational
expression to `factor` — which, with `sqrt(q**4+q**2+1)` in it, means factoring
over an algebraic extension. **Three `factor` calls consume 97.8 % of the run.**

So the cost is not in the probe's own `simplify` calls at all — those complete
before the series step (the run prints `R(q=1) exact = 1` and reaches the series
line). The cost is inside `sp.series`, triggered by the `cos`.

### Caveat on the numbers

`cProfile` adds per-call overhead, and at 2.6e9 calls that overhead is large in
absolute terms — the 1200 s is **not** a runtime estimate for an unprofiled run,
and the bias favours call-heavy pure-Python (`dmp_*` micro-functions) over C-level
work. The *relative* attribution is what this establishes, and a 97.8 % share has
room to survive the bias. The unprofiled run is still > 1800 s and still
UNMEASURED; this does not change that.

### What it implies for step 2 — stated as a candidate, and being tested

If the `cos` node is what summons `trigsimp` → `factor`, then expanding
`cos(alpha_eff)` into its Taylor polynomial **before** handing the expression to
`series` should remove the trig node and with it those three `factor` calls.
`alpha_eff(q=1) = 0`, so a truncated `cos` polynomial is exact to the order used.

**Not yet verified** — a route comparison at low orders is in flight. Recording
the reasoning separately from the result, because the whole point of this section
is that this bean previously recorded a plausible mechanism as if measured.

## The fix is MEASURED and VALIDATED — expand `cos` before `series`

The previous section recorded this as a candidate. It is now measured, and
validated against ground truth rather than against itself.

### Route comparison (per-route SIGALRM cap of 420 s)

| order N | A — live `cos` (what the probe does) | B — `cos` expanded first |
|---|---|---|
| 3 | **> 420 s CAPPED** | **4.53 s** |
| 4 | **> 420 s CAPPED** | **55.44 s** |
| 5 | **> 420 s CAPPED** | **56.19 s** |

**A cannot finish at N=3 — the lowest order tested — while the probe needs N=9.**
So the cost is not driven by series order; it is the trig node summoning
`trigsimp` → `factor`, exactly as the profile attributed. The ratio is ≥ 93× at
N=3 and unbounded from below, because A never completed at any order.

### Why B is not merely faster but CORRECT

**A produced no series at any order, so there was nothing to compare B against.**
Comparing B to A was therefore impossible, and a speedup on a different quantity
would be worthless. Validated instead against the **true function**, which is a
stronger test than A would have been:

evaluate `F(s) = log(Rq(1+s)/R1)` numerically with the **live `cos`** at 60 dps
(mpmath throughout, no float64 — the probe's own `Rq`, unexpanded), and check that
`|F(s) − P_N(s)|` decays like `s^N`:

```
  s=1e-2:  8.5558041e-10
  s=1e-3:  8.4936691e-15   -> falls 5.003 decades per decade (expect 5)
  s=1e-4:  8.4875754e-20   -> falls 5.000 decades per decade (expect 5)
```

Exactly the required order. `R(1) = 1.0` numerically also matches the probe's
own exact `R(q=1) exact = 1`. B is the correct order-N expansion of the same
function.

**Why the truncation is exact rather than an approximation:** `alpha_eff(q=1) = 0`
(verified symbolically), so `alpha_eff = O(s)` and a `cos` polynomial carried to
degree ≥ N contributes nothing beyond `O(s^N)`. No accuracy is traded for the
speed.

### Coefficients (N=5), exact

```
c[0] = 0
c[1] = 0
c[2] = 9/8
c[3] = -37/8 + sqrt(3)/8
c[4] = -887/192 - 9*sqrt(3)/16
```

The `sqrt(3)` is `sqrt(q**4+q**2+1)` at `q=1`, as expected.

> **Notation collision — do NOT conflate.** `9/8` here is the `s²` coefficient of
> `log(R(1+s)/R(1))`. AGENTS.md separately discusses `c̃₂ = c₂ − 1/8 = −9/8` for
> the *normalised* `Φ(u)/Φ(0)` model. Different object, different variable,
> opposite sign. This bean asserts **no** relationship between them; it is flagged
> only because the corpus already carries a documented history of confusing
> quantities that differ by normalisation.

### It is a class, not one producer

`c4even` is structurally identical (`Rq = Qb_over_me / (QA_over_me *
sp.cos(alpha_eff))` at line 101, `sp.series(sp.log(Rq...))` at line 108), so one
change covers both TIMEOUT qbeta probes — and neither needs `KC` touched, which
this bean establishes is not a tuning knob.

Corpus-wide, an AST pass (resolving each `series()` call's first argument through
local bindings, rather than grepping for files that merely contain both) finds
**13 sites in 9 files** where a trig node reaches the expanded expression:

```
qbeta/qbeta_c3even_exact_sseries_probe.py:110   cos   <- measured TIMEOUT
qbeta/qbeta_c4even_exact_sseries_probe.py:108   cos   <- measured TIMEOUT
qbeta/qbeta_eigenphase_taylor_in_u.py:128,129,160
qbeta/qbeta_h_frame_rungs_probe.py:76,86
qbeta/qbeta_crossing_weight_hecke_probe.py:247,248
qbeta/qbeta_h4_route_a_gate_probe.py:176
qbeta/_h4_g_linear_response.py:40   qbeta/_h4_route_ladder_scan.py:34
probes/qbeta_phib_saddle_fluctuation_transseries_probe.py:243   sin
```

**Two caveats, both load-bearing.** The detector binds names *last-write-wins over
the whole file* — the identical flaw that produced three wrong upstreams in
`inherited_q0_pin_audit.py` before it was made scope-aware — so an attribution
can be wrong where a name is rebound. And reaching a trig node does **not** imply
slowness: cost depends on whether `factor` receives a large algebraic input.
These are **13 candidates for one mechanism, of which 2 are measured**, not 13
slow producers.

### Still open

- **The N=9 timing** — the order the probe actually needs. B at N=5 is 56 s; N=9
  is running and is the number that decides whether this makes the probes
  tractable or merely faster. Do not quote a speedup for the real probe until it
  lands.
- **No producer has been edited.** Everything above was measured from outside, so
  no `scriptHash` has drifted. Applying the change to the two probes is a
  proposal, not something this bean has done — and it would pay the drift, so it
  should ride with the re-run that regenerates their witnesses.

## Scaling, with `series` timed apart from extraction — and a flaw in my own test

The previous section left the N=9 timing open. A first attempt burned 90+ minutes
with no output, and I could not attribute it: **that harness printed only after
`nsimplify` of every coefficient**, so a slow extraction and a slow `series` were
indistinguishable in it. Re-run with `series` printed immediately and extraction
timed on its own line:

| N | `sp.series` | extract + `simplify` |
|---|---|---|
| 5 | 56.2 s | — |
| 6 | **365.8 s** | **0.0 s** |
| 7 | **365.1 s** | **0.0 s** |
| 8 | **1386.8 s** | **0.0 s** |

**Extraction is free at every order.** So the 90-minute silence was `series`
itself; the harness flaw was real but did not change the answer. Worth recording
both facts — the instrument was wrong, and it happened not to matter.

### N=6 and N=7 are identical because MY truncation was too generous

365.8 s vs 365.1 s is not a coincidence. `cos_poly` used `range(n//2 + 2)`, so:

| N | cos degrees |
|---|---|
| 5 | 0..6 |
| 6, 7 | 0..8 |
| 8, 9 | 0..10 |

N=6 and N=7 expand the **same** polynomial, as do N=8 and N=9. The apparent
"scaling" is partly an artifact of my formula rather than a property of the
problem.

**And the generosity is not free.** `series(..., 0, N)` needs terms through
`s^(N-1)`, and `alpha_eff = O(s)`, so the `cos` truncation needs degree **≥ N-1**
— no more. At N=9 that is degree **8**, not the degree **10** my harness used —
and degree 10 is the same expression that made N=8 cost 1387 s, while degree 8
is the one that ran in **365 s**. So the N=9 number I was about to report would
have measured my own over-truncation.

Re-running N=9 at the minimal sufficient degree, with the ground-truth residual
check attached so a cheaper truncation cannot pass by being wrong.

## VERIFIED — and the verification found a SECOND, larger defect

The perf fix was applied to both probes and `c3even` re-run. It completed in
**360.9 s** (from > 1800 s censored). Then every value in its witness moved, and
its own gate went **FAIL**:

| quantity | committed (2026-07-02) | re-run |
|---|---|---|
| `c2_even` | −8.00641005870925 | **−7.45876032789888** |
| `c3_even` | +86.6611630646910 | **+78.5944241201959** |
| `[s^3] log R` | −33/8 + √3/8 | **−37/8 + √3/8** |
| `allPassed` | `true` | **`false`** |
| gate `c_2^even ≈ −8.006` | PASS | **FAIL** |

### The movement is NOT the perf fix — measured, not argued

Numeric Taylor of `log(R(1+s)/R(1))` with the **LIVE `cos`** (i.e. the perf change
absent), mpmath 60 dps, under each `z`:

| probe source | `[s^3]` | matches |
|---|---|---|
| **D** — today's `z = q**3/(q**2+1)` | −4.4084936490538903383 | the **re-run** value, `\|diff\| = 0.0` |
| **C** — witness-era `z = 1/(sqrt(q)+1/sqrt(q))` | −3.9084936490538903383 | the **committed** value, `\|diff\| = 3.1e-61` |

So the perf change contributes **exactly nothing**: the live-`cos` function under
D already gives the new value. **The entire movement is the C→D convention
migration.** `70d1ade383` ("excise C tiers 2+3: 176 producer sites to convention
D") swapped this probe's `z` on 2026-08-09 and did not regenerate its witness.

The gate threshold tells the same story: `−8.006` **is** the convention-C value —
the committed C witness carries `−8.00641005870925` exactly. The gate is
C-calibrated, so a correctly-migrated D producer must fail it.

### Already known as a class — this is candidate #33, now CONFIRMED

Corpus-grepped before declaring anything.
[`convention-frame-staleness-audit.witness.json`](computations/convention-frame-staleness-audit.witness.json)
already tracks this: **73 suspect witnesses** of 140 examined against 139 D-form
producers, and `qbeta-c3even-exact-sseries.witness.json` is **candidate 33**. Two
entries carry `confirmed_by_decisive_test` with beans (`qou-h4ab`,
`qou-g49k-followup`), and the `fr-pullback-cosh-h` entry has exactly the shape
measured above (committed / convention_D / convention_C).

**So the finding is not a new class — it is candidate 33 promoted from suspect to
confirmed**, by the audit's own decisive-test method.

### Why the D witness was NOT committed

The re-run's D numbers are correct arithmetic and are **not** a valid ladder.
AGENTS.md, the 2026-08-15 convention ruling:

> **The ladder must be RE-DERIVED under D, and that is not a z-swap** —
> `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` … makes the C-frame ladder and the
> mass channel's three-row forcing mutually exclusive, so substituting `z_D` into
> the existing ladder is not a valid move.

`70d1ade383` substituted `z_D` into this ladder. Whether it intended to claim
D-frame ladder values or was draining C-form sites mechanically is not something
this bean can establish — but either way the producer now emits numbers from the
move the ruling names as invalid. **Committing them would enshrine that.** The
committed C witness is restored; nothing was landed.

Tranche `qou-cds1` (§S1) owns the re-derivation. This adds a measured instance.

### The two defects were hiding each other

The probe times out in the sweep, so its verdict reads TIMEOUT rather than FAIL —
which is why a producer that **fails its own gate on `main`** went unnoticed for
16 days. Fixing the timeout is what made the convention staleness visible. That is
the argument for the perf fix independent of any speedup: it turns an unmeasurable
producer into one whose failures are legible.

### Status of the perf change

**Kept.** Validated value-neutral twice over — the `s^N` residual check, and the
live-`cos` numeric Taylor above, which reproduces the D value the perf-fixed
probe emits. It makes the probe *measurable*, not *correct*: its output is still
C-conditional per the ruling.

`c4even` carries the identical edit and has **not** been re-run — under the ruling
its D output would be no more landable than `c3even`'s.

### Not landed, deliberately

`scripts/precision-gates.sh --changed` regenerated three audit witnesses
(`q0-anchor-consistency`, `witness-provenance`, `mpf-float-source`) showing real
drains — `prov_missing` 94→79, `Q0_ANCHOR_MISSING` 1646→1639, `benign` 13→12.
**But `total_scanned` fell by 7 in two of them**, so the population changed and
not merely the verdicts; this session's snapshot/restore cycles have been adding
and removing untracked witnesses all along. The gate says attribute the movement
before claiming it, and I cannot attribute this cleanly to main either. Restored
rather than committed. All blocking precision gates were green.

## Read-only sweep: does any OTHER producer share the c3even shape?

Bounded, no runs, no writes. The c3even shape is: **a D-form producer gating on a
constant that is its own C-era answer.**

**First detector was noise, and the noise is the lesson.** Keying on "a producer
constant matches a value in its own committed witness" with `|c| > 1` and a 2e-3
relative tolerance produced ~20 hits, of which I can defend **zero**: `2.0`
matched a deuterium mass number, `10.0` a tolerance field, `3.0` an `A=3`, and
`2.0` vs `2.00272236446` passed at 0.14 %. Small round numbers match everything.

Tightened to the actual signature — non-round, ≥5 significant figures, relative
match < 1e-4, not a q₀ anchor — **13 survive, and most are legitimate**:

| class | examples | verdict |
|---|---|---|
| experimental inputs | `0.78233341` (Q_β CODATA), `0.15648` (Q_exp), `14899.169` / `18622.835` (AME) | correct by design |
| deliberate historical records | `-2.0097` (`c3_muon_hopf_on_record`), `-2.069342577115168` (`c3_proton_on_record`) | AGENTS.md says keep and scope, do not correct |
| search targets | `1.22035866` (`phase_5g_constit_factor_search/target`) | by design |

**One survivor has the c3even shape** —
[`probes/qbeta_ck_qholonomic_recurrence_test.py`](computations/probes/qbeta_ck_qholonomic_recurrence_test.py):

```python
z = q**3 / (q**2 + 1)                                   # line 210 — convention D
...
gate("muon_c3_matches_N3_witness",
     abs(c3_mu - mp.mpf("-2.021615577060006120530024970029644566094740817719")) < mp.mpf("1e-12"),
```

A **D-form** producer gating at **1e-12** on a **C-frame** `c_3` constant.

**NOT confirmed, and the gap is specific.** `c3_mu` is read from an anchors
structure (`anchors["muon"]["c_emp"][3]`), not computed from that `z`. So the gate
may never touch the migrated parameter, in which case a C constant against a
C-era witness passes consistently and there is no defect. Establishing which
needs the same decisive test used for c3even — evaluate under both `z` forms and
see which reproduces — and that sits in `qou-cds1`, not here.

By contrast `qbeta_ck_basis_constrained_pslq.py` is **clean**: its `c3_*_on_record`
constants are written *into* the witness as records (`mp.nstr(...)` in the output
dict), not compared against. That is the legitimate case.

**Result: 1 further candidate, 0 further confirmed.** Reported as a count rather
than a list of alarms, because the first detector's 20 hits were the alarm and
they were all mine.
