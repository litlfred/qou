**Lemma.**
*For every $k \geq 1$, the **corner hook** of the
[staircase partition](#def:staircase-partition) $\rho_k$ at cell
$(0, 0)$ satisfies*

$$
  h_{\mathrm{corner}}(\rho_k)
  \;:=\; \mathrm{arm}(0,0) + \mathrm{leg}(0,0) + 1
  \;=\; (k - 1) + (k - 1) + 1
  \;=\; 2k - 1.
$$

**Proof.**
*The corner cell $(0, 0)$ has arm length $k - 1$ (the row $0$ of
$\rho_k$ has $k$ cells, so $k - 1$ cells lie strictly to the right
of the corner) and leg length $k - 1$ (the column $0$ has $k$
cells, so $k - 1$ cells lie strictly below the corner).
Adding the corner cell itself gives
$h_{\mathrm{corner}}(\rho_k) = (k-1) + (k-1) + 1 = 2k - 1$. $\square$*

This combinatorial identity is the **arithmetic anchor** for the
[staircase EW-residual conjecture](#conj:staircase-ew-residual):
the empirically observed pairwise eigenvalue ratio
$q^{1/h_{\mathrm{corner}}(\rho_k)}$ in the spectrum of
$\beta_{\mathrm{EW}} \, \bowtie_K^{\mathrm{minimal}}$ on
$V_{\rho_k}$ uses *exactly* this corner hook as the inverse
exponent.  For $k = 3$ this gives the $q^{1/5}$ residual factor
that closes the cot $\theta_W$ gap from $2.19\%$ to
$0.13\%$ ([`computations/close_321_weinberg_gap.py`](https://github.com/litlfred/qou/blob/main/computations/close_321_weinberg_gap.py));
for $k = 4$ it predicts the $q^{1/7}$ residual scale empirically
verified at relative error $0.14\%$ in the dim-$768$ spectrum
([`staircase_ew_residual_conjecture.py`](https://github.com/litlfred/qou/blob/main/computations/staircase_ew_residual_conjecture.py)).

The Lean proof
(`QOU.StaircaseCornerHook.staircase_corner_hook_eq_two_k_sub_one`)
is fully discharged by `omega` after unfolding the definition; it
contains **no `sorry`** and is independent of any conjectural
spectral data.
