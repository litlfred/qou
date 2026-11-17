---
# qou-p77d
title: 'GAP: 883 non-integral float64 at .assertions[].computed/.expected across 300 witnesses — the class #5910 deferred'
status: in-progress
pr: 8290
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T02:28:37Z
updated_at: 2026-11-17T08:47:00Z
parent: qou-9nnz
---

## 2 of the 883 are already drained (PR #5952, bean `qou-t39x`) — 2026-08-29

Recorded so the tranche does not re-open them, and because the instance
reproduces this bean own reasoning from the opposite direction.

`computations/probes/qbeta_exponentiated_per_block_probe.py` had
`computed = float(results["proton"]["c"][2])` and `expected = -1.0` in its
`scale_fix_c2_minus1_solvable_and_exact` assertion. Both sat in the
INTEGRAL-EXCUSED majority — the value is exactly -1.0 — and both are now
`mp.nstr(..., 40)` and the string "-1", fixed at the producer and re-run, which
is the route this bean prescribes for a `computed` field.

It is a live instance of the "integral is safe by ACCIDENT OF CURRENT VALUE"
warning, and a sharp one: the cast was discarding a 35-DIGIT agreement (the
assertion tests |c+1| < 1e-35 at 60 dps) in order to report -1.0. Nothing was
excused about it except the current value.

Worth carrying into the sweep design: it surfaced from the OTHER end. The
raw-float64 ratchet went red on the same assertion tolerance, a bare 1e-35
literal — the #5910 declared-threshold class, repairable textually. Fixing that
put me inside the function, where the `computed` cast was visible three lines
up. The two classes co-occur in the same assertion dict, so a producer opened
for a #5910-style tolerance fix should have its `computed`/`expected` checked in
the same pass rather than left for a second visit.

After: raw-float64 ratchet NEW dirty 0, REGRESSED 0; integral-float population
down by exactly the 2 fields.

MEASURED 2026-08-29 (PR #5996) — A THIRD OF THE 883 MUST NOT BE DRAINED THE
PRESCRIBED WAY, AND THE RANKING IN THIS BEAN STARTS IN THAT THIRD.

This bean says the ranked worst-offenders list "is where it would start". I
started there, opened the #1 entry, and it is in the bucket where the
prescribed repair is wrong.

    583  A. producer raises mp.dps -> mpf carries real digits, the float()
            cast genuinely discards them. Repair as prescribed.
    291  B. producer NEVER raises mp.dps (or pins <= 15) -> the computation is
            float64-equivalent however much mpmath it imports.
      9  C. producer not found.

For B, float(x) -> mp.nstr(x, 40) prints forty digits of a double. Not a
repair; LAUNDERING, against AGENTS.md "never report a float64 agreement as
exact / to N digits".

SIX OF THE TOP EIGHT OFFENDERS ARE B. The largest single entry,
channel_product_mass.py at 64 fields (7% of the tranche), imports mpmath,
calls mp.log and casts back at :109/:111/:116 — while M_E_MEV, M_P_MEV,
m_n_derived_3input and Q are all plain floats and mp.dps is never raised off
its default 15. Its assertion tolerance is 2%, so precision is not the binding
constraint there by ~14 orders of magnitude.

B IS NOT "ALREADY FINE" — those producers are float64 while PRESENTING as
mpmath computations. But the fix is upstream (mpf(str(CONST)) + a real dps,
the pattern the corpus already uses at binding_link_volumes.py:111 and
option_e_v8_hecke_involution_isospin_mirror.py:43), not a serialization change
at the assertion. It changes what the numbers MEAN, not how they are written,
so it should not ride in on a drain. Wants its own bean.

WORK ORDER, corrected: drain within bucket A, ranked by --by-precision.
Starts at probe_he4_canonical_tr_m_fingerprint.py (18) and hadron_knot_table.py
(14). NOT started — #5996 is the measurement that fixes the order, nothing more.

TOOLING: --by-precision on assertion_value_float64_triage.py prints the split
and warns, in its own output, that the unsplit ranking above it is the wrong
thing to work. --selftest (7 cases) pins the discriminator on the #1 A and the
#1 B by name, four synthetic producers (no-dps / 15 / 60 / set_compute_dps),
and that an unknown producer lands in C rather than silently in A or B.

MEASUREMENT CORRECTION, mine: my first pass said 958 fields / 325 witnesses.
The excess is entirely computations/_deprecated (74) and the generated
qou-mass mirror (1), both out of scope. This bean 883/300 is right and
reproduces exactly. Recorded rather than quietly dropped — the failure mode all
session has been adopting whichever number agreed with me.

BUCKET B MEASURED 2026-08-29 (PR #5996) — IT IS THREE JOBS, AND THE BIGGEST IS
NOT A PRECISION FIX AT ALL.

291 fields over 58 producers. Split by what the producer actually is:

    15 producers  import mpmath but never raise mp.dps
                  -> plausibly mechanical: add set_compute_dps(), verify the
                     mpf actually flows, and they become bucket A.
    43 producers  NO MPMATH AT ALL — float64 end to end.
                  -> not a serialization or dps problem. "Fixing" one means
                     RE-DERIVING the computation in mpmath, per producer,
                     changing values that feed real claims.

The float64 constants they pull: q_parameter (38), experimental_constants
(16), codata_constants (12), codata_table (1). Those modules export plain
floats BY DESIGN — the corpus pattern for wanting precision is mpf(str(CONST))
at the call site (binding_link_volumes.py:111,
option_e_v8_hecke_involution_isospin_mirror.py:43).

FOR THE 43, THE CORPUS ALREADY DEFINES THE HONEST OUTCOMES and none is a
sweep:
  1. port to mpf — real work, per producer, moves values;
  2. declare precision_tier AND deprecate — note the audit is explicit that
     'precision_tier: "float64" alone excuses nothing', so a producer cannot
     self-excuse (witness_raw_float64_audit.py:311-332). main landed one of
     these on 2026-08-29: 4f246d4320 'the four H_9 A-operator extracts are
     float64 by measurement';
  3. establish float64 is adequate for what the producer claims, and say so.

Worked case for (3): channel_product_mass.py is the #1 offender at 64 fields,
and its assertion tolerance is 2% of the observed mass. Precision is not the
binding constraint there by ~14 orders of magnitude. Draining it would change
64 numbers and improve nothing that any claim rests on.

RECOMMENDATION (judgement, not a finding): do the 15, and treat the 43 as a
separate bean. Folding a mathematical re-derivation into a drain labelled
'remove float casts' is the same smuggling the zero-gain rule already refuses.


## Bucket B has a single upstream cause (measured 2026-08-29)

`computations/substrate/experimental_constants.py` casts every CODATA mass to
binary64 at import (`M_E_MEV = float(_M_E_MEV)`, same for M_P/M_N). Every
bucket-B producer that starts from those constants is float64 end to end no
matter how much mpmath it calls afterwards — `channel_product_mass.py`, the
corpus's single largest offender at 64 assertion fields, is exactly this.

The cast's stated reason is HALF STALE. Measured in
`computations/audits/experimental_constants_float64_rationale_probe.py` (6/6):

  * "an mpf would break json.dumps" — TRUE for a bare `json.dumps`, FALSE for
    the witness path, which is where the bucket-B fields come from.
    `qou_substrate/witness.py` uses `json.dump(..., default=str)`.
  * "importers' float arithmetic stays intact" — holds for arithmetic,
    comparison, f-strings. The real hazard is `math.log(mpf)`, which does not
    raise, it silently downcasts.
  * "~266 importers" — actually 204 live (+4 generated mirror).

DECISION NOT TAKEN — it is the owner's. Flipping three constants changes
numbers across the mass sector.

## Retracted this session

Claimed 13 producers / 52 fields were misfiled B→A via a one-hop import-cone
check. WRONG: the inherited `set_compute_dps()` in `mass_at_3A_proper` is
inside a function. Classifier stays file-local; both wrong versions pinned in
its selftest.

Also: "round-trips through float64" is NOT proof of laundering. It flagged 55
of the 302 already-drained fields; all 55 are exact k·2^-235 ULP residuals,
and a power of two round-trips losslessly. Flag for reading, never decide.


## CODATA flip DONE; bucket B does NOT generalise (2026-08-29, PR #6022)

Owner authorised both halves. First half landed, second half largely did not,
and the reason is the useful part.

### Flip (done)
`experimental_constants.py` casts removed — the registry already held mpf.
- No CODATA INPUT moved (rel 0.0 on m_e/m_p/m_n). Only derived quantities
  changed, by the float64 error they carried: Q_β 4.1e-50, κ=m_e/3 9.8e-17.
- 204 importers screened both sides, fresh subprocess each: 6 fail before,
  23 after, **6 after fixing → 0 attributable**.
- Fixed at cause: 96 `mpf(repr(CONST))` sites (broken for mpf, correct for
  float — the other 84 in the tree left alone); 2 bare `json.dump` given
  `default=str`; one silent `math.sqrt(mpf)` downcast in the module itself.

### Bucket B splits on q₀, which is float64 BY DESIGN
`q_parameter.Q` is a float (17 digits vs a canonical 50). `q_parameter.py`
header says do NOT change it; `q_at(dps)` is the accessor. So:
- 26 q-independent (82 fields) — ran them: **ok=4, reverted=22**
- 32 q-dependent (209 fields) — BLOCKED on a per-producer proton/muon anchor
  choice. Layer-straddle hazard; not mechanical. NOT attempted.

### The 22 reverts are diagnoses, not failures
- 17 "no gain", 12 with ZERO casts (`0+0`) — float64 enters by a route neither
  a dps raise nor a cast removal touches.
- 5 LAUNDERING — guard caught the value still round-tripping through binary64.
  Worked case: `codata_reconciliation` emitted
  `0.782333409309999949776…` = Q_NEUTRON_MEV (exact mpf) pushed through a
  double downstream and printed at 40 digits.

### Landed
qbeta_counit_substrate_consistency (17→65 digits), chi_free_via_lr,
qbeta_5two_tail_law_deep_cn_probe, qbeta_uw_reparam_probe.
Fields 599 → 593; ratchet NEW 0 / REGRESSED 0 / exit 0.

### Process notes for the next agent
- Pipe a long producer run to a FILE, never through `tail` — buffering swallows
  every verdict and a kill loses them all. Made this mistake twice today.
- Scope before running: my first pilot took the 6 LARGEST producers, 4 of them
  q-dependent and certain to revert.


## MERGED 2026-08-29 — 883 → 593 fields, 300 → 208 files

Two PRs on main: #5996 (`3eb2375`, bucket-A drain) and #6022 (`22b84c2`,
CODATA constants off float64 + 4 bucket-B producers).

**Bucket A: 139 producers drained.** Of 302 committed float→string fields,
**258 genuinely gained digits**. Every drain judged against a FRESH UNMODIFIED
baseline re-run, never the committed witness — three of the first five targets
already drift on an unmodified re-run, so the committed file blames the cast
removal for movement that was already there.

**The upstream cause, fixed.** `experimental_constants.py` cast every CODATA
mass to binary64 at import while `codata_2022_source` already held them as mpf
at full width. Removed. No input value moved (rel change 0.0 on M_E/M_P/M_N);
only `Q_NEUTRON_MEV` (4.1e-50) and `KAPPA` (9.8e-17) changed, by exactly the
float64 error they were carrying. 204 importers screened both sides in fresh
subprocesses: **0 new failures**.

## STILL OPEN — three jobs, not one

1. **32 q-dependent producers / 209 fields.** `q_parameter.Q` is a `float`
   (17 digits vs the canonical 50). DELIBERATE — `q_parameter.py` says not to
   change `Q`/`Q_50_DIGIT_STR` and provides `q_at(dps)`. So every producer
   reading `Q` has a float64 ceiling on its q-dependent arithmetic. Fixing
   them means `Q` → `q_at(dps)` per producer, which forces a PROTON-VS-MUON
   ANCHOR CHOICE each time — the layer straddle AGENTS.md singles out.
   **Owner decision, 32 times. Not guessable.**
2. **22 diagnosed reverts.** 17 "no gain" (12 with ZERO casts to remove — the
   float64 arrives by a route neither a dps raise nor a cast removal touches)
   and 5 laundering-guard hits (`codata_reconciliation` emitted
   `0.782333409309999949776…`: an exact mpf round-tripped through a double
   downstream, printed at 40 digits). Each needs its entry point found.
3. **The 593 remaining fields.** Re-measure; do not quote this figure.

## Traps established, each pinned by a selftest

- **The A/B split is a STATIC HEURISTIC and cannot settle any single
  producer.** A one-hop import-cone check reported "13 misfiled B→A" —
  RETRACTED: the inherited `set_compute_dps()` in `mass_at_3A_proper` is
  INSIDE A FUNCTION, and the hits came from an `ast.walk` descending into
  `def` bodies. An earlier regex draft was worse — it skipped comments with
  `line[0] != "#"`, letting through a docstring line starting with a backtick,
  so three producers were reclassified on the strength of PROSE.
- **"Round-trips through float64" does NOT prove laundering.** It flagged 55
  of 302 drained fields; all 55 are exact `k·2^-235` ULP residuals, and a
  power of two round-trips losslessly. Flag for reading, never decide.
- **The flip alone is necessary but NOT sufficient.** mpmath defaults to
  `mp.dps = 15` (~53 bits), so mpf constants still compute at float64 grade
  until the producer raises dps. Removing casts without raising dps is WORSE
  than nothing — it serializes a 53-bit value at full width (the
  float64-padding defect).
- **`math.log(mpf)` does not raise, it DOWNCASTS.** This module's own
  `Q_NEUTRON_MEV_ERR` was quietly the last float64 quantity after the casts
  came off.
- **`mpf(repr(x))` is right for a float, broken for an mpf.** `repr(mpf('.78'))`
  is `"mpf('0.78')"`, unparseable. 96 sites unwrapped; the OTHER 84 in the tree
  lift genuine floats and must stay.


## Session 2026-08-30 — the work order in this bean is INVERTED, and two drains landed

PR #6060. Job 3 re-measured, job 1 untouched (owner-blocked), bucket-A drain
started and immediately re-scoped.

### Job 3: re-measured, no drift

    ACTIONABLE fields  593    files 208
      A. dps raised          304   (153 producers, long-tailed: most carry 2)
      B. float64-equivalent  284
      C. producer not found    5

Reproduces the merged figure exactly. Re-checked against the 33 commits main
gained during the session: only 7 touch `computations/`, none in the candidate
set.

### THE WORK ORDER IS BACKWARDS — pick by BINDING shape, not by edit shape

I selected the 40 producers with an inline `computed=float(...)` because that
shape is mechanically rewritable. **That criterion selects AGAINST gains.**

    inline `computed=float(...)`     11 tried -> 0 KEEP, 4 REVERT, 5 SKIP
    local  `x = float(EXPR)` -> x    both confirmed gains are this shape

Not statistical. An inline cast at the assertion is what you write when
WRAPPING a solver's float; binding to a local first is what you write when
CARRYING an mpf. **Next agent: work the ~100 local-binding producers first.**

### Bucket A contains producers that are float64 IN FACT

Four confirmed: he4_sdp_compositional_probe, borromean_per_lambda_fr_probe,
fr_pullback_k1_k2_test, qbeta_c3_phib_pole_seed_sensitivity_probe. Each calls
`set_compute_dps()` (so the static classifier files it A) while its asserted
value comes from a solver, a helper, or a float accumulation. `_precision.fmt`
**short-circuits a Python float to `str()`** — its own docstring says so — so
the prescribed repair changes the JSON type and NOTHING ELSE.

This is this bean's own "the A/B split is a STATIC HEURISTIC" trap reached
from the OPPOSITE side: a bucket-A file that is float64-valued. So A=304
OVERSTATES what is drainable; the real boundary is between the two figures.

### Two drains landed

    probe_bring_residue_resolvent.py        8 fields  17 -> 60 digits
    qbeta_c3_two_route_cross_pin_probe.py   2 fields  17 -> 60 digits

Second witness: 16 raw float64 fields -> 1 (survivor is `expected: 0.0`).

### Automation ceiling: 2 of 152

With the only safe guard (the local feeds assertion values and nothing else),
exactly **2 producers of 152** are auto-rewritable. Everything else reuses the
local in a print or a comparison, where stringifying changes behaviour. This
CONFIRMS this bean's "nothing here is a candidate for a textual sweep", now
with a number.

### Traps established this session

- **`f"{mpf:.4f}"` raises TypeError.** Dropping a cast is not sufficient on
  its own; every `:.Nf` print of that value must move to `mp.nstr`. I found
  the second such print only by RUNNING the producer — it was on a branch the
  first run did not take.
- **A cast can hide in a list comprehension.** `dists = [(nm, float(...)) ...]`
  then `min(dists, ...)`: `min` chooses among values already cut to 17 digits.
  No rewriter here finds that shape.
- **The drain driver's `restore()` wipes a previous KEEP.** Batch drains must
  commit between producers, or run one at a time. (Batch 1's results were only
  trustworthy because it had 0 KEEPs.)
- **Re-running a producer in a bare container DOWNGRADES its provenance
  block** (numpy/scipy/python/pyhecke_native). The witness tooling warns and
  refuses. Build a venv matching the recorded environment; `pyhecke_native` is
  not on PyPI and must be built with `maturin build --release`.
- **precision-gates.sh already exits 1 on a CLEAN tree in a fresh container**
  (q0-anchor flip, q0-anchor refill, mpf(<float>) source, float64-padding,
  q0-value drift, CODATA stale-edition, mixed mpf/f64). Measure that baseline
  before attributing any red to your own change.

### Tooling added (both selftested; both were WRONG first)

- `computations/audits/assertion_drain_verify.py` — the methodology this bean
  states twice. **Its first version reported phantom gains**: it read a JSON
  float as the exact BINARY double against a string read as an exact DECIMAL,
  manufacturing a ~1e-17 difference from nothing (five phantom gains on a
  producer whose values are byte-identical). The right question is not "did
  the string change" but **does it carry information binary64 cannot hold**.
- `computations/audits/assertion_value_provenance_audit.py` — predicts
  DRAIN-NO-OP statically. **Three rule versions, first two pushed:**
  v1 flagged every sum/min/max (35/152 — wrong: `sum(1 for ...)` is an exact
  integer count); v2 required a visible float64 argument (3/152 — missed a
  confirmed case); v3 flags unless the accumuland is provably an int literal
  (34/152), validated **2 of 3** against the drain batch, negative control
  clean. Blind spot is structural: it is call-site-local and cannot see a
  float64 produced INSIDE a helper.

**A green selftest was never evidence about the corpus.** Both tools passed
their selftests through every wrong version; only running them against real
producer verdicts corrected them.

### Still open

1. 32 q-dependent producers / 209 fields — owner decision, 32 times. Untouched.
2. The 22 diagnosed reverts from #6022 — no committed list exists, so the list
   itself must be re-derived. DRAIN-NO-OP is a candidate explanation for part
   of the "no gain" half.
3. Bucket A minus the 4 confirmed no-ops and the 2 drained. Work the
   local-binding shape first, per above.
4. `computations/witness-raw-float64-audit.witness.json` regenerates with
   total_fields 35109 -> 34779 and drained_files +3, while this session's
   drains account for far less. NOT committed — the movement is not
   established as mine. Regenerate on a clean tree and attribute it.


## Continued 2026-08-30 — the binding-shape finding is confirmed, and three new traps

### The shape split, now with numbers

    inline `computed=float(...)`     11 verdicted -> 0 KEEP
    local  `x = float(EXPR)`          9 verdicted -> 7 KEEP

**Work the local-binding shape.** Not a tendency — 0/11 vs 7/9.

### Drained this session: 21 fields over 8 producers

    probe_bring_residue_resolvent            8
    qbeta_c3_two_route_cross_pin_probe       2
    qbeta_habiro_residual_probe              3
    seifert_volume_meson_n7_extension        2
    q0_figure_eight_phase_derivation         2
    binding_endomorphism_deuteron            2
    binding_per_bond_decomposition           2   (+ a STALE VALUE, see below)
    difference_knot_volume_extrema_stability 1   (unblocked by snappy)

Ratchet drained-since-baseline moved 150 -> 156 files, +623 -> +631 fields.

### THE TRANSFORM: parallel binding, not rewriting the local

Rewriting `x = float(EXPR)` to `x = fmt(EXPR)` is WRONG whenever `x` is read
anywhere else, and it usually is. `fmt` returns a str; `f"{x:.4f}"` on a str
raises, exactly as `f"{mpf:.4f}"` raises TypeError. Instead:

    x_exact_mpf = EXPR
    x = float(x_exact_mpf)      # unchanged; every existing use still works
    ... computed=fmt(x_exact_mpf)

Only the witness field moves, so no safety guard is needed at all. (Where
nothing but the assertion reads the local, the simple rewrite is used so no
dead line is left.) Driver at /tmp/drain_driver.py — NOT committed; it is
scaffolding, and the committed instruments are the two audits.

### 🛑 `git checkout -- <file>` DOES NOT give you an unmodified baseline

The driver now STAGES each KEEP, because its own restore uses
`git checkout -- <path>` which restores from the INDEX — that is what stops a
batch wiping earlier KEEPs. The same fact then makes `git checkout --` useless
for reverting: I ran a "truly unmodified" producer that was still my drained
version, and it reported a 17% VALUE-MOVED that would have been blamed on the
cast removal. **`git checkout HEAD -- <file>` is the spelling that reverts.**
Verify with `grep -c 'fmt(' <producer>` before trusting a baseline.

### A committed witness is STALE by 17% (independent of any drain)

`computations/binding-per-bond-decomposition.witness.json`,
`method_discrepancy_recorded`:

    committed         28.749413293755964
    fresh unmodified  23.800662623432725      rel 0.172

Measured on a genuinely unmodified producer (checked out from HEAD, 0
occurrences of `fmt(`). It is a diagnostic (records the binding_canonical vs
H_{3A} Δtr gap, tolerance 1) with nothing asserting on it downstream.
HYPOTHESIS NOT VERIFIED: this bean already records import-cone drift in exactly
this cone (`binding_canonical` source-stable while `tr_M_atom` moved 48%
because `tr_m_atom_via_transfer` changed). This producer reads
binding_canonical. Plausible mechanism; establishing it needs the import-cone
audit. Refreshed in a commit that leads with the value change, not with "drain".

### 🛑 "producer exit 1" is not a producer-health figure

9 of 13 exited 1 on an unmodified run. Triaged, they are three different
things and only one is a producer bug:

    ModuleNotFoundError: snappy       ENVIRONMENT — `pip install snappy`
                                      (SnapPy 3.3.2) and it runs; it then
                                      drained cleanly
    FileNotFoundError: jet-knot-...   a missing UPSTREAM WITNESS
    TypeError: Cannot convert expr    a genuine producer error

"9 of 13 cannot run" would have been a wrong headline. Install the optional
deps before counting: mpmath, sympy, numpy, scipy, snappy, and
`pyhecke-native` built locally (`maturin build --release`, it is not on PyPI).

### Recorded environments differ PER WITNESS — one venv cannot match them all

Correcting my own looser phrasing: `difference-knot-volume-extrema-stability`
records python 3.11.15 / numpy 2.4.6 (bare-container versions), while the venv
built for the earlier witnesses is 3.13.12 / numpy 2.5.0 / scipy 1.18.0. So
that re-run UPGRADES the block rather than matching it. Honest provenance, and
the tooling only refuses downgrades — but do not claim a blanket "matched
environment" across the corpus.

### Remaining bucket-A map (146 producers, measured on this branch)

     84 producers  173 fields  float() present but not reaching an assertion value
     34            64          predicted DRAIN-NO-OP (float64-valued)
     20            33          rewriter finds a cast -> drainable
      7            12          no float() at all — float64 enters another way
      1             4          producer file not found

The 84-producer group is the real remaining body of work and it is NOT
mechanical: the cast sits in a helper, a dict, or a comprehension. The
`min(dists, ...)` case in qbeta_c3_two_route_cross_pin is the worked example.


### CORRECTION to the count two sections up: 19 fields, not 21

I wrote "21 fields over 8 producers". **It is 19.** The 21 summed the drain
verifier's GAIN rows, which is not the same population as the tranche: a field
can be removed from the tranche without gaining digits (NO-DIGITS-RECOVERED is
still converted to a string), and a GAIN row can land on a field that was
integral and therefore never counted.

Measured properly — actionable fields in each drained witness, `origin/main`
vs this branch:

    9 -> 0  bring-residue-resolvent-probe
    2 -> 0  qbeta-c3-two-route-cross-pin
    2 -> 0  qbeta-habiro-residual
    1 -> 0  seifert-volume-meson-n7-extension
    1 -> 0  q0-figure-eight-phase-derivation
    1 -> 0  binding-endomorphism-deuteron
    2 -> 0  binding-per-bond-decomposition
    2 -> 1  difference-knot-volume-extrema-stability   <- one left undrained
                                                          in this witness

    20 -> 1, i.e. 19 removed.

Corpus tranche now **574 fields / 201 files** (was 593 / 208). The 19-field
delta is entirely attributable — I checked against `origin/main` per witness
rather than differencing two whole-corpus measurements taken 68 commits apart,
which would have conflated my drains with main's movement.

**Quote the per-witness attribution, not a whole-corpus difference.** This
branch merged 68 commits of main mid-session; a before/after of the global
figure cannot separate the two.


## 2026-08-30 — status at PR #6060 rebase onto `a917f3da1e`

**Done:** Job 3 re-measure reproduced `A=304 / B=284 / C=5` exactly. 20 fields
drained over 8 producers, all 17 → 60 digits, attribution measured per-witness
against a `git worktree` of the exact base.

**The bean's work order was backwards and is corrected in the PR body.** The 40
producers with an inline `computed=float(...)` are the *mechanically* easiest and
the *least* rewarding: 11 tried → 0 KEEP, against 9 tried → 7 KEEP for the
`x = float(EXPR)` … `computed=x` local-binding shape. Mechanical, not
statistical — an inline cast is what you write when wrapping a solver's float; a
local binding is what you write when carrying an `mpf`. **Work the local-binding
shape first.**

**Bucket A overstates what is drainable.** Four producers call
`set_compute_dps()` (so the static classifier files them A) while the asserted
value comes from a solver, a helper, or a float accumulation. `_precision.fmt`
short-circuits a Python `float` to `str()`, so the prescribed repair changes the
JSON type and nothing else. `computations/audits/assertion_value_provenance_audit.py`
predicts this statically — 34 producers / 64 fields of the 152 bucket-A — but it
is call-site-local and cannot see a float64 produced inside a helper.

**Remaining, unchanged:**

1. **32 q-dependent producers / 209 fields** — each forces a proton-vs-muon
   anchor choice. Owner decision, 32 times. Untouched.
2. **84 literal `expected` fields across 69 producers** — mechanically safe
   fidelity fix, needs 69 producer re-runs.

**Do not run item 2 in a weaker container.** Same constraint recorded on
`qou-3e5m`: `save()`'s environment guard fires only on the preserve path
(`_witnesses_substantively_equal`), and a drain is substantive by construction,
so the rewrite path takes a downgraded `environment` block under a warn-only
check. Match python/mpmath/clarabel to what the target witnesses record first.


---

## A float64 in this same probe that your drain could not have seen (found 2026-09-19, bean `qou-ejfy`, status NOT changed)

Your ledger records `probe_bring_residue_resolvent.py  8 fields  17 -> 60 digits`
and `9 -> 0  bring-residue-resolvent-probe`, which is the
`.assertions[].computed` class and is done. **One more float64 survives in that
file, and no witness-facing detector can reach it**, because it is upstream of
an **integer**:

```python
vals = [float(canonical_resolvent(q, n)) for n in POLE_ORDERS]   # line 85
distinct_count = len(set(round(v, 20) for v in vals))
w.add_assertion(name="resolvent_values_distinct", computed=distinct_count, ...)
```

`canonical_resolvent` returns an mpf; the cast keeps ~16 digits. The stored
field is `distinct_count`, a declared count that correctly stays an `int`, so
the raw-float64 ratchet, the padding audit and the `.assertions[].computed`
sweep are all structurally blind to it — there is no float in the witness. The
defect is in the *computation of the count*, not in a stored value.

**`round(v, 20)` is decoration.** `v` is already a binary64, so rounding it to
20 decimal places is a no-op past ~17 significant digits. The code's shape
implies a 1e-20 distinctness bar; the arithmetic can only certify ~1e-16. That
is the "never report a float64 agreement as to-N-digits" rule, reached through
a `round()` rather than through a printed string.

**Measured impact here: NONE — and say so rather than implying a wrong answer.**
At the proton pin the four values are

    n= 3  1.40036565495469647382847079723
    n= 4  1.46486612346572584804175008795
    n= 9  2.14910999622996260471937011268
    n=10  2.45999841888754838419214787150

minimum pairwise separation **0.0645**, fourteen orders above the binary64
floor. `distinct_count` is 4 under either arithmetic. So this is a false
precision *claim* with no effect on the verdict — worth fixing for the same
reason the rest of the class was, not because a number is wrong.

**Fix**: drop the cast and count at a declared precision, e.g.
`len({mp.nstr(v, 40) for v in vals})`.

**NOT fixed here, deliberately.** Re-running the producer on this container
would commit a WEAKER provenance block than the one on disk — its guard reports
`python 3.13.12 -> 3.11.15; numpy 2.5.0 -> 2.4.6; scipy 1.18.0 -> 1.17.1`, and
the Python version is not installable away. Worth a provenance downgrade only
if bundled with a run that needs one anyway; it is also a different domain from
the PR that found it (#7438, Markov-trace assembly chains). Left to whoever is
on this bean, on a container matching the recorded environment.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress 2026-11-17 (PR #8290)

Drained the remaining binary64 downcast `float(canonical_resolvent(q, n))` and `round(v, 20)` in `computations/probe_bring_residue_resolvent.py` by evaluating distinctness directly in `mpf` via `mp.nstr(v, 40)` and regenerated `computations/bring-residue-resolvent-probe.witness.json` on PR #8290 (`1c907342f24ac048c99eb24f30832b0b87b024b0`).
