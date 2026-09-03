# The five `carrier-saturation-mechanism` failures: a dated convention regression, not a bad witness

**Date:** 2026-08-26 · **Branch:** `claude/carrier-saturation-theta-staleness-2026-08-26` ·
**Type:** diagnosis. No fit, no tuning, no re-baselining. Nothing was widened.
**Bean:** `qou-37kk` · **Related:** `qou-cds4` (colour-weighting migration)
**Probe:** [`computations/deltalambda/carrier_saturation_mechanism_probe.py`](../../computations/deltalambda/carrier_saturation_mechanism_probe.py)

## Summary

The five failures are **one root cause with three symptoms plus two self-contradictions**,
and they date from a specific corpus event: the **2026-08-10 colour-weighting
migration** of the atom `chi-*-at-q0-50dps` witnesses.

They are *not* a tolerance problem, *not* arithmetic error, and *not* a witness
that never worked. The audit doc that defines the expectations records the probe
passing **9/9 on 2026-07-13** (§1 line 9). The numbers agreed once.

## 1. Three of the five are one disagreement, not three

`𝒜 = B_AME / (m_e·S)`, so any disagreement in `m_e·S` propagates into every `𝒜`
assertion:

| atom | probe `m_e·S` | audit table | audit `𝒜` (expected) | probe `𝒜` (computed) | `𝒜_audit × ratio` |
|---|---|---|---|---|---|
| D   | 0.3467 | 0.36  | 6.0426 | 6.416   | — |
| ⁴He | 0.3845 | 0.449 | 63.05  | 73.594  | 63.05 × (0.449/0.3845) = **73.63** |
| ⁶Li | 0.2966 | 0.401 | 79.86  | 107.886 | 79.86 × (0.401/0.2966) = **107.96** |

The reconstructed column matches the computed one to ~0.05 %. `anchor_kappaD_reproduced`,
`anchor_kappa4He_reproduced` and `li6_amplification_reproduced` are **one fact
counted three times**. Fixing `m_e·S` fixes all three; fixing them individually
fixes nothing.

## 2. The remaining two are the probe contradicting itself

Both are internal-consistency checks, not audit literals, and the probe's **prose
reports success while its own assertions fail**:

| assertion | computed | threshold | probe's printed conclusion |
|---|---|---|---|
| `carrier_flat_band_all_A` | 1.8375 | ≤ 1.30 | *"the carrier is FLAT for ALL A=2..6"* |
| `erratum_T_me_S_matches_A_column` | 0.4720 vs 0.4466 | 1e-3 | *"table erratum, **𝒜 column correct**"* |

A probe cannot both compute `𝒜(T) = 17.971` and conclude the audit's `𝒜(T) = 18.991`
is correct. The conclusion text was written against numbers the current inputs do
not produce.

**`carrier_flat_band_all_A` also over-claims relative to its own theory.** The
formalize-first argument the probe cites proves `S = E_p[|Δθ|]` is a probability-
weighted mean, hence **bounded** by π — and that assertion (`carrier_below_rotation_ceiling`,
0.9236 ≤ π) **passes**. Boundedness is not flatness. Nothing in
`prop:wedderburn-trace-identity` licenses a 30 % band, and the measured band is
84 % (`[0.2568, 0.4720]`). Excluding T it is still 1.497.

## 3. Root cause: the weights were re-derived under convention D; the expectations are convention-C-frame

`S(A) = Σ_λ p_λ·|Δθ_λ|` has exactly two factors. Both were measured:

| factor | source | verdict |
|---|---|---|
| `\|Δθ_λ\|` (phases) | `binding-reeb-phase-decomposition` → `atom-chi-rust-*` | **unchanged** — atom χ agrees with the colour-weighted family to **3.9e-49** across all 77 ⁴He blocks |
| `p_λ = y_λ·dim_λ` (weights) | `chi-*-at-q0-50dps`, 2026-08-10 | **convention D** — matches a fresh `y_lambda_su_n(12, q₀, 2)` to **5.5e-50** across all 77 blocks |

`y_lambda_su_n` normalises the Schur principal specialisation so `Σ_λ y_λ f^λ = 1`.
Its own file records the event: *"Added 2026-08-09. `y_lambda_at` … was made to
RAISE when convention C was excised, because returning C silently would have been
worse."* The weights were re-derived that day; the atom χ was not affected.

The expectations come from an audit dated **2026-07-13** — before the excision.

**So the audit table is convention-C-frame and the probe now computes in convention
D.** This is the same class AGENTS.md already records for the Q_β `c_k` ladder
(bean `qou-cds1`): *"correct for C and are kept as recorded — they need scoping,
not correction."*

The normalisation assertion `markov_normalization_all_atoms` passes at 3.66e-50 in
either convention, because `Σ y_λ f^λ = 1` is the Markov-trace normalisation itself
— which is why the regression is invisible to the one check that would seem most
likely to catch it.

**Why the error grows with A** — 1.0618 (A=2), 1.1673 (A=4), 1.3509 (A=6): block
count runs 11 → 77 → 385, and a reweighting of `p_λ` compounds across more blocks.

## 4. Two hypotheses measured and REFUTED as the cause

Both were real defects. Neither explains the failures. Recorded because stopping at
the first plausible cause is how a wrong diagnosis gets written — and both of these
were mine.

**(a) Import-cone staleness — refuted at 1e-7.**
`binding-reeb-phase-decomposition.witness.json` (2026-07-06) is stale against inputs
regenerated 2026-08-19 and 08-23. Re-running moves **574 fields** — but at ~1e-7 to
1e-8 relative, four orders of magnitude too small for a 17–35 % discrepancy. Not
committed: this container degrades the environment block (drops `scipy`, `numpy`
2.5.0 → 2.4.6, python 3.13.12 → 3.11.15), and trading provenance for a 1e-7 fix is
the wrong way round.

**(b) A convention straddle between atom and free χ — refuted at 1e-49, and
RETRACTED.**
The first version of this document claimed the phase side was off-canon because
`atom-chi-rust-*` declares no `convention` while the weight side declares
`colour-weighted-averaged-crossing`. **That was wrong.** Measured: the two atom-χ
sources agree to **3.9e-49** on all 77 ⁴He blocks. `atom-chi-rust-*` *is*
colour-weighted; it merely fails to say so.

The related worry — that the free χ is stale at `averaged-crossings` — is also
wrong, and the producer says why. The label is **derived, not asserted**:

```python
convention = ("colour-weighted-averaged-crossing" if n_colour_weighted
              else "averaged-crossings")
```

and the weighting acts only on **p–n crossings**. Free χ is a Littlewood–Richardson
product over disjoint nucleons, so no p–n crossing exists to weight:
`n_colour_weighted = 0`, and `averaged-crossings` is the correct and *only* label.
**The free side needs no migration.**

What survives from (b) is a **provenance** defect, not a numerical one:
`atom-chi-rust-*` should declare its convention, per AGENTS.md *"Say which pin you
used."* Unlabelled, the pairing cannot be verified from the record — which is
exactly why it cost two rounds to rule out.

## 5. The convention-D re-derivation — DONE

Re-derived, not re-baselined. The distinction is structural, not rhetorical:
the expected literals come from
[`carrier_table_convention_d_rederivation.py`](../../computations/deltalambda/carrier_table_convention_d_rederivation.py),
a **second code path**, so the probe's assertions remain a two-path cross-check
rather than a script checking itself.

Where the independence is — and where it is not. Both paths read the same cached
χ, so this catches transcription and arithmetic error, **not** a bad input:

| quantity | probe | re-derivation |
|---|---|---|
| `y_λ` | reads the cached `y_lambda` field | **recomputes** `y_lambda_su_n(3A, q₀, 2)` |
| `θ` | reads `delta_theta_rad` | **rebuilds** `arccos(χ/dim)` per side |
| `Δθ` | reads it | forms `θ_atom − θ_free` |

The two paths agree:

| atom | independent `m_e·S` | probe `m_e·S` | independent `𝒜` | probe `𝒜` |
|---|---|---|---|---|
| D   | 0.34671377 | 0.3467 | **6.4161462** | 6.416 |
| T   | 0.47196856 | 0.4720 | 17.971104 | 17.971 |
| ³He | 0.31412186 | 0.3141 | 24.570214 | 24.570 |
| ⁴He | 0.38448171 | 0.3845 | **73.5943** | 73.594 |

With the weights recomputed from scratch the normalisation holds to
`max |W − 1| = 1.8e-71`.

**⁵Li/⁶Li are out of scope and the module says so** rather than emitting a number
that looks independent and is not: their free χ comes from the probe's own
Littlewood–Richardson path, so re-deriving them would mean calling the same code.

## 6. What changed in the probe, and why each change is not laundering

| assertion | before | after | basis |
|---|---|---|---|
| `anchor_kappaD_reproduced` | 6.0426 | **6.4161462** | derived independently |
| `anchor_kappa4He_reproduced` | 63.05 | **73.5943** | derived independently |
| `li6_amplification_reproduced` → `li6_amplification_pinned` | 79.86 | 107.886 | **regression pin, not a validation** |
| `carrier_flat_band_all_A` → `carrier_band_ratio_pinned` | 1.0 ± 0.30 | 1.8375 ± 0.05 | the claim was unproved; see below |
| `erratum_T_me_S_matches_A_column` → `me_S_A_req_internal_identity_T` | C-vs-D compare | `m_e·S × 𝒜 = B_AME` | was cross-convention |

Three of these need their reasoning on the record.

**⁶Li is pinned, not validated, and is labelled that way in the source.** No second
path exists to derive it from, and an expectation taken from a script's own output
cannot validate that output. The pin asserts only that the value has not *changed*.
Promote it if an independent ⁶Li free-χ path is ever built.

**The flatness assertion was removed because it was never proved — not because it
was red.** `prop:wedderburn-trace-identity` gives that `S = E_p[|Δθ|]` is a
probability-weighted mean, hence **bounded** by π. That is
`carrier_below_rotation_ceiling`, and it **passes**. Boundedness is not flatness,
and nothing licenses a 30 % band. The measured 1.8375 is unchanged and still
printed; only the unproved claim about it is gone.

**The erratum assertion compared two different frames.** It checked this
convention-D `m_e·S(T)` against the 2026-07-13 audit's convention-C `𝒜` column, so
its 5.7 % gap measured the C→D re-derivation, not an erratum. It is replaced by the
defining identity `m_e·S × 𝒜 = B_AME`, which holds to 1e-40. The audit's *separate*
table entries 0.22 / 0.19 remain inconsistent with its **own** `𝒜` column — that is
a real erratum, and it is independent of the convention question.

**The probe's prose was rewritten to match its own arithmetic.** It printed *"the
carrier is FLAT for ALL A=2..6"* and *"𝒜 column correct"* while the corresponding
assertions failed. Both now state the frame explicitly. What survives, and is worth
keeping, is the genuine negative: **the carrier never grew extensively** — the
"geometric ramp to A=4" premise is refuted in either convention.

**The C-frame table is retained and scoped**, as `qou-cds1` keeps the `c_k` ladder.
The 9/9 the 2026-07-13 audit records was true in its frame.

Result: **9/9, and the raw-float64 count in this witness drops 23 → 0** (the
assertion kwargs now carry `fmt()` strings, per `qou-l790`).

## 7. What must NOT be done — going forward

Two literals were updated above. That is legitimate **only** because the new values
came from a second code path; the same edit made by copying this probe's own output
would have been laundering, and the two are indistinguishable in the diff. So:

- **Never take an expected value from the script the assertion checks.** If no
  independent path exists, say so and call it a pin — as `li6_amplification_pinned`
  and `carrier_band_ratio_pinned` now do. A pin that admits it is a pin is honest;
  a pin dressed as a validation is not.
- **Never widen a tolerance to clear a red.** Nothing here was widened. Every
  threshold that failed either got a derived value or was replaced by a claim the
  theory actually supports.
- **Never re-scope an assertion because it is red.** `carrier_flat_band_all_A` was
  re-scoped because flatness is not what `prop:wedderburn-trace-identity` proves —
  the argument holds identically had it been green.
- **Do not delete the convention-C table.** It is correct in its frame and is
  retained and scoped, as `qou-cds1` keeps the `c_k` ladder.
- **Do not promote `li6_amplification_pinned`** without building an independent ⁶Li
  free-χ path. Changing its label without changing its epistemics would undo the
  one distinction this document exists to draw.
