# Per-partition $k_\lambda$ rule — selector investigation + empirical reproduction status

**Date:** 2026-05-11
**Author:** coordination agent on
`claude/q-beta-spectral-bridge-handoff-QqMlK`
**Witness:**
[`computations/probe-phiq-per-partition-n-sweep.witness.json`](../../computations/probe-phiq-per-partition-n-sweep.witness.json)
**Probe:**
[`computations/probe_phiq_per_partition_n_sweep.py`](../../computations/probe_phiq_per_partition_n_sweep.py)
**§:** `/coordinate` skill §6 — investigated discrepancy, **partial
escalation** (selector mislabel + binding-closure overstatement, NOT
empirical-claim refutation).

## TL;DR

PR #639's `per-partition-k-lambda-rule.md` makes **two** empirical
claims about its per-partition $k_\lambda$ rule:

1. **Tower-magnitude claim**: at $k_\lambda = 1$ for the dominant
   partition, $k_\lambda = 2$ otherwise, $\lvert\mathrm{tower}\rvert < 2$
   (vs uniform-$k$ towers in $[5, 11]$).
2. **Binding closure claim**: "closes all three atoms
   simultaneously" within $\sim 5\%$.

Investigation finds:

- **Selector mislabel.** The .md states "max-$\lvert\mu\rvert$"
  selector, but the table's contribution values
  ($-6.220, -3.001, -11.692$) match the *actual* selector
  $\mathrm{argmax}_\lambda \lvert y_\lambda \cdot \sum_a \Phi_q^{[\le 2]}(\mu_a^{(\lambda)}) \rvert$
  (Selector B) **exactly to 4 decimal places**. The stated selector
  (max-$\lvert\mu\rvert$, Selector A) gives **different dominants**
  ($[3, 3]$, $[3, 3, 3]$, $[3, 3, 3]$ for $\{D, T, {}^3\mathrm{He}\}$).

- **Tower-magnitude claim REPRODUCES** under Selector B. At $N = 2$:
  $\lvert\mathrm{tower}\rvert \in \{0.255,\, 1.972,\, 1.066\}$ for
  $\{D, T, {}^3\mathrm{He}\}$ — all $< 2$. ✓

- **Binding closure claim DOES NOT REPRODUCE** under either
  selector at any $N \in \{1, 2, 3, 4, 5\}$. Best result (Selector B,
  $N = 2$): binding errors $\{-11.7\%,\, -44.3\%,\, -49.5\%\}$.
  Worst: $\sim 50\%$, far from the stated $\sim 5\%$.

- **Substrate $c(K)$ ceiling not realised**: the binding-formula
  residual exceeds the geometric ceiling by $\sim 10^5$ at $N = 2$,
  and the gap **grows** with $N$. The ceiling governs the
  *truncation remainder* $\lvert R_N \rvert$, not the binding-formula
  residual which folds in $\sigma_{3A}$ and the $\rho$ pre-factor.

## §6 escalation summary (for PR #639)

The empirical infrastructure in PR #639 is structurally correct —
the dominants ARE the max-contribution partitions, and tower
magnitudes DO collapse under the per-partition rule. **The two
issues are local**:

1. **Selector statement in `per-partition-k-lambda-rule.md`** says
   "max-$\lvert\mu\rvert$" but should say
   "$\mathrm{argmax}_\lambda \lvert y_\lambda \cdot \sum_a \Phi_q^{[\le 2]}(\mu_a^{(\lambda)}) \rvert$"
   (signed Wedderburn contribution magnitude at $k = 2$).

2. **Binding closure language** says "closes all three atoms to
   $\sim 5\%$" — this overstates the empirical reach. The
   tower-magnitude collapse is real (the tower drops from $[5, 11]$
   to $< 2$), but the binding-formula residual remains at $\sim 50\%$
   worst-case because $\sigma_{3A}$ and the $\rho$ pre-factor
   dominate.

The **structural claim** (per-partition rule sharpens the open form
of $n_\star$) stands. The witness file
`probe-phiq-per-partition-klambda.witness.json` referenced in
PR #639's .md but absent from PR #639's diff should be committed to
PR #639 (or my probe's witness from this branch adopted as the
canonical record).

## Findings — verbatim from the witness

### Dominant partitions: Selector A vs Selector B

Both selectors run on the same eigenvalue / character data from PR
#638's `probe_phiq_operator_valued.py` infrastructure, with
`atom_braid_word_3A(Z, N, include_inter=True)`.

| Atom | Selector A (max-$\lvert\mu\rvert$) | Selector B (max-$\lvert y \cdot \mathrm{contrib}_{k=2} \rvert$) |
|---|---|---|
| $D$ | $[3, 3]$, $\max\lvert\mu\rvert = 4.688$ | $[2, 2, 1, 1]$, $\lvert\mathrm{contrib}\rvert = 6.220$ |
| $T$ | $[3, 3, 3]$, $\max\lvert\mu\rvert = 8.771$ | $[6, 3]$, $\lvert\mathrm{contrib}\rvert = 3.001$ |
| ${}^3\mathrm{He}$ | $[3, 3, 3]$, $\max\lvert\mu\rvert = 11.115$ | $[5, 4]$, $\lvert\mathrm{contrib}\rvert = 11.692$ |

PR #639's table values: $D \to -6.220$, $T \to -3.001$,
${}^3\mathrm{He} \to -11.692$. **Selector B reproduces these to 4
decimal places**, confirming PR #639 actually used Selector B
internally even though the .md text states Selector A.

### Sweep results (Selector B — actual rule)

| $N$ | atom | $\lvert\mathrm{tower}\rvert$ | $B^{(N)}$ MeV | AME MeV | err% |
|---:|---|---:|---:|---:|---:|
| 1 | $D$ | 0.464 | 2.072 | 2.225 | $-6.87$ |
| 1 | $T$ | 0.277 | 2.990 | 8.482 | $-64.75$ |
| 1 | ${}^3\mathrm{He}$ | 0.575 | 3.399 | 7.718 | $-55.97$ |
| **2** | **$D$** | **0.255** | **1.965** | **2.225** | **$-11.67$** |
| **2** | **$T$** | **1.972** | **4.722** | **8.482** | **$-44.33$** |
| **2** | **${}^3\mathrm{He}$** | **1.066** | **3.900** | **7.718** | **$-49.47$** |
| 3 | $D$ | 6.031 | 4.916 | 2.225 | $+121.00$ |
| 3 | $T$ | 22.170 | 25.364 | 8.482 | $+199.04$ |
| 3 | ${}^3\mathrm{He}$ | 4.425 | 7.333 | 7.718 | $\mathbf{-4.99}$ |
| 4 | $D$ | 136.198 | 71.432 | 2.225 | $+3111.05$ |
| 4 | $T$ | 20.197 | 23.347 | 8.482 | $+175.26$ |
| 4 | ${}^3\mathrm{He}$ | 12.500 | 15.586 | 7.718 | $+101.95$ |

**At $N = 2$ (PR #639's stated rule)**: tower magnitudes
$\{0.255,\, 1.972,\, 1.066\}$ all $< 2$. ✓ This is PR #639's
tower-magnitude claim, reproduced.

**Binding errors at $N = 2$**: $\{-11.7\%,\, -44.3\%,\, -49.5\%\}$.
Worst error 49.5% — **not** within 5%.

Interesting at $N = 3$: ${}^3\mathrm{He}$ binding error drops to
$-4.99\%$, but $D$ and $T$ blow up to $+121\%$ and $+199\%$. **No
single $N$ closes all three within 5%** under Selector B.

### Headroom vs $c(K)$ ceiling (Selector B)

| $N$ | ceiling (ppb) | mean observed (ppb) | mean headroom |
|---:|---:|---:|---:|
| 1 | $9.73 \times 10^{4}$ | $4.30 \times 10^{8}$ | $4.4 \times 10^{3}$ |
| 2 | $9.56 \times 10^{2}$ | $3.51 \times 10^{8}$ | $3.7 \times 10^{5}$ |
| 3 | $9.38$ | $1.08 \times 10^{9}$ | $1.2 \times 10^{8}$ |
| 4 | $0.092$ | $1.13 \times 10^{10}$ | $1.2 \times 10^{11}$ |
| 5 | $9.0 \times 10^{-4}$ | $1.77 \times 10^{11}$ | $2.0 \times 10^{14}$ |

The binding-formula residual exceeds the $c(K)$ ceiling by 3-14
orders of magnitude across the $N$ sweep — **the ceiling does NOT
govern the binding-formula residual** under the per-partition rule.
This is consistent with the structural framing in PR #639's audit:
the ceiling bounds the *truncation remainder* $\lvert R_N \rvert$
in the brane-tower expansion, but the binding formula
$B = m_e \cdot \rho \cdot (\lvert\mathrm{tr}_M\rvert + \mathrm{tower} + \sigma_{3A})$
includes $\sigma_{3A}$ (Wedderburn jet correction) and the $\rho$
pre-factor (atomic gauge) which contribute to the empirical
residual independently of the tower truncation depth.

A direct probe of $\lvert R_N \rvert$ (subtracting $\mathrm{tr}_M$ and
$\sigma_{3A}$) would be needed to test the $c(K)$ ceiling
operationally — flagged as a follow-up.

## Recommended actions

For **PR #639** (one comment, not a stream):

1. **Amend the selector statement** in
   `per-partition-k-lambda-rule.md` to read

   > $k_\lambda = 1$ if $\lambda = \mathrm{argmax}_{\lambda'}
   > \lvert y_{\lambda'} \cdot \sum_a \Phi_q^{[\le 2]}(\mu_a^{(\lambda')})\rvert$,
   > $k_\lambda = 2$ otherwise.

   (Not "max-$\lvert\mu\rvert$" — that selector gives different
   dominants and does not close.)

2. **Tighten the binding closure language**. The "closes all three
   atoms simultaneously to ~5%" claim overstates the empirical
   reach. Suggested replacement:

   > The per-partition rule collapses the tower magnitude from
   > $[5, 11]$ (uniform $k$) to $[0.25, 2]$. The binding-formula
   > residual remains at $\sim 50\%$ worst-case because the
   > $\sigma_{3A}$ and $\rho$ pre-factor contribute independently
   > of the tower; resolving the binding closure requires a
   > separate refinement of $\sigma_{3A}$ and/or $\rho$.

3. **Commit the witness**
   `probe-phiq-per-partition-klambda.witness.json` cited in the
   .md but absent from the diff. Or adopt my probe's witness
   (`probe-phiq-per-partition-n-sweep.witness.json` on this branch)
   as the canonical record.

For **this branch**:

- Audit committed (this file).
- Probe + witness committed.
- Coordination comment posted on PR #639 with the §6 finding
  (next step).

For **future probes**:

- The next compute task in the cross-PR synthesis (path-to-1ppb)
  should be a **direct probe of $\lvert R_N \rvert$** (subtracting
  $\mathrm{tr}_M$ and $\sigma_{3A}$) to test the $c(K)$ ceiling
  operationally. The binding-formula residual under the
  per-partition rule does not test the ceiling directly.

## Files

| Path | Content |
|---|---|
| `computations/probe_phiq_per_partition_n_sweep.py` | Joint probe (#638 infra + #639 rule, both selectors A and B) |
| `computations/probe-phiq-per-partition-n-sweep.witness.json` | Per-atom eigenvalue spectra + per-selector sweep results |
| `docs/audits/2026-05-11-per-partition-k-lambda-selector-investigation.md` | This audit |
