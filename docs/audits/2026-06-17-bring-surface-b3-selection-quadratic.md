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
  `z₀ = √q₀ − 1/√q₀ ≈ 0.104` on the color fibre `𝓔_q`.

**Conjecture:** `𝓑₃` is the minimal-energy configuration of the **Bring-surface
quadratic** (period / polarization / Levi form on `H¹(Bring)=2W`, equivalently
the q-heat-kernel / Stokes action) evaluated at `z₀` — *not* of the Hecke Gram.

## Plan

1. Identify the Bring-side quadratic — candidates: `intrinsic-color-cubic-pairing`,
   `levi-form-defect`, `descartes-elliptic-curve` (period form), `color-elliptic`.
2. Identify the knot ↔ Bring map — candidate: `descartes-knot-eigenbasis`,
   `knot-basis-color-content`.
3. Evaluate the quadratic at `z₀`; test whether its minimal-energy operator maps
   to `NF(𝓑₃) = (0.998, −0.01, 0.009, 0.046, −0.044, 0)`.
4. Derive-or-refute. Record the honest outcome (this doc).

## Findings — the ingredients exist; the *selection* bridge does not

**1. The Bring-surface quadratic EXISTS — in two convergent forms.**

- **Color quadric** `h₂(c) = σb + rg` ([`color-tube-constraints`](../../content/quantum-observable-universe/brings-surface/color-tube-constraints.md)).
  Its shifted, q-dependent form is `h₂(c) + z·p₁(c) + 2z² = 0` (`z = √q−1/√q`),
  i.e. `σb + rg = −z(σ+r+g+b) − 2z²`. As a form on `(σ,r,g,b)` it is
  **indefinite, signature (2,2)** (eigenvalues `±½` each twice), pairing
  `(σ,b),(r,g)` — the same skip-one `w_k↔w_{5−k}` conjugation as
  [`intrinsic-color-cubic-pairing`](../../content/quantum-observable-universe/brings-surface/intrinsic-color-cubic-pairing.md),
  and indefinite *like* the Hecke Gram.
- **Non-abelian Stokes curvature** ([`yekutieli_borromean_h2_extraction.py`](../../computations/yekutieli_borromean_h2_extraction.py)):
  the Hecke quadratic relation **is** the Stokes 2-form, `F_i = σ_i²−1 = h·σ_i`.
  The h²- (quadratic-) order action of the Borromean braid `(σ₀σ₁⁻¹)³ = 𝓑₃` is
  **κ = 3/16 exactly** (mpmath.identify; `tr_M(𝓑₃,q₀)=1.00673`). *(Byproduct:
  this refutes that script's `κ = −G` Catalan/volume conjecture — `3/16 ≠
  0.916`.)*

**2. The knot↔color map EXISTS but is partial.**
[`knot-basis-color-content`](../../content/quantum-observable-universe/brings-surface/knot-basis-color-content.md)
makes a Hecke element a "photon with color content"
`γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` — **the NF coefficients ARE the color
content**. And `𝓑₃ ↔` the Borromean-rings Jones polynomial
`V(t)=−t⁻³+3t⁻²−2t⁻¹+4−2t+3t²−t³`. The categorical bridge
([`descartes-knot-eigenbasis`](../../content/quantum-observable-universe/brings-surface/descartes-knot-eigenbasis.md))
is `Rep(SU_q(2))` at the Descartes point `χ(A)=−6` (genus 4, rank-2),
braiding eigenvalues `q,−q⁻¹`.

**3. The SELECTION claim ("𝓑₃ minimizes the Bring quadratic at z₀") has NO clean
realization — REFUTED as stated.**

- The quadric `h₂` lives on the **4-color** space `(σ,r,g,b)`; the operator
  selection (the Gram / LP) lives on the **6-NF** space
  `{γ,σ₀,σ₁,L₊,L₋,e⁻}`. The `knot-basis-color-content` map carries only the
  3 color-content parameters `(φ₀,φ₁,φ₀₁)` — it is **not** a 1-1 identification
  of the two spaces, so there is no single quadratic form on one space to
  minimise.
- The existing Stokes/Yekutieli compute extracts the quadratic **action value**
  of `𝓑₃` (`κ=3/16`), **not** a quadratic *form whose minimiser is `𝓑₃`*.
  "Action of 𝓑₃" ≠ "form that selects 𝓑₃".

## Verdict (derive-or-refute)

The owner leads were **right that the quadratic and the q₀-geometry are real**
(the `h₂` quadric, the Stokes curvature, the color-content map, `𝓑₃`'s clean
`3/16` action all exist and converge). But the specific conjecture — *`𝓑₃` is
the minimal-energy configuration of a Bring quadratic at `z₀`* — **does not have
a realization**: the quadric and the operator-selection live on different spaces
(4-color vs 6-NF), connected only by a partial (3-parameter) color-content map,
and the existing quadratic compute gives `𝓑₃`'s *action*, not a *selection*. So
the bridge from "quadratic **action of** 𝓑₃" to "quadratic that **selects**
𝓑₃" is the genuinely unbuilt piece. Building it = constructing a 1-1
NF↔color(W-plane) identification under which `h₂`/Stokes restricts to the Gram —
a real categorical construction, **not** a numerical test runnable today, and
**not** a fit.

**Net:** the Δ_λ master-formula route's `𝓑₃`-selection gate is *not* closed by
the Bring quadratic as hoped; it is reduced to one sharp, formalizable
sub-problem (the NF↔color identification). Clean side-result: `𝓑₃`'s
non-abelian-Stokes h²-action `= 3/16` (exact).

## Cross-links
- [`2026-06-17-delta-lambda-master-formula-active-set-redesign.md`](2026-06-17-delta-lambda-master-formula-active-set-redesign.md) — the parent Δ_λ route + the LP/quadratic refutations (#2405).
- [`color-tube-constraints`](../../content/quantum-observable-universe/brings-surface/color-tube-constraints.md) — the `h₂` quadric + shifted forms.
- [`yekutieli_borromean_h2_extraction.py`](../../computations/yekutieli_borromean_h2_extraction.py) — Stokes curvature h²-action (`κ=3/16`).
- [`knot-basis-color-content`](../../content/quantum-observable-universe/brings-surface/knot-basis-color-content.md) — NF coeff ↔ color content (the partial map).
