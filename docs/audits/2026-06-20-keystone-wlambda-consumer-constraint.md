# What the keystone mass-ratio actually needs from the W_λ frontier — consumer side

**Date:** 2026-06-20
**Branch:** `claude/keystone-wlambda-consumer-constraint-2026-06-20`
**Status:** Constraint note (no fitting; build stays owner-gated)
**Follows:** [#2516](https://github.com/litlfred/qou/pull/2516), [#2519](https://github.com/litlfred/qou/pull/2519)
**Complements (does not duplicate):** the *producer*-side scoping —
[`2026-06-16-keystone-index-necessary-conditions.md`](2026-06-16-keystone-index-necessary-conditions.md)
(C1–C7 on the form of `W_λ`) and the in-flight [#2488](https://github.com/litlfred/qou/pull/2488)
geometric-`W_λ` handoff.

## Why this note

The W_λ geometric frontier is already heavily scoped on the **producer** side:
7 necessary conditions any Sasakian index must satisfy to reproduce
`W_λ = d_q(λ)²/[n]_q!`, with the diff-geo build owner-gated. This note records
the complementary **consumer** side — what the keystone *mass-ratio observable*
actually needs the frontier to deliver — now pinned down by probes #2516/#2519.
It adds one forward constraint; it does not attempt the owner-gated build and
does not edit the producer-side docs.

## The consumer constraint (from #2516 + #2519)

The muon/electron mass-ratio splitting under `conj:s5-so3-fiber-action` was hoped
to come from the operator-valued branching of the Borromean knot through the
`E_(3,2)` (ℓ=2) vs `E_(3,1,1)` (ℓ=1) projectors, unlocking the Borromean `h⁴`
coefficient. Probes #2516/#2519 establish that the **knot layer contributes
nothing differential between the generations**:

- **#2516** — the `h⁴`-bearing `(2,1)` block enters both branchings with the same
  classical multiplicity 2, cancelling exactly in the μ/e difference.
- **#2519** — this cancellation is **robust to q-deformation**: generic-q Hecke
  branching `H₃⊂H₅` carries classical multiplicities, so
  `χ_(3,1,1)^{H₅}(β) − χ_(3,2)^{H₅}(β) = χ_(1,1,1)(β) = 1` identically,
  h-independent, for all q.

**Consequence.** The entire generation structure the mass-ratio sees lives in
the **block weights**, not in the knot evaluation. The relevant *consumer*
object is the production trace weight `y_λ` (the nuclear-mass-trace weight — a
distinct object from the geometric-index target `W_λ`; see the three-weight
table in the necessary-conditions doc). At q₀:

$$ y_{(3,2)} \approx 0.06172,\quad y_{(3,1,1)} \approx 0.01677,\quad
   \frac{y_{(3,2)}}{y_{(3,1,1)}} \approx 3.6813 \quad\text{(ratio from unrounded values).} $$

## The magnitude separation (the actionable point)

The block-weight ratio the mass-ratio consumes is **order unity** (3.68, → 1
only at q=1). The 210 ppb muon target is **2.1×10⁻⁷** — seven orders of
magnitude smaller, and (per the 2026-06-13 doc §1) an anchor-shift artifact, not
a leading block-selection effect. So the two regimes are categorically distinct:

| regime | object | magnitude | what produces it |
|--------|--------|-----------|------------------|
| generation structure | block-weight ratio `y_(3,2)/y_(3,1,1)` | O(1) (3.68) | the geometric frontier (W_λ producer, #2488) |
| fine μ-shift | 210 ppb | 2.1×10⁻⁷ | anchor re-pin residual — **not** block selection |

**Consumer-side necessary condition (complements producer-side C1–C7).** A valid
geometric construction must reproduce the **O(1) generation block-weight
structure** `y_(3,2)/y_(3,1,1) ≈ 3.68`; it is **not** required (and cannot be
expected) to produce the 210 ppb fine shift, which is a separate anchor-shift
quantity. Any future attempt to "derive 210 ppb" from the `W_λ`/`y_λ` block
weights is mis-scoped: the block weights set the O(1) generation skeleton; the
fine shift lives elsewhere. This is the forward (consumer) complement to the
formalize-first pruning that closed the knot-layer mechanism.

## Status of the frontier

Unchanged and owner-gated: the geometric construction of `W_λ` (Wu-manifold
SU(3)/SO(3) Sasakian S¹-equivariant index, boxed by C1–C7, in-flight on #2488)
remains the single open object. This note only sharpens its **relevance** to the
mass observable — the knot/branching/character layer above it is now proven null
on the generation difference, so the frontier carries the *entire* O(1)
generation structure and *none* of the 210 ppb fine shift. No fit introduced.
