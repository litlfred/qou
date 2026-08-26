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

## 5. What resolving it means

The convention question is now measured, so the remaining step is a **content
decision, not a compute one**, and it belongs to the author.

Under convention D the probe's current output *is* the answer. The audit table's
numbers are not wrong — they are **correct for convention C**, and AGENTS.md's
standing treatment of exactly this situation is that such numbers *"need scoping,
not correction"*. Resolving the five failures therefore means:

1. **Re-derive the audit table under convention D** and update the three expected
   literals *from that re-derivation* — never by copying the probe's output into the
   assertion. The two are numerically the same edit and epistemically opposite: one
   is a derivation, the other is laundering.
2. **Retain the C-frame numbers, scoped.** Mark the 2026-07-13 table
   convention-C-frame and keep it, as the `c_k` ladder is kept (`qou-cds1`). The
   9/9 it records was true in its frame.
3. **Re-scope `carrier_flat_band_all_A` independently.** This is not a convention
   artefact and does not go away under D — see §6.

Two smaller items, both independent of the above:

4. **Label `atom-chi-rust-*`'s convention.** A provenance fix; it cost two rounds
   of this diagnosis to rule out a straddle that was never there.
5. **Drain the 1e-7 θ staleness** in a container that does not degrade the
   environment block.

What is *not* available: a direct C-vs-D re-run. Convention C was excised on
2026-08-09 and `y_lambda_at` was deliberately made to **raise** rather than return
C silently, so the C-era weights cannot be recomputed without resurrecting removed
code. The diagnosis above therefore rests on measurement plus elimination — χ and
`|Δθ|` shown unchanged to 1e-49 and 1e-7, `y_λ` shown to be D to 5e-50, and the
expectations dated before the excision — not on a side-by-side reproduction. That
is the honest limit of what this branch establishes.

## 6. What must NOT be done

- **Do not widen any tolerance.** Every threshold here is doing its job: it caught
  a real convention regression that the probe's own prose reports as a success.
- **Do not edit the expected literals to match.** Three of them are the same fact;
  all three descend from a table computed under a superseded convention.
- **Do not "fix" `carrier_flat_band_all_A` by relaxing 0.30.** That assertion is
  over-claiming against the theory it cites; the honest repair is to state what is
  proved (boundedness, which passes) and drop or re-scope the flatness claim.
