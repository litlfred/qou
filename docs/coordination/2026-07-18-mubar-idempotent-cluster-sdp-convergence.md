# Mixed-multibond shared channel — μ̄ / cluster / SDP convergence ledger

**Date:** 2026-07-18 · **Goal:** derive the mixed-multibond shared channel (Model-G
open trio; the `9b` / GAP-A-3 coordination-weight closure). Records how three
same-day PRs attack the one object from complementary sides. Owner steer:
"work on derived μ̄-idempotent / SDP-knot-ID invariant."

## The object

The light cluster `X` bridging `m` α's carries a shared, sub-additive binding
channel — the mixed-multibond miss (t-series ⁷Li/¹¹B/¹⁵N/¹⁹F: **0 / 6.44 / 7.84 /
2.26 MeV**, non-monotone, vanishing at m=1). Audit next-step #1
([`2026-07-14-mixed-multibond-interface-derive-or-refute.md`](../audits/2026-07-14-mixed-multibond-interface-derive-or-refute.md)):
"one |μ̄|-idempotent per light cluster." The channel factors as
`Σ_triples w_triple · μ̄_triple`.

## The three complementary attacks

| PR | side | result |
|---|---|---|
| **#3888** (this branch) | **μ̄ topology** — *which* triples | μ̄∈ℤ (Magnus); the **common-weight × integer Borromean-count** form is **refuted** (t-series needs 1.22 / 0.35 non-integer triples, robust ±5% b,g). ⇒ the magnitude `w_triple` must be **q-weighted per block**, not a common scalar. [audit](../audits/2026-07-18-mixed-multibond-mubar-idempotent-integrality.md) |
| **#3875** (`ka-additive-cluster`) | **cumulant magnitude** — the *weight/sign* | Ursell connected cumulants: **b₃ isospin-blind (+0.94), b₄ = −2.21 (opposite sign)**, and the **bar-parity obstruction** (raw tr_M bar-odd at q₀ ⇒ bar-even symmetrization *before* clustering). Supplies exactly the non-common per-triple magnitude/sign #3888 says is required. |
| **#3802** (`he4-binding-k-stage2`) | **SDP per-block weight** — the *derived* `w_triple` | Exact per-block seminormal χ_λ(K) → operator-selection **LP primal/dual** (active set `y_star>0`); **K(⁴He) not PSD** (naive T·cp⁻¹ fails at A=4). The LP duals **are** the per-block weight #3888 names as the missing input; the PSD result constrains the A=4 link topology. |

## Synthesis (not yet closed)

The shared channel = **bar-parity-signed connected cumulants** (μ̄-triples from #3888,
weighted by the b₃/b₄ sign structure from #3875, magnitudes fixed by the SDP LP-dual
per-block weights from #3802). Each PR rules out or supplies one leg:

- #3888 rules out the bare integer count (the topology alone) — **(a)**.
- #3875 shows the magnitude carries a bar-parity sign structure (not a common weight).
- #3802 produces the actual per-block LP-dual weights (the derived `w_triple`).

**Open closing step:** consume #3802's LP-dual per-block weights + #3875's bar-parity
symmetrization to build `w_triple`, then evaluate `Σ_triples w_triple·μ̄_triple`
against the t-series {6.44, 7.84, 2.26}. That requires #3802's exact run to land
(the LP duals) and a bar-even pre-symmetrization of the traces (#3875) — neither
available in the #3888 sandbox (no cvxpy/Clarabel + no Hecke wheel). This is the
concrete, named hand-off.

## Anti-fit note

Every leg is scope-(a) / structural; no fitted constant is wired. The synthesis is a
*derivation target*, not a closure — consuming derived (LP-dual, bar-parity) weights,
not inverting the AME anchors.

## Cross-refs

- #3888 audit + probe; #3875 [`ka-additive-cluster-negative-structural-findings.md`](2026-07-18-ka-additive-cluster-negative-structural-findings.md);
  #3808 Model-G rounds 8–11; #3841 per-knot b₂ (merged).
- Binding ledger: [`binding-scale-is-hyperbolic-volume.md`](binding-scale-is-hyperbolic-volume.md).
