# Narrowing the Δ_λ sign operator: pivotal/co-content grading at ζ₄, not a braid central element

**Date:** 2026-07-11 · **Axis:** Δ_λ chirality-sign carrier (strong sector) ·
**Follows:** the #3509 Δ_λ ζ₄ locus finding
([`2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md` §Finding 8](2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md)) ·
**Tier:** symbolic-exact (parameter-free) · **No fit; nothing wired.**

## Context

#3509 located the Δ_λ per-partition chirality sign exactly:
`sgn(Δ_λ) = sgn(w₀^{S_{λ'}}) = (−1)^{n(λ)} = q^{2n(λ)}|_{q=i}`, a value at `q=i`
(ζ₄, a non-semisimple point of H₅). The owner authorised continuing the
parameter-free hunt for the exact chiral operator realizing this central
character. This audit records the narrowing.

Probe [`deltalambda_sign_operator_narrowing_probe.py`](../../computations/deltalambda/deltalambda_sign_operator_narrowing_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-sign-operator-narrowing.witness.json) (3/3).

## The narrowing

The sign carrier `q^{2n(λ)}` is a central character of H_n(q). Three exact tests
rule out the simple/canonical candidates and pin its structural home:

- **(A) Not a framing power.** Neither the full twist `θ_λ = q^{2(n(λ')−n(λ))}` nor
  the framing sqrt `θ_λ^{1/2} = q^{n(λ')−n(λ)}` reproduces the sign at `q=i` — both
  are graded by the **content sum** `n(λ')−n(λ)`, not by `n(λ)`. (Corrects the
  transient "half-twist-class" label from the #3509 branch, already fixed there.)
- **(B) Not a low-degree JM central element.** The centre of H_n(q) is the symmetric
  functions of the Jucys–Murphy elements, whose eigenvalue on `V_λ` is a symmetric
  function of the content multiset `{q^{2c(box)}}`. Exact rational linear algebra
  (pooled over λ⊢4..7) shows `n(λ)` is **not** an exact polynomial in the content
  power sums `p_k = Σ_box c^k` (+ `|λ|`) up to degree 4. So `q^{2n(λ)}` is not a
  canonical low-degree JM/framing central element.
- **(C) It is the co-content / principal-specialization (pivotal) grading.** The
  statistic is `n(λ) = Σ_box row(box)` — the exponent in the principal specialization
  `s_λ(1,q,q²,…) = q^{n(λ)}·∏…`, a `q^{2ρ}`-type **pivotal grading** of the ribbon
  category. It is **distinct** from the JM contents `c = col − row` (which sum to
  `n(λ')−n(λ)`), and it is realizable (the content multiset determines λ, verified
  n≤10, but only via a high-degree/interpolation combination — consistent with (B)).

## Interpretation

The Δ_λ chirality sign lives in the ribbon **pivotal / ρ-grading** structure evaluated
at **ζ₄** — not in the braid group's central (framing/JM) elements. This is coherent
with the whole session's fibre-vs-archimedean theme: the chirality is a categorical
(pivotal, root-of-unity) datum, invisible to every real-q₀ braid-trace construction
(the six failed Δ_λ ansätze, the KL-positivity route, the raw T(2,5) trace, the
re-framed trace — all real-q₀).

## Still open (explicitly not claimed)

- The **exact pivotal element** realizing `q^{2n(λ)}` (a `q^{2ρ}`-type grading operator
  at ζ₄), as a canonical categorical morphism.
- The **magnitude** `|Δ_λ| = dim` (Track A / Subgoal-2, owner-gated).

This audit **locates and narrows** the sign carrier; it does **not** derive Δ_λ. The
exact-element + magnitude work stays gated Track-A — recorded, not fished.

## Cross-references

- Prior locus: [`2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md` §Findings 6–8](2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md)
- Selection-rule engine (on main): `QOU/SelectionRules.lean`
- Δ_λ gate + mixed-sign target: `QOU.BraidsAndKnots.S5SO3FiberAction.PartitionOf5.deltaSign_mixed`
