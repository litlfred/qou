# The Z=1–20 mass table was not produced by the published formula

**Date:** 2026-08-25 · **Bean:** `qou-1jw9` · **Status:** measurement, settles an open item

## What was open

[The recovery audit](2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md)
established that `atom-mass-complete-wedderburn.witness.json` exists (added
2026-04-10 in `1359fe23ac` under `folio-assistant/computations/`, out of tree
since the miga split), that it reproduces the published table, and that its
third coefficient departs from the published one by 14.2 %:

| | value | origin |
|:---|:---|:---|
| producer `beta3` | `0.0499` | no stated derivation |
| published `h_A²` | `0.043707282…` | `h_A = q − q⁻¹` at `q₀ = 1.10998`, the block's own definition |

Under the owner's no-fitting ruling neither may be adjusted to meet the other,
so the corpus was left with an authoring question phrased as a disjunction:
*either the published `h_A²` is wrong, or the table was never the formula's
output.*

**The two branches are not symmetric, and the disjunction is decidable.** Both
coefficients multiply the **same** recorded per-row `Φ₃`, and the witness records
`Φ₁`, `Φ₂`, `Φ₃`, `M_pred` and `M_obs` for all 20 rows. So the published formula
can be evaluated on the producer's own invariants with every other input held
fixed. Nothing is fitted, reconstructed or guessed:
[`computations/audits/wedderburn_beta3_vs_hA2_discrimination.py`](../../computations/audits/wedderburn_beta3_vs_hA2_discrimination.py),
mpmath at 50 dps throughout.

## Result 1 — the witness is the table's producer

Evaluating the formula with the recorded parameters reproduces every published
`M_pred` to a **maximum residual of 0.00049 MeV** — i.e. exactly, at the three
decimals the table quotes. The table has a real producer and that producer is
this artifact.

## Result 2 — the published coefficient reproduces none of the published values

Substituting `beta3 → h_A²(q₀)` and holding everything else fixed:

| rows reproduced at the published 3-dp precision | |
|:---|:---|
| with `beta3 = 0.0499` | **20 / 20** |
| with published `h_A² = 0.0437073` | **0 / 20** |

The shift is monotone in `Φ₃` and runs from `−0.024 MeV` (¹H) to `+1.205 MeV`
(⁴⁰Ar). The published summary figures are `beta3`'s fingerprint too: mean
`0.0740 %` and max `0.1917 %` under `beta3`, against `0.0746 %` and `0.1909 %`
under `h_A²` — the block quotes 0.074 % and 0.1917 %.

**So the first branch of the disjunction is confirmed: the published table is
not the published formula's output.**

## Result 3 — this is *not* evidence that `h_A²` is wrong

The two coefficients are indistinguishable on accuracy against AME2020:

| | mean \|Δ\|/m | max \|Δ\|/m |
|:---|:---|:---|
| `beta3 = 0.0499` | 0.0740 % | 0.1917 % |
| `h_A² = 0.0437073` | 0.0746 % | **0.1909 %** |

`h_A²` is marginally *better* on the worst row and marginally worse on the mean.
A 14.2 % change in the third coefficient moves the table by less than 1 part in
30 000, because `Φ₃` enters ~50× more weakly than `Φ₁`. **The table therefore
carries no evidence about which coefficient is correct**, and the second branch
of the disjunction is neither supported nor refuted by it. Scope (a): a statement
about these coefficients on these recorded invariants.

## Result 4 — `beta3` is not `h_A²` mis-anchored or mis-typed

Three candidate innocent explanations, all foreclosed:

- **A different `q₀` anchor.** `h_A²` at the proton pin is `0.0437062085` and at
  the muon pin `0.0437062182` — flat to 13 digits, and neither is `0.0499`. No
  anchor choice produces it. The `q` that *would* satisfy `h_A²(q) = 0.0499` is
  `q = 1.117910`, which is 0.71 % off `q₀` and is not any documented pin.
- **A mistyped exponent.** The ratio `beta3 / h_A² = 1.1416862` is `q₀^1.26992`
  — not an integer or half-integer power, so no `q^k` slip yields it.
- **A rounding artifact.** `alpha` carries 6 significant figures and `beta2`
  seven — computed precision. `beta3` carries **three**, the precision of a
  typed constant.

## Convention-independence

Worth stating explicitly, because `main` is mid-migration from the Markov
convention C to D and a future reader will ask which frame this was measured in:
**neither**. The comparison holds `Φ₁`, `Φ₂` and `Φ₃` fixed at the producer's
recorded values and varies only the third coefficient, so whatever convention
those invariants were computed under is common to both sides and cancels exactly.
The probe contains no Markov parameter at all — its only occurrence of the word
"convention" is a comment naming the `q₀` anchor. The 20/20-versus-0/20 result is
therefore unaffected by the convention-D cascade, and re-deriving the table under
D would not change it.

## What this settles, and what it leaves to the author

**Settled.** The published block states *"All quantities are derived from `q₀`
and `m_e`"* and *"The formula has zero fitted parameters."* The table beneath it
was computed with a third coefficient that is not derived from `q₀` and `m_e`
and whose value matches no quantity in the corpus. The claim and the table
disagree, and the disagreement is in the table's provenance, not in the formula.

**Not settled, and deliberately not acted on.** Which way to repair it is an
authoring call, and both repairs are cheap:

1. **Regenerate the table under the published `h_A²`** — parameter-free, costs
   0.0006 pp of mean accuracy, *improves* the worst row, and changes all 20
   quoted values. The replacement numbers are computed in the probe's `results`
   block and need no new derivation.
2. **Keep the numbers and document `beta3`** — but then "zero fitted parameters"
   cannot stand as written, since `beta3` has no derivation.

Under the no-fitting ruling (1) is the option that keeps the block's own claim
true; but changing twenty published values is the author's call, not the agent's,
and no such change is made here.

## Correction carried with this document

[`mass-table-z1-20.md`](../../content/quantum-observable-universe/mass-theory/mass-table-z1-20.md)
stated the rows are *"not currently reproducible from a committed witness"*. The
first half is now false — they are reproducible, to 0.0005 MeV, from a witness at
a named commit — while the operative point (it is **not** committed, and it does
**not** compute the published formula) is stronger than the sentence claimed. The
block is corrected accordingly.
