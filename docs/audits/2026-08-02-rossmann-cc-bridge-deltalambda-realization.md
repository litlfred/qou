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

**Update (2026-08-02, Green-function corpus read).** The natural attempt to
*force* the open identification — via Springer's Green functions — **fails**: the
substrate weight `y_λ` is the **q-Plancherel measure** `dim_q²(λ)/[n]_q!`, not a
Green function, and the substrate's only graded object is the **fake degree**,
which is exactly #4581's *cancelling* `H_λ`. The single-degree concentration is
therefore an **external theorem of Springer geometry the framework imports**, not
a gap the 13 drivers can close. See §"The Green-function route also fails" below.

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

## The Green-function route also fails (corpus read, 2026-08-02) — (IDENT) is not forceable from the substrate weights

Springer 1976's title names *Green functions*, so the natural "force (IDENT)"
attempt is: are the substrate's `y_λ(q)` weights the Green-function values that
Springer's construction feeds into the graded Weyl-representation? **They are
not.** Two corpus reads settle it:

1. **`y_λ` is the q-Plancherel weight, not a Green function.** The corpus
   ([`observations/q-plancherel-asymptotic-skeleton.md`](../../content/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md))
   defines the Markov-trace weight as `ỹ_λ = dim_q²(λ) / [n]_q!` — the
   **Kerov–Vershik/Biane q-Plancherel measure** on partitions. Green functions
   `Q^λ_μ(q)` are the transition matrix between the Springer-graded characters
   and the class functions on unipotent classes; they are indexed by a *pair*
   `(λ, μ)` and are not a single per-partition weight. The substrate has the
   *measure*, not the *transition kernel* — the Springer-geometry input is
   simply not present in `tr_M = Σ_λ y_λ χ_λ`.

2. **The framework's only graded object is the fake degree — exactly #4581's
   cancelling `H_λ`.** The dimension polynomial `dim_q(λ)` that appears in `y_λ`
   is the principal-specialisation fake degree; its `q → -1` (grade-parity)
   evaluation spreads `V_λ` over both parities and cancels to `f_λ(-1) < dim`,
   which is *precisely* the cancellation obstruction PR #4581 proved. So the one
   graded object the substrate actually carries is on the **wrong side** of the
   #4581 dichotomy — it is a genuine algebraic grading, hence cancelling, hence
   *not* the single-parity characteristic cycle (IDENT) requires.

**Consequence — the concentration is proved EXTERNAL, not merely open.** The
single-degree concentration `V_λ = H^{2n(λ)}(𝓑_λ)` is a theorem of *Springer
geometry* (top-cohomology vanishing on the Springer fibre), and it is **not
reachable from the substrate weights** `y_λ`: the substrate supplies the
q-Plancherel measure and the (cancelling) fake-degree grading, neither of which
is the Green-function/characteristic-cycle datum. This is a **positive external
input the framework consumes**, not a formalization gap the framework can close
from its 13 drivers. (IDENT) is therefore not "open pending more work on the
archimedean functor" — it is an *import of external Springer geometry*, which is
the honest status the arc has held all along.

## Verdict

**Conditional candidate mechanism, not a derived result — and the conditioning
input is now shown to be EXTERNAL, not internally forceable.** The Rossmann
characteristic-cycle bridge is the *first* candidate that escapes the #4581
cancellation obstruction (it is not an algebraic grading — it is a microlocal
cycle), and it composes cleanly with #4581's proved single-parity saturation.
But it is gated on **(IDENT)**, and the Green-function corpus read above shows
(IDENT) is **not forceable from the substrate weights**: `y_λ` is the
q-Plancherel measure, not a Green function, and the substrate's only graded
object is the cancelling fake degree. Reported as **scope (a) / conditional**,
no `DeltaLambdaDTRealization` instance fabricated, nothing wired to production.

The honest next step is therefore settled in the negative: **(IDENT) cannot be
*forced* from the archimedean-functor construction** — the substrate weights do
not carry the Springer Green-function/characteristic-cycle datum. The
single-degree concentration is an **external theorem of Springer geometry the
framework imports**, sitting under the standing microlocal-is-analogy guard. The
`Δ_λ` **value** stays fully substrate-derived (the proved arc); the **geometric
concentration** that names it a Behrend-signed DT count is external input, not a
closure the drivers can reach. This is language, per the 2026-06-09 guard.

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
