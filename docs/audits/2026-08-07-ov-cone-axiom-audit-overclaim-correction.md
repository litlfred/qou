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


---

## Update, 2026-08-15 — six of seven closed; one survivor

Re-measured after main advanced ~2800 commits. Siblings closed almost the whole list:

| declaration | 2026-08-07 | now |
|---|---|---|
| `specht_exhausts_irreducibles` | sorry | **closed** (`c1d45fd4c5`) |
| `spechtIso_imp_dom_both` | sorry | **closed** |
| `specht_finrank_eq_numSYT` | sorry | **closed** |
| `numSYT_mul_hookProduct` | sorry | **closed** (moved to `HookProductHLF`) |
| `seminormalVector_base_exists` | sorry | **closed** (`1553638166`, moved to `SeminormalBaseExists`) |
| `specht_isSimple` | sorry | **closed** (moved to `SpechtIrreducible`; file has 0 real sorries) |
| **`sn_isotypic_specht_split`** | sorry | **still open — the sole survivor** |

### A fifth grep false positive, from the same root cause

An intermediate version of this update recorded `specht_isSimple` as *still open*. It is not. The
check windowed 45 lines from the declaration and matched the **next** declaration's docstring, which
contains the phrase "fully `sorry`-free"; `--` comments were stripped, `/- -/` blocks were not. This
is the fifth time in this line of work that a hand-rolled `sorry` screen has produced a wrong answer,
every time from comment text. The rule in §4 of "Required follow-ups" stands and should be read as
absolute: **screen with `lean`'s own `declaration uses 'sorry'` warnings, never with grep.**

### What the survivor needs

The sibling result `WedderburnSn.sn_wedderburnArtin_alg` is sorry-free but **abstract** — Mathlib's
`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing` gives
`k[S_n] ≃ₐ[k] ∀ i : Fin N, Matrix (Fin (𝔫 i)) (𝔇 i)` with `N`, `𝔇`, `𝔫` all existentially bound. Four
identifications separate it from `sn_isotypic_specht_split`:

1. index by `PartitionIndex n` rather than `Fin N` (the labelling bijection);
2. `𝔇 i = R` — rationality; Mathlib collapses the division rings only over an algebraically closed base;
3. `𝔫 i = finrank R (SpechtSubmodule i.diagram)`;
4. the isotypic alignment `e C₂ = fun i => contentSqSum λᵢ • 1`.

This is the Okounkov–Vershik identification, not packaging. **What changed in this window is that its
prerequisites now exist**: Specht modules are simple, exhaust the irreducibles, and are pairwise
non-isomorphic across distinct partitions — so the labelling bijection is derivable rather than
assumed. Item 4 is the tractable entry (`JucysMurphy.centralC2_acts_by_contentSqSum` already exists,
making it Schur-per-isotypic-component); items 1–3 are the hard core.

### Item 2 (rationality) is now closed — and it was not the hard part

**Update, same day, PR #5139.** `SpechtAbsolutelyIrreducible.simple_end_scalar`: over any
characteristic-zero field, **no simple `k[S_n]`-module admits a non-scalar equivariant
endomorphism**. Sorry-free (`#print axioms` = `propext, Classical.choice, Quot.sound`). A block's
`𝔇 i` *is* the commutant of the corresponding simple, so this is item 2 in module-theoretic form.

I had this filed as the item needing a descent from ℚ. It needs no descent and no character theory —
the corpus already carried both halves, in the file that proves the submodule theorem:
`kapL_mem_line` (`κ_t` maps all of `M^μ` into the line `k·e_t`) and `kapL_polytabloid`
(`κ_t e_t = |C_t|·e_t`). Equivariance moves `θ` past `κ_t`, characteristic zero divides by `|C_t|`,
and the polytabloids' single `S_n`-orbit spreads the scalar over a spanning set. The upgrade from
Specht modules to arbitrary simples is a transport along `specht_exhausts_irreducibles` — one of the
six gaps a sibling closed in this same nine-day window, which is what made the general form reachable
immediately rather than as a follow-up.

The generalisable lesson is the same one this audit already records twice: **measure before scoping**.
"Mathlib gives the collapse only over an algebraically closed base" is true and was the reason to
expect difficulty, but it says nothing about what *this corpus* carries. Items 1 and 3 — the labelling
bijection and the block-size identification — remain the hard core, and `sn_isotypic_specht_split`
stays open. The `sorryAx` labels on `RSKBurnsideHolds` and the Plancherel normalisation are
unchanged.

Consequence for the two `sorryAx`-carrying keystones (`RSKBurnsideHolds`, the Plancherel
normalisation): unchanged. `OVTopAssembly` consumes exactly this survivor, so they still inherit
`sorryAx`. Their labels stay as recorded.
