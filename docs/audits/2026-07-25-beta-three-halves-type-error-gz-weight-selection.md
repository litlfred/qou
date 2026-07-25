# The `β = 3/2` failure is a type error — GZ weight-difference selection rule (2026-07-25)

**PR:** #4213. **Branch:** `claude/aomega-weight-selection-infra-2026-07-25`.
**Axis:** A_ω odd-channel Stokes constant / the "correct modular weight" question.

## The failure, and its cause

The corpus probe
[`qbeta_modular_resurgence_stokes_probe.py`](../../computations/probes/qbeta_modular_resurgence_stokes_probe.py)
(sub-test T2) tested a Borel loggamma exponent `β = 3/2` — inverting `(A, β)` from
the exact Ohtsuki κ-ladder via `κ_n ~ (S/π)·Γ(n+β)/A^{n+β}` — and it **failed**
(`β_inf ≈ 0.2–0.26`, far from `1.5`; recorded in
[`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
§2). A literature pass pins the cause: **`3/2` is a type error here.**

The `3/2` is the **Garoufalidis–Zagier modular weight `κ(σ₀)` of the trivial
connection** — the automorphy-factor exponent of the Kashaev `N^{3/2}` prefactor
(`⟨K⟩_N ∼ N^{3/2} e^{v N} Φ(2πi/N)`, GZ eq. 1.1; `κ(σ) = 3/2` iff `σ = σ₀`, else `0`,
GZ [2111.06645](https://arxiv.org/abs/2111.06645) eq. 3.7). It is **not** the
characteristic exponent of a single Borel singularity. The Borel exponent of a Stokes
ray joining connections `σ, σ′` is the **weight difference** `b = κ(σ) − κ(σ′)`.

## The correct structure (formalized in #4213)

The A_ω singularity sits at `ω = Vol(4₁)/π`, the **geometric↔conjugate** ray
(`σ₁ ↔ σ̄₁`, GGM [2007.10190](https://arxiv.org/abs/2007.10190)) — **both non-trivial,
both weight 0** — so its Borel exponent is the **integer `b = 0`**, and its Stokes
constant is the **integer** DT/BPS `3d`-index count `[q⁰] Ind^{rot}_{4₁} = 3` (GGM
Conj. 2). A value `b = ±3/2` can occur only on a `σ₀ ↔ (non-trivial)` ray — a
**different** singularity. So testing `β = 3/2` against the geometric–conjugate ladder
was a category error, and the observed `β_inf ≈ 0.2–0.26` is the finite-rung
Richardson signature of an integer `b = 0`, not of `3/2`.

[`QOU/QBeta/GZWeightSelection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/GZWeightSelection.lean)
(sorry-free, `lean`-direct exit 0) encodes `κ` on the three connections and proves:
`weightDiff_mem` (exponent `∈ {0, ±3/2}` — discrete, no `β` to fit),
`weightDiff_aomega_zero` (`b = 0` on the A_ω ray), `weightDiff_three_halves_needs_trivial`
(`±3/2` needs a `σ₀` endpoint), `kappa_eq_three_halves_iff`, `weightDiff_eq_zero_iff`.

## Consistency with the corpus (grep-checked, does not re-open settled items)

- The `u=0` `4₁` Stokes constant is the **integer 3 = DT/BPS invariant**, not the
  trace-field disc `−3`
  ([`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md),
  scope-a). This PR's "integer Stokes constant" is the same object, now with its
  *weight* correctly located.
- The bar-odd A_ω is deformation-carried (`no_anchor_invariant_realizes_swing`), and
  the ledger notes it is not a `u=0` `4₁` Stokes phase — the genuine odd channel lives
  on the non-amphichiral `5₂` class. The weight rule and "Stokes = integer 3d-index"
  are **knot-independent** (`κ(σ₀)=3/2` for every hyperbolic knot), so the same
  template applies to `5₂` with `Ind^{rot}_{5₂}` — the follow-up integer.

## Net

The "correct modular weight" is **not a single number to fit** — it is a **discrete
weight-difference selection rule** `b = κ(σ) − κ(σ′) ∈ {0, 3/2}`, and A_ω sits on the
**integer branch** (`b = 0`). The next quantitative target is therefore the **integer**
`[q⁰]Ind^{rot}` for the relevant knot (`4₁`: `3`; the odd channel: the `5₂` analogue),
an anti-laundering-compliant integer identification — not a continuous `β`.

### Sources
- Garoufalidis–Zagier, *Knots, Perturbative Series and Quantum Modularity*, SIGMA 20 (2024) 055, [arXiv:2111.06645](https://arxiv.org/abs/2111.06645) — eq. 3.7 `κ(σ₀)=3/2`; eq. 1.1 `N^{3/2}` prefactor.
- Garoufalidis–Gu–Mariño, *Resurgent Structure of Quantum Knot Invariants*, CMP 386 (2021), [arXiv:2007.10190](https://arxiv.org/abs/2007.10190) — Conj. 2, integer Stokes = rotated 3d-index.
- Garoufalidis–Gu–Mariño, *Peacock Patterns and Resurgence*, [arXiv:2012.00062](https://arxiv.org/abs/2012.00062) — `4₁` Stokes `{3,4}`.
- Fantini–Rella, *Modular resurgent structures*, [arXiv:2404.11550](https://arxiv.org/abs/2404.11550) — single tower ⇒ Stokes = L-function/QMF coefficients.
