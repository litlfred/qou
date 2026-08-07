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

The import cone of `OVTopAssembly` contains 23 QOU modules, **16 of which contain `sorry`** (377
occurrences; largest: `SpechtStandardBasisCore` 107, `SpechtDominanceCore` 50, `JucysMurphy` 42,
`SpechtTriangularCore` 35, `IdentityIContentDecomposition` 33, `OVTopAssembly` itself 28,
`RegularRepBlockTrace` 1 — the last being the module `sum_numSYT_sq_eq_factorial` specialises).

File-level counts are not decisive on their own (a file may carry sorries in declarations a given
result never touches), which is why the axiom check was needed. But with `RegularRepBlockTrace`
carrying a `sorry` on the very lemma being specialised, the count was a strong signal that should
have prompted the axiom check **before** the merges, not after.

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
3. **The real gap** is upstream: `RegularRepBlockTrace`'s sorry (and the Specht-core cone). Closing
   the RSK identity means closing those, not reindexing around them.
4. **Process fix:** run `#print axioms` on any keystone before claiming a discharge. File-level
   `grep sorry` is a screen, not a verdict; the proof term is the verdict.
