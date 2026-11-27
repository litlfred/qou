# q-NS Part A: modal triad model and the DEC model as N → ∞

Date: 2026-11-27. Bean `qou-pa7n`. Owner picks (card): "Modal triad model +
Parseval", and in chat, "And also the deck to Infinity" (the DEC model as the
mode count N → ∞). Rule: only QOU-formalised work is used. No empirical value
enters any proof.

Lean (sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, axioms
`propext, Classical.choice, Quot.sound`):

- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_modal_triad.lean`
- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_dec_refinement.lean`

## Why

Over the weakened `QNsWellposednessContext`, Part A is trivially true
(`partA_trivial_over_weakened_class`, PR #9523). The class does not tie the
transfer term `T_k` to the amplitudes. A real model needs energy-conserving
transfer between modes.

## Track 1: modal triad model

**Where the structure comes from.** The q-NS modes are the `Δ_q` eigenmodes,
which carry `SU_q(2)` irreducible labels with eigenvalues `[k]_q²`
(`thm:quantum-peter-weyl`, `prop:q-laplacian-spectral-tower`). A quadratic
nonlinearity `μ ∘ (v ⊗ ∇_q v)` can couple mode `n` to the pair `(p, r)` only
when `V_n ⊂ V_p ⊗ V_r`. For generic `q` that is the Clebsch–Gordan fusion rule:
the triangle inequalities plus `n + p + r` even, in doubled spins
(`FusionTriad`).

**What is proved.**

| Lean | Statement |
|---|---|
| `TriadCoeff` | Couplings vanish off fusion triads, are symmetric in the pair, and conserve the weighted Parseval energy `∑ wₙ aₙ²` triad by triad |
| `galerkin_energy_conservation` | `∑ wₙ aₙ Tₙ = 0` on every finite mode set |
| `transfer_eq_zero_of_gt` | Data on modes `≤ m` feed only modes `≤ 2m` |
| `GalerkinSol.energy_hasDerivAt` | `dE/dt = −2νΩ` exactly |
| `GalerkinSol.enstrophy_le` | `Ω(t) ≤ λ_max · E(0)` |
| `partA_fails_on_truncation` | For a truncation to modes `≤ N`, `sup_t Ω ≤ [N]_{q₀}² · E(0)` for every `q ∈ (1, q₀]`, every coefficient system (which may depend on `q`), and every `ν ≥ 0`, Euler included |
| `kraichnan`, `kraichnan_ne_zero`, `singleMode` | Non-vacuity: a nonzero coefficient system and an explicit nonzero solution |

**Scope (b).** On every finite truncation, Part A is structurally excluded. The
invariant is triad-wise energy conservation together with the monotonicity of
`[n]_q` in `n` and `q`. This generalises the DEC finding of PR #9434 from one
discretisation to every truncation and every choice of coefficients.

**Consequence.** If `sup_t Ω` diverges as `q → 1⁺`, the divergence must come from
energy reaching arbitrarily high modes. By `transfer_eq_zero_of_gt`, reaching
mode `N` from data on modes `≤ m` takes at least `log₂(N/m)` triad steps. Part A
is therefore a statement about the infinite-mode system.

**Not established.**
- The actual q-NS coefficients. These are the `q`-Clebsch–Gordan coefficients
  of `μ ∘ (v ⊗ ∇_q v)` on Peter–Weyl modes, and the corpus does not compute them.
  The `kraichnan` system is only a non-vacuity witness.
- Existence for the infinite-mode system.
- Part A itself.

## Track 2: the DEC model as N → ∞

**Finding.** The DEC model of PR #9434 lives on a 2-complex, where vorticity is
one scalar per face. In two dimensions there is no vortex stretching. If the
discrete advection creates no enstrophy, `⟨ω, d₁B⟩ = 0`, then:

- `enstrophy_equality_of_enstrophy_skew`: `⟨ω, ω̇⟩ = −ν |d₁ᵀ ω|²`;
- `GalerkinTraj.enstrophy_le_initial`: `Ω(t) ≤ Ω(0)` for every `t ≥ 0`;
- `partA_fails_dec2d`: this bound holds uniformly in `q`, in `ν ≥ 0`, and in
  the complex.

The condition `⟨ω, d₁B⟩ = 0` is the hypothesis `hens`, named in every lemma that
uses it. It is the discrete form of the continuum 2D identity
`∫ω(u·∇ω) = 0` for divergence-free `u`. It is not derived here for any specific
scheme.

**Scope (b), conditional on `hens`.** No mesh refinement of a 2-complex model
can carry Part A, because the bound does not depend on the resolution.
Non-vacuity: `gradient_advection_skew` exhibits a nonzero advection that
satisfies both skew conditions.

**What Part A needs from DEC.** A 3-complex, with vorticity a 2-form on a
3-manifold and the stretching term. No such q-NS model exists in the corpus. A
gap bean has been filed.

## Status of Part A

Part A remains an open conjecture (bean `qou-pa7n` stays open). Both tracks
narrow where it can live:
- it needs infinitely many modes;
- in the DEC picture, it needs three dimensions.

What it needs next is the `q`-Clebsch–Gordan coefficients of the corpus
nonlinearity, or a 3-complex DEC model.
