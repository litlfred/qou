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

## General n (added 2026-08-29 — `qou-3quc`)

The identification generalises. Define, for every `n`, the `S_n` reflection-rep
Molien series `M_ν(u,t)` and

  **`y_λ(q,z) = M_ν(u=q², t=q z/(q²−qz−1)) · (1 + q z − q²)^{n−1}`.**

The normaliser is `Z_n = (1 + q z − q²)^{n−1}` — a power of **one** linear form
(the Poincaré/Molien shape, not `[n]_q!`). For `n=3`, `Z_3 = (1+qz−q²)² =
(q²−qz−1)²`, the even power in the theorem above; for `n≥4` the `1+qz−q²` sign is
load-bearing.

**Verified at `n=4`**
([`molien_jones_markov_general_n_probe.py`](../../computations/qbeta/molien_jones_markov_general_n_probe.py),
3/3), by checks independent of the `S₄` Molien side:

- Markov normalisation `Σ_λ f^λ y_λ = 1` — **exact symbolic** in `z`.
- at `z = z_D = q³/(q²+1)`: the `≥3`-row weights `y_(2,1,1)`, `y_(1⁴)` **vanish**
  (`~10⁻⁴³`) — the convention-D two-row cap emerges automatically — and the
  surviving `y_(4)`, `y_(3,1)`, `y_(2,2)` reproduce the corpus SU(2) quantum
  dimensions `y_lambda_su_n(4, q₀, 2)` to full precision (diff `< 10⁻¹⁴`).

## Honest scope

**Lean:** `n=3` and `n=4` are **both** now Lean-proved, sorry-free, general `z`.

- `n=3`: the exact identity `y_λ = M_ν·Z` (`MolienJonesMarkovN3.lean`).
- `n=4` (upgraded 2026-08-29): the **full** weight identity `y_λ^Molien =
  y_λ^Jones-Markov` (`MolienJonesMarkovN4.lean`, `n4_full_identity`). The missing
  ingredient — an *independent* general-`z` `H₄` weight — is supplied by **Wenzl's
  Schur-principal closed form** `s_λ = Q^{n(λ)}∏(1−R Q^c)/∏(1−Q^h)`,
  `R = qz/(1−q²+qz)` (no Molien input). The Molien weight *ratios* are proved
  (`ring`) to equal the Wenzl `ŝ_λ` ratios, and the Markov normalisation pins the
  scale ⇒ the two families coincide. The symbolic `(q,z)` equality
  `y_λ^Molien = y_λ^Wenzl` at n=3 and n=4 is checked exactly in
  [`molien_wenzl_weight_identity_probe.py`](../../computations/qbeta/molien_wenzl_weight_identity_probe.py).

The **∀n** Lean proof is a genuine formalisation project (abstract `S_n` Molien +
`H_n` Markov-weight machinery), tracked under `qou-3quc`. Nothing is wired;
`free_parameters = 0`.

## Molien → binding: the signed dimensions come from the SAME series (added 2026-08-29)

Probe:
[`molien_binding_signed_dimension_probe.py`](../../computations/qbeta/molien_binding_signed_dimension_probe.py)
(exact sympy, no float; S₃ + S₄ all pass).

The binding formula is `B = m_e · Σ_λ y_λ χ^λ Δ_λ` with the **proved** per-partition
signed dimension (2026-08-02, sorry-free, general-n,
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`):

  `Δ_λ = (−1)^{n(λ)} · dim V_λ`.

The weights `y_λ` live at the `(u=q², t=qz/(q²−qz−1))` corner of `M_ν(u,t)`. The
**binding signed dimensions live at the *other* corner** — the fake-degree edge
`t = 0`. Define the fake-degree polynomial

  `fd_λ(u) := M_ν(u, 0) · ∏_{i=2}^{n}(1 − u^i)`

(the graded multiplicity of `V_λ` in `Sym•(𝔥*)`, made a genuine polynomial by the
**full** coinvariant denominator — the `S_n` fundamental degrees `2,3,…,n`). Then

  `n(λ) = u-valuation (lowest u-degree) of fd_λ(u)`,   `dim V_λ = fd_λ(1)`,

so `Δ_λ = (−1)^{u-val fd_λ} · fd_λ(1)`. Verified exact at S₃ and S₄:

| λ | `fd_λ(u)` | u-val = n(λ) | fd_λ(1) = dim | Δ_λ |
|---|---|---|---|---|
| (3) | `1` | 0 | 1 | +1 |
| (2,1) | `u + u²` | 1 | 2 | −2 |
| (1³) | `u³` | 3 | 1 | −1 |
| (4) | `1` | 0 | 1 | +1 |
| (3,1) | `u + u² + u³` | 1 | 3 | −3 |
| (2,2) | `u² + u⁴` | 2 | 2 | +2 |
| (2,1,1) | `u³ + u⁴ + u⁵` | 3 | 3 | −3 |
| (1⁴) | `u⁶` | 6 | 1 | +1 |

Every `fd_λ` has non-negative integer coefficients summing to `dim V_λ` — the
genuine graded-multiplicity polynomial, not an artifact.

**Honest correction:** an earlier cut of this probe took the *reduced* numerator of
`M_ν(u,0)` and read `dim = fd(1)` off it — that is wrong (it gives `1` for every λ
because reduction cancels the coinvariant denominator into the numerator). The
u-valuation `= n(λ)` survives reduction, but `fd(1) = dim` needs the **unreduced**
fake degree `M_ν(u,0)·∏(1−u^{d_i})`. The table above uses the corrected form.

**What Molien buys for binding.** The *whole* `B = Σ_λ y_λ χ^λ Δ_λ` is one bigraded
Molien object `M_ν(u,t)` read at two specialisations: the weights `y_λ` from the
`(u=q², t=qz/W)` corner (this document's main result) and the signed dimensions
`Δ_λ` from the `(u, t=0)` fake-degree edge. It does **not** re-derive the binding
*magnitude* (the open `M_n(K)` extensive term is untouched); it unifies the two
already-known ingredients under one generating object. `∀n` stays open (`qou-3quc`).
Nothing wired; `free_parameters = 0`.

## Bearing on the cds1 wall

Modest and indirect. This identifies the `tr_M` *weights* with a bigraded Molien
object, which is the machinery the cohomological "different D construction" would
need. But it does **not** by itself supply a `D`-admissible functional reaching the
excluded `z=1` value — the specialisation here reproduces `tr_M` at general `z`,
not a new admissible object. It closes lead items 4/2, not the cds1 correction wall.
