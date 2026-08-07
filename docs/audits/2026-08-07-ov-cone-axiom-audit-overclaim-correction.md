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

**Two hand-rolled `grep sorry` counts of this cone gave two different answers (377/16, then 7/5), so
neither is used here.** The first matched the phrase "sorry-free" in docstrings, inflating figures
~50x and inventing a `sorry` in `RegularRepBlockTrace` that does not exist. The table below is
instead the **compiler's own** `declaration uses 'sorry'` output — the only authoritative screen.

| declaration | module:line | what it is |
|---|---|---|
| `sn_isotypic_specht_split` | `SnWedderburnPartitionBridge`:234 | **the Wedderburn split** — what `OVTopAssembly` actually consumes |
| `numSYT_mul_hookProduct` | `StandardYoungTableau`:149 | the hook-length formula (the corpus' named "brick-1" target) |
| `specht_finrank_eq_numSYT` | `Specht`:309 | `dim S^μ = #SYT` (Sagan 2.5.2; needs the standard-polytabloid basis) |
| `specht_isSimple` | `Specht`:320 | Specht modules are irreducible |
| `spechtIso_imp_dom_both` | `SpechtClassification`:449 | iso ⇒ mutual dominance |
| `specht_exhausts_irreducibles` | `SpechtClassification`:485 | Specht modules exhaust the irreducibles |

| `seminormalVector_base_exists` | `JucysMurphy`:840 | seminormal base vector; sibling intent recorded (#3799 — reuse Hoefsmit) |

**7 confirmed sorry-carrying declarations.** `JucysMurphy` was measured after building its dep chain
(`SytAdjacentSwap`, `SytEntryMono`, `SytRowSuperstandard`, `SytMathlibBridge`, `Mathlib.PermInversion`):
it carries **exactly one** sorry, at line 840. A regex had suggested two there — `rep_mem_spechtSubmodule`
is in fact **complete**, so the "one bounded, startable item" named in the first version of this audit
was already proved and needs no work. That is a fourth grep miss; the compiler was right again. `RegularRepBlockTrace` and
`OVTopAssembly` carry **none**. `Specht.polytabloid_mem_specht`, which a regex flagged, is
**complete** — the compiler does not warn on it.

**Honest read of difficulty.** This is neither the 377-sorry swamp of the first count nor "a handful
of easy lemmas" of the second: it is the standard Specht-module development — basis, simplicity,
classification, Wedderburn split. Textbook-known, genuinely multi-session in Lean. The one bounded,
startable item is `JucysMurphy.rep_mem_spechtSubmodule` if it is real (Sₙ-stability of the Specht
submodule: `σ·polytabloid t = polytabloid (σ·t)`, so `Submodule.span_le` on generators);
`seminormalVector_base_exists` has sibling intent recorded (#3799 — reuse Hoefsmit, don't duplicate).

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
3. **The real gap** is upstream and is enumerated above (6 confirmed + `JucysMurphy` pending).
   Closing the RSK identity means closing those, not reindexing around them. Do **not** triage from
   either retracted grep count (377/16 or 7/5).
4. **Process fix:** run `#print axioms` on any keystone before claiming a discharge
   (`scripts/lean-axiom-guard.py`). File-level `grep sorry` is a screen, not a verdict; the proof
   term is the verdict. And do not screen with hand-rolled `grep sorry` at all — two attempts here
   disagreed with each other and both disagreed with the compiler. Use `lean`'s own
   `declaration uses 'sorry'` warnings.
