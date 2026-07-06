# Audit: N_⊙ construction (sub-problem 1) — n-stability selects the bare count

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Builds on.** [`2026-05-31-casimir-xi-2-reconciliation.md`](2026-05-31-casimir-xi-2-reconciliation.md)
**Witness.** [`casimir-n-unknot-construction.witness.json`](../../computations/casimir-n-unknot-construction.witness.json)
**Result.** A **conditional** construction of the N_⊙ mode-count functional. A
principled selection criterion — **n-stability** — uniquely picks the bare
disjoint-unknot count, which fixes **ξ_k = 0 at leading 1/d⁴ order** and
**derives the π²/720 prefactor**, *conditional on* the free-field ↔
disjoint-unknot identification.

## Why this is not a fourth flip

The reconciliation doc retracted "ξ_2 = 0" to **OPEN, gated on the N_⊙
construction**. This audit *attempts that construction* (the user's explicit
ask) and reports what it forces. It is framed **conditionally**: it identifies
the precise modeling assumption that would settle ξ_2, and derives the
consequence. It does **not** restore the over-broad "Casimir isn't Hecke"
closure — it *refines* it (see below).

## The missing ingredient: a selection principle

The 5-source survey failed because it had **no principle** to pick one candidate
trace functional over another — five sources gave five values spanning a factor
~32. The reconciliation showed the value of ξ_2 is *entirely fixed* by which
functional N_⊙'s mode-count is. So the construction reduces to: **what selects
the functional?**

**n-stability.** The Casimir prefactor is a single physical number. A mode-count
functional whose substrate-deviation depends on the mode-cutoff n is therefore
**inadmissible** — an observable cannot depend on where you truncate the mode
tower. Testing the candidates on the n-component vacuum (witness, `dps=50`):

| n | bare count | Jones δ^{n−1} | unnorm. Σ y_λ | norm. trace |
|---|---|---|---|---|
| 2 | 0.000 | 0.031 | 0.000 | 1.000 |
| 3 | 0.000 | 0.062 | −0.944 | 1.000 |
| 4 | 0.000 | 0.094 | −2.233 | 1.000 |
| 5 | 0.000 | 0.125 | −3.787 | 1.000 |
| 6 | 0.000 | 0.156 | −5.506 | 1.000 |
| 7 | 0.000 | 0.188 | −7.203 | 1.000 |
| 8 | 0.000 | 0.219 | −8.910 | 1.000 |

(values = relative h²-coefficient of each functional's substrate deviation;
δ = q^{1/2}+q^{−1/2} is the quantum dimension.)

- **Bare component count** N(n) = n: q-independent → **n-stable, admissible, unique.**
- **Jones of the n-unlink** δ^{n−1}: rel-h² ∝ (n−1) (slope ≈ 0.0312) → **diverges → inadmissible.**
- **Unnormalized Wenzl sum** Σ_λ y_λ(q): rel-h² diverges → **inadmissible.**
- **Normalized Markov trace** Σ_λ y_λ·dim ≡ 1: constant for *any* identity → **content-free.**

Among non-trivial functionals, **n-stability uniquely selects the bare count.**

## The free-field ↔ disjoint-unknot identification

Why is the bare count the *physical* functional? Maxwell is **linear**: photon
vacuum modes are non-interacting, hence **unbraided** = disjoint unknots.
Disjoint unknots carry `linking_weight = 1` (Hoefsmit-additivity probe, cited in
the block) and **no y_λ weighting** — they are not an n-strand braid closure but
n separate 1-strand closures, so the `H_n(q)` partition machinery does not even
apply. The ε-vacuum axiom then gives

$$
\mathrm{Geom}_\varepsilon(N \cdot \unicode{9737}) = N \cdot \varepsilon / \hbar^2_q,
\qquad N = \text{bare count},
$$

which is exactly the n-stable functional. **This is a modeling identification
(well-motivated by Maxwell linearity), not a QOU theorem** — it is the residual
open assumption.

## The prefactor (sub-problem 3) falls out

Under the disjoint count with the geometric per-level degeneracy ∝ n³ (the
k_⊥-integral of the free-field mode energy), the ζ-regularized mode tower gives

$$
\underbrace{\frac{\pi^2}{6}}_{k_\perp \text{ integral}} \cdot
\underbrace{|\zeta(-3)|}_{\text{n-sum} = 1/120} \;=\; \frac{\pi^2}{720},
$$

verified exact to 40 digits (witness assertion `prefactor_pi2_over_720_from_disjoint_count`).
**q appears nowhere**; the textbook energy prefactor is derived with no Hecke
`y_λ`. This is the first derivation of the π²/720 prefactor from QOU primitives
(sub-problem 3 was previously "hard, not proved").

## Conditional conclusion

$$
\boxed{
\begin{aligned}
\textbf{IF } &\text{(free-field} \leftrightarrow \text{disjoint-unknot identification)} \\
\textbf{AND } &\text{(n-stability admissibility of the mode-count observable)} \\
\textbf{THEN } &\xi_k = 0 \ \forall k \ge 1 \text{ at leading } 1/d^4 \text{ order, and } \pi^2/720 \text{ is derived.}
\end{aligned}
}
$$

**Where q-corrections actually live.** A non-zero ξ_2 requires **braided** modes
= field **interactions** = QED loops. These live at the subleading **1/d⁶** order
(the 1-loop QED correction to Casimir), a *different* coefficient in a *different*
expansion — **not** ξ_2 of the leading 1/d⁴ term. This is the precise sense in
which the retracted "Casimir isn't Hecke at ANY order" closure over-reached:
Casimir **is** in the knot framework, as disjoint unknots, whose trace functional
is the trivial count; q-deformation re-enters only when modes braid.

## Status after this audit

| Sub-problem | Before | After |
|---|---|---|
| 1 (existence of N_⊙) | Open | **trace functional identified** (bare count, via n-stability) under the free-field model; full Yekutieli-homotopy lift still open |
| 2 (A/d³ scaling) | Derived at rank 0 | unchanged |
| 3 (π²/720 prefactor) | Hard, not proved | **DERIVED** under the disjoint model: (π²/6)·ζ(−3) |
| 4 (ξ_k, k ≥ 1) | OPEN | **= 0 at leading order, conditional** on the free-field ↔ disjoint identification; first q-correction relocated to 1/d⁶ (QED-loop) order |

## What remains genuinely open

1. **The free-field ↔ disjoint-unknot identification.** This is the one residual
   assumption. Proving it from a QOU axiom (rather than asserting it from Maxwell
   linearity) would make the leading-order ξ_k = 0 unconditional.
2. **The full Yekutieli-homotopy lift** of the plate-bounded link-projection
   functor — the rigorous categorical object N_⊙(A,d). The selection principle
   identifies *which* functional it must reduce to; constructing it is the
   formalization layer.
3. **The 1/d⁶ q-correction.** If braided (interacting) modes are the right model
   for the subleading term, QOU predicts a *specific* q-dependent 1/d⁶ coefficient
   — a falsifiable next target, distinct from the (vanishing) leading ξ_2.

## Proposed block update (NOT yet applied — awaiting author sign-off)

The conjecture block currently lists sub-problem 3 as "hard, not proved" and
sub-problem 1 as "not started". This audit would justify softening both to
"prefactor derived under the disjoint model" and "trace functional identified
via n-stability". Because this re-touches a coefficient that just went through a
flip-flop, **the block edit is deferred until the author confirms** the
conditional framing is acceptable.
