# The c_k slope tension, and two extractions of the same c_k that disagree

**Date:** 2026-08-10
**Beans:** `qou-0etg` (the slope tension), `qou-ai9u` (the kernel survey)
**Probe:** [`computations/qbeta/ck_qgevrey_slope_probe.py`](../../computations/qbeta/ck_qgevrey_slope_probe.py)
→ `ck-qgevrey-slope.witness.json`

## 1. The slope tension — settled

[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
asserts two things about the same `c_k`:

- **(a)** they satisfy a **constant-kernel** linear recursion
  `c_{k+1} = Σ_j a_j(q₀)·c_{k+1−j}` with `a_j(q₀) ∈ ℚ(q₀)`, fixed in `k`;
- **(b)** they obey the **Hahn–Exton q-Bessel second-order q-difference
  equation**.

Constant-kernel solutions are geometric — q-Gevrey order `s = 0`. A genuine
second-order q-difference equation generically has `s > 0`, i.e.
`|c_k| ∼ C^k q^{s k²/2}`, **super-geometric**. Different growth classes, so at
most one reading can describe the growth.

`QOU.Mathlib.QGevreyOrder.IsQGevreyOrder` supplies the test:
`s = lim_k 2·log_q|c_k| / k²`. Measured on both committed datasets:

| dataset | `s` estimates, k = 2…10 | turning over? |
|---|---|---|
| A closed-form | 0, 1.48, 0.15, 0.17, 0.59, 0.81, 0.25, 0.43, 0.10 | yes |
| B SDP | 0.08, 1.5, 1.12, 3.91, 5.25, 5.72, **5.81**, 5.72, 5.54 | yes, from k=8 |

**Verdict: (a) is right; (b) does not describe these `c_k`'s growth.** Neither
dataset carries a positive slope. B's apparent `s ≈ 5.8` is the finite-`k`
artifact of purely geometric growth — `2·log_q(A)/k → 0` — and is already
turning over by `k = 8`. Scope-(a): a statement about the measured growth of
these sequences, not a refutation of the q-Bessel identification as a
*fibre-level structural* claim, which this probe does not test.

## 2. Where the truncation constant `2.07` comes from — it is derived

AGENTS.md frames the ladder `Q_β = Q_base·∏(1 + c_k u^k)` as convergent with
truncation order `N ≥ log₁₀(1/ε)/2.07 − 1`. The `2.07` has been carried as a
bare constant. It is

```
log₁₀(1/u) = 2.0697013928582786        u = 0.008517234550156142
```

So the rule is **derived, not fitted** — the ladder term at rung `k` is
`O(u^k)` and `log₁₀(1/u)` digits are gained per rung. That closes the
`qou-ai9u` target for this rule, **conditional on `c_k = O(1)`**.

## 3. The serious finding: two extractions of the same `c_k` disagree

The two committed datasets are **not different objects**. Dataset B's own
description: *"EXTENDED c_k extraction at rungs k=8, 9, 10 via SDP-T_β.
Continues `qbeta_decay_sdp_full_ck.py` beyond k=7."* Same ladder, second method.

| k | A `closed_form_c_k_at_q0` | B `c_k_extracted_50dps` | ratio |
|---|---|---|---|
| 2 | −1.0 | −1.0172 | 1.02 |
| 3 | −2.0 | −2.0216 | 1.01 |
| 4 | −1.1331 | −2.5379 | 2.2 |
| 5 | −1.2527 | −164.93 | **132** |
| 10 | 1.7058 | −3.652×10¹² | **2×10¹²** |

They agree to ~2 % at k = 2, 3 and then part company completely.

### Why B is the suspect one

B's ratio `c_{k+1}/c_k` locks to **117.4** from k = 6, and `1/u = 117.409`. So
`c_k ∼ C·u^{−k}`, and therefore

```
|c_k u^k|  =  7.34e-09   for k = 6, 7, 8, 9, 10   — FLAT
```

whereas A's ladder terms decay `7.2e-05 → 3.4e-21`.

Flat ladder terms are the signature of an extractor **solving for `c_k` to
absorb a fixed residual at each order**: the `u^{−k}` is exactly what cancels
the `u^k`, so every rung contributes the same `7.34e-09` and the ladder stops
converging. Under B the convergence premise behind §2's truncation rule fails
outright.

### DIAGNOSED AND FIXED (same day, bean `qou-8ofm`)

Opened `qbeta_decay_sdp_extended_ck.py`. `R` **is** correctly divided by each
rung's factor — that was not the bug. The bug is that the script emits
`c_k := (R_k − 1)/u^k` **unconditionally**, including after `R_k − 1` has
stopped dropping. Instrumented, the residual reads:

| k | \|R_k − 1\| | drop vs prev | resolving? |
|---|---|---|---|
| 2 | 7.379e-05 | — | yes |
| 3 | 1.249e-06 | 59.1× | yes |
| 4 | 1.336e-08 | 93.5× | yes |
| 5 | 7.393e-09 | **1.81×** | no |
| 6 | 7.336e-09 | 1.01× | no |
| 7–10 | 7.337e-09 | 1.00× | no |

A contributing rung should drop the residual by ~`1/u ≈ 117×`. After k = 4 it
drops by 1×: that is the model's **accuracy floor**, not a rung contribution.
Dividing a fixed floor by an ever-smaller `u^k` is precisely what manufactures
`c_k ∼ floor/u^k` — hence ratio exactly `1/u` and flat `|c_k u^k| = 7.34e-09`.

**Only `c_2, c_3, c_4` are determined by this extraction. `c_5 … c_10` were
artifacts of the floor.**

The script's own docstring already said the leverage was gone — *"the extracted
values are essentially noise floor / numerically ambiguous"*, *"not as a
precision claim at q₀"* — but it emitted the numbers anyway and the witness
recorded them where they read as data. Prose caveats do not stop downstream
consumption; the emission has to.

**Fix applied.** Per-rung residual tracking with a floor detector
(`MIN_RESIDUAL_DROP = 10×`, far more permissive than the ~117× a real rung
gives, so only an unambiguous stall is rejected). Unresolved rungs now emit
`null` in `c_k_extracted_50dps` / `_float`; the raw quotients are preserved
under `c_k_unresolved_raw_quotient` so nothing is hidden; and a new
`c_k_resolution` block records the residual, the drop, and the verdict per
rung. The printed table flags each unresolved rung inline.

### The k=4 conflict is moot — and the first guard was off by one

Chasing the surviving k = 4 disagreement produced two corrections, one to this
audit's own fix.

**(i) `R` carries exactly one degree of freedom.** At 70 dps,
`R₀ − 1 = −7.379e-05`, and

```
c₂ := (R₀ − 1)/u²  =  −1.01721732856672495132406625322
R₀ / (1 + c₂u²) − 1  =  0.0        exactly
```

One rung consumes `R` completely; a self-consistent chain then extracts
`c_k = 0` for every `k ≥ 3`. `R(q₀)` is a **single scalar**, so **at most one
`c_k` can ever be determined by this procedure.** What the later rungs do is
not measurement: the canonical `c_k` are *imposed*, and the extraction reports
the leftover. Those impositions are still genuine *tests* — a wrong canonical
leaves the residual high — but a test is not an extraction.

**(ii) The guard credited each rung with its predecessor's drop.** `residual[k]`
is the residual *before* rung `k` is applied, so the reduction achieved **by**
rung `k` is `residual[k]/residual[k+1]`, not `residual[k−1]/residual[k]`.
Attributed correctly:

| canonical imposed | residual before → after | drop |
|---|---|---|
| `c₂ = −1` | 7.379e-05 → 1.249e-06 | **59.1×** |
| `c₃ = −2` | 1.249e-06 → 1.336e-08 | **93.5×** |
| `c₄ = −2b⁴ = −1.133` | 1.336e-08 → 7.393e-09 | **1.81×** |
| `c₅` | → 7.336e-09 | 1.01× |
| `c₆, c₇` | → 7.337e-09 | 1.00× |

So **only `c₂` and `c₃` are supported by the data.** `c₄` buys 1.81× against a
~117× expectation — it is already inside the floor. The corrected witness emits
values for `c₂, c₃` and `null` for `c₄ … c₁₀` (`last_resolved_rung: 3`,
`n_unresolved: 7`).

**Therefore the k=4 conflict needs no adjudication.** `−1.133` (closed form)
versus `−2.538` (extraction) is a disagreement between a prediction and a
leftover; neither is a measurement of `c₄`, because this procedure cannot
measure `c₄`.

**What survives.** `c₂ = −1` and `c₃ = −2` are tested and pass convincingly
against `R(q₀)`. Everything above is unconstrained by this datum and must come
from the Habiro/q-difference structure — which is exactly what
`prop:q-beta-c-k-recursion-from-habiro-q-difference` says, and why it insists
`R` *"cannot be fixed by fitting the `Bₙ`"*. The extraction was doing the thing
that proposition forbids.

### Do not "fix" this by renaming

The obvious tidy-up — call B's sequence `cl_k` and declare a notation clash —
would be wrong. There is no notational discrepancy: both **are** the Q_β ladder
coefficients, by B's own description. Renaming would launder a numerical
contradiction into a naming convention and let both live in the corpus
unreconciled. One of the two extractions is wrong (or they are anchored
differently, see below) and that has to be settled on the merits.

### Secondary defect: neither witness records its q₀ anchor

Neither `qbeta-decay-sdp-extended-ck.witness.json` nor
`qbeta-closed-form-wiring-n4-to-n10.witness.json` records a `q0Anchor` or a q₀
value anywhere. So an anchor mismatch can be neither blamed nor excluded from
the witnesses alone — and AGENTS.md §"q₀ anchor convention" rule 4 requires it:
*"Say which pin you used. Any new witness must record its q₀ so a later reader
can tell which layer it belongs to."* A sibling probe
(`qbeta-ck-recursion-kernel-constraint-probe`) does record `q0Anchor: muon`,
so the field is in use elsewhere. Note an anchor difference could not plausibly
produce a 10¹² divergence by itself.

## What is NOT claimed

Nothing here says which extraction is correct, and nothing here bears on
whether the ladder is the right object. §1 settles only which growth class the
committed numbers exhibit; §3 identifies a contradiction and its likelier
suspect without opening the extractor.
