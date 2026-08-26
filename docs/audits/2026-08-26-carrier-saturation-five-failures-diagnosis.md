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

## 3. Root cause: the two sides of the product are on different conventions

`S(A) = Σ_λ p_λ · |Δθ_λ|` draws its two factors from separate witness families:

| side | supplies | source family | `convention` | computed |
|---|---|---|---|---|
| `p_λ = y_λ·dim_λ` | the weights | `chi-*-at-q0-50dps` | **`colour-weighted-averaged-crossing`** | **2026-08-10** |
| `\|Δθ_λ\|` | the phases | `binding-reeb-phase-decomposition` → `atom-chi-rust-*` | **absent** | 2026-07-06 → 08-19/23 |

The weights were migrated to colour-weighted crossings on **2026-08-10** — one day
after the owner ruling making `bring_color_weighted` canonical (AGENTS.md R3). The
phase side was not, and **declares no convention at all**, so the pairing cannot
be verified from the record. That is the `qou-cds4` surface ("six live non-comparison
files still off-canon") reaching a consumer.

The expectations (audit table, 2026-07-13) predate the migration. So does the 9/9.

**Why the error grows with A** — 1.0618 (A=2), 1.1673 (A=4), 1.3509 (A=6): block
count runs 11 → 77 → 385, and a reweighting of `p_λ` compounds across more blocks.

## 4. A second, independent defect — real but NOT the cause

`binding-reeb-phase-decomposition.witness.json` (2026-07-06) is stale against its
own inputs, which were regenerated 2026-08-19 and 2026-08-23. Re-running it moves
**574 fields**.

**The movement is ~1e-7 to 1e-8 relative — four orders of magnitude too small to
explain a 17–35 % discrepancy.** Recorded because it is a genuine staleness that
should be drained, and because the temptation to stop at the first plausible cause
is exactly what produces a wrong diagnosis. Import-cone staleness was the
hypothesis; measuring it refuted it as the explanation while confirming it as a
defect.

The re-run was **not committed**: this container degrades the environment block
(drops `scipy`, `numpy` 2.5.0 → 2.4.6, python 3.13.12 → 3.11.15), and committing a
weaker provenance record to fix a 1e-7 drift is the wrong trade.

## 5. What would settle it

Re-run the probe with **pre-migration** `y_λ` (or regenerate the phase side under
the colour-weighted convention) and check whether 9/9 returns. If it does, the
expectations are simply pre-migration and must be re-derived under the canonical
convention — **re-derived, not re-baselined**: the audit table's numbers would then
be *wrong under the canonical convention*, and updating the literals without
recomputing the audit would be laundering.

## 6. What must NOT be done

- **Do not widen any tolerance.** Every threshold here is doing its job: it caught
  a real convention regression that the probe's own prose reports as a success.
- **Do not edit the expected literals to match.** Three of them are the same fact;
  all three descend from a table computed under a superseded convention.
- **Do not "fix" `carrier_flat_band_all_A` by relaxing 0.30.** That assertion is
  over-claiming against the theory it cites; the honest repair is to state what is
  proved (boundedness, which passes) and drop or re-scope the flatness claim.
