# Does a Bring-surface quadratic select 𝓑₃? (investigation, 2026-06-17)

**Branch:** `claude/delta-lambda-bring-quadratic-2026-06-17`
**Picks up:** the Δ_λ master-formula-route open item from
[`2026-06-17-delta-lambda-master-formula-active-set-redesign.md`](2026-06-17-delta-lambda-master-formula-active-set-redesign.md)
(merged in #2405). **Discipline:** exploratory; derive-or-refute; **no fit, no
production rewire.**

## The conjecture under test (owner leads, 2026-06-17)

The cooperative-binding (Δ_λ) gate routes through the confinement master formula
`⟨O⟩_T = Σ_{i,j∈A*} u_i (G⁻¹)_{ij} ⟨O,b_j⟩`, which needs the bound state `T=𝓑₃`
to be **selected**. The #2405 investigation established, decisively:

1. The min-action **LP** does not select `𝓑₃` — its global min is the trivial
   `tr_M=0` state (the objective coincides with the `i=0` Frobenius row).
2. The naive **quadratic** (`min x^T G x` / min-|λ| eigenvector of the Hecke
   Gram) does not select `𝓑₃` either: Gram eigenvalues `[−0.855, +0.102,
   +0.855×4, +3.48]` (the Hecke `(q, −q⁻¹)` two-sign signature), but
   `NF(𝓑₃) ≈ (0.998, −0.01, …)` is ≈ pure identity `γ`, aligned with no
   eigenvector (`|cos|≈0.47`).

So **the selection principle is not internal to the Hecke Gram.** Two owner
leads assemble the alternative:

- **"Lots of quadratic things"** — q-heat kernel (q-Laplacian, eigenvalues
  `[j]_q[j+1]_q`), q-Bessel 2nd kind (its radial solution), the quadratic from
  non-abelian Stokes (Yekutieli: Markov trace = quadratic action integral over
  the braid-closure surface), the Hecke relation `σ²=(q−q⁻¹)σ+1`. These are one
  quadratic *action*, of which the Hecke Gram is the linearized shadow.
- **"q₀-specific ⇒ Bring's surface"** — the −0.855 eigenvalue and the
  `𝓑₃`-local-min are functions of `q₀`, so the principle should live where `q₀`
  is geometrically fixed: **H¹(Bring) = 2W** (rank-2 W-plane) at
  `z₀ = √q₀ − 1/√q₀ ≈ 0.104` on the coral fibre `𝓔_q`.

**Conjecture:** `𝓑₃` is the minimal-energy configuration of the **Bring-surface
quadratic** (period / polarization / Levi form on `H¹(Bring)=2W`, equivalently
the q-heat-kernel / Stokes action) evaluated at `z₀` — *not* of the Hecke Gram.

## Plan

1. Identify the Bring-side quadratic — candidates: `intrinsic-color-cubic-pairing`,
   `levi-form-defect`, `descartes-elliptic-curve` (period form), `coral-elliptic`.
2. Identify the knot ↔ Bring map — candidate: `descartes-knot-eigenbasis`,
   `knot-basis-color-content`.
3. Evaluate the quadratic at `z₀`; test whether its minimal-energy operator maps
   to `NF(𝓑₃) = (0.998, −0.01, 0.009, 0.046, −0.044, 0)`.
4. Derive-or-refute. Record the honest outcome (this doc).

## Status

Investigation opened. Findings below as they land.
