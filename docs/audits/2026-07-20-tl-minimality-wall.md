# TL-minimality — what [Tr4] L3.1–3.3 prove, and why full minimality is a wall

Bean `qou-jshd`; branch `claude/qlift-borel-kernel-derivation-2026-07-20`.
Companion Lean: `content/quantum-observable-universe/lean/QOU/Machinery/AJMinimality.lean`
(verified `lean`-direct exit 0, sorry-free). Closes the last-open-hypothesis
question of NT-T4's `TransferLemmas.minimality`.

## What [Tr4] = arXiv:1404.0331 (Tran) Lemmas 3.1–3.3 actually prove

Tran, "The strong AJ conjecture for cables of torus knots." The strong-AJ proof
is by two ideal (radical) inclusions:

- **Lemma 2.1** — AJ-holds + no non-trivial M-factors ⟹ `√ε(A^σ_K) ⊂ p`.
- **Lemma 2.2** — `∃ P ∈ A^σ_K` with `ε(P) = M^k L^l (A_K)^{2m}` ⟹ `p ⊂ √ε(A^σ_K)`.
- **Lemma 2.3** — *construction*: given `h₁,…,h_k ∈ R[t^{±2n}]`, there **exists**
  `P ∈ R[L^{±1}]`, σ-invariant, `ε(P) = (L+L⁻¹−2)^m`, with `P·hᵢ = 0`.

§3 (case `s` odd, `q > 2`) then:

- **Lemma 3.1** — for the *torus* knot `T(p,q)`:
  `(L^{2m} − t^{-4pqm²}M^{-2pqm}) J_T ∈ R[M^{±1}]` for all `m > 0` (powers of the
  base recurrence still land in the coefficient ring).
- **Proposition 3.2** — explicit σ-invariant `P₁,P₂` with `PᵢGᵢ ∈ R[M^{±1}]`
  for the cable pieces `G₁,G₂`.
- These assemble (via Lemma 2.3) into `R ∈ A^σ_C` with
  `ε(R) = M^{k}L^{l}(A_C)^{2k}`, which feeds **Lemma 2.2**.

## Why this does NOT discharge `minimality`

**1. [Tr4] L3.1–3.3 are an annihilator *construction* (existence), not a
minimality theorem.** They build a specific, high-degree, **non-minimal**
σ-invariant element to feed the radical inclusion. No operator is ever shown to
be minimal-degree. Tran's route lives entirely at the level of radicals of
σ-invariant ideals (`√ε(A^σ_K) = p`); it never establishes that the recurrence
ideal is **principal**. Principality/minimality is the content of the *plain* AJ
conjecture (Garoufalidis's recurrence polynomial = minimal-order generator),
which Tran **assumes** (Lemma 2.1: "Suppose the AJ conjecture holds for `K`").

**2. [Tr4] §3 is about *cables of torus knots*, not `4₁`.** The figure eight is
hyperbolic — neither a torus knot nor a cable of one — so these lemmas do not
literally apply. The figure-eight paper reuses the *method* (build a σ-invariant
annihilator, feed Lemma 2.2), not these statements. The `TransferLemmas.minimality`
docstring citation "[Tr4, L3.1–3.3]" is therefore a **mischaracterization**:
minimality is the plain-AJ input, not what these transfer lemmas provide.

## The wall

`TransferLemmas.minimality` (`Â_hom` is the minimal-order nonzero annihilator)
is, at the concrete function-model level, `NoLowOrderHomogAnnihilator q`:

> no nonzero order-≤2 **homogeneous** operator `(c₀,c₁,c₂)` annihilates the `4₁`
> colored-Jones tower.

For `4₁` this is TRUE (its recurrence polynomial / minimal homogeneous annihilator
has order 3; the well-known order-2 recurrence is *inhomogeneous*). But a proof
requires ruling out **all** order-≤2 `R[M^{±1}]`-coefficient recurrences — the
holonomic-rank / A-polynomial-L-degree fact. That needs either:

- the **A-polynomial of `4₁`** via the SL₂(ℂ) character variety of the knot
  complement / skein-module theory, or
- a **q-holonomic-rank** (Wronskian / creative-telescoping minimality) argument
  over the quantum torus.

**Neither exists in Mathlib 4.24 or the corpus.** There is no character variety,
no A-polynomial, no skein module, no q-holonomic-rank framework. So full
minimality is a genuine wall — NOT axiomatized here (anti-laundering red line).

## Smallest honest formalizable reduction (landed sorry-free)

`AJMinimality.lean` reduces the wall to the single sharp premise
`NoLowOrderHomogAnnihilator q` and proves the two NECESSARY ingredients:

- **`hc3_ne_zero` (order-exactness).** `Â_hom`'s `L³` coefficient
  `hc3 = −feRhs·feCoeff₂` is nonzero at generic `q` — so `topDeg Â_hom = 3`, the
  reference degree minimality is stated against (not a disguised lower order).
  `coeffAt_ajHomElement_three` confirms `hc3` IS that leading coefficient.
- **`figureEight_not_homogAnnihilator` (order-2 obstruction).** The order-2
  figure-eight triple is **not** a homogeneous annihilator (it hits `feRhs ≠ 0`,
  not `0`) — the concrete reason order 3 is forced, ruling out the naive candidate.
- **`minimal_order_gt_two_of_noLowOrder`** — the logical reduction: given
  `NoLowOrderHomogAnnihilator`, the minimal homogeneous order is `> 2`; with
  `ajHomElement_annihilates` (order-3, corpus-proved) that pins it at exactly 3.

These rule out one candidate and fix the order; the residual `NoLowOrder…`
(all candidates) is the wall. No `TransferLemmas` instance is provided.

## Bottom line — how close is NT-T4 to unconditional strong-AJ

Three inputs to `strong_aj_figure_eight_of_transfer`: `aj_mem` (corpus-PROVED
order-3 `ajHomElement_annihilates`, module-bridge untranslated), `division` (B3
`exists_skew_right_division`, sorry-free per 2026-07-20 update), and `minimality`
(**this wall**). Two of three are proved/reducible; `minimality` needs the
A-polynomial / holonomic-rank machinery Mathlib lacks. NT-T4 strong-AJ therefore
remains **honestly conditional** — the conditional theorem is real, the last
premise is a genuine external-math wall, not laundered.
