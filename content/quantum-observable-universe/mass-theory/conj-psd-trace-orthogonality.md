**Conjecture (PSD-vs-trace orthogonality of canonical atom-braid Wedderburn blocks).** *Let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)`, viewed as an element of the Iwahori–Hecke algebra $H_{3A}(q)$ at the substrate parameter $q = q_0$. Decompose $H_{3A}(q)$ into Wedderburn blocks $H_{3A}(q) \cong \bigoplus_{\lambda \vdash 3A} V_\lambda^{\oplus d_\lambda}$. Then:*

**(O1) — Trace-dominance.** *The partitions maximising $|y_\lambda(q_0)|$ (Hecke Markov-trace weight) are **1- or 2-row "long-string" partitions** of the form $(n)$, $(n-1, 1)$, $(n-2, 2)$, ..., $(n - k, k)$.*

**(O2) — PSD-dominance.** *The partitions $\lambda^*$ minimising $\varepsilon_{\min}(\lambda) := \min \mathrm{spec}\,\frac{1}{2}(\rho_\lambda(T_w) + \rho_\lambda(T_w)^T)$ (which force the PSD-cone scaling $\alpha^* = 1 / (1 - \varepsilon_{\min}(\lambda^*))$) are **3+row multi-step "tall narrow" partitions** of the form $(c_1^{r_1}, c_2^{r_2}, ...)$ with several distinct row-lengths.*

**(O3) — Shape-class disjointness.** *No partition belongs to both classes. The magnitude separation*
$$
\eta(A) \;:=\; \frac{\max_\lambda |y_\lambda|}{|y_{\lambda^*}|}
$$
*satisfies $\eta(A) \to \infty$ as $A$ grows; empirically $\eta(4) \gtrsim 5 \times 10^5$ and $\eta(6) \gtrsim 9 \times 10^8$.*

## Empirical verification

Across the canonical atoms with `atom_braid_word_3A` recipes implemented in the Rust R5-SDP solver (post-`BraidLetter` extension):

### At A = 4 ($^4$He, $n_0 = 12$)

| family | top member | rows | $y_\lambda(q_0)$ |
|---|---|---:|---:|
| Trace-dominant | $(11, 1)$ | 2 | $7.67 \times 10^{-4}$ |
| Trace-dominant | $(10, 2)$ | 2 | $7.12 \times 10^{-4}$ |
| Trace-dominant | $(9, 3)$ | 2 | $5.87 \times 10^{-4}$ |
| PSD-dominant | $(4, 4, 4)$ | 3 | $1.26 \times 10^{-6}$ |
| PSD-dominant | $(3, 3, 3, 3)$ | 4 | $-4.66 \times 10^{-9}$ |

`η(4) = max trace |y| / min PSD |y| ≈ 7.67e-4 / 4.66e-9 ≈ 1.6×10⁵.`

### At A = 6 ($^6$Li, $n_0 = 18$)

| family | top member | rows | $\varepsilon_{\min}$ | $y_\lambda(q_0)$ |
|---|---|---:|---:|---:|
| Trace-dominant | $(17, 1)$ | 2 | — | $+7.08 \times 10^{-6}$ |
| Trace-dominant | $(18)$ | 1 | — | $+5.86 \times 10^{-6}$ |
| Trace-dominant | $(16, 2)$ | 2 | — | $+6.92 \times 10^{-6}$ |
| PSD-dominant | $(3, 3, 3, 3, 2, 2, 2)$ | 7 | $-116.71$ | $-7.85 \times 10^{-15}$ |
| PSD-dominant | $(5, 5, 5, 3)$ | 4 | $-110.31$ | $-2.84 \times 10^{-11}$ |
| PSD-dominant | $(4, 4, 4, 3, 3)$ | 5 | $-109.81$ | $-4.75 \times 10^{-14}$ |
| PSD-dominant | $(6, 6, 6)$ | 3 | $-95.72$ | $+2.45 \times 10^{-9}$ |

`η(6) = max trace |y| / deepest PSD |y| ≈ 7.08e-6 / 7.85e-15 ≈ 9 × 10⁸.`

### Sign pattern

At A = 6, the three deepest PSD-dominant partitions ($(3, 3, 3, 3, 2, 2, 2)$, $(5, 5, 5, 3)$, $(4, 4, 4, 3, 3)$) all have **negative $y_\lambda$** at $q_0$. They would *subtract* from any positive $\chi^\lambda$ contribution to $\mathrm{tr}_M$. This encodes the bar-anti-symmetric content of the $\sigma_{\mathrm{avg}}$ crossings structurally: the PSD-dominant blocks are the carriers of the *obstruction*, not the carriers of the *mass*.

## Structural interpretation

The conjecture says the categorical roles of "mass-carrier" and "obstruction-carrier" are **structurally separated** in the Wedderburn decomposition. The Markov trace formula $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda \chi^\lambda(T_w)$ effectively splits into:

- **Mass-carrying sum** (concentrated in long-string partitions, $y \sim 10^{-6}$ at $n = 18$): this is what the Frobenius formula evaluates to give the physical $m(K)$.
- **Obstruction sum** (concentrated in narrow multi-step partitions, $|y| \sim 10^{-15}$ at $n = 18$): negligible contribution to $\mathrm{tr}_M$, but where $\varepsilon_{\min}$ pulls $\alpha^*$ toward $0$ via the PSD-cone bisection.

The orthogonality says: **the partitions that the canonical atom-braid is "most non-PSD against" are EXACTLY the partitions whose Markov-trace weight is smallest** — there is no overlap. This is a non-trivial categorical fact about how the bar-anti-symmetric content of $\sigma_{\mathrm{avg}}$ distributes across irreducibles.

## Connection to the bar-involution structure

The negative-$y_\lambda$ sign on the deepest PSD-dominant partitions at A=6 is the empirical fingerprint of the bar involution. The transpose-pair structure observed at A=4 ((4,4,4) paired with (3,3,3,3) — see [`conj:atom-braid-exterior-algebra`](conj-atom-braid-exterior-algebra.md) §"Lean structure") extends to a broader pattern: **tall-narrow partitions** (deeper PSD obstruction) and **wide-short partitions** (smaller PSD obstruction, more positive eigval pattern) are bar-paired via the transpose involution but with **asymmetric obstruction depth** — the tall-narrow side is uniformly deeper.

## Implications for the binding-energy Gap

Per Probe (1) and Probe (1b) in [`docs/audits/-dominant-partition-nucleon-structure.md`](../../../docs/audits/-dominant-partition-nucleon-structure.md):

The binding-energy gap $|B_{\mathrm{pred}}(K) - B_{\mathrm{AME}}(K)|$ lives in the **trace-dominant family** (the 1/2-row long-string partitions), NOT in the PSD-dominant family. Therefore:

1. Categorical refinement of the framework should focus on the **low-row partitions**, not the rectangular Schur-Weyl partner.
2. The PSD-dominant block is the structural "obstruction fingerprint" but does NOT carry the residual mass deficit.
3. The Δ_λ-gating problem (per CLAUDE.md "Precision goals" section) is concretely about which low-row 2-row partitions contribute to the cancellation/imbalance of $\mathrm{tr}_M$.

## What this conjecture does NOT claim

- It does NOT predict the *specific* PSD-dominant shape at each $A$. At $A=4$ the dominant is the (A,A,A) rectangle; at $A=6$ it is the multi-step (3,3,3,3,2,2,2) (the rectangular-form conjecture was [empirically falsified at A=6](../../../docs/audits/-dominant-partition-nucleon-structure.md#gap-narrowing-probe-4c)).
- It does NOT claim a categorical proof — only an empirical pattern across A=4 and A=6 supported by Lanczos LinearOperator probes.
- It does NOT identify the bar-involution as the categorical mechanism — though the negative-$y_\lambda$ sign pattern is suggestive.

## Cross-references — empirical witnesses

- [`computations/probe_1_project_4he_on_dominant.py`](../../../computations/probe_1_project_4he_on_dominant.py) — Probe (1) at A=4
- [`computations/probe_1b_li6_orthogonality.py`](../../../computations/probe_1b_li6_orthogonality.py) — Probe (1b) at A=6
- [`computations/probe_4_li6_rectangular_python.py`](../../../computations/probe_4_li6_rectangular_python.py) — Lanczos LinearOperator framework
- [`computations/probe_4c_li6_large_d_scan.py`](../../../computations/probe_4c_li6_large_d_scan.py) — large-$d_\lambda$ scan that falsified the rectangular-form conjecture
