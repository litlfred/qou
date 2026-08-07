---
# qou-b7cy
title: 'Route 9: Bloch torsion at ℚ(ζ₇)⁺ makes the 5₂ sum rule a RATIONALITY statement'
status: in-progress
type: task
priority: high
tags:
    - qbeta
    - dilogarithm
    - 5two
    - bloch-group
    - reduction
created_at: 2026-08-07T17:05:00Z
updated_at: 2026-08-07T17:05:00Z
parent: 0yqu
---


## Result: the rationality is PROVED. One rational number is left.

Route 6 hoped the open problem "would stop being a transcendental evaluation and
become a rationality statement", and failed. **That is now achieved**, by a
different mechanism, off the back of Route 8's transport (`qou-8v3k`).

Probe `computations/probes/qbeta_5two_route9_bloch_torsion_rationality_probe.py`,
witness `computations/qbeta-5two-route9-bloch-torsion-rationality.witness.json`,
6 gates at 40 dps, all pass.

## Setup

Route 8 reduced the sum rule to the totally real cyclotomic point. Put
`w := −y = 1 + 2cos(2πk/7)`, so `V(−1,y) = 2Li₂(w) + Li₂(−w) + log²w`, and the
target is `Σₖ Re V = −π²/2`.

`w` is a root of **`w³ − 2w² − w + 1 = 0`**, and

    N(w) = −1,     N(1−w) = −1,     N(1+w) = +1

so **`w`, `1−w`, `1+w` are all units** of `F = ℚ(ζ₇)⁺`.

## The algebraic key — a ring identity, hence a Lean one-liner

    (1 − w)²·(1 + w)  =  1 − w − w² + w³  =  w²        using   w³ = 2w² + w − 1

Therefore, for `ξ := 2[w] + [−w] ∈ ℤ[F]`,

    δ(ξ) = 2·(w ∧ (1−w)) + ((−w) ∧ (1+w)) = w ∧ [(1−w)²(1+w)] = w ∧ w² = 0

in `∧²F* ⊗ ℚ` (the torsion `−1` dies on tensoring). **So `ξ` lies in the Bloch
group `B(F)`.** This is elementary and fully formalizable — `ring` plus the
minimal polynomial.

## The classical input

`F = ℚ(ζ₇)⁺` is **totally real**, so `r₂ = 0` and by Borel `B(F) ⊗ ℚ = 0`: every
element of `B(F)` is torsion. The Rogers dilogarithm carries Bloch torsion into
`π²ℚ`. Hence

    Σ_σ L(σ(ξ)) ∈ π²ℚ           ← the rationality, PROVED modulo that theorem

## The measurement

    Σₖ Re[2L(wₖ) + L(−wₖ)] = π²/2       exactly, to 26 digits   (G5)
    Σₖ Re V = Σₖ Re L(ξₖ) − π²          exactly                 (G6)

giving `Σₖ Re V = π²/2 − π² = −π²/2` ✓, which is Route 8's target and hence the
sum rule.

## ⚠ What is NOT proved

1. **That the rational is exactly `1/2`.** Rationality is proved; the value is
   verified to 26 digits, not derived. Note `π²/2 = 3·L(1)`, which is a
   suspiciously clean value for a 3-embedding trace and is probably the tell for
   an explicit five-term / Y-system derivation.
2. **The `−π²` branch constant in G6.** A per-embedding formula
   `V − L(ξ) = iπ·log[(1−w)/w]` was tried and **is FALSE** — it fails at two of
   the three embeddings on branch grounds; only the *sum* comes out exact. That
   bookkeeping still needs doing properly, and the failed attempt is recorded so
   nobody re-derives it.
3. Nothing here is Lean. Toolchain unavailable in this environment (`qou-clx8`).

## Why this is nevertheless the qualitative step

Every earlier route died on *real part vs volume side*. The chain is now:

    sum rule  --Route 8-->  cyclotomic identity at Q(zeta_7)+
              --Route 9-->  L(xi) for xi in B(F), F totally real
              --Borel-->    L(xi) in pi^2 Q
              --???-->      L(xi) = pi^2/2

Only the last arrow is open, and it is a **rational-number** question, not a
transcendence question. That is a different kind of problem from the one this
bean started with.

## Next step

Pin `1/2`. Two concrete options:

1. **Explicit five-term derivation.** Use the Rogers duplication
   `L(z²) = 2L(z) + 2L(−z)` to rewrite `2L(w) + L(−w) = L(w) + ½L(w²)`, then
   exploit `w² = (1−w)²(1+w)` — exactly the shape that generates Y-system
   dilogarithm identities. **Not attempted.**
2. **Torsion order.** Compute the order of `ξ` in `B(F)` (equivalently the order
   of the relevant class); torsion of order `n` bounds the denominator, and a
   finite check then pins the numerator.

## Refs

* parent `qou-0yqu`; builds on `qou-8v3k` (Route 8)
* siblings `qou-r7ml` (Route 7, refuted), `qou-g2wr` (literature closed)
* PR #4658
