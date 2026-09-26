---
# qou-epxx
title: 'raw-float64 drain: two float() casts on full-precision inputs — q0_proton in bn_minus_bp_brane_tower_parity_probe (~44 digits lost) and CAL-1 m_e + AME_B in atom_vhyp_bar_trace_test (~2e-17, in the arithmetic not just the witness)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-26T14:28:50Z
updated_at: 2026-09-26T14:31:31Z
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
