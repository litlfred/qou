# Three structural derivation paths refuted — open math is now well-localized

**Date:** 2026-06-04
**Audit type:** consolidated negative result (companion to #1853)
**Owners:** PR chain — #1762 (1ppQ roadmap; 5 attack options), #1816 (Option A diagnostic, MERGED), #1841 (Option B Bratteli, MERGED), #1850 (Markov trace axis, MERGED), #1853 (H₃→H₄ axes-refuted consolidation, MERGED), #1860 (Option E Kashiwara Δ_λ, MERGED), the Δ_λ-gate audit [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md).
**Status:** **closes three structural derivation candidate families.** Two open derivation questions — the H₃→H₄ jump in `linking_weight_family_a` and the per-isotope Δ_λ closure — are now sharply localized to a single productive research direction: GAP-A-3 / GAP-A-4 (categorical brane-tower level selection, ρ general rule).

This is a **roadmap-level consolidation**, not a new probe. #1853 covered the H₃→H₄ jump alone; this audit extends it with the orthogonal Δ_λ axis and lays out what the combined negatives say about the next productive direction.

---

## §1. The two open derivation questions

The framework has two open structural questions that resist closed-form derivation:

### Q1. The H₃→H₄ jump in `linking_weight_family_a`

`linking_weight_family_a(q) = (3q²+4+3q⁻²)/4 = (1/4)·Σ_{λ⊢4} dim_q(V_λ) ≈ 2.53` is applied as a global multiplier in `vol_density_borromean`. The proton braid `𝓑₃` lives in H₃, but the multiplier sums over partitions of **4**. **Why H₄?** — surfaced in PR #1762 §2.

### Q2. The per-isotope Δ_λ binding-energy closure

Under Path D (the canonical T6-unit choice declared in PR #564), the binding-energy formula
`B(K) = m_e · Σ_{λ⊢3A} y_λ(q₀)·χ^λ(β_K)·Δ_λ(K)` requires per-partition `Δ_λ(K)` values. For the deuteron alone this is 1 equation in 11 unknowns. **What forces Δ_λ?** — surfaced in the Δ_λ-gate audit.

## §2. Five structural candidates tried; all REFUTED

| Question | Candidate axis | PR | Verdict |
|---|---|---|---|
| Q1 | Algebra-tower induction (Bratteli `Ind_{H₃}^{H₄}`) under uniform / y_λ-weighted / per-source weightings | #1841 | **REFUTED** (3/3 sub-hypotheses) |
| Q1 | Trace-level Markov stabilization (z = 1/(q^½+q^{-½})) — identity-trace OR z-renormalised H₃ | #1850 | **REFUTED** (z<1 obstruction; M1 = 1 exactly; M2 no exact `z^k` coincidence) |
| Q2 | Frobenius co-Casimir `1/dim_q(λ)` | [#602](https://github.com/litlfred/qou/pull/602) | **failed** — residual −2.30 MeV (wrong sign) |
| Q2 | Demazure-fibre `y_λ·D_w/D_w₀` | (sibling e77a4b4d) | **failed** — tautological (reproduces M_LO) |
| Q2 | LP-Plancherel / LP-Frobenius shadow prices | [#603](https://github.com/litlfred/qou/pull/603) | **shifts** underdetermination from value to cost |
| Q2 | Occam single-support | (legacy) | **arbitrary** singleton picking |
| Q2 | Wenzl-bridge augmented Markov | (in flight) | **failed at first attempt** — a serialization error (Python `pickle` could not round-trip the augmented Markov closure object across the symbolic / numeric boundary), which blocked the closure from being checked; the ansatz was abandoned rather than re-engineered because the parallel candidates (E1-E5, Frobenius, Demazure, LP) already covered the no-fit family |
| Q2 | **Kashiwara crystal (Option E)** — five no-fit candidates E1-E5 | **#1860** | **REFUTED** (all 5: Macdonald `n(λ)`, conjugate `n(λ')`, dim ratio at q₀, constant-zero control, ordinary dim `f^λ`) |

That's **2 structural axes refuted for Q1** + **7 for Q2** = 9 total no-fit closure attempts, all closed.

## §3. The remaining productive direction — GAP-A-3 / GAP-A-4

Per the Δ_λ-gate doc and the [Δ_λ Phase-4 audit](./2026-05-19-delta-lambda-phase4-z4N-closure.md), the remaining productive directions for **Q2** are:

- **GAP-A-3**: categorical brane-tower level selection — Δ_λ as a property of the brane-tower truncation order ℓ(K, q_0), not of any per-partition functional
- **GAP-A-4**: ρ general rule — the per-atom λ(K) substrate-derivation (Path B's gate), which would close Q1's "why H₄" structurally by making the Wedderburn-count interpretation moot

Both are **research-grade categorical work**, not closed-form probes. They sit above the Δ_λ-gate cap; AGENTS.md is explicit that no seventh fit ansatz is permitted.

## §4. What this audit does NOT close

- **The production multipliers stay in place.** `linking_weight_family_a` remains the production multiplier; m_p round-trips on it (Option A's diagnostic confirmed flipping breaks m_p by ≈ 2.38× and the gap grows with A). This audit is structural, not actionable on production.
- **Q_β c_3 categorical lift** remains pending (PRs #1801, #1806, #1822 all refuted candidate rung-2 lifts; the recent PR #1822 item-2 catalog showed /25 is a structural marker shared by m_μ V9 + Q_β c_3 — the L2-failing observables — but the categorical mechanism is still open). The m_n + Δ_pn predictions are downstream of Q_β closure.
- **The full Path B route** (Borromean tower extension; per-atom λ(K) substrate-derivation, PRs #751 / #690 / #777) is the alternative if GAP-A-3 / GAP-A-4 also refute. Per the audit-doc table it bypasses the Δ_λ gate at the cost of re-opening the per-atom λ(K) derivation problem (which the framework is already working on for individual baryons).

## §5. Honest framing for downstream content

After these refutations, the recommended scholarly framing is:

- `linking_weight_family_a(q)` is a **CODATA-implied near-match** (`_li_2_q_util.py:298-313`), landing near `λ = m_p/(m_e·Vol/ℏ²) ≈ 2.46`. Not a derived categorical count. The `(1/4)·Σ_{λ⊢4} dim_q` decomposition is exact, but the choice of H₄ is not structurally derived.
- The per-partition `Δ_λ(K)` for binding-energy is **structurally underdetermined** at the level of partition-statistic ansätze. The framework's open math at this layer is GAP-A-3 / GAP-A-4 (categorical research, not closed-form fitting), per the Δ_λ-gate doc.
- Both questions point to the **same structural feature**: the production formula's H₄ Wedderburn count and the per-block Δ_λ binding weights are not derivable as **partition-indexed closed forms**. The categorical content lives at the **brane-tower / level-selection** layer, above what any per-partition statistic can express.

## §6. Outstanding `#1762` 1ppQ roadmap status

| Option | Pre-session status | Post-session status |
|---|---|---|
| A — Vol(β_K) for the light series (diagnostic) | open | **shipped** (#1816, merged) — confirmed the gap; not a derivation |
| B — H₃ brane-tower / Bratteli induction | open | **REFUTED** (#1841) |
| C — Hilbert-space resolution-of-identity in extended H₄ | open (not prioritised) | open (not prioritised; orthogonal to two structural axes above) |
| D — Δ_λ closure via Kashiwara crystal | open | **REFUTED** (#1860; no-fit family closed) |
| E — literature analogy import (Markov stabilization) | open | **REFUTED** (#1850 at the trace level) |

The roadmap is now reduced to **Option C** (Hilbert-space resolution-of-identity, never prioritised) + the **GAP-A-3 / GAP-A-4** research-grade categorical work that this audit identifies as the post-Option-D-and-E productive direction.

## §7. Cross-references

- [`2026-06-04-h3-h4-jump-both-axes-refuted.md`](./2026-06-04-h3-h4-jump-both-axes-refuted.md) — the H₃→H₄ jump consolidation (#1853, merged)
- [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) — the Δ_λ gate doc (audit-doc table this PR extends)
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md) — GAP-A-3 / GAP-A-4 framing
- [`2026-06-04-option-b-h3-h4-bratteli-scoping.md`](./2026-06-04-option-b-h3-h4-bratteli-scoping.md) — Q1 axis 1 scope (#1841)
- [`2026-06-04-markov-stab-trace-axis-scope.md`](./2026-06-04-markov-stab-trace-axis-scope.md) — Q1 axis 2 scope (#1850)
- [`2026-06-04-option-e-kashiwara-crystal-scope.md`](./2026-06-04-option-e-kashiwara-crystal-scope.md) — Q2 axis scope (#1860)
