---
# qou-dyij
title: 'GAP/INFRA: Mathlib knot theory — Jones polynomial, connected sum, Markov-trace multiplicativity'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:33:56Z
updated_at: 2026-11-17T07:06:58Z
parent: qou-rtxm
---

Consumer: qou-301d (discharge the ArchimedeanTraceBridge multiplicativity hypothesis). Parent epic:
qou-08a2 (keystone hard-Mathlib-gap infra). This bean scopes the upstream primitives themselves.

## What Mathlib has (verify against current pin before starting; this is the v4.24.0-era state)
- BraidGroup — the repo carries its OWN (QOU.MathlibExt.BraidGroup: PresentedGroup + exponentSum).
- Coxeter groups + some Iwahori–Hecke algebra of a Coxeter system.
- NOTHING knot-theoretic: no Link, no KnotDiagram, no Reidemeister moves, no Kauffman bracket, no
  Temperley–Lieb algebra, no Markov trace / Ocneanu trace, no Jones polynomial, no connected sum.
So this is a from-scratch subfield, comparable in scope to a multi-year Mathlib area (modular forms,
Lie theory). Knot theory is a GENUINE Mathlib gap — building it would be a real community contribution.

## Two routes
### A. Diagram route (define Jones as a diagram invariant)
Formalise planar link diagrams (crossings, orientations, planar isotopy), Reidemeister moves I/II/III,
the Kauffman bracket, prove Reidemeister invariance, define Jones, define connected sum on diagrams,
prove J(K₁#K₂)=J(K₁)·J(K₂). The invariance proofs are tractable ONCE the diagram infrastructure
exists — but that infrastructure (planar/combinatorial-topology of diagrams) is a massive, essentially
absent Mathlib layer. UNBOUNDED. Do NOT start here.
### B. Algebraic Ocneanu-trace route (RIGHT scope for the consumer)
Build the H_n(q) tower, the Ocneanu/Markov trace functional tr with its defining properties
(tr(xy)=tr(yx); Markov stabilisation tr(x·σ_n)=z·tr(x)); prove the MULTIPLICATIVITY of tr under
juxtaposition (distant-strand product) — this gives J(K₁#K₂)=J(K₁)·J(K₂) as an ALGEBRAIC identity.
Define the Jones polynomial as the normalised trace of a braid closure. This does NOT need Markov's
theorem (that closure is a well-defined LINK invariant up to Markov moves) — and the bridge does not
need it either: it needs only the trace's multiplicativity, which route B delivers. BOUNDED, and it
reuses the repo's existing Hecke infra (BorromeanMarkovTrace, hecke_character_symbolic, Hoefsmit
seminormal reps, gram_matrix_seminormal_h6). Estimate: weeks, not months, for the multiplicativity
functional alone; the full "it's a link invariant" (Markov's theorem) is a separate, much larger item
NOT needed here.

## Literature (NO new lit needed — all standard)
Jones, "Hecke algebra representations of braid groups and link polynomials", Ann. Math. 126 (1987) —
the Ocneanu trace + Jones polynomial. Kassel–Turaev, "Braid Groups" (GTM 247) — Markov trace, Markov's
theorem, connected-sum multiplicativity. Goodman–de la Harpe–Jones, "Coxeter graphs and towers of
algebras" — the trace on the tower. The MATH is settled; the gap is Lean labour.

## ROAST (red-team — should QOU do this?)
- **For QOU: low priority, hygiene only.** It discharges a citation in one lemma. No new physics, no
  open problem closed. qou-brng is already "derived modulo declared calibrations".
- **Partly IRREDUCIBLE even if fully built.** Route B proves the Markov trace is multiplicative. It
  does NOT prove "the SUBSTRATE assembly amplitude IS that trace" — that identification is the fibre
  functor τ's DEFINITION, a modelling choice, not a theorem. So the hypothesis moves from "assume
  multiplicative" to "assume amplitude = Jones trace" + "Jones trace multiplicative (proved)". The
  assumption relocates; it does not vanish. Building all of route B still leaves an input.
- **Amplitude mismatch (the sharp point).** The mass self-carrier is lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1),
  a SUM of q-dims — NOT the product-multiplicative Jones polynomial. The multiplicative object is J;
  the binding lives in the interaction factor I = J(linked)/∏J ≠ 1, i.e. in the LINKING, not in the
  multiplicativity. Route B proves the UNLINKED reference factorises; it says nothing about the
  linking deviation that IS the binding. So the theorem you'd spend weeks on is about the reference
  state, orthogonal to the physics of interest.
- **Where it IS worth it: as a Mathlib contribution.** Knot theory is a real Mathlib gap; route B
  (Ocneanu trace + multiplicativity) is a clean, citable, bounded addition of independent value to
  the community. If someone wants to build Mathlib knot theory for its own sake, this is a good
  entry point — but that is a Mathlib project, not a QOU deliverable.

## Verdict / recommendation
Do NOT pursue for QOU as a priority. If pursued, ONLY route B (algebraic Ocneanu trace), upstreamed
to Mathlib, and scoped to the multiplicativity functional (skip Markov's theorem). Even then the
amplitude=trace identification stays a modelling input, so the net QOU gain is converting one citation
into "citation of a now-formalised theorem". Leave qou-301d at the citation boundary; revisit only if
the qou-08a2 keystone epic builds the general Hecke Markov-trace functional for other reasons.



---
**Update 2026-08-30 — route B's consumer-facing piece is DELIVERED; route A untouched by design.**
MarkovTraceMultiplicative lands the multiplicativity functional (trace of juxtaposition = product),
generic over CommRing with NO QOU dependency — Mathlib-upstreamable next to Matrix.trace_kronecker.
This is what qou-301d needed, and it needed neither Markov's theorem nor any link-diagram
infrastructure, confirming the roast's route-B scoping.

Still open for a genuine Mathlib knot-theory contribution (unchanged priority — LOW for QOU, real
for Mathlib): the Hecke tower + Ocneanu trace as a functional with the Markov stabilisation property,
the Jones polynomial as a normalised braid-closure trace, and (much larger) Markov's theorem that the
closure is a link invariant. Route A (diagrams, Reidemeister, Kauffman bracket) remains UNBOUNDED and
advised-against.

**Bridging note (#6158, same day).** The two updates above and below were written independently
within minutes of each other and are **not duplicative** — they are about different objects, and it
is worth saying so before someone reconciles them into one.

`MarkovTraceMultiplicative.lean` is **matrix-level**: `Matrix m m R`, `Matrix.trace_kronecker`, and an
`IsJuxtaposition` hypothesis. It imports no Hecke module and does not mention the Hecke algebra. The
correction below is about the **algebra** `H_n(q)` itself. Neither supersedes the other, and neither
is the Ocneanu trace *on the Hecke tower* — that still wants the Markov stabilisation property
`tr(x·σ_n) = z·tr(x)`, which both updates independently name as the open item.

---

## Correction from #6158 (2026-08-30): Mathlib has NO Iwahori–Hecke algebra at this pin

The "What Mathlib has" section above reads *"Coxeter groups + some Iwahori–Hecke algebra of a
Coxeter system."* **The second half is wrong**, and it matters because route B's scoping leans on it.

Measured at the pinned Mathlib (`rev f897ebcf72cd16f89ab4577d0c826cd14afaafc7`,
`leanprover/lean4:v4.24.0`), by binary-grepping the 6990 oleans — the source tree is absent in this
container, 0 `.lean` files, which is exactly how this class of claim goes wrong:

- positive control `CoxeterSystem` -> **3** oleans. The grep works.
- `HeckeAlgebra` -> **0** oleans.
- bare `Hecke` -> **1** olean, `Mathlib/NumberTheory/FLT/Basic.olean`, and it is a **bibliography
  string in a docstring**: *"R. Taylor and A. Wiles, Ring-theoretic properties of certain Hecke
  algebras"*. Not a declaration.

So Mathlib has the Coxeter layer (`CoxeterMatrix`, `CoxeterSystem`, length, inversions) and **no
Hecke algebra of any kind**. The first half of the sentence is right; the second describes something
that is not there.

## What this changes for route B — its first step is no longer from scratch

PR #6158 (branch `claude/hecke-braid-ideal-and-header-2026-08-29`, following #6055/#6053) builds
exactly the "H_n(q) tower" route B opens with, as local Mathlib-style infra:

- `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` — the **real** algebra: `RingQuot (FreeAlgebra R B)` modulo
  an inductive relation carrying the quadratic **and** braid families over an arbitrary Coxeter matrix
  `M`. Universal property (`lift`, `lift_T`, `hom_ext`, `exists_unique_lift`), non-vacuity
  (`indexRep`, `signRep`, `indexRep_ne_signRep`), generator invertibility (`isUnit_T`).
- `QOU/IwahoriHecke/Defn.lean` — the previous `axiom` here is **deleted**; the corpus had something
  *named* `IwahoriHecke` that was quadratic-only, i.e. not the Hecke algebra.
- `QOU/BraidKnot/HeckeTypeAPresentationEquiv.lean` — `algEquiv` proves two of the repo's presentations
  are the same algebra, and transports `finrank = (n+1)!` and the `T_w` basis (from #6053) across it.
- `QOU/BraidKnot/HeckeCellular.lean` — the cellular anti-involution (Graham–Lehrer axiom C2), the two
  extreme cell modules, and the rank-one Murphy element with its `q`-eigenvector property.

Route B's remaining ask is the **trace functional**, not the algebra. On that:
`QOU/IwahoriHecke/MarkovTrace.lean` now carries `GradedMarkovTraceExistence` with **real** Prop fields
(`gradedTrace_add`, `gradedTrace_cyclic`, `gradedTrace_zero`) — its trivial default instance and the
vacuous `graded_markov_trace_exists` were deleted in the same arc. Cyclicity `tr(xy) = tr(yx)` is
stated; **Markov stabilisation `tr(x·σ_n) = z·tr(x)` is not**, and that is the honest next step.

## The ROAST is unaffected

None of the above touches the red-team verdict, which is the part of this bean worth keeping. The
amplitude=trace identification is still a modelling definition rather than a theorem; multiplicativity
is still about the **unlinked** reference while the binding lives in the linking factor `I =
J(linked)/∏J`. Both objections survive verbatim, and the recommendation ("not a QOU priority; route B
only, upstreamed") stands. What changes is the **cost estimate**: less of route B is greenfield than
this bean assumed, because the layer it says Mathlib provides does not exist and the layer it says
must be built partly now does — in this repo.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 56 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8241 (`f5d60a0cc755a36459696dc679eebd3728acc344`)
- **Module:** `QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity` (`folio/quantum-observable-universe/lean/QOU/Foundations/SymplecticAtomicityWenzlSemisimplicity.lean`), wired into `QOU.lean`.
- **Theorems:** `jonesConnectedSum_mul`, `jonesConnectedSum_unit_left`, `jonesConnectedSum_unit_right`, `jonesConnectedSum_assoc`, `jonesConnectedSum_comm`, `reducedJones_trefoil_connected_sum_eq_sq` — proving reduced Jones polynomial multiplicativity `Vtilde(K_1 # K_2) = Vtilde(K_1) Vtilde(K_2)` from connected-sum writhe additivity `w(K_1 # K_2) = w(K_1) + w(K_2)` and reduced Kauffman bracket multiplicativity.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
