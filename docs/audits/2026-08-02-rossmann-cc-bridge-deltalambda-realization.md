# Rossmann characteristic-cycle bridge as a **candidate** `DeltaLambdaDTRealization` mechanism (CONDITIONAL — not derived)

**Date:** 2026-08-02
**Status:** frontier scaffold / conditional candidate. **NOT a closure, NOT a
derived mechanism.** Owner-directed (uploads of Springer 1976, Shoji 2019,
Rossmann II).
**Epic:** `qou-r2nh` (the Δ_λ arc). **Frontier:** the single-degree geometric
concentration left open by PR #4581.

---

## TL;DR

The arc proved (sorry-free) that **`Δ_λ`'s value** `= (-1)^{n(λ)}·dim V_λ` is
fully substrate-derived and general, and that the **single-degree geometric
concentration** (which upgrades that value to the "Behrend-signed DT count of the
Springer fibre") is **not forced by any *algebraic* substrate route** — count
(#4559), SDP (#4570), valuation (#4574), and *every graded structure* unified
under one **cancellation** obstruction (#4581): a genuine graded multiplicity
tower spreads `V_λ` over both grade-parities and cancels to `f_λ(-1) < dim`,
never `Δ_λ`.

This note records the **one candidate mechanism** that is *not* an algebraic
grading: the **characteristic cycle of the archimedean character**. It is a
**conditional candidate**, honestly gated on a single open identification, and it
is explicitly **subject to the standing guard**
([`2026-06-09-aqa-dmodule-analogy-not-mechanism.md`](2026-06-09-aqa-dmodule-analogy-not-mechanism.md))
that the microlocal / perverse / Riemann–Hilbert layer is *analogy, not
mechanism*, until a QOU result is proved **through** it.

---

## The algebraic hook (real, in-corpus)

`tr_M` **is a character**: the corpus proves the Frobenius pairing

  `tr_M(σ_w) = Σ_λ y_λ(q) · χ_λ`,

a `y_λ`-weighted sum of irreducible characters, with an archimedean evaluation
`tr_M_at_q0`. This is exactly the class-function datum that **Springer 1976**
(*Trigonometric sums, Green functions of finite groups and representations of
Weyl groups*, Invent. Math. **36**, 173–207) connects to Weyl-group
representations through the nilpotent geometry. So the character → geometry link
is the right *kind* of object — not a far-fetched re-pitch.

## The published bridge (theorems — legitimate to cite, not to re-prove)

1. **Springer 1976 / Springer 1978** (Invent. Math. 36 / 44): the Springer
   correspondence realizes the irreducible `V_λ` in the cohomology of the
   Springer fibre `𝓑_λ`, with `dim_ℂ 𝓑_λ = n(λ)` and `V_λ = H^{2n(λ)}(𝓑_λ)`
   (**top degree, single-degree**).
2. **Shoji 2019** (arXiv:1909.06744, survey): the perverse-sheaf reformulation
   (Lusztig 1981); the grading **is** cohomological degree, and Kostka
   polynomials are the graded IC-multiplicities. Concentration = top cohomology.
3. **Rossmann II** (*Invariant eigendistributions on a semisimple Lie algebra and
   homology classes on the conormal variety, II: representations of Weyl
   groups*): a Harish-Chandra **invariant eigendistribution** `θ` on `𝔤` has a
   **characteristic cycle** `CC(θ)` — a Lagrangian cycle on the conormal variety
   `T*(flag)`, a `ℤ`-combination of conormals to nilpotent orbits — and this map
   **realizes the Weyl-group representations** (microlocal Springer).

**Chain:** an invariant eigendistribution `θ` ⟶ (Rossmann) its `CC(θ)` is a
Springer conormal cycle ⟶ (Springer/Shoji) the component at orbit `λ` is
`V_λ` concentrated in the single top degree `2n(λ)` ⟶ a **single grade-parity**
graded object with total `= dim V_λ` ⟶ (PR #4581, *proved*) it **saturates**
`|χ| = dim = |Δ_λ|` and realizes `Δ_λ` — *cancellation-free*, unlike every
algebraic tower.

So the missing input `#4581` named — "a space whose cohomology concentrates in
degree `2n(λ)` with fibre `V_λ`" — **is** the characteristic cycle of the
character, *if* the character is such an eigendistribution.

## The one open step (load-bearing — this is what makes it conditional)

> **(IDENT)** the archimedean `tr_M` evaluation is (the Green-function /
> invariant-eigendistribution avatar of) a class function on `𝔤𝔩_n` whose
> Springer characteristic cycle is the single-parity concentrated object.

The corpus establishes `tr_M = Σ y_λ χ_λ` (a character of the *finite-dimensional*
`H_n(q)`). It does **not** establish that its archimedean evaluation is a
*distribution on the Lie algebra `𝔤`* in Harish-Chandra's sense, nor that a
perverse / characteristic-variety structure is present — the 2026-06-09 standing
guard records "Riemann–Hilbert (holonomic ↔ perverse): **no current
counterpart**." **(IDENT) is genuinely open**, and it is where the derivation
would have to be *earned* from the 13 drivers (q₀ → categorical action →
archimedean functor), not declared.

- If **(IDENT)** is **forced** by the upstream data → the concentration is
  **derived** (Rossmann + Shoji are then applied theorems) and the frontier
  closes.
- If **(IDENT)** is **assumed** → the concentration is **imported**, i.e. exactly
  the `DeltaLambdaDTRealization` the arc kept honestly open — no progress beyond
  a nicer name.

## Verdict

**Conditional candidate mechanism, not a derived result.** The Rossmann
characteristic-cycle bridge is the *first* candidate that escapes the #4581
cancellation obstruction (it is not an algebraic grading — it is a microlocal
cycle), and it composes cleanly with #4581's proved single-parity saturation.
But it is gated on **(IDENT)**, an open identification the corpus does not have,
and it sits under the standing microlocal-is-analogy guard. Reported as **scope
(a) / conditional**, no `DeltaLambdaDTRealization` instance fabricated, nothing
wired to production.

The honest next step is *not* a numerical probe and *not* a Lean closure — it is
to determine whether **(IDENT)** can be *forced* from the archimedean-functor
construction (does q₀ → the categorical action → `tr_M_at_q0` land in the
Harish-Chandra invariant-eigendistribution setting?), or whether it is an
interpretive overlay. Until then this is language, per the 2026-06-09 guard.

## Lean

[`QOU/BraidsAndKnots/RossmannCCBridge.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/RossmannCCBridge.lean)
encodes the conditional as a **conjecture class** `RossmannCCConcentration`
(§3b-cond): its single content field is **(IDENT)** — the archimedean character's
Springer characteristic cycle is single grade-parity with total `dim`. The
theorem `rossmann_cc_realizes_deltaLambda` then **derives** (using #4581's proved
`abs_altSum_eq_sum_of_single_parity`) that such an object realizes `Δ_λ` — i.e.
`DeltaLambdaDTRealization` holds *conditionally on (IDENT)*. **No instance** (open);
the hypothesis is the genuinely-open input, the conclusion is derived, so this is
a non-degenerate conditional (not a self-assuming projection).

## References
- Springer, *Trigonometric sums, Green functions of finite groups and
  representations of Weyl groups*, Invent. Math. **36** (1976) 173–207.
- Springer, *A construction of representations of Weyl groups*, Invent. Math.
  **44** (1978) 279–293, https://doi.org/10.1007/BF01403165.
- Shoji, *Springer correspondence for symmetric spaces*, arXiv:1909.06744 (2019).
- Rossmann, *Invariant eigendistributions on a semisimple Lie algebra and
  homology classes on the conormal variety, II: representations of Weyl groups*.
- Standing guard: [`2026-06-09-aqa-dmodule-analogy-not-mechanism.md`](2026-06-09-aqa-dmodule-analogy-not-mechanism.md).
- Frontier: [`2026-08-02-deltalambda-graded-concentration-frontier.md`](2026-08-02-deltalambda-graded-concentration-frontier.md) (PR #4581).
