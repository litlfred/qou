# Q_β Markov-trace inner product collapses the L2 SHAPE to T_β = S · I

**Date.** 2026-06-03
**PR.** [#1750](https://github.com/litlfred/qou/pull/1750) (`claude/qbeta-markov-trace-2026-06-03`)
**Companion compute.** [`computations/qbeta/qbeta_markov_trace_norm_probe.py`](../../computations/qbeta/qbeta_markov_trace_norm_probe.py)
**Witness.** [`qbeta-markov-trace-norm-probe.witness.json`](../../computations/qbeta/qbeta-markov-trace-norm-probe.witness.json)
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
| What IS T_β as an operator? | 6-channel q-rational SHAPE × S | `S · I` (just a scalar × identity) |
| Per-channel NF coordinates | spread across 6 channels | 1 non-zero (γ = I) |
| Habiro question for T_β-as-operator | per-channel `F_i(q) = A_i/‖A‖²` | trivially `S(q)` (a single scalar) |
| **τ_M(T_β)(q) (the observable)** | **= S(q) (SDP constraint)** | **= S(q) (Markov normalisation)** |
| **c_k Taylor coefficients of Q_β** | **= w-Taylor of S(q)** | **= w-Taylor of S(q)** — *identical* |
| Cross-anchor c_3 swing source | **structural (upstream of SDP)** | **structural (upstream of SDP)** |

**The c_k are L2/Markov-INVARIANT.** Both norms reproduce `τ_M(T_β)(q) ≡ S(q)` identically (the SDP **constraint**), so the c_k extracted from `τ_M(T_β)(q)` are the Taylor coefficients of `S(q)` in either case. The Markov collapse is a structural simplification of **T_β-as-operator** — it does NOT redirect c_k extraction. *See [`docs/audits/2026-06-03-qbeta-markov-trace-step-4-ck-invariance.md`](2026-06-03-qbeta-markov-trace-step-4-ck-invariance.md) for the algebraic-identity proof + companion witness.*

The numerical Q_β prediction is **unchanged** — both T_β^L2 and T_β^Markov satisfy `τ_M(T_β) = S` by construction. The Q_β value is determined by the SDP **constraint**, not by the choice of **objective**. What changes is the **structural picture** of which operator inside H₃(q) is the canonical primal-feasible solution.

## What this implies for the c_k precision ladder

**Nothing directly.** The c_k come from `τ_M(T_β)(q) = S(q)`, which is identical in both norms (Step 4 diagnostic, witness `qbeta-markov-trace-step-4-ck-invariance.witness.json`). The cross-anchor c_3 swing recorded in the canonical-framing audit ([`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)) is a property of `S(q)` itself (the canonical Q_β-derivation chain), not of any SDP projection choice.

**What the Markov collapse DOES buy for c_k work**: a cleaner structural framing. The L2 picture suggested that `T_β`'s spread across 6 NF channels carried independent q-dependence; the Markov picture clarifies that all the q-dependence flows through the single scalar `S(q)`. Searches for a categorical residue / Habiro element for the c_k saga can target `S(q)` directly, with no detour through the 6-channel basis.

This was originally framed as "the swing might be an L2-projection artifact". That framing was wrong: the swing is upstream of the SDP and is therefore **structural**, not an L2 artifact. The honest correction landed in commit `<step-4-correction>` on this PR.

## Caveats

1. **Symbolic A^T G^{-1} A = 1 is fully discharged.** Commit `9bd3f95444` verified the column identity `G·e_γ = A` as a polynomial identity in `(q, b, y_λ)` — all 6 residues simplify to `0` symbolically. This gives `G^{-1} A = e_γ` ⇒ `A^T G^{-1} A = A_γ = τ_M(I) = 1` exactly, without needing a 6×6 symbolic inverse (which sympy's GCD machinery silently OOM'd on).

2. **This does not redefine the Q_β prediction.** Both L2 and Markov SDPs reproduce `Q_β/E_0 = S` at q₀; the difference is which operator inside H₃(q) you call "T_β". The numerical predictions of PR #1739 and subsequent integrations are unaffected.

3. **The 6-channel SHAPE × S of PR #1739 is still a true theorem under L2** — that PR is not wrong; it just answers the question "what does T_β look like when you measure with the Euclidean coordinate norm?" The present finding answers the parallel question "what does T_β look like under the natural categorical norm?" and gets a much simpler answer.

4. **Habiro integrality** of `S(q) = Q_β(q)/E_0(q)` is the right next-probe question. The Habiro element work in PR #1511 / #1727 territory already studies this scalar function (via the eigenphase / α_EM construction); the present finding **redirects attention** from the 6-channel SHAPE to that single scalar.

## Follow-ups planned on this PR

- [x] Symbolic verification of `A^T G^{-1} A = 1` — done in commit `9bd3f95444` via the column-identity route (`G·e_γ = A` as a polynomial identity in `(q, b, y_λ)`). Witness: `qbeta-markov-trace-steps-4-5.witness.json`.
- [x] c_k L2/Markov-invariance diagnostic — done as Step 4 honest correction. Witness: `qbeta-markov-trace-step-4-ck-invariance.witness.json`. Result: c_k extracted from `τ_M(T_β)(q) = S(q)` are identical in both norms; the cross-anchor c_3 swing is structural (upstream of any SDP norm choice), not an L2 artifact.
- [x] Audit-doc cross-link from [`2026-06-03-qbeta-step1-symbolic-min-l2.md`](2026-06-03-qbeta-step1-symbolic-min-l2.md) §"Caveats" §1 — caveat §1 is now resolved by this finding (Markov picture is the canonical answer; L2 result is still true under its norm).
- [ ] Lean formalisation candidate: `T_β = S · I` as a theorem-conditional-on-min-Frobenius-norm (§3b-cond exception of AGENTS.md). Stub planned for the same PR.
