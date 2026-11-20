---
# qou-epxx
title: 'raw-float64 drain: two float() casts on full-precision inputs — q0_proton in bn_minus_bp_brane_tower_parity_probe (~44 digits lost) and CAL-1 m_e + AME_B in atom_vhyp_bar_trace_test (~2e-17, in the arithmetic not just the witness)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-26T14:28:50Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Picked up 2026-09-26 as exemption-covered drain work while PR #7457 waits on
merge permission. Capped at the idle policy's budget rather than opened as a
campaign: the drain queue is **975 witnesses / 25,396 fields** live (see §0).

## 0. Quote the AUDIT, not the baseline file — they disagree by design

`raw-float64-baseline.json` lists **1003 files / 30,985 fields**; the live
audit reports **975 / 25,396**. Both are right about different questions: the
audit splits out three declared carve-outs the baseline file does not —
`deprecated-f64` (**91,732** fields in 6 witnesses), `f64-integrator` (65 in 3),
and `runtime-duration` (125 in 62, a reclassification not a drain). I quoted the
baseline number first and corrected it; do not repeat that.

## 1. The ratchet counts NON-INTEGRAL floats only — confirmed independently

Eight 1-field baseline entries were scanned. Each carries 1-4 raw floats but
exactly **one non-integral** float, matching its baseline count of 1 every time.
So `1.0` / `0.0` / `10.0` are invisible to the ratchet by design.

That corroborates, from the other direction, the `braid_encoding_audit` finding
recorded on `qou-ejfy`: its 6 warned `word_cd` floats are `1.0`/`0.0`, which is
why the producer's guard warns while the ratchet reports the file clean. **Two
correct tools, different rules — not a contradiction.**

It also means a whole class in the queue is NOT drainable-by-precision: of the
eight, five were authored 4-sig-fig literals (`expected = 17.4`, `120.6`,
`0.7587`, `tolerance = 10.0`). An `mpf` cast on those buys nothing; they are a
serialization-style question, not a precision one. Do not spend drain budget
on them.

## 2. FIX A — `computations/probes/bn_minus_bp_brane_tower_parity_probe.py`

Line 252 passed `float(qp)` into `_emit_witness`, which wrote it verbatim to
`substrate.q0_proton`. `qp = mpf(str(q_at()))` under `set_compute_dps()`, so it
carries the full 60-digit proton pin and the cast kept 16:

    stored   1.1099785827513808
    true     1.10997858275138080759166909561076887987449912187357873607281

**~44 digits, and this one is exemption 1 proper.** Fixed by carrying the mpf
and serializing once with `_precision.fmt` at the emit site.

### The trap that nearly went the wrong way, recorded because it is general

The obvious repair — wrap the existing float in `fmt()` — is **worse than the
defect**:

    fmt(float(qp))  = 1.10997858275138083783417641825508326292037963867187500000000
    fmt(qp)         = 1.10997858275138080759166909561076887987449912187357873607281
                                   ^ diverge at the 17th significant digit

It pads a binary64 value to 60 digits, manufacturing **44 wrong ones**, i.e. it
drains the raw-float64 ratchet straight into the float64-PADDING ratchet
(`qou-3jwy`). Carry the mpf to the emit site; never `fmt()` a float.

I also reached the opposite wrong conclusion first, and the cause is worth
knowing: measuring `q_at()` in a bare harness **without `set_compute_dps()`**
returns ~15 digits, which reads as "the cast loses nothing, and fmt would pad".
Both halves of that are artifacts of the harness. **Measure a producer's
constants under the producer's own precision setup.**

## 3. FIX B — `computations/atom_vhyp_bar_trace_test.py`

Lines 51 and 54 cast three `codata_constants` mpf values to float:

    M_E  = float(_M_E)                                   # CAL-1
    AME_B = {... float(AME_B_DEUTERON_MEV_VALIDATION) ...}

Both feed the arithmetic at lines ~87-88 (`B / (M_E * BP)`), so these are
computations in binary64, not displays — AGENTS.md permits `float(x)` only
inside an f-string. Fixed by dropping all three casts; `B_AME_MeV` now
serializes via `mp.nstr(B, 18)` like its sibling fields.

### I claimed this loses nothing, and that was WRONG — the test was wrong

I first compared `str(v)` against `repr(float(v))`. Both render `2.2245662`, so
the DECIMAL RENDERINGS agree and it reads as an exact round-trip. Comparing the
**values** — `mpf(str(v)) == mpf(float(v))` — is False for all three:

    M_E_MEV (CAL-1)   rel err 1.74e-17
    AME_B_DEUTERON    rel err 2.78e-17
    AME_B_TRITIUM     rel err 2.53e-17

**Scope it honestly:** ~2e-17 is *below* the L1 1 ppQ (1e-15) target, so this is
not claimed to threaten L1. It is a float64 path in a computation, which the
rule forbids outright, and `M_E` is CAL-1 — the constant that fixes the MeV
unit. That is reason enough not to round it on the way in; it is not a dramatic
number and should not be reported as one.

## 4. 🛑 NEITHER WITNESS IS REGENERATED, and for FIX B the reason is a finding

Re-running `atom_vhyp_bar_trace_test` moved `tr_M_q0` **1.33178248330425462 →
1.45469928113235984 — 9.2 %**. My change cannot do that: `tr_M(Z, N, q)` reads
neither `M_E` nor `AME_B`.

**Verified by reverting my source change and re-running `main` unmodified: it
produces 1.45469928113235984, byte-identical to the fixed version.** So the 9.2 %
is entirely pre-existing **import-cone drift** and the committed witness is
stale — the producer's own source is not what moved.

The committed witness is dated **2026-06-22**, the same date as
`derive-binding-bond-type`'s, whose 4x drift I recorded this morning on
`qou-7xa5` — also cone drift, also invisible to a `git diff <producer>`. **Two
witnesses, same date, same class**, which suggests a cone-wide event in that
window rather than two coincidences. Not chased here; worth a scoped look.

Its internal cross-check was already failing before any of this: the hardcoded
catalogue `TRM_Q0_WITNESS["deuteron"] = 1.3317821792991125...` disagrees with
even the *committed* `1.33178248330425462` at the 7th digit.

So: **source fixes only, no witness commits.** Regenerating a derived artifact
that belongs to someone else's arc is not covered by either ASK-THE-OWNER
exemption, and committing this one would publish a 9.2 % move I did not cause
and cannot explain. The consequence is that the ratchet count does **not** drop
today — the float64 path is removed for whoever regenerates next, for a reason
of their own.

## 5. What is NOT claimed

- The drain queue is not measurably smaller. Two producers can no longer emit
  float64; no witness was re-emitted.
- The 9.2 % drift is *observed*, not diagnosed. I did not identify the cone
  module responsible, and this bean does not assert one.
- `qou-xwjs` (the qns probes) is a different file set and is untouched.


---

## 6. Gate-family triage (measuring only — no sweep started)

`scripts/precision-gates.sh` on `main`, full family, ~3 min: **10 RED**. None is
mine. Sized so the sweep-vs-tranche question is answerable rather than guessed:

| gate | scope | shape |
|---|---|---|
| module-const precision | **LOSSY 1** (+41 padding-risk, 21 files) | one line |
| mixed mpf/f64 -> serializer | 7 candidates, baseline 3, **4 over** | small |
| q0-value drift | 207 stale under a 329 baseline, **NEW 5** | small |
| never-raises-dps | 9 producers / 31 constructions | small |
| import-time dps | **8 proven lossy** (+26 not provably so), 21 files | small tranche |
| q0-anchor flip | ~24 `*_NO_REASON` of 1495 OK | annotation |
| float64-padding | 75 occurrences, 29 values, 8 live files | medium |
| q0-anchor refill | **drained 204** / NEW 188 | mixed — the 204 only need the baseline re-banked |
| reference-literal | 113 TRUNCATED + **90 DIVERGENT** ("agrees then DISAGREES — WRONG, not short") across 100+ files | sweep |
| witness-value copy | 222 NARROW in 148 files | sweep |

So roughly **5 small / 2 medium-mixed / 2 genuine sweeps**. The two sweeps are
what ASK-THE-OWNER gates; the small ones are individually exemption-1 shaped.
Nothing here is claimed to be a defect until its own file is read — this is a
sizing pass.

## 7. 🛑 `rev_e_infinity_g1_bottom_edge_cap_probe` — fix IDENTIFIED, NOT VERIFIED

The module-const LOSSY row is `deltalambda/rev_e_infinity_g1_bottom_edge_cap_probe.py:168`:

    RECORDED_DIFF = mp.mpf("0.0198162676389039602300948111946348416306")

a 40-digit literal, and the file **never imports or calls `set_compute_dps` at
all** — so it builds its constants, and runs its whole comparison, at mpmath's
default `mp.dps = 15`. Measured:

    literal          0.0198162676389039602300948111946348416306
    built at dps=15  0.0198162676389039595081786870878204354085...
                                      ^ diverges at the 18th significant digit
    rel err 3.64e-17

Real, and **below the L1 1 ppQ (1e-15) target** — not a claim that L1 was
threatened.

**Blast radius is zero external consumers**: the only two references to this
probe in the repo are the file itself and its own witness. That makes it the
cleanest exemption-1 target in the family ("raising `mp.dps` where it was
silently truncating" is the directive's own wording).

**But the fix is NOT in the branch, because I could not verify it.** Adding
`set_compute_dps()` at module scope moves the probe from 15 dps to 70 — a real
behavioural change to every number it computes, not a serialization tweak. The
run to see that movement **did not complete**: killed silently after ~19 min
with the log frozen at 7 lines (last line `G1a/G1b/G1c vary the bottom row
cap`), no witness written (mtime unchanged at 2026-09-19). Per the long-compute
discipline a silent stop is treated as a crash, not a success, so the edit was
reverted rather than committed unverified.

**Next agent:** the diagnosis and the measurement above stand; what is missing
is one completed run. Launch with `-u` and a teed log, budget well over 20 min,
and expect the witness's numbers to move — that movement is the intended effect
and is explainable (15 -> 70 dps), unlike the three cone-drift cases in §4.
Note the witness is hand-rolled (no `WitnessBuilder`, so no `scriptHash` /
`engine` / `durationMs`), so staleness detection does not cover it.

## 8. Branch relocated by the `.beans/` -> `beans/defs/` move

`main` `58a1f3231c` (bean `qou-utbr`) moved the bean store, which turned this
branch's bean ADD into a `CONFLICT (file location)` against the renamed
directory — structural, not textual. Rebased onto `6957def215` and resolved by
accepting git's own rename detection into `beans/defs/`; `beans/beans.json`
declares DIRECTORIES rather than individual beans, so no index row was needed.
Verified afterwards: no file left under the old `.beans/` path, both source
fixes intact, `merge-tree` exit 0.


---

## 9. `mixed mpf/f64 -> serializer` is RED on FOUR FALSE POSITIVES — verdicted 7/7

Took the smallest gate tranche from §6 and verdicted every candidate. The gate
reports **7 candidates / baseline 3 / 4 OVER**, and the audit itself says these
are "CANDIDATES for an agent verdict, not proved defects". Result: **3 real, 4
false**, and the 3 real ones ARE the baseline.

### The 4 false positives

| site | why it is not a defect |
|---|---|
| `binding_rotation_phase_lead.py:196` and `:197` | `rs = [rho[i] …]` are **mpf**, so `max(rs)/min(rs)` stays mpf and `fmt(spread)` is correct. The audit cannot see that max/min over mpf is mpf. |
| `borromean-axial-coupling.py:384` | `_gap_rec = getattr(lp, "gap_recomputed_str", None)` — the `_str` suffix is real (`he3_pairknot_composite_lp_probe.py:258` groups it with `residual_primal_str` / `residual_dual_str`, the string serializations of LP duals), so `mpf(_gap_rec)` is `mpf(str)`, exact. An untyped `getattr()` is being read as float64. |
| `probes/nucleon_h3_marshalling_divergence_probe.py:242` | the named taint source is `mp.fsum(...)`, which returns **mpf**, over terms that are `mp.mpf(str(...))`. |

**The `binding_rotation_phase_lead` pair is the one to notice: the audit is
re-flagging an ALREADY-DRAINED site.** Lines 181-185 of that file carry a
comment recording its own prior fix — *"NO `float()` HERE. `rho[i]` is an mpf;
`float(rho[i])` truncated every spread below to binary64…"*. A detector that
re-flags the fix it prompted is worse than one that misses: it spends the next
agent's budget re-deriving a settled verdict.

### The 3 real ones are the baseline, and they are BLOCKED — do not "fix" them

`qbeta/qbeta_habiro_taylor_investigation.py:235-237`. Real, and worse than a
plain cast:

    tr_p_num = float(sp.N(tr_p_sym.subs(q, sp.Float(str(q0_num), 50)), 30))
    "tr_M_proton_at_q0": mp.nstr(tr_p_num, 18)
    delta_tr_num = tr_n_num - tr_p_num

sympy computes at 30 digits, `float()` keeps ~16, the witness then asks for
**18** — and the extra digits are WRONG, not merely absent. Demonstrated on a
stand-in: `nstr(float, 18)` gives `1.33178217929911247` against the true
`1.33178217929911251`. Plus `delta_tr_num` is a float64 subtraction of two
nearby values.

**They are already known and deliberately parked.** The baseline's own
`_comment`: *"Drained 28 -> 3 under bean `qou-65qv`. The residual 3 are all in
`qbeta_habiro_taylor_investigation.py` and are BLOCKED, not unexamined: the
float() fix there is correct and written, but re-running that producer
regenerates its witness from convention C to convention D, which belongs to bean
`qou-cds1`."* So my independent verdicts match the recorded ones exactly — which
is the useful part of having done them blind.

### Consequence

**The gate's RED is entirely false positives.** The 3 genuine defects sit AT the
baseline (so they do not trip `--strict`); the 4 that trip it are all
misreadings. A blocking gate red on 4-for-4 false positives trains agents to
discount it, which is how a real regression gets waved through.

### One attempted fix, and it FAILED — recorded so it is not re-tried

`y_lambda_wenzl_bridge_numeric` had no return annotation, and the audit's
registry is built from `-> mpf` / `-> float` annotations, so `y[λ]` read as
unknown-typed. Annotating it `-> mp.mpf` (runtime-verified, committed, correct
on its own merits) **did not clear the `nucleon_h3_marshalling` flag**: measured
before and after, registry 792 -> 793, candidates stayed 7, taint still
attributed to `mp.fsum(` on L232.

So the cause is NOT the missing annotation. What is established is narrower and
sharper: **the flag contradicts the audit's own spec**, whose line 49 classifies
`mp.*(...)` as MPF. The mechanism is NOT established — a list-comprehension
argument and a multi-line call shape are both consistent with what was observed,
and neither was tested. The docstring on the annotated function now warns the
next agent off this route.

**Not fixed here, and the reason is the ASK-THE-OWNER gate**: narrowing the
detector changes what a blocking gate reports corpus-wide, which is the
"changes numbers everyone quotes" class rather than either exemption. Framed
for a decision instead.


---

## 10. 🛑 THE g1 RUN COMPLETED AND MY PREDICTION WAS WRONG

The run finished: **exit 0, 7/7 checks pass**, ~381 s, witness written. The
probe's own mathematical verdict is unchanged — *"G1 is STILL OPEN"*.

**§7 and commit `8f2ba091b2` both predicted the witness would move**, on the
reasoning that "raising dps moves the probe from 15 to 70, which changes every
number it computes". **That is false.** Measured field-by-field against `HEAD`
with the ephemeral keys masked:

    NON-ephemeral fields that moved: 0

The entire diff is **five lines**: `computedAt` plus four wall-clock `seconds`
(452→381, 9→8, 28→24, 82→68). Not one numeric result changed.

**Why, and it is the interesting part.** This probe computes on **exact integers
at scale 1e-40** — its comparison is over integer row-profiles like
`[1,1,2,2,2,2,1,1]`, so mpmath's working precision never entered the results at
all. `RECORDED_DIFF` feeds only an internal boolean (`recorded_s_equal`), and a
boolean does not flip at 1e-17. Corroborating this from the committed artifact
rather than from my reasoning: `diff_at_break` already carried the full 40 digits
**before** the fix, as an unchanged context line in the diff.

So the truncation at construction was real (3.64e-17, measured in §7) and its
effect on published output is **nil, verified**. That is the best outcome a
precision fix can have — it means nothing downstream was silently leaning on the
truncation — but it is NOT what I said would happen, and the claim is withdrawn.

**Contaminated by that wrong prediction, now corrected:** §7 of this bean, and
commit `8f2ba091b2`'s message. The commit stands (the source fix is right); its
forecast does not.

**The gate row is CLOSED.** `module_const_precision_audit.py` now reports
`LOSSY: 0` (was 1), across 20 files (was 21). `PADDING_RISK` is unchanged at 41.

**The witness is NOT committed.** The diff is provenance and timing only, which
is exactly the churn `qou-v0t8` says not to commit — the same disposition as
`braid_encoding_audit` in §"merge-time verification". Reverted; tree clean.

## 11. STANDING DOWN from the `never-raises-dps` tranche — it is someone's arc

Scoped it as the natural sibling of §10 (same exemption-1 shape) and **did not
take it.** The gate is red on **4 NEW producers**, with `REGRESSED 0` and
**42 files / +175 constructions already drained** — i.e. it is being actively and
successfully worked.

- **`qou-fl9i` is `in-progress`**: *"Raise 838 sub-canonical `mp.dps` sites to
  `set_compute_dps()`"*. That is this drain.
- `qou-yh08` (`todo`): *"952 sites set precision below OUTPUT_DPS=60"*.
- **3 of the 4 NEW files are already claimed** — `saddle_offset_zero_location_probe`
  and `rho_binding_constancy_probe` by `qou-hgm6` (*"three q0-stale probes compute
  in float64 end-to-end — the literal cannot be drained without fixing that
  first"*), the latter also by `qou-840k`. Only
  `flavor_split_pair_product_half_ceiling_probe` is unclaimed.

AGENTS.md is explicit that mechanical work has ONE owner and must not be
overlapped; the research-overlap relaxation covers open-outcome questions, which
this is not. Left alone.

**Checked that §2/§3/§10 did not already overlap it**, since those are the same
class: none of `bn_minus_bp_brane_tower_parity`, `atom_vhyp_bar_trace_test`,
`y_lambda_wenzl_bridge` or `rev_e_infinity_g1` is named in `qou-fl9i` or
`qou-yh08`. The g1 site came from the **module-const** gate's LOSSY row, a
different gate from the never-raises-dps one.


---

## 12. MERGED — PR #7457, merge sha `be07fbd97f`, 8/8 replayed

Owner gave explicit merge permission; `/prepare-merge-auto` run in full. Rebased
onto `origin/main` @ `19387e8707` (9 commits on) and re-verified there:
`module_const_precision` **LOSSY 0**, raw-float64 ratchet NEW 0 / REGRESSED 0
exit 0, `atom_vhyp` exit 0, all four source fixes intact, tree clean.
`verify-merge-replay.py`: **8 branch commits, 8 replayed, 0 MISSING.**

The two long producers were not re-run, and that was measured rather than
waved at: **main's 9 commits touched zero `computations/*.py`**, so neither
import cone moved and the pre-rebase runs (422 s and 381 s / 7-of-7) carry.

## 13. 🛑 RETRACTED: the "2026-06-22 cone-wide event" — it is coincidence

Four times today I noted that two of the drifted witnesses share a `computedAt`
of 2026-06-22 and called it *"suggestive of a cone-wide event"*, each time
flagged as not-diagnosed and not-asserted. **Now measured, and it is not
supported. Withdrawn.**

**2026-06-22 is a below-average day, not a spike.** Across 3405 witnesses
carrying `computedAt` over 133 distinct dates:

    mean per day        25.6
    median per day       7
    2026-06-22          20      -> rank 38 of 133
    busiest day        393      (2026-08-23)

**And the coincidence is unremarkable on its own terms:**

    P(two random witnesses share a date)      = 0.0425   (1 in 23.5)
    with 4 drifted witnesses -> 6 pairs,
    EXPECTED same-date pairs                  = 0.255

Observed: 1. That is a roughly one-in-four event — precisely the kind of
pattern an eye manufactures from noise, which is why it read as a signal.

**One caveat against myself, in the direction that does NOT rescue the
hypothesis.** The null above draws uniformly from all witnesses, and my four
were not random — they came from the drain queue and so skew toward OLD
witnesses. Old dates carry *fewer* witnesses each, which makes a chance
collision *less* likely, not more. So the correction is small and it pushes the
wrong way for a rescue; the headline stands either way.

**What is NOT retracted.** Every individual staleness finding holds and was
verified per-file, by its own method:

- `derive-binding-bond-type` 4x — `qou-7xa5`
- `atom-vhyp-bar-trace-test` 9.2 % — verified by reverting my source and
  re-running `main` unmodified (byte-identical)
- `bn-minus-bp-brane-tower-parity` exact rationals — verified by `scriptHash`
  mismatch against unmodified `main` (`66ce72dd10ba` vs `d7fd2ea82e62`)

The per-file drift is real. The **cluster** is not. Do not go looking for a
common upstream cause on the strength of the date; there is nothing there to
find, and anyone who follows that thread is spending a session on a 1-in-4
coincidence I put in a PR body.

**Contaminated, and corrected here:** PR #7457 §4 (merged, so the body now
carries a claim this supersedes), the `qou-epxx` §4 table, and two commit
messages. This bean entry is the correction of record.


## 2026-09-27 — item (d): I REVERSED MY OWN RECOMMENDATION. Do not narrow the detector.

Owner instruction "resolve issues". I had reported the mixed-arithmetic gate's RED
as **4-for-4 false positives** and recommended narrowing it. **That recommendation
is withdrawn.** Re-verdicting the same four, I reversed twice in one sitting:

1. false positives (original claim, verdicted blind);
2. → TRUE positives, on finding explicit `float()` casts at
   `binding_rotation_phase_lead.py:133-136`;
3. → false positives *for the reason I first gave*, on measuring that
   `mpf(str(float(v)))` round-trips EXACTLY (rel_err **0.0** on all four AME
   constants — they carry ≤ 9 significant digits, far under 17).

**But the gate was right anyway, for a reason none of the three verdicts saw.**
That file has TWO consumers of `AME[iso]` and they behave oppositely:

    line 196  rho = mpf(str(AME[iso])) / vals[iso]     <- str() heals the cast
    line 247  strong_channel_rho(..., AME[iso], ...)   <- passed RAW

The second passes a binary64 straight into the arithmetic. The cast was safe only
where a `str()` happened to sit below it. **Fixed** — casts dropped, exemption 1.

Counter-intuitive and I nearly wrote it backwards: on the `mpf(str(...))` path the
`float()` detour was *cleaner* than passing the mpf, since `str(<9-digit float>)`
is exact while `str(<70-dps mpf>)` re-rounds. That is why `spread_pct` moves.

**Witness movement, honestly:** 16 fields. `d0_strong_channel/*` is the real fix
(the line-247 path). `aggregations/*/spread_pct` and `A3_pair_spread_pct` move at
~the 50th significant digit of a 60-digit serialization — **AT THE FLOOR**, not
claimed as an accuracy gain. Plus `/commitSha` (provenance). Assertion still
passes; producer exit 0.

**RESULT: candidates 7 → 5, OVER baseline 4 → 2.** Both
`binding_rotation_phase_lead` rows cleared **at the root**, not by widening a
carve-out. Baseline NOT raised (baselines drain, never grow).

### The remaining 2 over-baseline rows — both verdicted FALSE POSITIVE

* `borromean-axial-coupling.py:384` — `mp.mpf(getattr(lp, "gap_recomputed_str"))`.
  `lp_dual_solver.py:86` declares `gap_recomputed_str: Optional[str] = None`, so
  it is a **string** and `mp.mpf(<str>)` parses exactly. Taint inherited from the
  `lp` object. Blind spot: `getattr(obj, "<…_str>")` yields a string.
* `nucleon_h3_marshalling_divergence_probe.py:242` — `mp.fsum([...])` whose cone
  includes `marshal_to_chi_lambda_braid(chain, float(h))`. **Settled:**
  that marshaller returns `List[Tuple[int, int]]` — integer `(sign, gen)` pairs —
  and `h_val` only feeds a discrete four-way `classify_crossing`. No float64
  reaches the arithmetic. Blind spot: the detector propagates taint from a call's
  ARGUMENTS without consulting the callee's RETURN type, though it already keeps a
  registry of 793 `-> float` / `-> mpf` annotations that could answer it.

  Separate risk class, noted and NOT this gate's business: a binary64 `h` could in
  principle flip a borderline `classify_crossing` verdict. That is a discrete
  misclassification changing a sign by ±1, not a lost digit. Unmeasured.

### Also correcting a specific claim of mine

I wrote that the `mp.fsum` flag "contradicts the audit's own spec (line 49
classifies `mp.*(...)` as MPF)". **It does not.** Line 249 makes `mp.*(...)`
taint-**propagating** rather than taint-clearing, which is more correct than the
prose spec; the fsum's taint arrives through its arguments.

### Why the detector question goes back to the owner

The three narrowings the evidence actually supports are (i) `str(<Subscript>)`
round-trip, (ii) `getattr(…, "*_str")` is a string, (iii) consult the callee's
return annotation. (iii) is the cleanest and reuses machinery already present.
But a recommendation to narrow a **BLOCKING** precision gate, resting on a verdict
I got wrong twice in one sitting, is not one I stand behind — narrowing it would
have hidden the line-247 path this arc just fixed. **Owner's call.**

Commit `49df609730`.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8332, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-26: "beans(qou-epxx): the g1 run completed and REFUTED my own prediction -- zero numbers moved"). The work may be partly or fully done. Read the bean before you close it.
