# The Jones–Markov weights ARE Webster–Williamson Molien series (n=3) — items 4/2 resolved, the correct normaliser found

**Date:** 2026-08-29 · **Beans:** `qou-sf1t` (Molien lead), `qou-3quc` (general-n) ·
**Status:** DERIVATION (exact, non-fit) for `n=3`; general `n` open · **Lean:**
[`QOU/QBeta/MolienJonesMarkovN3.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MolienJonesMarkovN3.lean)
(sorry-free) · **Probe:**
[`molien_jones_markov_n3_identification_probe.py`](../../computations/qbeta/molien_jones_markov_n3_identification_probe.py)
(exact ℚ(q,z), 6/6).

## Context

The 2026-08-21 lead
([`webster-williamson-molien-lead-for-equivariant-index.md`](2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md))
recognised that Webster–Williamson (*The geometry of Markov traces*,
`arxiv-0911.4494v2`) realise the Jones–Ocneanu trace weights as **Molien series**
`M_ν(u,t)` of the reflection representation, and named four verification items.
The 2026-08-22 note refuted the *guessed* closed form `y_λ = f^λ q^{−κ_λ}/[n]_q!`
— it had the wrong normaliser. This audit supplies the **correct** identification
for `n=3`.

## The two independently-computed objects

1. **Webster–Williamson `S₃` Molien series** (§6): with the reflection rep `𝔥`
   (2-dim standard), `E = Sym•(𝔥*) ⊗ ∧•(𝔥*)`,
   `M_ν(u,t) = Σ_{i,j} u^i t^j dim Hom_{S₃}(V_ν, Sym^i 𝔥* ⊗ ∧^j 𝔥*)`, computed by
   Molien `(1/6) Σ_g χ_ν(g) det(1+t·g)/det(1−u·g)`. (Verified: `t=0` gives the
   fake degrees `1, u+u², u³`; `u=0` gives the exterior powers `1, t, t²`.)
2. **Jones–Markov weights `y_λ(z)`** of the `H₃(q)` Markov trace, from the exact
   6-dim regular-rep character solve.

These share no inputs, so the match below is an identity, not a tautology.

## The derivation — the specialisation is FORCED (not fitted)

Eliminate the weight variable `t` from the Molien ratios `M_sign/M_triv`,
`M_std/M_triv`: the result is a **Molien conic**
`R₁R₂u + R₁u² + 2R₁u + R₁ − R₂²u² − R₂² + R₂u = 0`. Demand the three `y_λ`-ratios
lie on it. This is an **overdetermined** system — three coefficients in `z`, one
unknown `u` — and its **only** solution is the monomial

  `u = q²`   (and its bar `u = q⁻²`).

At `u = q²` the weight variable is forced, `t = q z/(q² − q z − 1)`, and then

  **`y_λ = M_ν(u=q², t) · Z`,   `Z = (q² − q z − 1)²`**

with **one common perfect-square normaliser** `Z`, identical for all three irreps
(`triv↔(3)`, `std↔(2,1)`, `sign↔(1³)`). `Z` is the **Poincaré/Molien** shape the
lead predicted — *not* `[n]_q!` — which is exactly why the 2026-08-22 guess (with
`[n]_q!`) failed: right family, wrong normaliser.

## Which lead items this resolves (for n=3)

- **Item 4 (weight family):** the Molien weights land on the **Jones–Markov `y_λ`**
  family — settled, not `w_λ(q)` or `w_λ(1)`.
- **Item 2 (specialisation):** `u = q²`, `t = q z/(q²−qz−1)` — exhibited and forced.
- **Item 1 (Tr_Γ = tr_M), weight-level half:** the geometric-trace weights equal
  `tr_M`'s `y_λ` — established for `n=3`. (The full trace-level identification of
  `Tr_Γ` with Jones–Ocneanu is the literature theorem; not re-proved here.)
- **Item 3 (type-A descent):** implicit — the computation is type A (`S₃`) at the
  weight level.

## Lean

[`MolienJonesMarkovN3.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MolienJonesMarkovN3.lean),
sorry-free, over a generic `CommRing`, certifies both halves as pure `ring`
identities: `nSign = molSignNum(q², qz/W)·W²` (the cleared Molien numerator) and
`ySignNum · molOneDimDen(q²) = yOneDimDen · nSign` (the cleared `y_λ = M_ν·Z`), and
likewise for `(3)` and `(2,1)`; capstone `jonesMarkov_weights_are_molien`.

## Honest scope

**`n = 3` only.** General `n` (`qou-3quc`) is the real prize and stays open — this
is one (strong, overdetermined, exact) data point. The pattern to test at `n=4`:
does the same monomial `u = q²` and a perfect-square normaliser `Z_n` reproduce
the `y_λ` from the general `S_n` Molien series? Nothing is wired; `free_parameters = 0`.

## Bearing on the cds1 wall

Modest and indirect. This identifies the `tr_M` *weights* with a bigraded Molien
object, which is the machinery the cohomological "different D construction" would
need. But it does **not** by itself supply a `D`-admissible functional reaching the
excluded `z=1` value — the specialisation here reproduces `tr_M` at general `z`,
not a new admissible object. It closes lead items 4/2, not the cds1 correction wall.
