# Δ_λ residual moments μ₃, μ₄ from ρ_F cluster integrals — WALL (split)

**Date:** 2026-07-26
**Branch:** `claude/deltalambda-mu4-rhoF-cluster-2026-07-26` (PR #4354)
**Redirect from:** #4320 (`QOU.MassTheory.AdditiveResidualSimplex`, sorry-free,
`6851e214`) — the deuteron-wall that re-scoped the Δ_λ residual as a pure ≥3-body
simplex object and named the ρ_F cluster integrals as the derivation target for μ₄.

## Task

#4320 proved the Δ_λ damping-wall residual `M(A) = ρ_strong(A) − ρ_grad(A)` is a
**pure ≥3-body** simplex object over the derived coordination-graph counts `C(A,k)`:

    M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4),
    μ₂ = 0 (deuteron self-reference),  μ₃ = +0.4708 (A=3),  μ₄ = −4.591 (A=4).

The three residual points `M(2)=0, M(3)=+0.4708, M(4)=−2.708` fix the three
coefficients by an exact 0-parameter unit-triangular solve. **Do the interface
operator ρ_F cluster integrals reproduce μ₃, μ₄ from 0–1 derived parameters (no
AME inversion)?**

## Infra — NOT gated

`pyhecke_native` 0.9.0 is functional here (`markov_z`, `gram_matrix`,
`chi_lambda_*`, `gauge_aligned_a_combiner_*`). The derived ρ_F connected 3-body
cluster is cached 0-fit at `computations/three-body-joint-trace-a3.witness.json`
(H₉ joint trace). **No Rust build required.** This is not an infra-gate.

## What ρ_F is

The interface-product binding `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)` with categorically-derived
per-bond factors (Lean-proved exact): `f ∈ {z, z−h, z−h/2}`,
`z = 1/(√q+1/√q) ≈ 0.4993`, `h = q−1/q ≈ 0.2091`. There is no dedicated `rho_f`
function; the connected `k`-body **cluster integral** is the beyond-pairwise
(Ursell) content of that pairwise product, computed from the χ_λ / A-combiner
primitives.

## The decomposition that pins the test

The residual is the **difference of two simplex ladders**, `μ_k = s_k − g_k`:

| k | `g_k` (ρ_grad = [A]_q!/[2]_q!, **DERIVED**) | `s_k` (ρ_strong, AME target) | `μ_k = s_k − g_k` |
|---|---:|---:|---:|
| 2 | 1.000 | 1.000 | **0** |
| 3 | 0.342 | 0.8128 | **+0.4708** |
| 4 | **+8.371** | 3.780 | **−4.591** |

`g_k` is fully derived (q-factorial, 0-param); `s_k` is the AME side. **μ₄<0 is
dominated by the derived graded `g₄ = +8.37` being subtracted** — it is a property
of the graded *reference*, not evidence for an ρ_F 4-body cluster.

## The derived ρ_F cluster integrals (0-fit, q₀-only)

- **3-body** `c₃ = joint − pair_sum` (H₉ joint trace): `c₃(T) = −1.769`,
  `c₃(³He) = −1.405` MeV → ⟨c₃⟩ = **−1.59 MeV**. Sign **−**.
- **4-body** product-model beyond-pairwise content on K₄ (6 bonds): **−2.63**.
  Sign **−**.

## Sign gate (normalization-free) + free-parameter count

| moment | target sign | derived cluster sign | match |
|---|:--:|:--:|:--:|
| μ₃ = +0.4708 | **+** | c₃ < 0 | ❌ **WALL** |
| μ₄ = −4.591 | **−** | c₄ < 0 | ✅ consistent |

A single normalization `N > 0` maps same-sign `(c₃, c₄)` to same-sign
`(Nc₃, Nc₄)`, so it **cannot** hit the opposite-sign target `(μ₃>0, μ₄<0)`. No
0–1-parameter derivation lands both moments; a per-moment fit (1 param each) would
be needed, and it still **fails the μ₃ sign** (`Nc₃ < 0 ≠ μ₃ > 0`).

**Lean-proved wall (scope (b)).** The merged sorry-free
`QOU.BraidKnot.Cluster.productModel_3body_nonpos` (beyond-pairwise 3-body content
of any product model `c(1−∏f)`, `f∈[0,1]`, is `≤ 0`) together with
`markovParam_le_half` (`z ≤ 1/2 < 1` for all `q>0`, foreclosing the only pairwise
escape `f>1`) prove **no pairwise interface product yields a positive 3-body
cluster** — so `μ₃ > 0` is structurally unreachable by the multiplicative ρ_F
route. This session formalizes the bridge in
`QOU/MassTheory/Mu4RhoFCluster.lean`:
`one_sub_prod_le_oneSum` (general beyond-pairwise ≤0, covering both 3- and 4-body),
`pairwise_3body_content_nonpos` (mirrors the canonical), `mu3_ne_pairwise_3body_cluster`
(the wall: μ₃>0 ≠ a ≤0 cluster), `mu4_sign_consistent_with_pairwise_cluster`
(the 4-body sign is consistent, not a derivation).

## Verdict

**WALL (split). NOT infra-gated. NOT a derivation.**

- **μ₃ — scope-(b) proved sign exclusion** of the pairwise-product cluster route
  (`productModel_3body_nonpos` + `z≤½<1`). The residual's positive 3-body triangle
  moment cannot come from any multiplicative ρ_F cluster.
- **μ₄ — scope-(a) sign-consistent-but-not-derived.** The derived 4-body cluster is
  negative like μ₄, but μ₄'s magnitude is the *derived graded* `g₄` subtraction, not
  an ρ_F cluster; no normalization lands both moments together.

**Open door.** The only route to a positive 3-body cluster is a **non-multiplicative
/ enhancing (`f>1`) cluster operator** — a genuine 3-body operator that is not a
product of pairwise factors. The *sign* of the 3-body cluster (not its scale — the
scale already matches at ~1.5 MeV) is the standing open question, consistent with
`binding_cluster_operator_vs_mayer_probe.py` (scale matches, sign opposed).

**Anti-fit (STRICT).** No normalization is wired. The `μ_k` targets enter from the
AME side only; the ρ_F clusters are q₀-only, 0 fit. `κ = 2.385` (the #4316
bond-frustration fit) stays labelled a fit; `μ₂ = 0` is the derived, AME-independent
fact. "No seventh fit-based ansatz" and the PROBE-4 KL-prune stand.

## Artefacts

- `computations/deltalambda/mu4_rhoF_cluster_derivation_probe.py`
- `computations/deltalambda/mu4-rhoF-cluster-derivation.witness.json`
- `content/quantum-observable-universe/lean/QOU/MassTheory/Mu4RhoFCluster.lean`
  (hand-audited; lean-direct blocked by pruned lake-cache + disk ENOSPC — see the
  file's verification note)
