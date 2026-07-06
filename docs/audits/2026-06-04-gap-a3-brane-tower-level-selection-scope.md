# GAP-A-3 — categorical brane-tower level selection for the per-partition Δ_λ decomposition

**Date:** 2026-06-04
**Audit type:** research-grade scoping for the productive direction identified in the just-merged consolidated audit ([`2026-06-04-three-paths-refuted-roadmap-update.md`](./2026-06-04-three-paths-refuted-roadmap-update.md), PR #1864).
**Status:** scoping doc. No probe in this PR.
**Sibling chain:** #1816 (Option A diagnostic, MERGED) → #1841 (Option B Bratteli, MERGED) → #1850 (Markov trace axis, MERGED) → #1853 (H₃→H₄ axes-refuted, MERGED) → #1860 (Option E Kashiwara, MERGED) → #1864 (3-paths-refuted roadmap, MERGED) → **this PR (GAP-A-3 scope)**.

---

## §1. What GAP-A-3 means after the Phase-4 amplitude

The [Δ_λ Phase-4 audit](./2026-05-19-delta-lambda-phase4-z4N-closure.md) already shipped a **zero-parameter substrate-derived closure** for the per-atom |Δ_λ*(K)| amplitude:

$$
\boxed{\;|\Delta_\lambda^*(K)| \;\approx\; \frac{\mathrm{Vol}_{\mathrm{hyp}}(K)}{[8]_q} \cdot [3]_q^{2(Z-1)} \cdot \bigl(q^{1/2} + q^{-1/2}\bigr)^{4N}\;}
$$

with max rel. err. **≤ 2.51 %** across D, T, ³He, ⁴He (zero fit parameters). The Phase-4 categorical reading:

- **per-neutron** factor `(q^{1/2}+q^{-1/2})^4 = (dim_q V_{1/2})^4` — 4 fundamental-rep evaluations per neutron
- **per-extra-proton** factor `[3]_q^2 = (dim_q V_1)^2` — 2 adjoint-rep evaluations per proton beyond the first
- **overall normalisation** `1/[8]_q` — inverse quantum dim of V_{7/2}

This is the **brane-tower level structure**. But the Phase-4 amplitude is the **single-block dominant** extraction — it closes the *per-atom* amplitude, not the *per-partition* distribution. The Phase-4 doc itself notes (caveat 1): *"the per-partition decomposition is the remaining work."*

That remaining work is exactly what **GAP-A-3** names.

## §2. What today's negatives say about GAP-A-3

PRs #1841 / #1850 / #1860 (this session) closed the following structural-derivation families for the per-partition `Δ_λ`:

| Family | Verdict | PR |
|---|---|---|
| Bratteli induction (H₃ → H₄) under uniform / y_λ-weighted / per-source | REFUTED | #1841 |
| Markov stabilization at trace level (z = 1/(q^{1/2}+q^{-1/2})) | REFUTED | #1850 |
| Kashiwara crystal — single partition-statistic c(λ) | REFUTED | #1860 (E1-E5) |

Combined with the six prior Δ_λ-gate failures (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, Occam, Wenzl-bridge), **9 partition-statistic / induction / stabilization ansätze are closed**.

These negatives are **consistent with the Phase-4 amplitude existing**: every partition-statistic ansatz collapses the per-partition structure into a single number per λ, which then either matches the *aggregate* `Σ_λ y_λ·χ^λ·c(λ)` target or doesn't. The fact that none does **and** the Phase-4 amplitude does match the per-atom target means:

> **The per-partition distribution does not factor as a single statistic of λ. It factors as a function of `(λ, K)` jointly — the brane-tower level structure of `K` projecting onto `λ`.**

This is the **two-layer** factorisation that GAP-A-3 names.

## §3. The structural pivot — two-layer factorisation

Pose the closure as a product of an **atom-level** factor and a **partition-projection** factor:

$$
\Delta_\lambda(K) \;=\; \underbrace{A(K)}_{\text{per-atom amplitude}} \cdot \underbrace{P_\lambda(K)}_{\text{partition projection}}
$$

where:

- `A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` is the Phase-4 substrate-derived amplitude.
- `P_λ(K)` is the unknown **partition-projection** of `K`'s brane-tower content onto irrep `λ`.

**Notation note** (Copilot review #1868). The Phase-4 doc reports
the absolute-value amplitude `|Δ_λ*(K)|`, which is the magnitude of
the single-block-dominant extraction. The factorisation here is on
the *signed* `Δ_λ(K)` that enters the closure equation
`Σ y_λ·χ^λ·Δ_λ = −B(K)/m_e`. The two are related by
`|Δ_λ*(K)| = |A(K)·P_λ(K)|`; the per-atom amplitude `A(K)` is taken
as the Phase-4 substrate-derived expression and is positive at q_0
(every factor is positive), so any sign / phase information lives in
`P_λ(K)`. The probe in §4 is constructed so that `P_λ(K)` is
unconstrained in sign (no `|·|`, no normalisation, no sum-to-one)
— each candidate channel evaluates to a real number per partition,
and the deuteron sum `Σ_λ y_λ·χ^λ·P_λ` is compared to
`−B(K)/(m_e·A(K))` rather than to `−B(K)/m_e` directly. This is
the precise way to read the Phase-4 amplitude as the per-atom
multiplier without conflating it with the signed binding-energy
target.

The closure requirement becomes:

$$
\sum_{\lambda \vdash 3A} y_\lambda(q_0) \cdot \chi^\lambda(\beta_K) \cdot A(K) \cdot P_\lambda(K) \;=\; -B(K) / m_e
$$

Since `A(K)` is `λ`-independent, it factors out:

$$
A(K) \cdot \sum_{\lambda \vdash 3A} y_\lambda(q_0) \cdot \chi^\lambda(\beta_K) \cdot P_\lambda(K) \;=\; -B(K) / m_e
$$

The remaining unknown is the **per-partition projection** `P_λ(K)`. The Phase-4 closure says `A(K)` is known to ≤ 2.5 %; the per-partition decomposition is whatever distribution of `P_λ(K)` reproduces `B(K)` consistently across atoms.

**Why this isn't the seventh fit ansatz.** Per AGENTS.md, *"do not propose a seventh fit-based ansatz."* The pivot is not a new closed-form for `Δ_λ`; it is a **factorisation** that takes the per-atom layer as already-derived (Phase 4) and asks what the per-partition layer must structurally be. A fit-based candidate for `P_λ(K)` would still be a fit; a brane-tower-derived candidate would be a derivation. The next sub-section identifies which sub-categories of `P_λ(K)` are categorical-derivation candidates (not fits) and which are not.

## §4. The cheapest formalize-first probe for `P_λ(K)`

Per [PR #1826](https://github.com/litlfred/qou/pull/1826), narrow the search before scanning. The Phase-4 amplitude's three factors suggest three **brane-tower content channels**:

| Channel | Phase-4 carrier | Brane-tower projection candidate |
|---|---|---|
| **Color** (per-extra-proton) | `[3]_q^2 = (dim_q V_1)^2` | `P_λ` proportional to multiplicity of `V_1`-content in the partition `λ`'s plethystic decomposition |
| **Spin** (per-neutron) | `(q^{1/2}+q^{-1/2})^4 = (dim_q V_{1/2})^4` | `P_λ` proportional to multiplicity of `V_{1/2}`-content (fundamental rep) |
| **Normalisation** | `1/[8]_q = 1/dim_q V_{7/2}` | `P_λ` divided by the `V_{7/2}` quantum dimension of λ's principal content |

**Pre-formalize-first prediction.** Each of these is a **categorical content count**, not a partition statistic. Per the closed no-fit-statistic family (#1860 et al.), simple partition statistics fail; but the brane-tower content channels carry the categorical structure that the Phase-4 amplitude already verified — they are the natural candidates for `P_λ(K)`.

**Cheapest first probe** (not run in this PR — scoping only):

1. Compute the **fundamental-rep content** (multiplicity of `V_{1/2}` in `λ`'s plethystic expansion) for each `λ ⊢ 3A` for the deuteron (`A=2, n=6, 11 partitions`).
2. Set `P_λ(D) = m_{1/2}(λ)` (the multiplicity).
3. Evaluate `A(D) · Σ_λ y_λ · χ^λ · P_λ` against `−B(D)/m_e = −4.353`.
4. If it lands within 5 %, the brane-tower content channel for spin is the natural projection; if not, try the color channel; if both fail, the per-partition layer requires a **mixture** (still not a fit, but a more structural decomposition).

The probe is one cheap sympy/mpmath script per channel — no Hecke construction, no LP, no fitted scalar. Each candidate is a closed-form categorical count, not a partition statistic.

## §5. Honest expected outcome

The Phase-4 amplitude works to ≤ 2.5 % zero-parameter, so **some structural decomposition exists**. The remaining question is whether `P_λ(K)` follows one of the natural brane-tower channels (color, spin, normalisation) or requires a more refined categorical reading.

If **all three channels refute**, the productive direction shifts to GAP-A-4 (the **ρ general rule** / per-atom λ(K) substrate-derivation in Path B). If **any channel lands**, the deuteron Δ_λ closure is the first concrete demonstration of the brane-tower level-selection direction, with the Phase-4 caveat-1 closed.

Either way, the framework's open math advances by one structural step.

## §6. What this PR does NOT do

- **No probe in this PR.** This is a scoping doc that frames the precise question GAP-A-3 names, gives the two-layer factorisation, and identifies the three cheapest formalize-first content channels. A follow-up branch would implement the probe.
- **No production code changes.** No content blocks, no Lean files, no witnesses.
- **No closed-form for `Δ_λ`.** The factorisation `A(K) · P_λ(K)` is the structural pivot; `P_λ(K)` itself is what GAP-A-3 must derive.
- **No 7th fit ansatz.** Per AGENTS.md, this PR is built to **pass** the Δ_λ-gate discipline review.

## §7. Discipline

- **EXPLORATORY** — scoping doc only.
- **Builds on**: Δ_λ Phase 4 (per-atom amplitude derived) + today's negatives (per-partition statistics refuted) → two-layer factorisation is the natural reading.
- **Formalize-first** — narrows the search to three brane-tower content channels before any probe runs.
- **Research-grade**: the brane-tower content multiplicities require plethystic decomposition machinery; the framework has the infrastructure (`y_lambda_at`, hook-length formula, quantum dims) but not yet wired plethystic content multiplicities. The probe-side scoping (§4) is one cheap script per channel.

## §8. Cross-references

- [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate doc + the seven-ansatz table
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md) — the Phase-4 amplitude formula + categorical reading
- [`2026-06-04-three-paths-refuted-roadmap-update.md`](./2026-06-04-three-paths-refuted-roadmap-update.md) — today's consolidated negative result; identifies GAP-A-3 / GAP-A-4 as the productive direction
- [`2026-06-04-option-e-kashiwara-crystal-scope.md`](./2026-06-04-option-e-kashiwara-crystal-scope.md) — yesterday's Option E Kashiwara test (closes the single-statistic family for `Δ_λ`)
- [`2026-06-04-h3-h4-jump-both-axes-refuted.md`](./2026-06-04-h3-h4-jump-both-axes-refuted.md) — the H₃→H₄ jump axes-refuted consolidation (the Q1 axis; this PR is on the Q2 axis but cites the same brane-tower interpretation)
