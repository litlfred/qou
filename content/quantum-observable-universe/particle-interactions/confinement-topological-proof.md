## Proof of (i): the Gram matrix has a negative eigenvalue

The eigenvalues of $G$ are (symbolically in $q$):

$$
  \mathrm{spec}(G)
  =
  \{
    \lambda_+(q),\;
    \lambda_+(q),\;
    \lambda_+(q),\;
    \lambda_{\max}(q),\;
    \lambda_0(q),\;
    \lambda_-(q)
  \}
$$

where $\lambda_-(q) < 0$ for all $q > 1$.  At $q_0$:
$\lambda_- \approx -0.855$.

The LP exploits this: the direction $v_-$ (eigenvector of
$\lambda_-$) satisfies $t \cdot v_- < 0$ while $Gv_- \geq 0$
in certain components.  Moving along $v_-$ decreases the
objective without violating Frobenius positivity.

## Proof of (iii): exhaustive enumeration

Among the $4^6 = 4096$ braid words of length exactly $6$ over
generators $\{\sigma_0, \sigma_1, \sigma_0^{-1}, \sigma_1^{-1}\}$,
and all shorter words:

- $\mathcal{B}_3 = \sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}$
  achieves $|\Delta\mathrm{net}| = 0.000$ for both proton and neutron.
- The mirror $\mathcal{B}_3^{\sigma} = \sigma_0^{-1}\sigma_1\sigma_0^{-1}\sigma_1\sigma_0^{-1}\sigma_1$
  achieves $|\Delta\mathrm{net}| = 0.004$ — an order of magnitude worse.
- All other words have $|\Delta\mathrm{net}| > 0.01$.

**Witness**: `confinement-lp.witness.json`.
