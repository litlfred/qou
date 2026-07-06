# 2026-05-25 — Δ_λ(K) is canonical: probe-2 reframing + Option E next steps

## TL;DR

**Probe-2's negative diagnostic does NOT falsify the framework.** It confirms a property the framework already has: **Δ_λ is knot-operator dependent**, written **Δ_λ(K)** in the canonical formula
([`prop:rho-k-h3a-refinement`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md)).

Probe-2 tested a counter-framework hypothesis (Δ_λ atom-independent across D + T + ³He). The 27× blowup (max |Δ_λ| = 431.7 vs 15.7 for D-only) ruled out the counter-hypothesis. The framework's existing K-dependence stands.

This is a categorisation, not a finding — the per-atom analyses (probes 1, 3) were already operating in the canonical formulation; only probe-2's "global" hypothesis was off-framework.

## ⛔ DO NOT pursue global Δ_λ again (anti-pattern gate)

This audit closes the global-Δ_λ ansatz permanently. Any future probe,
ansatz, audit, or compute that imposes:

- "Δ_λ is the same for D and T and ³He and ⁴He"
- "Δ_λ depends only on the partition λ, not on the atom K"
- "Δ_λ is a universal per-partition function"

**will be rejected on review.** Empirical falsification (probe-2,
max |Δ_λ| = 431.7 ⇒ counter-framework) + categorical mismatch
(canonical formula has Δ_λ(K) since [`rho-k-h3a-refinement.lean`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.lean) L49-66) together close
this design space.

Codified in [`docs/coordination/1ppb-compute-tranche-queue.md`](../coordination/1ppb-compute-tranche-queue.md) §Anti-patterns
item 6.

**The closure problem is**: categorically determine Δ_λ(K) per
atom. Options:

- **Option E** ([PR #1252](https://github.com/litlfred/qou/pull/1252)) — Δ_λ(K) = Σ_w n^w_λ · ρ_w(K) via
  Kazhdan–Lusztig multiplicities × canonical-basis trace at
  crystal vertices.
- **Path B** (per [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)) — Borromean tower extension; bypasses Δ_λ gate by
  re-routing through different categorical machinery.

Both Option E and Path B are K-dependent by construction —
neither is a global ansatz.

## Canonical formula (the framework as-written)

From [`rho-k-h3a-refinement.lean`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.lean) lines 49–66 + [`rho-k-h3a-refinement.md`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md):

$$
  \rho_K(q) = \rho_K^{\mathrm{LO}}(Z, N) + \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|} \sum_{\lambda \vdash 3A} y_\lambda(q)\, \chi^\lambda(\mathcal{B}_K)\, \Delta_\lambda(K)
$$

where $\Delta_\lambda(K) \in \mathbb{R}$ is the **block-binding correction** and the **K subscript is explicit in the existing formalism**. The LO ansatz $\rho_K^{\mathrm{LO}}$ matches CODATA mass to ≤ 0.1% across {p, n, D, T, ³He, ⁴He}; the residual IS the binding energy, distributed across Wedderburn blocks via Δ_λ(K).

## What the three single-session probes told us

| probe | tested | result | within framework? |
|-------|--------|--------|-------------------|
| 1 | min-norm Δ_λ(D) under bar-invariance Δ_λ = Δ_{λ^T} | max |Δ_λ| = 15.7 | ✓ (canonical D-only) |
| 3 | + dominant pin Δ_{(5,1)}(D) = round(dim_q) | max |Δ_λ| = 29.5 | ✓ (tested GAP-A-4 pin form) |
| 2 | "global" Δ_λ across D + T + ³He (no K dep) | max |Δ_λ| = 431.7 | ✗ (counter-framework hypothesis) |

The 1+3 results give VALID information about Δ_λ(D)'s structural constraints. Probe-2 ruled out a non-framework simplification.

## What's left to determine — Δ_λ(K) closure

Per atom K, the framework formula gives **1 equation in p(3A) unknowns** for Δ_λ(K) (p(6)=11 for D, p(9)=30 for T/³He, p(12)=77 for ⁴He of which only 24 have non-zero χ in the current witness). Per atom this is wildly underdetermined.

**Closure requires a structural constraint** on Δ_λ(K). The viable directions:

1. **Per-atom bar-invariance** (probe-1 form) — Δ_λ(K) = Δ_{λ^T}(K). Reduces unknowns by ~½. ✓ canonical (Type-B fold, AGENTS.md §7b).

2. **Per-atom dominant pin from GAP-A-4** — Δ_{λ*}(K) = round(dim_q(λ*)) for the dominant partition. ✗ falsified for D (probe-3).

3. **Crystal-weight assignment (Option E)** — Δ_λ(K) = Σ_w n^w_λ · ρ_w(K) where ρ_w is the canonical-basis trace and n^w_λ are Kazhdan–Lusztig multiplicities. Open conjecture (`conj:crystal-graph-realization`, `conj:kazhdan-lusztig-classical-limit`).

4. **Per-atom polynomial in (Z, N, |β_K|, dim_q(λ))** — fit-style. ✗ excluded per AGENTS.md anti-pattern.

## Probe-4 (this branch) — per-atom Δ_λ(K) sweep

Stacks on PR #1229 alongside probes 1, 2, 3. Runs probe-1's bar-invariance min-norm separately for each of {D, T, ³He, ⁴He}; reports:

- max |Δ_λ(K)| per atom — does it scale with Z, N, A, |tr_M(β_K)|?
- dominant λ*(K) per atom — does it follow a hook / two-row / principal pattern across atoms?
- bar-pair coverage — fraction of partitions with bar-symmetric Δ vs self-conjugate

These are inputs to Option E's crystal-graph weight assignment: the per-atom dominant-λ pattern across {D, T, ³He, ⁴He} provides empirical fingerprints that the categorical theory needs to match.

## Option E (new branch) — Kashiwara crystal scaffolding

Open scope per user direction 2026-05-25. New branch `claude/kashiwara-crystal-option-e-scaffolding-2026-05-25`. First-week deliverables:

1. **Lean scaffolding** for crystal-graph weight assignment at H_6 (deuteron).
   - Build on existing [`lusztig-canonical-basis-q-eq-1.lean`](../../content/quantum-observable-universe/braids-and-knots/lusztig-canonical-basis-q-eq-1.lean), [`kashiwara-jones-c4-categorical.lean`](../../content/quantum-observable-universe/braids-and-knots/kashiwara-jones-c4-categorical.lean).
   - Replace `gram_matrix q = 0` stub in [`universal-ilp-algorithm.lean`](../../content/quantum-observable-universe/particle-interactions/universal-ilp-algorithm.lean) with the computed 6×6 Frobenius matrix from [`gram-matrix-dual.py`](../../computations/gram-matrix-dual.py).
   - First crystal vertices computed for sl₃ level 6 (deuteron weight).

2. **Audit doc**: `docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md` — frames the conjecture Δ_λ(K) = canonical-basis-trace sum precisely; identifies the categorical theorem needed.

3. **Inverse-Gram / dual-basis machinery** (per user direction "E also gram inverse basis/canonical 6 dim basis/dual basis"):
   - Generalise [`gram_matrix(q)` / `gram_inverse(q)` in pyhecke-native](../../tools/pyhecke-native/src/lib.rs) from hardwired n=3 to general n (covers n=6 deuteron, n=9 T/³He, n=12 ⁴He).
   - Coordinate with PR #1228 §10 action #1 (pyhecke/chi_lambda_eval.py) — same wrapper scope.

## Coordination with siblings

- **#1224** (synthesis): already coordinated. Probe-2 reframed as confirming canonical K-dependence, not falsifying framework.
- **#1228** (vol-density-derivation): already coordinated. §10 action #1 (chi_lambda_eval.py wrapper) + Option E's general-n Gram needs converge.
- **#1127** (Q_β fitting): GAP-A-4 reference shared. Probe-3 falsifies one form of `conj:rho-prefactor-structural`; Option E may provide the right form via crystal weights.
- **#1246** (CAL-2 cohomological audit): potentially upstream of substrate q_0 derivation; relevant if Option E's KL classical-limit needs q_0 framing.

## Ledger entry

This audit accompanies the probe-4 commit on PR #1229. Single-session probe sequence (1+2+3) has shipped its full informational payload; probe-4 maps out the per-atom landscape that Option E's categorical theory must reproduce.
