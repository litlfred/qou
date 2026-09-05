---
# qou-i6cn
title: 'TRIAGE: 29 library files carry 59 standalone axioms — Mathlib-gap or laundering?'
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T14:57:07Z
updated_at: 2026-09-05T17:50:46Z
---


## CORRECTION (2026-08-08, same session) — 29 files, not 8

The "8 files" in the title came from the same loose grep that produced
the wrong consumer counts in `qou-up56`. A proper scan (regex for
`^axiom\s+NAME` across `QOU/**/*.lean`, minus files where the axiom
feeds a discharging instance) gives:

**29 files, 59 axioms.**

| axioms | file |
|---|---|
| 9 | `QOU/HeckeAlgebra/MarkovTrace.lean` |
| 5 | `QOU/BraidsKnots/LinearJSJVolume.lean` |
| 5 | `QOU/HeckeAlgebra/Formal.lean` |
| 4 | `QOU/MathlibExt/SDPRankEquality.lean` |
| 4 | `QOU/HeckeAlgebra/JonesMarkovWenzl.lean` |
| 3 | `QOU/BraidKnot/IwahoriHeckeAPI.lean` |
| 3 | `QOU/HeckeAlgebra/Hoefsmit.lean` |
| 2 | `QOU/BraidKnot/QuantumDilogarithm.lean` |
| 2 | `QOU/BraidKnot/PSDFeasibilityProxy.lean` |
| 2 | `QOU/BraidKnot/LpDualityHypothesisClass.lean` |
| 2 | `QOU/HeckeAlgebra/Common.lean` |
| 1 each | `StaircaseCornerHook`, `JetHorizon`, `MathlibExt/SDP`, `MathlibExt/PhiBProd`, `QuantumObservableUniverses/QIntegralTransforms`, `Mathlib/RSKBridge`, `IwahoriHecke/Defn`, `AppendixSurreals/B1HyperbolicRowsTheorem`, `Archimedean/NuclearGroebnerReduction`, `Archimedean/WeierstrassProjection`, `Archimedean/BorromeanVolumeCatalan`, `BraidKnot/CommutativeCrossingEnergy`, `HeckeAlgebra/Wedderburn`, `FlavorDressing/DressedMassFromSubstrateSplit`, `Hecke/MarkovTrace`, `Hecke/Wedderburn`, `Eightfold/Sym2Gate`, `QBeta/MarkovZToCkMapping` |

Note three of the previously-listed eight are absent: two
(`n-v-bring-action`, `n-v-leading-order-derivation`,
`spectral-chart-correspondence`, `figure-eight-branching-rule`,
`q-codifferential-formula-prop`, `y-lambda-recipe-from-partition`) were
content-block sibling `.lean` files rather than library files and are
covered by their `.qa.json` sidecars; the axiom-bearing library set is
the table above. Re-derive the list before working it — do not trust
either the old 8 or this 29 without re-running the scan.

## The triage question, sharpened

The one axiom-discharged *instance* left in the corpus
(`SDPRealUniqueness`) turned out to be legitimate, and for a reason that
generalises to this queue. The test is **not** "is there an axiom" but:

> Does the axiom assert **an open conjecture of this framework**, or **a
> published theorem that Mathlib does not yet have**?

- **Published-theorem / Mathlib-gap** → legitimate. Keep, provided it
  carries a `-- Ref:` citation to the actual source (AGENTS.md §1) and
  the class/statement it discharges is content-bearing. `SDPRankEquality`
  and `SDPRealUniqueness` are the exemplars.
- **Open QOU conjecture** → laundering. The honest state is a
  content-bearing carrier with no instance (§3b-tax).

`HeckeAlgebra/MarkovTrace.lean` (9) and `HeckeAlgebra/Formal.lean` (5)
are the highest-value reads: Markov-trace properties are load-bearing
for the whole mass chain, and whether those nine are Jones/Wenzl
citations or QOU assertions materially changes what the mass results
rest on.

**Do not batch-process.** Every file needs the question above answered
by reading it.

## SECOND CORRECTION (2026-08-08) — 55 axioms in 26 files

The "29 files / 59 axioms" figure above was itself slightly inflated: a
`^axiom\s+NAME` regex also matches **docstring prose that happens to wrap
onto a line beginning with the word "axiom"**. Nine such false hits, with
tell-tale "names" — `equation`, `beyond`, `with`, `is`, `in`, `audit`.
Example, `SDPRankEquality.lean:63`:

```
have **proven sub-instances**, and the rank-via-eigenvalues
axiom is consumed only via Mathlib-standard reasoning; the
```

Stripping block/line comments before matching gives the real figure:

**55 axioms in 26 files.**

That is now three successive wrong counts in this bean's lineage (8 files →
29 → 26), each from a regex I did not validate against the thing it was
counting. **Strip comments before counting anything in Lean source.**

| axioms | file |
|---|---|
| 9 | `QOU/HeckeAlgebra/MarkovTrace.lean` |
| 5 | `QOU/BraidsKnots/LinearJSJVolume.lean` |
| 5 | `QOU/HeckeAlgebra/Formal.lean` |
| 4 | `QOU/HeckeAlgebra/JonesMarkovWenzl.lean` |
| 3 | `QOU/BraidKnot/IwahoriHeckeAPI.lean` |
| 3 | `QOU/HeckeAlgebra/Hoefsmit.lean` |
| 2 | `LpDualityHypothesisClass`, `PSDFeasibilityProxy`, `QuantumDilogarithm`, `HeckeAlgebra/Common`, `SDPRankEquality`, `SDPRealUniqueness` |
| 1 | `B1HyperbolicRowsTheorem`, `BorromeanVolumeCatalan`, `NuclearGroebnerReduction`, `WeierstrassProjection`, `Eightfold/Sym2Gate`, `DressedMassFromSubstrateSplit`, `Hecke/MarkovTrace`, `HeckeAlgebra/Wedderburn`, `IwahoriHecke/Defn`, `JetHorizon`, `Mathlib/RSKBridge`, `MathlibExt/SDP`, `QBeta/MarkovZToCkMapping`, `StaircaseCornerHook` |

## Cheap first-pass discriminator: the citation

Sorting axioms by the `-- Ref:` immediately above them separates the two
classes fairly well:

- **published DOI / arXiv ref** → almost certainly the legitimate
  Mathlib-gap class (Wenzl, Jones, Kassel, Geck–Pfeiffer, Lang, Schrijver).
- **`[manuscript]`-only ref** → the ones that may assert a QOU conjecture.
  13 of these; they are where the reading effort belongs.
- **no ref at all** → an AGENTS.md §1 violation regardless of class.

The `[manuscript]`-only list: `b1_hyperbolic_rows`,
`normal_form_exists_unique`, `evenPower_necessary_for_blockPosSemidef`,
`phi_q_residual`, `li2_q_residual`, `AtomicKnot`, `Vol_p`,
`dressed_mass_split_substrate_closed_form`, `partitions_as_finset`,
`aeon_recycling`, `affine_slater_rigidity`,
`slater_strict_complementarity_kernel_axiom`, `canonicalScaleAxiom`.

**The discriminator is a sort, not a verdict.** `weierstrass_diff_eq_axiom`
carried a perfectly good Lang DOI and was still a provable triviality that
never mentioned the function it claimed to constrain (PR #4774). A correct
citation says the *intent* was sound; it says nothing about whether the
Lean matches it.

## Read so far (18 of 55)

| file | verdict |
|---|---|
| `HeckeAlgebra/MarkovTrace.lean` (9) | **2 defects, fixed** (PR #4774) — `∀`-bound `z` collapsed `tr_M` to zero; `wenzlBridge`'s `∀ q` made the block-sum q-independent. Other 7 are Wenzl/Kassel/Jones citations + `partitions_as_finset` (a genuine Mathlib-API gap: `Nat.Partition n` has no `Finset` enumeration). Cleared. |
| `HeckeAlgebra/Formal.lean` (5) | **Cleared** — all Geck–Pfeiffer §4.4, Mathlib has no Iwahori–Hecke port. *Caveat worth a follow-up:* the operations (`heckeFormalMul`, `heckeFormalOne`, `heckeFormalSMul`) are axiomatised **without** associativity or unit laws, so nothing proves the result is an algebra. Not laundering, but the interface is weaker than it reads. |
| `Archimedean/WeierstrassProjection.lean` (1) | **Defect, fixed** (PR #4774) — was provable from nothing. |
| `MathlibExt/SDPRealUniqueness.lean` (2) | **Cleared** — Boyd–Vandenberghe §5.5.4, content-bearing class, cited. |
| `MathlibExt/SDPRankEquality.lean` (2) | **Cleared** — documents its axioms deliberately as Mathlib-gap inputs. |

**37 axioms in ~21 files remain unread.** Highest value next:
`BraidsKnots/LinearJSJVolume.lean` (5, and two are `[manuscript]`-only —
`AtomicKnot`, `Vol_p` — with `Vol`/`JSJ_volume_additivity` feeding the
volume side of the mass formula), then
`HeckeAlgebra/JonesMarkovWenzl.lean` (4) and
`BraidKnot/IwahoriHeckeAPI.lean` (3).

The `∀`-bound-constant shape specifically is now covered by
[`scripts/lean-one-sided-binder-audit.py`](scripts/lean-one-sided-binder-audit.py)
(corpus currently clean), so the remaining reads are looking for the
*other* failure modes: an axiom that does not mention the object it claims
to constrain, an uncited assertion, or a QOU conjecture wearing a citation.


## RE-MEASURED 2026-09-05 — the queue is 18 in 12 files, not 55 in 26

Fourth count in this bean's lineage, and the previous one is stale by **37
axioms / 14 files**. Measured on current `main`, stripping block comments,
docstrings AND line comments before matching `^\s*(noncomputable\s+)?axiom\s+NAME`:

    before this session:  19 axioms / 13 files
    after removing aeon_recycling: 18 / 12

**The bean's two highest-value targets now carry ZERO axioms**, so its
priority guidance must not be followed as written:

| file | bean said | now |
|---|---|---|
| `BraidsKnots/LinearJSJVolume.lean` | 5 (incl. `AtomicKnot`, `Vol_p`) | **0** |
| `HeckeAlgebra/JonesMarkovWenzl.lean` | 4 | **0** |
| `HeckeAlgebra/MarkovTrace.lean` | 9 | 2 |
| `HeckeAlgebra/Formal.lean` | 5 | 1 |
| `HeckeAlgebra/Hoefsmit.lean` | 3 | 2 |

Both files still EXIST — the axioms were drained, not the files. `Eightfold/Sym2Gate.lean`
is the only named file actually gone.

### All 18 carry a `-- Ref:` — no AGENTS.md §1 violations

`[manuscript]`-only, i.e. where the reading effort belongs (4):

- `b1_holds_at_row` — `AppendixSurreals/B1HyperbolicRowsTheorem.lean`
- `evenPower_necessary_for_blockPosSemidef` — `BraidKnot/PSDFeasibilityProxy.lean`
- `affine_slater_rigidity` — `MathlibExt/SDPRankEquality.lean`
- `slater_strict_complementarity_kernel_axiom` — `MathlibExt/SDPRealUniqueness.lean`

**The last two are in files this bean marks "cleared".** Both cite the QOU
manuscript's own `prop:operator-selection-lp`, so that clearance plausibly
covered each file's *other* (Alizadeh–Haeberly–Overton / Boyd–Vandenberghe)
axiom rather than these. Re-read before trusting the clearance.

## aeon_recycling — VACUOUS, removed (PR #6859)

`axiom aeon_recycling (cmb : CMBFunctorValue) : PlanckStepResult` **never
mentions `cmb` in its result type**, so its statement is discharged by a
constant function. Now two theorems in `JetHorizon.lean`:

- `planckStepResult_cmb_independent` `[propext, Quot.sound]` — exhibits
  `f` with `f c₁ = f c₂` for all inputs.
- `planckStepResult_nonempty` `[propext]` — a toy algebra (`ULift Bool` at
  every degree) inhabits the result type.

The axiom's own NOTE justified `axiom` over `opaque` by claiming `Nonempty
PlanckStepResult` "cannot be witnessed without proving the conjecture
itself". Category error: inhabiting the RESULT TYPE ≠ the conjecture.

**The real gap: there is no Planck-step map in the formalisation.** `Φ₁`
occurs only in prose. And — the non-obvious part — a §3b-tax content-bearing
carrier cannot be written either, because any statement about an *abstract*
`Φ` is satisfied by choosing `Φ` to be the toy. The object is absent, so this
is not a "should have been a class" case.

Zero consumers; nothing downstream changed.
