# Assessment: the categorical P=NP-contradiction dialogue (Khovanov / HH / LKB / Brieskorn)

**Date:** 2026-08-01 · **Trigger:** external-AI dialogue proposing to cross the
`res ≠ 0 ⟹ P≠NP` wall via categorification (Khovanov homology, Rouquier
complexes), Hochschild homology (`HH_0`/`HH_1`), the Lawrence–Krammer–Bigelow
(LKB) representation, and a P=NP contradiction on the categorical Bring/Brieskorn
fibre. **Verdict:** the categorical scaffolding is real and citable and
*sharpens where the wall sits*; the actual contradiction
(`decision_collapse_refutes_homology`) is **circular** and rests on a **category
error**. Do **not** formalize it as a proof of P≠NP. Companion to the
[2026-05-30 KLR-dialog assessment](2026-05-30-klr-dialog-assessment.md) — same
class of re-pitch (categorical dressing over a smuggled premise).

## The two flaws in the contradiction

### 1. Category error — "exponential group growth ⟹ no polynomial decision"

The load-bearing physical claim is that a faithful, exponentially-growing
mapping class group cannot admit a polynomially-bounded decision metric, so
`P=NP` would force a contradiction. **This is false, and the braid group is the
counterexample:**

- The **word problem in `B_n` is polynomial-time** (Garside normal form;
  Dehornoy handle reduction) — *despite* `B_n` having exponential growth and a
  faithful LKB representation.
- Unknot recognition sits in `NP ∩ coNP` (Hass–Lagarias–Pippenger; Lackenby);
  its complexity is unrelated to `B_n`'s growth rate.

Group growth rate and decision complexity are **independent axes** — exactly the
magnitude-vs-quantifier split of
[`MagnitudeAxisBoundary`](../../content/quantum-observable-universe/lean/QOU/Information/MagnitudeAxisBoundary.lean)
and
[`CountingModuliGrade`](../../content/quantum-observable-universe/lean/QOU/Information/CountingModuliGrade.lean).
Exponential word growth is a **magnitude** fact, invariant under P vs NP (true in
both worlds); no P≠NP conclusion follows from it. The dialogue's "photon ≠
unknot" self-correction did not touch this — it reran the same word-metric
argument.

### 2. Circularity — the wall is smuggled into `h_resolve`

The proposed Lean lemma's contradiction lives entirely in one hypothesis:

```
h_resolve : ∀ n, homological_width (decision_cone n) ≤ decisionCost n
```

This asserts *deciding costs at least the topological/homological magnitude* —
the **no-shortcut / faithfulness** assumption, which **is**
`counting-hard ⟹ decision-hard`, which **is** the wall. The proposed proof body
is literally `not_superPolynomial_of_polyGrowth` (the sorry-free lemma from
[`PolyGrowthAlgebra`](../../content/quantum-observable-universe/lean/QOU/Information/PolyGrowthAlgebra.lean))
applied to a premise that already encodes the conclusion:

- `FaithfulHomologicalAction.width_growth` (cone width is super-polynomial) is
  *fine* — that is the **counting** hard point, provable and P-vs-NP-invariant
  (`physicalCost_superPoly` analogue).
- `h_resolve` is
  [`PhotonicDecisionHard`](../../content/quantum-observable-universe/lean/QOU/Information/CountingModuliGrade.lean)
  in a Brieskorn costume — a no-instance conditional. Providing the instance
  *is* proving P≠NP.

Composing the two assumes the wall, then "derives" it. The gap between
`width_growth` (proved) and `h_resolve` (assumed) is the untouched Millennium
problem. Landing it as a closed contradiction is the axiom-laundering AGENTS.md
§"Axiomatization is NOT a Proof" forbids.

## What is genuinely useful (salvage)

1. **`HH_0(H) = H/[H,H]` = cocenter = `ker(trace)` = the magnitude home;
   `HH_1(H)` = outer derivations = home of a *non-trace* decision functional.**
   Correct, and it sharpens "decision lives in `ker(tr)`" from a subspace to a
   precise homological home. **Xuhua He's cocenter / density-theorem basis**
   (minimal-length conjugacy-class representatives spanning `[H,H]`) is real and
   citable. Candidate: a small Lean note tying the image of
   `MagnitudeTraceCommutator.trace_comp_conjOp_sub_id` to the cocenter.
   (Bean `qou-ftre`.)
2. **LKB faithfulness** is a real candidate for a functional surviving on
   `[H,H]` — with the caveat the dialogue omits: *faithful ≠ efficiently
   computable decision separator*. Faithfulness separates braids as group
   elements; it is not a poly-time decision procedure (the same
   counting/decision confusion, one level up). **Khovanov categorification**
   (Jones = graded Euler characteristic; the chain complex remembers what the
   trace forgets) is a genuine categorical analogue of `trace_comp_conjOp` —
   the trace kills what the homology retains. (Bean `qou-5erw`.)

## Disposition

- The `[H,H] = ker(trace)` framing and the `HH_0`/`HH_1` split are adopted as
  the sharpened home of the wall; Xuhua He is the citation.
- LKB / Khovanov are recorded as candidate directions, honestly scoped (faithful
  ≠ efficient decision).
- `decision_collapse_refutes_homology` is **not** formalized as a P≠NP proof. If
  written at all, only as a no-instance conditional class with an explicit
  "conditional on the unproved faithful-decision lower bound" banner — never a
  closed contradiction.
- Recurring re-pitch pattern (categorical dressing over a smuggled decision
  lower bound): read this doc before re-deriving the analysis on a new
  categorical route.
