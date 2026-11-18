---
# qou-i6cn
title: 'TRIAGE: 29 library files carry 59 standalone axioms — Mathlib-gap or laundering?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T14:57:07Z
updated_at: 2026-11-18T11:45:08Z
parent: qou-6qbv
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


## All four `[manuscript]`-only axioms now read (2026-09-05)

| axiom | verdict |
|---|---|
| `aeon_recycling` | **VACUOUS — removed** (PR #6859) |
| `affine_slater_rigidity` | **legitimate Mathlib-gap** — citation corrected |
| `slater_strict_complementarity_kernel_axiom` | **legitimate Mathlib-gap** — citation corrected |
| `evenPower_necessary_for_blockPosSemidef` | **QOU conjecture, not a Mathlib gap** — see below |
| `b1_holds_at_row` | **honest conditional bookkeeping** — but uninterpreted |

### The two SDP axioms: legitimate, wrong section number

Both assert a published convex-optimization theorem and `SDPRankEquality`
carries PROVEN sub-instances for the positive-definite case. But **the two
files contradicted each other on the citation**, and one contradicted itself.
`SDPRealUniqueness.lean` had already diagnosed it in its `-- Ref:` lines —
*"Boyd's §5.5.4 is 'Mechanics interpretation of KKT', which doesn't cover
this"* — and never drained the same stale number from its own prose.
11 sites across 3 files corrected; authority is Alizadeh-Haeberly-Overton
(1997) §3, with B-V §5.5.2 for the definition of strict complementarity.
`SDP.lean` additionally read *"the §3b-cond §5.5.4 pattern"*, conflating an
AGENTS.md section with a book section.

### `evenPower_necessary_for_blockPosSemidef` — the one that fails the discriminator

Its ref is `[manuscript] Ch. braid-knot, prop:operator-selection-lp
(... binding-k-solver.witness.json)` — a QOU proposition backed by **numerics**,
which is this bean's laundering class, not the Mathlib-gap class.

The file argues it is *"an honest `axiom`"* because the necessity direction
"needs the algebra-evaluation map the header lists as an open Lean port". That
is fair about the EFFORT and does not answer the discriminator: effort is not
provenance.

**Not vacuous, though — and that distinction matters.** Unlike `aeon_recycling`,
it mentions `w` on both sides and states a real implication. What it cannot do
is fire: `braidWordEval` is `opaque`, so `(braidWordEval n w).PosSemidef` is
underivable for any concrete `w`. **Zero code consumers** (two prose mentions
in `HopfBindingK.lean`). So it is inert, and there is no urgency.

Per this bean's own rule the honest state would be a §3b-tax content-bearing
carrier with no instance. NOT done here: it would delete a name the file
deliberately defends, and the axiom is inert either way. Left as a framed
choice for the author.

### `b1_holds_at_row` — honest, and worth one caveat

Genuinely well-built: explicitly a conjecture, **conditional** on two named
external inputs (`BlochSuslinRegulator`, `VanDerVeenVolumeConjecture`) threaded
as real hypotheses, with `b1_hyperbolic_rows` *derived* from it rather than
assumed. Zero consumers.

The caveat: all three symbols are `opaque`, so the structure is uninterpreted.
The docstring claims *"It is falsifiable: it says something about the named
`B1HoldsAt` at each named row, rather than about an arbitrary numeral."* That is
right about FORM; with `B1HoldsAt` opaque it is not falsifiable in CONTENT.
Do not cite `b1_hyperbolic_rows` as an established result — it is bookkeeping
over three undefined symbols, correctly wired.

### Remaining

14 axioms with published citations, unread: `IwahoriHeckeAPI` (3, Dipper-James
+ Murphy ×2), `Hoefsmit` (2), `HeckeAlgebra/MarkovTrace` (2, Wenzl + Jones),
`Hecke/MarkovTrace` (1, Jones), `Formal` (1, Geck-Pfeiffer),
`WeierstrassProjection` (1, Lang — bean says "defect, fixed", but the axiom is
still present, so re-read), `ParallelogramContour` (1, Ahlfors), `SDP` (1,
Todd), `SDPRankEquality`/`SDPRealUniqueness` (1 each, AHO).


## `weierstrass_diff_eq_axiom` — legitimate, and I misread this bean

This bean records it as *"Defect, fixed (PR #4774) — was provable from nothing"*,
yet the axiom is still present. I flagged that as a contradiction and offered
two explanations — "the fix re-cited it, or the record is wrong". **Both wrong.**
The fix was a **restatement**. The old form was

    ∀ (g2 g3 : R_q) (z : ℂ), z ≠ 0 →
      ∃ (wp_deriv wp_val : ℂ), wp_deriv ^ 2 = 4 * wp_val ^ 3 - ...

— an existential over two FREE complex numbers that never mentioned
`weierstrassProjection`, hence a theorem over ℂ (take `wp_val := 0`). The
current form quantifies over the **named primitives** `weierstrassProjection`
and `weierstrassProjectionDeriv`, so it is genuinely unproved and correctly
cited (Lang Thm VI.3.6). **Legitimate Mathlib-gap — and the exemplar of the
right fix.**

Note the through-line: *quantify over the named primitive* is exactly what
`aeon_recycling` lacked. The corpus already held the correct repair pattern.

## NEGATIVE RESULT: the `aeon_recycling` shape is a one-off, not a class

I tried three mechanical detectors for "an axiom that does not mention the
object it claims to constrain". **All three produced only false positives on
the live corpus**, while each caught a synthetic reconstruction of
`aeon_recycling`:

| shape | live flags | why they were false |
|---|---|---|
| axiom mentions no FILE-LOCAL symbol | 2 | symbols were IMPORTED (`SDPPrimal`, `RealStrictComplementarityPair`) — and this shape would have MISSED `aeon_recycling` itself, whose two symbols are file-local |
| explicit binder absent from the CONCLUSION | 2 | conclusion was about an *implicit* variable (`D = 0`); and an ASCII-only identifier regex never extracted `ω₁ ω₂ z₀ w` |
| binder never used AFTER its binder group | 3 | named **hypotheses** (`horient`, `hw`, `h_slater`, `h_feas`) are normally never referenced again in Lean |

Not shipped. Three shapes, 0 true positives across 18 axioms, so the useful
conclusion is the negative one: **no other axiom in the corpus has this
shape**, and it does not warrant a guard. Recording the three dead ends so
nobody spends the afternoon again — this is the detector-blindness pattern
AGENTS.md already catalogues, one level up.

## Tally after this pass

- **18 axioms / 12 files** (was 19/13; `aeon_recycling` removed).
- **All 4 `[manuscript]`-only axioms READ.** 1 removed vacuous, 2 legitimate
  (citations corrected), 1 (`evenPower_necessary_for_blockPosSemidef`) is a
  QOU conjecture rather than a Mathlib gap — inert, zero consumers, left as a
  framed choice.
- **`weierstrass_diff_eq_axiom` re-read and cleared.**
- Remaining unread: 13, all with published citations — `IwahoriHeckeAPI` (3),
  `Hoefsmit` (2), `HeckeAlgebra/MarkovTrace` (2), `Hecke/MarkovTrace` (1),
  `Formal` (1), `ParallelogramContour` (1), `SDP` (1), `SDPRankEquality` (1),
  `SDPRealUniqueness` (1).


## 🛑 CORRECTION to my own "one-off" claim — a SECOND vacuity, in `IwahoriHeckeAPI`

I recorded above that the `aeon_recycling` shape is *"a one-off, not a class"*
after three detectors found nothing. **Wrong, and scoped too narrowly.** The
three `IwahoriHeckeAPI` axioms — the best-cited in the corpus (Murphy 1981,
Dipper–James 1986) — constrained an API that was **provably collapsed**.

    noncomputable def centralIdempotent (H : _) (_lam : List ℕ) : H.carrier :=
      Classical.ofNonempty

The index is **discarded**, so a `def` is definitionally constant in it and
`centralIdempotent H [1]` IS `centralIdempotent H [2]`. With
`centralIdempotent_orthogonal_axiom`: `e*e = e` (λ=μ) and `e*e = 0` (λ≠μ, same
term) ⟹ **`e = 0`**. Machine-checked before the fix — the derivation compiled
on exactly `[propext, Classical.choice, centralIdempotent_orthogonal_axiom]`.
The other two axioms then held trivially (`0` commutes; `star 0 = 0`), so the
whole idempotent API asserted nothing.

**Not an inconsistency**, checked rather than assumed:
`wedderburn_decomposition_generic` quantifies EXISTENTIALLY over a fresh `e`
and never plugs in `centralIdempotent`, so its `(parts.map e).sum = 1` never
meets the zero. No external consumers either.

Fixed: both placeholders (`centralIdempotent`, `jucysMurphy`) are now `opaque`,
which their docstrings always said they were. Verified the collapse is gone —
the derivation now fails *"not definitionally equal"*.

**Why the earlier detectors could not see it:** the axiom's statement DOES
mention `lam` on both sides. The vacuity is in the DEFINITION, not the axiom.
So the negative result should have read "no other axiom has `aeon_recycling`'s
shape", not "the shape is a one-off". Two shapes, both invisible to scanning
axiom text.

## A detector that actually works — shipped

[`scripts/lean-constant-def-under-axiom-audit.py`](scripts/lean-constant-def-under-axiom-audit.py)
flags the CONJUNCTION: a `def` that discards an argument, has a constant body,
**and is constrained by an axiom**. Carries a `--selftest` and refuses to
report a clean tree if the self-test fails.

None of the three parts is a signal alone, which is why the earlier attempts
failed:

- **Constant body is usually CORRECT.** 24 such defs are live.
  `dimqPartition3 _q := 1` is right — `dim_q([3]) = [3]_q!/([3]_q[2]_q[1]_q)`
  really is q-independent. `ySign _q := 0` is right — a Schur polynomial in two
  variables vanishes on a three-row partition, which IS convention D. Both
  carry docstrings deriving exactly that.
- **An axiom over a placeholder** is the ordinary Mathlib-gap pattern.

Validated: on the pre-fix tree it flags `centralIdempotent` under all three
axioms; on the live tree, **0**. This is the first detector this session that
both self-tests positive AND reports a meaningful zero — the previous four
shapes each produced only false positives.


## Hoefsmit (2) and HeckeAlgebra/MarkovTrace (2) — all four LEGITIMATE

- `HoefsmitMatrix_hecke_relation`, `HoefsmitMatrix_braid_relation` — constrain
  `HoefsmitMatrix`, which is **`opaque`**, so no collapse is possible. Real
  content (Hecke quadratic `T² = (q−1)T + q` in T-form, plus the braid
  relation), cited to Hoefsmit 1974. Mathlib has no Iwahori–Hecke seminormal
  form. The T-form choice is deliberate and reasoned (F_p compatibility —
  integer coefficients in q, where the σ-form's `q^{1/2}` forces `ℚ(q^{1/2})`).
- `JonesMarkovCoefficient_sum_eq_one` (Wenzl 1988 Lemma 3.2) — constrains a
  real `def` equal to `wenzlClosedForm` by `rfl`, over `partitions_as_finset =
  Finset.univ` (legitimate; Mathlib supplies `Fintype (Nat.Partition n)`).
- `MarkovTrace_markov_axiom` (Jones 1985) — `heckeStab` is `opaque`; the
  `markovParameter` is a named constant, not `∀`-bound.

## 🛑 THE COLLAPSE CLASS HAS THREE INSTANCES, AND THE CORPUS ALREADY KNEW

`MarkovTrace.lean` documents, at the axiom I was reading to clear it, the
**exact failure mode I found twice today** — and it was found first:

> **The `z` used to be a `∀`-bound variable, which made this axiom collapse the
> Markov trace to zero.** … hence `markovTrace n x = 0` for *every* `n` and
> *every* `x`. The corpus stayed consistent … but `tr_M`, the central object of
> the mass chain, was pinned to the zero function. Bean `qou-ck1f`.

So the class is:

| instance | mechanism | status |
|---|---|---|
| `MarkovTrace_markov_axiom` | `∀`-bound `z` ⟹ `tr_M ≡ 0` | found earlier, `qou-ck1f`, fixed |
| `centralIdempotent` | index-discarding `def` ⟹ `e_λ ≡ 0` | found today, fixed |
| `aeon_recycling` | conclusion independent of argument | found today, removed |

**My "one-off, not a class" call was wrong twice over.** Not only did I find a
second instance by reading two turns later — a THIRD was already documented in
the corpus, in a file on my own remaining-to-read list, with its own bean. I
declared a negative result from three failed detectors **without running the
corpus-grep checklist on the claim**, which is exactly what AGENTS.md requires
before declaring anything open, closed or absent. Detector silence is not
corpus silence.

Note the three mechanisms are all different (binder scope / discarded index /
argument-independent conclusion) and share only the *consequence*: an axiom
that pins its object to a trivial value while reading as substantive content.
That is why no single syntactic detector finds them, and why
`lean-constant-def-under-axiom-audit.py` is scoped to one mechanism and says so.

## Tally

**12 of 18 axioms read. 3 defects found and fixed.** Remaining 6, all
published-citation: `Hecke/MarkovTrace` (Jones), `Formal` (Geck–Pfeiffer),
`ParallelogramContour` (Ahlfors), `SDP` (Todd), `SDPRankEquality` (AHO),
`SDPRealUniqueness` (AHO).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 85 (`lane-e667`): Formalized `qou-ep4e`, `qou-fpjy`, `qou-i6bn`, `qou-i6cn`, `qou-mkm8` in `QOU.Foundations.TableauSquareSumPromotionBinderObligationVisibilityLogDeterminantBoundaryStandaloneAxiomDistributionNonHyperbolicVolumeVanishing` with 80-dps `mpmath` 2-commit witness stamp (`dfc69944cbe55f3b2622843a90dea18c98e576d7` -> `cbb6c21aa01988c4135bc7451f24b559c8179f67`, `scriptHash=0e68280fe3476a3f8543bf6de4770766624506d689b2ae34edd201278173e989`) in PR `litlfred/qou#8455` (`status: in-progress`).
