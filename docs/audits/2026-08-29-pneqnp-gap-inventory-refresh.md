# P≠NP-in-QOU — gap inventory, re-measured against `main` (2026-08-29)

**Scope.** A full re-read of the P≠NP cluster against the live tree, prompted by
the question *"what are the remaining gaps, what is still open, what can we chip
away at?"*. The four standing audits are 1–5 weeks old and **one of them is
stale in a way that misdirects effort**; that correction is the main content
here.

Prior audits, all still worth reading and all still correct except where noted:
[2026-07-25 status](2026-07-25-p-vs-np-in-qou-status.md) ·
[2026-08-01 two-axis wall inventory](2026-08-01-pneqnp-in-qou-two-axis-wall-inventory.md) ·
[2026-08-09 robustness / Mathlib survey](2026-08-09-pneqnp-robustness-mathlib-infra.md) ·
[2026-08-15 obstruction route](2026-08-15-obstruction-route-three-legs.md) ·
[2026-08-21 TL_n route scoping](2026-08-21-wenzl-discharge-tln-route-scoping.md)

## 0. Measured facts (this is what changed)

Everything below was measured on `main` at `df81b22be4`, not read off a status
note.

**The cone is sorry-free in code.** Every `sorry` occurrence under
`QOU/Information/`, `QOU/Hecke/` and `QOU/MathlibExt/` is inside a docstring or
comment. There is no live `sorry` in the P≠NP cluster.

**No conjecture carrier has been laundered.** All sixteen carriers are
instance-free:

`QouPNeqNp`, `TraceFaithfulness`, `JetHorizonTransfer`, `ComplexityDictionary`,
`WenzlCriterion`, `SchurElementCriterion`, `JonesComplexityCitations`,
`ResidueFaithfulness`, `QouGCTObstruction`, `QOUTraceCountHard`,
`PhotonicDecisionHard`, `MatchingFacts`, `CitedComplexity`, `QOUObstruction`,
`IsOcneanuWeightSystem`, `WedderburnDecomp`.

So the open content of this programme is located **entirely** in instance-free
§3b-cond classes, not in sorries. That is the honest shape, and it is the shape
the guardrails were built to produce.

## 1. The stale row — correct this before planning any Hecke work

[2026-07-25 §4](2026-07-25-p-vs-np-in-qou-status.md) reads:

> | `H_n(q)` semisimple ⟺ `[n]_q!≠0` | **n=2 fully discharged as a theorem**; general `n` needs the `T_w` basis (Mathlib wall) |

and §5 item 1 tells the next agent that the remaining work is *"the general `T_w`
basis / `dim = n!` … and the symmetrizing-trace Gram `det(Gram)=[n]_q!`"*.

**Both halves are now misleading, in opposite directions.**

**(a) The rank ladder went past n=2.** `QOU/Machinery/HeckeH3Semisimple.lean`
and `QOU/Machinery/HeckeH4Semisimple.lean` both exist and both prove
`IsSemisimpleRing` at their rank by transport along an explicit Wedderburn
isomorphism — *"the statement the cited `WenzlCriterion` /
`SchurElementCriterion` classes carry, now **proved** rather than cited at this
rank"*. The H₄ file is explicitly **det-free**: the 24×24 Gram determinant is
sympy-verified but Lean-out-of-reach (`det_fin_24` would carry 24! terms), so
the rung was reached *without* the determinant the §5 plan says to go get.

**(b) The general-`n` gap is no longer the `T_w` basis.** A second route exists
and is further along: `QOU/MathlibExt/WenzlSchurElement.lean`
`semisimple_of_substrate` gives semisimplicity **at every rank** for `Q > 1`,
`X ≤ 0`. Its Schur-element leg is *computed, not assumed* —
`schurElement_ne_zero` (line 231) is a genuine sorry-free theorem whose only
hypotheses are `1 < Q` and `X ≤ 0`; no class, no `sorry`, no `native_decide`.

**Do not over-read (b).** This is **not** a discharge, and calling it one would
be exactly the laundering the guardrails forbid. `semisimple_of_substrate`
carries `[SchurElementCriterion Q X ss]`, which is itself instance-free. The
honest statement of the change is:

> The all-`n` route now cites **one** literature theorem — Geck–Pfeiffer Thm
> 7.2.6, *"every Schur element nonzero ⟹ semisimple"* — with the
> **Schur-element non-vanishing computed in Lean for all `n`**. Previously the
> all-`n` route needed the whole `T_w`/Matsumoto basis theory *and* a Gram
> determinant *and* the criterion.

Per [2026-08-21](2026-08-21-wenzl-discharge-tln-route-scoping.md),
`WenzlCriterion` and `SchurElementCriterion` *"state the same literature theorem
from two equivalent angles"*. So the citation **count** did not improve. What
improved is that one of the two legs feeding it is now proved outright, and the
residual is a single named theorem rather than a missing basis theory.

**Consequence for planning.** The `T_w` basis (beans `qou-lrz1` / `qou-twwf`)
is still the honest Mathlib gap for the *determinant* route, and item 1 of the
`TL_n` scoping audit's build list is still the smallest independently
worthwhile piece. But it is **no longer on the critical path to all-`n`
semisimplicity**, and an agent following §5 item 1 as written will build a large
thing the Schur route does not need.

## 2. What is open, by kind

Three genuinely different kinds of open, which the corpus has historically
blurred. Keep them apart.

### Kind A — the Millennium wall (never chip; never fabricate)

`TraceFaithfulness` / `JetHorizonTransfer.transfer` /
`ComplexityDictionary.separation_of_blocked` — the counting→decision transfer,
`(exact-Jones ∉ FP) ⟹ (P ≠ NP)`.

This is P≠NP itself. It is not merely unproved; it is **fenced on three sides**,
and each fence is a corpus result, not an opinion:

- **refuted as a generic law** — `OptionBCountingTransfer.generic_transfer_false`
  (perfect matching: `#P`-hard to count, poly-time to decide);
- **blocked as a uniform argument** — Razborov–Rudich; *"works at every
  non-torsion `q₀`"* is uniform;
- **barred by algebrization** — Aaronson–Wigderson; a poly algebraic shortcut
  refutes the full-tree-read hypothesis of every horizon lower bound
  (`SkeinHorizonLowerBound.no_horizon_cost_of_polyObservable`).

The [2026-08-01 inventory](2026-08-01-pneqnp-in-qou-two-axis-wall-inventory.md)
sharpens the residue to *a non-trace, non-algebraic fibre-level `HH₁` cocycle
over Bring's surface, beyond every finite Vassiliev order*. Bean `qou-iv9f` is
correctly marked *"constructing it = proving P≠NP"*; bean `qou-b7j7` is
correctly **scrapped** as *"RETIRED — DO NOT PROVE"*.

### Kind B — cited literature, not in Mathlib (chippable only as a Mathlib contribution)

Real theorems that Lean cannot currently see. Carrying them as instance-free
cited classes is the correct disposition; fabricating an instance launders the
literature.

| Class | Literature | Note |
|---|---|---|
| `WenzlCriterion` / `SchurElementCriterion` | Wenzl 1988 / Geck–Pfeiffer Thm 7.2.6 | same theorem, two angles; **the one live chippable** — see §3 |
| `JonesComplexityCitations` | Jaeger–Vertigan–Welsh; Arora–Barak | `#P`-hardness of exact Jones; `NP ⊆ P^#P` |
| `IsOcneanuWeightSystem` | Wenzl 1988 | deliberately **not** an `instance`, so typeclass search cannot silently discharge it |

Mathlib has `TM2ComputableInPolyTime` but **no `P`, `NP`, `#P`, and no
poly-time many-one reduction** ([2026-08-09 §1](2026-08-09-pneqnp-robustness-mathlib-infra.md)).
`Computability.Reduce` is many-one on *decidability* — the wrong granularity.
Building a TM-based scaffold would make the statements *look* like the
literature without closing anything; the gap is a transfer theorem, not a
missing definition.

### Kind C — genuinely open, in scope, and not P≠NP

- **`QouGCTObstruction`** (`VP` vs `VNP`). The GCT files
  (`GCTMultiplicityObstruction`, `GCTSchurMultiplicity`, `GCTPerRankObstruction`)
  prove **regime** separations only — explicitly *not* `QouGCTObstruction`
  instances. Bürgisser–Ikenmeyer–Panova is the known barrier here (occurrence
  obstructions do not suffice), which is a *different* barrier from
  algebrization and is worth keeping distinct.
- **`WedderburnDecomp` has no instance anywhere** — its `y_lambda` is the
  corpus's only algebra-attached Ocneanu weight and is an unconstructed class
  field. This is a real structural hole *below* the Wenzl question.

## 3. What can actually be chipped

Ranked by (value to the programme) ÷ (cost), with the barrier each one does
**not** cross stated, so nobody mistakes progress for a crossing.

**1. `qou-0y6h` — Geck–Pfeiffer `det(Gram) = ∏ Schur` (already a `todo` bean).**
This is the single highest-value chippable item and it is *closer than the
standing plan says*, because §1(b) already supplies the Schur-element half for
all `n`. Formalising the criterion turns `semisimple_of_substrate` from
class-conditional into an outright theorem at every rank, which discharges the
`WenzlCriterion` hypothesis of `PNeqNpEquivalence` *for real*. Crosses no
barrier — semisimplicity is a magnitude-axis fact — but it removes one of the
two remaining cited classes from the conditional chain.

**2. `qou-z0pr` — wire the proved n=2/3/4 semisimplicity into
`PNeqNpEquivalence`.** Small, mechanical, and currently *not done*: the
concrete instances exist (`H2TraceForm`, `HeckeH3Semisimple`,
`HeckeH4Semisimple`) but `PNeqNpEquivalence` still consumes the cited class at
those ranks. Low cost, immediate honesty gain — the conditional statement gets
strictly smaller.

**3. `qou-h56b` — the `WedderburnDecomp*` name collision.** Three distinct
objects share one name, and the middle one
(`Mathlib/HeckeAlgebra.lean:118`) has `Prop`-**variable** fields
(`blocks_sum_to_one : Prop` plus `blocks_sum_holds : blocks_sum_to_one`) with a
global `instance triv_wedderburn` discharging it via `True` over `PUnit`. It
asserts nothing and **is found by typeclass search** — the
`proof-claims-unencoded` / `true-class-field` pattern of AGENTS.md §3b-tax.
Not on the Wenzl path, but it is a live vacuity hazard sitting in a namespace
adjacent to the real work.

**4. `qou-fpjy` — `#print axioms` cannot see the Wenzl dependency.** The three
`_of_wenzl` rows are byte-identical to the unconditional ones, so the axiom
check does **not** reveal that they are conditional. Any claim of the form
*"`#print axioms` shows no `sorryAx`, therefore unconditional"* is unsound in
this cluster. Worth a guard, and worth stating in any PR that cites axiom output
as evidence.

**5. Item 1 of the `TL_n` build list — `A_n` presents `S_n` as a Coxeter group.**
Still the smallest independently worthwhile Mathlib-scale piece, and genuinely
useful beyond this programme. But per §1(b) it is **no longer** blocking all-`n`
semisimplicity, so it should be scheduled as a Mathlib contribution on its own
merits, not as P≠NP critical path.

## 4. Do not re-attack

Consolidated from the prior audits; each is a *proved* dead end, not a matter of
taste.

1. **`χ(A) ≠ 0` as the decision residue** — wrong axis. `χ` is a `K₀`/
   Hattori–Stallings trace, factors through `HH₀`, blind to `[A,A]`
   (`CocenterTraceFactor.not_trace_of_separates_commutator`).
2. **Any trace / birthday / census / ω-grade invariant crossing to decision** —
   `census_blind_to_decision`, `trace_comp_conjOp`,
   `trace_eq_of_sub_mem_commutator`.
3. **Any finite-order Vassiliev invariant as the residue** — doubly excluded:
   poly-time by Goussarov–Polyak–Viro *and* a trace by Birman–Lin.
4. **The `TL_n` route to the Wenzl discharge** — scope-(a) refuted in
   [2026-08-21](2026-08-21-wenzl-discharge-tln-route-scoping.md): it saves the
   two items already done (5, 6) and pays the two never started (2, 4), and its
   stated premise (*"only the vanishing set matters"*) is falsified by a live
   sibling consuming weight **values**, plus by
   `vanishingSet_not_determines_weights`.
5. **The categorical `decision_collapse` contradiction** — circular; and *"exp
   group growth ⟹ no poly decision"* is false (braid word problem ∈ P).
6. **Fabricating any instance of the sixteen carriers in §0.**

## 5. Honest bottom line

Unchanged in substance from
[2026-08-01](2026-08-01-pneqnp-in-qou-two-axis-wall-inventory.md), and worth
restating because this review found nothing that moves it: the magnitude axis is
proved from every angle; every magnitude route across the wall is *proved* dead;
the one open link is localized to a non-trace, non-algebraic fibre-level `HH₁`
cocycle beyond every finite Vassiliev order. **That link is the Millennium
problem and this framework does not cross it.** The value delivered is the
localization and the pruning, not a proof.

What this review adds is narrower and purely practical: the semisimplicity gap
is **smaller and differently shaped** than the standing plan says, the residual
citation there is **one named theorem** with its companion leg already proved
for all `n`, and there are four small honesty-improving items (§3.2–§3.5) that
nobody is currently working.

## 6. Verification

Read-only review; no Lean was modified, so there is nothing to build.

- Sorry-freeness and instance-freeness were established by **grep over the live
  tree** at `df81b22be4`, not from status notes — the AGENTS.md corpus-grep
  discipline, applied to the *claim shape* (does an instance exist?) rather than
  the topic.
- `lean`-direct was **not** run: no `.lean` file changed in this commit. The
  sorry-free claims restated above are carried from each source audit's own
  verification block, which recorded `lean`-direct exit 0 and `#print axioms`
  with no `sorryAx` at the time — with the §3.4 caveat that in *this* cluster
  `#print axioms` cannot see the Wenzl conditionality.
- This document is prose with no math-bearing `$…$`/`$$…$$` beyond inline code
  spans, so the render-QA grep battery is not applicable.
