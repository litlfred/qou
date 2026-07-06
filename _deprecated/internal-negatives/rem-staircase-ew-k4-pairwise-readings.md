**Remark (coincidence-by-chance analysis falsifies the literal
staircase EW-residual at $k=4$).** Companion to
[the $k=3$ 50-dps finding](#rem:staircase-ew-k3-mpfr-finding)
(PR #680), this remark extends the negative result to $k=4$
($V_{(4,3,2,1)}$, $\dim = 768$).

The existing
[`staircase_ew_residual_conjecture.py`](https://github.com/litlfred/qou/blob/main/computations/staircase_ew_residual_conjecture.py)
cites a $0.14\%$ pairwise match at $k=4$ as evidence for the literal
conjecture.
[`probe_staircase_ew_k4_pairwise_readings.py`](https://github.com/litlfred/qou/blob/main/computations/probe_staircase_ew_k4_pairwise_readings.py)
adds a **coincidence-by-chance** test: among $\sim 147\,072$ ordered
pairs of positive-real eigenvalues (eigenvalue magnitudes spanning
$[0.018,\ 56]$), the expected best ratio match by *random search* is

$$
  \mathbb{E}\bigl[\,\min_{(i,j)} |r_{ij} - q^{1/7}|\bigr] \;\approx\;
  \frac{\max|\lambda_i|}{N_{\mathrm{pairs}}}
  \;\approx\;
  \frac{56.0}{147\,072}
  \;\approx\;
  3.8 \times 10^{-4}.
$$

The actual best pair $(e_{236}, e_{188})$ gives
$|r - q_0^{1/7}|/q_0^{1/7} = 1.42 \times 10^{-3}$ —
**3.73 $\times$ *worse* than the random-coincidence floor.** If the
conjecture were structural, the empirical match should be
*tighter* than the random floor by several orders of magnitude;
instead it is 3.7 $\times$ *looser*.

**The $0.14\%$ match is essentially noise** — not evidence of a
structural $q^{1/7}$ identity in the $V_{(4,3,2,1)}$ spectrum.

Combined with the $k=3$ finding (literal pairwise reading off by
$6.95\%$ at 50 dps), the literal content of
[`conj:staircase-ew-residual`](#conj:staircase-ew-residual) is
**falsified at every testable $k$**:

| $k$ | dim | testability | literal-pairwise $|\Delta_{\mathrm{rel}}|$ | status |
| --- | --- | --- | --- | --- |
| $2$ | $2$ | untestable | n/a (length-0 word at $n=3$) | — |
| $3$ | $16$ | 50 dps (mpmath) | $6.95\,\%$ | falsified |
| $4$ | $768$ | float64 (probe-only; NOT 1-ppb cross-method verified) + coincidence test | $0.14\,\%$ (3.7$\times$ worse than random) | falsified |

The empirical content that *survives* is the **leading-order match**
via the CODATA-residual reading (only directly testable at $k=3$,
where cot $\theta_W^{\mathrm{CODATA}} / (e_{\mathrm{top}}/e_{2\mathrm{nd}}) \approx q^{1/5}$
to $0.15\%$). Future work should look for the next-order correction
series.

**Bar-pair structure verified.** All 768 eigenvalues form 384 perfect
$e_+ \cdot e_- = -1$ bar-pairs at float64 precision (probe; bar-pair
property is algebraic and independent of dps) — confirms the
conjugate-pairing analysis from
[`prop:beta-ew-bar-pair-recursion`](#prop:beta-ew-bar-pair-recursion)
independently of the $q^{1/(2k-1)}$ claim.

**Precision-upgrade caveat.** Direct 50-dps verification of $k=4$ at
$\dim = 768$ is infeasible in a single session (~14 hours just for
the matrix product). But the coincidence-by-chance analysis gives
the same conclusion without needing high precision — at this
spectrum size, the random-coincidence floor is already comparable
to the empirical match. See
[`docs/audits/2026-05-17-staircase-ew-k4-pairwise-readings.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-17-staircase-ew-k4-pairwise-readings.md)
for the sparse-aware mpmath / Schur-Weyl block-decomposition
infrastructure that would be needed for a direct high-precision
verification.
