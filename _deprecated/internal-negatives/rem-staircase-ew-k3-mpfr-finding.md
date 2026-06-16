**Remark (mpmath 50-dps spectral analysis of the staircase EW-residual
at $k=3$).** The
[staircase EW-residual conjecture](#conj:staircase-ew-residual) states
that on the staircase Specht module $V_{\rho_k}$, the matrix image of
the canonical $\beta_{\mathrm{EW}}\,\bowtie_K^{\mathrm{minimal}}$
word has two nonzero eigenvalues whose pairwise ratio equals
$q^{1/(2k-1)}$.

For $k = 3$ (the Weinberg-angle case), this prediction was previously
verified at **float64 precision** to $0.13\%$ accuracy via
[`close_321_weinberg_gap.py`](https://github.com/litlfred/qou/blob/main/computations/close_321_weinberg_gap.py).
A natural question was whether the residual $0.13\%$ is float-precision
noise (which would imply the conjecture is a closed-form identity)
or a genuine correction.

[`probe_staircase_ew_k3_categorical.py`](https://github.com/litlfred/qou/blob/main/computations/probe_staircase_ew_k3_categorical.py)
re-does the spectral computation at **mpmath 50 dps**, building the
$16 \times 16$ Hoefsmit $V_{(3,2,1)}$ matrices and the
27-generator word image at that precision, and diagonalising via
`mp.eig`. Findings:

* **Reading A — residual factor**. The ratio
  $\operatorname{cot}\theta_W^{\mathrm{CODATA}} / (e_{\mathrm{top}}/e_{2\mathrm{nd}})$
  equals $1.0226\ldots$ at $q_0$; predicted $q_0^{1/5} = 1.0211\ldots$;
  relative deviation $|\Delta_{\mathrm{rel}}| = 1.50 \times 10^{-3}$
  (= $0.150\%$). **The $0.13\%$ residual is structural, not float
  precision noise.**
* **Reading B — literal conjecture**. Scanning all pairs of
  positive-real eigenvalues for the best match to $q_0^{1/5}$ gives
  the pair $(e_5, e_6)$ with ratio $1.0921$; relative deviation
  $|\Delta_{\mathrm{rel}}| = 6.95 \times 10^{-2}$ (= $6.95\%$).
  **No internal eigenvalue pair on $V_{(3,2,1)}$ has ratio
  exactly $q^{1/5}$.**

The conjecture, read as an exact identity, is therefore **falsified
at 50 dps** in both natural interpretations. The empirical content
stands as an approximate leading-order match good to $\sim 0.15\%$.

Implications for the Lean formalisation
([`StaircaseCornerHook.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/StaircaseCornerHook.lean)):
the `StaircaseEWResidual` class instance's single `sorry` should be
re-interpreted as encoding the conditional approximate match (with a
controlled correction series), not an exact closed-form theorem. See
[`docs/audits/2026-05-17-staircase-ew-k3-mpfr-spectral.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-17-staircase-ew-k3-mpfr-spectral.md)
for the full numerical comparison and recommended refinement of the
conjecture statement.

This is a **negative result**: the categorical route via corner-hook
combinatorics alone does not produce the cot $\theta_W$ value to
better than $\sim 0.15\%$. Future work should look for the
next-order correction term — e.g. an expansion
$q^{1/(2k-1) + \varepsilon(q)}$ with $\varepsilon(q) \to 0$ as
$q \to 1$ — that lifts the approximate match to a structural identity.
