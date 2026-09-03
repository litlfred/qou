# The first `binding_energy` value the corrected framework has ever produced

**Measured 2026-09-02.** Completes the `qou-sv7h` arc: the Rust LP-accumulator
kernel is wired into both loops, and `binding_energy` runs end to end for the
first time.

## The result

```
atom        Z   N       B_pred (MeV)      secs
deuterium   1   1       -7.271102125      942.3
```

against AME2020 (`ame_binding_mev(Z, A)`, signature confirmed empirically
against three known values — deuteron 2.224566, triton 8.481796, ⁴He 28.295662):

| | value |
|---|---|
| **predicted** `B(²H)` | **−7.271102125 MeV** |
| **AME2020** `B(²H)` | **+2.224566 MeV** |
| sign | **WRONG** |
| \|ratio\| | 3.27× |

Term decomposition, same run: `unified_iterative_correction = −9.1477362310`,
`sdp_cross_channel_contribution = 0.0`, so `binding_from_frobenius_pairing =
+1.8766`. The negative sign is carried by term 1.

## The sign was already negative before the correction

Important, and it constrains what the correction can be blamed for. The
accumulator was negative on the **old** (braid-violating) matrices too —
measured `−0.0319` (k=4) through `−2.1955` (k=8) — and is negative on the
corrected family — `−0.0896` through `−2.0200`. **The correction changed the
magnitude by 71–221 %; it did not introduce the sign.**

So this is not "the fix broke the physics". It is: the framework's binding
accumulator has produced a wrong-signed result all along, and until now nobody
could see it, because the function could not complete.

## What is established

- `binding_energy` **runs**, for the first time, in 942 s for A = 2.
- Its deuteron value has the **wrong sign** against AME2020 and is 3.27× the
  magnitude.
- Both checked-in gates pass on this tree:
  `lp_accumulator_kernel_gate.py` → **7.092e-48**, exit 0.

## What is NOT established

- **One atom.** A = 3 was still running at 28 min when this was written (cost
  grows as A²). A single point is not a pattern, and the sign could plausibly
  differ across the light isotopes. Do not generalise from deuterium.
- **No witness regenerated.** `hadron-knot-table.witness.json` is untouched.
- **Nothing about *why* the sign is wrong.** That is a physics question this
  measurement opens and does not answer.

## `ysn_braid_relation_audit.py` still exits 1 — that is CORRECT

`_build_ysn_matrices` is deliberately **unchanged**. The kernel bypasses it by
building the correct family in Rust; it does not repair the Python one. So the
braid audit continues to flag a real defect in a function that is **no longer on
the binding path**. Do not read its exit 1 as the wiring having failed, and do
not "fix" it by weakening the audit — other callers
(`sdp_cross_channel.py`) still use that builder and are still affected.

## What changed in the code

`unified_iterative_correction`: each partition's whole trajectory is precomputed
in Rust before Pass 1, and the step loop reads `(trace, log_norm)` from it.
**Every line of the accumulation — `raw_delta`, `cumul_partition`,
`final_tr_sign` — and the whole of Pass 2's complementary-slackness gate are
untouched.** That distinction is the point: a reimplementation that drops Pass 2
is wrong by ~4.6× (measured), which is why the kernel is wired *in* rather than
*around*.

`atom_character_raw`: same kernel, taking the final step's trace and log-norm,
which is all that function returns.

Both fall back to the original Python path when `pyhecke_native` is absent — a
bare container has no extension module, and this module must still import there.

---

# Second atom: the wrong sign is SYSTEMATIC, and the magnitude is nearly flat in A

| atom | A | B_pred (MeV) | AME2020 (MeV) | sign | \|pred\|/AME | secs |
|---|---|---|---|---|---|---|
| deuterium | 2 | -7.271102125 | +2.224566 | **WRONG** | 3.269 | 942.3 |
| tritium | 3 | -7.742121347 | +8.481796 | **WRONG** | 0.913 | 1567.6 |

**Both wrong-signed.** Two points is not many, but it is enough to say the sign
is not an A = 2 peculiarity.

**The more informative number is the shape, not the sign.** From A = 2 to A = 3
the prediction moves `-7.271 → -7.742` — **6.5 %** — while the experimental
binding moves `2.225 → 8.482`, **+281 %**. The accumulator is close to
**A-independent** over this range, where real binding grows steeply and roughly
linearly in A.

So the defect is unlikely to be a stray sign convention: flipping the sign would
give `+7.27` and `+7.74` against `2.22` and `8.48`, which is wrong in the
opposite direction at A = 2 and still nearly flat. **Whatever is missing is
extensive in A**, and a sign flip does not supply it.

That is consistent with the standing open problem recorded in AGENTS.md — the
"separate, super-pairwise additive extensive object" that the six Δ_λ closure
ansätze all failed to produce, and the pairwise cap
`QOU.MassTheory.exchangeDet_pow_two_le_four`. This measurement does not solve
that; it is the first time the framework's own binding path has been able to
*exhibit* it end to end.

## Still not established

- **Two atoms.** he3, he4, li6, li7 did not complete: the container's worker was
  restarted mid-run (SIGKILL) and the process died. They are not reported.
- **No witness regenerated.** `hadron-knot-table.witness.json` untouched, and it
  should stay that way while the sign is wrong — recording these as a witness
  would publish them.
- **No cause identified.** "Extensive term missing" is a reading of two points,
  consistent with prior work; it is not a measurement of the mechanism.

# Copilot review (#6427) — finding accepted, fix relocated

Copilot flagged, correctly, that the kernel path makes `tr_run` and
`s['log_norm']` `mpmath.mpf`, so `unified_iterative_correction` and
`binding_energy` return `mpf`, and `hadron_knot_table.py:204`'s
`round(B, 4)` then hits
`TypeError: Object of type mpf is not JSON serializable`. **Verified by
reproduction**, not taken on trust.

**Its suggested fix — coerce at the kernel boundary — is wrong for this repo**,
and the fix is applied one level out instead: the casts are at the *public
returns* of `unified_iterative_correction` and `binding_energy`, which is where
the float contract has always been. Coercing at the kernel would discard the
50-dps the kernel exists to carry, through the entire accumulation, which is
exactly what the NO-FLOAT64 discipline forbids.

**And it costs nothing measurable either way**, which is worth stating because
it identifies a real defect Copilot did not flag: `log_cur = s['log_norm'] +
math.log(abs(tr_run))` at line 1604 **already narrows to float64 inside the
loop** — `math.log` returns a Python float whatever it is handed. Measured:
`math.log(mpf(3)/7)` → `-0.8472978603872037` (float) against `mp.log` →
`-0.847297860387203613710107506521`. So this accumulator has been
float64-limited at its log step all along, upstream of any cast. That is a
**pre-existing precision defect**, neither introduced nor repaired here.

---

# Third atom: the prediction is very nearly a CONSTANT

| atom | A | Z | B_pred (MeV) | AME2020 | sign | \|pred\|/AME | secs |
|---|---|---|---|---|---|---|---|
| deuterium | 2 | 1 | -7.271102125 | +2.224566 | **WRONG** | 3.269 | 942 |
| tritium | 3 | 1 | -7.742121347 | +8.481796 | **WRONG** | 0.913 | 1568 |
| he3 | 3 | 2 | -7.456199506 | +7.718041 | **WRONG** | 0.966 | 1496 |

**This is the finding, and it is sharper than the sign.**

```
prediction spread :  -7.742 .. -7.271   =   6.3 % of its mean
AME2020    spread :  +2.225 .. +8.482   = 101.9 % of its mean
```

Across A = 2 → 3, and across two *different* A = 3 nuclei, the framework's
binding accumulator moves **6 %** while the experimental binding it is meant to
reproduce moves **102 %**. The output is essentially **a constant ≈ −7.5 MeV**,
almost independent of both A and Z.

That reframes the defect. A wrong sign suggests a convention; a wrong *magnitude*
suggests a missing coefficient. **A near-constant where the target varies by 4×
suggests the accumulator is not computing a binding energy at all** — it is
producing something whose nuclear dependence is almost entirely absent.

## The mirror pair, stated carefully

⁴³H (tritium, Z = 1) and ³He (Z = 2) are mirror nuclei, and the comparison is
worth making precisely rather than loosely:

```
raw differences (tritium − he3):   prediction  -0.2859      AME  +0.7638
```

Those have **opposite signs as raw differences** — I initially mislabelled them
as agreeing, and that was wrong. The defensible statement is about **ordering
under the global sign flip**: `|pred(tritium)| > |pred(he3)|` and
`B(tritium) > B(he3)`, so the framework does rank the mirror pair the way
experiment does, at **0.37×** the experimental splitting.

That is a genuine but weak positive: some Z-dependence exists and points the
right way. It does not survive as evidence for the sign being a mere convention,
because the near-constancy above is not something a sign flip repairs.

## Consistency with the standing open problem

AGENTS.md records the arc's one real open problem as a **"separate,
super-pairwise additive extensive object"** that six Δ_λ closure ansätze all
failed to produce, with the pairwise cap proved
(`QOU.MassTheory.exchangeDet_pow_two_le_four`). A binding accumulator that is
**flat in A** is exactly what that description predicts you would see if the
extensive term is absent — the intensive part is present and the extensive part
is not.

**This measurement does not prove that reading.** Three points, two of them at
the same A. It is consistent with the standing account, which is a different and
much weaker claim than confirming it.

## Still running / still not established

- **he4 (A = 4) is the real test** and was still running when this was written.
  AME `B(⁴He) = 28.296` — more than 3× the A = 3 values — so if the prediction
  stays near −7.5 there, flatness is established across a 13× range of the
  target. li6/li7 after that.
- **No witness regenerated.** `hadron-knot-table.witness.json` untouched.
- **No mechanism identified.** Flatness is a symptom; where the A-dependence is
  lost in the accumulator is not measured.

---

# ⁴He settles it: the accumulator carries no extensive term

| atom | A | Z | B_pred (MeV) | AME2020 | sign | \|pred\|/AME | secs |
|---|---|---|---|---|---|---|---|
| deuterium | 2 | 1 | -7.271102125 | +2.224566 | **WRONG** | 3.269 | 942 |
| tritium | 3 | 1 | -7.742121347 | +8.481796 | **WRONG** | 0.913 | 1568 |
| he3 | 3 | 2 | -7.456199506 | +7.718041 | **WRONG** | 0.966 | 1496 |
| he4 | 4 | 2 | -6.828594293 | +28.295662 | **WRONG** | 0.241 | 2425 |

```
prediction :  -7.742 .. -6.829     spread  12.5 % of its mean
AME2020    :  +2.225 .. +28.296    range   12.7x
```

**The target varies by 12.7×. The prediction varies by 12.5 %.**

And ⁴He is the sharpest point available: it has the **lowest** \|prediction\|
(6.829) at the **highest** experimental binding (28.296). The prediction does not
merely fail to grow with A — at the one place where binding triples, it *falls*.

```
correlation  |pred| vs AME :  r = -0.731
correlation  |pred| vs A   :  r = -0.471
```

Both **negative**, on four points. Read cautiously — four points, and two share
an A — but the sign of the trend is the opposite of what a binding energy must do.

## What this establishes

The framework's binding accumulator, computed correctly for the first time,
produces **a number near −7.3 MeV that is essentially independent of the
nucleus**. It is not a mis-scaled binding energy and not a sign-flipped one:

- A **sign flip** does not help — `+7.27, +7.74, +7.46, +6.83` against
  `2.22, 8.48, 7.72, 28.30` is wrong at both ends and still flat.
- A **constant rescale** does not help — the ratios run 3.269, 0.913, 0.966,
  0.241, spanning 13.6×.

**Nothing multiplicative repairs a quantity that is flat where the target is
extensive.** What is missing has to be *additive and extensive in A* — which is
precisely the object AGENTS.md records as the arc's one real open problem: a
"separate, super-pairwise additive extensive object" that six Δ_λ closure
ansätze failed to produce, with the pairwise cap proved
(`QOU.MassTheory.exchangeDet_pow_two_le_four`).

**This is the first direct measurement of that gap.** Prior work inferred it from
failed closures; this exhibits it, end to end, in the framework's own binding
path, at four nuclei.

## What it does NOT establish

- **Not a mechanism.** *Where* the A-dependence is lost inside the accumulator is
  not measured. Flatness is the symptom.
- **Not a refutation of the framework.** It is a measurement of one computational
  path, which until this week could not run at all. The intensive part may well
  be right; what is absent is absent.
- **Four points, two at A = 3.** li6/li7 were not reached — cost per atom is
  942, 1568, 1496, 2425 s and grows.
- **No witness regenerated.** `hadron-knot-table.witness.json` is untouched and
  should stay so: recording a wrong-signed, nucleus-independent number as a
  witness would publish it.

---

# A numerical target for the extensive term (`qou-brng`) — weak, and labelled so

The four points give the missing term directly. Writing
`B_true = B_pred + E(A)`:

| atom | A | E = AME − B_pred | E/A | E/C(A,2) | E/(A−1) |
|---|---|---|---|---|---|
| deuterium | 2 | 9.496 | 4.748 | 9.496 | 9.496 |
| tritium | 3 | 16.224 | 5.408 | **5.408** | 8.112 |
| he3 | 3 | 15.174 | 5.058 | **5.058** | 7.587 |
| he4 | 4 | 35.124 | 8.781 | **5.854** | 11.708 |

Across all four, every normalisation is poor (E/A 67 %, E/C(A,2) 69 %,
E/(A−1) 45 %). **Excluding the deuteron** — which this corpus already treats as
special (owner ruling 2026-08-29: its knot is the canonical braid closure,
`Vol = 0`, and the Gram/SDP route is a scope-(a) negative) — one normalisation
separates:

```
E / C(A,2)   5.408, 5.058, 5.854     spread 14.6 %
E / A        5.408, 5.058, 8.781     spread 58.0 %
E / (A−1)    8.112, 7.587, 11.708    spread 45.1 %
```

So for A ≥ 3 the required term is roughly **`E ≈ 5.4 MeV × C(A,2)`** — it scales
like the **all-pairs count**.

## How much this is worth, stated honestly

**Not much on its own, and the arithmetic says why.**

- Excluding the deuteron leaves **two distinct A values** (3 and 4). Many forms
  fit two points.
- The **within-A scatter is the noise floor**: tritium and ³He are both A = 3 and
  their `E/C(A,2)` differ by **6.7 %**. The cross-A spread is 14.6 %, i.e. only
  **2.2×** that floor.

A trend 2.2× above the noise, over two distinct abscissae, is a **target, not a
determination**. It says where to aim; it does not say the term is pairwise.

## And it sits in tension with a proved result — deliberately flagged

AGENTS.md records the missing object as **"super-pairwise"**, with the pairwise
cap **proved** (`QOU.MassTheory.exchangeDet_pow_two_le_four`, `ρ_A ≤ C(A,2)`).
An `E` that scales *as* `C(A,2)` is pairwise-shaped, which is not obviously
consistent with that framing.

Three readings, none settled here:

1. The apparent `C(A,2)` scaling is an artefact of two points and 6.7 % noise.
2. `E` genuinely saturates the proved cap rather than exceeding it — `≤ C(A,2)`
   permits `∝ C(A,2)`.
3. The A ≥ 5 behaviour, where `C(A,2)` and any super-pairwise form diverge
   sharply, distinguishes them — and is exactly what was not reached.

**⁶Li (A = 6) is the discriminating measurement**, and it is now merely
expensive rather than impossible: per-atom cost ran 942, 1568, 1496, 2425 s for
A = 2,3,3,4. That is the concrete next step this arc leaves behind.

---

# ⁶Li attempt 1: killed, not completed — recorded as a negative

The A = 6 run **did not produce a value**. The process is gone and `li6` never
reached the incremental save, so it was killed mid-computation rather than
erroring — the script's `except BaseException` handler would have recorded an
exception, and it recorded nothing.

**Cause undetermined, and I am not going to guess it.**

- **Not a timeout expiry.** The cap was 20000 s and the run was alive at 4839 s
  when last observed.
- **OOM cannot be confirmed or excluded** — `dmesg` is unavailable in this
  container. Post-mortem memory is 13.9 GB free of 16 GB, which says nothing
  about the peak.
- A **container worker restart** killed an earlier run in this same session
  (SIGKILL, mid-`binding_energy`), so that is a live possibility.

What *is* established: he3 and he4 survived because the runner writes each result
the moment it lands. That design choice is the only reason this session has four
points rather than one — the earlier run lost everything in flight when it died.

**Retried, ⁶Li alone**, with a 300 s heartbeat so a future kill is
distinguishable from a hang, and a 25000 s cap.

## The discriminator is still open

Nothing here changes the four-point result or the extracted target. It means the
one measurement that separates the three readings —

1. the `C(A,2)` scaling is a two-point artefact,
2. `E` saturates the proved pairwise cap (`≤ C(A,2)` permits `∝ C(A,2)`),
3. super-pairwise growth, which only shows above A ≈ 5

— **has not been made.** ⁶Li has `C(A,2) = 15` against ⁴He's 6, which is why it
is the point that matters and also why it is the expensive one.

## ⁶Li attempt 2: killed again — and the heartbeat says *killed*, not hung

Attempt 2 (⁶Li alone, 300 s heartbeat, 25000 s cap) also produced no value:

```
6Li Z=3 N=3 A=6  C(A,2)=15
  ... alive at 326s
[process gone, no result file]
```

**The heartbeat did the job it was added for.** One beat fired at 326 s and the
process was gone with the beat still current — so this is a **kill**, not a hang.
Attempt 1 could not distinguish those.

It also died *earlier* than attempt 1: within ~600 s of starting ⁶Li, against
~900 s+ before. Two kills, both early in A = 6, cause still undetermined
(`dmesg` unavailable).

**Stopping the identical retries**, per the rule set before attempt 2: two kills
is a signal to change approach, not to try a third time.

### Approach changed: split the terms

`binding_energy` is three terms. Term 2 (`sdp_cross_channel_contribution`) is
**measured 0.0** at these A. Terms 1 and 3 are independently expensive and each
runs the same kernel. Splitting them:

- halves the exposure window per process, and
- makes a kill cost **one term**, not the atom —

which is the same reasoning that saved he3 and he4 when the earlier combined run
died. Term 1 (`unified_iterative_correction`) is launched alone; it carries the
sign and most of the magnitude. Term 3 follows separately.

This is not a workaround for a wrong answer — it is scheduling. If A = 6 is
simply beyond this container, that is worth knowing plainly too, and the split
will show which term is the one that cannot finish.

## ⁶Li attempt 3 (split, term 1 alone): killed too — recording the ceiling

```
6Li term 1 (unified_iterative_correction) Z=3 N=3
  ... alive at 124s
[process gone, no result file]
```

Three attempts, and **each died earlier than the last**:

| attempt | scope | last heartbeat / sighting | outcome |
|---|---|---|---|
| 1 | full `binding_energy` | alive ~900 s into ⁶Li | killed |
| 2 | ⁶Li alone | `alive at 326s` | killed |
| 3 | term 1 alone | `alive at 124s` | killed |

**Stopping here**, per the rule set before attempt 2. A fourth identical attempt
is not an experiment.

### The honest ceiling

**The corrected binding path reaches A = 4 in this container, and not A = 6.**

```
A=2  deuterium   942 s     A=3  he3    1496 s
A=3  tritium    1568 s     A=4  he4    2425 s
A=6  ⁶Li        3 kills, no value
```

A = 2…4 completed **reliably**, including across long idle periods, so background
compute is not categorically reclaimed here — the failures are specific to A = 6.

**Cause undetermined**, and I am not inventing one. `dmesg` is unavailable, so
OOM is neither confirmed nor excluded. The "each attempt dies earlier" pattern is
recorded as an observation, not explained: it is *consistent* with a resource
ceiling that tightens as the container fills, and equally consistent with several
other things. Noting a pattern is not diagnosing it.

### What stays open, and it is the important one

The discriminator between

- **`E` saturates the proved pairwise cap** (`≤ C(A,2)` permits `∝ C(A,2)`), and
- **super-pairwise growth**, per AGENTS.md's framing,

**is not measured, and is recorded as open rather than guessed.** The four points
in hand cannot separate them: they span two distinct A values above the deuteron,
with a 6.7 % within-A noise floor against a 14.6 % cross-A spread.

### What would settle it

Two routes, neither attempted here:

1. **A = 6 on a machine that will hold the process.** Nothing about the
   computation is known to be wrong — it is scheduling, and the per-atom trend
   (942 → 2425 s for A = 2 → 4) does not obviously forbid A = 6.
2. **A = 4 and A = 6 both at a reduced `k_exact`.** Truncated values are not
   comparable to the k = 11 points above, but they *are* comparable to each
   other, so the ratio `E(6)/E(4)` could discriminate at a fraction of the cost.
   This is a genuinely different measurement, not a cheaper version of the same
   one, and would need its own gate.

---

# 🛑 RETRACTION: the `E ≈ 5.4 × C(A,2)` target is mostly an artefact of my own arithmetic

The section above extracted `E = AME − B_pred` and reported that, excluding the
deuteron, `E/C(A,2)` is near-constant at 5.408 / 5.058 / 5.854 — offering it to
`qou-brng` as a numerical target. **That framing is wrong and is withdrawn.**

**Why.** `B_pred` is nearly constant at ≈ −7.3 and small compared with AME at
A ≥ 3, so `E ≈ AME + 7.3`. Measured:

| nucleus | A | AME | E = AME − B_pred | E/C(A,2) | (AME+7.3)/C(A,2) |
|---|---|---|---|---|---|
| ²H | 2 | 2.225 | 9.496 | 9.496 | 9.525 |
| ³H | 3 | 8.482 | 16.224 | 5.408 | 5.261 |
| ³He | 3 | 7.718 | 15.174 | 5.058 | 5.006 |
| ⁴He | 4 | 28.296 | 35.124 | 5.854 | 5.933 |

The last two columns agree to **~1 %**. So `E/C(A,2)` is very nearly a statement
about **AME2020's own light-nucleus systematics**, with the framework
contributing an almost constant offset.

**And AME alone does not support the scaling:**

```
nucleus   A     AME    AME/A   AME/C(A,2)
2H        2    2.225   1.112      2.225
3H        3    8.482   2.827      2.827
4He       4   28.296   7.074      4.716
6Li       6   31.994   5.332      2.133
7Li       7   39.245   5.606      1.869
12C      12   92.162   7.680      1.396
```

`AME/C(A,2)` **peaks at ⁴He and falls steeply**. The apparent constancy I
reported lives entirely in the A = 3…4 window, and **⁶Li breaks it on
experimental grounds alone** — `(31.994 + 7.3)/15 ≈ 2.62`, less than half of 5.4.

## What this does to the ⁶Li plan

**It removes the discriminator as I posed it.** Running ⁶Li would not separate
"E saturates the pairwise cap" from "super-pairwise growth", because `E` is
dominated by experiment, not by the framework. I could have predicted the answer
from AME2020 without running anything — which is the tell that the quantity was
not measuring what I said it measured.

The generosity of the framing was the error: I normalised a *residual against
experiment* and read its shape as a property of the *theory*.

## The measurement that IS informative

**`B_pred` itself at A = 6**, not `E`.

The four-point claim that carries weight is that the framework's own output is
flat: −7.271, −7.742, −7.456, −6.829 across a 12.7× range of the target. The
question ⁶Li actually answers is **whether `B_pred` stays ≈ −7.3 at A = 6**, where
`C(A,2)` is 15 and any genuine many-body term would have to show. That is a
statement about the framework alone, with no experimental normalisation in it,
and it is worth the compute.

`qou-brng` should take from this arc **the flatness of `B_pred`**, and **not**
the withdrawn `5.4 × C(A,2)` figure.

---

# Both routes run — and the flatness holds at A = 6

The retraction above left one question standing: **does `B_pred` stay flat at
A = 6?** That is a statement about the framework alone, with no experimental
normalisation in it, so it is the one worth the compute.

The answer comes from the **paired** comparison — ⁴He and ⁶Li at the *same*
truncation, which is comparable even when the truncated values are not
comparable to the k = 11 points:

| `k_exact` | ⁴He (A=4) | ⁶Li (A=6) | ratio ⁶Li/⁴He |
|---|---|---|---|
| 5 | -0.375110164 | -0.539212954 | 1.4375 |
| 6 | -0.838749076 | -0.992757495 | 1.1836 |
| 7 | -1.515118319 | -1.414063111 | 0.9333 |
| 8 | -2.153722974 | -2.183158129 | 1.0137 |
| 9 | -3.711581534 | -3.404340982 | 0.9172 |
| 10 | -5.669659692 | -5.467686217 | 0.9644 |

```
A          :  4  ->  6      (1.5x)
C(A,2)     :  6  ->  15     (2.5x)
accumulator:  ratio 0.917 .. 1.014 at k >= 7,  mean 0.957
```

**⁶Li returns essentially the same number as ⁴He**, at six independent
truncations, while `C(A,2)` grows 2.5× and `A` grows 1.5×. The low-k ratios
(1.44, 1.18) are the truncation still settling; from k = 7 the four values sit
within ±5 % of unity with no trend.

So the flatness established at A = 2…4 **extends to A = 6**. The accumulator's
output is not merely slowly-varying over the light isotopes — it is close to
independent of the nucleus across a range where every candidate many-body term
grows substantially.

## The retraction produced a better experiment, not a cheaper one

I had framed the reduced-`k_exact` route as a cheap substitute for the real
measurement. It is the opposite:

- it isolates **the framework's own A-dependence**, with no AME normalisation to
  contaminate it — which is exactly what the withdrawn `E/C(A,2)` framing failed
  to do;
- it is cheap enough to run at **six truncations** rather than one, so the
  result is a trend rather than a point;
- and it sidesteps the A = 6 kill ceiling entirely — the paired run at k ≤ 10
  finished in **minutes**, where three full-`binding_energy` attempts at A = 6
  had all been killed.

The three ⁶Li kills were real, and the ceiling on the *full* path at A = 6
stands. What changed is that the full path was never the measurement this
question needed.

## Still open

- **k = 11** (production truncation) for the pair was still running. The k = 7…10
  trend is flat and the k = 11 pair is expected to follow, but that is an
  expectation, not a measurement.
- **Why** the accumulator is nucleus-independent remains unmeasured. This
  localises the symptom to A = 6; it does not identify where the A-dependence is
  lost.
- **`E`-based scalings are withdrawn** — see the retraction above. `qou-brng`
  should take the flatness of `B_pred`, not any `C(A,2)` figure.
