---
# qou-dyij
title: 'GAP/INFRA: Mathlib knot theory — Jones polynomial, connected sum, Markov-trace multiplicativity'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T12:33:56Z
updated_at: 2026-08-30T12:55:30Z
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
