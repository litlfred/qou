# OV-cone axiom audit — two of my claims were overclaims (correction)

**Date:** 2026-08-07 · **Tier:** audit / correction · **Method:** per-declaration `#print axioms`
(proof-term dependency, not file-level `sorry` counting).

## What I claimed, and what is actually true

I merged #4649 with the title *"discharge RSKBurnsideHolds — the documented 'not yet a theorem'
target"* and #4652 as *"ν_n closed form now unconditional"*. I attached an "inherited-input caveat"
to both, saying the results hold "at the strength of the OV Wedderburn result" and that I had not
audited that cone. **I have now audited it, and the caveat was not strong enough: the operative
claims are false.**

`#print axioms` on the actual proof terms:

| declaration | axioms | verdict |
|---|---|---|
| `OVTopAssembly.sum_numSYT_sq_eq_factorial` | propext, **sorryAx**, Classical.choice, Quot.sound | **not proved** |
| `RSKBurnsideDischarge.rskBurnsideHolds` | propext, **sorryAx**, Classical.choice, Quot.sound | **not proved** |
| `PlancherelNormalisation.sum_sytDim_sq_eq_factorial` | propext, **sorryAx**, Classical.choice, Quot.sound | **not proved** |
| `PlancherelNormalisation.nuV_top_closed_form_unconditional` | propext, **sorryAx**, Classical.choice, Quot.sound | **not proved** |
| `YoungDiagramTailFirstInstance.nuV_top_nonneg` | propext, Classical.choice, Quot.sound | **genuinely sorry-free** |
| `SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux` | propext, Classical.choice, Quot.sound | **genuinely sorry-free** |

So the corpus' original label on `RSKBurnsideHolds` — *"not yet a theorem"* — was **substantively
correct**, and my discharge of it did not change that. It moved the dependency, not the burden:
`sum_numSYT_sq_eq_factorial` itself rests on `sorryAx`, so everything reindexed from it does too.

## Why file-level counting was not enough, and why it was still the tell

**A first count of this cone, reported earlier the same day, was wrong** — the regex matched the
phrase "sorry-free" in docstrings, inflating the figures roughly fifty-fold and inventing a `sorry`
in `RegularRepBlockTrace` that does not exist. Corrected count (comments and docstrings stripped,
`sorry` not followed by `-`):

| module | real `sorry` |
|---|---|
| `QOU.BraidKnot.Specht` | 2 |
| `QOU.BraidKnot.SpechtClassification` | 2 |
| `QOU.BraidKnot.JucysMurphy` | 1 |
| `QOU.BraidKnot.SnWedderburnPartitionBridge` | 1 |
| `QOU.BraidKnot.StandardYoungTableau` | 1 (`numSYT_mul_hookProduct`, the known HLF gap) |

**7 sorries across 5 of the 23 cone modules** — not 377 across 16. `RegularRepBlockTrace` and
`OVTopAssembly` contain **no** real `sorry`; the modules named earlier as the largest offenders
(`SpechtStandardBasisCore` 107, `SpechtDominanceCore` 50, `JucysMurphy` 42) carry 0, 0 and 1.

This materially changes the strategic read: closing the RSK identity is plausibly **a handful of
named lemmas**, not a multi-session march through a sorry swamp. It also reinforces the process
point below in both directions — a bad screen can overstate difficulty as easily as understate it,
and only the axiom check is load-bearing.

## What survives

The (TAIL) first instance's *content* is intact and genuinely sorry-free:

* **`nuV_top_nonneg` — `0 ≤ ν_n` for `3 ≤ k ≤ 20`** is clean. This was the point of the (TAIL)
  first instance, and it never needed the RSK normalisation (the sign follows from the numerator's
  closed form plus `tiltNorm > 0`).
* **`numSYT_eq_numStandardYoungTableaux`** — the SYT-encoding bridge — is clean, and remains a real
  contribution: it is what makes the two encodings interchangeable, independent of whether the RSK
  identity is proved.
* The upstream chain feeding `nuV_top_nonneg` (carrier lemma, hook-shape data, moment sums, the
  bracket collapse, the `mean_zero` discharge) is unaffected.

What does **not** survive: `RSKBurnsideHolds` as "discharged", and the *exact* `ν_n` closed form as
"unconditional".

## Required follow-ups

1. **Relabel.** `RSKBurnsideDischarge` and `PlancherelNormalisation` docstrings must say the results
   inherit `sorryAx` from `OVTopAssembly.sum_numSYT_sq_eq_factorial`. `nuV_top_closed_form_unconditional`
   should be renamed — "unconditional" is true only of its *hypothesis list*, not its proof term.
2. **Do not cite** either as settled. In particular `RSKBurnsideTarget`'s "not yet a theorem"
   docstring should stay as-is.
3. **The real gap** is upstream, and is now enumerated: the 7 sorries in the five modules tabled
   above. Closing the RSK identity means closing those, not reindexing around them. Do **not** use
   the retracted 377/16 figures for triage.
4. **Process fix:** run `#print axioms` on any keystone before claiming a discharge
   (`scripts/lean-axiom-guard.py`). File-level `grep sorry` is a screen, not a verdict; the proof
   term is the verdict. And when screening, strip comments first — an unstripped count of this cone
   was off by ~50x.
