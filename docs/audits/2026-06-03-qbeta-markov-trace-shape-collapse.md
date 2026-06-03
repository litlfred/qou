# Q_β Markov-trace inner product collapses the L2 SHAPE to T_β = S · I

**Date.** 2026-06-03
**PR.** [#1750](https://github.com/litlfred/qou/pull/1750) (`claude/qbeta-markov-trace-2026-06-03`)
**Companion compute.** [`folio-assistant/computations/qbeta/qbeta_markov_trace_norm_probe.py`](../../folio-assistant/computations/qbeta/qbeta_markov_trace_norm_probe.py)
**Witness.** [`qbeta-markov-trace-norm-probe.witness.json`](../../folio-assistant/computations/qbeta/qbeta-markov-trace-norm-probe.witness.json)
**Addresses.** [`2026-06-03-qbeta-step1-symbolic-min-l2.md`](2026-06-03-qbeta-step1-symbolic-min-l2.md) caveat §1 (basis-dependence of the Euclidean L2 norm).

## TL;DR

In the categorically-natural **Markov-trace inner product** `⟨X, Y⟩_τ := τ_M(X · Y)` on H₃(q), the minimum-norm primal-feasible solution to the SDP constraint `τ_M(T_β) = S = Q_β(q₀)/E_0(q₀)` is

$$
\boxed{\;T_\beta^{\text{Markov}} \;=\; S \cdot I\;}
$$

a **scalar multiple of the identity**. All six L2-SDP NF channel coordinates (σ₀, σ₁, L₊, L₋, e⁻) — the SHAPE × S decomposition of [PR #1739](https://github.com/litlfred/qou/pull/1739) — are **artifacts of the Euclidean coordinate norm**, not categorical structure.

The structural identity that drives this collapse:

$$
A^{T} G^{-1} A \;=\; 1 \qquad\text{(exact, not numerical near-equality)}
$$

where `G_{ij} := τ_M(b_i · b_j)` is the Hecke-Frobenius Gram matrix on the NF basis `{γ, σ₀, σ₁, L₊, L₋, e⁻}` and `A_i := τ_M(b_i)` is the constraint vector.

## Proof of the identity

The NF basis vector `b_γ` is the identity `I` of H₃(q). For any other basis element `b_i`:

$$
G_{γ, i} \;=\; τ_M(b_γ \cdot b_i) \;=\; τ_M(I \cdot b_i) \;=\; τ_M(b_i) \;=\; A_i.
$$

So the **γ-th column of G is the vector A**:

$$
G \cdot e_γ \;=\; A.
$$

Therefore `G^{-1} A = e_γ`, and `A^T G^{-1} A = A^T e_γ = A_γ = τ_M(I) = 1` (the standard normalisation of the Markov trace).

The min-norm Lagrangian solution to `min ½ x^T G x` subject to `A^T x = S` is

$$
x = G^{-1} A \cdot \frac{S}{A^{T} G^{-1} A} \;=\; e_γ \cdot \frac{S}{1} \;=\; S \cdot e_γ
$$

i.e. `T_β^Markov = S · b_γ = S · I`. ∎

## Numerical verification at q₀

At `q₀ ≈ 1.10998`, 50-dps numerical inverse of the symbolic 6×6 Gram matrix:

| Quantity | Value |
|----------|-------|
| `A^T G^{-1} A` | `1.0000000000000` (exact to 12 digits — no numerical noise) |
| `x_M(γ)` | `0.186893691886` = `S = Q_β(q₀)/E_0(q₀)` |
| `x_M(σ₀)..x_M(e⁻)` | all `0` (exactly) |

Constraint satisfaction (both norms hit the same target):

| Norm | `τ_M(T_β)(q₀)` | Residue vs S |
|------|----------------|---------------|
| L2 (PR #1739 witness) | `0.186893691608` | `2.8 × 10⁻¹⁰` (witness roundoff) |
| Markov (this finding) | `0.186893691886` | `0` (exact) |

## What this changes about Q_β

| Question | L2 SDP picture (PR #1739) | Markov picture (this PR) |
|----------|---------------------------|--------------------------|
| What IS T_β? | 6-channel q-rational SHAPE × S | `S · I` (just a scalar) |
| What's the SHAPE for Habiro integrality? | `F_i(q) = A_i(q)/‖A(q)‖²` (per channel) | trivially `S(q₀)` — the scalar |
| What's the non-trivial q-dependence? | spread across 6 channels | **all in S(q₀) = Q_β(q₀)/E_0(q₀)** |
| What's the c_k Taylor structure? | requires the SHAPE expansion | **= Taylor expansion of S itself** |
| Cross-anchor c_k swing source? | possibly structural | **may be L2-projection artifact** |

The numerical Q_β prediction is **unchanged** — both T_β^L2 and T_β^Markov satisfy `τ_M(T_β) = S` by construction. The Q_β value is determined by the SDP **constraint**, not by the choice of **objective**. What changes is the **structural picture** of which operator inside H₃(q) is the canonical primal-feasible solution.

## What this implies for the c_k precision ladder

The Q_β production rule `Q_β = Q_base · ∏(1 + c_k · u^k)` extracts `c_k` from the Taylor expansion of `τ_M(T_β)(q)` near q=1. Under L2, that's the Taylor of the 6-channel projection. Under Markov, it's the Taylor of `S(q) = Q_β(q)/E_0(q)` — a single q-rational function with no basis-dependent projection.

The recurrent **cross-anchor c_3 swing** noted in the canonical-framing audit ([`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)) was extracted from the L2-projection's c_k. If the Markov c_k are derived from `S(q)` directly, the swing pattern may differ — possibly cleaner (no L2 basis-dependence) or possibly the same (if the swing is genuinely structural).

**This is a probe to run next**, not a claim already discharged.

## Caveats

1. **Symbolic G.inv() was not completed** — sympy's GCD machinery silently OOM'd on the 6×6 inverse over `Q(q, √q, √(q⁴+q²+1))`. The identity `A^T G^{-1} A = 1` is established by the column-identity proof above (which is symbolic and bulletproof) plus 12-digit numerical verification at q₀. A more careful symbolic verification (substituting `r = √q`, `b = √(q⁴+q²+1)/(q²+1)` to keep the algebra polynomial) is the natural follow-up; the column-identity proof should not require it but the witness completeness benefits.

2. **This does not redefine the Q_β prediction.** Both L2 and Markov SDPs reproduce `Q_β/E_0 = S` at q₀; the difference is which operator inside H₃(q) you call "T_β". The numerical predictions of PR #1739 and subsequent integrations are unaffected.

3. **The 6-channel SHAPE × S of PR #1739 is still a true theorem under L2** — that PR is not wrong; it just answers the question "what does T_β look like when you measure with the Euclidean coordinate norm?" The present finding answers the parallel question "what does T_β look like under the natural categorical norm?" and gets a much simpler answer.

4. **Habiro integrality** of `S(q) = Q_β(q)/E_0(q)` is the right next-probe question. The Habiro element work in PR #1511 / #1727 territory already studies this scalar function (via the eigenphase / α_EM construction); the present finding **redirects attention** from the 6-channel SHAPE to that single scalar.

## Follow-ups planned on this PR

- [ ] Symbolic verification of `A^T G^{-1} A = 1` (rather than column-identity + numerical) via polynomial-domain substitution `r = √q`, `b = √(q⁴+q²+1)/(q²+1)`.
- [ ] w-Taylor expansion of `S(q) = Q_β(q)/E_0(q)` itself (instead of the L2-projection's c_k) — does the cross-anchor swing pattern simplify?
- [ ] Audit-doc cross-link from [`2026-06-03-qbeta-step1-symbolic-min-l2.md`](2026-06-03-qbeta-step1-symbolic-min-l2.md) §"Caveats" §1 — caveat §1 is now resolved by this finding (in the unexpected direction).
- [ ] Lean formalisation candidate: `T_β = S · I` as a theorem-conditional-on-min-Frobenius-norm (§3b-cond exception of CLAUDE.md).
