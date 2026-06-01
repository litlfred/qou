# Audit: the free-field ↔ disjoint-unknot identification is established QOU, not an assumption

**Date.** 2026-06-01
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Builds on.** [`2026-05-31-casimir-n-unknot-construction.md`](2026-05-31-casimir-n-unknot-construction.md)
**Result.** The lone residual assumption of the N_⊙ construction — the
*free-field ↔ disjoint-unknot identification* — is **not a new modeling
ansatz**. QOU already represents the free EM field (photon) as the identity
braid whose closure is disjoint unknots. The conditional `ξ_k = 0` result
therefore reduces to established QOU content; the only genuinely-physical
input is "the Casimir effect is a free-field phenomenon", which is standard.

## The gap this closes

PR #1540's construction ([N_⊙ audit](2026-05-31-casimir-n-unknot-construction.md))
showed: under the free-field ↔ disjoint-unknot identification, the *n*-stable
mode-count functional is the bare disjoint-unknot count (no `y_λ`), which
forces `ξ_k = 0` at leading 1/d⁴ order and derives π²/720. That audit flagged
the identification itself as "a modeling statement (well-motivated by Maxwell
linearity), not a QOU theorem" — the one open lever.

It is not open. QOU's existing content already makes the identification.

## Established QOU content grounding the identification

1. **Photon = identity braid, no crossings.**
   [`rem:trivial-knot-photon-interpretation`](../../content/quantum-observable-universe/brings-surface/trivial-knot-photon-interpretation.md):
   the trivial knot operator has braid word β = 𝟙, so a photon process is the
   raw Hecke product "with **no crossings inserted**." A free photon carries no
   braiding.

2. **Photon closure = disjoint unknots.**
   [`prop:recursive-atom-knot-atlas`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.md):
   the photon γ is `T_w = 𝟙_{B_4} ∈ H_4(q_0)` with closure `ŵ = 4·0_1` — four
   disjoint unknots (one per polarisation × chirality component). The notation
   legend states `𝟙_{B_n}` = "identity element of B_n (no crossings); Markov
   closure = n disjoint unknots."

3. **Degree-≤1 closures carry no substrate-q deformation.**
   [`lem:degree-one-braid-trivial-volume`](../../content/quantum-observable-universe/mass-theory/degree-one-braid-trivial-volume.md):
   the n-component unlink and each single-crossing closure are non-hyperbolic,
   so `Vol = 0`; "mass generation requires a closure that is genuinely
   hyperbolic, which forces the braid word to have degree ≥ 2 in the generators
   σ_i, σ_i^{-1}." Free (degree-≤1) configurations transmit no q-deformation
   through the Vol pipeline.

These three are the standing QOU statement that **free ↔ identity braid ↔
disjoint unknots ↔ no q-deformation**, and **interacting ↔ crossings (σ_i) ↔
degree ≥ 2 ↔ hyperbolic / q-deformed**. (The broader "interactions ↔ braid
crossings" principle is foundational from
`braids-and-knots/intro.md` onward: "particle interactions correspond to the
action of braid operators … encoded in braid-group representations rather than
in Feynman vertices.")

## The reduction

$$
\begin{aligned}
&\text{Casimir is a \textbf{free} EM-field vacuum effect (standard physics; no QED vertices at leading order)} \\
\Rightarrow\ &\text{each photon mode} = \text{identity braid} \;\;[\text{rem:trivial-knot-photon-interpretation}] \\
\Rightarrow\ &\text{closure} = \text{disjoint unknots} \;\;[\text{prop:recursive-atom-knot-atlas}] \\
\Rightarrow\ &\text{vacuum} = \text{disjoint union of mode-photons; no inter-mode braiding} \\
\Rightarrow\ &\text{mode-count functional} = \text{bare count (no } y_\lambda) = \text{the } n\text{-stable functional [PR \#1540]} \\
\Rightarrow\ &\xi_k = 0 \ \ (k \ge 1) \text{ at leading } 1/d^4; \quad (\pi^2/6)\,|\zeta(-3)| = \pi^2/720 \text{ derived.}
\end{aligned}
$$

The chain no longer rests on a new assumption. Step 1 is standard physics
(Casimir is a free-field effect). Steps 2–4 are **cited** QOU content. The
result is a derivation of `ξ_k = 0` at leading order modulo only the
already-formalised photon representation and the *n*-stability admissibility
criterion.

## Where q-corrections live (consistency check)

`lem:degree-one-braid-trivial-volume` says q-deformation (mass, hyperbolic
volume) requires **degree ≥ 2** braid words — i.e. crossings, i.e.
interactions. The first q-correction to Casimir therefore sits at the
interacting-mode order: the 1/d⁶ QED-loop term, exactly as the N_⊙ audit
predicted. The vanishing of `ξ_2` on the leading 1/d⁴ term and the appearance
of q-dependence only at 1/d⁶ are the **same statement** as "free = degree ≤ 1 =
Vol 0; interacting = degree ≥ 2 = hyperbolic" — full internal consistency.

## Status after this audit

| Sub-problem | Before (PR #1540) | After |
|---|---|---|
| 1 (existence of N_⊙) | trace functional identified via *n*-stability, under a *modeling* identification | identification **grounded in established QOU photon representation**; only the Yekutieli-homotopy lift (the explicit categorical object) remains |
| 3 (π²/720 prefactor) | derived under the disjoint model | unchanged — derivation now rests on cited content, not an ansatz |
| 4 (ξ_k, k ≥ 1) | = 0 at leading order, conditional on the identification | = 0 at leading order, the identification reduced to cited QOU content; first q-correction at 1/d⁶ |

## What remains genuinely open

1. **The Yekutieli-homotopy lift** — the explicit categorical object N_⊙(A,d).
   The selection principle + the photon representation fix *what it must reduce
   to* (a disjoint-unknot count); building the lift is the formalisation layer.
2. **The 1/d⁶ q-correction** — now a sharply-posed target: it is the
   degree-≥2 (interacting-mode) contribution, a *specific* q-dependent
   coefficient, distinct from the vanishing leading `ξ_2`.

## Caveat

This is a reduction, not a new Lean proof. It shows the identification is
already QOU's stance (photon = identity braid) rather than a fresh assumption.
The one non-cited input — "the Casimir vacuum tower is built from free photon
modes" — is standard physics, not a QOU-specific claim, and is the appropriate
place for the physical content to enter.
