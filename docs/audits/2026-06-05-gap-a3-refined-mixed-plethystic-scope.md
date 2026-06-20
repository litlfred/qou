# GAP-A-3 refined — mixed plethystic content channel for P_λ(K)

**Date:** 2026-06-05
**Branch:** `claude/gap-a3-a4-mass-formalize-first-2026-06-05`
**Status:** scoping doc. No probe in this PR.
**Builds on:** [GAP-A-3 brane-tower level-selection scope (PR #1868)](2026-06-04-gap-a3-brane-tower-level-selection-scope.md), [GAP-A-3 deuteron P_λ probe — 5 channels refuted (PR #1870)](https://github.com/litlfred/qou/pull/1870), Q_β §4 formalize-first chain (PRs #1875, #1889, #1890, #1893).

## §1. Why a refined candidate now

PR #1870's deuteron probe refuted **all five** simple brane-tower content channels for `P_λ(D)`:

- C1 sl_2 Schur–Weyl (V_{1/2}^⊗6 ≤2-row)
- C2 sl_3 Schur–Weyl (V_1^⊗? ≤3-row)
- C3 sl_2 q-dim
- C4 sl_2 indicator (≤2-row baseline)
- C5 constant-zero control

The audit's predicted §5 outcome — *"if all channels refute, the pivot to GAP-A-4 is justified"* — was followed, and PRs #1882 / `eb07055c34` / `dade49f99c` ran the GAP-A-4 Path B candidates (L1 / L2 / L3) — also refuted, with the sub-leading sqrt([3]_q/[2]_q) flagged as numerology pending derivation (PR #1882).

This leaves the question: **is there a refined per-partition content channel NOT yet tested, that respects the categorical-derivation discipline?**

## §2. The structural pivot — mixed plethystic content

The Phase-4 amplitude carries TWO multiplicative content factors:

```
A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · ([2]_q)^{4N}
```

- `[3]_q^{2(Z-1)}` — color channel (adjoint V_1), exponent `2(Z-1)`
- `([2]_q)^{4N}` — spin channel (fundamental V_{1/2}), exponent `4N`

PR #1870's tests treated these as **separate channels** for `P_λ`. The refined candidate is the **product**: for each partition `λ ⊢ 3A`,

$$
P_\lambda^{\text{mixed}}(K) \;=\; m_{1/2}(\lambda)^{4N} \cdot m_1(\lambda)^{2(Z-1)}
$$

where `m_{1/2}(λ)` is the V_{1/2}-content multiplicity (Schur-Weyl for V_{1/2}^⊗n, SU(2)). **Convention note (per Gemini review on PR #1896):** `V_1` here denotes the **sl_3 fundamental representation** (3-dimensional) when written as `(dim_q V_1)^{2(Z-1)}` in the Phase-4 carrier; the Schur-Weyl decomposition of `V_1^⊗n` selects ≤3-row partitions and `m_1(λ)` is the corresponding sl_3 multiplicity. The earlier description "adjoint V_1" in §2's reading of `[3]_q^{2(Z-1)}` refers to the QUANTUM-DIM identity `[3]_q = dim_q(V_1^{sl_3 fund}) = dim_q(V_1^{SU(2) adj})` (both 3-dimensional reps share the quantum-dim numerical value `[3]_q`); the partition-level multiplicity computation uses the sl_3 fundamental's Schur-Weyl decomposition. The exponents `(4N, 2(Z-1))` are NOT fitted — they are read directly off the Phase-4 carrier exponents.

**Categorical interpretation:** the per-atom amplitude `A(K)` carries the brane-tower content via the product `(dim_q V_{1/2}^{SU(2) fund})^{4N} · (dim_q V_1^{sl_3 fund})^{2(Z-1)}`; the per-partition projection should carry the SAME product of multiplicities at the irrep-content level.

## §3. Why this is NOT yet refuted

For the deuteron `A=2, Z=1, N=1`:

$$
P_\lambda^{\text{mixed}}(D) \;=\; m_{1/2}(\lambda)^{4} \cdot m_1(\lambda)^{0} \;=\; m_{1/2}(\lambda)^4
$$

which is the C1 channel **raised to the 4th power** — a NEW projection NOT in the 5 already-tested. For ⁴He `A=4, Z=2, N=2`:

$$
P_\lambda^{\text{mixed}}({^4\text{He}}) \;=\; m_{1/2}(\lambda)^{8} \cdot m_1(\lambda)^{2}
$$

a different per-partition distribution from any tested in PR #1870.

The candidate is **zero-parameter, closed-form, and categorically motivated** — it falls out of the Phase-4 carrier exponents, no fitting.

## §4. Why this PR scopes but does not probe

The probe requires:

1. **`m_{1/2}(λ)` for partitions of `n = 3A`** — Schur-Weyl multiplicity of V_{1/2} in V_{1/2}^⊗n. For SU(2), only ≤2-row partitions contribute; this is the same closure as PR #1870 C1 (Specht dim `f^λ` for ≤2-row, 0 otherwise).
2. **`m_1(λ)` for partitions of `n = 3A`** — Schur-Weyl multiplicity of V_1 in V_1^⊗(2(Z-1)) (for the proton, Z-1 = 0 ⇒ trivial channel). For larger atoms (Z ≥ 2), this is sl_3 Schur-Weyl, requiring ≤3-row partition contributions.
3. **χ^λ(β_K) for higher-A atoms** — currently the cached witnesses cover only the deuteron (n=6, see [`chi-deuteron-h6-at-q0-50dps.witness.json`](../../computations/chi-deuteron-h6-at-q0-50dps.witness.json)). Probes for ⁴He (n=12) would need new Hecke character extractions.

For the deuteron specifically (Z=1 ⇒ m_1 channel trivial), the mixed candidate collapses to `f^λ^4 · 1` = `f^λ^4` (restricted ≤2-row), which is the PR #1870 C1 channel **raised to the 4th power**. The deuteron test of the mixed candidate is therefore a one-line modification of the existing C1 probe — but only the deuteron alone does not test the genuine MIXED case (which requires Z ≥ 2).

## §5. Forward direction (not in this PR)

A future probe (out of scope here; deferred to the GAP-A-3 / GAP-A-4 sibling track) would:

1. **Deuteron test (cheap):** modify PR #1870's C1 channel to `f^λ^4` and re-run the closure. If lands within 5%, the "mixed" framing is supported even at Z=1.
2. **⁴He test (research-grade):** extract χ^λ(β_{⁴He}) for partitions of 12, compute `f^λ^8 · m_1(λ)^2`, evaluate the closure target. This is the genuine mixed-channel test; requires new Hecke character compute.

## §6. Discipline

- **EXPLORATORY scope only** — this PR does not run the probe.
- **Formalize-first** — the mixed candidate is identified BEFORE running, per AGENTS.md §"Formalize-first probe discipline". The exponents `(4N, 2(Z-1))` are derived from the Phase-4 carrier, not fitted.
- **Not a 7th fit ansatz** — the per-partition projection is a categorical content count product, not a free statistic of λ.
- **Owner-gated for the ⁴He test** — the Hecke character extraction at n=12 is research-grade infrastructure work. The deuteron-only one-line modification is foreground-discharable but is a SUB-case of the genuine mixed candidate.

## §7. Cross-references

- [GAP-A-3 brane-tower level-selection scope (PR #1868)](2026-06-04-gap-a3-brane-tower-level-selection-scope.md)
- [GAP-A-3 deuteron P_λ probe — 5 channels refuted (PR #1870)](https://github.com/litlfred/qou/pull/1870)
- [Δ_λ Phase-4 amplitude](2026-05-19-delta-lambda-phase4-z4N-closure.md)
- [Mass-theory formalize-first invariants scope](2026-06-05-mass-theory-formalize-first-gates-scope.md) — sibling Track 3 deliverable in this PR
- [Refuted-class map §C8](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) — algebra-tower box-adding refuted; mixed-plethystic is a DIFFERENT proposal NOT in that row
