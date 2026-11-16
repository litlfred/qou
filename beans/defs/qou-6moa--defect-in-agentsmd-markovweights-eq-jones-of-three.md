---
# qou-6moa
title: 'DEFECT in AGENTS.md: markovWeights_eq_jones_of_threeRow_eq_zero is cited for its own HYPOTHESIS'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-26T14:15:29Z
updated_at: 2026-11-16T18:38:00Z
parent: qou-rtxm
---

## The mis-citation

AGENTS.md (§"q₀ anchor convention", R1 block) states that `y_(1³) = 0` holds *by
construction* under convention D, **citing
`markovWeights_eq_jones_of_threeRow_eq_zero`**. That declaration runs the other
way. Literal signature,
`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`,
context `variable {R : Type*} [CommRing R] [IsDomain R]`:

```lean
theorem markovWeights_eq_jones_of_threeRow_eq_zero (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hTL : y₁₃ = 0)          -- ← HYPOTHESIS
    (hfaith : y₂₁ ≠ 0) :     -- ← and faithfulness on the 2-row block is another
    (q + qi) ^ 2 * y₂₁ = 1 ∧ y₃ = 1 - 2 * y₂₁ ∧ z * (q + qi) = q ^ 2
```

So `y₁₃ = 0` is the **hypothesis** and **convention D is the conclusion** — the
implication the document wants is the exact reverse. And `hfaith` is
load-bearing, not decorative: the same file's `markovWeights_degenerate_root`
proves that dropping it makes the conclusion **false** (the `y = (1,0,0)` trivial
character at `z = q`), not merely unprovable. A declaration that *assumes* a form
of faithfulness cannot be evidence about faithfulness.

## The correct citations, both sorry-free on `main`

- `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser`
  (`TemperleyLiebTower.lean:368`) — `z·(q²+1) = q³` plus the three moment
  equations gives `y₁₃ = 0`. This is the forward direction.
- `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`
- and for general `n` on the actual weight,
  `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`
  (`OcneanuWeight.lean:142`), unconditional over any field with `q²+1 ≠ 0` —
  which is what PR #7458 uses.

## Why this is not fixed in #7458

It is a citation swap inside a STRICT document, and the standing rule is to ask
the owner before changing things unless the change increases precision or is
corpus-derived. It *is* corpus-derived (the Lean signature decides it and a
reviewer can check it by opening one file), so it qualifies — but a STRICT
document is where a wrong edit costs the most, so it was raised in the PR body
with the signature quoted rather than swept. **Blast radius**: the report that
found it counted ~35 corpus sites citing this declaration; whether any of them
repeat the reversal is NOT measured and is the first thing to do here.

Found by the corpus-grep for PR #7458 (bean `qou-r7kp`), 2026-09-26.


## MEASURED 2026-09-26 — it is a CLASS, 14 reversed across 9 files

Population: **81 line hits / 56 files** excluding `__pycache__`. (My first figure
of 82/57 counted the stale `computations/__pycache__/wedderburn_jones_markov.cpython-311.pyc`.
Both are right about different populations — say which.) The bean's own original
"~35" was low by ~60 %.

**Tally: REVERSED 14 · HFAITH-DROPPED 2 · UNCLEAR 2 · CORRECT 49 · NEUTRAL 14.**

**The corpus is overwhelmingly RIGHT about this** — 49 correct against 14
reversed, and four sites explicitly warn against exactly this reversal
(`docs/audits/2026-08-16-two-row-cap-proved-and-deltalambda-magnitude.md:73`,
`MassTheory/TwoRowCapDerived.lean:256`, `FibreDimensionForcesTL.lean:165`,
`qbeta_cap_is_jointly_determined_probe.py:9`). **Nothing reader-facing
(`content/**/*.md`) is affected, and no validator's verdict changes.**

### FIXED (this bean's PR #7459)

| site | status |
|---|---|
| `AGENTS.md` §q₀-anchor PSD-reading block | fixed + 🛑 note |
| `QOU/Mass/AltCharShiftMultiset.lean:381` | fixed + 🛑 note; `lean`-direct RC=0 |

Those two plus `.beans/qou-99qc:2523` were **the same sentence in three places**,
backed by one probe.

### STILL REVERSED — 12 hits / 7 files, NOT swept (needs owner scope)

Spelling A, *"that vanishing IS convention D"*:
- `computations/qbeta/qbeta_ecat_block_cost_vector_probe.py:46,259` → witness
- `computations/qbeta/qbeta-ecat-block-cost-vector.witness.json:19` (`checks[].source`)
- `computations/qbeta/qbeta_reading3_does_not_constrain_the_budget_probe.py:35,224` → witness
  — **this probe is the SOURCE of the AGENTS.md paragraph**
- `computations/qbeta/qbeta-reading3-does-not-constrain-the-budget.witness.json:12`

Spelling B, asserted as an **iff** and used in the ⟸ direction (wrong in *both*
halves — ⟸ is a different lemma, ⟹ is false without `hfaith`):
- `computations/deltalambda/wlambda_qbeta_d_ladder_attack_options.py:31,110` → witness
- `computations/deltalambda/qbeta-d-ladder-attack-options.witness.json:24` (`checks[].detail`)
- `docs/audits/2026-08-29-convention-d-qbeta-front-adversarial-audit.md:31-32`
  — **also carries two stale line numbers**: cites `MarkovTraceTLUniqueness.lean:97`
  and `:147`; the declarations are at **119** and **169**.

Spelling C, D ⟹ TL as an explicit inference chain:
- `docs/audits/2026-08-21-cds1-d-frame-ladder-state-synthesis.md:45` — reasons
  *from* `z_D·[2]_q = q²` *to* the TL weight vector. The cleanest instance of the
  error, and it is a **state synthesis** (written to be read as the current
  position, not a dated snapshot).

Beans (append, never rewrite — `scripts/bean-append-merge.py` at merge time):
`.beans/qou-99qc:2523`, `.beans/qou-cds1:4972`. **Correction notes appended
2026-09-26.**

### 🛑 The claim SURVIVES a citation-keyed sweep

Three further files assert *"that vanishing IS convention D"* with **no lemma
named at all** — invisible to any grep on the identifier:
`qbeta_knot_operator_ilp_ohara_cost_probe.py:270`,
`qbeta_ecat_lp_radical_pairing_probe.py:30,207` (the last → witness). Found with
`grep -rn "vanishing IS convention D\|vanishing \*is\* convention D\|two-row truncation that defines convention D"`.
**Grep the phrase, not the identifier** — detector-blindness class, worth a row in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`.

### The `qou-3nva` audit-doc precedent does NOT cleanly apply

`qou-3nva:2771` leaves dated audit docs as *"historical records of that
analysis"*. That protects a **superseded number** — *"we measured 4.66e6 that
day"* is a true statement about a past measurement. *"Lemma X proves P"* is not:
the signature has not changed, so it was wrong on the day it was written and
stays wrong. Recommendation (agent judgement): fix both audit docs in the 🛑-note
style, preserving the original sentence.

### The replacement lemmas differ in TYPECLASS — do not swap the wrong one in

| lemma | typeclass | scope |
|---|---|---|
| `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (`:142`) | `[Field R]`, one hypothesis `q²+1 ≠ 0` | general `n`, the actual Ocneanu weight |
| `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu` (`:179`) | `[CommRing R] [IsDomain R]`, division-free | `n = 3`, **same variable frame** as the defective lemma |
| `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` (`:368`) | **`[Field R] [LinearOrder R] [IsStrictOrderedRing R]`** (`section PinningOrdered`) | `n = 3`, **archimedean only** |

The third is the wrong citation at any §7c generic-`R` site. Verified by reading
the `section`/`variable` structure, not taken from a report.

**`threeRow_eq_zero_of_jones_ocneanu`'s own docstring already states the
distinction this bean is about**, verbatim: *"The converse direction of
`markovWeights_eq_jones_of_threeRow_eq_zero`: there, `y_(1³) = 0` implies
`z·[2] = q²`; here, `z·[2] = q²` implies `y_(1³) = 0`."* The sentence existed one
file over the whole time.

### Machine consumers: none

Three witness `source`/`detail` fields carry it; the witness validators key on
structure (`scriptHash`, `q0Anchor`, LP-dual fields), never on prose. The registry
validator prints `forcing_note[:120]` only inside an R6 error message, and within
that window the **correct** direction is what surfaces. `trace-convention-audit.ts`
keys on decimal literals and cannot see a lemma name.

### HFAITH-DROPPED, 2 mild fields, both in `trace-convention-registry.json`

`:199` and `:362` say `markovWeights_…` forces D *"uniquely"* without the word
"faithful" — and "uniquely" is exactly what `hfaith` buys. The **file** covers
itself: `:173`, 26 lines above, spells out both roots (`z = q` degenerate and
`z = z_D`) and is **the corpus's single best citation of this lemma**. Left as-is.

## Resolution (2026-11-16, PR [`litlfred/qou#8151`](https://github.com/litlfred/qou/pull/8151), commit `11d9d9a0016ff7aacd751e96586ecbf5f1217753`)

- Added `threeRow_eq_zero_of_conventionD` directly in `QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean` proving the converse direction `D ⟹ TL` (`z * (q + qi) = q ^ 2 ⟹ y₁₃ = 0` when `[2]_q ≠ 0` and `[3]_q = [2]_q² − 1 ≠ 0`, sorry-free via `linear_combination`) side-by-side with `markovWeights_eq_jones_of_threeRow_eq_zero` (`TL + faithful ⟹ D`).
- Updated `docs/coordination/trace-convention-registry.json` (`:199` and `:362`) to explicitly state `FibreDimensionForcesTL.twoDimFibre_pins_h3_weights` and the faithfulness requirement (`hfaith : y_(2,1) != 0` on `TL_3`).
