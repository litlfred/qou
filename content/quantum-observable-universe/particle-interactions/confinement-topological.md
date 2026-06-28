## Statement

**Proposition.**
*Let $G \in \mathbb{R}^{6 \times 6}$ be the Gram matrix of $H_3(q)$
at $q = q_0$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).
Consider the linear program:*

$$
  \min_{x \in \mathbb{R}^6} \;
  \sum_{i=1}^{6} t_i x_i
  \qquad
  \text{s.t.} \quad
  \mathbf{1}^\top x = n_{\mathrm{target}},
  \quad
  Gx \geq 0
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the
NF basis elements.*

**(i)** *The LP has optimal value $\mathrm{tr}_M^* = 0$, achieved
by exploiting the negative eigenvalue $\lambda_{\min}(G) < 0$.*

**(ii)** *The LP optimum $x^*$ has $|x_i^*| \gg 1$ for some
components (specifically $x_{e^-}^* \to +\infty$ without bounds).
It is NOT in the image of the braid group representation
$\rho \colon B_3 \to H_3(q)$.*

**(iii)** *Among all elements $\Phi \in H_3(q)$ that are images
of braid group elements of length $\leq 6$,
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the unique element
with $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - n_{\mathrm{target}}| = 0$
for both proton and neutron typed crossings.*

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
